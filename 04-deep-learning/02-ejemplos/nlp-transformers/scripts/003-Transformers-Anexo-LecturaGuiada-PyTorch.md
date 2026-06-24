---
title: "Transformers: Lectura Guiada del Script en PyTorch"
output:
  html_document:
    toc: true
    toc_depth: 2
    toc_float: true
    number_sections: true
    fig_caption: true
    code_folding: hide
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true
    fig_caption: true
    latex_engine: xelatex
---


# Lectura Guiada del Script `transformerPytorch.py`

Este documento explica paso a paso la implementación de un Transformer en PyTorch contenida en el archivo:

`/home/jmsa/IESRafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD4/04-modelado-avanzado/nlp/transformers/scripts/transformerPytorch.py`

La idea es leer el código no solo como un programa, sino como una traducción directa de los conceptos teóricos vistos en clase.

---

## 1. ¿Qué implementa este script?

El script construye un **Transformer clásico de tipo encoder-decoder**. Incluye:

* embeddings para la secuencia de entrada y de salida,
* codificación posicional sinusoidal,
* bloques de encoder,
* bloques de decoder,
* atención multicabeza,
* red *feed-forward* por posición,
* máscaras para padding y para impedir ver tokens futuros,
* proyección final al vocabulario de salida.

No incluye entrenamiento completo ni carga de datos. Es, sobre todo, una **implementación de la arquitectura**.

---

## 2. Imports iniciales

