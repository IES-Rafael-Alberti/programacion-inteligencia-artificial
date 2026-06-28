# Tracking de Objetos: YOLOv8 y SORT

## De la detección al seguimiento

La detección de objetos actúa sobre fotogramas individuales (frames). El **tracking** añade una dimensión temporal: debe mantener la identidad de cada objeto a lo largo de la secuencia de vídeo.

Problemas comunes del tracking:
- **Oclusiones**: un objeto queda tapado por otro y se pierde su ID.
- **ID switches**: el mismo objeto recibe IDs diferentes tras una oclusión.
- **Pérdida de objeto**: el tracker deja de seguir un objeto que sale del campo de visión o cambia drásticamente de apariencia.

## YOLOv8 en modo tracking

YOLOv8 (Ultralytics) incorpora tracking integrado mediante el método `track()`. Internamente combina:

1. **Detección frame a frame** con YOLOv8.
2. **Asignación de identidades** mediante un algoritmo de tracking ligero (BoT-SORT o ByteTrack según la configuración).

El flujo es:
- Se procesa cada frame con YOLOv8 para obtener detecciones.
- Se comparan las detecciones actuales con las trayectorias activas.
- Se asignan IDs basándose en solapamiento (IoU) entre detecciones consecutivas.
- Los objetos nuevos reciben un ID nuevo; los que desaparecen se dan de baja.

## Algoritmo SORT

SORT (Simple Online and Realtime Tracking) es un algoritmo de tracking ligero y eficiente:

1. **Estado del objeto**: se modela cada objeto con su posición, velocidad y tamaño (filtro de Kalman).
2. **Predicción**: el filtro de Kalman predice dónde estará cada objeto en el siguiente frame.
3. **Asociación**: se calcula la matriz de costes (IoU) entre detecciones y predicciones, y se resuelve con el algoritmo húngaro para maximizar la asignación.
4. **Actualización**: las detecciones asignadas actualizan el filtro de Kalman.
5. **Gestión de nacimiento/muerte**: detecciones no asignadas crean nuevos objetos; predicciones no asignadas durante varios frames se descartan.

SORT asume velocidad constante entre frames. Es rápido pero sensible a oclusiones prolongadas.

## Métricas de tracking

### MOTA (Multiple Object Tracking Accuracy)

Mide errores combinados:

$$MOTA = 1 - \frac{FN + FP + IDSW}{GT}$$

Donde:
- **FN**: falsos negativos (objetos no detectados)
- **FP**: falsos positivos (detecciones fantasmas)
- **IDSW**: cambios de ID (identity switches)
- **GT**: número total de ground truth

MOTA puede ser negativo si los errores superan el número de objetos reales.

### MOTP (Multiple Object Tracking Precision)

Mide la precisión en la localización:

$$MOTP = \frac{\sum d}{TP}$$

Donde **d** es la distancia entre la posición predicha y la real (normalmente IoU o distancia euclídea) para todas las correspondencias correctas (**TP**).

MOTA mide si estás siguiendo a los objetos correctos; MOTP mide qué bien los estás localizando.

## Referencias

- [Ultralytics YOLOv8 Docs - Tracking](https://docs.ultralytics.com/modes/track/)
- [SORT: Simple Online and Realtime Tracking](https://arxiv.org/abs/1602.00763)
- [MOT Challenge Benchmark](https://motchallenge.net/)
