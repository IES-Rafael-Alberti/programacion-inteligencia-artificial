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

## Relación con prácticas y notebooks

La evaluación se apoya en las prácticas de `08-vision-xai/03-practicas/`:

**Segmentación (notebooks 78-80):**
- `78_unet_segmentation.ipynb`: segmentación semántica con U-Net
- `79_maskrcnn_instances.ipynb`: segmentación de instancias con Mask R-CNN
- `80_metrics_segmentation.ipynb`: cálculo de IoU y Dice Score

**Tracking (notebooks 81-83):**
- `81_yolov8_tracking.ipynb`: tracking con YOLOv8
- `82_sort_tracking.ipynb`: algoritmo SORT
- `83_metrics_tracking.ipynb`: métricas MOTA y MOTP

**XAI (notebooks 84-86):**
- `84_lime_text.ipynb`: explicaciones locales con LIME
- `85_shap_tabular.ipynb`: importancia de variables con SHAP
- `86_gradcam_cnn.ipynb`: mapas de activación Grad-CAM en CNNs

El profesorado puede seleccionar uno o varios bloques como entrega evaluable. No es obligatorio entregar los tres bloques en la misma entrega salvo que el enunciado lo indique.

## Cuestionario disponible

- `cuestionario-vision-xai.gift`: preguntas de comprensión sobre segmentación, tracking y XAI.

Sirve para comprobar comprensión conceptual y preparar la corrección. No sustituye automáticamente a la rúbrica práctica salvo decisión expresa del profesorado.

## Criterios de superación

- La entrega alcanza al menos 5 sobre 10 en la rúbrica.
- Los notebooks ejecutan el flujo principal con evidencias verificables.
- Las métricas calculadas son coherentes con los datos y el código.
- La solución está suficientemente documentada para que otra persona pueda revisarla.