Al comienzo aparecen:

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import math
import copy
```

Los realmente importantes en este script son:

* `torch`: operaciones con tensores.
* `torch.nn`: capas y módulos de red neuronal.
* `math`: para usar `sqrt` y `log`.

Los imports `optim`, `data` y `copy` están preparados para un contexto más amplio, aunque en este archivo no se aprovechan después.

---

## 3. Clase `MultiHeadAttention`

La primera gran pieza es:

```python
class MultiHeadAttention(nn.Module):
```

Esta clase implementa la **atención multicabeza**. Aquí es donde aparecen `Q`, `K` y `V`.

### 3.1. Constructor

En el constructor se definen:

```python
self.W_q = nn.Linear(d_model, d_model)
self.W_k = nn.Linear(d_model, d_model)
self.W_v = nn.Linear(d_model, d_model)
self.W_o = nn.Linear(d_model, d_model)
```

Estas capas lineales hacen lo siguiente:

* `W_q`: transforma la entrada en **queries**.
* `W_k`: transforma la entrada en **keys**.
* `W_v`: transforma la entrada en **values**.
* `W_o`: mezcla la salida final de todas las cabezas.

Además, se calcula:

```python
self.d_k = d_model // num_heads
```

Es decir, la dimensión de cada cabeza individual.

La comprobación:

```python
assert d_model % num_heads == 0
```

garantiza que el modelo pueda dividirse en varias cabezas sin que sobren dimensiones.

---

## 4. Atención escalada: `scaled_dot_product_attention`

Este método implementa la fórmula central del Transformer:

```python
attn_scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)
```

Aquí ocurre esto:

1. `Q × K^T` calcula cuánto se relaciona cada token con los demás.
2. Se divide por `sqrt(d_k)` para evitar que los valores crezcan demasiado.
3. Después se aplica `softmax` para convertir esas puntuaciones en pesos.
4. Finalmente esos pesos se aplican sobre `V`.

El código sigue exactamente ese orden:

```python
attn_probs = torch.softmax(attn_scores, dim=-1)
output = torch.matmul(attn_probs, V)
```

### ¿Y la máscara?

Si existe una máscara, se aplica aquí:

```python
attn_scores = attn_scores.masked_fill(mask == 0, -1e9)
```

Eso hace que las posiciones prohibidas reciban un valor muy negativo. Tras el `softmax`, su peso queda prácticamente en cero.

Didácticamente, esta línea es muy importante porque conecta directamente con la idea de:

* no atender al padding,
* no ver tokens futuros en el decoder.

---

## 5. `split_heads` y `combine_heads`

Estas dos funciones son esenciales para entender por qué esto se llama **multi-head attention**.

### `split_heads`

```python
return x.view(batch_size, seq_length, self.num_heads, self.d_k).transpose(1, 2)
```

Lo que hace es:

* tomar un tensor de forma `(batch, seq_len, d_model)`,
* partir la dimensión `d_model` en varias cabezas,
* reorganizar el tensor para que quede como:

```text
(batch, num_heads, seq_len, d_k)
```

Así, cada cabeza puede trabajar por separado.

### `combine_heads`

Después de calcular la atención por cabeza, hay que unirlas otra vez:

```python
return x.transpose(1, 2).contiguous().view(batch_size, seq_length, self.d_model)
```

Esto recompone la salida en la forma original:

```text
(batch, seq_len, d_model)
```

---

## 6. Método `forward` de `MultiHeadAttention`

El flujo completo es:

```python
Q = self.split_heads(self.W_q(Q))
K = self.split_heads(self.W_k(K))
V = self.split_heads(self.W_v(V))
attn_output = self.scaled_dot_product_attention(Q, K, V, mask)
output = self.W_o(self.combine_heads(attn_output))
```

Interpretación:

1. Se proyecta la entrada a `Q`, `K` y `V`.
2. Se separan las cabezas.
3. Se aplica atención escalada en cada cabeza.
4. Se vuelven a juntar las cabezas.
5. Se pasa la salida por una última capa lineal.

Este bloque, por sí solo, ya representa el núcleo de la atención multicabeza.

---

## 7. Clase `PositionWiseFeedForward`

La clase:

```python
class PositionWiseFeedForward(nn.Module):
```

implementa la red *feed-forward* que aparece después de la atención en cada bloque del Transformer.

El código es:

```python
self.fc1 = nn.Linear(d_model, d_ff)
self.fc2 = nn.Linear(d_ff, d_model)
self.relu = nn.ReLU()
```

y en `forward`:

```python
return self.fc2(self.relu(self.fc1(x)))
```

Esto significa:

* primero se amplía la dimensión de cada token,
* se aplica una no linealidad,
* luego se vuelve a la dimensión original.

Es importante recordar que esta red se aplica **a cada posición por separado**, no mezclando tokens entre sí. La mezcla entre tokens ya ocurrió en la atención.

---

## 8. Clase `PositionalEncoding`

Como el Transformer no procesa secuencias paso a paso, necesita que le indiquemos la posición de cada token.

Aquí se construye la codificación sinusoidal clásica:

```python
pe[:, 0::2] = torch.sin(position * div_term)
pe[:, 1::2] = torch.cos(position * div_term)
```

Luego se guarda con:

```python
self.register_buffer("pe", pe.unsqueeze(0))
```

Esto significa que `pe`:

* forma parte del módulo,
* se moverá con el modelo a CPU o GPU,
* pero no se entrenará como parámetro.

En `forward`, simplemente se suma a los embeddings:

```python
return x + self.pe[:, : x.size(1)]
```

---

## 9. Clase `EncoderLayer`

El bloque codificador reúne tres piezas:

* self-attention,
* conexión residual + normalización,
* feed-forward + residual + normalización.

Se ve claramente aquí:

```python
attn_output = self.self_attn(x, x, x, mask)
x = self.norm1(x + self.dropout(attn_output))
ff_output = self.feed_forward(x)
x = self.norm2(x + self.dropout(ff_output))
```

Observa que en el encoder:

* `Q = x`
* `K = x`
* `V = x`

Eso significa que el encoder usa **self-attention**: cada token atiende a los demás tokens de la misma secuencia.

---

## 10. Clase `DecoderLayer`

El bloque decodificador es más complejo porque contiene tres subbloques:

1. self-attention enmascarada,
2. cross-attention,
3. feed-forward.

En código:

```python
attn_output = self.self_attn(x, x, x, tgt_mask)
x = self.norm1(x + self.dropout(attn_output))
attn_output = self.cross_attn(x, enc_output, enc_output, src_mask)
x = self.norm2(x + self.dropout(attn_output))
ff_output = self.feed_forward(x)
x = self.norm3(x + self.dropout(ff_output))
```

### Primera atención: self-attention del decoder

Aquí el decoder atiende a sus propios tokens generados hasta el momento:

```python
self.self_attn(x, x, x, tgt_mask)
```

Se usa `tgt_mask` para impedir que un token vea posiciones futuras.

### Segunda atención: cross-attention

Aquí aparece la conexión con el encoder:

```python
self.cross_attn(x, enc_output, enc_output, src_mask)
```

Esto significa:

* `Q` sale del decoder,
* `K` y `V` salen del encoder.

Justo esa es la definición de **atención encoder-decoder**.

---

## 11. Clase `Transformer`

La clase principal integra todo el modelo.

### 11.1. Embeddings

Se crean dos capas de embedding:

```python
self.encoder_embedding = nn.Embedding(src_vocab_size, d_model)
self.decoder_embedding = nn.Embedding(tgt_vocab_size, d_model)
```

Una para la secuencia de entrada y otra para la secuencia de salida.

### 11.2. Codificación posicional

```python
self.positional_encoding = PositionalEncoding(d_model, max_seq_length)
```

La misma codificación posicional se reutiliza para encoder y decoder.

### 11.3. Pilas de capas

```python
self.encoder_layers = nn.ModuleList([...])
self.decoder_layers = nn.ModuleList([...])
```

Esto crea una lista de capas repetidas. Es la forma en la que PyTorch representa la idea de “apilar varias capas del encoder y del decoder”.

### 11.4. Capa final

```python
self.fc = nn.Linear(d_model, tgt_vocab_size)
```

Esta capa toma la representación final del decoder y la convierte en puntuaciones sobre el vocabulario de salida.

---

## 12. Método `generate_mask`

Este método genera dos máscaras:

* `src_mask`: para ocultar padding en la secuencia de entrada.
* `tgt_mask`: para ocultar padding y además impedir mirar al futuro en la salida.

### Máscara de origen

```python
src_mask = (src != 0).unsqueeze(1).unsqueeze(2)
```

Esto marca como válidas las posiciones distintas de cero. Aquí se está suponiendo que el token `0` es el padding.

### Máscara de destino

```python
tgt_mask = (tgt != 0).unsqueeze(1).unsqueeze(3)
```

Después se combina con la máscara triangular:

```python
nopeak_mask = (1 - torch.triu(torch.ones(1, seq_length, seq_length), diagonal=1)).bool()
tgt_mask = tgt_mask & nopeak_mask
```

La idea es:

* no atender a padding,
* no atender a tokens futuros.

Este bloque es una de las mejores partes del script para explicar la diferencia entre:

* máscara de padding,
* máscara causal o de no-anticipación.

---

## 13. Método `forward` del Transformer

El flujo completo del modelo es:

### Paso 1. Generar máscaras

```python
src_mask, tgt_mask = self.generate_mask(src, tgt)
```

### Paso 2. Obtener embeddings y añadir posición

```python
src_embedded = self.dropout(self.positional_encoding(self.encoder_embedding(src)))
tgt_embedded = self.dropout(self.positional_encoding(self.decoder_embedding(tgt)))
```

### Paso 3. Pasar por el encoder

```python
enc_output = src_embedded
for enc_layer in self.encoder_layers:
    enc_output = enc_layer(enc_output, src_mask)
