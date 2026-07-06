---
title: "Tarea Transformers PyTorch: Entrega y Criterios"
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


# Tarea Transformers PyTorch: Entrega y Criterios

## 1. Entregables

Debes entregar dos elementos:

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

## 2. Criterios de evaluación

La calificación se basará en estos criterios:

| Apartado | Puntuación |
| -------- | ---------- |
| Comprensión del script y localización correcta de bloques | 4 puntos |
| Explicación clara de embeddings, `Q/K/V`, máscaras, encoder y decoder | 3 puntos |
| Modificaciones realizadas y justificadas | 2 puntos |
| Claridad, orden y presentación | 1 punto |

---

## 3. Orientación para sacar buena nota

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
