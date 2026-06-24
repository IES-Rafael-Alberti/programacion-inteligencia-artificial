# Semana 22 – Segmentación de Imágenes: U-Net y Mask R-CNN

## 🎯 Objetivos
- Comprender las diferencias entre **clasificación, detección y segmentación**.
- Implementar una **U-Net** básica para segmentación biomédica.
- Usar **Mask R-CNN** preentrenado en PyTorch para segmentación de instancias.
- Evaluar segmentaciones con **IoU** y **Dice Score**.

---

## 📚 Contenidos principales
1. **Tipos de segmentación**
   - Semántica vs instancias.
   - Aplicaciones en medicina, tráfico, industria.

2. **Modelos**
   - **U-Net**: encoder–decoder para biomédico.
   - **Mask R-CNN**: extensión de Faster R-CNN con máscaras.

3. **Métricas de segmentación**
   - IoU (Intersection over Union).
   - Dice Score.

---

## 📂 Notebooks trabajados
- **78_unet_segmentation** → U-Net básica en Keras/TensorFlow.
- **79_maskrcnn_pytorch** → Mask R-CNN en PyTorch.
- **80_metrics_segmentation** → Cálculo de IoU y Dice Score.

Cada notebook incluye:
- Versión base.
- Versión con soluciones.
- Versión con soluciones + autotests.

---

## 🛠️ Actividades prácticas
1. Entrenar U-Net con dataset sintético (círculos/cuadrados).
2. Probar Mask R-CNN en imágenes urbanas.
3. Calcular IoU y Dice en ejemplos de segmentación.
4. Comparar resultados: ¿qué ventajas tiene Mask R-CNN sobre U-Net?

---

## ✅ Evaluación (RA2)
- **RA2.c**: Definición de arquitecturas de segmentación.
- **RA2.d**: Implementación en Keras y PyTorch.
- **RA2.e**: Evaluación con métricas IoU y Dice Score.

**Criterios de evaluación:**
- Construcción de una U-Net funcional.
- Ejecución de inferencia con Mask R-CNN.
- Uso de IoU y Dice Score en evaluaciones.
- Reflexión crítica sobre aplicaciones prácticas.

---

## 📌 Recursos recomendados
- [Paper original U-Net](https://arxiv.org/abs/1505.04597)
- [Mask R-CNN (He et al. 2017)](https://arxiv.org/abs/1703.06870)
- [Torchvision Detection Models](https://pytorch.org/vision/stable/models.html#detection)
