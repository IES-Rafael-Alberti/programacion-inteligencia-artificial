import cudf
import cupy as cp
import numpy as np
from cuml.model_selection import train_test_split
from cuml.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras

# Cargar el dataset desde UCI con cudf
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset = cudf.read_csv(url, names=names)

# Convertir las clases categóricas a valores numéricos
dataset['class'] = dataset['class'].factorize()[0]

# Separar características y etiquetas
X = dataset.iloc[:, :4]
y = dataset.iloc[:, 4]

# Dividir en conjunto de entrenamiento y prueba con cuML
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# Normalizar los datos con cuML StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convertir datos a NumPy para usarlos en TensorFlow/Keras
X_train = cp.asnumpy(X_train)
X_test = cp.asnumpy(X_test)
y_train = cp.asnumpy(y_train)
y_test = cp.asnumpy(y_test)

# Definir el modelo en Keras
model = keras.Sequential([
    keras.layers.Dense(8, activation='relu', input_shape=(4,)),
    keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=100, batch_size=32)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print('Test Accuracy:', test_acc)
