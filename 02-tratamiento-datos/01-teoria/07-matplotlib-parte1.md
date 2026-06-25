---
title: "Tutorial de Matplotlib - Parte 1: Principales Gráficas y Parámetros de Configuración"
author: "Curso de Especialización en Inteligencia Artificial y Big Data"
subtitle: "Programación de Inteligencia Artificial — Semana 04"
date: "2025-11-03"
geometry: margin=2cm
output: 
    pdf_document:
        toc: true
        
fontsize: 11pt
---

# Tutorial de Matplotlib - Parte 1: Principales Gráficas y Parámetros de Configuración

## Introducción

Matplotlib es una de las bibliotecas más utilizadas para la visualización de datos en Python. A continuación, veremos los tipos de gráficos más comunes, explicando qué información proporcionan sobre los datos y cómo personalizar cada gráfico usando los parámetros disponibles en `Matplotlib`.

---

## 1. Gráfico de Líneas (`plt.plot`)

### ¿Qué es y para qué se usa?

Un gráfico de líneas es útil para visualizar la evolución o tendencia de una variable a lo largo del tiempo o de otra variable continua. Cada punto de datos se conecta con el siguiente mediante una línea, lo que facilita observar el cambio en los datos.

### Parámetros principales de `plt.plot`

- **x**: Coordenadas en el eje X. (`array` o `list` de valores numéricos)
- **y**: Coordenadas en el eje Y. (`array` o `list` de valores numéricos)
- **color**: Color de la línea. Valores comunes: `'b'`, `'r'`, `'g'`, etc. Valores hexadecimales también son válidos (p. ej., `'#FF5733'`).
- **linestyle**: Estilo de línea. Valores: `'-'` (línea continua), `'--'` (línea discontinua), `':'` (punteada).
- **linewidth**: Grosor de la línea. Valor por defecto: `1.5`. Puede ser un valor numérico mayor para líneas más gruesas.
- **marker**: Marcador de cada punto. Valores: `'.'`, `'o'`, `'v'`, `'^'`, etc.

### Ejemplo

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y, color='blue', linestyle='-', linewidth=2, marker='o')
plt.title("Gráfico de Línea")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
```

---

## 2. Gráfico de Barras (`plt.bar`)

### ¿Qué es y para qué se usa?

Un gráfico de barras muestra la comparación entre diferentes categorías. Es ideal para visualizar frecuencias, cantidades o cualquier métrica de comparación discreta.

### Parámetros principales de `plt.bar`

- **x**: Coordenadas en el eje X (categorías o valores discretos).
- **height**: Altura de las barras, correspondiente a los valores de cada categoría.
- **color**: Color de las barras. Puede ser un solo color o una lista de colores para cada barra.
- **width**: Ancho de cada barra. Valor por defecto: `0.8`.
- **align**: Alineación de las barras (`'center'` o `'edge'`).

### Ejemplo

```python
categorias = ['A', 'B', 'C', 'D']
valores = [5, 7, 2, 4]

plt.bar(categorias, valores, color='purple', width=0.6)
plt.title("Gráfico de Barras")
plt.xlabel("Categoría")
plt.ylabel("Valor")
plt.show()
```

---

## 3. Histograma (`plt.hist`)

### ¿Qué es y para qué se usa?

Un histograma muestra la distribución de una variable continua, dividiéndola en intervalos (bins) y contando el número de valores que caen en cada intervalo. Es útil para visualizar la forma y dispersión de los datos.

### Parámetros principales de `plt.hist`

- **x**: Valores de datos.
- **bins**: Número de intervalos o bins en los que dividir los datos. Valor por defecto: `10`.
- **range**: Rango de los datos en el eje X (`(min, max)`).
- **density**: Si se establece en `True`, muestra una distribución de probabilidad en lugar de frecuencias absolutas.
- **color**: Color de las barras del histograma.

### Ejemplo

```python
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='teal', density=True)
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.show()
```

---

## 4. Gráfico de Dispersión (`plt.scatter`)

### ¿Qué es y para qué se usa?

Un gráfico de dispersión muestra la relación entre dos variables numéricas. Cada punto representa una observación y permite observar tendencias y relaciones, incluyendo la detección de posibles correlaciones.

### Parámetros principales de `plt.scatter`

- **x**: Coordenadas en el eje X.
- **y**: Coordenadas en el eje Y.
- **color**: Color de los puntos. Puede ser un solo color o un array de valores para asignar colores distintos.
- **s**: Tamaño de los puntos. Valor por defecto: `20`. Puede ser un valor numérico o un array para asignar tamaños diferentes.
- **alpha**: Transparencia de los puntos. Valor por defecto: `1.0` (opaco).

### Ejemplo

```python
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 100

