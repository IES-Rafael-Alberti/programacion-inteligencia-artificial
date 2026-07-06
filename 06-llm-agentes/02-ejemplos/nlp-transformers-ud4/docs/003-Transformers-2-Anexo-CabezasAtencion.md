---
title: "Transformers 2: Anexo sobre Cabezas de Atención y Multi-Head Attention"
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


# Cabezas de Atención y Multi-Head Attention

Este documento amplía la explicación del mecanismo de atención centrándose en la estructura de una cabeza de atención y en cómo varias cabezas se combinan en la atención multicabeza.

---

## 🔹 Cabeza 2

Usamos un conjunto diferente de matrices para que "mire" otras relaciones:

```python
Wq₂ = [[0, 1], [1, 0]]
Wk₂ = [[1, 1], [1, 0]]
Wv₂ = [[0, 1], [1, 1]]
```

### Paso 1: Calcular Q₂, K₂, V₂

Por ejemplo, para "El" = \[1, 0]:

```python
Q₂("El") = [1, 0] @ Wq₂ = [0, 1]
K₂("El") = [1, 0] @ Wk₂ = [1, 1]
V₂("El") = [1, 0] @ Wv₂ = [0, 1]
```

El procedimiento se repite igual que en el ejemplo anterior, pero con nuevos pesos para esta segunda cabeza.

### Paso 2: Calcular scores y softmax

Para "El":

* Q = \[0, 1]
* Dot con K("El") = \[0, 1]·\[1, 1] = 1
* Dot con K("gato") = ...
* Dot con K("duerme") = ...

→ Aplicas softmax → obtienes **pesos de atención para Cabeza 2**

### Paso 3: Salidas ponderadas de Cabeza 2

Ejemplo para "El":

```python
salida₂("El") = w1 * V₂("El") + w2 * V₂("gato") + w3 * V₂("duerme")
```

Resultado → nuevo vector, diferente al de la Cabeza 1.

---

## 🔄 Fusión de cabezas

Al final:

```python
output_final("El") = concat(salida₁("El"), salida₂("El"))
```

Si cada salida es de tamaño 2, el resultado concatenado será de tamaño 4.

Luego, se suele aplicar una capa lineal (una nueva matriz) para combinar esa información. Pero en este ejemplo, puedes dejarlo así para visualizar que:

* Cada cabeza **mira diferente**.
* El resultado final **combina ambas perspectivas**.

---

### 📌 Conclusión

Con dos cabezas:

* Cada una tiene **sus propios pesos** (`Wq`, `Wk`, `Wv`).
* Cada una **atiende** a diferentes palabras.
* Se combinan para crear una representación más **rica y completa**.

---

## Estructura de la cabeza de atención

A nivel más técnico, **una cabeza de atención** en un Transformer es un submódulo autónomo que aplica el mecanismo de atención escalada (*scaled dot-product attention*) con sus propios parámetros. Se puede ver como una función matemática que toma tensores de entrada y genera una representación contextualizada de la misma dimensión de salida.

---

### ⚙️ Estructura interna de una cabeza de atención

#### 📥 Entrada

* Un tensor `X` ∈ ℝ<sup>seq_len × d_model</sup>, donde:
* `seq_len`: número de tokens (por ejemplo, palabras).
* `d_model`: dimensión del embedding (por ejemplo, 512 o 768).

#### 🧠 Parámetros de la cabeza

Tres matrices de pesos entrenables:

* `W_Q` ∈ ℝ<sup>d_model × d_k</sup>
* `W_K` ∈ ℝ<sup>d_model × d_k</sup>
* `W_V` ∈ ℝ<sup>d_model × d_v</sup>

> En Transformers típicos, `d_k = d_v = d_model / num_heads`.

---

### 📊 Pasos de procesamiento

1. **Proyección lineal:**

   * `Q = X × W_Q` → consultas (*queries*)
   * `K = X × W_K` → claves (*keys*)
   * `V = X × W_V` → valores (*values*)
   * Cada uno queda con forma `ℝ<sup>seq_len × d_k</sup>` o `d_v`.

2. **Cálculo de los scores (compatibilidad entre tokens):**

   $$
   \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right)V
   $$

   * `Q × Kᵀ` genera una matriz de atención ∈ ℝ<sup>seq_len × seq_len</sup>.
   * Se escala por `√d_k` para evitar que los valores crezcan demasiado.
   * Se aplica **softmax por fila** para obtener pesos de atención.
   * La multiplicación final con `V` da como resultado la salida contextual.

---

### 🧾 Salida

* Tensor ∈ ℝ<sup>seq_len × d_v</sup>, que representa la información contextualizada para cada token, vista por esta cabeza.

---

### 🧠 Multi-Head Attention en contexto

En la **atención multicabeza**, se ejecutan `h` cabezas en paralelo con diferentes `W_Q`, `W_K`, `W_V`, y sus salidas se concatenan:

$$
\text{MultiHead}(X) = \text{Concat}(\text{head}_1, ..., \text{head}_h) × W_O
$$

donde `W_O` ∈ ℝ<sup>(h × d_v) × d_model</sup> es otra matriz entrenable.

---

### ✅ Ventajas de dividir en varias cabezas

* Permite al modelo **capturar diferentes tipos de relaciones** entre tokens.
* Las distintas cabezas se especializan automáticamente en diferentes aspectos: sintaxis, semántica o dependencias largas.

---
