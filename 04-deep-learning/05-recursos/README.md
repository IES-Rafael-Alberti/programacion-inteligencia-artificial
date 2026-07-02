# UD4 — Redes Neuronales: Fundamentos, Práctica y Modelado Avanzado

Módulo de **Programación de Inteligencia Artificial** — IES Rafael Alberti 2025/26.

---

## Estructura general

```
UD4/
├── 01-teoria/            Teoría organizada por bloques
├── 02-ejemplos/          Ejemplos, notebooks y scripts
├── 03-practicas/         Laboratorios y tareas
├── 04-evaluacion/        Rúbrica, checklist y cuestionario
└── 05-recursos/          Recursos complementarios
```

---

## Bloques

### 01 · Fundamentos ([`01-redes-neuronales-genericas/`](../01-teoria/01-redes-neuronales-genericas/))

Teoría completa de deep learning desde cero:
- Capítulos 01–08: introducción, perceptrones, activaciones, pérdida, optimización, backpropagation, regularización, hiperparámetros
- Scripts de generación de imágenes y animaciones
- Notebooks de visualización del gradiente y fundamentos visuales

### 02 · Frameworks ([`frameworks/`](../02-ejemplos/frameworks/))

Implementación de redes neuronales con los tres frameworks principales:
- Keras: clasificación binaria y multiclase (FashionMNIST)
- PyTorch: mismo problema, training loop manual
- JAX: enfoque funcional, Equinox
- Optimizadores comparados en los tres frameworks

### 03 · Laboratorios ([`laboratorios/`](../03-practicas/laboratorios/))

Laboratorios evaluables con enunciado, rúbrica y plantilla de entrega:

| Lab | Título | Materiales |
|-----|--------|------------|
| 1 | TF Playground — exploración visual de redes | enunciado, rúbrica, notebook |
| 2 | Backpropagation desde cero | enunciado, rúbrica, scripts Python |
| 3 | De Playground a código real | enunciado, rúbrica |

### 04 · Modelado avanzado ([`02-redes-neuronales-vision/`](../01-teoria/02-redes-neuronales-vision/) y [`03-redes-neuronales-nlp/`](../01-teoria/03-redes-neuronales-nlp/))

Módulo extenso con temas avanzados y proyectos reales:
- **Vision**: CNN, detección de objetos (YOLO, Faster R-CNN), segmentación de tumores
- **NLP**: embeddings, Transformers (teoría + notebooks + tareas)
- **Proyectos**: Boston Housing, House Prices (Kaggle), Used Cars, Euromillones
- **Docs**: frameworks, conceptos, métricas, teoría, libros (15+ PDFs)
- **Tareas** evaluables, **entornos** conda/pip

---

## Progresión pedagógica

```
01-teoria  →  02-ejemplos/frameworks  →  03-practicas/laboratorios  →  bloques de visión/NLP
   (teoría)          (código)          (evaluación)          (profundización)
```
