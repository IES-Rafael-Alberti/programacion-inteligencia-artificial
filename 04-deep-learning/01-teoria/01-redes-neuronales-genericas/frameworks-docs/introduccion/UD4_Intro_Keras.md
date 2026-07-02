# UD4 - Introduccion a Keras (guia rapida y practica)

## 1. Que es Keras y para que sirve

Keras es una API de alto nivel para construir, entrenar y evaluar redes
neuronales. Actualmente se usa principalmente sobre TensorFlow.

Ventajas principales:
- Codigo mas corto y legible.
- Flujo de trabajo muy claro: definir, compilar, entrenar, evaluar.
- Facil pasar de CPU a GPU.
- Buen ecosistema para docencia y prototipado rapido.

Flujo tipico:
1. Preparar datos.
2. Definir modelo.
3. Compilar (`loss`, `optimizer`, `metrics`).
4. Entrenar (`fit`).
5. Evaluar (`evaluate`) y predecir (`predict`).

---

## 2. Formas de montar una red en Keras

### 2.1 `Sequential` (lineal, la mas simple)

Se usa cuando la red es una pila simple de capas.

```python
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])
```

### 2.2 API Funcional (flexible)

Permite redes con varias entradas/salidas o conexiones no lineales.

```python
inputs = keras.Input(shape=(784,))
x = layers.Dense(128, activation="relu")(inputs)
outputs = layers.Dense(10, activation="softmax")(x)
model = keras.Model(inputs, outputs)
```

### 2.3 Subclassing (`keras.Model`)

Mayor control, util para casos avanzados.

```python
class MiRed(keras.Model):
    def __init__(self):
        super().__init__()
        self.d1 = layers.Dense(128, activation="relu")
        self.out = layers.Dense(1, activation="sigmoid")

    def call(self, x):
        x = self.d1(x)
        return self.out(x)
```

---

## 3. Tipos de capas mas usadas

### 3.1 Capas densas
- `Dense`: capa totalmente conectada.
- Uso tipico: tabular, MLP basica, capas finales de clasificacion.

### 3.2 Capas convolucionales (vision)
- `Conv2D`, `MaxPooling2D`, `GlobalAveragePooling2D`.
- Uso tipico: imagenes.

### 3.3 Capas recurrentes (secuencias)
- `SimpleRNN`, `LSTM`, `GRU`.
- Uso tipico: series temporales y texto.

### 3.4 Embeddings y texto
- `Embedding` para convertir indices de tokens en vectores densos.

### 3.5 Otras utiles
- `Dropout` (regularizacion).
- `BatchNormalization` (normalizacion interna).
- `Flatten`, `Reshape` (cambio de forma).

---

## 4. Funciones de activacion

Activacion = no linealidad. Sin activaciones, la red se comporta de forma lineal.

Activaciones mas comunes:
- `relu`: por defecto en capas ocultas; rapida y efectiva.
- `sigmoid`: salida en clasificacion binaria.
- `softmax`: salida en clasificacion multiclase.
- `tanh`: alternativa en algunos escenarios.
- `linear`: salida en regresion.
- `leaky_relu` (como capa o funcion): evita neuronas muertas de ReLU.

Regla practica de salida:
- Regresion: salida `linear`.
- Binaria: salida `sigmoid`.
- Multiclase: salida `softmax`.

---

## 5. "Tipos de neuronas" en practica

En implementacion real hablamos mas de tipos de capas que de neuronas
individuales. Aun asi, en clase puede pensarse asi:
- Neurona densa: combina todas las entradas (MLP).
- Neurona convolucional: ve un parche local (CNN).
- Neurona recurrente: mantiene estado temporal (RNN/LSTM/GRU).
- Neurona de salida: adaptada al problema (sigmoid/softmax/linear).

---

## 6. Funcion de perdida, optimizador y metricas

### 6.1 Perdida (`loss`)
- Regresion: `mse`, `mae`.
- Binaria: `binary_crossentropy`.
- Multiclase: `categorical_crossentropy` o `sparse_categorical_crossentropy`.

