"""
Ejemplo 3 LFM: Clasificación de Intenciones (Encoder-Only)
=========================================================

Arquitectura: Liquid Encoder
Datos: mini_clasificacion_intenciones.tsv

Este ejemplo demuestra cómo usar Liquid Foundation Models para clasificación,
usando solo el encoder (como BERT pero con bloques Liquid).

Clases: peticion, agradecimiento, pregunta, afirmacion, saludo
"""

import random
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

import sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm_blocks import LiquidEncoderClassifier


DATA_PATH = Path(__file__).resolve().parent.parent / "datos" / "mini_clasificacion_intenciones.tsv"
MODEL_PATH = Path(__file__).resolve().parent.parent / "modelos_lfm" / "lfm_clasificacion_intenciones.pt"

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
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
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


def evaluate(model, dataloader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for x, y in dataloader:
            x = x.to(device)
            y = y.to(device)
            logits = model(x)
            preds = logits.argmax(dim=-1)
            correct += (preds == y).sum().item()
            total += y.size(0)
    return correct / total


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
    model = LiquidEncoderClassifier(
        vocab_size=len(text_vocab),
        num_classes=len(label_vocab),
        d_model=64,
        num_layers=6,
        kernel_size=5,
        max_seq_length=20,
    ).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.001)

    print(f"Device: {device}")
    print(f"Samples: {len(dataset)} | Classes: {list(label_vocab.keys())}")
    print("=" * 50)
    train_model(model, dataloader, optimizer, criterion, device)
    
    # Evaluar
    accuracy = evaluate(model, dataloader, device)
    print(f"\nAccuracy: {accuracy:.2%}")

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
        "que hora es",
    ]
    print("\n" + "=" * 50)
    print("EJEMPLOS DE CLASIFICACIÓN DE INTENCIÓN:")
    print("=" * 50)
    for sentence in tests:
        label = predict(model, sentence, text_vocab, label_vocab, device)
        print(f"'{sentence}' -> {label}")
        print("-" * 40)


if __name__ == "__main__":
    main()
