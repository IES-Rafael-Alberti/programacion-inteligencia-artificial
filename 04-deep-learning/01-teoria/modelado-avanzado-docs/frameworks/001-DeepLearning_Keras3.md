---
title: "Deep Learning con Keras 3"
output: 
  pdf_document:
    toc: true
    toc_depth: 3
  engine: lualatex
   
---

# Deep Learning con Keras 3

Keras 3 es la nueva versión de Keras, la API de redes neuronales de alto nivel de Google. Una de las principales novedades es que ahora es **multi-backend**, pudiendo usar TensorFlow, JAX o PyTorch como motor de ejecución.

## 1. Introducción a Keras 3

### 1.1 ¿Qué es Keras?

Keras es una API de redes neuronales de alto nivel, diseñada para ser:
- **Fácil de usar**: API clara y minimalista
- **Modular**: Construye modelos como bloques
- **Extensible**: Fácil de ampliar con nuevas funcionalidades

### 1.2 Keras 3: Multi-backend

```python
# Especificar el backend antes de importar keras
import os
os.environ["KERAS_BACKEND"] = "tensorflow"  # o "jax" o "torch" o "numpy"

import keras
print(keras.config.backend())  # Muestra el backend activo
```

### 1.3 Instalación

```bash
pip install keras>=3.0.0
```

---

## 2. Tensores y Operaciones Básicas

### 2.1 Creación de tensores

```python
import keras
import keras.ops as ops
import numpy as np

# Desde NumPy
x = keras.ops.convert_to_tensor(np.array([1, 2, 3]))

# Directamente con Keras
x = keras.ops.ones((3, 3))
x = keras.ops.zeros((2, 4))
x = keras.ops.random.normal((10, 10))

# Operaciones
y = x * 2
z = ops.matmul(x, x.T)
```

---

## 3. Construcción de Modelos

### 3.1 API Secuencial

```python
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization

model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Clasificación binaria
])

# Resumen del modelo
model.summary()
```

### 3.2 API Funcional (más flexible)

```python
from keras.layers import Input, Dense, Concatenate
from keras.models import Model

# Entradas
input_a = Input(shape=(10,), name="entrada_a")
input_b = Input(shape=(5,), name="entrada_b")

# Ramas
x1 = Dense(32, activation='relu')(input_a)
x2 = Dense(32, activation='relu')(input_b)

# Concatenar
merged = Concatenate()([x1, x2])
output = Dense(1, activation='sigmoid')(merged)

# Modelo
model = Model(inputs=[input_a, input_b], outputs=output)
```

### 3.3 Capas Personalizadas

```python
from keras.layers import Layer

class MyDense(Layer):
    def __init__(self, units, **kwargs):
        super().__init__(**kwargs)
        self.units = units
    
    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer='glorot_uniform',
            trainable=True
        )
        self.b = self.add_weight(
            shape=(self.units,),
            initializer='zeros',
            trainable=True
        )
    
    def call(self, inputs):
        return ops.matmul(inputs, self.w) + self.b
    
    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config
```

---

## 4. Entrenamiento

### 4.1 Compilación y Entrenamiento

```python
# Compilar modelo
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Entrenar
history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=32,
    validation_split=0.2,
    callbacks=[
        keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
        keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=3)
    ]
)
```

### 4.2 Entrenamiento con Generadores

```python
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    horizontal_flip=True
)

train_generator = datagen.flow(X_train, y_train, batch_size=32)

history = model.fit(
    train_generator,
    steps_per_epoch=len(X_train) // 32,
    epochs=30
)
```

### 4.3 Custom Training Loop

```python
import jax  # si usas backend jax
import torch  # si usas backend torch

# Obtener el backend
backend = keras.config.backend()

if backend == "tensorflow":
    import tensorflow as tf
elif backend == "jax":
    import jax.numpy as jnp
elif backend == "torch":
    import torch

# Ejemplo con TF
model = keras.Sequential([Dense(1)])
model.compile(optimizer='adam', loss='mse')

# Usar train_on_batch para control fino
for epoch in range(10):
    for i in range(0, len(X), 32):
        X_batch = X[i:i+32]
        y_batch = y[i:i+32]
        loss = model.train_on_batch(X_batch, y_batch)
```

---

## 5. Callbacks

### 5.1 Callbacks Disponibles

