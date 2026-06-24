"""
Script Completo de Comparativa
==============================

Este script entrena los tres modelos (Transformer, Mamba, LFM)
en la misma tarea y genera comparativas.

Usage:
    python comparativa.py --tarea clasificacion
    python comparativa.py --tarea traduccion
    python comparativa.py --tarea generacion
    python comparativa.py --tarea reformulacion
"""

import argparse
import time
import random
import json
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import matplotlib.pyplot as plt

# Los módulos de los modelos
# (Asume que están en el mismo directorio o en scripts_mamba/scripts_lfm)
import sys
sys.path.insert(0, str(Path(__file__).parent / "scripts_mamba"))
sys.path.insert(0, str(Path(__file__).parent / "scripts_lfm"))

from mamba_blocks import MambaSeq2Seq, MambaDecoderOnly, MambaEncoderClassifier
from lfm_blocks import LiquidSeq2Seq, LiquidDecoderOnly, LiquidEncoderClassifier

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

class Config:
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    D_MODEL = 64
    EPOCHS = 300  # Reducido para demo, usar más en práctica real
    BATCH_SIZE = 8
    LR = 0.001
    SEED = 42
    
    # Paths
    DATA_DIR = Path(__file__).parent / "datos"
    OUTPUT_DIR = Path(__file__).parent / "resultados"


def set_seed(seed):
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# =============================================================================
# TRANSFORMER (Implementación simplificada)
# =============================================================================

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_length):
        super().__init__()
        import math
        pe = torch.zeros(max_seq_length, d_model)
        position = torch.arange(0, max_seq_length, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe.unsqueeze(0))
    
    def forward(self, x):
        return x + self.pe[:, :x.size(1)]


class TransformerEncoderClassifier(nn.Module):
    """Transformer Encoder para clasificación"""
    def __init__(self, vocab_size, num_classes, d_model=64, num_heads=4, num_layers=2, max_seq=30):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq)
        
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=num_heads, dim_feedforward=4*d_model, 
            batch_first=True
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.classifier = nn.Linear(d_model, num_classes)
    
    def forward(self, x):
        x = self.pos_enc(self.embed(x))
        x = self.encoder(x)
        return self.classifier(x.mean(dim=1))


class TransformerSeq2Seq(nn.Module):
    """Transformer Encoder-Decoder para seq2seq"""
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model=64, num_heads=4, 
                 num_layers=2, max_seq=30):
        super().__init__()
        self.src_embed = nn.Embedding(src_vocab_size, d_model)
        self.tgt_embed = nn.Embedding(tgt_vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq)
        
        self.encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=num_heads, dim_feedforward=4*d_model, batch_first=True
        )
        self.encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        
        self.decoder_layer = nn.TransformerDecoderLayer(
            d_model=d_model, nhead=num_heads, dim_feedforward=4*d_model, batch_first=True
        )
        self.decoder = nn.TransformerDecoder(self.decoder_layer, num_layers=num_layers)
        
        self.fc = nn.Linear(d_model, tgt_vocab_size)
    
    def forward(self, src, tgt):
        src_emb = self.pos_enc(self.src_embed(src))
        tgt_emb = self.pos_enc(self.tgt_embed(tgt))
        
        memory = self.encoder(src_emb)
        output = self.decoder(tgt_emb, memory)
        return self.fc(output)


