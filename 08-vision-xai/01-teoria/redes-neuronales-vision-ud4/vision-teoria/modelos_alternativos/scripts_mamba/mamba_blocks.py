"""
Mamba Blocks: Módulo base con arquitecturas Mamba adaptadas para NLP

Contiene:
- MambaEncoderBlock: Mamba bidireccional para encoder
- MambaDecoderBlock: Mamba causal para decoder  
- MambaSeq2Seq: Encoder-Decoder completo
- MambaDecoderOnly: Solo decoder para generación
- MambaEncoderClassifier: Encoder para clasificación
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalization"""
    def __init__(self, d_model, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(d_model))
    
    def forward(self, x):
        output = x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)
        return self.weight * output


class MambaBlock(nn.Module):
    """
    Bloque Mamba: Selective State Space Model (versión bidireccional/independiente)
    
    Para uso en encoder (bidireccional) procesamos la secuencia en ambas direcciones.
    Para uso en decoder (causal) aplicamos masking.
    """
    
    def __init__(self, d_model, d_state=16, d_conv=4, expand=2, bidirectional=False):
        super().__init__()
        self.d_model = d_model
        self.d_state = d_state
        self.d_inner = int(expand * d_model)
        self.d_conv = d_conv
        self.bidirectional = bidirectional
        
        # Proyección de entrada
        self.in_proj = nn.Linear(d_model, self.d_inner * 2, bias=False)
        
        # Convolución local
        self.conv1d = nn.Conv1d(
            in_channels=self.d_inner,
            out_channels=self.d_inner,
            kernel_size=d_conv,
            padding=d_conv - 1,
            groups=self.d_inner,
        )
        
        # Parámetros SSM
        self.x_proj = nn.Linear(self.d_inner, d_state * 2 + 1, bias=False)
        self.A_log = nn.Parameter(torch.randn(self.d_inner, d_state))
        self.D = nn.Parameter(torch.ones(self.d_inner))
        
        # Proyección de salida
        self.out_proj = nn.Linear(self.d_inner, d_model, bias=False)
    
    def forward(self, x, reverse=False):
        b, l, d = x.shape
        
        # Proyección y split
        xz = self.in_proj(x)
        x_inner, z = xz.chunk(2, dim=-1)
        
        # Convolución local
        x_inner = x_inner.transpose(1, 2)
        x_inner = self.conv1d(x_inner)[:, :, :l]
        x_inner = x_inner.transpose(1, 2)
        x_inner = F.silu(x_inner)
        
        # Proyecciones para B, C, dt
        x_decay = self.x_proj(x_inner)
        B, C, dt = x_decay.split([self.d_state, self.d_state, 1], dim=-1)
        dt = F.softplus(dt)
        
        # Matriz A
        A = -torch.exp(self.A_log.float())
        
        # SSM scan
        if self.bidirectional and reverse:
            x_inner = torch.flip(x_inner, dims=[1])
            B = torch.flip(B, dims=[1])
            C = torch.flip(C, dims=[1])
            dt = torch.flip(dt, dims=[1])
        
        y = self.ssm_scan(x_inner, dt, A, B, C)
        
        if self.bidirectional and reverse:
            y = torch.flip(y, dims=[1])
        
        # Puerta y salida
        y = y * torch.sigmoid(z)
        y = y + x * torch.sigmoid(self.D)
        
        return self.out_proj(y)
    
    def ssm_scan(self, x, dt, A, B, C):
        """SSM scan simplificado"""
        b, l, d_inner = x.shape
        d_state = self.d_state
        
        h = torch.zeros(b, d_inner, d_state, device=x.device, dtype=x.dtype)
        outputs = []
        
        for i in range(l):
            dti = dt[:, i, :]
            Bi = B[:, i, :]
            Ci = C[:, i, :]
            
            h_new = dti.unsqueeze(-1) * (
                A.unsqueeze(0) * h + 
                (Bi.unsqueeze(1) * x[:, i, :].unsqueeze(-1))
            )
            
            y_i = (Ci.unsqueeze(1) * h_new).sum(-1)
            outputs.append(y_i)
            
            h = h_new
        
        return torch.stack(outputs, dim=1)


class MambaEncoderBlock(nn.Module):
    """Bloque encoder con Mamba bidireccional"""
    
    def __init__(self, d_model, d_state=16, d_conv=4, expand=2):
        super().__init__()
        self.mamba_fwd = MambaBlock(d_model, d_state, d_conv, expand, bidirectional=False)
        self.mamba_rev = MambaBlock(d_model, d_state, d_conv, expand, bidirectional=True)
        self.norm = RMSNorm(d_model)
    
    def forward(self, x):
        # Procesar en ambas direcciones y combinar
        out_fwd = self.mamba_fwd(x)
        out_rev = self.mamba_rev(x, reverse=True)
        return self.norm(out_fwd + out_rev)


class MambaDecoderBlock(nn.Module):
    """Bloque decoder con Mamba causal"""
    
    def __init__(self, d_model, d_state=16, d_conv=4, expand=2):
        super().__init__()
        self.mamba = MambaBlock(d_model, d_state, d_conv, expand, bidirectional=False)
        self.norm = RMSNorm(d_model)
        self.ff = nn.Sequential(
            nn.Linear(d_model, 4 * d_model),
            nn.GELU(),
            nn.Linear(4 * d_model, d_model)
        )
    
    def forward(self, x, mask=None):
        x = self.mamba(x)
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


class MambaSeq2Seq(nn.Module):
    """Mamba Encoder-Decoder para traducción/reformulación"""
    
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model=64, 
                 num_encoder_layers=3, num_decoder_layers=3, 
                 d_state=16, d_conv=4, max_seq_length=30):
        super().__init__()
        self.d_model = d_model
        
        self.src_embed = nn.Embedding(src_vocab_size, d_model)
        self.tgt_embed = nn.Embedding(tgt_vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq_length)
        
        self.encoder_layers = nn.ModuleList([
            MambaEncoderBlock(d_model, d_state, d_conv) 
            for _ in range(num_encoder_layers)
        ])
        
        self.decoder_layers = nn.ModuleList([
            MambaDecoderBlock(d_model, d_state, d_conv) 
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


class MambaDecoderOnly(nn.Module):
    """Mamba Decoder-Only para generación de texto"""
    
    def __init__(self, vocab_size, d_model=64, num_layers=6, 
                 d_state=16, d_conv=4, max_seq_length=120):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq_length)
        
        self.layers = nn.ModuleList([
            MambaDecoderBlock(d_model, d_state, d_conv) 
            for _ in range(num_layers)
        ])
        
        self.norm = RMSNorm(d_model)
        self.fc = nn.Linear(d_model, vocab_size)
        self.dropout = nn.Dropout(0.1)
    
    def forward(self, x):
        x = self.dropout(self.pos_enc(self.embedding(x)))
        for layer in self.layers:
            x = layer(x)
        return self.fc(self.norm(x))


class MambaEncoderClassifier(nn.Module):
    """Mamba Encoder para clasificación"""
    
    def __init__(self, vocab_size, num_classes, d_model=64, 
                 num_layers=4, d_state=16, d_conv=4, max_seq_length=30):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_seq_length)
        
        self.layers = nn.ModuleList([
            MambaEncoderBlock(d_model, d_state, d_conv) 
            for _ in range(num_layers)
        ])
        
        self.norm = RMSNorm(d_model)
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
