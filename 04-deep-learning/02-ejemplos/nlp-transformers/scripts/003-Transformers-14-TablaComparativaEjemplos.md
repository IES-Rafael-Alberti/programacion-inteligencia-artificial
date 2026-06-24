---
title: "Transformers 14: Tabla Comparativa de Ejemplos"
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


# Tabla Comparativa de los 4 Ejemplos

Esta tabla resume los cuatro ejemplos prácticos construidos a partir del tema de Transformers.

---

## 1. Comparativa general

| Ejemplo | Tarea | Arquitectura | Entrada | Salida | Idea principal |
| ------- | ----- | ------------ | ------- | ------ | -------------- |
| Transformers 10 | Traducción inglés-español | Encoder-decoder | Frase en inglés | Frase en español | Transformar una secuencia en otra |
| Transformers 11 | Generación de texto | Decoder-only | Prompt o comienzo de texto | Continuación del texto | Predecir el siguiente token |
| Transformers 12 | Reformulación | Encoder-decoder | Frase original | Frase reformulada | Expresar lo mismo de otra forma |
| Transformers 13 | Clasificación | Encoder-only | Frase | Etiqueta | Comprender el texto y asignar una categoría |

---

## 2. Qué bloques usa cada uno

| Ejemplo | Encoder | Decoder | Cross-attention | Máscara causal | Capa de clasificación |
| ------- | ------- | ------- | --------------- | -------------- | --------------------- |
| Transformers 10 | Sí | Sí | Sí | Sí, en el decoder | No |
| Transformers 11 | No | Sí | No | Sí | No |
| Transformers 12 | Sí | Sí | Sí | Sí, en el decoder | No |
| Transformers 13 | Sí | No | No | No | Sí |

---

## 3. Tipo de datos que necesita cada uno

| Ejemplo | Tipo de dataset | Formato básico |
| ------- | --------------- | -------------- |
| Transformers 10 | Dataset paralelo | `entrada -> salida` en idiomas distintos |
| Transformers 11 | Texto continuo | una sola secuencia larga |
| Transformers 12 | Dataset de paráfrasis | `entrada -> salida` en el mismo idioma |
| Transformers 13 | Dataset etiquetado | `texto -> clase` |

---

## 4. Qué aprende el modelo en cada caso

| Ejemplo | Qué aprende |
| ------- | ----------- |
| Transformers 10 | A generar una traducción condicionada por la frase de entrada |
| Transformers 11 | A continuar una secuencia generando el siguiente token |
| Transformers 12 | A producir una reformulación manteniendo el significado |
| Transformers 13 | A construir una representación del texto y clasificarla |

---

## 5. Qué se quiere enseñar con cada ejemplo

| Ejemplo | Punto didáctico principal |
| ------- | ------------------------- |
| Transformers 10 | Cuándo usar el Transformer completo para tareas seq2seq |
| Transformers 11 | Por qué la generación libre suele usar decoder-only |
| Transformers 12 | Que el encoder-decoder no solo sirve para traducción |
| Transformers 13 | Que un Transformer también puede usarse solo para comprender y clasificar |

---

## 6. Regla práctica final

| Si la tarea es... | La arquitectura más natural suele ser... |
| ----------------- | ---------------------------------------- |
| transformar una secuencia en otra | encoder-decoder |
| continuar texto | decoder-only |
| clasificar o comprender un texto | encoder-only |

---

## 7. Idea final

Los cuatro ejemplos no son solo cuatro scripts distintos. En conjunto, sirven para entender una idea más importante:

* la arquitectura no se elige por costumbre,
* se elige según el tipo de tarea.

Por eso, al diseñar un modelo, una de las primeras preguntas debe ser:

> ¿Quiero transformar una secuencia, generar texto o clasificar una entrada?

La respuesta a esa pregunta orienta directamente la elección entre:

* **Transformer completo**,
* **decoder-only**,
* o **encoder-only**.

---
