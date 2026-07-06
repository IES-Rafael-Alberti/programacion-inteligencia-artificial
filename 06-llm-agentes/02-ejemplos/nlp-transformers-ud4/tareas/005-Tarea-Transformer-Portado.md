# Tarea: Implementación del Transformer en otra librería

## Objetivo

Demostrar tu conocimiento profundo del modelo Transformer portando la implementación de PyTorch a **otra librería** de deep learning.

---

## Librerías disponibles

| Librería | Framework | Dificultad | Notes |
|---------|-----------|------------|-------|
| **Keras** (TensorFlow) | Python | Media | Ya la conoces de antes |
| **Flax** | JAX | Alta | Moderno, muy usado en investigación |
| **PyTorch Lightning** | PyTorch | Baja | Muy similar a PyTorch vanilla |

### Recomendaciones

- **Keras**: Si quieres una implementación limpia y bien documentada
- **Flax**: Si quieres aprender JAX y verte en entornos de investigación
- **PyTorch Lightning**: Si quieres mantener la familiaridad con PyTorch pero con código más limpio

---

## Parte 1: Esqueleto base

Se proporciona un esqueleto con las clases principales. Completar los métodos marcados con `TODO`.

### Para Keras (usando Sequential y Functional API)

Se proporciona una estructura usando Sequential y capas que ya conoces de cursos anteriores.

