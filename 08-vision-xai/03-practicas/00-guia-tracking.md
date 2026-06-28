# Semana 23 – Video análisis y seguimiento de objetos

## 🎯 Objetivos
- Comprender la diferencia entre detección en imágenes y **detección + seguimiento en vídeo**.
- Aplicar **YOLOv8 en modo tracking** para identificar y seguir múltiples objetos.
- Implementar un seguidor simple (mini‑SORT) para entender la lógica de asignación.
- Evaluar el rendimiento de tracking con métricas: **MOTA, MOTP**.

---

## 📚 Contenidos principales
1. **Tracking en vídeo**
   - Persistencia de IDs entre frames.
   - Problemas comunes: oclusiones, pérdida de objeto, ID switches.

2. **Herramientas**
   - `YOLOv8.track()` de la librería `ultralytics`.
   - Mini‑SORT implementado en clase.
   - Métricas MOTA y MOTP para benchmarking.

3. **Ejemplos prácticos**
   - Vídeo sintético generado con OpenCV.
   - Tracking con YOLOv8 preentrenado (personas, coches).
   - Cálculo de métricas con trayectorias simuladas.

---

## 📂 Notebooks trabajados
- **81_yolov8_tracking** → Ejemplo de YOLOv8 en modo `track` sobre vídeo.
- **82_sort_tracking** → Mini‑SORT implementado paso a paso.
- **83_metrics_tracking** → Cálculo de MOTA y MOTP en ejemplos simulados.

Incluyen:
- Versión base.
- Versión con soluciones.
- Versión con soluciones + autotests.

---

## 🛠️ Actividades prácticas
1. Ejecutar YOLOv8 en modo `track` sobre un vídeo corto de tráfico o personas.
2. Probar el mini‑SORT con detecciones simuladas.
3. Comparar métricas MOTA/MOTP en distintas configuraciones.
4. Reflexión: ¿qué limitaciones tienen estos algoritmos y cómo mejorarlos?

---

## ✅ Evaluación (RA2)
- **RA2.c**: Explicación de modelos de detección y seguimiento.
- **RA2.d**: Implementación práctica en YOLOv8 y SORT.
- **RA2.e**: Evaluación con métricas de tracking.

**Criterios de evaluación:**
- Ejecución de YOLOv8 en vídeos reales o sintéticos.
- Implementación funcional de un tracker simple.
- Correcto uso de métricas MOTA y MOTP.
- Reflexión crítica sobre aplicaciones prácticas (seguridad, tráfico, deportes).

---

## 📌 Recursos recomendados
- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)
- [MOT Challenge Benchmark](https://motchallenge.net/)
- [Artículo original SORT](https://arxiv.org/abs/1602.00763)
