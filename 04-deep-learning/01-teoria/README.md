# UD4 · Teoría de Deep Learning base

Esta carpeta contiene la teoría que permanece en UD4 tras separar visión, NLP y series temporales hacia sus unidades naturales.

## Frontera de UD4

UD4 cubre:

- fundamentos de redes neuronales;
- tensores, activaciones y funciones de pérdida;
- gradiente descendente y backpropagation;
- frameworks base de deep learning;
- métricas y generalización;
- material de modelado avanzado sólo cuando refuerza el núcleo de deep learning;
- una introducción conceptual breve a RNN/LSTM como puente hacia UD6 y UD10.

No cubre ya como bloque activo:

- visión aplicada, YOLO, transfer learning y datasets de imagen: `08-vision-xai/`;
- NLP, embeddings, transformers, BERT y spaCy: `06-llm-agentes/`;
- series temporales: `10-series-temporales/`.

## Estructura actual

```text
01-teoria/
├── 01-fundamentos-redes-neuronales/
│   ├── Parte-I-Fundamentos/
│   └── Parte-II-RedesEspecializadas/
├── 02-frameworks-deep-learning/
├── 03-metricas-evaluacion/
└── README.md
```

## Nota de limpieza

Los `.html` generados se han eliminado de UD4 cuando existía fuente Markdown equivalente. La referencia activa debe ser Markdown, notebook o código fuente, no HTML derivado. El antiguo `modelado-avanzado-docs/` queda cerrado y archivado en `04-deep-learning/90-archivo/modelado-avanzado-docs/`.
