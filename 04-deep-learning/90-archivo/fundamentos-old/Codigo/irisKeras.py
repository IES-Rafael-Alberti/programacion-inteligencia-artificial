import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
# Load the iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset = pd.read_csv(url, names=names)
# Split the data into training and test sets
train_data, test_data, train_labels, test_labels = train_test_split(dataset.values[:, :4], dataset.values[:, 4], test_size=0.2, stratify=dataset.values[:, 4])
# Convert the labels to numeric classes
train_labels = pd.Categorical(train_labels).codes
test_labels = pd.Categorical(test_labels).codes


# Standardize the data
scaler = StandardScaler()
train_data = scaler.fit_transform(train_data)
test_data = scaler.transform(test_data)
# Create the model
model = keras.Sequential([
    keras.layers.Dense(8, activation='relu', input_shape=(4,)),
    keras.layers.Dense(3, activation='softmax')
])
# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
# Train the model
history = model.fit(train_data, train_labels, epochs=100, batch_size=32)
# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_data, test_labels, verbose=0)
print('Test Accuracy:', test_acc)

# Ejemplo de red neuronal con el dataset Iris en Keras

import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar el dataset Iris
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Normalizar los datos
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo
model = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar
model.fit(X_train, y_train, epochs=100, verbose=0)

# Evaluación
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Precisión: {accuracy:.4f}')
