---
title: "Transformers 5: Atención Encoder-Decoder"
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

# Atención Encoder-Decoder (Cross-Attention)

## 🔗 Introducción

La atención encoder-decoder, también llamada **cross-attention**, es una parte esencial del decodificador de un modelo Transformer. Es el mecanismo que permite que el decodificador utilice la información de la secuencia de entrada (procesada por el encoder) mientras genera la salida paso a paso.

---

## 🤔 ¿Para qué sirve?

Mientras que la *self-attention* del decodificador solo mira palabras ya generadas, la *cross-attention* le permite al modelo acceder al contexto completo de la entrada. Es decir, cuando el modelo está generando una palabra de salida, puede fijarse en cualquier parte de la frase de entrada.

Ejemplo:

```
Entrada: "El gato duerme"
Salida generada: "The cat sleeps"
```

Para generar "cat", el modelo puede fijarse en "gato" (entrada). Para generar "sleeps", puede mirar "duerme".

---

## 🔀 Diferencia clave: Self-Attention vs. Cross-Attention

### Self-Attention

* Q, K, V se calculan a partir de la **misma secuencia**.
* Se usa tanto en el encoder como en el decoder.

### Cross-Attention (encoder-decoder attention)

* Q se calcula a partir de la salida del **decoder** (tokens generados hasta ese punto).
* K y V se calculan a partir de la salida del **encoder** (la representación completa de la entrada).

### ¿Qué significan aquí Q, K y V?

En la *cross-attention*, estos vectores mantienen la misma idea general:

* **Q (Query)**: representa lo que el decodificador necesita en este paso de generación.
* **K (Key)**: representa cómo está indexada la información de la salida del encoder.
* **V (Value)**: contiene la información contextual del encoder que puede recuperarse.

Por eso el decoder usa sus **Q** para consultar las **K** del encoder y recuperar, a través de los **V**, la parte de la entrada más útil en ese momento.

📌 En términos de tensores:

```
Q = decoder_output × Wq
K = encoder_output × Wk
V = encoder_output × Wv
```

Entonces:

```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) × V
```

Esto permite que, en cada paso de generación, el decodificador consulte el encoder y sepa **qué partes de la entrada son relevantes** para producir la siguiente palabra.

---

## 🌟 Ejemplo simple

Supongamos que el encoder ya procesó la entrada "El gato duerme" y produjo 3 vectores de salida (uno por palabra). Cuando el decodificador quiere generar la primera palabra de salida:

* Calcula su Q (de su estado interno).
* Aplica atención sobre los K y V del encoder.
* Decide a qué palabra del input prestar más atención.

Este proceso se repite en cada paso de generación.

---

## 🔹 Resumen

* Cross-attention permite que el decoder acceda al contexto completo del input.
* Se diferencia de self-attention en que **Q viene del decoder, y K/V del encoder**.
* Es crucial para tareas como traducción, resumen o generación condicional.

---

📍 **Próximo paso sugerido:** visualizar cómo varía la atención encoder-decoder en distintas fases de generación de texto.