```python
import tensorflow as tf
from tensorflow.keras import layers, Model, Sequential

# =============================================================================
# CAPAS PERSONALIZADAS (necesitan subclases)
# =============================================================================

class PositionalEncoding(layers.Layer):
    """Codificación posicional - SUMA a los embeddings"""
    
    def __init__(self, max_seq_length, d_model, **kwargs):
        super().__init__(**kwargs)
        self.max_seq_length = max_seq_length
        self.d_model = d_model
    
    def get_angles(self, position, i, d_model):
        # TODO: Calcular los ángulos para sen/cos
        # Fórmula: position / (10000^(2i/d_model))
        pass
    
    def call(self, x):
        # TODO: Crear matriz PE y sumar a x
        # Recordar: tf.range o tf.range + 1
        pass
    
    def get_config(self):
        return {"max_seq_length": self.max_seq_length, "d_model": self.d_model}


class MultiHeadAttention(layers.Layer):
    """Atención multi-cabeza - LA PARTE MÁS IMPORTANTE DEL TRANSFORMER"""
    
    def __init__(self, d_model, num_heads, **kwargs):
        super().__init__(**kwargs)
        self.num_heads = num_heads
        self.d_model = d_model
        self.d_k = d_model // num_heads
        
    def build(self, input_shape):
        # TODO: Crear 4 capas densas sin sesgo:
        # W_q, W_k, W_v (d_model -> d_model)
        # W_o (d_model -> d_model)
        self.W_q = layers.Dense(self.d_model, use_bias=False)
        self.W_k = layers.Dense(self.d_model, use_bias=False)
        self.W_v = layers.Dense(self.d_model, use_bias=False)
        self.W_o = layers.Dense(self.d_model, use_bias=False)
    
    def split_heads(self, x, batch_size):
        # TODO: Dividir en num_heads
        # x shape: (batch, seq_len, d_model) -> (batch, num_heads, seq_len, d_k)
        pass
    
    def call(self, q, k, v, mask=None):
        batch_size = tf.shape(q)[0]
        
        # TODO: Proyectar y dividir en cabezas
        # 1. q, k, v = W_q(q), W_k(k), W_v(v)
        # 2. split_heads para cada uno
        
        # TODO: Atención escalada
        # 3. scores = matmul(q, k.T) / sqrt(d_k)
        # 4. aplicar mask si existe
        # 5. softmax(scores)
        # 6. output = matmul(softmax(scores), v)
        
        # TODO: Recombinar cabezas
        # 7. concatenar cabezas
        # 8. output = W_o(concatenated)
        
        pass
    
    def get_config(self):
        return {"d_model": self.d_model, "num_heads": self.num_heads}


# =============================================================================
# ENCODER (usando Sequential - ya lo conoces)
# =============================================================================

def create_encoder_layer(d_model, num_heads, d_ff, dropout=0.1):
    """Un bloque de encoder - SE PUEDE HACER CON SEQUENTIAL"""
    return Sequential([
        # TODO: Multi-head self-attention + Add & Norm
        # 1. MultiHeadAttention
        # 2. Add: x + attn_output
        # 3. LayerNorm
        
        # TODO: Feed Forward + Add & Norm  
        # 4. Dense(d_ff) -> ReLU -> Dense(d_model)
        # 5. Add: x + ff_output
        # 6. LayerNorm
        
        # 7. Dropout
        layers.Dropout(dropout)
    ], name="encoder_layer")


def create_encoder(num_layers, d_model, num_heads, d_ff, max_seq_length, dropout=0.1):
    """Encoder completo - VARIOS EncoderLayers en Sequential"""
    return Sequential([
        layers.Input(shape=(max_seq_length,)),  # Input shape
        layers.Embedding(vocab_size, d_model),  # TODO: parameterizar vocab_size
        PositionalEncoding(max_seq_length, d_model),
        layers.Dropout(dropout),
        # TODO: Apilar num_layers de encoder_layer
        # layers.Embedding(...),
        # PositionalEncoding(...),
        # [create_encoder_layer(...) for _ in range(num_layers)]
    ], name="encoder")


# =============================================================================
# DECODER (más complejo, pero similar)
# =============================================================================

def create_decoder_layer(d_model, num_heads, d_ff, dropout=0.1):
    """Un bloque de decoder con 3 subcapas"""
    return Sequential([
        # TODO: MASKED self-attention + Add & Norm
        # 1. MultiHeadAttention (máscara causal)
        # 2. Add + LayerNorm
        
        # TODO: CROSS attention + Add & Norm
        # 3. MultiHeadAttention(q del decoder, k,v del encoder)
        # 4. Add + LayerNorm
        
        # TODO: Feed Forward + Add & Norm
        # 5. Dense(d_ff) -> ReLU -> Dense(d_model)
        # 6. Add + LayerNorm
        
        layers.Dropout(dropout)
    ], name="decoder_layer")


# =============================================================================
# TRANSFORMER COMPLETO (Functional API - lo has usado en híbridos)
# =============================================================================

def create_transformer(src_vocab_size, tgt_vocab_size, 
                       d_model=64, num_heads=4, num_layers=2, 
                       d_ff=128, max_seq_length=30, dropout=0.1):
    """Transformer completo usando Functional API"""
    
    # TODO: Entradas
    # src_input = layers.Input(shape=(max_seq_length,))
    # tgt_input = layers.Input(shape=(max_seq_length,))
    
    # TODO: Encoder
    # src_embedded = Embedding(src_vocab_size, d_model)(src_input)
    # src_encoded = encoder_block(src_embedded)
    
    # TODO: Decoder
    # tgt_embedded = Embedding(tgt_vocab_size, d_model)(tgt_input)
    # tgt_decoded = decoder_block(tgt_embedded, src_encoded)
    
    # TODO: Salida
    # output = Dense(tgt_vocab_size)(tgt_decoded)
    
    # TODO: Crear modelo
    # model = Model(inputs=[src_input, tgt_input], outputs=output)
    # return model


# =============================================================================
# ENTRENAMIENTO (igual que en los ejemplos de clase)
# =============================================================================

def train_model(model, train_dataset, val_dataset, epochs=20):
    """Entrenamiento típico de Keras"""
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    history = model.fit(
        train_dataset,
        validation_data=val_dataset,
        epochs=epochs,
        callbacks=[
            tf.keras.callbacks.EarlyStopping(patience=3),
            tf.keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=2)
        ]
    )
    return history
```

### Para Flax (JAX)