plt.scatter(x, y, color='blue', s=sizes, alpha=0.6)
plt.title("Gráfico de Dispersión")
plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.show()
```

---

## 5. Gráfico de Tarta (`plt.pie`)

### ¿Qué es y para qué se usa?

Un gráfico de tarta muestra la proporción de diferentes categorías en un conjunto de datos. Es útil para observar la distribución porcentual de una variable categórica.

### Parámetros principales de `plt.pie`

- **x**: Lista de valores para cada porción.
- **labels**: Etiquetas para cada segmento.
- **colors**: Colores de cada porción.
- **autopct**: Muestra los porcentajes dentro de cada porción, usando un formato como `'%1.1f%%'`.
- **startangle**: Ángulo de inicio. Valor por defecto: `0`.
- **explode**: Lista de valores para “separar” segmentos. Valor por defecto: `None`.

### Ejemplo

```python
sizes = [25, 35, 20, 20]
labels = ['A', 'B', 'C', 'D']
explode = (0, 0.1, 0, 0)

plt.pie(sizes, labels=labels, colors=['red', 'green', 'blue', 'yellow'], autopct='%1.1f%%', startangle=140, explode=explode)
plt.title("Gráfico de Tarta")
plt.show()
```

---

## 6. Boxplot (`plt.boxplot`)

### ¿Qué es y para qué se usa?

El boxplot es una visualización que muestra la mediana, los cuartiles y los valores atípicos de una distribución. Es muy útil para detectar outliers y analizar la dispersión de los datos.

### Parámetros principales de `plt.boxplot`

- **x**: Datos para el boxplot. Puede ser una lista de listas si se quieren comparar varias distribuciones.
- **vert**: Orientación del gráfico. `True` para vertical, `False` para horizontal.
- **patch_artist**: Si es `True`, rellena el boxplot con color.
- **notch**: Si es `True`, se muestra una muesca en el boxplot alrededor de la mediana.

### Ejemplo

```python
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert=True, patch_artist=True)
plt.title("Boxplot")
plt.xlabel("Grupo")
plt.ylabel("Valor")
plt.show()
```

---

Este primer tutorial cubre los gráficos más comunes de Matplotlib y cómo personalizarlos mediante parámetros. En la **segunda parte** veremos cómo configurar la apariencia y el tamaño de las gráficas en diferentes contextos, como pantallas o impresión.

---

# Tutorial de Matplotlib - Parte 2: Configuración de la Apariencia y Tamaño de las Gráficas

En esta parte, aprenderemos a ajustar la apariencia de las gráficas de Matplotlib para adaptarlas al contexto de visualización, explorando:

1. Los valores por defecto de Matplotlib.
2. Cómo ajustar el tamaño de las gráficas para distintos contextos.
3. Configurar múltiples gráficos en un mismo `plot`.
4. Definir y personalizar los ejes de las gráficas.

---

## 1. Valores por Defecto de Matplotlib

Matplotlib tiene un conjunto de configuraciones predefinidas que puedes personalizar según tus necesidades. Las configuraciones por defecto incluyen elementos como colores, tamaños de fuente, tamaño de figuras, y más.

### Configuración con `plt.rcParams`

Para cambiar los valores por defecto de Matplotlib, puedes usar `plt.rcParams`, un diccionario que contiene todas las configuraciones. Modificar `plt.rcParams` afecta todas las gráficas en la sesión.

Ejemplo:

```python
import matplotlib.pyplot as plt

