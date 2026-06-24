---
editor_options: 
  markdown: 
    wrap: 72
output: 
  pdf_document:
    toc:
      true
    latex_engine: xelatex
---

# Documentación sobre Redes Neuronales

Este documento proporciona una guía paso a paso sobre distintos tipos de
redes neuronales, desde modelos básicos hasta arquitecturas avanzadas.
Cada sección incluye descripciones teóricas y ejemplos prácticos en
PyTorch y Keras.

------------------------------------------------------------------------

## 1. Funciones de Pérdida y su Importancia

### ¿Qué es la función de pérdida?

La función de pérdida o error es una métrica que cuantifica cuán bien
está funcionando una red neuronal. Su objetivo es minimizar esta pérdida
durante el entrenamiento para mejorar la precisión del modelo.

### Importancia de la función de pérdida

-   Nos permite evaluar qué tan bien está aprendiendo la red neuronal.
-   Es la base para el ajuste de los pesos mediante el algoritmo de
    **gradiente descendente**.
-   Un valor alto de pérdida indica que el modelo está aprendiendo
    incorrectamente.

### Principales funciones de pérdida

Las funciones de pérdida dependen del tipo de problema:

#### **Para problemas de regresión**

1.  **Error Cuadrático Medio (MSE)**:
    $$ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
    -   **¿Qué significa?** Calcula la media de los errores al cuadrado.
        Penaliza más los errores grandes.
    -   **Cuándo usarla:** Problemas de regresión donde los errores
        grandes deben ser castigados.
2.  **Error Absoluto Medio (MAE)**:
    $$ MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$
    -   **¿Qué significa?** Calcula la media de los errores absolutos.
    -   **Cuándo usarla:** Si queremos una métrica menos sensible a
        valores extremos.

#### **Para problemas de clasificación**

1.  **Entropía Cruzada (Cross-Entropy Loss o Log Loss)**:
    $$ L = - \sum_{i=1}^{n} y_i \log(\hat{y}_i) $$
    -   **¿Qué significa?** Mide la diferencia entre la distribución
        real y la predicha por el modelo.
    -   **Cuándo usarla:** Problemas de clasificación binaria o
        multiclase.
2.  **Hinge Loss** (usada en SVMs):
    $$ L = \sum_{i=1}^{n} max(0, 1 - y_i \cdot \hat{y}_i) $$
    -   **¿Qué significa?** Penaliza clasificaciones incorrectas.
    -   **Cuándo usarla:** Modelos de clasificación con margen (SVM).

### Visualización de la pérdida en Python

Podemos graficar las funciones de pérdida para entender su
comportamiento:

``` python
import numpy as np
import matplotlib.pyplot as plt

# Valores simulados de predicciones y reales
y_true = np.linspace(-2, 2, 100)
y_pred = np.linspace(-2, 2, 100)

mse = (y_true - y_pred) ** 2
mae = np.abs(y_true - y_pred)

plt.figure(figsize=(8, 4))
plt.plot(y_true, mse, label='MSE')
plt.plot(y_true, mae, label='MAE')
plt.xlabel('Valores reales vs predichos')
plt.ylabel('Pérdida')
plt.legend()
plt.title('Comparación de funciones de pérdida')
plt.show()
```

------------------------------------------------------------------------

## 2. Algoritmo de Gradiente Descendente

### ¿Qué es el gradiente descendente?

El **gradiente descendente** es un algoritmo de optimización utilizado
para ajustar los pesos de una red neuronal minimizando la función de
pérdida. Se basa en el cálculo de la derivada para encontrar la
dirección en la que debemos mover los pesos.

### Cómo funciona

1.  Se calcula el **gradiente** (derivada parcial de la función de
    pérdida respecto a los pesos).
2.  Se actualizan los pesos en la dirección opuesta al gradiente.
3.  Se repite el proceso hasta encontrar un mínimo óptimo.

### Dirección hacia el mínimo

El gradiente nos indica la dirección de mayor incremento de la función
de pérdida. Para minimizarla, nos movemos en la dirección opuesta a
dicho gradiente.

### Algoritmo de Backpropagation

El **backpropagation** es el algoritmo que permite ajustar los pesos de
una red neuronal multicapa utilizando gradiente descendente.

### Pasos del Backpropagation:

1.  **Paso hacia adelante (Forward Pass):**
    -   Se calcula la salida de cada capa aplicando la función de
        activación.
    -   Se obtiene la predicción final.
2.  **Cálculo del error:**
    -   Se compara la salida obtenida con la esperada utilizando la
        función de pérdida.
3.  **Paso hacia atrás (Backward Pass):**
    -   Se calculan los gradientes de cada capa respecto a la función de
        pérdida usando la regla de la cadena.
    -   Se actualizan los pesos utilizando gradiente descendente.

### Implementación de Backpropagation en Python

``` python
import numpy as np

# Función de activación sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Inicialización de pesos
np.random.seed(42)
pesos_entrada = np.random.rand(2, 2)
pesos_salida = np.random.rand(2, 1)

# Tasa de aprendizaje
alpha = 0.5

# Entrenamiento con Backpropagation
for epoch in range(10000):
    # Forward pass
    capa_oculta = sigmoid(np.dot(X, pesos_entrada))
    salida = sigmoid(np.dot(capa_oculta, pesos_salida))
    
    # Error
    error = y - salida
    
    # Backward pass
    delta_salida = error * sigmoid_derivative(salida)
    delta_oculta = np.dot(delta_salida, pesos_salida.T) * sigmoid_derivative(capa_oculta)
    
    # Actualización de pesos
    pesos_salida += np.dot(capa_oculta.T, delta_salida) * alpha
    pesos_entrada += np.dot(X.T, delta_oculta) * alpha
```

### Visualización del proceso de Backpropagation

(Similar a lo hecho anteriormente con el gradiente descendente,
agregando gráficos intermedios para cada paso).

------------------------------------------------------------------------

## 3. Funciones de Activación y su Impacto

Las funciones de activación introducen no linealidad en las redes
neuronales, permitiendo que aprendan relaciones complejas en los datos.

### ¿Qué es una función de activación?

Una función de activación es una transformación matemática aplicada a la
salida de cada neurona en una red neuronal. Su objetivo principal es
determinar si una neurona debe activarse o no, dependiendo de la entrada
que recibe.

### Principales funciones de activación

#### 3.1. Función Sigmoide

$$ \sigma(x) = \frac{1}{1 + e^{-x}} $$ - **Ventajas:** Suaviza la salida
y la restringe al rango (0,1), útil en clasificación binaria. -
**Desventajas:** Sufre del problema de gradientes desaparecidos en redes
profundas.

#### 3.2. Función Tangente Hiperbólica (Tanh)

$$ tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} $$ - **Ventajas:**
Similar a sigmoide pero con salida en (-1,1), lo que ayuda en la
normalización de datos. - **Desventajas:** También tiene el problema de
gradientes desaparecidos.

#### 3.3. Función ReLU (Rectified Linear Unit)

$$ ReLU(x) = max(0, x) $$ - **Ventajas:** Evita el problema de
gradientes desaparecidos al permitir que los valores positivos fluyan
sin cambios. - **Desventajas:** Puede causar neuronas muertas si muchas
salidas son cero (problema de "Dying ReLU").

#### 3.4. Función Leaky ReLU

$$ LeakyReLU(x) = max(\alpha x, x) $$ - **Ventajas:** Evita el problema
de "Dying ReLU" permitiendo pequeñas derivadas para valores negativos. -
**Desventajas:** Introduce un hiperparámetro adicional ($\alpha$).

#### 3.5. Función ELU (Exponential Linear Unit)

$$ ELU(x) = \begin{cases} x & \text{si } x > 0 \\ \alpha (e^x - 1) & \text{si } x \leq 0 \end{cases} $$ -
**Ventajas:** Mejora el flujo de gradientes en redes profundas. -
**Desventajas:** Más costosa computacionalmente que ReLU.

#### 3.6. Función Softmax

$$ Softmax(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}} $$ - **Ventajas:**
Convierte salidas en probabilidades, útil en clasificación multiclase. -
**Desventajas:** Sensible a valores extremos en la entrada.

### Visualización de funciones de activación

Podemos visualizar cómo estas funciones transforman sus entradas:

``` python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

x = np.linspace(-5, 5, 100)

activations = {
    'Sigmoid': 1 / (1 + np.exp(-x)),
    'Tanh': np.tanh(x),
    'ReLU': np.maximum(0, x),
    'Leaky ReLU': np.where(x > 0, x, 0.01 * x),
    'ELU': np.where(x > 0, x, np.exp(x) - 1)
}

plt.figure(figsize=(10, 6))
for name, func in activations.items():
    plt.plot(x, func, label=name)
plt.legend()
plt.title('Funciones de Activación')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
```

