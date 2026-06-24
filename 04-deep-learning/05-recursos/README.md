# UD4 — Redes Neuronales: Fundamentos, Práctica y Modelado Avanzado

Módulo de **Programación de Inteligencia Artificial** — IES Rafael Alberti 2025/26.

---

## Estructura general

```
UD4/
├── 01-fundamentos/       Teoría de redes neuronales (8 capítulos)
├── 02-frameworks/        Práctica con Keras, PyTorch y JAX
├── 03-laboratorios/      Laboratorios guiados con rúbricas y entregas
├── 04-modelado-avanzado/ CNN, NLP, Transformers, proyectos reales
└── trabajo_documentacion.md  Notas de progreso docente
```

---

## Bloques

### 01 · Fundamentos ([`01-fundamentos/`](01-fundamentos/README.md))

Teoría completa de deep learning desde cero:
- Capítulos 01–08: introducción, perceptrones, activaciones, pérdida, optimización, backpropagation, regularización, hiperparámetros
- Scripts de generación de imágenes y animaciones
- Notebooks de visualización del gradiente y fundamentos visuales

### 02 · Frameworks ([`02-frameworks/`](02-frameworks/README.md))

Implementación de redes neuronales con los tres frameworks principales:
- Keras: clasificación binaria y multiclase (FashionMNIST)
- PyTorch: mismo problema, training loop manual
- JAX: enfoque funcional, Equinox
- Optimizadores comparados en los tres frameworks

### 03 · Laboratorios ([`03-laboratorios/`](03-laboratorios/README.md))

Laboratorios evaluables con enunciado, rúbrica y plantilla de entrega:

| Lab | Título | Materiales |
|-----|--------|------------|
| 1 | TF Playground — exploración visual de redes | enunciado, rúbrica, notebook |
| 2 | Backpropagation desde cero | enunciado, rúbrica, scripts Python |
| 3 | De Playground a código real | enunciado, rúbrica |

### 04 · Modelado Avanzado ([`04-modelado-avanzado/`](04-modelado-avanzado/README.md))

Módulo extenso con temas avanzados y proyectos reales:
- **Vision**: CNN, detección de objetos (YOLO, Faster R-CNN), segmentación de tumores
- **NLP**: embeddings, Transformers (teoría + notebooks + tareas)
- **Proyectos**: Boston Housing, House Prices (Kaggle), Used Cars, Euromillones
- **Docs**: frameworks, conceptos, métricas, teoría, libros (15+ PDFs)
- **Tareas** evaluables, **entornos** conda/pip

---

## Progresión pedagógica

```
01-fundamentos  →  02-frameworks  →  03-laboratorios  →  04-modelado-avanzado
   (teoría)          (código)          (evaluación)          (profundización)
```

---

## Notas de trabajo

Ver [`trabajo_documentacion.md`](trabajo_documentacion.md) para el registro de decisiones
de contenido, pendientes de notebooks y notas de consistencia de nombres.