# Cambiando el color de fondo y el tamaño de fuente de los títulos y etiquetas
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
```

> **Tip**: Cambiar valores por defecto es útil si planeas hacer varias visualizaciones con el mismo estilo.

---

## 2. Ajuste del Tamaño de las Gráficas

El tamaño de las gráficas es importante para asegurar que la visualización sea clara y efectiva. Los tamaños ideales pueden variar dependiendo de si la visualización se muestra en pantalla o se imprime.

### Tamaño de la Figura con `figsize`

Usa `figsize` para especificar el tamaño de la figura en pulgadas. Este parámetro se define en la función `plt.figure()` o `plt.subplots()`. Para un gráfico en pantalla, un tamaño adecuado es entre `(10, 6)` y `(12, 8)`, mientras que para impresión puede ser mayor, como `(14, 10)`.

```python
# Figura con tamaño para pantalla
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Gráfico de Ejemplo en Pantalla")
plt.show()

# Figura con tamaño para impresión
plt.figure(figsize=(14, 10))
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Gráfico de Ejemplo para Impresión")
plt.show()
```

### DPI (Dots Per Inch)

`dpi` controla la resolución de la gráfica. Para visualizar en pantalla, `dpi=100` es suficiente, mientras que para impresión puede ser adecuado `dpi=300` para obtener mayor claridad.

```python
# Configuración de resolución
plt.figure(figsize=(10, 6), dpi=300)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Gráfico con DPI alto para impresión")
plt.show()
```

---

## 3. Múltiples Gráficas en un Mismo `Plot`

Combinar múltiples gráficas en una misma figura puede ayudar a comparar datos y visualizar interacciones. Algunas de las formas comunes de lograr esto incluyen:

### Superposición de Gráficos

Puedes superponer varios gráficos en una misma figura llamando a múltiples funciones de gráficos (`plot`, `bar`, etc.) antes de `plt.show()`.

```python
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 8, 27, 64]

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="y = x^2", color="blue")
plt.plot(x, y2, label="y = x^3", color="green")
plt.title("Superposición de Gráficos")
plt.xlabel("Eje X")
plt.ylabel("Valores de Y")
plt.legend()
plt.show()
```

### Configuración de Ejes y Límites

Ajustar los límites y los ejes de una gráfica permite centrar la atención en áreas específicas de los datos.

- **`plt.xlim()` y `plt.ylim()`**: Establece los límites de los ejes X e Y.

    ```python
    plt.plot(x, y1)
    plt.xlim(0, 5)
    plt.ylim(0, 20)
    plt.title("Límites del Eje")
    plt.show()
    ```

- **`plt.xlabel()` y `plt.ylabel()`**: Etiqueta los ejes X e Y para claridad.

    ```python
    plt.plot(x, y1)
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.show()
    ```

### Configuración de la Escala de los Ejes

En algunos gráficos, como los de crecimiento exponencial, puede ser útil una escala logarítmica.

```python
plt.plot(x, y2)
plt.yscale("log")  # Escala logarítmica en el eje Y
plt.title("Gráfico con Escala Logarítmica")
plt.show()
```

---

## 4. Configuración de Gráficos Múltiples en la Misma Figura (`plt.subplots()`)

A veces, es útil mostrar varias gráficas en una sola figura con diferentes subgráficos. Esto es útil para comparar visualmente diferentes variables o tipos de datos en una única visualización.

### Uso de `plt.subplots()`

`plt.subplots()` permite crear una cuadrícula de subgráficas, especificando el número de filas y columnas.

- **`nrows`** y **`ncols`**: Número de filas y columnas de subplots.
- **`figsize`**: Tamaño de la figura total.
- **`sharex`** y **`sharey`**: Permiten compartir ejes entre subgráficas.

Ejemplo de 2x2 subplots:

```python
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Gráfico en la posición (0, 0)
axs[0, 0].plot(x, y1)
axs[0, 0].set_title("Gráfico 1")

# Gráfico en la posición (0, 1)
axs[0, 1].bar(x, y2)
axs[0, 1].set_title("Gráfico 2")

# Gráfico en la posición (1, 0)
axs[1, 0].scatter(x, y1)
axs[1, 0].set_title("Gráfico 3")

# Gráfico en la posición (1, 1)
axs[1, 1].hist(y2, bins=3)
axs[1, 1].set_title("Gráfico 4")