```

### Paso 4. Pasar por el decoder

```python
dec_output = tgt_embedded
for dec_layer in self.decoder_layers:
    dec_output = dec_layer(dec_output, enc_output, src_mask, tgt_mask)
```

### Paso 5. Proyección final al vocabulario

```python
output = self.fc(dec_output)
```

La salida tiene forma aproximada:

```text
(batch_size, seq_len, tgt_vocab_size)
```

Es decir, para cada posición de la secuencia genera una puntuación para cada palabra posible del vocabulario.

---

## 14. Qué representa bien este script

Este script es especialmente bueno para enseñar:

* cómo se construyen `Q`, `K` y `V`,
* dónde aparece la atención escalada,
* cómo se implementa la atención multicabeza,
* cómo se estructura un encoder y un decoder,
* cómo funciona la máscara causal del decoder,
* cómo se encadenan las capas en el `forward`.

---

## 15. Simplificaciones o limitaciones del script

Aunque es muy útil para aprender, conviene señalar algunas simplificaciones:

* `d_ff=2` es demasiado pequeño para un Transformer real.
* No hay bucle de entrenamiento.
* No hay tokenización ni ejemplo con datos reales.
* No se devuelve explícitamente la matriz de pesos de atención, solo la salida.
* Está pensado más para **entender la arquitectura** que para usarlo en producción.

---

## 16. Idea final para clase

Una buena forma de explicarlo es esta:

1. Primero enseñar el bloque `MultiHeadAttention`.
2. Después mostrar cómo ese bloque se reutiliza en encoder y decoder.
3. Finalmente enseñar el `forward` completo del Transformer.

Así el alumnado ve la relación entre:

* la teoría del mecanismo de atención,
* la implementación en PyTorch,
* y la arquitectura completa del modelo.

---
