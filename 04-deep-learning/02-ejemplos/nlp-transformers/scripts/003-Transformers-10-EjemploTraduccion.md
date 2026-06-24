---
title: "Transformers 10: Ejemplo Completo de Traducción Inglés-Español"
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


# Ejemplo Completo de Traducción Inglés-Español

Este ejemplo muestra cómo usar un **Transformer encoder-decoder** para una tarea de traducción:

* **entrada**: una frase en inglés,
* **salida**: su traducción al español.

No es un traductor realista de gran escala. Es un ejemplo pequeño y controlado para entender el flujo completo de una tarea seq2seq.

---

## 1. Archivos del ejemplo

El ejemplo usa estos archivos:

* Dataset base:  
  `mini_trad_es_en_ampliado.tsv`

* Script autosuficiente:  
  `ejemplo_transformers_1_traduccion_en_es.py`

El script **no modifica** ni depende del archivo original `transformerPytorch.py`. Implementa su propia versión compacta de la arquitectura.

---

## 2. Por qué este ejemplo usa el Transformer completo

La traducción es una tarea muy adecuada para un Transformer encoder-decoder porque:

* el **encoder** procesa la frase de entrada,
* el **decoder** genera una secuencia nueva,
* y la **cross-attention** conecta ambas.

Por eso este ejemplo sirve muy bien para mostrar cuándo tiene sentido usar el Transformer completo.

---

## 3. Cómo se reutiliza el dataset existente

El dataset disponible estaba pensado como:

* **español -> inglés**

Pero en este ejemplo queremos:

* **inglés -> español**

Por eso el script carga cada pareja y la invierte internamente:

* origen: inglés
* destino: español

De ese modo no hace falta crear un segundo fichero de datos.

---

## 4. Preparación de los datos

El flujo de preparación es este:

1. leer pares de frases,
2. tokenizar separando por espacios,
3. construir vocabulario origen y destino,
4. convertir palabras en índices,
5. preparar tres tensores:
   * `src`
   * `tgt_input`
   * `tgt_output`

### Ejemplo

Si la pareja es:

```text
good morning -> buenos dias
```

entonces:

```text
src        = [good, morning]
tgt_input  = [<sos>, buenos, dias]
tgt_output = [buenos, dias, <eos>]
```

---

## 5. Papel del DataLoader

En este ejemplo, el `DataLoader` solo hace tres cosas:

* agrupar muestras,
* rellenar con `<pad>` las secuencias más cortas,
* devolver batches listos para entrenar.

La función `collate_batch` usa:

```python
nn.utils.rnn.pad_sequence(...)
```

Es decir, aquí el `DataLoader` no tiene misterio: solo organiza y rellena.

---

## 6. Arquitectura usada

El script implementa:

* `MultiHeadAttention`
* `PositionWiseFeedForward`
* `PositionalEncoding`
* `EncoderLayer`
* `DecoderLayer`
* `Transformer`

Es una versión pequeña, pensada para clase:

* `d_model = 64`
* `num_heads = 4`
* `num_layers = 2`
* `d_ff = 128`

---

## 7. Entrenamiento

El entrenamiento sigue este esquema:

1. se carga un batch,
2. el modelo genera logits para la secuencia destino,
3. se compara con `tgt_output`,
4. se calcula la pérdida,
5. se actualizan los pesos.

La función de pérdida es:

```python
nn.CrossEntropyLoss(ignore_index=pad_id)
```

Eso evita que el padding cuente como error.

---

## 8. Inferencia

Para traducir una frase:

1. el encoder procesa la frase inglesa,
2. el decoder empieza con `<sos>`,
3. predice una palabra,
4. la añade a la salida parcial,
5. repite hasta llegar a `<eos>`.

En este ejemplo se usa `greedy decoding`, es decir:

* en cada paso se elige el token más probable.

Es la opción más sencilla para fines didácticos.

---

## 9. Qué enseña bien este ejemplo

Este ejemplo permite mostrar:

* cómo preparar un dataset paralelo,
* cómo construir `src`, `tgt_input` y `tgt_output`,
* cuándo usar encoder-decoder,
* cómo entrenar un modelo seq2seq,
* cómo traducir paso a paso.

---

## 10. Sobre traducir en ambos sentidos

Si se quisiera traducir también:

* **español -> inglés**

hay varias posibilidades:

### Opción 1

Entrenar un segundo modelo para el sentido inverso.

### Opción 2

Entrenar un solo modelo con ambas direcciones, usando un token que indique el idioma de destino.

Por ejemplo:

```text
<2es> good morning
<2en> buenos dias
```

Para clase, la opción más simple es entrenar primero un único sentido.

---

## 11. Limitaciones del ejemplo

Este ejemplo:

* usa un corpus pequeño,
* no pretende producir traducciones perfectas,
* no usa tokenización subword,
* no está optimizado para producción.

Su valor está en que permite entender muy bien **cómo usar el Transformer completo cuando la tarea requiere transformar una secuencia en otra**.

---

## 12. Idea final

Este ejemplo es un buen punto de partida antes de pasar a otro caso distinto:

* **traducción** -> Transformer completo,
* **generación libre de texto** -> normalmente decoder-only.

Ese contraste ayuda a entender por qué no siempre se usa la misma arquitectura para todas las tareas.

---
