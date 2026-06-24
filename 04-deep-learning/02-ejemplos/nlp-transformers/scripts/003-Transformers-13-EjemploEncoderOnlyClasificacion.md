---
title: "Transformers 13: Ejemplo de Encoder-Only para Clasificación"
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


# Ejemplo de Encoder-Only para Clasificación

Este ejemplo muestra el tercer gran uso didáctico de la familia Transformer:

* **encoder-only** para tareas de comprensión o clasificación.

En este caso, el modelo no genera otra secuencia ni continúa texto. Lo que hace es:

* leer una frase,
* construir una representación contextual,
* y asignarle una etiqueta.

---

## 1. Tipo de tarea

La tarea elegida es una clasificación sencilla de intención o tipo de enunciado.

Ejemplos:

* `quiero comprar un billete` -> `peticion`
* `gracias por tu ayuda` -> `agradecimiento`
* `que hora es` -> `pregunta`
* `hola buenos dias` -> `saludo`

Esto permite ver con claridad cuándo un Transformer no necesita decoder.

---

## 2. Archivos del ejemplo

Este ejemplo usa:

* Dataset:
  `mini_clasificacion_intenciones.tsv`

* Script independiente:
  `ejemplo_transformers_4_encoder_only_clasificacion.py`

No modifica `transformerPytorch.py`. Implementa una versión propia y más adecuada para clasificación.

---

## 3. ¿Qué cambia respecto al Transformer completo?

Aquí desaparecen varias piezas:

* no hay decoder,
* no hay cross-attention,
* no hay generación token a token.

Solo se conserva:

* embedding,
* codificación posicional,
* pila de capas de encoder,
* y una capa final de clasificación.

---

## 4. Flujo del modelo

El flujo general es:

1. la frase entra tokenizada,
2. pasa por embeddings,
3. se añade codificación posicional,
4. atraviesa varias capas de encoder,
5. se obtiene una representación global,
6. esa representación se pasa a una capa lineal,
7. se predice una etiqueta.

---

## 5. ¿Cómo se obtiene una representación global?

En este ejemplo se usa una solución sencilla:

* calcular la media de las representaciones de los tokens válidos.

Es decir:

* el encoder produce una representación contextualizada para cada palabra,
* luego esas representaciones se agregan,
* y el resultado se usa para clasificar.

Es una solución simple y muy útil para fines docentes.

---

## 6. Qué enseña este ejemplo

Este caso sirve para mostrar que un Transformer no tiene por qué generar texto.

También puede utilizarse para:

* clasificación,
* detección de intención,
* análisis de sentimiento,
* clasificación temática,
* reconocimiento de categorías.

---

## 7. Comparación con los otros ejemplos

### Traducción

* arquitectura: encoder-decoder
* tarea: secuencia -> secuencia

### Generación libre

* arquitectura: decoder-only
* tarea: continuar texto

### Clasificación

* arquitectura: encoder-only
* tarea: texto -> etiqueta

Esta comparación completa el mapa básico de usos de la arquitectura Transformer.

---

## 8. Idea final

Con este ejemplo ya quedan cubiertos los tres casos principales:

* **Transformer completo**: cuando hay una secuencia de entrada y otra de salida.
* **Decoder-only**: cuando queremos generar texto.
* **Encoder-only**: cuando queremos entender un texto y clasificarlo.

Esa es una de las distinciones más importantes para decidir qué arquitectura usar según la tarea.

---
