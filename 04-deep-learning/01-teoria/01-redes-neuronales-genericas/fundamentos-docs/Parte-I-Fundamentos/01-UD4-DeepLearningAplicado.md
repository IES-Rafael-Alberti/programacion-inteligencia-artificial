# 📘 UD4 — Deep Learning aplicado
## De Machine Learning clásico a Redes Neuronales

---

## 1. Introducción: ¿por qué Redes Neuronales Deep Learning?

En las unidades anteriores hemos trabajado con:
- Pandas y EDA
- Modelos clásicos de Machine Learning
- Métricas y validación
- Despliegue de modelos

Estos modelos funcionan muy bien cuando:
- Los datos están bien estructurados
- Las relaciones entre variables son relativamente simples
- Podemos diseñar características “a mano”

Pero aparecen problemas donde esto **no es suficiente**:

- Muchas variables con relaciones complejas
- Datos secuenciales (tiempo, texto)
- Datos no estructurados (imágenes, audio)
- Necesidad de aprender representaciones internas

Aquí es donde aparece el **Deep Learning**.

> Deep Learning no es magia:
> es una forma sistemática de **aprender representaciones** a partir de datos.

---

## 2. ¿Qué cambia respecto al ML clásico?

En Machine Learning clásico:
- Elegimos las características
- Elegimos el modelo
- Ajustamos parámetros

En las redes neuronales en general y Deep Learning que las amplía:
- El modelo **aprende las características**
- Trabajamos con **estructuras numéricas más generales**
- El entrenamiento se basa en **optimización matemática continua**

Para entender esto, necesitamos una base matemática mínima.

---

## 3. Los datos como objetos matemáticos

### 3.1 Escalares

Un **escalar** es un único número.

Ejemplos:
- Edad
- Temperatura
- Precio

En Python:
```python
x = 42
````

---

### 3.2 Vectores

Un **vector** es una lista ordenada de números.

Ejemplos:

* Características de una película
* Variables de una observación

Geométricamente:
➡️ Un vector es un **punto o una flecha** en un espacio.

```python
import numpy as np
v = np.array([120, 8.5, 2023])
```

---

### 3.3 Matrices

Una **matriz** es una colección de vectores.

Ejemplo típico:

* Un dataset tabular
* Filas = observaciones
* Columnas = variables

```python
X = np.array([
    [120, 8.5, 2023],
    [95, 7.9, 2021]
])
```

Geométricamente:

* Transformaciones del espacio
* Rotaciones, escalados, combinaciones

---

### 3.4 Tensores

Un **tensor** es una generalización:

* Escalar → tensor 0D
* Vector → tensor 1D
* Matriz → tensor 2D
* Más dimensiones → tensor ND

Ejemplos:

* Imagen: (alto, ancho, canales)
* Serie temporal: (tiempo, variables)
* Batch de datos: (ejemplos, características)

```python
tensor = np.random.rand(32, 10)  # batch de 32 ejemplos
```

> Deep Learning trabaja **exclusivamente con tensores**.

---

## 4. Batches: procesar datos en grupos

Entrenar con todo el dataset a la vez es:

* Costoso
* Poco eficiente

Por eso se usan **batches**:

* Pequeños grupos de datos
* Permiten paralelización
* Introducen variabilidad beneficiosa

```python
batch_size = 32
```

> Un batch es simplemente un tensor más grande.

---

## 5. Operaciones con tensores

### 5.1 Operaciones elemento a elemento

Se aplican posición a posición.

```python
A + B
A * B
```

Uso:

* Activaciones
* Normalizaciones

---

### 5.2 Broadcasting

Permite operar tensores de distinta forma.

Ejemplo:

```python
X + bias
```

Geométricamente:

* Desplazar todos los puntos del espacio
* Ajustar referencias

---

### 5.3 Producto de tensores (producto matricial)

Es el **corazón** de una red neuronal.

```python
Y = X @ W
```

Interpretación geométrica:

* Cambio de base
* Proyección del espacio
* Combinación lineal de características

---

### 5.4 Cambio de forma (reshape)

No cambia los datos, solo su interpretación.

```python
X.reshape(32, 10)
```

Clave en:

* CNN
* RNN
* Transformers

---

## 6. Redes neuronales como funciones

Una red neuronal es:

> Una función compleja construida a partir de funciones simples.

Cada capa:

* Aplica una transformación lineal
* Aplica una función no lineal

```text
Entrada → Transformación → Activación → Salida
```

Geométricamente:

* Curvar el espacio
* Separar regiones
* Crear fronteras complejas

---

## 7. El problema del entrenamiento

Queremos:

* Que la salida sea lo más correcta posible

Para eso definimos:

* Una **función de pérdida**
* Un proceso de **optimización**

---

## 8. Derivadas y gradientes (la idea, no el formalismo)

### 8.1 Derivada

Una derivada responde a:

> ¿Cómo cambia el resultado si cambio un poco el parámetro?

En Deep Learning:

* Queremos saber cómo cambiar pesos
* Para reducir el error

---

### 8.2 Gradiente

El **gradiente** es:

* La derivada en muchas dimensiones
* La dirección de máximo aumento del error

👉 Para reducir el error, vamos en sentido contrario.

---

## 9. Gradiente descendente

Idea central:

1. Calculamos el error
2. Calculamos el gradiente
3. Ajustamos los pesos
4. Repetimos

```text
nuevo_peso = peso - learning_rate × gradiente
```

---

### 9.1 Gradiente descendente estocástico (SGD)

En lugar de todo el dataset:

* Usamos batches
* Más rápido
* Mejor generalización

---

## 10. Backpropagation: encadenar derivadas

Una red neuronal es una **cadena de operaciones**.

La derivada total se calcula usando:

* Regla de la cadena
* Propagando el error hacia atrás

Esto es **backpropagation**.

> No es magia:
> es cálculo sistemático de derivadas encadenadas.

---

## 11. Qué hemos conseguido entender

Al final de esta introducción sabemos que:

* Deep Learning = tensores + funciones + optimización
* Las matemáticas no son un fin, sino una herramienta
* Las redes neuronales aprenden representaciones
* El entrenamiento es ajuste iterativo guiado por el gradiente

---

## 12. A partir de aquí…

En esta unidad vamos a:

* Construir redes neuronales reales
* Compararlas con ML clásico
* Ver cuándo aportan valor
* Evitar usarlas cuando no conviene

> Deep Learning no sustituye al Machine Learning:
> lo amplía.
