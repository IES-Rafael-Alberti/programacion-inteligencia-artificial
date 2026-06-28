# Segmentación de Imágenes: U-Net y Mask R-CNN

## De la clasificación a la segmentación

En visión por computadora existen tres niveles principales de análisis:

- **Clasificación**: asignar una etiqueta global a toda la imagen (ej. "gato", "perro").
- **Detección**: localizar objetos mediante bounding boxes y clasificarlos.
- **Segmentación**: asignar una etiqueta a cada píxel de la imagen.

La segmentación se divide en dos categorías:

- **Segmentación semántica**: cada píxel se asigna a una clase (ej. todos los coches son "coche").
- **Segmentación de instancias**: cada objeto tiene su propia máscara aunque pertenezca a la misma clase (coche 1, coche 2).

## U-Net

U-Net es una arquitectura convolutional diseñada originalmente para segmentación biomédica. Su nombre proviene de la forma de "U" de su estructura:

- **Encoder (contractivo)**: secuencia de capas convolucionales y pooling que reducen la resolución espacial mientras aumentan la profundidad de características.
- **Bottleneck**: capa de mayor profundidad que captura las representaciones más abstractas.
- **Decoder (expansivo)**: capas de up-convolution que restauran la resolución original, con conexiones skip que concatenan características del encoder para preservar información espacial fina.

Las conexiones skip son clave: permiten que el decoder acceda a detalles de alta resolución del encoder, evitando que se pierdan durante la contracción.

## Mask R-CNN

Mask R-CNN extiende Faster R-CNN añadiendo una rama de segmentación que predice máscaras binarias para cada región propuesta. Combina:

1. **Backbone** (ResNet + FPN) para extraer características multiescala.
2. **RPN (Region Proposal Network)** para generar candidatos.
3. **RoiAlign** para extraer características de cada región sin pérdida de cuantización.
4. **Cabezales paralelos**: clasificación, bounding box y máscara binaria.

Mask R-CNN hace segmentación de instancias: distingue objetos individuales incluso de la misma clase.

## Métricas de segmentación

### IoU (Intersection over Union)

Mide el solapamiento entre la máscara predicha y la real:

$$IoU = \frac{TP}{TP + FP + FN}$$

Un IoU > 0.5 se considera generalmente una predicción correcta. Es la métrica estándar en benchmarks como COCO.

### Dice Score

Similar al F1-score pero aplicado a píxeles:

$$Dice = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$$

Es más sensible que IoU cuando el área de la región es pequeña, por eso se usa mucho en segmentación biomédica.

## Referencias

- [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)
- [Mask R-CNN](https://arxiv.org/abs/1703.06870)
- [Torchvision Detection Models](https://pytorch.org/vision/stable/models.html#detection)
