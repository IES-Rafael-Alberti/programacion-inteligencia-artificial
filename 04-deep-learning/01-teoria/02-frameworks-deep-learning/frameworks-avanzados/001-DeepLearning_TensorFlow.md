# Guía de TensorFlow (Standalone)

TensorFlow es el framework de deep learning de Google que ofrece un ecosistema completo para entrenamiento y despliegue de modelos.

---

## 1. Instalación

```bash
pip install tensorflow
# o con soporte GPU
pip install tensorflow[and-cuda]
```

---

## 2. Conceptos Básicos

### Tensores

```python
import tensorflow as tf

# Crear tensores
x = tf.constant([[1.0, 2.0], [3.0, 4.0]])
print(x.shape)  # (2, 2)

# Operaciones
y = tf.matmul(x, x)  # Multiplicación de matrices
z = tf.nn.relu(y)    # Activación ReLU
```

### Variables

```python
# Variables (contenedor de valores que pueden cambiar)
w = tf.Variable(tf.random.normal((10, 5)))
b = tf.Variable(tf.zeros((5,)))

# Actualizar valores
w.assign(w * 0.5)
w.assign_add(tf.ones_like(w))
```

---

## 3. Building Models

### Sequential API

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

### Functional API

```python
# Para modelos más complejos
inputs = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(64, activation='relu')(inputs)
x = tf.keras.layers.Dropout(0.5)(x)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

### Custom Model (Subclassing)

```python
class MyModel(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(64, activation='relu')
        self.dense2 = tf.keras.layers.Dense(10, activation='softmax')
    
    def call(self, x, training=False):
        x = self.dense1(x)
        if training:
            x = tf.keras.layers.Dropout(0.5)(x)
        return self.dense2(x)

model = MyModel()
```

---

## 4. Custom Training Loop

```python
# Datos
dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
dataset = dataset.shuffle(10000).batch(32)

# Optimizador y loss
optimizer = tf.keras.optimizers.Adam(1e-3)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()

# Métricas
train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')

# Training step
@tf.function  # Compila a graph
def train_step(images, labels):
    with tf.GradientTape() as tape:
        predictions = model(images, training=True)
        loss = loss_fn(labels, predictions)
    
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    train_loss(loss)
    train_accuracy(labels, predictions)

# Loop
for epoch in range(5):
    train_loss.reset_states()
    train_accuracy.reset_states()
    
    for images, labels in dataset:
        train_step(images, labels)
    
    print(f"Epoch {epoch}: Loss {train_loss.result()}, Acc {train_accuracy.result()}")
```

---

## 5. tf.data API

```python
# Pipeline de datos eficiente
dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))

dataset = dataset.shuffle(buffer_size=10000)
dataset = dataset.batch(32)
dataset = dataset.prefetch(tf.data.AUTOTUNE)

# Data augmentation
dataset = dataset.map(lambda x, y: (tf.image.random_flip_left_right(x), y))

# Lectura de archivos
dataset = tf.data.TextLineDataset(["file1.txt", "file2.txt"])
dataset = tf.data.Dataset.from_generator(generator_func, output_signature=...)
```

---

## 6. Custom Layers

```python
class MyLayer(tf.keras.layers.Layer):
    def __init__(self, units, **kwargs):
        super().__init__(**kwargs)
        self.units = units
    
    def build(self, input_shape):
        self.kernel = self.add_weight(
            name='kernel',
            shape=(input_shape[-1], self.units),
            initializer='glorot_uniform',
            trainable=True
        )
    
    def call(self, inputs):
        return tf.matmul(inputs, self.kernel)
    
    def get_config(self):
        config = super().get_config()
        config.update({'units': self.units})
        return config
```

---

## 7. Custom Metrics

```python
class MeanSquaredError(tf.keras.metrics.Metric):
    def __init__(self, name='mse', **kwargs):
        super().__init__(name=name, **kwargs)
        self.total = self.add_weight(name='total', initializer='zeros')
        self.count = self.add_weight(name='count', initializer='zeros')
    
    def update_state(self, y_true, y_sample_weight=None):
        values = tf.math.square(y_true - self.sample)
        values = tf.cast(values, self.dtype)
        if sample_weight is not None:
            values = tf.multiply(values, sample_weight)
        self.total.assign_add(tf.reduce_sum(values))
        self.count.assign_add(tf.cast(tf.shape(y_true)[0], self.dtype))
    
    def result(self):
        return self.total / self.count
    
    def reset_state(self):
        self.total.assign(0.0)
        self.count.assign(0.0)
```

---

## 8. TensorFlow Lite (Mobile/Edge)

### Conversión

```python
# Convertir a TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Guardar
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

# Cuantización
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
tflite_model = converter.convert()
```

### Inference

```python
import numpy as np

interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_data = np.array(data, dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output = interpreter.get_tensor(output_details[0]['index'])
```

---

## 9. TensorFlow Serving (Production)

### Guardar modelo

```python
model.save('my_model/1')  # Formato SavedModel
```

### Docker

```bash
docker pull tensorflow/serving
docker run -p 8501:8501 \
  --mount type=bind,source=$(pwd)/my_model,target=/models/my_model \
  -e MODEL_NAME=my_model \
  tensorflow/serving
```

### Inference (REST)

```bash
curl -X POST http://localhost:8501/v1/models/my_model:predict \
  -d '{"instances": [[1.0, 2.0, 3.0]]}'
```

---

## 10. TensorFlow Hub (Transfer Learning)

```python
import tensorflow_hub as hub

# Cargar modelo pre-entrenado
model = tf.keras.Sequential([
    hub.KerasLayer('https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(dataset, epochs=5)
```

---

## 11. Distributed Training

### Multi-GPU

```python
# MirroredStrategy
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = build_model()
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

model.fit(dataset, epochs=10)
```

### Multi-Machine

```python
# ParameterServerStrategy
strategy = tf.distribute.ParameterServerStrategy(
    cluster_resolver=tf.distribute.cluster_resolver.TFConfigClusterResolver()
)
```

---

## 12. TensorFlow.js

```python
# Guardar modelo para web
model.save('tfjs_model')

# En JavaScript:
// const model = await tf.loadLayersModel('/tfjs_model/model.json');
# const prediction = model.predict(tf.tensor2d([[1, 2, 3]]));
```

---

## 13. Recursos

- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [TensorFlow Hub](https://tfhub.dev)
- [TensorFlow Lite](https://www.tensorflow.org/lite)
- [TensorFlow Serving](https://www.tensorflow.org/tfx/serving)
