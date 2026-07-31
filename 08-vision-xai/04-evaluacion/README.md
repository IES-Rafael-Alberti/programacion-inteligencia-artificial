# Evaluación — UD8 Visión por Computadora y XAI

Esta carpeta reúne los instrumentos para evaluar la unidad de segmentación de imágenes, tracking de objetos y explicabilidad de modelos (XAI). El cuestionario GIFT cubre comprensión teórica; la entrega principal debe evidenciar una implementación práctica correcta con métricas y visualizaciones.

## Camino rápido

1. Completa los notebooks indicados por el profesorado (segmentación, tracking o XAI).
2. Entrega el código, notebooks y evidencias siguiendo `checklist-entrega.md`.
3. Revisa la calificación esperada con `rubrica.md`.
4. Realiza el cuestionario GIFT si el profesorado lo activa en Moodle.

## Qué se evalúa

| Bloque | Evidencia esperada |
| --- | --- |
| Funcionamiento e implementación | Notebook ejecutado sin errores críticos, con salidas que muestren los resultados obtenidos. |
| Métricas cuantitativas | Cálculo correcto de IoU/Dice (segmentación), MOTA/MOTP (tracking) o importancias/gradientes (XAI). |
| Visualizaciones | Máscaras, bounding boxes, heat maps o gráficas de importancia que permitan revisar los resultados visualmente. |
| Análisis e interpretación | Breve comentario sobre los resultados obtenidos: qué funciona bien, qué falla y por qué. |
| Documentación y reproducibilidad | Instrucciones claras, entorno declarado y estructura suficiente para reproducir la solución. |

## Evidencias de entrega

- Notebooks completados con salidas visibles o instrucciones para reproducirlas.
- Al menos una visualización relevante por bloque evaluado (máscara, traza de tracking o mapa XAI).
- Tabla o texto con las métricas calculadas y un breve comentario interpretativo.
- Instrucciones de ejecución o dependencias si son necesarias para reproducir el entorno.

No se deben entregar claves API, tokens, credenciales ni datos sensibles.

## Relación con ejemplos y prácticas

El profesorado seleccionará uno o varios bloques. La ruta canónica parte siempre de los notebooks base, no de las versiones `*_SOLUCIONES*`:

| Bloque | Ubicación | Material base |
| --- | --- | --- |
| Segmentación | [`../02-ejemplos/`](../02-ejemplos/) | [`78_unet_segmentation.ipynb`](../02-ejemplos/78_unet_segmentation.ipynb), [`79_maskrcnn_pytorch.ipynb`](../02-ejemplos/79_maskrcnn_pytorch.ipynb) y [`80_metrics_segmentation.ipynb`](../02-ejemplos/80_metrics_segmentation.ipynb) |
| Tracking | [`../03-practicas/`](../03-practicas/) | [`81_yolov8_tracking.ipynb`](../03-practicas/81_yolov8_tracking.ipynb), [`82_sort_tracking.ipynb`](../03-practicas/82_sort_tracking.ipynb) y [`83_metrics_tracking.ipynb`](../03-practicas/83_metrics_tracking.ipynb) |
| XAI | [`../03-practicas/`](../03-practicas/) | [`84_lime_text.ipynb`](../03-practicas/84_lime_text.ipynb), [`85_shap_tabular.ipynb`](../03-practicas/85_shap_tabular.ipynb) y [`86_gradcam_cnn.ipynb`](../03-practicas/86_gradcam_cnn.ipynb) |

El profesorado puede seleccionar uno o varios bloques como entrega evaluable. No es obligatorio entregar los tres bloques en la misma entrega salvo que el enunciado lo indique.

Antes de entregar, comprueba las evidencias en [`checklist-entrega.md`](checklist-entrega.md) y contrasta el resultado con [`rubrica.md`](rubrica.md).

## Cuestionario disponible

- `cuestionario-vision-xai.gift`: preguntas de comprensión sobre segmentación, tracking y XAI.

Sirve para comprobar comprensión conceptual y preparar la corrección. No sustituye automáticamente a la rúbrica práctica salvo decisión expresa del profesorado.

## Criterios de superación

- La entrega alcanza al menos 5 sobre 10 en la rúbrica.
- Los notebooks ejecutan el flujo principal con evidencias verificables.
- Las métricas calculadas son coherentes con los datos y el código.
- La solución está suficientemente documentada para que otra persona pueda revisarla.
