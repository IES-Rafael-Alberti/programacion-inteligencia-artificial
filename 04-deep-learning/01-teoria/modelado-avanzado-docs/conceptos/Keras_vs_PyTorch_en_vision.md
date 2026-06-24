# Keras vs PyTorch en visión por computador

Hasta ahora, en esta unidad, la mayor parte de los ejemplos se han trabajado con Keras. Eso no significa que las mismas tareas no puedan hacerse con PyTorch: en realidad, casi todo lo que hemos visto en clasificación, `transfer learning`, vídeo o detección puede implementarse también con esa librería.

## Idea principal

No suele cambiar tanto **qué se puede hacer**, sino **cómo se trabaja**.

- Con `Keras`, muchas tareas resultan más directas y guiadas.
- Con `PyTorch`, normalmente tenemos más control explícito sobre el flujo de entrenamiento.

## Qué se puede hacer con ambos

Con Keras y con PyTorch se puede trabajar en:

- clasificación de imágenes
- redes convolucionales
- `transfer learning`
- fine-tuning
- detección de objetos
- segmentación
- análisis de vídeo
- pose estimation

Por tanto, elegir una u otra no significa renunciar a ciertas tareas, sino adoptar un estilo de desarrollo distinto.

## Diferencia de estilo

### Keras

Suele ser más cómodo para:

- introducir redes neuronales
- montar prototipos rápidos
- trabajar con APIs más compactas
- centrar la atención en la idea del modelo y no tanto en el detalle del entrenamiento

Ejemplo típico:

- preparar datos con generadores
- definir el modelo con `Sequential` o API funcional
- compilar con `optimizer`, `loss` y `metrics`
- entrenar con `fit()`

### PyTorch

Suele ser más habitual en:

- investigación
- repositorios modernos de visión
- proyectos donde interesa controlar bien el entrenamiento
- escenarios en los que se necesita más flexibilidad

Ejemplo típico:

- preparar datos con `Dataset` y `DataLoader`
- definir el modelo con `torch.nn.Module`
- escribir el bucle de entrenamiento de forma explícita
- controlar manualmente la propagación, el optimizador y el dispositivo

## Equivalencias conceptuales

### Carga de datos

- Keras:
  `ImageDataGenerator`, `flow_from_directory`, `tf.data`
- PyTorch:
  `Dataset`, `DataLoader`, `torchvision.transforms`

### Modelos

- Keras:
  `tf.keras.Sequential`, API funcional, `tf.keras.applications`
- PyTorch:
  `torch.nn.Module`, `torchvision.models`

### Entrenamiento

- Keras:
  `model.compile(...)` y `model.fit(...)`
- PyTorch:
  bucle manual con:
  - `model.train()`
  - `loss.backward()`
  - `optimizer.step()`

### Evaluación

- Keras:
  `model.evaluate(...)`
- PyTorch:
  `model.eval()` con `torch.no_grad()`

## Ejemplo mental sencillo

### En Keras

Podemos cargar una red preentrenada con algo de este estilo:

```python
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(160, 160, 3),
    include_top=False,
    weights="imagenet"
)
```

### En PyTorch

La idea equivalente sería:

```python
from torchvision import models

model = models.mobilenet_v2(weights="IMAGENET1K_V1")
```

En ambos casos estamos reutilizando un modelo entrenado previamente con ImageNet.

## Entonces, ¿cuál conviene usar?

### Para empezar

`Keras` suele ser más cómodo porque:

- reduce código repetitivo
- permite ver antes el flujo completo
- facilita centrarse en los conceptos

### Para ampliar o profundizar

`PyTorch` resulta muy interesante porque:

- da más control
- ayuda a entender mejor cómo funciona realmente el entrenamiento
- aparece en muchos proyectos y artículos modernos de visión

## Recomendación docente

Una progresión razonable podría ser esta:

1. aprender primero los conceptos con Keras
2. ver después una versión equivalente en PyTorch
3. dejar que el alumnado explore PyTorch si quiere profundizar más

Así se evita mezclar demasiadas novedades al principio, pero se muestra que no existe una única forma de trabajar en visión por computador.

## Conclusión

Sí, todo lo esencial que hemos hecho con Keras se puede hacer también con PyTorch.

La diferencia principal no está en la capacidad de la librería, sino en el estilo:

- `Keras`: más directo para aprender y prototipar
- `PyTorch`: más explícito y flexible para profundizar o investigar

Lo importante es dominar bien las ideas comunes: datos, modelo, entrenamiento, evaluación y reutilización de redes preentrenadas.
