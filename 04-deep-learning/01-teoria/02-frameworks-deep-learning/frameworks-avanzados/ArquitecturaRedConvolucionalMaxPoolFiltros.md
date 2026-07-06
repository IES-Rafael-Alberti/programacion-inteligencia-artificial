### Definiendo la Arquitectura de la Red Neuronal

Este código define la arquitectura de una Red Neuronal Convolucional (CNN) utilizando PyTorch. Es similar a la utilizada en el tutorial de CIFAR-10, pero adaptada para Fashion-MNIST, que tiene imágenes en escala de grises (1 canal de color) en lugar de imágenes en RGB (3 canales de color).

```python
# 4. Definir la arquitectura de la red neuronal de forma parecida al tutorial de CIFAR-10,
# con la diferencia de que estas imágenes tienen un solo canal y aquellas tienen tres.
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 4 * 4)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()
```

### Explicación del Código

#### Definición de la Clase `Net`
Esta línea define una clase en Python llamada `Net`, que hereda de `nn.Module`.

```python
class Net(nn.Module):
```
`nn.Module` es la clase base para todos los módulos de redes neuronales en PyTorch. Heredar de esta clase proporciona la funcionalidad necesaria para construir y entrenar la red.

#### Constructor `__init__`
El constructor de la clase `Net` es donde se definen las capas de la red neuronal.

```python
def __init__(self):
    super(Net, self).__init__()
```
Esta línea inicializa la clase padre (`nn.Module`) para la clase `Net`.

#### Definición de Capas
```python
self.conv1 = nn.Conv2d(1, 6, 5)
```
- Define la primera capa convolucional (`conv1`).
- Toma una imagen en escala de grises (1 canal de entrada) y produce 6 mapas de características.
- Usa un kernel de tamaño `5x5`.

```python
self.pool = nn.MaxPool2d(2, 2)
```
- Define una capa de **max pooling** (`pool`) con un tamaño de kernel `2x2`.
- Reduce las dimensiones espaciales de la imagen para disminuir la cantidad de parámetros y la carga computacional.

```python
self.conv2 = nn.Conv2d(6, 16, 5)
```
- Define la segunda capa convolucional (`conv2`).
- Toma 6 mapas de características como entrada (de la capa anterior) y genera 16 mapas de salida.
- Usa un kernel de `5x5`.

```python
self.fc1 = nn.Linear(16 * 4 * 4, 120)
```
- Define la primera capa completamente conectada (`fc1`).
- Recibe una entrada de tamaño `16 * 4 * 4` (salida aplanada de la última capa convolucional) y produce una salida de tamaño `120`.

```python
self.fc2 = nn.Linear(120, 84)
```
- Define la segunda capa completamente conectada (`fc2`).
- Toma una entrada de tamaño `120` y genera una salida de tamaño `84`.

```python
self.fc3 = nn.Linear(84, 10)
```
- Define la tercera capa completamente conectada (`fc3`).
- Toma una entrada de tamaño `84` y genera una salida de tamaño `10` (las 10 clases de Fashion-MNIST).

#### Propagación hacia adelante `forward`
```python
def forward(self, x):
    x = self.pool(F.relu(self.conv1(x)))
    x = self.pool(F.relu(self.conv2(x)))
    x = x.view(-1, 16 * 4 * 4)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.fc3(x)
    return x
```
- Define la forma en que los datos fluyen a través de la red.
- Aplica convoluciones y activaciones ReLU (`F.relu`).
- Reduce las dimensiones con la capa de max pooling.
- Aplana la salida (`view(-1, 16 * 4 * 4)`) para alimentar las capas completamente conectadas.
- La última capa (`fc3`) genera las predicciones finales.

### ¿Qué Hace una Capa Convolucional?
Una **capa convolucional** es un bloque fundamental en las Redes Neuronales Convolucionales (CNNs) y se encarga de extraer características de las imágenes.

#### Función Principal:
- **Extracción de características**: Aprende automáticamente bordes, texturas y patrones en las imágenes.
- **Uso de filtros (kernels)**: Cada filtro es una pequeña matriz de pesos que se desplaza sobre la imagen.
- **Mapas de características**: Al aplicar los filtros, se crean mapas que representan la presencia e intensidad de ciertas características en distintas partes de la imagen.

Ejemplo de una capa convolucional en el código:
```python
self.conv1 = nn.Conv2d(1, 6, 5)
```
- Aplica `6` filtros de `5x5` a la imagen de entrada (escala de grises, 1 canal).
- Genera `6` mapas de características.

### ¿Qué Filtros Aplica?
Los filtros en una capa convolucional se **aprenden** durante el entrenamiento. A diferencia de los filtros predefinidos como **Sobel** o **Gaussianos**, las CNN aprenden automáticamente los filtros más relevantes para la tarea.

Ejemplo:
- Un filtro podría aprender a detectar **bordes horizontales**.
- Otro filtro podría especializarse en **texturas** o **curvas**.

Los filtros no están predefinidos, sino que se ajustan mediante un proceso de **retropropagación** (backpropagation) y optimización.

### ¿Cómo Se Aprenden los Filtros?
Los filtros se aprenden mediante el entrenamiento de la red con **backpropagation** y **descenso de gradiente**:

1. **Paso hacia adelante (Forward Pass)**: Se calcula la salida de la red usando los filtros actuales.
2. **Cálculo de pérdida (Loss Function)**: Se compara la salida con la etiqueta real.
3. **Retropropagación (Backpropagation)**: Se calcula el gradiente de los filtros con respecto a la pérdida.
4. **Actualización de pesos (Optimización)**: Se ajustan los pesos de los filtros para reducir la pérdida.

En el código:
```python
criterion = nn.CrossEntropyLoss()  # Función de pérdida
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9) # Algoritmo de optimización
```
- `CrossEntropyLoss()`: Función de pérdida para clasificación multiclase.
- `SGD`: Algoritmo de optimización que ajusta los pesos de los filtros.

### ¿Qué Hace la Capa de Max Pooling?
La **capa de max pooling** reduce el tamaño de los mapas de características, manteniendo las características más importantes.

#### Funciones Clave:
1. **Reducción de dimensionalidad**: Disminuye el número de parámetros y cálculos.
2. **Resistencia a pequeñas variaciones**: Si un objeto se desplaza ligeramente en la imagen, la red aún puede reconocerlo.
3. **Extracción de características más relevantes**: Selecciona los valores máximos en pequeñas regiones.

Ejemplo:
Dado un mapa de características de `4x4`:
```
[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 12]
[13, 14, 15, 16]
```
Aplicando max pooling `2x2`, obtenemos:
```
[6, 8]
[14, 16]
```
En el código:
```python
self.pool = nn.MaxPool2d(2, 2)
```
- Usa una ventana de `2x2`, reduciendo la imagen a la mitad en cada dimensión.

### Resumen
- **Capas convolucionales** aprenden filtros automáticamente.
- **Los filtros se optimizan** con retropropagación y descenso de gradiente.
- **Max pooling** reduce la dimensionalidad y mejora la eficiencia del modelo.

¡Espero que esta explicación sea útil! 🚀