class TransformerDecoderOnly(nn.Module):
    """Transformer Decoder-Only para generación"""
    def __init__(self, vocab_size, d_model=64, num_heads=4, num_layers=2, max_seq=120):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq)
        
        decoder_layer = nn.TransformerDecoderLayer(
            d_model=d_model, nhead=num_heads, dim_feedforward=4*d_model, batch_first=True
        )
        self.decoder = nn.TransformerDecoder(decoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(d_model, vocab_size)
    
    def forward(self, x):
        x = self.pos_enc(self.embed(x))
        x = self.decoder(x, x)
        return self.fc(x)


# =============================================================================
# DATOS
# =============================================================================

def load_clasificacion_data():
    """Carga datos de clasificación de intenciones"""
    data_path = Config.DATA_DIR / "mini_clasificacion_intenciones.tsv"
    samples = []
    for line in data_path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        text, label = line.strip().split("\t")
        samples.append((text.lower().split(), label))
    
    # Build vocab
    vocab = {"<pad>": 0, "<unk>": 1}
    for tokens, _ in samples:
        for t in tokens:
            if t not in vocab:
                vocab[t] = len(vocab)
    
    labels = sorted(set(l for _, l in samples))
    label_vocab = {l: i for i, l in enumerate(labels)}
    
    return samples, vocab, label_vocab


def load_seq2seq_data():
    """Carga datos de traducción/reformulación"""
    data_path = Config.DATA_DIR / "mini_trad_es_en_ampliado.tsv"
    pairs = []
    for line in data_path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        src, tgt = line.strip().split("\t")
        pairs.append((tgt.lower().split(), src.lower().split()))  # EN -> ES
    
    vocab = {"<pad>": 0, "<sos>": 1, "<eos>": 2, "<unk>": 3}
    for src, tgt in pairs:
        for t in src + tgt:
            if t not in vocab:
                vocab[t] = len(vocab)
    
    return pairs, vocab


class ClasificacionDataset(Dataset):
    def __init__(self, samples, vocab, label_vocab):
        self.data = []
        for tokens, label in samples:
            ids = [vocab.get(t, vocab["<unk>"]) for t in tokens]
            self.data.append((ids, label_vocab[label]))
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return torch.tensor(self.data[idx][0], dtype=torch.long), self.data[idx][1]


def train_and_measure(model, train_loader, criterion, optimizer, epochs, device, model_name):
    """Entrena un modelo y mide tiempos"""
    model = model.to(device)
    metrics = {
        "modelo": model_name,
        "epochs": [],
        "epoch_times": [],
        "parametros": sum(p.numel() for p in model.parameters()),
    }
    
    start_total = time.time()
    
    for epoch in range(1, epochs + 1):
        start_epoch = time.time()
        model.train()
        total_loss = 0
        
        for x, y in train_loader:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad()
            out = model(x)
            loss = criterion(out, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        epoch_time = time.time() - start_epoch
        avg_loss = total_loss / len(train_loader)
        
        metrics["epochs"].append({"epoch": epoch, "loss": avg_loss})
        metrics["epoch_times"].append(epoch_time)
        
        if epoch % 50 == 0 or epoch == 1:
            print(f"  {model_name} - Epoch {epoch}: loss={avg_loss:.4f}, time={epoch_time:.2f}s")
    
    metrics["tiempo_total"] = time.time() - start_total
    metrics["loss_final"] = metrics["epochs"][-1]["loss"]
    
    return metrics


def plot_comparison(all_metrics, tarea, save_dir):
    """Genera gráficos comparativos"""
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    
    # Gráfico 1: Curvas de pérdida
    plt.figure(figsize=(10, 6))
    for m in all_metrics:
        epochs = [e["epoch"] for e in m["epochs"]]
        losses = [e["loss"] for e in m["epochs"]]
        plt.plot(epochs, losses, label=m["modelo"], linewidth=2)
    
    plt.xlabel("Época")
    plt.ylabel("Loss")
    plt.title(f"Comparativa de Convergencia - {tarea}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(save_dir / f"loss_curves_{tarea}.png", dpi=150)
    plt.close()
    
    # Gráfico 2: Tiempos
    plt.figure(figsize=(8, 5))
    modelos = [m["modelo"] for m in all_metrics]
    tiempos = [m["tiempo_total"] for m in all_metrics]
    plt.bar(modelos, tiempos, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.ylabel("Tiempo total (s)")
    plt.title(f"Tiempo de Entrenamiento - {tarea}")
    for i, t in enumerate(tiempos):
        plt.text(i, t + 1, f"{t:.1f}s", ha='center')
    plt.savefig(save_dir / f"tiempos_{tarea}.png", dpi=150)
    plt.close()
    
    # Gráfico 3: Loss final
    plt.figure(figsize=(8, 5))
    losses = [m["loss_final"] for m in all_metrics]
    plt.bar(modelos, losses, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.ylabel("Loss Final")
    plt.title(f"Loss Final - {tarea}")
    for i, l in enumerate(losses):
        plt.text(i, l + 0.01, f"{l:.4f}", ha='center')
    plt.savefig(save_dir / f"loss_final_{tarea}.png", dpi=150)
    plt.close()


def print_summary(all_metrics):
    """Imprime tabla comparativa"""
    print("\n" + "="*70)
    print("RESUMEN COMPARATIVO")
    print("="*70)
    print(f"{'Modelo':<15} | {'Loss':<10} | {'Tiempo(s)':<12} | {'Params':<12}")
    print("-"*70)
    
    for m in all_metrics:
        print(f"{m['modelo']:<15} | {m['loss_final']:<10.4f} | {m['tiempo_total']:<12.2f} | {m['parametros']:<12,}")
    
    print("-"*70)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tarea", type=str, default="clasificacion",
                       choices=["clasificacion", "traduccion", "generacion", "reformulacion"])
    parser.add_argument("--epochs", type=int, default=300)
    args = parser.parse_args()
    
    set_seed(Config.SEED)
    print(f"Dispositivo: {Config.DEVICE}")
    print(f"Tarea: {args.tarea}")
    print(f"Épocas: {args.epochs}")
    print("="*50)
    
    all_metrics = []
    
    # -------------------------------------------------------------------------
    # Clasificación
    # -------------------------------------------------------------------------
    if args.tarea == "clasificacion":
        samples, vocab, label_vocab = load_clasificacion_data()
        dataset = ClasificacionDataset(samples, vocab, label_vocab)
        loader = DataLoader(dataset, batch_size=Config.BATCH_SIZE, shuffle=True)
        
        input_size = len(vocab)
        num_classes = len(label_vocab)
        
        # Transformer
        print("\n>>> Entrenando TRANSFORMER...")
        model = TransformerEncoderClassifier(input_size, num_classes, 
                                            d_model=Config.D_MODEL, num_layers=2)
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=Config.LR)
        metrics = train_and_measure(model, loader, criterion, optimizer, 
                                   args.epochs, Config.DEVICE, "Transformer")
        all_metrics.append(metrics)
        
        # Mamba
        print("\n>>> Entrenando MAMBA...")
        model = MambaEncoderClassifier(input_size, num_classes,
                                      d_model=Config.D_MODEL, num_layers=4)
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=Config.LR)
        metrics = train_and_measure(model, loader, criterion, optimizer,
                                   args.epochs, Config.DEVICE, "Mamba")
        all_metrics.append(metrics)
        
        # LFM
        print("\n>>> Entrenando LFM...")
        model = LiquidEncoderClassifier(input_size, num_classes,
                                       d_model=Config.D_MODEL, num_layers=6)
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=Config.LR)
        metrics = train_and_measure(model, loader, criterion, optimizer,
                                   args.epochs, Config.DEVICE, "LFM")
        all_metrics.append(metrics)
    
    # -------------------------------------------------------------------------
    # Traducción (simplificado - usar scripts completos para mejores resultados)
    # -------------------------------------------------------------------------
    elif args.tarea == "traduccion":
        print("\n[!] Para traducción, usa los scripts completos:")
        print("    python scripts_mamba/ejemplo_mamba_1_traduccion_en_es.py")
        print("    python scripts_lfm/ejemplo_lfm_1_traduccion_en_es.py")
        return
    
    # -------------------------------------------------------------------------
    # Generación (simplificado)
    # -------------------------------------------------------------------------
    elif args.tarea == "generacion":
        print("\n[!] Para generación, usa los scripts completos:")
        print("    python scripts_mamba/ejemplo_mamba_2_generacion_decoder_only.py")
        print("    python scripts_lfm/ejemplo_lfm_2_generacion_decoder_only.py")
        return
    
    # -------------------------------------------------------------------------
    # Reformulación (simplificado)
    # -------------------------------------------------------------------------
    elif args.tarea == "reformulacion":
        print("\n[!] Para reformulación, usa los scripts completos:")
        print("    python scripts_mamba/ejemplo_mamba_4_reformulacion.py")
        print("    python scripts_lfm/ejemplo_lfm_4_reformulacion.py")
        return
    
    # -------------------------------------------------------------------------
    # Generar comparativas
    # -------------------------------------------------------------------------
    print_summary(all_metrics)
    plot_comparison(all_metrics, args.tarea, Config.OUTPUT_DIR)
    
    # Guardar métricas
    with open(Config.OUTPUT_DIR / f"metricas_{args.tarea}.json", "w") as f:
        json.dump(all_metrics, f, indent=2)
    
    print(f"\nResultados guardados en {Config.OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
