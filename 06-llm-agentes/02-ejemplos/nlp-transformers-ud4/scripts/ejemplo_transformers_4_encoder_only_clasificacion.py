import math
import random
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset


DATA_PATH = (
    Path(__file__).resolve().parent.parent / "datos" / "mini_clasificacion_intenciones.tsv"
)
MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "modelos"
    / "transformers_4_encoder_only_clasificacion.pt"
)

PAD_TOKEN = "<pad>"
UNK_TOKEN = "<unk>"
SPECIAL_TOKENS = [PAD_TOKEN, UNK_TOKEN]


def tokenize(text):
    return text.lower().strip().split()


def load_dataset(path):
    samples = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        text, label = line.split("\t")
        samples.append((tokenize(text), label))
    return samples


def build_vocab(sentences):
    vocab = {token: idx for idx, token in enumerate(SPECIAL_TOKENS)}
    for sentence in sentences:
        for token in sentence:
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab


def build_label_vocab(labels):
    return {label: idx for idx, label in enumerate(sorted(set(labels)))}


def encode(tokens, vocab):
    unk_id = vocab[UNK_TOKEN]
    return [vocab.get(token, unk_id) for token in tokens]


class ClassificationDataset(Dataset):
    def __init__(self, samples, text_vocab, label_vocab):
        self.samples = []
        for tokens, label in samples:
            text_ids = encode(tokens, text_vocab)
            label_id = label_vocab[label]
            self.samples.append((text_ids, label_id))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        text_ids, label_id = self.samples[idx]
        return (
            torch.tensor(text_ids, dtype=torch.long),
            torch.tensor(label_id, dtype=torch.long),
        )


def collate_batch(batch, pad_id):
    texts, labels = zip(*batch)
    texts_padded = nn.utils.rnn.pad_sequence(texts, batch_first=True, padding_value=pad_id)
    labels = torch.stack(labels)
    return texts_padded, labels


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


class EncoderLayer(nn.Module):
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


class EncoderOnlyClassifier(nn.Module):
    def __init__(
        self,
        vocab_size,
        num_classes,
        d_model=64,
        num_heads=4,
        num_layers=2,
        d_ff=128,
        max_seq_length=30,
        dropout=0.1,
    ):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.positional_encoding = PositionalEncoding(d_model, max_seq_length)
        self.layers = nn.ModuleList(
            [EncoderLayer(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)]
        )
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(d_model, num_classes)

    def generate_mask(self, x):
        return (x != 0).unsqueeze(1).unsqueeze(2)

    def forward(self, x):
        mask = self.generate_mask(x)
        x = self.dropout(self.positional_encoding(self.embedding(x)))
        for layer in self.layers:
            x = layer(x, mask)

        # Pooling simple: media de las representaciones válidas
        token_mask = (mask.squeeze(1).squeeze(1)).unsqueeze(-1).float()
        pooled = (x * token_mask).sum(dim=1) / token_mask.sum(dim=1).clamp(min=1.0)
        return self.classifier(pooled)


def train_model(model, dataloader, optimizer, criterion, device, epochs=200):
    model.train()
    for epoch in range(1, epochs + 1):
        total_loss = 0.0
        for x, y in dataloader:
            x = x.to(device)
            y = y.to(device)
            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if epoch % 20 == 0 or epoch == 1:
            print(f"Epoch {epoch:03d} | loss = {total_loss / len(dataloader):.4f}")


def predict(model, sentence, text_vocab, label_vocab, device):
    model.eval()
    inv_label_vocab = {idx: label for label, idx in label_vocab.items()}
    x = torch.tensor([encode(tokenize(sentence), text_vocab)], dtype=torch.long, device=device)
    with torch.no_grad():
        logits = model(x)
        pred = logits.argmax(dim=-1).item()
    return inv_label_vocab[pred]


def main():
    random.seed(42)
    torch.manual_seed(42)

    samples = load_dataset(DATA_PATH)
    text_vocab = build_vocab(tokens for tokens, _ in samples)
    label_vocab = build_label_vocab(label for _, label in samples)

    dataset = ClassificationDataset(samples, text_vocab, label_vocab)
    dataloader = DataLoader(
        dataset,
        batch_size=8,
        shuffle=True,
        collate_fn=lambda batch: collate_batch(batch, text_vocab[PAD_TOKEN]),
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = EncoderOnlyClassifier(
        vocab_size=len(text_vocab),
        num_classes=len(label_vocab),
        d_model=64,
        num_heads=4,
        num_layers=2,
        d_ff=128,
        max_seq_length=20,
        dropout=0.1,
    ).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    print(f"Device: {device}")
    print(f"Samples: {len(dataset)} | classes: {len(label_vocab)}")
    train_model(model, dataloader, optimizer, criterion, device)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "text_vocab": text_vocab,
            "label_vocab": label_vocab,
        },
        MODEL_PATH,
    )
    print(f"Saved model: {MODEL_PATH}")

    tests = [
        "gracias por todo",
        "donde esta el tren",
        "hola buenos dias",
        "quiero reservar una mesa",
        "la puerta esta abierta",
        "quiero reservar un hotel",
    ]
    print("\nPredictions:")
    for sentence in tests:
        print(f"{sentence} -> {predict(model, sentence, text_vocab, label_vocab, device)}")


if __name__ == "__main__":
    main()