plt.tight_layout()
plt.show()
```

---

## 5. Configuración de Ejes y Límites Personalizados en Múltiples Subplots

Al trabajar con múltiples subplots, también puedes ajustar los ejes y límites de cada subplot de manera individual.

- **Establecer límites de ejes específicos** en cada gráfico individual.

    ```python
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    axs[0, 0].plot(x, y1)
    axs[0, 0].set_xlim(0, 4)
    axs[0, 0].set_ylim(0, 20)

    axs[1, 0].scatter(x, y1)
    axs[1, 0].set_xlim(0, 4)
    axs[1, 0].set_ylim(0, 20)

    plt.tight_layout()
    plt.show()
    ```

---

En esta segunda parte, hemos cubierto cómo ajustar los valores por defecto, el tamaño de las figuras, y cómo configurar múltiples gráficos en el mismo plot. En la **tercera parte** exploraremos más sobre los **subplots**, incluyendo ejes compartidos y el uso de `spines` para personalizar el aspecto de los bordes de los gráficos.

---

# Tutorial de Matplotlib - Parte 3: Subplots, Ejes y Spines

En esta sección, aprenderemos a:
1. Crear múltiples subplots de forma personalizada.
2. Configurar límites de los ejes y ejes compartidos entre subplots.
3. Manipular los spines para mejorar la presentación y el estilo de las gráficas.

---

## 1. Creación de Subplots

Los subplots permiten organizar varias gráficas en una sola figura, facilitando la comparación y el análisis de diferentes variables en un solo lugar.

### Uso de `plt.subplots()`

Con `plt.subplots()`, podemos crear una cuadrícula de subplots y definir el tamaño y el diseño de la figura:

- **`nrows` y `ncols`**: Número de filas y columnas de subplots.
- **`figsize`**: Tamaño total de la figura.
- **`sharex` y `sharey`**: Para compartir los ejes X o Y entre los subplots.

Ejemplo:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear una figura de 2x1 subplots
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(10, 8), sharex=True)

# Primer subplot
axs[0].plot(x, y1, color="blue")
axs[0].set_title("Seno de X")
axs[0].set_ylabel("Amplitud")

# Segundo subplot
axs[1].plot(x, y2, color="red")
axs[1].set_title("Coseno de X")
axs[1].set_xlabel("X")
axs[1].set_ylabel("Amplitud")

plt.tight_layout()
plt.show()
```

> **Tip**: `sharex=True` o `sharey=True` es útil para alinear los ejes y facilitar la comparación visual.

---

## 2. Configuración de Ejes y Límites en Subplots

Ajustar los límites de los ejes en cada subplot permite centrar la atención en un rango específico de datos.

### Configuración de Límites de los Ejes

Usa `set_xlim()` y `set_ylim()` para definir los límites de los ejes X e Y en cada subplot.

```python
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Configuración de límites en cada subplot
axs[0, 0].plot(x, y1)
axs[0, 0].set_xlim(0, 5)
axs[0, 0].set_ylim(-1, 1)
axs[0, 0].set_title("Gráfico 1: Límite X e Y")

axs[0, 1].plot(x, y2)
axs[0, 1].set_xlim(2, 8)
axs[0, 1].set_ylim(-1, 1)
axs[0, 1].set_title("Gráfico 2: Límite X e Y")

plt.tight_layout()
plt.show()
```

### Ejes Compartidos

Compartir ejes en subplots es útil para comparaciones directas y asegura que las escalas sean consistentes.

```python
# Subplots con ejes compartidos
fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True, sharey=True)

axs[0].plot(x, y1, label="Seno", color="blue")
axs[1].plot(x, y2, label="Coseno", color="red")

axs[0].legend()
axs[1].legend()
plt.show()
```

---

## 3. Manipulación de Spines

Los **spines** son los bordes de la gráfica (es decir, los ejes que enmarcan la gráfica). Modificar los spines puede ayudar a mejorar la apariencia y a dirigir la atención a áreas clave de los datos.

### Ocultar Spines

Puedes ocultar ciertos spines para simplificar el gráfico.

