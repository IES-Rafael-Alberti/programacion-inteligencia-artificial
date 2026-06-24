"""
Ejemplo 4 LFM: Reformulación con Sinónimos (Seq2Seq)
======================================================

Arquitectura: Liquid Encoder-Decoder
Datos: mini_reformulacion_es.tsv

Este ejemplo demuestra cómo usar Liquid Foundation Models para reformular frases,
reemplazando palabras con sinónimos o frases equivalentes.

Ejemplo: "el coche es rojo" -> "el automóvil es rojo"
"""

import random
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

import sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm_blocks import LiquidSeq2Seq


DATA_PATH = Path(__file__).resolve().parent.parent / "datos" / "mini_reformulacion_es.tsv"
MODEL_PATH = Path(__file__).resolve().parent.parent / "modelos_lfm" / "lfm_reformulacion_es.pt"

PAD_TOKEN = "<pad>"
SOS_TOKEN = "<sos>"
EOS_TOKEN = "<eos>"
UNK_TOKEN = "<unk>"
SPECIAL_TOKENS = [PAD_TOKEN, SOS_TOKEN, EOS_TOKEN, UNK_TOKEN]


def tokenize(text):
    return text.lower().strip().split()


def load_pairs(path):
    pairs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        src, tgt = line.split("\t")
        pairs.append((tokenize(src), tokenize(tgt)))
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


class ReformulationDataset(Dataset):
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
        src, tgt_in, tgt_out = self.samples[idx]
        return (
            torch.tensor(src, dtype=torch.long),
            torch.tensor(tgt_in, dtype=torch.long),
            torch.tensor(tgt_out, dtype=torch.long),
        )


def collate_batch(batch, pad_id):
    src_batch, tgt_in_batch, tgt_out_batch = zip(*batch)
    src_padded = nn.utils.rnn.pad_sequence(src_batch, batch_first=True, padding_value=pad_id)
    tgt_in_padded = nn.utils.rnn.pad_sequence(tgt_in_batch, batch_first=True, padding_value=pad_id)
    tgt_out_padded = nn.utils.rnn.pad_sequence(tgt_out_batch, batch_first=True, padding_value=pad_id)
    return src_padded, tgt_in_padded, tgt_out_padded


def train_model(model, dataloader, optimizer, criterion, device, epochs=350):
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
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            total_loss += loss.item()

        if epoch % 35 == 0 or epoch == 1:
            print(f"Epoch {epoch:03d} | loss = {total_loss / len(dataloader):.4f}")


def greedy_generate(model, sentence, src_vocab, tgt_vocab, device, max_len=16):
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

    tokens = [
        inv_tgt_vocab[idx]
        for idx in generated[1:]
        if idx != tgt_vocab[EOS_TOKEN]
    ]
    return " ".join(tokens)


def main():
    random.seed(42)
    torch.manual_seed(42)

    pairs = load_pairs(DATA_PATH)
    src_vocab = build_vocab(src for src, _ in pairs)
    tgt_vocab = build_vocab(tgt for _, tgt in pairs)

    dataset = ReformulationDataset(pairs, src_vocab, tgt_vocab)
    pad_id = tgt_vocab[PAD_TOKEN]
    dataloader = DataLoader(
        dataset,
        batch_size=8,
        shuffle=True,
        collate_fn=lambda batch: collate_batch(batch, pad_id),
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = LiquidSeq2Seq(
        src_vocab_size=len(src_vocab),
        tgt_vocab_size=len(tgt_vocab),
        d_model=64,
        num_encoder_layers=4,
        num_decoder_layers=4,
        kernel_size=5,
        max_seq_length=24,
    ).to(device)

    criterion = nn.CrossEntropyLoss(ignore_index=pad_id)
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.001)

    print(f"Device: {device}")
    print(f"Pairs: {len(dataset)}")
    print("=" * 50)
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

    examples = [
        "el coche es rojo",
        "tengo hambre",
        "la respuesta es correcta",
        "me gusta leer",
        "la estacion esta lejos",
    ]
    print("\n" + "=" * 50)
    print("EJEMPLOS DE REFORMULACIÓN:")
    print("=" * 50)
    for sentence in examples:
        reformulation = greedy_generate(model, sentence, src_vocab, tgt_vocab, device)
        print(f"ORIGINAL:    {sentence}")
        print(f"REFORMULADO: {reformulation}")
        print("-" * 40)


if __name__ == "__main__":
    main()
