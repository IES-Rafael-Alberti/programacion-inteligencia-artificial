import math
import random
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset


DATA_PATH = (
    Path(__file__).resolve().parent.parent / "datos" / "mini_trad_es_en_ampliado.tsv"
)
MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "modelos"
    / "transformers_1_traduccion_en_es.pt"
)

PAD_TOKEN = "<pad>"
SOS_TOKEN = "<sos>"
EOS_TOKEN = "<eos>"
UNK_TOKEN = "<unk>"
SPECIAL_TOKENS = [PAD_TOKEN, SOS_TOKEN, EOS_TOKEN, UNK_TOKEN]


def tokenize(text):
    return text.lower().strip().split()


def load_parallel_data(path):
    pairs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        src_es, tgt_en = line.split("\t")
        # Reutilizamos el dataset existente, pero invertimos el sentido:
        # inglés -> español
        pairs.append((tokenize(tgt_en), tokenize(src_es)))
    return pairs


def build_vocab(sentences):
    vocab = {token: idx for idx, token in enumerate(SPECIAL_TOKENS)}
    for sentence in sentences:
        for token in sentence:
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab


def encode(tokens, vocab):
    unk_id = vocab[UNK_TOKEN]
    return [vocab.get(token, unk_id) for token in tokens]


class TranslationDataset(Dataset):
    def __init__(self, pairs, src_vocab, tgt_vocab):
        self.samples = []
        for src_tokens, tgt_tokens in pairs:
            src_ids = encode(src_tokens, src_vocab)
            tgt_input = [tgt_vocab[SOS_TOKEN]] + encode(tgt_tokens, tgt_vocab)
            tgt_output = encode(tgt_tokens, tgt_vocab) + [tgt_vocab[EOS_TOKEN]]
            self.samples.append((src_ids, tgt_input, tgt_output))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        src_ids, tgt_input, tgt_output = self.samples[idx]
        return (
            torch.tensor(src_ids, dtype=torch.long),
            torch.tensor(tgt_input, dtype=torch.long),
            torch.tensor(tgt_output, dtype=torch.long),
        )


def collate_batch(batch, pad_id):
    src_batch, tgt_in_batch, tgt_out_batch = zip(*batch)
    src_padded = nn.utils.rnn.pad_sequence(
        src_batch, batch_first=True, padding_value=pad_id
    )
    tgt_in_padded = nn.utils.rnn.pad_sequence(
        tgt_in_batch, batch_first=True, padding_value=pad_id
    )
    tgt_out_padded = nn.utils.rnn.pad_sequence(
        tgt_out_batch, batch_first=True, padding_value=pad_id
    )
    return src_padded, tgt_in_padded, tgt_out_padded


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def split_heads(self, x):
        batch_size, seq_length, _ = x.size()
        return x.view(batch_size, seq_length, self.num_heads, self.d_k).transpose(1, 2)

    def combine_heads(self, x):
        batch_size, _, seq_length, _ = x.size()
        return x.transpose(1, 2).contiguous().view(batch_size, seq_length, self.d_model)

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


class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        attn_output = self.self_attn(x, x, x, mask)
        x = self.norm1(x + self.dropout(attn_output))
        ff_output = self.feed_forward(x)
        return self.norm2(x + self.dropout(ff_output))


class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.cross_attn = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, enc_output, src_mask, tgt_mask):
        x = self.norm1(x + self.dropout(self.self_attn(x, x, x, tgt_mask)))
        x = self.norm2(
            x + self.dropout(self.cross_attn(x, enc_output, enc_output, src_mask))
        )
        ff_output = self.feed_forward(x)
        return self.norm3(x + self.dropout(ff_output))