```python
fig, ax = plt.subplots(figsize=(8, 6))

# Gráfico de ejemplo
ax.plot(x, y1, color="blue")

# Ocultar el borde superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.title("Gráfico con Spines Ocultos")
plt.show()
```

### Cambiar Color y Grosor de Spines

Es posible personalizar el color y grosor de los spines para mejorar la estética del gráfico.

```python
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y2, color="green")

# Personalización de color y grosor de los spines
ax.spines['bottom'].set_color('purple')
ax.spines['left'].set_color('purple')
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

plt.title("Spines Personalizados")
plt.show()
```

### Desplazar Spines

Mover los spines puede ser útil cuando se necesita centrar los ejes en el origen o ajustar la visualización.

```python
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y1, color="orange")

# Mover los spines
ax.spines['left'].set_position(('data', 0))  # Mover el eje Y al origen en X
ax.spines['bottom'].set_position(('data', 0))  # Mover el eje X al origen en Y

plt.title("Spines Desplazados al Origen")
plt.show()
```

---

## Ejemplo Completo: Configuración de Subplots, Ejes Compartidos y Spines

En el siguiente ejemplo, crearemos una figura con varios subplots, compartiendo ejes y personalizando los spines.

```python
# Datos de ejemplo
x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Configuración de subplots 1x2
fig, axs = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Primer subplot
axs[0].plot(x, y1, color="blue")
axs[0].set_title("Seno de X")
axs[0].set_xlabel("X")
axs[0].set_ylabel("Amplitud")
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)

# Segundo subplot
axs[1].plot(x, y2, color="red")
axs[1].set_title("Coseno de X")
axs[1].set_xlabel("X")
# Configuración de spines
axs[1].spines['top'].set_color("grey")
axs[1].spines['top'].set_linewidth(1.5)
axs[1].spines['right'].set_color("grey")
axs[1].spines['right'].set_linewidth(1.5)

plt.tight_layout()
plt.show()
```

---

Con esta tercera parte, hemos cubierto cómo:

1. Crear subplots y configurarlos.
2. Compartir ejes entre subplots y establecer límites personalizados.
3. Personalizar y manipular los spines para mejorar la presentación de las gráficas.

Estas técnicas permiten crear visualizaciones complejas y adaptarlas a las necesidades específicas del análisis y la comunicación visual de los datos.

---

# Tutorial de Matplotlib - Parte 4: Estilos y Temas en Matplotlib

Matplotlib permite aplicar temas o estilos para cambiar rápidamente la apariencia de las gráficas. Los estilos predefinidos incluyen opciones para adaptar las visualizaciones a diferentes contextos (publicaciones, presentaciones, etc.).

A continuación, exploraremos cómo funcionan los estilos en las versiones recientes de Matplotlib, cuáles están disponibles y cómo aplicar o personalizar temas visuales.

---

## 1. Aplicar Estilos Predefinidos

Matplotlib incluye una serie de estilos predefinidos que se pueden aplicar utilizando `plt.style.use()`. Estos estilos ajustan configuraciones como los colores, el grosor de las líneas, el tamaño de fuente, el fondo y otros elementos visuales de los gráficos.

### Ver los Estilos Disponibles

Para ver la lista de estilos disponibles en tu versión actual de Matplotlib, usa:

```python
import matplotlib.pyplot as plt

print(plt.style.available)
```

> **Nota**: Algunos estilos populares de versiones anteriores, como `'fivethirtyeight'` o `'bmh'`, pueden no estar disponibles en las versiones más recientes de Matplotlib.

### Aplicar un Estilo Predefinido

Para aplicar un estilo, usa `plt.style.use('nombre_del_estilo')` al comienzo de tu sesión o antes de una gráfica específica. Esto cambia el estilo de todas las gráficas que se generen después de aplicar el estilo.

```python
plt.style.use('ggplot')  # Aplicar estilo 'ggplot'

# Crear un gráfico simple
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title("Gráfico con Estilo 'ggplot'")
plt.show()
```

---

## 2. Cambios en Estilos en Versiones Recientes

En las versiones más recientes de Matplotlib, algunos estilos clásicos han sido modificados o eliminados. Esto es debido a mejoras en la compatibilidad y en la consistencia visual de los estilos.

