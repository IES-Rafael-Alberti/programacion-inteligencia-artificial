---
title: "Transformers 6: Multi-Head Attention"
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


# Multi-Head Attention en Transformer

## 🧪 Introducción

El mecanismo de **multi-head attention** permite al modelo Transformer aplicar múltiples cabezas de atención en paralelo. Cada una de estas cabezas puede aprender a enfocarse en distintos tipos de relaciones entre palabras, enriqueciendo la comprensión del contexto.

---

## 🤝 ¿Por qué usar múltiples cabezas?

Una sola cabeza de atención puede tener limitaciones a la hora de capturar relaciones diversas (como dependencia a largo plazo, relaciones sintácticas, semánticas, etc.). Las **múltiples cabezas** permiten al modelo:

* Aprender distintas representaciones del mismo input.
* Prestar atención a diferentes aspectos del contexto simultáneamente.
* Capturar relaciones complejas en lenguaje natural.

---

## 🔢 Cómo funciona

Supongamos que tenemos `h` cabezas. Para cada una de ellas, el modelo calcula:

```
head_i = Attention(QW_Q_i, KW_K_i, VW_V_i)
```

Esto genera `h` salidas distintas de atención, cada una de forma:

```
(seq_len, d_k)
```

Luego, todas estas salidas se **concatenan** y se proyectan de nuevo a la dimensión original:

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) × W_O
```

Cada cabeza usa sus propias matrices de proyección para transformar la entrada en `Q`, `K` y `V`. Esto permite que distintas cabezas aprendan relaciones diferentes sobre los mismos tokens.

### Diagrama de formas (shapes)

```
          h x (seq_len × d_k)
              │
              ▼
      Concat (seq_len × (h × d_k))
              │
              ▼
     Proyección final (seq_len × d_model)
```

---

## 🔄 Interacción con otras capas

Multi-head attention **no actúa de forma aislada**. Está dentro de un bloque que también incluye:

* **Conexión residual**: la salida se suma a la entrada original.
* **Layer Normalization**: estabiliza los valores de activación.
* **Feed-Forward Network (FFN)**: red neuronal aplicada a cada posición.

Esto se aplica en cada capa del encoder y del decoder.

---

## 🔹 Resumen

* Multi-head attention permite al modelo **ver el contexto desde distintos puntos de vista**.
* Aumenta la expresividad y capacidad de generalización.
* Las salidas se concatenan y proyectan para mantener la dimensión original.

---

📍 **Nota final:** lo que hace especial al Transformer no es solo su capacidad de atención, sino **cómo distribuye la atención de forma paralela** y prescinde totalmente de mecanismos secuenciales como RNN o LSTM. Esto le permite escalar y aprender relaciones complejas de forma más eficiente.
