# Visión por Computadora y XAI

## Estructura de la unidad

La unidad se organiza en tres bloques temáticos, cada uno con una semana de trabajo:

### Semana 22 — Segmentación de Imágenes
- Diferencias entre clasificación, detección y segmentación
- U-Net: arquitectura encoder-decoder para segmentación semántica
- Mask R-CNN: segmentación de instancias con PyTorch
- Métricas: IoU (Intersection over Union) y Dice Score

### Semana 23 — Tracking de Objetos
- Detección vs seguimiento en vídeo
- YOLOv8 en modo tracking
- Algoritmo SORT (Simple Online and Realtime Tracking)
- Métricas: MOTA (Multiple Object Tracking Accuracy) y MOTP (Multiple Object Tracking Precision)

### Semana 24 — Explicabilidad (XAI)
- Conceptos de caja blanca vs caja negra
- LIME: explicaciones locales agnósticas al modelo
- SHAP: valores de Shapley para importancia de variables
- Grad-CAM: mapas de activación en CNNs

## Notebooks asociados

| Semana | Notebooks | Tema |
|---|---|---|
| 22 | 78, 79, 80 | U-Net, Mask R-CNN, métricas segmentación |
| 23 | 81, 82, 83 | YOLOv8 tracking, SORT, métricas tracking |
| 24 | 84, 85, 86 | LIME, SHAP, Grad-CAM |

## RA/CE trabajados
- **RA2.c**: Definición de arquitecturas de segmentación, tracking y XAI
- **RA2.d**: Implementación práctica con Keras, PyTorch y librerías específicas
- **RA2.e**: Evaluación con métricas estándar (IoU, Dice, MOTA, MOTP)
- **RA3.a**: Identificación de ventajas de integrar explicabilidad en sistemas de IA
