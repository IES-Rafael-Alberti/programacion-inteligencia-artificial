"""
LFM Blocks: Módulo base con arquitecturas Liquid Foundation Models adaptadas para NLP

Contiene:
- LiquidBlock: Bloque liquid con conv + gates (bidireccional/causal)
- LiquidEncoderBlock: Para encoder bidireccional
- LiquidDecoderBlock: Para decoder causal
- LiquidSeq2Seq: Encoder-Decoder completo
- LiquidDecoderOnly: Solo decoder para generación
- LiquidEncoderClassifier: Encoder para clasificación
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class LiquidBlock(nn.Module):
    """
    Bloque Liquid: Conv1D + Gates dinámicos
    
    Para encoder: bidireccional (procesa en ambas direcciones)
    Para decoder: causal (solo contexto izquierdo)
    """
    
    def __init__(self, d_model, kernel_size=5, bidirectional=False):
        super().__init__()
        self.d_model = d_model
        self.kernel_size = kernel_size
        self.bidirectional = bidirectional
        
        self.norm1 = nn.LayerNorm(d_model)
        self.in_proj = nn.Linear(d_model, d_model)
        self.gate1 = nn.Linear(d_model, d_model)
        self.conv = nn.Conv1d(
            d_model, d_model, kernel_size,
            padding=kernel_size // 2,
            groups=d_model
        )
        self.gate2 = nn.Linear(d_model, d_model)
        self.out_proj = nn.Linear(d_model, d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.ff = nn.Sequential(
            nn.Linear(d_model, 4 * d_model),
            nn.GELU(),
            nn.Linear(4 * d_model, d_model)
        )
    
    def forward(self, x, reverse=False):
        residual = x
        x = self.norm1(x)
        
        # Gate 1: filtrar entrada
        z = self.in_proj(x) * torch.sigmoid(self.gate1(x))
        
        # Conv: procesar localmente
        z = z.transpose(1, 2)
        z = self.conv(z)
        z = z.transpose(1, 2)
        
        # Bidireccional: procesar dirección inversa
        if self.bidirectional and reverse:
            z = torch.flip(z, dims=[1])
            z = self.conv(z)
            z = torch.flip(z, dims=[1])
        
        # Gate 2: filtrar salida de conv
        z = z * torch.sigmoid(self.gate2(x))
        z = self.out_proj(z)
        
        x = residual + z
        x = self.norm2(x)
        x = x + self.ff(x)
        
        return x


class LiquidEncoderBlock(nn.Module):
    """Bloque encoder con Liquid bidireccional"""
    
    def __init__(self, d_model, kernel_size=5):
        super().__init__()
        self.liquid_fwd = LiquidBlock(d_model, kernel_size, bidirectional=False)
        self.liquid_rev = LiquidBlock(d_model, kernel_size, bidirectional=True)
        self.norm = nn.LayerNorm(d_model)
    
    def forward(self, x):
        # Procesar en dirección normal
        out_fwd = self.liquid_fwd(x)
        # Procesar en dirección inversa
        out_rev = self.liquid_rev(x, reverse=True)
        return self.norm(out_fwd + out_rev)


class LiquidDecoderBlock(nn.Module):
    """Bloque decoder con Liquid causal"""
    
    def __init__(self, d_model, kernel_size=5):
        super().__init__()
        self.liquid = LiquidBlock(d_model, kernel_size, bidirectional=False)
        self.norm = nn.LayerNorm(d_model)
        self.ff = nn.Sequential(
            nn.Linear(d_model, 4 * d_model),
            nn.GELU(),
            nn.Linear(4 * d_model, d_model)
        )
    
    def forward(self, x):
        x = self.liquid(x)
        return x + self.ff(self.norm(x))


class PositionalEncoding(nn.Module):
    """Positional encoding sinusoidal"""
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
        return x + self.pe[:, :x.size(1)]


class LiquidSeq2Seq(nn.Module):
    """Liquid Encoder-Decoder para traducción/reformulación"""
    
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model=64,
                 num_encoder_layers=4, num_decoder_layers=4,
                 kernel_size=5, max_seq_length=30):
        super().__init__()
        self.d_model = d_model
        
        self.src_embed = nn.Embedding(src_vocab_size, d_model)
        self.tgt_embed = nn.Embedding(tgt_vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq_length)
        
        self.encoder_layers = nn.ModuleList([
            LiquidEncoderBlock(d_model, kernel_size)
            for _ in range(num_encoder_layers)
        ])
        
        self.decoder_layers = nn.ModuleList([
            LiquidDecoderBlock(d_model, kernel_size)
            for _ in range(num_decoder_layers)
        ])
        
        self.fc = nn.Linear(d_model, tgt_vocab_size)
        self.dropout = nn.Dropout(0.1)
    
    def encode(self, src):
        x = self.dropout(self.pos_enc(self.src_embed(src)))
        for layer in self.encoder_layers:
            x = layer(x)
        return x
    
    def decode(self, tgt, memory):
        x = self.dropout(self.pos_enc(self.tgt_embed(tgt)))
        for layer in self.decoder_layers:
            x = layer(x)
        return self.fc(x)
    
    def forward(self, src, tgt):
        memory = self.encode(src)
        return self.decode(tgt, memory)


class LiquidDecoderOnly(nn.Module):
    """Liquid Decoder-Only para generación de texto"""
    
    def __init__(self, vocab_size, d_model=64, num_layers=8,
                 kernel_size=5, max_seq_length=120):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq_length)
        
        self.layers = nn.ModuleList([
            LiquidDecoderBlock(d_model, kernel_size)
            for _ in range(num_layers)
        ])
        
        self.norm = nn.LayerNorm(d_model)
        self.fc = nn.Linear(d_model, vocab_size)
        self.dropout = nn.Dropout(0.1)
    
    def forward(self, x):
        x = self.dropout(self.pos_enc(self.embedding(x)))
        for layer in self.layers:
            x = layer(x)
        return self.fc(self.norm(x))


class LiquidEncoderClassifier(nn.Module):
    """Liquid Encoder para clasificación"""
    
    def __init__(self, vocab_size, num_classes, d_model=64,
                 num_layers=6, kernel_size=5, max_seq_length=30):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq_length)
        
        self.layers = nn.ModuleList([
            LiquidEncoderBlock(d_model, kernel_size)
            for _ in range(num_layers)
        ])
        
        self.norm = nn.LayerNorm(d_model)
        self.classifier = nn.Linear(d_model, num_classes)
        self.dropout = nn.Dropout(0.1)
    
    def forward(self, x):
        x = self.dropout(self.pos_enc(self.embedding(x)))
        for layer in self.layers:
            x = layer(x)
        
        # Pooling: media de todos los tokens
        x = self.norm(x)
        pooled = x.mean(dim=1)
        return self.classifier(pooled)
