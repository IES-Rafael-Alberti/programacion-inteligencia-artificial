---
title: "Tarea: Análisis y Modificación de un Transformer en PyTorch"
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


# Tarea: Análisis y Modificación de un Transformer en PyTorch

## 1. Objetivo

El objetivo de esta tarea es comprender cómo se implementa un modelo Transformer en PyTorch y analizar cómo afectan pequeños cambios a su comportamiento.

No se busca entrenar un gran modelo ni generar texto perfecto, sino:

* entender la arquitectura,
* identificar sus bloques principales,
* modificar el código de forma razonada,
* y explicar con claridad qué hace cada parte.

---

## 2. Material de partida

El trabajo se realizará a partir del script:

`transformerPytorch.py`

Puede ayudarte también el documento:

`003-Transformers-Anexo-LecturaGuiada-PyTorch.md`

---

## 3. Tarea

Debes realizar las siguientes actividades.

### Parte 1. Análisis del script

Explica con tus palabras qué hace el script y qué tipo de Transformer implementa.

Debes identificar en el código dónde aparecen estos elementos:

* embeddings
* codificación posicional
* `Q`, `K` y `V`
* atención escalada
* atención multicabeza
* encoder
* decoder
* máscaras
* capa final de salida

Además, debes explicar brevemente qué función cumple cada uno de estos bloques.

---

### Parte 2. Modificación del script

Debes realizar **dos modificaciones** sobre el script y explicar por qué las has elegido.

Puedes escoger entre estas opciones:

* cambiar `num_heads`
* cambiar `d_model`
* cambiar `d_ff`
* sustituir `ReLU` por `GELU`
* quitar temporalmente la máscara causal del decoder y explicar qué problema aparece
* hacer que la atención devuelva también los pesos de atención
* mostrar por pantalla la forma de algunos tensores importantes
* añadir comentarios aclaratorios al código
* explicar qué ocurriría si se eliminara la codificación posicional

También puedes proponer una modificación propia, siempre que tenga sentido y esté bien explicada.

---

### Parte 3. Análisis de efectos

Después de realizar las modificaciones, debes indicar:

* qué esperabas que ocurriera,
* qué ha ocurrido realmente, si has podido probarlo,
* o qué debería ocurrir según la teoría, si no has llegado a ejecutarlo.

No es obligatorio obtener un resultado espectacular. Lo importante es el razonamiento.

---

## 4. Entregables

Debes entregar:

### 1. Documento explicativo

Un archivo PDF o Markdown breve que incluya:

* explicación general del script,
* localización de los bloques principales,
* explicación de las dos modificaciones realizadas,
* análisis de los efectos observados o esperados.

Extensión orientativa:

* entre 2 y 4 páginas.

### 2. Script modificado

Debes entregar también el archivo Python modificado con el siguiente formato de nombre:

`apellido_nombre_transformer.py`

---

## 5. Recomendaciones

Para hacer bien la tarea:

* no intentes cambiar demasiadas cosas a la vez,
* haz modificaciones pequeñas pero bien razonadas,
* relaciona siempre el código con la teoría,
* y prioriza explicar bien lo que haces.

Es preferible una tarea sencilla y bien entendida que una muy ambiciosa pero mal explicada.

---

## 6. Criterios de evaluación

La calificación se basará en estos criterios:

| Apartado | Puntuación |
| -------- | ---------- |
| Comprensión del script y localización correcta de bloques | 4 puntos |
| Explicación clara de embeddings, `Q/K/V`, máscaras, encoder y decoder | 3 puntos |
| Modificaciones realizadas y justificadas | 2 puntos |
| Claridad, orden y presentación | 1 punto |

---

## 7. Orientación para sacar buena nota

Para obtener una buena calificación, conviene que:

* expliques el script con precisión,
* señales con claridad en qué líneas o bloques aparece cada componente,
* justifiques bien las modificaciones,
* y relaciones cada cambio con un efecto esperado.

Ejemplo:

* Si aumentas `num_heads`, explica que el modelo dividirá `d_model` en más cabezas y que cada cabeza tendrá menor dimensión individual.
* Si eliminas la máscara causal, explica por qué el decoder podría “ver el futuro”.
* Si cambias `d_ff`, explica cómo afecta a la capacidad de la red feed-forward.

---

## 8. Idea clave

En esta tarea no se evalúa si el modelo genera literatura de alta calidad, sino si comprendes:

* cómo está construido un Transformer,
* cómo se traduce la teoría a código,
* y cómo afectan los cambios de diseño a la arquitectura.

---
