import math
import random
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset


DATA_PATH = (
    Path(__file__).resolve().parent.parent / "datos" / "mini_estilo_quijote.txt"
)
MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "modelos"
    / "transformers_2_generacion_decoder_only.pt"
)

PAD_TOKEN = "<pad>"
SOS_TOKEN = "<sos>"
EOS_TOKEN = "<eos>"
SPECIAL_TOKENS = [PAD_TOKEN, SOS_TOKEN, EOS_TOKEN]


def load_text(path):
    return path.read_text(encoding="utf-8").lower()


def build_char_vocab(text):
    vocab = {token: idx for idx, token in enumerate(SPECIAL_TOKENS)}
    for ch in sorted(set(text)):
        if ch not in vocab:
            vocab[ch] = len(vocab)
    return vocab


def encode_text(text, vocab):
    return [vocab[ch] for ch in text]


class CharDataset(Dataset):
    def __init__(self, text_ids, block_size, sos_id, eos_id):
        self.samples = []
        for i in range(len(text_ids) - block_size):
            chunk = text_ids[i : i + block_size]
            target = text_ids[i + 1 : i + block_size + 1]
            x = [sos_id] + chunk[:-1]
            y = target[:-1] + [eos_id]
            self.samples.append((x, y))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        x, y = self.samples[idx]
        return torch.tensor(x, dtype=torch.long), torch.tensor(y, dtype=torch.long)


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def split_heads(self, x):
        batch_size, seq_len, _ = x.size()
        return x.view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)

    def combine_heads(self, x):
        batch_size, _, seq_len, _ = x.size()
        return x.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)

    def scaled_dot_product_attention(self, q, k, v, mask=None):
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        probs = torch.softmax(scores, dim=-1)
        return torch.matmul(probs, v)

    def forward(self, q, k, v, mask=None):
        q = self.split_heads(self.W_q(q))
        k = self.split_heads(self.W_k(k))
        v = self.split_heads(self.W_v(v))
        attended = self.scaled_dot_product_attention(q, k, v, mask)
        return self.W_o(self.combine_heads(attended))


class PositionWiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Linear(d_ff, d_model),
        )

    def forward(self, x):
        return self.net(x)


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_length):
        super().__init__()
        pe = torch.zeros(max_seq_length, d_model)
        position = torch.arange(0, max_seq_length, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe.unsqueeze(0))

    def forward(self, x):
        return x + self.pe[:, : x.size(1)]


class DecoderOnlyLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        x = self.norm1(x + self.dropout(self.self_attn(x, x, x, mask)))
        ff_output = self.feed_forward(x)
        return self.norm2(x + self.dropout(ff_output))


class DecoderOnlyTransformer(nn.Module):
    def __init__(
        self,
        vocab_size,
        d_model=64,
        num_heads=4,
        num_layers=2,
        d_ff=128,
        max_seq_length=120,
        dropout=0.1,
    ):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.positional_encoding = PositionalEncoding(d_model, max_seq_length)
        self.layers = nn.ModuleList(
            [DecoderOnlyLayer(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)]
        )
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(d_model, vocab_size)

    def generate_causal_mask(self, x):
        seq_len = x.size(1)
        pad_mask = (x != 0).unsqueeze(1).unsqueeze(2)
        causal_mask = (
            1 - torch.triu(torch.ones(1, seq_len, seq_len), diagonal=1)
        ).bool().to(x.device)
        return pad_mask & causal_mask

    def forward(self, x):
        mask = self.generate_causal_mask(x)
        x = self.dropout(self.positional_encoding(self.embedding(x)))
        for layer in self.layers:
            x = layer(x, mask)
        return self.fc(x)


def train_model(model, dataloader, optimizer, criterion, device, epochs=200):
    model.train()
    for epoch in range(1, epochs + 1):
        total_loss = 0.0
        for x, y in dataloader:
            x = x.to(device)
            y = y.to(device)
            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits.view(-1, logits.size(-1)), y.view(-1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if epoch % 20 == 0 or epoch == 1:
            print(f"Epoch {epoch:03d} | loss = {total_loss / len(dataloader):.4f}")


def sample_next_token(logits, temperature=0.9):
    logits = logits / max(temperature, 1e-6)
    probs = torch.softmax(logits, dim=-1)
    return torch.multinomial(probs, num_samples=1).item()


def generate_text(model, prompt, vocab, inv_vocab, device, max_new_tokens=180, temperature=0.9):
    model.eval()
    generated = [vocab[SOS_TOKEN]] + [vocab[ch] for ch in prompt.lower() if ch in vocab]
    with torch.no_grad():
        for _ in range(max_new_tokens):
            x = torch.tensor([generated], dtype=torch.long, device=device)
            logits = model(x)
            next_id = sample_next_token(logits[0, -1], temperature=temperature)
            if next_id == vocab[EOS_TOKEN]:
                break
            generated.append(next_id)
    chars = [
        inv_vocab[idx]
        for idx in generated[1:]
        if idx not in (vocab[PAD_TOKEN], vocab[EOS_TOKEN])
    ]
    return "".join(chars)


def main():
    random.seed(42)
    torch.manual_seed(42)

    text = load_text(DATA_PATH)
    vocab = build_char_vocab(text)
    inv_vocab = {idx: token for token, idx in vocab.items()}
    text_ids = encode_text(text, vocab)

    block_size = 80
    dataset = CharDataset(text_ids, block_size, vocab[SOS_TOKEN], vocab[EOS_TOKEN])
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = DecoderOnlyTransformer(
        vocab_size=len(vocab),
        d_model=64,
        num_heads=4,
        num_layers=2,
        d_ff=128,
        max_seq_length=block_size + 32,
        dropout=0.1,
    ).to(device)

    criterion = nn.CrossEntropyLoss(ignore_index=vocab[PAD_TOKEN])
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    print(f"Device: {device}")
    print(f"Corpus length: {len(text_ids)} | vocab size: {len(vocab)}")
    train_model(model, dataloader, optimizer, criterion, device)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state_dict": model.state_dict(), "vocab": vocab}, MODEL_PATH)
    print(f"Saved model: {MODEL_PATH}")

    prompts = ["en un lugar", "el escudero", "al caer la tarde"]
    print("\nGenerated examples:\n")
    for prompt in prompts:
        print(f"PROMPT: {prompt}")
        print(generate_text(model, prompt, vocab, inv_vocab, device))
        print("-" * 60)


if __name__ == "__main__":
    main()
