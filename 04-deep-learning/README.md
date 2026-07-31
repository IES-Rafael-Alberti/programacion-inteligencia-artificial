# 04 - Deep Learning

## Propósito

Unidad dedicada al **deep learning base**: fundamentos de redes neuronales, entrenamiento, backpropagation, gradiente descendente, funciones de pérdida, métricas y frameworks principales.

Tras la reorganización, UD4 deja de ser el contenedor de visión y NLP aplicados. Ese material se ha movido a sus unidades naturales:

- visión, CNN aplicada, transfer learning, YOLO y datasets de imagen → `08-vision-xai/`;
- NLP, embeddings, transformers, BERT y spaCy → `06-llm-agentes/`;
- prácticas/notebooks de series temporales → `10-series-temporales/`.

## Ruta recomendada

1. Empieza por el [índice de teoría](01-teoria/README.md).
2. Realiza los [tres laboratorios canónicos](03-practicas/laboratorios/README.md) en orden.
3. Consulta la [evaluación](04-evaluacion/README.md) antes de preparar la entrega.

Para la ruta PyTorch local, usa el entorno `ud4` definido en el `pixi.toml` de la raíz:

```bash
pixi install --environment ud4
pixi run --environment ud4 jupyter lab
```

TensorFlow Playground se usa en el navegador y no requiere instalación. Keras, JAX y otras variantes son material complementario: usa su receta especializada sólo cuando la actividad o el profesorado la indiquen; no son rutas paralelas por defecto.

## Materiales incluidos

- **Teoría (`01-teoria/`)**: fundamentos generales de redes neuronales, frameworks, métricas y modelado avanzado estrictamente relacionado con deep learning base.
- **Ejemplos (`02-ejemplos/`)**: notebooks y scripts de fundamentos, frameworks y ejemplos introductorios.
- **Prácticas (`03-practicas/`)**: laboratorios de TensorFlow Playground, backpropagation y transición de conceptos a código real, además de proyectos opcionales documentados por separado.
- **Evaluación (`04-evaluacion/`)**: rúbricas, checklist y cuestionario GIFT consolidados para la frontera actual de UD4.
- **Recursos (`05-recursos/`)**: datos y entornos asociados a modelado y frameworks de deep learning.
- **Archivo (`90-archivo/`)**: material histórico o no activo.

## Prácticas asociadas

- Laboratorio 1: TensorFlow Playground.
- Laboratorio 2: implementación de backpropagation desde cero.
- Laboratorio 3: de Playground a código real.
- Proyectos de modelado opcionales, fuera del itinerario canónico salvo indicación docente.

## Documentos de reorganización

- [`00-inventario.md`](00-inventario.md): inventario de situación previo a la reorganización.
- [`00-decisiones-reorganizacion.md`](00-decisiones-reorganizacion.md): tabla de decisiones y registro de movimientos.
