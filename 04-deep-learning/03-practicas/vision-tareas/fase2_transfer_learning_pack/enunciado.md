# Fase 2. Transfer learning para mejorar el clasificador

En la fase 1 construisteis un clasificador de imágenes para distinguir entre `chihuahua` y `muffin` usando una red diseñada por vuestro equipo en Keras o PyTorch. En esta fase 2 debéis partir de ese trabajo y comprobar si es posible mejorar los resultados utilizando `transfer learning`.

La idea es comparar un modelo entrenado desde cero con otro basado en una arquitectura ya preentrenada en ImageNet, como `MobileNetV2` o `MobileNetV3Small`, y analizar si esa estrategia permite obtener mejor rendimiento, entrenar más rápido o generalizar mejor.

## Objetivo

Debéis entrenar y evaluar varios enfoques sobre el dataset `muffin vs chihuahua` y justificar qué solución final consideráis más adecuada.

El trabajo debe incluir, como mínimo:

- Un modelo base entrenado desde cero, que sirva como referencia.
- Un modelo con `transfer learning` usando una red preentrenada.
- Una prueba con la base convolucional congelada.
- Una fase de `fine-tuning` parcial desbloqueando parte de las últimas capas.
- Una comparación final de resultados.

## Dataset

Se trabajará con el dataset organizado en carpetas con una estructura similar a esta:

```text
dataset_chihuahua_muffin/
├── train/
├── val/
└── test/
```

Cada subconjunto debe contener las clases correspondientes a `chihuahua` y `muffin`.

## Tareas a realizar

1. Cargar correctamente el dataset desde carpetas.
2. Preparar un pipeline adecuado para entrenamiento, validación y test.
3. Visualizar algunas muestras para comprobar que la carga es correcta.
4. Entrenar un modelo de referencia creado por vuestro equipo.
5. Implementar un modelo de `transfer learning` usando `MobileNetV2` o `MobileNetV3Small`.
6. Entrenar primero el modelo preentrenado con la base congelada.
7. Aplicar después `fine-tuning` parcial, ajustando también la tasa de aprendizaje si es necesario.
8. Evaluar todos los modelos sobre el conjunto de test.
9. Comparar resultados en términos de precisión, tiempo de entrenamiento y capacidad de generalización.
10. Extraer una conclusión razonada sobre qué enfoque funciona mejor en este problema.

## Aspectos técnicos esperados

Se espera que el trabajo incorpore, cuando tenga sentido:

- Redimensionado homogéneo de imágenes.
- Trabajo por lotes (`batching`).
- Optimización del pipeline con `cache`, `shuffle` y `prefetch`.
- Algún bloque de `data augmentation`.
- Uso del preprocesado específico requerido por la arquitectura elegida.
- Alguna estrategia básica para controlar el sobreentrenamiento, como `EarlyStopping`.

## Comparativa obligatoria

No basta con entrenar un modelo preentrenado. La práctica consiste en comparar enfoques. Por tanto, en la entrega debe quedar claro:

- El resultado del modelo entrenado desde cero.
- El resultado del modelo con transfer learning y base congelada.
- El resultado del modelo tras el fine-tuning.
- Qué modelo obtiene mejor accuracy en test.
- Qué modelo entrena más rápido.
- Si la mejora obtenida compensa el coste adicional.

## Cuestiones a responder

Responded de forma breve, pero justificada:

1. ¿Qué modelo generaliza mejor sobre el conjunto de test?
2. ¿Cuál entrena más rápido?
3. ¿Qué diferencias habéis observado entre usar la base congelada y aplicar fine-tuning?
4. ¿Qué decisión final tomaríais para este problema y por qué?

## Idea de fondo

En la fase 1 aprendisteis a construir un clasificador de imágenes. En esta fase debéis demostrar que sabéis reutilizar modelos preentrenados y comparar de forma crítica un entrenamiento desde cero frente a una estrategia de `transfer learning`.
