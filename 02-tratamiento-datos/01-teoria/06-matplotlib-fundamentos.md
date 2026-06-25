# Manual de Matplotlib para Análisis Exploratorio de Datos

## 1. Introducción a Matplotlib

Matplotlib es una biblioteca de visualización de datos en Python que proporciona una amplia gama de herramientas para crear gráficos estáticos, animados e interactivos. Es una de las bibliotecas más utilizadas en el ecosistema de ciencia de datos de Python debido a su flexibilidad y capacidad para generar visualizaciones de alta calidad.

### Configuración Inicial

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Configuración para mejorar la visualización
plt.style.use('seaborn')
# Para mostrar gráficos en Jupyter Notebook
%matplotlib inline
# Para establecer el tamaño predeterminado de las figuras
plt.rcParams['figure.figsize'] = [10, 6]
# Para mejorar la resolución de las figuras
plt.rcParams['figure.dpi'] = 100
```

## 2. Gráficos Básicos

### 2.1 Gráfico de Líneas

#### ¿Qué es?
Un gráfico de líneas muestra la relación entre dos variables continuas, conectando puntos de datos con líneas. Es especialmente útil para visualizar tendencias a lo largo del tiempo o secuencias ordenadas.

#### Uso en EDA
- Análisis de tendencias temporales
- Visualización de patrones cíclicos
- Comparación de múltiples series temporales

#### Ejemplo Básico

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Gráfico de Línea Simple')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
```

#### Modificaciones Comunes

```python
# Múltiples líneas con diferentes estilos
plt.figure(figsize=(12, 6))
plt.plot(x, np.sin(x), 'r--', label='Seno')
plt.plot(x, np.cos(x), 'b-', label='Coseno')
plt.plot(x, -np.sin(x), 'g:', label='-Seno')
plt.title('Múltiples Líneas con Diferentes Estilos')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
```

### 2.2 Gráfico de Barras

#### ¿Qué es?
Un gráfico de barras representa datos categóricos con rectángulos rectangulares de alturas proporcionales a los valores que representan.

#### Uso en EDA
- Comparación de cantidades entre categorías
- Visualización de distribuciones discretas
- Análisis de frecuencias

#### Ejemplo Básico

```python
categorias = ['A', 'B', 'C', 'D']
valores = [4, 3, 2, 5]

plt.figure(figsize=(8, 6))
plt.bar(categorias, valores)
plt.title('Gráfico de Barras Simple')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.show()
```

#### Modificaciones Avanzadas

```python
# Gráfico de barras horizontal con colores personalizados
plt.figure(figsize=(10, 6))
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
plt.barh(categorias, valores, color=colors)
plt.title('Gráfico de Barras Horizontal')
plt.xlabel('Valores')
plt.ylabel('Categorías')

# Añadir valores en las barras
for i, v in enumerate(valores):
    plt.text(v, i, str(v), va='center')

plt.show()
```

### 2.3 Histograma

#### ¿Qué es?
Un histograma es una representación gráfica de la distribución de datos numéricos mediante barras de diferentes alturas.

#### Uso en EDA
- Visualización de la distribución de datos
- Identificación de outliers
- Análisis de la forma de la distribución (simetría, modalidad)

#### Ejemplo Básico

```python
datos = np.random.normal(100, 15, 1000)

plt.figure(figsize=(10, 6))
plt.hist(datos, bins=30, edgecolor='black')
plt.title('Histograma Simple')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
```

#### Modificaciones Avanzadas

```python
# Histograma con densidad de probabilidad
plt.figure(figsize=(12, 6))
plt.hist(datos, bins=30, density=True, alpha=0.7, color='skyblue', 
         edgecolor='black', label='Histograma')

# Añadir curva de densidad
from scipy import stats
x_min, x_max = plt.xlim()
x = np.linspace(x_min, x_max, 100)
p = stats.norm.pdf(x, datos.mean(), datos.std())
plt.plot(x, p, 'k', linewidth=2, label='Curva Normal')

plt.title('Histograma con Curva de Densidad')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.legend()
plt.show()
```

### 2.4 Gráfico de Tarta (Pie Chart)

#### ¿Qué es?
Un gráfico de tarta muestra datos categóricos como sectores de un círculo, donde el área de cada sector es proporcional al valor que representa.

#### Uso en EDA
- Visualización de proporciones
- Análisis de composición
- Distribución de categorías

#### Ejemplo Básico

```python
categorias = ['A', 'B', 'C', 'D']
valores = [35, 25, 25, 15]

plt.figure(figsize=(8, 8))
plt.pie(valores, labels=categorias, autopct='%1.1f%%')
plt.title('Gráfico de Tarta Simple')
plt.show()
```

#### Modificaciones Avanzadas

```python
# Gráfico de tarta con explosión y colores personalizados
explode = (0.1, 0, 0, 0)
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

plt.figure(figsize=(10, 10))
plt.pie(valores, explode=explode, labels=categorias,
        colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')
plt.title('Gráfico de Tarta Personalizado')
plt.show()
```