### 6.2 Optimizadores
- `Adam`: opcion general por defecto en docencia.
- `SGD`: util para explicar learning rate y momentum.
- `RMSprop`: comun en algunos escenarios secuenciales.

### 6.3 Metricas
- Clasificacion: `accuracy`, precision, recall, AUC.
- Regresion: MAE, RMSE.

Compilar modelo:

```python
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

---

## 7. Regularizacion (evitar overfitting)

Estrategias principales:
- `Dropout`: apaga neuronas al azar durante entrenamiento.
- Penalizacion L1/L2 (`kernel_regularizer`).
- `EarlyStopping`: parar cuando validacion deja de mejorar.
- `Data augmentation` en imagen.
- Reducir complejidad del modelo.

Ejemplo L2 + Dropout:

```python
from tensorflow.keras import regularizers

layers.Dense(128, activation="relu", kernel_regularizer=regularizers.l2(1e-4))
layers.Dropout(0.3)
```

---

## 8. Normalizacion

### 8.1 Escalado de datos de entrada
- Estandarizar o normalizar suele mejorar estabilidad.
- Imagenes: dividir por 255.0 en muchos casos.

### 8.2 `BatchNormalization`
- Normaliza activaciones intermedias por lote.
- Suele acelerar y estabilizar entrenamiento.

Ejemplo:

```python
layers.Dense(128),
layers.BatchNormalization(),
layers.Activation("relu")
```

---

## 9. Batches, epochs y pasos

- `batch_size`: numero de muestras por actualizacion.
- `epoch`: pasada completa por todo el dataset.
- `steps_per_epoch`: lotes por epoch (si aplica).

Trade-off basico:
- Batch pequeno: mas ruido, puede generalizar mejor.
- Batch grande: mas estable y rapido en GPU, puede requerir ajuste de LR.

Regla docente inicial:
- Empezar con `batch_size=32` o `64`.
- Ajustar segun memoria y estabilidad.

---

## 10. Callbacks utiles (control de entrenamiento)

- `EarlyStopping`: evita sobreentrenamiento.
- `ModelCheckpoint`: guarda mejor modelo.
- `ReduceLROnPlateau`: baja learning rate si no mejora.
- `TensorBoard`: seguimiento visual.

Ejemplo:

```python
callbacks = [
    keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
    keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=2)
]

history = model.fit(
    x_train, y_train,
    validation_split=0.2,
    epochs=30,
    batch_size=64,
    callbacks=callbacks
)
```

---

## 11. Entrenamiento en CPU y GPU

Comprobacion basica:

```python
import tensorflow as tf
print(tf.config.list_physical_devices("GPU"))
```

Recomendacion practica:
- Clase inicial: CPU para entender pipeline.
- Entrenamiento mas largo: GPU local o Colab.

---

## 12. Errores frecuentes en Keras

- Elegir mal activacion de salida para el problema.
- Elegir mal funcion de perdida.
- No escalar datos.
- Overfitting por red grande y pocos datos.
- Evaluar solo con accuracy en datasets desbalanceados.
- No separar train/valid/test correctamente.

---

## 13. Plantilla minima recomendada

```python
# 1) Definicion
model = keras.Sequential([
    layers.Input(shape=(input_dim,)),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(1, activation="sigmoid")
])

# 2) Compilacion
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# 3) Entrenamiento
history = model.fit(
    x_train, y_train,
    validation_data=(x_val, y_val),
    epochs=20,
    batch_size=32
)

# 4) Evaluacion
model.evaluate(x_test, y_test)
```

---

## 14. Resumen rapido para alumnado

- Keras permite construir redes neuronales de forma clara y rapida.
- La clave no es memorizar API, sino entender:
  - arquitectura,
  - activaciones,
  - perdida,
  - optimizacion,
  - validacion.
- Si entiendes ese bloque, luego cambiar de Keras a PyTorch/JAX es una cuestion
  de sintaxis y nivel de control.