```python
from keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau,
    TensorBoard,
    LearningRateScheduler,
    CSVLogger
)

# Early Stopping - detener cuando no mejora
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

# Guardar mejor modelo
checkpoint = ModelCheckpoint(
    'best_model.keras',
    monitor='val_loss',
    save_best_only=True
)

# Reducir LR cuando se estanca
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=3,
    min_lr=1e-6
)

# TensorBoard
tensorboard = TensorBoard(
    log_dir='./logs',
    histogram_freq=1,
    write_graph=True
)

# Reducir LR con schedule
def scheduler(epoch):
    if epoch < 10:
        return 0.001
    return 0.001 * 0.5 ** (epoch // 10)

lr_scheduler = LearningRateScheduler(scheduler)

# Usar múltiples callbacks
model.fit(X, y, callbacks=[early_stop, checkpoint, reduce_lr, tensorboard])
```

---

## 6. Regularización

### 6.1 Dropout

```python
from keras.layers import Dropout, Dense

model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dropout(0.3),  # 30% de neuronas desactivadas
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])
```

### 6.2 L1/L2 Regularization

```python
from keras import regularizers

model = Sequential([
    Dense(64, activation='relu', input_shape=(10,),
          kernel_regularizer=regularizers.l2(0.01)),
    Dense(32, activation='relu',
          kernel_regularizer=regularizers.l1(0.001)),
    Dense(1, activation='sigmoid')
])

# O combinado (Elastic Net)
model.add(Dense(32, 
    kernel_regularizer=regularizers.l1_l2(l1=0.01, l2=0.01)))
```

### 6.3 Batch Normalization

```python
from keras.layers import BatchNormalization, Dense

model = Sequential([
    Dense(64, input_shape=(10,)),
    BatchNormalization(),
    Activation('relu'),
    Dense(32),
    BatchNormalization(),
    Activation('relu'),
    Dense(1, activation='sigmoid')
])
```

---

## 7. SavedModel y Exportación

### 7.1 Guardar/Cargar Modelo Completo

```python
# Guardar modelo completo
model.save('mi_modelo.keras')

# Cargar modelo
model = keras.models.load_model('mi_modelo.keras')

# Guardar solo pesos
model.save_weights('pesos.weights.h5')

# Cargar pesos
model.load_weights('pesos.weights.h5')
```

### 7.2 Exportar a TensorFlow Lite

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

with open('modelo.tflite', 'wb') as f:
    f.write(tflite_model)
```

---

## 8. Redes Neuronales Especializadas

### 8.1 Redes Convolucionales (CNN)

```python
from keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout
)
from keras.models import Sequential

