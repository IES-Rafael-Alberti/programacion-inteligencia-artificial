# 10-series-temporales

## Propósito
Cubre análisis y forecasting de series temporales: desde introducción y procesamiento hasta deep learning (TCN, Transformers) y proyecto final.

## Ruta canónica del alumnado

| Paso | Material |
|---|---|
| Empieza aquí | [`01-teoria/01_introduccion_series_temporales.md`](01-teoria/01_introduccion_series_temporales.md) y los notebooks progresivos `01`–`09` de `02-ejemplos/`. |
| Tarea canónica | Proyecto final descrito en [`01-teoria/10_proyecto_final.md`](01-teoria/10_proyecto_final.md), trabajado sobre `02-ejemplos/10_proyecto_final.ipynb`. |
| Entrega y evaluación | Notebook final ejecutado, tabla del Torneo, visualización y análisis de resultados, según [`04-evaluacion/rubrica.md`](04-evaluacion/rubrica.md) y [`04-evaluacion/checklist-entrega.md`](04-evaluacion/checklist-entrega.md). |
| Entorno real | [`01-teoria/requirements.txt`](01-teoria/requirements.txt) es la fuente de dependencias del taller. Esta unidad no tiene todavía un entorno Pixi propio en el manifiesto raíz. |

## Materiales incluidos
- **Material reorganizado desde UD4**: notebooks de series temporales procedentes de deep learning se han movido a `03-practicas/modelado-notebooks-series-ud4/`.
- **01-teoria**: Guías MD, PDFs, presentaciones (slides HTML+PDF+MD) de los 10 temas + seguimiento del taller
- **02-ejemplos**: Notebooks Jupyter de los 10 temas (introducción, procesamiento, análisis, baselines, regresión, feature engineering, DL, TCN, Transformers, proyecto)
- **03-practicas**: Scripts Python (generación de datos, creación de notebooks) y código fuente del paquete `series_temporales`
- **05-recursos**: Datasets (consumo eléctrico, clima, tráfico peatonal, ventas) + checkpoints de modelos (lightning_logs)

## Prácticas asociadas
- Taller completo de series temporales (10 notebooks progresivos)

## Opciones docentes

- Los notebooks `01`–`09` pueden usarse como trabajo guiado o refuerzo. El enunciado y la evaluación formalizados de la ruta ordinaria corresponden al proyecto final.