### 2.5 Gráfico de Dispersión (Scatter Plot)

#### ¿Qué es?
Un gráfico de dispersión muestra la relación entre dos variables continuas mediante puntos en un plano cartesiano.

#### Uso en EDA
- Análisis de correlaciones
- Identificación de patrones
- Detección de clusters y outliers

#### Ejemplo Básico

```python
x = np.random.normal(0, 1, 100)
y = x + np.random.normal(0, 0.4, 100)

plt.figure(figsize=(10, 6))
plt.scatter(x, y)
plt.title('Gráfico de Dispersión Simple')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
```

#### Modificaciones Avanzadas

```python
# Scatter plot con tamaño y color variables
tamanios = np.random.randint(50, 500, 100)
colores = np.random.rand(100)

plt.figure(figsize=(12, 8))
scatter = plt.scatter(x, y, s=tamanios, c=colores, 
                     alpha=0.5, cmap='viridis')
plt.colorbar(scatter)
plt.title('Gráfico de Dispersión con Tamaño y Color Variables')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
```

## 3. Gráficos Avanzados

### 3.1 Mapa de Calor (Heatmap)

#### ¿Qué es?
Un mapa de calor representa datos mediante una matriz de colores donde cada color representa un valor.

#### Uso en EDA
- Visualización de correlaciones
- Análisis de matrices de datos
- Identificación de patrones en datos bidimensionales

#### Ejemplo Básico

```python
# Crear matriz de correlación
data = np.random.randn(10, 10)
correlation_matrix = np.corrcoef(data)

plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm')
plt.colorbar()
plt.title('Mapa de Calor Simple')
plt.show()
```

### 3.2 Gráfico de Violín (Violin Plot)

#### ¿Qué es?
Un gráfico de violín combina un boxplot con un kernel density plot para mostrar la distribución completa de los datos.

#### Uso en EDA
- Comparación de distribuciones entre grupos
- Análisis de la forma de las distribuciones
- Identificación de multimodalidad

#### Ejemplo Básico

```python
# Crear datos de ejemplo
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(80, 20, 200)
data3 = np.random.normal(90, 15, 200)

plt.figure(figsize=(10, 6))
plt.violinplot([data1, data2, data3])
plt.title('Gráfico de Violín')
plt.xticks([1, 2, 3], ['Grupo 1', 'Grupo 2', 'Grupo 3'])
plt.ylabel('Valores')
plt.show()
```

### 3.3 Gráfico de Superficie 3D

#### ¿Qué es?
Un gráfico de superficie 3D muestra una función de dos variables mediante una superficie tridimensional.

#### Uso en EDA
- Visualización de relaciones tridimensionales
- Análisis de superficies
- Modelado de funciones bivariadas

#### Ejemplo Básico

```python
from mpl_toolkits.mplot3d import Axes3D

# Crear datos
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Crear gráfico 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
plt.colorbar(surf)
ax.set_title('Gráfico de Superficie 3D')
plt.show()
```

### 3.4 Boxplot

#### ¿Qué es?
Un boxplot muestra la distribución de datos numéricos mediante cuartiles y valores atípicos.

#### Uso en EDA
- Identificación de outliers
- Comparación de distribuciones
- Análisis de la dispersión de datos

#### Ejemplo Básico

```python
# Crear datos de ejemplo
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure(figsize=(10, 6))
plt.boxplot(data)
plt.title('Boxplot Simple')
plt.xticks([1, 2, 3], ['Grupo 1', 'Grupo 2', 'Grupo 3'])
plt.ylabel('Valores')
plt.show()
```

### Consejos Generales para la Visualización

1. **Claridad**: Asegúrate de que tus gráficos sean claros y fáciles de interpretar.
2. **Consistencia**: Mantén un estilo consistente en todos tus gráficos.
3. **Color**: Usa colores que sean accesibles para personas con daltonismo.
4. **Etiquetas**: Siempre incluye títulos, etiquetas de ejes y leyendas claras.
5. **Tamaño**: Ajusta el tamaño de la figura según la cantidad de información.
6. **Formato**: Considera el formato final donde se mostrarán los gráficos.

### Parámetros Comunes

- **figsize**: Tuple que define el tamaño de la figura (ancho, alto)
- **dpi**: Resolución de la figura
- **color**: Color de los elementos gráficos
- **alpha**: Transparencia (0-1)
- **label**: Etiqueta para la leyenda
- **title**: Título del gráfico
- **xlabel/ylabel**: Etiquetas de los ejes
- **grid**: Mostrar/ocultar cuadrícula
- **legend**: Mostrar/ocultar leyenda

### Recursos Adicionales

- [Documentación oficial de Matplotlib](https://matplotlib.org/)
- [Galería de ejemplos de Matplotlib](https://matplotlib.org/stable/gallery/index.html)
- [Cheatsheet de Matplotlib](https://github.com/matplotlib/cheatsheets)