model = Sequential([
    # Bloque convolucional 1
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    
    # Bloque convolucional 2
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    
    # Clasificación
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

### 8.2 Redes Recurrentes (RNN/LSTM/GRU)

```python
from keras.layers import LSTM, GRU, Dense, Input
from keras.models import Model

# LSTM para secuencias
inputs = Input(shape=(timesteps, features))
x = LSTM(64, return_sequences=True)(inputs)
x = LSTM(32)(x)
outputs = Dense(1)(x)

model = Model(inputs, outputs)

# GRU
model.add(GRU(64, return_sequences=True, input_shape=(timesteps, features)))
model.add(GRU(32))
```

### 8.3 Transformer/Attention

```python
from keras.layers import MultiHeadAttention, LayerNormalization, Dense, Dropout

class TransformerBlock(Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super().__init__()
        self.att = MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = Dense(ff_dim, activation='relu')
        self.layernorm1 = LayerNormalization(epsilon=1e-6)
        self.layernorm2 = LayerNormalization(epsilon=1e-6)
        self.dropout1 = Dropout(rate)
        self.dropout2 = Dropout(rate)
    
    def call(self, inputs, training=False):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)
```

---

## 9. Optimizadores

### 9.1 Optimizadores Disponibles

```python
# Adam
model.compile(optimizer='adam', loss='mse')

# Adam con parámetros
model.compile(
    optimizer=keras.optimizers.Adam(
        learning_rate=0.001,
        beta_1=0.9,
        beta_2=0.999,
        epsilon=1e-7
    ),
    loss='mse'
)

# SGD con momentum
model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
    loss='mse'
)

# RMSprop
model.compile(optimizer='rmsprop', loss='mse')

# AdamW (Adam con weight decay)
model.compile(
    optimizer=keras.optimizers.AdamW(learning_rate=0.001, weight_decay=0.01),
    loss='mse'
)
```

### 9.2 Gradient Clipping

```python
# Clip por valor
optimizer = keras.optimizers.Adam(clipvalue=1.0)

# Clip por norma
optimizer = keras.optimizers.Adam(clipnorm=1.0)
```

---

## 10. Funciones de Pérdida

### 10.1 Pérdidas para Regresión

```python
model.compile(optimizer='adam', loss='mse')           # Error cuadrático medio
model.compile(optimizer='adam', loss='mae')            # Error absoluto medio
model.compile(optimizer='adam', loss='mse')           # Huber
```

### 10.2 Pérdidas para Clasificación

```python
# Clasificación binaria
model.compile(optimizer='adam', loss='binary_crossentropy')

# Clasificación multiclase
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy'  # etiquetas como enteros
)

# One-hot encoded
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy'  # etiquetas one-hot
)
```

---

## 11. Métricas

### 11.1 Métricas Integradas

```python
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=[
        'accuracy',
        keras.metrics.Precision(),
        keras.metrics.Recall(),
        keras.metrics.AUC(),
        keras.metrics.F1Score()
    ]
)
```

### 11.2 Métricas Personalizadas

```python
import keras.backend as K

def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_true - y_pred)))

model.compile(optimizer='adam', loss='mse', metrics=[rmse])
```

---

## 12. Transfer Learning

### 12.1 Usar Modelo Preentrenado

```python
from keras.applications import VGG16, ResNet50, EfficientNetB0
from keras.models import Sequential
from keras.layers import Dense, GlobalAveragePooling2D

# Cargar modelo preentrenado (sin capa final)
base_model = VGG16(weights='imagenet', include_top=False, 
                   input_shape=(224, 224, 3))

# Congelar capas base
base_model.trainable = False

# Añadir capas personalizadas
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(256, activation='relu'),
    Dense(10, activation='softmax')
])
```

### 12.2 Fine-tuning

```python
# Descongelar últimas capas
base_model.trainable = True

# Congelar capas tempranas
for layer in base_model.layers[:-4]:
    layer.trainable = False

# Re-entrenar con LR baja
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```

---

## 13. Distributed Training

### 13.1 Multi-GPU con MirroredStrategy

```python
# TensorFlow multi-GPU
strategy = keras.distribution.TensorFlowDistributionStrategy(
    keras.distribute.MirroredStrategy()
)

with strategy.scope():
    model = Sequential([...])
    model.compile(optimizer='adam', loss='mse')
```

### 13.2 Multi-GPU con DeviceMirroringStrategy

```python
# Más moderno
strategy = keras.distribute.DeviceMirroringStrategy()

with strategy.scope():
    model = build_model()
    model.compile(optimizer='adam', loss='categorical_crossentropy')

# Entrenar
model.fit(dataset, epochs=10)
```

### 13.3 Multi-GPU con DataParallel

```python
# Para PyTorch backend en Keras 3
import torch
torch.cuda.set_device(0)  # Primary device

# Keras automáticamente usa todas las GPUs disponibles
model.fit(X_train, y_train, epochs=10)
```

### 13.4 TPU Training

```python
# Conectar a TPU
resolver = keras.distribute.TPUClusterResolver()
keras.distribute.connect_to_cluster(resolver)
tpu_strategy = keras.distribute.TPUStrategy(resolver)

with tpu_strategy.scope():
    model = build_model()
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

model.fit(dataset, epochs=10)
```

### 13.5 Parameter Server Strategy (múltiples máquinas)

```python
# Para entrenamiento distribuido en múltiples máquinas
strategy = keras.distribute.ParameterServerStrategy(
    variable_partitioner=keras.distribute.MinSizePartitioner(
        min_shard_bytes=(256 << 10),
        max_shards=2
    )
)

with strategy.scope():
    model = build_model()
    model.compile(optimizer='adam', loss='mse')
```

### 13.6 Ejemplo completo Multi-GPU

```python
import keras
from keras import layers

# Detectar GPUs
gpus = keras.config.list_logical_devices('GPU')
print(f"GPUs disponibles: {len(gpus)}")

# Estrategia
if len(gpus) > 1:
    strategy = keras.distribute.MirroredStrategy()
else:
    strategy = keras.distribute.OneDeviceStrategy(device=gpus[0])

# Construir modelo dentro del scope
with strategy.scope():
    model = keras.Sequential([
        layers.Dense(256, activation='relu', input_shape=(784,)),
        layers.Dropout(0.5),
        layers.Dense(10, activation='softmax')
    ])
    
    model.compile(
        optimizer=keras.optimizers.Adam(1e-3),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

# Datos sintéticos para prueba
import numpy as np
X_train = np.random.rand(10000, 784).astype('float32')
y_train = np.random.randint(0, 10, 10000)

# Entrenar
history = model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=32 * len(gpus),  # Scale batch size
    validation_split=0.2
)
```

---

## 14. Debugging y Troubleshooting

### 14.1 Visualizar Arquitectura

```python
# Resumen textual
model.summary()

# Diagrama
keras.utils.plot_model(model, 'model.png', show_shapes=True)

# Ver pesos
for layer in model.layers:
    print(f"{layer.name}: {layer.get_weights()[0].shape}")
```

### 14.2 Checkpoints

```python
# Guardar cada época
checkpoint = ModelCheckpoint('weights_{epoch:02d}.keras')

# Guardar mejor modelo
best_checkpoint = ModelCheckpoint('best_model.keras', 
                                   monitor='val_loss',
                                   save_best_only=True)
```

### 14.3 Problemas comunes y soluciones

#### a) Loss = NaN
```python
# 1. Learning rate muy alto
model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-4))

# 2. Reducir batch size (menos ejemplos = más ruido)
model.fit(X_train, y_train, batch_size=16)

# 3. Añadir clipping
x = keras.ops.clip(x, -1e6, 1e6)

# 4. Usar gradient clipping
optimizer = keras.optimizers.Adam(clipnorm=1.0)
```

#### b) Overfitting excesivo
```python
# 1. Añadir Dropout
from keras.layers import Dropout
model.add(Dropout(0.5))

# 2. Añadir regularización L2
from keras import regularizers
model.add(Dense(64, kernel_regularizer=regularizers.l2(0.01)))

# 3. Early Stopping
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=10, restore_best_weights=True
)

# 4. Reducir complejidad
model.add(Dense(32))  # en lugar de 256
```

#### c) Modelo no converge
```python
# 1. Verificar normalización
print(f"X mean: {X.mean():.2f}, std: {X.std():.2f}")

# 2. Verificar labels
print(f"y unique: {np.unique(y)}")

# 3. Learning rate schedule
lr_scheduler = keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss', factor=0.5, patience=5
)

# 4. Verificar arquitectura (output shape)
model.summary()
```

#### d) GPU memory issues
```python
# 1. Reducir batch size
model.fit(X, y, batch_size=32)

# 2. Clear session
keras.backend.clear_session()

# 3. Mixed precision
keras.mixed_precision.set_global_policy('mixed_float16')

# 4. Generators en lugar de cargar todo
model.fit(train_dataset)  # tf.data.Dataset
```

### 14.4 Debugging con TensorBoard

```python
# Habilitar TensorBoard callback
tb_callback = keras.callbacks.TensorBoard(
    log_dir='./logs',
    histogram_freq=1,  # weights cada época
    write_graph=True,
    embeddings_freq=1
)

model.fit(X_train, y_train, callbacks=[tb_callback])

# Ver en terminal: tensorboard --logdir=./logs
```

### 14.5 Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| ValueError: Shapes | Input shape incorrecto | Ajustar input_shape |
| OOM | Batch muy grande | Reducir batch_size |
| Loss NaN | LR muy alto | Reducir LR |
| Low accuracy | Underfitting | Más capacidad |
| High val/low train | Overfitting | Dropout, regularización |

### 14.6 Debugging tips

```python
# 1. Verificar shapes en cada capa
import keras
debug_model = keras.Model(inputs=model.input, outputs=[l.output for l in model.layers])
outputs = debug_model.predict(X[:1])
for i, out in enumerate(outputs):
    print(f"Layer {i}: {out.shape}")

# 2. Disable execution eager for debugging
keras.config.run_eagerly(False)

# 3. Verificar con un solo batch
model.fit(X[:32], y[:32], epochs=1)

# 4. Debugger integrado
from keras import callbacks
dbg = callbacks.DebuggingLogger()
```

---

## 15. Best Practices con Keras 3

1. **Usar DataLoaders** para datasets grandes
2. **Normalizar datos** antes de entrenar
3. **EarlyStopping** para evitar overfitting
4. **Learning Rate Scheduler** para mejor convergencia
5. **TensorBoard** para visualización
6. **Guardar checkpoints** durante entrenamiento largo
7. **Usar Mixed Precision** (float16) para acelerar entrenamiento
8. **Progressive Resizing** en imágenes

---

## 16. Recursos Adicionales

- [Documentación oficial de Keras](https://keras.io/)
- [Keras API Reference](https://keras.io/api/)
- [Keras Examples](https://github.com/keras-team/keras-io/tree/master/examples)
