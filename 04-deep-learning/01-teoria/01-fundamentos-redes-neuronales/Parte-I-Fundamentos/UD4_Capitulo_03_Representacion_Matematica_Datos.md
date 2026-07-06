---
editor_options: 
  markdown: 
    wrap: 72
output: 
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true 
    fig_caption: true
    latex_engine: xelatex
---
# Capítulo 3 — Representación matemática de los datos

## 3.1. Por qué necesitamos una representación matemática

Las redes neuronales no trabajan con:
- textos
- categorías
- fechas
- imágenes “tal cual”

Trabajan con **números organizados**.

La pregunta clave no es “qué datos tengo”, sino:

> ¿Cómo represento mis datos para que una red neuronal pueda operar con ellos?

La respuesta es: **escalares, vectores, matrices y tensores**.

---

## 3.2. Escalares: un solo valor

Un **escalar** es un número individual.

![Escalares, Vectores, Matrices y Tensores](images/13_escalares_vectores_matrices_tensores.png)

Ejemplos:
- Temperatura
- Precio
- Edad
- Pérdida de un modelo

En Python:
```python
x = 42
````

En redes neuronales:

* El valor de la función de pérdida es un escalar
* Un learning rate es un escalar

---

## 3.3. Vectores: una observación

Un **vector** es una colección ordenada de números.

Representa:

* Una observación
* Un conjunto de características

Ejemplo:

* Película: duración, presupuesto, puntuación
* Medición meteorológica: temperatura, humedad, presión

```python
import numpy as np
x = np.array([120, 8.5, 2023])
```

Interpretación geométrica:

* Un vector es un **punto** o una **flecha** en un espacio de dimensión *n*

---

## 3.4. Matrices: un dataset completo

Una **matriz** es un conjunto de vectores.

En Machine Learning:

* Filas → observaciones
* Columnas → variables

![Interpretación Geométrica](images/14_interpretacion_geometrica.png)

```python
X = np.array([
    [120, 8.5, 2023],
    [95, 7.9, 2021],
    [140, 9.1, 2024]
])
```

Forma (`shape`):

```
(n_observaciones, n_variables)
```

Interpretación:

* Una nube de puntos en un espacio multidimensional

---

## 3.5. Tensores: generalización de matrices

Un **tensor** es una estructura que generaliza:

* Escalar → tensor 0D
* Vector → tensor 1D
* Matriz → tensor 2D
* Más dimensiones → tensor ND

Ejemplos:

* Batch de datos → (batch, variables)
* Imagen → (alto, ancho, canales)
* Serie temporal → (tiempo, variables)
* Texto → (tokens, embedding_dim)

```python
tensor = np.random.rand(32, 10)
```

En Deep Learning:

> Todo son tensores.

---

## 3.6. Forma y dimensión (`shape`)

La **forma** de un tensor describe:

* Cuántas dimensiones tiene
* Cuántos elementos hay en cada una

![Shape y Debugging](images/18_shape_debugging.png)

Ejemplo:

```python
tensor.shape
```

Una forma incorrecta es una de las causas más comunes de error en redes neuronales.

Entender `shape` es **más importante que memorizar fórmulas**.

---

## 3.7. Batches de datos

Entrenar con todo el dataset a la vez:

* Consume mucha memoria
* Es ineficiente
* Dificulta la generalización

Por eso se usan **batches**:

* Pequeños subconjuntos del dataset
* Procesados de forma iterativa
* Aprovechan paralelización

![Batches de Datos](images/15_batches_datos.png)

Ejemplo:

```
(batch_size, n_variables)
```

> Un batch no es un tipo nuevo de dato,
> es simplemente un tensor más grande.

---

## 3.8. Operaciones elemento a elemento

Son operaciones que se aplican **posición a posición**.

![Operaciones Básicas con Tensores](images/16_operaciones_basicas.png)

Ejemplos:

```python
A + B
A * B
```

Se usan en:

* Funciones de activación

---

## 3.7. Preguntas de autoevaluación

### Opción múltiple

1. **¿Cuál es la diferencia principal entre un vector y una matriz?**
   - A) Un vector es más rápido  
   - **B) Un vector tiene 1 dimensión, una matriz tiene 2**  
   - C) Una matriz siempre es cuadrada  
   - D) No hay diferencia real

2. **¿Qué es un tensor en el contexto de redes neuronales?**
   - A) Una operación matemática  
   - **B) Un arreglo multidimensional de números**  
   - C) Un tipo de neurona  
   - D) Un parámetro de aprendizaje

3. **¿Por qué es importante la operación de broadcasting en redes neuronales?**
   - A) Porque hace el código más bonito  
   - **B) Porque permite operaciones eficientes entre tensores de distintos tamaños**  
   - C) Porque es obligatoria  
   - D) Para reducir memoria

### Pregunta corta

4. **¿Cómo representarías un batch de 32 imágenes RGB de 28×28 píxeles como un tensor? ¿Cuáles serían sus dimensiones?** (2 líneas)
* Normalización
* Cálculo de pérdidas

Estas operaciones son rápidas y fáciles de paralelizar.

---

## 3.9. Broadcasting

El **broadcasting** permite operar tensores de distinta forma.

Ejemplo conceptual:

```python
X + bias
```

Interpretación:

* Se suma el mismo vector a todas las filas
* Se desplaza la nube de puntos

El broadcasting es clave para:

* Añadir sesgos
* Aplicar normalizaciones
* Evitar bucles explícitos

---

## 3.10. Producto matricial

El **producto matricial** es la operación central de una red neuronal.

```python
Y = X @ W
```

Qué representa:

* Combinación lineal de variables
* Cambio de base
* Proyección del espacio

Geométricamente:

> Cada capa “reorganiza” el espacio de datos.

---

## 3.11. Cambio de forma (reshape)

Cambiar la forma de un tensor **no cambia los datos**, solo cómo se interpretan.

![Reshape](images/17_reshape.png)

```python
X.reshape(32, 10)
```

Muy común en:

* Redes convolucionales
* Redes recurrentes
* Paso de capas densas a otras arquitecturas

---

## 3.12. Interpretación geométrica del aprendizaje

Cada capa de una red neuronal:

1. Aplica una transformación lineal
2. Aplica una activación no lineal

El efecto acumulado es:

* Deformar el espacio de datos
* Separar regiones
* Facilitar la clasificación o regresión

Esta visión geométrica es clave para entender:

* Por qué funcionan las redes
* Por qué necesitan varias capas

---

## 3.13. Idea clave del capítulo

> Las redes neuronales no trabajan con “datos”,
> trabajan con **tensores y transformaciones geométricas**.

Comprender:

* escalares
* vectores
* matrices
* tensores
* shapes
* operaciones básicas

es imprescindible para entender:

* entrenamiento
* gradiente descendente
* backpropagation



---

### 🔜 Siguiente paso

👉 **Capítulo 4 — Operaciones con tensores y redes como funciones**
.