------------------------------------------------------------------------

## 4. Implementación de una Red Neuronal con 3 Entradas, 1 Capa Oculta y 2 Salidas

Para comprender cómo aplicar los conceptos teóricos en una red neuronal
real, construiremos una red con las siguientes características:

- **Entradas:** 3 neuronas
- **Capa oculta:** 1 capa con 2 neuronas
- **Salida:** 2 neuronas (para clasificación binaria o regresión con dos
variables de salida)

### 4.1. Implementación en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim

# Definición de la red neuronal
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.hidden = nn.Linear(3, 2)  # Capa oculta con 2 neuronas
        self.output = nn.Linear(2, 2)  # Capa de salida con 2 neuronas
    
    def forward(self, x):
        x = torch.relu(self.hidden(x))
        x = self.output(x)  # Sin activación para regresión o softmax para clasificación
        return x

# Creación del modelo
model = SimpleNN()

# Definición de la función de pérdida y el optimizador
criterion = nn.MSELoss()  # Para regresión, usar CrossEntropyLoss para clasificación
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Datos de ejemplo
X_train = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]], dtype=torch.float32)
y_train = torch.tensor([[0.5, 0.7], [0.2, 0.3], [0.9, 1.0]], dtype=torch.float32)

# Entrenamiento de la red neuronal
for epoch in range(1000):
    optimizer.zero_grad()
    output = model(X_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()

# Evaluación del modelo
print("Salida final:", model(X_train).detach().numpy())
```

### 4.2. Implementación en Keras

``` python
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Definir el modelo en Keras
model = keras.Sequential([
    keras.layers.Dense(2, activation='relu', input_shape=(3,)),
    keras.layers.Dense(2, activation='linear')  # Sin activación para regresión
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse')

# Datos de entrenamiento
X_train = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
y_train = np.array([[0.5, 0.7], [0.2, 0.3], [0.9, 1.0]])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=1000, verbose=0)

# Evaluación del modelo
print("Salida final:", model.predict(X_train))
```

------------------------------------------------------------------------

## 5. Extensión a Problemas de Clasificación

Tras haber construido una red para regresión, ahora adaptaremos la
arquitectura para problemas de clasificación. Usaremos la función de
activación **Softmax** en la capa de salida y la función de pérdida
**CrossEntropyLoss** en PyTorch y **categorical_crossentropy** en Keras.

### 5.1. Implementación en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim

# Definición de la red neuronal para clasificación
class ClassificationNN(nn.Module):
    def __init__(self):
        super(ClassificationNN, self).__init__()
        self.hidden = nn.Linear(3, 2)  # Capa oculta con 2 neuronas
        self.output = nn.Linear(2, 2)  # Capa de salida con 2 neuronas
    
    def forward(self, x):
        x = torch.relu(self.hidden(x))
        x = torch.softmax(self.output(x), dim=1)  # Softmax para clasificación
        return x

# Creación del modelo
model = ClassificationNN()

# Definición de la función de pérdida y el optimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Datos de ejemplo
X_train = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]], dtype=torch.float32)
y_train = torch.tensor([0, 1, 1], dtype=torch.long)  # Etiquetas de clase

# Entrenamiento de la red neuronal
for epoch in range(1000):
    optimizer.zero_grad()
    output = model(X_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()

# Evaluación del modelo
print("Salida final (probabilidades):", model(X_train).detach().numpy())
```

### 5.2. Implementación en Keras

``` python
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Definir el modelo en Keras
model = keras.Sequential([
    keras.layers.Dense(2, activation='relu', input_shape=(3,)),
    keras.layers.Dense(2, activation='softmax')  # Softmax para clasificación
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Datos de entrenamiento
X_train = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
y_train = np.array([0, 1, 1])  # Etiquetas de clase

# Entrenar el modelo
model.fit(X_train, y_train, epochs=1000, verbose=0)

# Evaluación del modelo
print("Salida final (probabilidades):", model.predict(X_train))
```

------------------------------------------------------------------------

## 6. Evaluación y Ajuste del Modelo

Después de entrenar un modelo, es crucial evaluar su rendimiento y
ajustarlo para mejorar su precisión. Examinaremos métricas de evaluación
y estrategias de ajuste en modelos de clasificación.

### 6.1. Métricas de Evaluación

Para evaluar la calidad del modelo, usamos métricas como:

-   \- **Precisión (Accuracy)**: Proporción de predicciones correctas.

-   \- **Matriz de Confusión**: Tabla que muestra predicciones correctas
    e incorrectas.

-   \- **Precisión, Recall y F1-score**:

    -   \- **Precisión**: $\frac{TP}{TP + FP}$

    -   \- **Recall**: $\frac{TP}{TP + FN}$

    -   \- **F1-score**: Media armónica de precisión y recall.

Ejemplo en **PyTorch**:

``` python
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Predicciones del modelo
y_pred = model(X_train).argmax(dim=1).detach().numpy()

# Evaluación del modelo
print("Accuracy:", accuracy_score(y_train, y_pred))
print("Reporte de Clasificación:\n", classification_report(y_train, y_pred))
```

Ejemplo en **Keras**:

``` python
from sklearn.metrics import accuracy_score, classification_report

# Predicciones del modelo
y_pred = np.argmax(model.predict(X_train), axis=1)

# Evaluación del modelo
print("Accuracy:", accuracy_score(y_train, y_pred))
print("Reporte de Clasificación:\n", classification_report(y_train, y_pred))
```

### 6.2. Estrategias de Ajuste del Modelo

Para mejorar el rendimiento del modelo, se pueden aplicar las siguientes
técnicas:

- **Ajuste de la tasa de aprendizaje**: Reducirla progresivamente puede mejorar la convergencia.
- **Aumento del número de épocas**: Puede mejorar la generalización si el modelo no ha convergido.
- **Regularización (L1, L2, Dropout)**: Evita el sobreajuste.
- **Aumento de datos**: Introducir más ejemplos de entrenamiento mejora la robustez del modelo.

Ejemplo de **Regularización con Dropout** en **Keras**:

``` python
model = keras.Sequential([
    keras.layers.Dense(4, activation='relu', input_shape=(3,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(2, activation='softmax')
])
```

------------------------------------------------------------------------

## 7. Introducción a Redes Neuronales Convolucionales (CNN)

Las **Redes Neuronales Convolucionales (CNN)** son una arquitectura
especializada en el procesamiento de imágenes y datos con estructura
espacial. Utilizan capas convolucionales para detectar patrones y
características en los datos.

### 7.1. Componentes Claves de una CNN

-   **Capa Convolucional**: Aplica filtros para extraer características
    locales.
-   **Capa de Activación (ReLU)**: Introduce no linealidad en la red.
-   **Capa de Pooling (MaxPooling o AvgPooling)**: Reduce la
    dimensionalidad y mejora la generalización.
-   **Capas Densas**: Se conectan después de la extracción de
    características para realizar la clasificación.

### 7.2. Implementación de una CNN en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# Definir la arquitectura de la CNN
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(32 * 7 * 7, 10)  # Para imágenes de entrada 28x28
    
    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 32 * 7 * 7)
        x = self.fc1(x)
        return x

# Creación del modelo y configuración del entrenamiento
model = CNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 7.3. Implementación de una CNN en Keras

``` python
import tensorflow as tf
from tensorflow import keras

# Definir la arquitectura de la CNN en Keras
model = keras.Sequential([
    keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(28,28,1)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(32, (3,3), activation='relu'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

### 7.4. Aplicaciones de las CNN

-   **Reconocimiento de Imágenes** (Clasificación en datasets como
    CIFAR-10, MNIST, ImageNet).
-   **Detección de Objetos** (Usado en modelos como YOLO, Faster R-CNN).
-   **Reconocimiento Facial** (Implementado en sistemas de autenticación
    biométrica).

------------------------------------------------------------------------

## 8. Introducción a Redes Neuronales Recurrentes (RNN)

Las **Redes Neuronales Recurrentes (RNN)** están diseñadas para procesar
datos secuenciales, como texto, audio y series temporales. Su principal
característica es la capacidad de mantener memoria sobre entradas
previas mediante conexiones recurrentes.

### 8.1. Componentes Claves de una RNN

-   **Capa Recurrente**: Procesa datos secuenciales con memoria sobre
    estados anteriores.
-   **Capa de Activación (Tanh, ReLU)**: Introduce no linealidad en la
    red.
-   **Estados Ocultos**: Permiten el almacenamiento de información de
    pasos previos en la secuencia.
-   **Capas Densas**: Transforman los estados ocultos en la salida
    final.

### 8.2. Implementación de una RNN en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim

# Definir la arquitectura de la RNN
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # Estado inicial
        out, _ = self.rnn(x, h0)
        out = self.fc(out[:, -1, :])  # Tomamos la última salida de la secuencia
        return out

# Creación del modelo
model = RNN(input_size=10, hidden_size=20, output_size=2)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 8.3. Implementación de una RNN en Keras

``` python
import tensorflow as tf
from tensorflow import keras

# Definir la arquitectura de la RNN en Keras
model = keras.Sequential([
    keras.layers.SimpleRNN(20, activation='tanh', input_shape=(None, 10)),
    keras.layers.Dense(2, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

### 8.4. Aplicaciones de las RNN

-   **Procesamiento de Lenguaje Natural** (Traducción automática,
    generación de texto).
-   **Análisis de Series Temporales** (Predicción de datos financieros,
    climatológicos).
-   **Reconocimiento de Voz** (Conversión de voz a texto, asistentes
    virtuales).

------------------------------------------------------------------------

## 9. Redes Neuronales de Memoria a Largo Plazo (LSTM)

Las **Redes Neuronales de Memoria a Largo Plazo (LSTM)** son una mejora
de las RNN diseñadas para manejar secuencias largas y evitar el problema
del gradiente desaparecido. Incorporan **celdas de memoria** y
**puertas** para regular la información que se mantiene o se olvida.

### 9.1. Componentes Claves de una LSTM

-   **Puerta de Entrada**: Decide cuánta información nueva almacenar en
    la celda de memoria.
-   **Puerta de Olvido**: Regula cuánta información antigua descartar.
-   **Puerta de Salida**: Determina la información a enviar a la
    siguiente capa.
-   **Celda de Estado**: Memoria interna que acumula información a
    través del tiempo.

### 9.2. Implementación de una LSTM en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim

# Definir la arquitectura de la LSTM
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # Estado inicial
        c0 = torch.zeros(1, x.size(0), self.hidden_size)  # Estado de celda inicial
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])  # Tomamos la última salida de la secuencia
        return out

# Creación del modelo
model = LSTM(input_size=10, hidden_size=20, output_size=2)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 9.3. Implementación de una LSTM en Keras

``` python
import tensorflow as tf
from tensorflow import keras

# Definir la arquitectura de la LSTM en Keras
model = keras.Sequential([
    keras.layers.LSTM(20, activation='tanh', input_shape=(None, 10)),
    keras.layers.Dense(2, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

### 9.4. Aplicaciones de las LSTM

-   **Traducción automática** (Modelos de traducción neuronal como
    Google Translate).
-   **Generación de texto** (Redacción automática de artículos o
    subtítulos).
-   **Predicción de series temporales** (Análisis de tendencias en datos
    financieros, salud y climatología).
-   **Reconocimiento de actividades** (Identificación de patrones en
    datos de sensores).

------------------------------------------------------------------------

## 10. Redes Neuronales de Convolución Transpuesta (DCNN)

Las **Redes Neuronales de Convolución Transpuesta (DCNN)**, también
conocidas como *Deconvolutional Networks* o *Transposed Convolutional
Networks*, se utilizan en tareas donde se requiere aumentar la
resolución espacial de los datos, como en la generación de imágenes y la
superresolución.

### 10.1. Componentes Claves de una DCNN

-   **Capas de Convolución Transpuesta**: Operan de manera inversa a las
    convoluciones estándar, expandiendo la dimensionalidad de la imagen.
-   **Upsampling**: Permite aumentar la resolución de la imagen antes de
    aplicar convoluciones transpuestas.
-   **Capas de Activación (ReLU, Tanh, Sigmoid)**: Se utilizan para
    regular la salida del modelo.
-   **Capas Densas**: Se emplean en combinación con las convoluciones
    para reconstruir los datos de entrada.

### 10.2. Implementación de una DCNN en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim

# Definir la arquitectura de la DCNN
class DCNN(nn.Module):
    def __init__(self):
        super(DCNN, self).__init__()
        self.deconv1 = nn.ConvTranspose2d(100, 64, kernel_size=4, stride=2, padding=1)
        self.deconv2 = nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1)
        self.deconv3 = nn.ConvTranspose2d(32, 1, kernel_size=4, stride=2, padding=1)
    
    def forward(self, x):
        x = torch.relu(self.deconv1(x))
        x = torch.relu(self.deconv2(x))
        x = torch.sigmoid(self.deconv3(x))  # Salida en el rango [0,1]
        return x

# Creación del modelo
model = DCNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 10.3. Implementación de una DCNN en Keras

``` python
import tensorflow as tf
from tensorflow import keras

# Definir la arquitectura de la DCNN en Keras
model = keras.Sequential([
    keras.layers.Conv2DTranspose(64, (4,4), strides=2, padding='same', activation='relu', 
    input_shape=(8,8,100)),
    keras.layers.Conv2DTranspose(32, (4,4), strides=2, padding='same', activation='relu'),
    keras.layers.Conv2DTranspose(1, (4,4), strides=2, padding='same', activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse')
```

### 10.4. Aplicaciones de las DCNN

-   **Generación de imágenes** (Modelos como GAN utilizan capas
    convolucionales transpuestas para crear imágenes realistas).
-   **Superresolución de imágenes** (Aumento de la calidad de imágenes
    de baja resolución).
-   **Segmentación de imágenes** (Reconstrucción de contornos y objetos
    en visión por computadora).
-   **Conversión de mapas de características en imágenes** (Ejemplo:
    generación de mapas de calor para IA en imágenes médicas).

------------------------------------------------------------------------



## 11. Redes Neuronales Generativas Adversariales (GAN)

Las **Redes Generativas Adversariales (GAN)** son modelos compuestos por
dos redes neuronales que compiten entre sí: un **generador** y un
**discriminador**. Se utilizan ampliamente en la generación de imágenes,
mejora de calidad visual y síntesis de datos realistas.

### 11.1. Componentes Claves de una GAN

-   **Generador**: Crea muestras sintéticas similares a los datos
    reales.
-   **Discriminador**: Clasifica si una muestra es real o generada.
-   **Competencia entre ambos modelos**: El generador aprende a engañar
    al discriminador, mientras que este último mejora en la detección de
    falsificaciones.

### 11.2. Implementación de una GAN en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim

# Definición del Generador
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 784),
            nn.Tanh()
        )
    
    def forward(self, x):
        return self.model(x)

# Definición del Discriminador
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(784, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        return self.model(x)

# Creación de los modelos
generator = Generator()
discriminator = Discriminator()
```

### 11.3. Implementación de una GAN en Keras

``` python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, LeakyReLU

# Definir el Generador
generator = keras.Sequential([
    Dense(256, activation='relu', input_shape=(100,)),
    Dense(512, activation='relu'),
    Dense(784, activation='tanh')
])

# Definir el Discriminador
discriminator = keras.Sequential([
    Dense(512, activation='relu', input_shape=(784,)),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilación del Discriminador
discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

### 11.4. Aplicaciones de las GAN

-   **Generación de imágenes** (Creación de imágenes sintéticas para
    entrenar modelos de visión).
-   **Aumento de datos** (Generación de muestras adicionales en
    conjuntos de datos limitados).
-   **Mejora de resolución de imágenes** (Reducción de ruido y
    reconstrucción de detalles en imágenes de baja calidad).
-   **Creación de rostros sintéticos** (Modelos como StyleGAN pueden
    generar caras realistas).
    ------------------------------------------------------------------------

## 12. Redes Neuronales de Crecimiento de Grafo (GNN)

Las **Redes Neuronales de Crecimiento de Grafo (GNN)** están diseñadas
para trabajar con datos estructurados en forma de grafos, como redes
sociales, estructuras moleculares o sistemas de recomendación. Se
utilizan para aprender representaciones de nodos y relaciones en grafos
complejos.

### 12.1. Componentes Claves de una GNN

-   **Nodos**: Representan entidades en el grafo (ejemplo: usuarios en
    una red social).
-   **Aristas**: Representan conexiones o relaciones entre los nodos.
-   **Agregación de Vecindades**: Permite que un nodo incorpore
    información de sus vecinos para mejorar la representación de sus
    características.

### 12.2. Implementación de una GNN en PyTorch Geometric

``` python
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data

# Definición de la arquitectura de la GNN
class GNN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GNN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Creación de un grafo de ejemplo
edge_index = torch.tensor([[0, 1, 1, 2, 2, 3], [1, 0, 2, 1, 3, 2]], dtype=torch.long)
x = torch.tensor([[1], [2], [3], [4]], dtype=torch.float)
data = Data(x=x, edge_index=edge_index)

# Creación del modelo
model = GNN(in_channels=1, hidden_channels=4, out_channels=2)
```

### 12.3. Aplicaciones de las GNN

-   **Análisis de redes sociales** (Predicción de enlaces y
    clasificación de usuarios).
-   **Biología computacional** (Predicción de estructuras moleculares y
    proteínas).
-   **Sistemas de recomendación** (Recomendaciones basadas en relaciones
    de usuario-producto).
-   **Procesamiento de datos estructurados** (Aprendizaje en redes de
    tráfico y conocimiento).

------------------------------------------------------------------------

## 13. Redes Neuronales de Transformadores (Transformers)

Las **Redes Neuronales de Transformadores** son modelos diseñados para
procesar secuencias de datos en paralelo mediante mecanismos de
atención. Han revolucionado el procesamiento del lenguaje natural (PLN)
y otros dominios con estructuras secuenciales.

### 13.1. Componentes Claves de un Transformer

-   **Mecanismo de Atención (Self-Attention)**: Permite que cada
    elemento de una secuencia se relacione con otros, sin importar su
    distancia en la secuencia.
-   **Capa de Normalización (Layer Norm)**: Ayuda a estabilizar el
    entrenamiento y a mejorar la generalización.
-   **Redes Feedforward Posicionales**: Agregan no linealidad tras la
    atención.
-   **Codificación Posicional**: Como los Transformers no tienen memoria
    secuencial, se añaden vectores de posición a las entradas.
    
### Capas

El modelo Transformer generalmente está compuesto por:
1. **Capa de Embedding**: Transforma las palabras en vectores de características.
2. **Codificador**: Contiene varias capas, cada una con:
   - Un mecanismo de atención, específicamente "Multi-Head Self-Attention".
   - Una red neuronal feedforward completamente conectada.
3. **Decodificador**: Similar al codificador, pero incluye atención cruzada para relacionar la entrada y la salida.
4. **Capa de Salida**: Genera las predicciones o resultados.

#### Objetivo de las capas

1. **Capa de Embedding**:
   - Convierte las palabras o tokens en vectores numéricos que representan sus significados y relaciones semánticas.
   - Facilita el trabajo de las siguientes capas al representar los datos en un formato adecuado para el modelo.

2. **Codificador**:
   - Está compuesto por varias capas idénticas con dos subcomponentes principales:
     - **Mecanismo de Multi-Head Self-Attention**: Evalúa las relaciones entre diferentes palabras (o tokens) de la entrada, permitiendo que el modelo preste atención a las partes más relevantes del contexto.
     - **Red Feedforward**: Procesa cada token individualmente y ajusta la representación aprendida en el paso anterior.
   - El codificador genera representaciones enriquecidas de la entrada.

3. **Decodificador**:
   - También tiene varias capas como el codificador, pero incluye un tercer componente:
     - **Atención cruzada (Cross-Attention)**: Relaciona las representaciones de la entrada generadas por el codificador con las palabras generadas hasta el momento en la salida.
   - El decodificador genera secuencias de salida (como traducciones o textos generados).

4. **Capa de Salida**:
   - Convierte las representaciones internas del decodificador en predicciones finales, como palabras, etiquetas, o cualquier tipo de salida específica del modelo.

#### El mecanismo de atención
El mecanismo de atención, en el contexto de los Transformadores (Transformers), está compuesto por los siguientes elementos principales:

1. **Matriz de consultas (Query)**: Representa el token que "pregunta" a otros tokens en la secuencia sobre su relevancia.
2. **Matriz de claves (Key)**: Define la información contextual que un token ofrece a otros tokens.
3. **Matriz de valores (Value)**: Contiene la información real que se transmitirá según la atención asignada.
4. **Softmax**: Calcula los pesos de atención basándose en la similitud entre las consultas y las claves.
5. **Producto ponderado**: Multiplica los pesos de atención por los valores para generar la salida final de atención.

### ¿Qué hace el mecanismo de atención?
En pocas palabras, el mecanismo de atención permite que el modelo enfoque su atención en las partes más relevantes de la secuencia de entrada. A continuación, te explico su funcionamiento:

- Para cada token de la secuencia, se calcula cuánto debe "prestar atención" a los demás tokens (o incluso a sí mismo). Esto se hace midiendo la similitud entre las matrices de consultas y claves mediante el producto escalar.
- Los pesos resultantes (tras pasar por Softmax para normalizarlos) determinan la importancia relativa de cada token.
- Finalmente, los pesos se usan para combinar los valores en una representación enriquecida.

Por ejemplo, en una tarea de traducción automática, el mecanismo de atención permite que el modelo relacione palabras en un idioma con sus contrapartes relevantes en otro idioma, incluso si las palabras no están en el mismo orden.

El poder del mecanismo de atención radica en su capacidad para modelar relaciones a larga distancia en los datos secuenciales.

### 13.2. Implementación de un Transformer en PyTorch

``` python
import torch
import torch.nn as nn

# Definición de la arquitectura del Transformer
class TransformerModel(nn.Module):
    def __init__(self, input_dim, model_dim, num_heads, num_layers, output_dim):
        super(TransformerModel, self).__init__()
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=model_dim, nhead=num_heads)
        self.transformer_encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(model_dim, output_dim)
    
    def forward(self, x):
        x = self.transformer_encoder(x)
        x = self.fc(x.mean(dim=0))  # Promedio sobre la secuencia
        return x

# Creación del modelo
model = TransformerModel(input_dim=512, model_dim=512, num_heads=8, num_layers=6, output_dim=10)
```

### 13.3. Implementación de un Transformer en Keras

``` python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, LayerNormalization, MultiHeadAttention, Dropout, Input

# Definir una capa de Transformer personalizada
def transformer_block(embed_dim, num_heads, ff_dim, rate=0.1):
    inputs = Input(shape=(None, embed_dim))
    attention = MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)(inputs, inputs)
    norm1 = LayerNormalization(epsilon=1e-6)(inputs + attention)
    ffn = keras.Sequential([
        Dense(ff_dim, activation='relu'),
        Dense(embed_dim)
    ])
    ffn_output = ffn(norm1)
    norm2 = LayerNormalization(epsilon=1e-6)(norm1 + ffn_output)
    return keras.Model(inputs=inputs, outputs=norm2)

# Construcción del modelo con múltiples capas Transformer
input_layer = Input(shape=(None, 512))
x = transformer_block(512, 8, 2048)(input_layer)
x = Dense(10, activation='softmax')(x)
model = keras.Model(inputs=input_layer, outputs=x)

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

### 13.4. Aplicaciones de los Transformers

-   **Procesamiento del Lenguaje Natural (PLN)** (Traducción automática,
    modelos de lenguaje como GPT y BERT).
-   **Generación de Texto** (Resúmenes, generación de contenido
    automático).
-   **Visión por Computadora** (Modelos como Vision Transformer - ViT
    para análisis de imágenes).
-   **Aprendizaje Automático en Series Temporales** (Predicciones en
    datos financieros y científicos).

------------------------------------------------------------------------

## 14. Modelos Híbridos y Especializados

Además de las arquitecturas convencionales, existen modelos híbridos y
especializados diseñados para resolver problemas específicos, como la
reducción de dimensión, la detección de anomalías y la generación de
nuevas representaciones de datos.

### 14.1. Autoencoders

Los **autoencoders** son redes neuronales diseñadas para aprender una
representación comprimida de los datos de entrada. Se utilizan en tareas
como la eliminación de ruido, reducción de dimensiones y generación de
datos sintéticos.

#### Componentes Claves de un Autoencoder

-   **Codificador (Encoder):** Reduce la dimensionalidad de los datos.
-   **Capa Latente:** Representación comprimida de la entrada.
-   **Decodificador (Decoder):** Reconstruye los datos a partir de la
    capa latente.

#### Implementación de un Autoencoder en PyTorch

``` python
import torch
import torch.nn as nn

# Definición de la arquitectura del Autoencoder
class Autoencoder(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, latent_dim)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Linear(64, input_dim)
        )
    
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

# Creación del modelo
model = Autoencoder(input_dim=784, latent_dim=32)
```

#### Implementación de un Autoencoder en Keras

``` python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Input

# Definir la arquitectura del Autoencoder en Keras
input_layer = Input(shape=(784,))
encoded = Dense(64, activation='relu')(input_layer)
latent = Dense(32, activation='relu')(encoded)
decoded = Dense(64, activation='relu')(latent)
decoded = Dense(784, activation='sigmoid')(decoded)

# Construcción del modelo
autoencoder = keras.Model(inputs=input_layer, outputs=decoded)

# Compilar el modelo
autoencoder.compile(optimizer='adam', loss='mse')
```

### 14.2. Redes de Crecimiento Celular

Las **Redes de Crecimiento Celular** son modelos inspirados en procesos
biológicos que se utilizan para simular el desarrollo celular,
crecimiento de tejidos y evolución de organismos artificiales.

#### Aplicaciones de las Redes de Crecimiento Celular

-   **Modelado de procesos biológicos** (Crecimiento de tejidos y
    regeneración celular).
-   **Diseño de estructuras optimizadas** (Estructuras auto-organizadas
    en diseño computacional).
-   **Simulación de ecosistemas** (Modelos de interacción de organismos
    en entornos dinámicos).

------------------------------------------------------------------------

## 15. Ajuste de Hiperparámetros en Redes Neuronales

El ajuste de hiperparámetros es un paso crucial en el entrenamiento de
redes neuronales, ya que define el rendimiento y la estabilidad del
modelo. Uno de los hiperparámetros más importantes es la **tasa de
aprendizaje (learning rate)**.

### 15.1. Cómo elegir la tasa de aprendizaje óptima

La tasa de aprendizaje determina el tamaño del paso que da el
optimizador en cada iteración. Un valor muy alto puede hacer que el
modelo no converja y oscile, mientras que un valor demasiado bajo puede
hacer que el entrenamiento sea muy lento.

#### Estrategias para encontrar una buena tasa de aprendizaje:

-   **Búsqueda manual:** Probar distintos valores y observar el
    comportamiento.
-   **Búsqueda en escala logarítmica:** Probar tasas de aprendizaje en
    un rango amplio, como $10^{-3}$, $10^{-2}$, $10^{-1}$.
-   **Técnicas automáticas:** Uso de algoritmos como **Grid Search** o
    **Random Search**.
-   **Técnicas visuales:** Gráficos de la pérdida a lo largo del
    entrenamiento para observar si la red está aprendiendo
    correctamente.

### 15.2. Reducción Adaptativa de la Tasa de Aprendizaje

Para mejorar el entrenamiento, se pueden utilizar estrategias de ajuste
dinámico de la tasa de aprendizaje:

#### En **PyTorch** con un Scheduler.

Código de ejemplo

``` python
import torch.optim as optim

# Definir el optimizador
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Scheduler para reducir la tasa de aprendizaje si la pérdida no mejora
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=5, factor=0.5)

for epoch in range(50):
    loss = train_model()  # Función de entrenamiento
    scheduler.step(loss)  # Ajusta la tasa de aprendizaje automáticamente
```

#### En **Keras** con un Callback.

Código de ejemplo:

``` python
import tensorflow as tf
from tensorflow import keras

# Definir el callback para reducción de la tasa de aprendizaje
lr_callback = keras.callbacks.ReduceLROnPlateau(monitor='val_loss',
factor=0.5, patience=5, min_lr=1e-6)

# Entrenamiento con el callback
model.fit(X_train, y_train, epochs=50, callbacks=[lr_callback])
```

### 15.3. Comparación de Optimizadores

El **optimizador** es el algoritmo que ajusta los pesos de la red
neuronal utilizando el cálculo del gradiente. No debe confundirse con
**backpropagation**, que es el método utilizado para calcular esos
gradientes.

A lo largo del tiempo, han surgido diferentes optimizadores para mejorar
el entrenamiento de redes neuronales. Se presentan en orden de creación:

#### **1. Stochastic Gradient Descent (SGD)**

-   Método clásico basado en el **descenso del gradiente estocástico**.
-   Se actualizan los pesos en función de cada minibatch de datos.
-   Puede ser lento y sensible a la elección de la tasa de aprendizaje.

#### **2. Momentum (SGD + Momentum)**

-   Introduce una velocidad acumulada que ayuda a superar mínimos
    locales.

-   Se inspira en la física de movimiento (aceleración por inercia).

-   Se representa como:

    $$ v_t = \beta v_{t-1} + (1 - \beta) \nabla L $$
    $$ \theta_t = \theta_{t-1} - \alpha v_t $$

#### **3. RMSprop (Root Mean Square Propagation)**

-   Propone un ajuste adaptativo de la tasa de aprendizaje.
-   Divide el gradiente entre la raíz cuadrada de la media acumulativa
    de los gradientes al cuadrado.
-   Se evita el problema de oscilaciones en terrenos abruptos de la
    función de pérdida.

#### **4. Adam (Adaptive Moment Estimation)**

-   Combina **Momentum** y **RMSprop**.

-   Calcula una media móvil del gradiente y su magnitud, ajustando la
    tasa de aprendizaje de cada peso de manera independiente.

-   Fórmulas:

    $$ m_t = \beta_1 m_{t-1} + (1 - \beta_1) \nabla L $$
    $$ v_t = \beta_2 v_{t-1} + (1 - \beta_2) \nabla L^2 $$
    $$ \theta_t = \theta_{t-1} - \frac{\alpha m_t}{\sqrt{v_t} + \epsilon} $$

-   **Ventajas de Adam:**

    -   Funciona bien en la mayoría de los casos sin necesidad de ajuste
        manual.
    -   Es estable y eficiente en problemas con datos ruidosos.
    -   Se recomienda como optimizador predeterminado en redes
        neuronales profundas.

------------------------------------------------------------------------

### Conclusión

Cada optimizador tiene ventajas y desventajas dependiendo del problema y
el tipo de red neuronal. En general:

-   **SGD** es una opción básica, pero puede ser lenta.

-   **Momentum** mejora SGD al suavizar el camino hacia el óptimo.

-   **RMSprop** se usa comúnmente en redes recurrentes.

-   **Adam** es el más usado por su balance entre velocidad y
    estabilidad.

Al experimentar con diferentes optimizadores y tasas de aprendizaje, se
puede mejorar significativamente el desempeño de la red neuronal.

|     |
|:----|
|     |
|     |

## 16. Ejemplo Práctico con un Dataset Realista

Para aplicar los conceptos aprendidos, implementaremos una red neuronal
utilizando el dataset **MNIST**, que contiene imágenes de dígitos
escritos a mano. Se entrenará un modelo para clasificación de los
dígitos (0-9).

### 16.1. Implementación en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# Cargar el dataset MNIST
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# Definir la arquitectura de la red
class MNISTModel(nn.Module):
    def __init__(self):
        super(MNISTModel, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = x.view(-1, 28*28)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Inicializar modelo, pérdida y optimizador
model = MNISTModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entrenamiento del modelo
for epoch in range(5):
    for images, labels in trainloader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

### 16.2. Implementación en Keras

``` python
import tensorflow as tf
from tensorflow import keras

# Cargar dataset MNIST
dataset = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = dataset.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Definir el modelo
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compilar y entrenar
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=64)
```

### 16.3. Implementación en Flax (JAX)

``` python
import jax
import jax.numpy as jnp
import flax.linen as nn
import optax
from tensorflow.keras.datasets import mnist

# Cargar dataset
(x_train, y_train), _ = mnist.load_data()
x_train = x_train.astype(jnp.float32) / 255.0

# Definir la red en Flax
class MLP(nn.Module):
    @nn.compact
    def __call__(self, x):
        x = x.reshape(-1, 28*28)
        x = nn.relu(nn.Dense(128)(x))
        x = nn.Dense(10)(x)
        return x

# Inicializar modelo y optimizador
model = MLP()
params = model.init(jax.random.PRNGKey(0), jnp.ones([1, 28, 28]))
optimizer = optax.adam(learning_rate=0.001)
```

### 16.4. Implementación en Haiku (JAX)

``` python
import haiku as hk

def forward_fn(x):
    x = hk.Flatten()(x)
    x = hk.Linear(128)(x)
    x = jax.nn.relu(x)
    x = hk.Linear(10)(x)
    return x

# Transformar modelo en Haiku
model = hk.transform(forward_fn)
params = model.init(jax.random.PRNGKey(0), jnp.ones([1, 28, 28]))
```

### 16.5. Comparación de Implementaciones

| Librería | Backend    | Definición de Modelo |
|----------|------------|----------------------|
| PyTorch  | Tensor     | Clases (OOP)         |
| Keras    | TensorFlow | API secuencial       |
| Flax     | JAX        | Compact Methods      |
| Haiku    | JAX        | Funciones puras      |

Este ejemplo práctico muestra cómo implementar una red neuronal en
distintas librerías, facilitando la comparación de diferentes frameworks
de deep learning.

------------------------------------------------------------------------

## 17. Guía para la Selección de Parámetros e Hiperparámetros

El diseño de una red neuronal involucra la selección de múltiples
hiperparámetros que afectan su rendimiento. A continuación, se
proporciona una guía para elegir los mejores valores dependiendo del
problema a resolver.

### 17.1. Tasa de Aprendizaje (Learning Rate)

-   **Reglas generales:**
    -   Valores entre `0.001` y `0.01` suelen funcionar bien.
    -   **Muy alta**: Convergencia rápida, pero posible inestabilidad.
    -   **Muy baja**: Convergencia lenta, riesgo de quedar atrapado en
        mínimos locales.
-   **Estrategias de ajuste:**
    -   Uso de técnicas como **ReduceLROnPlateau** o **Learning Rate
        Schedulers**.
    -   Implementar **búsqueda en escala logarítmica**
        (`10^{-3}, 10^{-4}, 10^{-5}`).

### 17.2. Número de Entradas y Salidas

-   **Entradas:**
    -   Determinado por la cantidad de características del dataset.
    -   Normalizar o estandarizar los datos mejora la convergencia.
-   **Salidas:**
    -   **Clasificación binaria**: 1 neurona con activación
        **sigmoide**.
    -   **Clasificación multiclase**: N neuronas con activación
        **softmax**.
    -   **Regresión**: 1 neurona con activación **lineal**.

### 17.3. Función de Pérdida (Error)

| Tipo de Problema         | Función de Pérdida       |
|--------------------------|--------------------------|
| Regresión                | MSE, MAE                 |
| Clasificación Binaria    | Binary CrossEntropy      |
| Clasificación Multiclase | Categorical CrossEntropy |

### 17.4. Optimizador

| Optimizador | Descripción |
|------------------------------------|------------------------------------|
| **SGD** | Descenso de gradiente simple. Lento pero útil para convergencia estable. |
| **Momentum** | Introduce velocidad acumulada para superar mínimos locales. |
| **RMSprop** | Ajusta adaptativamente la tasa de aprendizaje por parámetro. |
| **Adam** | Combinación de Momentum y RMSprop. Ideal para la mayoría de los casos. |

**Recomendación:** Si no se tiene conocimiento previo, **Adam** suele
ser una buena opción inicial.

### 17.5. Número de Capas Ocultas

-   **Reglas generales:**
    -   Para datos simples, 1 o 2 capas ocultas pueden ser suficientes.
    -   Para problemas más complejos (como imágenes o texto), usar más
        capas.
-   **Métodos de búsqueda:**
    -   **Grid Search / Random Search**.
    -   **Búsqueda progresiva**: Comenzar con pocas capas y aumentar
        gradualmente.

### 17.6. Número de Neuronas por Capa

-   **Reglas generales:**
    -   **Demasiadas neuronas**: Sobreajuste y cómputo innecesario.
    -   **Muy pocas neuronas**: Subajuste, modelo incapaz de aprender
        patrones.
-   **Reglas empíricas:**
    -   Número de neuronas en una capa oculta: entre el número de
        entradas y salidas.
    -   Experimentos con múltiplos de 16 o 32 pueden mejorar eficiencia
        en GPUs.

### 17.7. Función de Transferencia / Activación

| Función de Activación | Características |
|------------------------------------|------------------------------------|
| **ReLU** | Rápida, evita gradiente desaparecido, recomendada para capas ocultas. |
| **Leaky ReLU** | Variante de ReLU que soluciona el problema de neuronas muertas. |
| **Sigmoid** | Útil en salidas para clasificación binaria, pero propensa a saturación. |
| **Tanh** | Similar a sigmoid, pero centrada en 0. Mejor para normalización. |
| **Softmax** | Útil para clasificación multiclase. |

### 17.8. Estrategias de Ajuste de Hiperparámetros

-   **Búsqueda aleatoria (Random Search)**: Más eficiente que Grid
    Search.
-   **Optimización Bayesiana**: Ajuste automático en función de
    iteraciones previas.
-   **Validación Cruzada**: Evaluar modelos con distintos conjuntos de
    datos.

------------------------------------------------------------------------

### 17.9. Ejemplo Completo de Búsqueda de Hiperparámetros

Para ilustrar cómo seleccionar hiperparámetros óptimos, implementaremos
una búsqueda de hiperparámetros utilizando **Grid Search** en
**PyTorch** y **Keras** con el dataset MNIST.

#### Implementación en PyTorch

``` python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from itertools import product

# Cargar datos
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# Definir la red neuronal
class Model(nn.Module):
    def __init__(self, hidden_units, activation):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(28*28, hidden_units)
        self.fc2 = nn.Linear(hidden_units, 10)
        self.activation = activation
    
    def forward(self, x):
        x = x.view(-1, 28*28)
        x = self.activation(self.fc1(x))
        x = self.fc2(x)
        return x

# Definir hiperparámetros a probar
hidden_units_list = [64, 128, 256]
learning_rates = [0.1, 0.01, 0.001]
activations = [torch.relu, torch.tanh]

# Grid Search
for hidden_units, lr, activation in product(hidden_units_list, learning_rates, activations):
    model = Model(hidden_units, activation)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    print(f"Entrenando con {hidden_units} unidades ocultas, lr={lr}, activación={activation.__name__}")
    for epoch in range(3):  # Solo 3 épocas para pruebas
        for images, labels in trainloader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
```

#### Implementación en Keras

``` python
import tensorflow as tf
from tensorflow import keras
from itertools import product

# Cargar dataset MNIST
dataset = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = dataset.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Definir función para construir el modelo
def build_model(hidden_units, activation):
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(hidden_units, activation=activation),
        keras.layers.Dense(10, activation='softmax')
    ])
    return model

# Definir hiperparámetros a probar
hidden_units_list = [64, 128, 256]
learning_rates = [0.1, 0.01, 0.001]
activations = ['relu', 'tanh']

# Grid Search
for hidden_units, lr, activation in product(hidden_units_list, learning_rates, activations):
    model = build_model(hidden_units, activation)
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=lr), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    print(f"Entrenando con {hidden_units} unidades ocultas, lr={lr}, activación={activation}")
    model.fit(x_train, y_train, epochs=3, batch_size=64, verbose=1)
```

------------------------------------------------------------------------

Este ejemplo demuestra cómo probar distintas configuraciones de
hiperparámetros utilizando una estrategia de **Grid Search**. Se puede
extender usando **Random Search** o técnicas más avanzadas como
**Optimización Bayesiana**.

## Apéndice I: Perceptrón

``` python
import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    # Fill in code
    for i in range(len(X)):
        p=prediction(X[i], W, b)
        if p < y[i]:
            W = W + learn_rate * X[i].reshape(-1,1)
            b += learn_rate
        elif p > y[i]:
            W = W - learn_rate * X[i].reshape(-1,1)
            b -= learn_rate
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines
```

Otra forma de escribir la función del paso del perceptrón

``` python
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b
```

## 18. Monitorización y Explicabilidad del Modelo

### 18.1. Uso de TensorBoard para Explorar el Aprendizaje y los Datos

TensorBoard es una herramienta útil para visualizar métricas de
entrenamiento, gráficos de la arquitectura del modelo, hiperparámetros y
distribuciones de datos.

#### **Configuración de TensorBoard en Keras para Visualizar el Entrenamiento y Datos**

``` python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import TensorBoard
import datetime

# Definir directorio de logs
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1, write_graph=True, write_images=True)

# Entrenar el modelo con el callback de TensorBoard
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_val, y_val), callbacks=[tensorboard_callback])
```

Para visualizar los resultados:

``` sh
tensorboard --logdir=logs/fit
```

#### **Configuración de TensorBoard en PyTorch para Visualizar Métricas, Hiperparámetros y Distribuciones de Datos**

``` python
from torch.utils.tensorboard import SummaryWriter
import torch
import torch.nn as nn
import torch.optim as optim

# Inicializar TensorBoard
writer = SummaryWriter("runs/covid_risk_model")

# Modelo de ejemplo
model = COVIDRiskModel()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Registrar hiperparámetros
writer.add_text("Hiperparámetros", "Optimizador: Adam, LR: 0.001, Función de Pérdida: BCELoss")

# Entrenamiento con logging en TensorBoard
for epoch in range(20):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    writer.add_scalar("Loss/train", loss.item(), epoch)
    writer.add_histogram("Pesos de la capa oculta", model.fc1.weight, epoch)

# Registrar imágenes de datos de entrada
img_grid = torchvision.utils.make_grid(torch.tensor(X_train[:10].reshape(-1, 1, 28, 28)))
writer.add_image("Ejemplo de datos de entrada", img_grid)

writer.close()
```

Para visualizar los logs:

``` sh
tensorboard --logdir=runs/covid_risk_model
```

------------------------------------------------------------------------

### 18.2. Explicabilidad del Modelo con SHAP y LIME

Las técnicas de **explicabilidad** ayudan a entender cómo un modelo toma
decisiones y qué características influyen en la predicción.

#### **Explicabilidad con SHAP en Keras**

``` python
import shap
import numpy as np

# Crear un explainer para el modelo Keras
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Visualizar la importancia de las características
shap.summary_plot(shap_values, X_test, feature_names=features)
```

#### **Explicabilidad con SHAP en PyTorch**

``` python
import shap
import torch

# Crear un explainer para PyTorch
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Visualizar la importancia de las características
shap.summary_plot(shap_values, X_test.numpy(), feature_names=features)
```

#### **Explicabilidad con LIME en Keras**

``` python
from lime.lime_tabular import LimeTabularExplainer

# Inicializar el explicador
explainer = LimeTabularExplainer(X_train, feature_names=features, class_names=['No Riesgo', 'Riesgo'], discretize_continuous=True)

# Explicación de una instancia específica
exp = explainer.explain_instance(X_test[0], model.predict)
exp.show_in_notebook()
```

#### **Explicabilidad con LIME en PyTorch**

``` python
from lime.lime_tabular import LimeTabularExplainer
import torch.nn.functional as F

# Definir función para LIME
def predict_fn(x):
    x_tensor = torch.tensor(x, dtype=torch.float32)
    return F.softmax(model(x_tensor), dim=1).detach().numpy()

# Inicializar el explicador
explainer = LimeTabularExplainer(X_train, feature_names=features, class_names=['No Riesgo', 'Riesgo'], discretize_continuous=True)

# Explicación de una instancia específica
exp = explainer.explain_instance(X_test[0], predict_fn)
exp.show_in_notebook()
```

------------------------------------------------------------------------

### **Conclusión**

Con **TensorBoard**, se pueden analizar métricas del entrenamiento en
tiempo real, explorar hiperparámetros y visualizar distribuciones de los
datos. Además, con **SHAP** y **LIME**, se pueden explicar las
decisiones del modelo para mejorar la interpretabilidad y detectar
posibles sesgos en los datos.

------------------------------------------------------------------------

## 19. Comparación con Modelos Tradicionales

Antes de entrenar una red neuronal, es útil compararla con modelos
tradicionales como **Regresión Logística** o **Árboles de Decisión**
para evaluar si el modelo neuronal aporta mejoras significativas.

### 19.1. Implementación de un Modelo Base con Regresión Logística

#### **Regresión Logística en Scikit-Learn**

``` python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Definir el modelo
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)

# Evaluación del modelo
y_pred = logistic_model.predict(X_test)
print("Precisión del modelo de Regresión Logística:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

### 19.2. Implementación de un Árbol de Decisión

``` python
from sklearn.tree import DecisionTreeClassifier

# Definir el modelo
tree_model = DecisionTreeClassifier(max_depth=5)
tree_model.fit(X_train, y_train)

# Evaluación del modelo
y_pred_tree = tree_model.predict(X_test)
print("Precisión del modelo de Árbol de Decisión:", accuracy_score(y_test, y_pred_tree))
print(classification_report(y_test, y_pred_tree))
```

### 19.3. Comparación con la Red Neuronal

Después de entrenar y evaluar la red neuronal, se puede comparar su
desempeño con los modelos tradicionales:

| Modelo              | Precisión |
|---------------------|-----------|
| Regresión Logística | XX.X%     |
| Árbol de Decisión   | XX.X%     |
| Red Neuronal        | XX.X%     |

Si la red neuronal no supera significativamente a los modelos
tradicionales, puede ser necesario:

- **Ajustar hiperparámetros**.
- **Agregar más datos de entrenamiento**.
- **Reducir la complejidad de la red para evitar sobreajuste**.

------------------------------------------------------------------------

## 20. Ajuste de Hiperparámetros Automatizado

El ajuste de hiperparámetros puede realizarse manualmente mediante
prueba y error, pero existen técnicas automáticas más eficientes como
**Optuna** y **Hyperopt**, que optimizan la búsqueda del mejor conjunto
de parámetros de forma inteligente.

### 20.1. Carga de Datos y Preprocesamiento

Para ilustrar el ajuste de hiperparámetros, utilizaremos el dataset
**Breast Cancer Wisconsin** de `sklearn.datasets`. Este dataset es
adecuado para clasificación binaria y tiene múltiples características
clínicas relevantes.

``` python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Cargar dataset
cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalización
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

------------------------------------------------------------------------

### 20.2. Búsqueda de Hiperparámetros con Optuna en PyTorch

Optuna es una herramienta poderosa para optimizar hiperparámetros
mediante búsqueda bayesiana y estrategias de pruning.

``` python
import optuna
import torch
import torch.nn as nn
import torch.optim as optim

# Convertir datos a tensores
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

# Definir la función objetivo para Optuna
def objective(trial):
    hidden_units = trial.suggest_int('hidden_units', 32, 256)
    lr = trial.suggest_loguniform('lr', 1e-4, 1e-2)
    activation = trial.suggest_categorical('activation', [nn.ReLU(), nn.Tanh()])
    
    class Model(nn.Module):
        def __init__(self):
            super(Model, self).__init__()
            self.fc1 = nn.Linear(X_train.shape[1], hidden_units)
            self.fc2 = nn.Linear(hidden_units, 1)
            self.activation = activation
        
        def forward(self, x):
            x = self.activation(self.fc1(x))
            x = torch.sigmoid(self.fc2(x))
            return x
    
    model = Model()
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    for epoch in range(10):
        optimizer.zero_grad()
        outputs = model(X_train_tensor)
        loss = criterion(outputs, y_train_tensor)
        loss.backward()
        optimizer.step()
    
    with torch.no_grad():
        y_pred = model(X_test_tensor).round()
        accuracy = (y_pred == y_test_tensor).float().mean().item()
    
    return accuracy

# Ejecutar la búsqueda de hiperparámetros
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)
print("Mejor conjunto de hiperparámetros:", study.best_params)
```

------------------------------------------------------------------------

### 20.3. Búsqueda de Hiperparámetros con Hyperopt en Keras

Hyperopt es otra herramienta útil basada en búsqueda bayesiana para
optimizar hiperparámetros de modelos de deep learning en Keras.

``` python
from hyperopt import hp, tpe, fmin, Trials
import tensorflow as tf
from tensorflow import keras

# Definir la función objetivo
def objective(params):
    model = keras.Sequential([
        keras.layers.Dense(int(params['hidden_units']), activation=params['activation'], input_shape=(X_train.shape[1],)),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=params['lr']),
                  loss='binary_crossentropy', metrics=['accuracy'])
    
    history = model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0, validation_split=0.1)
    
    return -history.history['val_accuracy'][-1]

# Definir el espacio de búsqueda
space = {
    'hidden_units': hp.quniform('hidden_units', 32, 256, 32),
    'lr': hp.loguniform('lr', -4, -2),
    'activation': hp.choice('activation', ['relu', 'tanh'])
}

# Ejecutar la búsqueda
t_best = fmin(fn=objective, space=space, algo=tpe.suggest, max_evals=20, trials=Trials())
print("Mejor conjunto de hiperparámetros:", t_best)
```

------------------------------------------------------------------------

### 20.4. Comparación de Optuna y Hyperopt

| Herramienta | Algoritmo de Búsqueda | Soporte | Facilidad de Uso |
|------------------|------------------|------------------|------------------|
| Optuna | Búsqueda Bayesiana + Pruning | PyTorch, Keras | Fácil de implementar |
| Hyperopt | Búsqueda Bayesiana | Keras | Más flexible pero menos automático |

------------------------------------------------------------------------

### **Conclusión**

Optuna y Hyperopt permiten encontrar los mejores hiperparámetros sin
necesidad de hacer prueba y error manualmente. Estas técnicas son
fundamentales para mejorar el rendimiento de los modelos de redes
neuronales de manera eficiente.

## 21. Explicabilidad Mejorada con DeepLIFT y Captum

Explicar las decisiones de una red neuronal es crucial para comprender
su comportamiento y mejorar la interpretabilidad. A continuación, se
presentan técnicas avanzadas de explicabilidad con **DeepLIFT** y
**Captum (PyTorch)**.

### 21.1. Explicabilidad con DeepLIFT en Keras

DeepLIFT (Deep Learning Important Features) compara la activación de
cada neurona con una referencia base y permite analizar la contribución
de cada característica a la predicción del modelo.

#### **Implementación de DeepLIFT en Keras**

``` python
import shap
import numpy as np

# Crear un explainer para el modelo Keras
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Visualizar la importancia de las características
shap.summary_plot(shap_values, X_test, feature_names=cancer.feature_names)
```

------------------------------------------------------------------------

### 21.2. Explicabilidad con Captum en PyTorch

Captum es una librería de PyTorch diseñada para analizar la
interpretabilidad de modelos de aprendizaje profundo. Proporciona
herramientas para visualizar cómo influyen las características en las
predicciones.

#### **Implementación de Captum en PyTorch**

``` python
import torch
import captum.attr as attr
import matplotlib.pyplot as plt

# Inicializar el modelo entrenado
model.eval()

# Convertir una muestra de entrada en tensor
input_tensor = torch.tensor(X_test[0], dtype=torch.float32).unsqueeze(0)
input_tensor.requires_grad = True

# Definir el método de atribución (Integrated Gradients)
ig = attr.IntegratedGradients(model)
attributions = ig.attribute(input_tensor, target=0)

# Visualizar la importancia de cada característica
plt.figure(figsize=(10, 5))
plt.bar(cancer.feature_names, attributions.detach().numpy().flatten())
plt.xticks(rotation=90)
plt.ylabel("Importancia de la característica")
plt.title("Importancia de las características con Captum")
plt.show()
```

------------------------------------------------------------------------

### 21.3. Comparación de Técnicas de Explicabilidad

| Técnica  | Framework | Método                              |
|----------|-----------|-------------------------------------|
| DeepLIFT | Keras     | Comparación con referencia base     |
| Captum   | PyTorch   | Atribución de gradientes integrados |

------------------------------------------------------------------------

### **Conclusión**

Las técnicas de explicabilidad como **DeepLIFT y Captum** permiten
analizar cómo un modelo toma decisiones y qué características influyen
en las predicciones. Esto es clave para la auditoría de modelos y la
detección de sesgos en datos.


## Apéndice 1 Lotes (batches)

### **¿Qué es un lote (*batch*) en aprendizaje profundo?**  
Un **lote** (*batch*) es un subconjunto de datos del conjunto de entrenamiento que se procesa **antes de actualizar los pesos del modelo**. En lugar de calcular el gradiente para cada ejemplo individualmente (*Stochastic Gradient Descent, SGD*) o para todo el dataset (*Batch Gradient Descent*), se usa un **tamaño de lote intermedio** (*Mini-batch Gradient Descent*).

---

### **¿Por qué se usan lotes?**  
1. **Eficiencia computacional**  
   - Calcular el gradiente para todo el dataset (*Batch GD*) es costoso en memoria y tiempo.  
   - Procesar un ejemplo a la vez (*SGD*) es lento y ruidoso.  
   → **Los mini-lotes equilibran velocidad y estabilidad**.

2. **Convergencia más estable**  
   - *SGD puro* (batch=1) tiene alta varianza en las actualizaciones.  
   - *Batch completo* puede quedar atrapado en mínimos locales.  
   → **Los mini-lotes promedian el gradiente**, reduciendo ruido y mejorando la generalización.

3. **Aprovechamiento de hardware**  
   - Las GPUs/TPUs están optimizadas para operaciones matriciales paralelas.  
   - Procesar un lote de 32, 64 o 256 ejemplos es **más rápido** que procesarlos uno por uno.

---

### **¿Por qué los lotes son paralelizables?**  
1. **Operaciones matriciales**  
   - Las redes neuronales usan multiplicaciones de matrices (ej.: `input_batch @ weights`).  
   - Un lote se organiza como una matriz de tamaño `[batch_size, n_features]`, permitiendo que la GPU procese **todas las muestras del lote en paralelo**.

2. **Optimización en GPUs**  
   - Las GPUs tienen miles de núcleos que pueden calcular **gradientes para múltiples ejemplos simultáneamente**.  
   - Ejemplo: Si `batch_size=64`, la GPU procesa 64 muestras en paralelo (vs. 1 en SGD).

3. **Reducción de sobrecarga**  
   - Transferir datos a la GPU tiene un costo fijo. Procesar un lote grande **amortiza este costo** (vs. enviar datos ejemplo por ejemplo).

---

### **Elección del tamaño de lote (*batch_size*)**  
- **Lotes pequeños (ej.: 8-32)**:  
  - + Ruido en los gradientes → mejor generalización.  
  - – Más lento (menos paralelización).  
- **Lotes grandes (ej.: 256-1024)**:  
  - + Más rápido (mejor uso de GPU).  
  - – Riesgo de sobreajuste (*overfitting*) y peor convergencia.  
- **Valores típicos**: 32, 64, 128 (depende de la memoria de la GPU).

---

### **Ejemplo en Keras**  
```python
model.fit(X_train, y_train, batch_size=64, epochs=10)
```
- Aquí, el modelo toma **64 muestras a la vez**, calcula el gradiente promedio y actualiza los pesos.

---

### **Resumen de conceptos clave**  
| Concepto               | Descripción                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **SGD (batch_size=1)** | Máxima varianza, lento, pero bueno para evitar mínimos locales.            |
| **Mini-batch**         | Balance entre velocidad y estabilidad (ej.: 32-256 muestras).              |
| **Batch completo**     | Costoso en memoria, converge suavemente pero puede quedar atascado.        |
| **Paralelización**     | Los lotes permiten a la GPU procesar múltiples muestras en paralelo.       |

**Conclusión**: Los lotes son esenciales para equilibrar velocidad, estabilidad y uso eficiente de hardware en el entrenamiento de modelos de deep learning. 🚀

*cálculo paso a paso para una red neuronal de **1 neurona** con **2 entradas** y un **lote de tamaño 2**. 
Esto implica que procesaremos simultáneamente **2 ejemplos** en cada iteración.* 
Te muestro cómo sería:

### Configuración
- **Entradas:** Cada ejemplo tiene 2 valores, así que el lote tendrá una matriz de forma `(2, 2)` (2 ejemplos con 2 características cada uno).
- **Pesos de la neurona:** \(w_1\) y \(w_2\), uno para cada entrada.
- **Bias:** \(b\), el término independiente de la neurona.
- **Activación:** La salida se calcula como una combinación lineal: \( y = w_1x_1 + w_2x_2 + b \).

### Datos de entrada
Supongamos que los datos de entrada y los pesos son:
```plaintext
Entradas (X): [[x11, x12],  # Primer ejemplo en el lote
               [x21, x22]]  # Segundo ejemplo en el lote

Pesos (w): [w1, w2]
Bias (b): b
```

### Cálculo para el lote
La red neuronal procesará ambos ejemplos simultáneamente en una sola operación matricial:
1. **Producto punto de los pesos con las entradas:**
   \[
   Y = X \cdot W + B
   \]
   En notación matricial:
   \[
   Y = \begin{bmatrix} 
   x_{11} & x_{12} \\ 
   x_{21} & x_{22} 
   \end{bmatrix} 
   \cdot 
   \begin{bmatrix} 
   w_1 \\ 
   w_2 
   \end{bmatrix} 
   + 
   b
   \]

   Si expandemos:
   \[
   y_1 = w_1x_{11} + w_2x_{12} + b \quad \text{(salida del primer ejemplo)}
   \]
   \[
   y_2 = w_1x_{21} + w_2x_{22} + b \quad \text{(salida del segundo ejemplo)}
   \]

2. **Resultado (salidas del lote):**
   El resultado será un vector:
   \[
   Y = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix}
   \]

### Ejemplo numérico
Supongamos los siguientes valores:
- \(X = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\)
- \(W = \begin{bmatrix} 0.5 \\ 1.0 \end{bmatrix}\)
- \(b = 0.1\)

#### Paso 1: Multiplicar entradas por pesos
\[
X \cdot W = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \cdot \begin{bmatrix} 0.5 \\ 1.0 \end{bmatrix} 
= \begin{bmatrix} (1 \cdot 0.5 + 2 \cdot 1.0) \\ (3 \cdot 0.5 + 4 \cdot 1.0) \end{bmatrix}
= \begin{bmatrix} 2.5 \\ 5.5 \end{bmatrix}
\]

#### Paso 2: Sumar el bias
\[
Y = \begin{bmatrix} 2.5 \\ 5.5 \end{bmatrix} + 0.1 = \begin{bmatrix} 2.6 \\ 5.6 \end{bmatrix}
\]

### Resultado final
Las salidas para los 2 ejemplos del lote son:
\[
Y = \begin{bmatrix} 2.6 \\ 5.6 \end{bmatrix}
\]

### Resumen
Usar un lote de tamaño 2 no significa que entrenas 2 redes neuronales distintas, sino que procesas 2 ejemplos en paralelo utilizando la **misma red neuronal**. Esto es eficiente gracias a las operaciones vectorizadas. 

