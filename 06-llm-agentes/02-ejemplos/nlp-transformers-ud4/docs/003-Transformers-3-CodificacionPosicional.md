---
title: "Transformers 3: Codificación Posicional"
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


# 📍 Codificación Posicional en Transformer
Explicación detallada de la **codificación posicional** (*Positional Encoding*).

## 🧠 ¿Por qué es necesaria?

A diferencia de las RNNs o LSTMs, los modelos Transformer **no procesan los tokens en orden secuencial**. Todas las palabras se procesan en paralelo. Esto significa que por sí solos **no saben qué palabra va antes o después**.

Para que el modelo pueda entender **el orden y la posición de las palabras**, se introduce una **codificación posicional**, que se suma a los embeddings.

---

## ✍️ ¿Cómo se implementa?

### ✅ Opción 1: **Codificación Posicional Fija (sinusoidal)**

Esta fue la propuesta original del paper de Vaswani et al. (2017). Usa funciones seno y coseno con diferentes frecuencias.

### Fórmulas:

$$
PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i / d_{model}}}\right)
$$

$$
PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i / d_{model}}}\right)
$$

* `pos`: posición de la palabra (0, 1, 2, ...)
* `i`: dimensión dentro del embedding
* `d_model`: tamaño del embedding (por ejemplo, 512)

👉 Se calcula una matriz de forma `(seq_len × d_model)` que se **suma** al embedding de cada palabra.

---

### 🔢 Ejemplo en Python (simplificado)

```python
import numpy as np
import matplotlib.pyplot as plt

def positional_encoding(pos, d_model):
    PE = np.zeros((pos, d_model))
    for p in range(pos):
        for i in range(0, d_model, 2):
            angle = p / (10000 ** ((2 * i)/d_model))
            PE[p, i] = np.sin(angle)
            if i+1 < d_model:
                PE[p, i+1] = np.cos(angle)
    return PE

# Generamos PE para las primeras 50 posiciones
pe = positional_encoding(50, 16)

plt.figure(figsize=(10, 6))
plt.imshow(pe.T, cmap='viridis', aspect='auto')
plt.xlabel("Posición en la secuencia")
plt.ylabel("Dimensiones del embedding")
plt.title("Codificación Posicional (sinusoidal)")
plt.colorbar()
plt.show()
```

---

### ✅ Opción 2: **Codificación Aprendida**

* En lugar de usar funciones seno/coseno, se define una **matriz de embedding para las posiciones**.
* Se entrena igual que los embeddings de las palabras.
* Tiene forma `(max_len × d_model)`.

Ejemplo (en PyTorch):

```python
import torch.nn as nn

max_len = 512
d_model = 768
pos_embedding = nn.Embedding(max_len, d_model)
```

---

## 🧩 ¿Cómo se usa?

Al preparar la entrada al modelo Transformer:

```python
input = word_embeddings + positional_encoding
```

Cada vector de palabra se modifica ligeramente para reflejar **su posición relativa en la secuencia**, permitiendo al modelo distinguir:

* “El gato duerme.”
* “Duerme el gato.”

---

## 🎯 ¿Cuál usar?

| Tipo       | Ventajas                                                | Desventajas                             |
| ---------- | ------------------------------------------------------- | --------------------------------------- |
| Sinusoidal | No necesita entrenarse, generaliza a longitudes mayores | No se adapta a datos específicos        |
| Aprendida  | Se ajusta a los datos                                   | No generaliza fuera del rango entrenado |

---
