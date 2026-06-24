"""
Ejemplo 2 LFM: Generación de texto estilo Quijote (Decoder-Only)
================================================================

Arquitectura: Liquid Decoder-Only
Datos: mini_estilo_quijote.txt

Este ejemplo demuestra cómo usar Liquid Foundation Models para generación de texto,
usando solo el decoder (como GPT pero con bloques Liquid).
"""

import random
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

import sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm_blocks import LiquidDecoderOnly


DATA_PATH = Path(__file__).resolve().parent.parent / "datos" / "mini_estilo_quijote.txt"
MODEL_PATH = Path(__file__).resolve().parent.parent / "modelos_lfm" / "lfm_generacion_quijote.pt"

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
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
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
            x = torch.tensor([generated[-100:]], dtype=torch.long, device=device)
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
    model = LiquidDecoderOnly(
        vocab_size=len(vocab),
        d_model=64,
        num_layers=8,
        kernel_size=5,
        max_seq_length=block_size + 32,
    ).to(device)

    criterion = nn.CrossEntropyLoss(ignore_index=vocab[PAD_TOKEN])
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.001)

    print(f"Device: {device}")
    print(f"Corpus length: {len(text_ids)} | vocab size: {len(vocab)}")
    print("=" * 50)
    train_model(model, dataloader, optimizer, criterion, device)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state_dict": model.state_dict(), "vocab": vocab}, MODEL_PATH)
    print(f"Saved model: {MODEL_PATH}")

    prompts = ["en un lugar", "el escudero", "al caer la tarde"]
    print("\n" + "=" * 50)
    print("EJEMPLOS DE GENERACIÓN (ESTILO QUIJOTE):")
    print("=" * 50)
    for prompt in prompts:
        print(f"\nPROMPT: {prompt}")
        print(generate_text(model, prompt, vocab, inv_vocab, device))
        print("-" * 60)


if __name__ == "__main__":
    main()