### Alternativas para Estilos Eliminados

1. **Estilos clásicos como `'fivethirtyeight'`**: Aunque algunos estilos específicos ya no están incluidos directamente en Matplotlib, se pueden instalar y usar los estilos de paquetes externos como `mplcyberpunk` (similar al estilo `fivethirtyeight`).

   ```bash
   pip install mplcyberpunk
   ```

   Luego, aplica el estilo:

   ```python
   import mplcyberpunk
   plt.style.use("cyberpunk")
   ```

2. **Creación de un estilo personalizado**: Si un estilo específico no está disponible, puedes crear uno propio o modificar uno existente.

---

## 3. Personalización de Estilos y Creación de Temas Propios

### Ajuste de Estilos con `plt.rcParams`

Para personalizar elementos específicos en un estilo, puedes modificar `plt.rcParams`. Cualquier cambio en `rcParams` afectará todas las visualizaciones que se creen posteriormente.

Ejemplo de personalización de colores y fuente:

```python
# Configuración personalizada
plt.rcParams['axes.facecolor'] = 'whitesmoke'  # Fondo de los ejes
plt.rcParams['axes.edgecolor'] = 'grey'        # Color del borde de los ejes
plt.rcParams['axes.grid'] = True               # Mostrar cuadrícula
plt.rcParams['grid.color'] = 'lightgrey'       # Color de la cuadrícula
plt.rcParams['font.size'] = 14                 # Tamaño de la fuente
plt.rcParams['font.family'] = 'serif'          # Familia de la fuente

# Crear un gráfico con la configuración personalizada
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, color='royalblue')
plt.title("Gráfico con Configuración Personalizada")
plt.show()
```

### Crear y Guardar un Estilo Personalizado

Para reutilizar una configuración personalizada en múltiples sesiones, puedes crear un archivo de estilo personalizado.

1. **Crear un archivo `.mplstyle`**: Guarda la configuración en un archivo `.mplstyle`. Por ejemplo, crea un archivo `mi_estilo.mplstyle` con el siguiente contenido:

   ```plaintext
   axes.facecolor : whitesmoke
   axes.edgecolor : grey
   grid.color : lightgrey
   font.size : 14
   font.family : serif
   ```

2. **Aplicar el estilo**: Guarda el archivo `.mplstyle` en el directorio de trabajo o en el directorio de estilos de Matplotlib (`~/.config/matplotlib/stylelib/` en sistemas UNIX).

   Luego, aplica el estilo con:

   ```python
   plt.style.use('mi_estilo')
   ```

---

## 4. Ejemplo Comparativo de Estilos

Aquí tienes un ejemplo que muestra cómo aplicar diferentes estilos en Matplotlib y ver sus efectos visuales.

```python
# Lista de algunos estilos disponibles (si tu versión los incluye)
estilos = ['default', 'ggplot', 'seaborn', 'dark_background', 'fast']

x = range(10)
y = [i**2 for i in x]

# Crear una figura con múltiples subplots para comparar estilos
fig, axs = plt.subplots(1, len(estilos), figsize=(15, 4))

for i, estilo in enumerate(estilos):
    plt.style.use(estilo)
    axs[i].plot(x, y)
    axs[i].set_title(estilo)

plt.tight_layout()
plt.show()
```

> **Nota**: Los estilos disponibles pueden variar, así que ajusta la lista `estilos` a los estilos que se muestran en `plt.style.available` en tu sistema.

---

## 5. Revertir al Estilo Predeterminado

Si aplicaste un estilo pero deseas volver al estilo predeterminado, usa:

```python
plt.style.use('default')
```

---

En esta cuarta parte, aprendiste cómo:

1. Aplicar y ver los estilos predefinidos disponibles.
2. Adaptar estilos clásicos no incluidos en versiones recientes.
3. Crear y guardar un estilo personalizado.
4. Comparar diferentes estilos visualmente en una figura.

Con esta información, puedes crear visualizaciones consistentes y visualmente atractivas adaptadas a tus necesidades específicas. Esto es especialmente útil en proyectos donde las visualizaciones deben mantener una estética uniforme para presentaciones o publicaciones.