class Transformer(nn.Module):
    def __init__(
        self,
        src_vocab_size,
        tgt_vocab_size,
        d_model=64,
        num_heads=4,
        num_layers=2,
        d_ff=128,
        max_seq_length=30,
        dropout=0.1,
    ):
        super().__init__()
        self.encoder_embedding = nn.Embedding(src_vocab_size, d_model)
        self.decoder_embedding = nn.Embedding(tgt_vocab_size, d_model)
        self.positional_encoding = PositionalEncoding(d_model, max_seq_length)
        self.encoder_layers = nn.ModuleList(
            [EncoderLayer(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)]
        )
        self.decoder_layers = nn.ModuleList(
            [DecoderLayer(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)]
        )
        self.fc = nn.Linear(d_model, tgt_vocab_size)
        self.dropout = nn.Dropout(dropout)

    def generate_mask(self, src, tgt):
        src_mask = (src != 0).unsqueeze(1).unsqueeze(2)
        tgt_mask = (tgt != 0).unsqueeze(1).unsqueeze(3)
        seq_length = tgt.size(1)
        nopeak_mask = (1 - torch.triu(torch.ones(1, seq_length, seq_length), diagonal=1)).bool().to(tgt.device)
        tgt_mask = tgt_mask & nopeak_mask
        return src_mask, tgt_mask

    def forward(self, src, tgt):
        src_mask, tgt_mask = self.generate_mask(src, tgt)
        src_embedded = self.dropout(
            self.positional_encoding(self.encoder_embedding(src))
        )
        tgt_embedded = self.dropout(
            self.positional_encoding(self.decoder_embedding(tgt))
        )
        enc_output = src_embedded
        for layer in self.encoder_layers:
            enc_output = layer(enc_output, src_mask)
        dec_output = tgt_embedded
        for layer in self.decoder_layers:
            dec_output = layer(dec_output, enc_output, src_mask, tgt_mask)
        return self.fc(dec_output)


def train_model(model, dataloader, optimizer, criterion, device, epochs=300):
    model.train()
    for epoch in range(1, epochs + 1):
        total_loss = 0.0
        for src, tgt_input, tgt_output in dataloader:
            src = src.to(device)
            tgt_input = tgt_input.to(device)
            tgt_output = tgt_output.to(device)
            optimizer.zero_grad()
            logits = model(src, tgt_input)
            loss = criterion(logits.view(-1, logits.size(-1)), tgt_output.view(-1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if epoch % 25 == 0 or epoch == 1:
            print(f"Epoch {epoch:03d} | loss = {total_loss / len(dataloader):.4f}")


def greedy_translate(model, sentence, src_vocab, tgt_vocab, device, max_len=12):
    model.eval()
    inv_tgt_vocab = {idx: token for token, idx in tgt_vocab.items()}
    src_ids = torch.tensor([encode(tokenize(sentence), src_vocab)], dtype=torch.long, device=device)
    generated = [tgt_vocab[SOS_TOKEN]]
    with torch.no_grad():
        for _ in range(max_len):
            tgt_tensor = torch.tensor([generated], dtype=torch.long, device=device)
            logits = model(src_ids, tgt_tensor)
            next_id = logits[0, -1].argmax().item()
            generated.append(next_id)
            if next_id == tgt_vocab[EOS_TOKEN]:
                break
    tokens = [inv_tgt_vocab[idx] for idx in generated[1:] if idx != tgt_vocab[EOS_TOKEN]]
    return " ".join(tokens)


def main():
    random.seed(42)
    torch.manual_seed(42)

    pairs = load_parallel_data(DATA_PATH)
    src_vocab = build_vocab(src for src, _ in pairs)
    tgt_vocab = build_vocab(tgt for _, tgt in pairs)

    dataset = TranslationDataset(pairs, src_vocab, tgt_vocab)
    pad_id = tgt_vocab[PAD_TOKEN]
    dataloader = DataLoader(
        dataset,
        batch_size=8,
        shuffle=True,
        collate_fn=lambda batch: collate_batch(batch, pad_id),
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = Transformer(
        src_vocab_size=len(src_vocab),
        tgt_vocab_size=len(tgt_vocab),
        d_model=64,
        num_heads=4,
        num_layers=2,
        d_ff=128,
        max_seq_length=30,
        dropout=0.1,
    ).to(device)

    criterion = nn.CrossEntropyLoss(ignore_index=pad_id)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    print(f"Device: {device}")
    print(f"Training pairs: {len(dataset)}")
    train_model(model, dataloader, optimizer, criterion, device)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "src_vocab": src_vocab,
            "tgt_vocab": tgt_vocab,
        },
        MODEL_PATH,
    )
    print(f"Saved model: {MODEL_PATH}")

    tests = [
        "hello",
        "good morning",
        "i am tired",
        "i am happy",
        "thank you",
        "goodbye",
        "I am learning transformers",
    ]
    print("\nExamples:")
    for sentence in tests:
        print(f"{sentence} -> {greedy_translate(model, sentence, src_vocab, tgt_vocab, device)}")


if __name__ == "__main__":
    main()