```python
import jax
import jax.numpy as jnp
from flax import linen as nn

class MultiHeadAttention(nn.Module):
    d_model: int
    num_heads: int
    
    @nn.compact
    def __call__(self, q, k, v, mask=None):
        # TODO: Implementar atención multi-cabeza
        pass

class PositionalEncoding(nn.Module):
    max_seq_length: int
    d_model: int
    
    @nn.compact
    def __call__(self, x):
        # TODO: Crear y aplicar positional encoding
        pass

class EncoderLayer(nn.Module):
    d_model: int
    num_heads: int
    d_ff: int
    dropout: float = 0.1
    
    @nn.compact
    def __call__(self, x, mask=None, training: bool = True):
        # TODO: Implementar bloque de encoder
        pass

class DecoderLayer(nn.Module):
    d_model: int
    num_heads: int
    d_ff: int
    dropout: float = 0.1
    
    @nn.compact
    def __call__(self, x, enc_output, src_mask=None, tgt_mask=None, training: bool = True):
        # TODO: Implementar bloque de decoder
        pass

class Transformer(nn.Module):
    src_vocab_size: int
    tgt_vocab_size: int
    d_model: int = 64
    num_heads: int = 4
    num_layers: int = 2
    d_ff: int = 128
    max_seq_length: int = 30
    dropout: float = 0.1
    
    @nn.compact
    def __call__(self, src, tgt, training: bool = True):
        # TODO: Implementar transformer completo
        pass
```

### Para PyTorch Lightning

```python
import pytorch_lightning as pl
import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        # TODO: Similar a PyTorch vanilla pero en clase independiente
        pass

class TransformerModel(pl.LightningModule):
    def __init__(self, src_vocab_size, tgt_vocab_size, 
                 d_model=64, num_heads=4, num_layers=2, d_ff=128):
        super().__init__()
        # TODO: Crear embeddings, positional encoding, capas
        pass
    
    def forward(self, src, tgt):
        # TODO: Forward pass
        pass
    
    def training_step(self, batch, batch_idx):
        # TODO: Step de entrenamiento
        pass
    
    def validation_step(self, batch, batch_idx):
        # TODO: Step de validación
        pass
    
    def configure_optimizers(self):
        # TODO: Configurar optimizador
        pass
```

---

## Parte 2: Implementación completa

### Requisitos mínimos

1. **Embedding layer** con positional encoding
2. **Multi-head attention** (al menos self-attention)
3. **Feed-forward network**
4. **Layer normalization**
5. **Al menos 1 Encoder layer y 1 Decoder layer** (o equivalentes)
6. **Clasificación/Secuencia** según el ejemplo elegido

### Funcionalidades obligatorias

- [ ] Forward pass completo
- [ ] Generación de máscaras (padding y causal)
- [ ] Pérdida y entrenamiento funcional
- [ ] Ejecución en GPU si está disponible

---

## Parte 3: Comparar con PyTorch original

### Tareas

1. **Ejecutar el ejemplo original en PyTorch** con los datos proporcionados

2. **Implementar en la nueva librería** con los mismos hiperparámetros

3. **Comparar**:
   - Mismos inputs → ¿mismos outputs? (deben ser similares, no idénticos)
   - Tiempo de entrenamiento
   - Uso de memoria
   - Facilidades de debugging

4. **Documentar diferencias**:
   - ¿Qué te ha resultado más fácil/difícil?
   - ¿Qué peculiaridades tiene cada librería?
   - ¿Pros y contras de cada una?

---

## Parte 4: Elegir un ejemplo para portar

| Ejemplo original | Tipo | Descripción |
|-----------------|------|-------------|
| `ejemplo_transformers_1_traduccion_en_es.py` | Encoder-Decoder | Traducción inglés → español |
| `ejemplo_transformers_2_generacion_decoder_only.py` | Decoder-only | Generación estilo Quijote |
| `ejemplo_transformers_3_reformulacion.py` | Encoder-Decoder | Reformulación de texto |
| `ejemplo_transformers_4_encoder_only_clasificacion.py` | Encoder-only | Clasificación |

---

## Recursos

### Keras

```bash
pip install tensorflow
```

- [Documentación oficial](https://keras.io/)
- [Guía de capas personalizadas](https://keras.io/guides/making_new_layers_and_models_via_subclassing/)

### Flax (JAX)

```bash
pip install flax jax jaxlib
```

- [Documentación oficial](https://flax.readthedocs.io/)
- [Ejemplos de transformers](https://github.com/google/flax/tree/main/examples)

### PyTorch Lightning

```bash
pip install pytorch-lightning
```

- [Documentación oficial](https://pytorch-lightning.readthedocs.io/)
- [Guía de migración desde PyTorch](https://pytorch-lightning.readthedocs.io/en/stable/starter/converting.html)

---

## Entrega

Consultar el documento `Tarea-Transformer-Portado-Entrega.md` para ver los requisitos específicos de entrega.
