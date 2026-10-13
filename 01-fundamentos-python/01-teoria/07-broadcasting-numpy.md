---

# 🧩 ¿Qué es el *broadcasting* en NumPy?

El **broadcasting** es una forma en la que **NumPy permite hacer operaciones entre arrays de distinto tamaño o forma**, **sin necesidad de usar bucles** ni copiar datos.

> 👉 En otras palabras: NumPy “extiende” (broadcast) los arrays más pequeños para que coincidan con la forma del más grande.

---

## 🎯 Idea principal

Supón que quieres sumar una matriz y un número:

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = 10
C = A + B
```

✅ NumPy entiende que el número `10` se “repite” por toda la matriz:
→ `10` se convierte internamente en `[[10, 10, 10], [10, 10, 10]]`

Resultado:

```
[[11, 12, 13],
 [14, 15, 16]]
```

---

## 📏 Regla general del broadcasting

Cuando se operan dos arrays, **NumPy compara sus dimensiones empezando desde la última hacia atrás**:

1. Si las dimensiones son **iguales**, se pueden combinar.
2. Si una de ellas es **1**, se “expande” (broadcast).
3. Si son **diferentes y ninguna es 1**, → ❌ error.

---

## 📚 Ejemplo 1: vector fila + vector columna

```python
a = np.array([[1, 2, 3]])   # forma (1,3)
b = np.array([[10],
              [20],
              [30]])        # forma (3,1)

print(a + b)
```

🔹 NumPy expande `a` verticalmente y `b` horizontalmente:

```
[[ 1,  2,  3]]   → se repite ↓ 3 veces
[[10], [20], [30]] → se repite → 3 veces
```

Resultado:

```
[[11, 12, 13],
 [21, 22, 23],
 [31, 32, 33]]
```

Formas compatibles:

```
(3,1)
(1,3)
↓
(3,3)
```

---

## 📚 Ejemplo 2: matriz + vector

```python
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

v = np.array([10,20,30])
print(A + v)
```

🔹 NumPy expande el vector `v` por cada fila.
Resultado:

```
[[11,22,33],
 [14,25,36],
 [17,28,39]]
```

Forma `(3,3)` + `(3,)` → `(3,3)`

---

## ❌ Ejemplo incompatible

```python
a = np.ones((3,4))
b = np.ones((2,1))
a + b
```

Da error porque:

```
(3,4)
(2,1)
```

→ ni 3 = 2, ni 4 = 1 → ❌ no hay coincidencia posible.

---

## 🧠 Ejemplo útil: distancia entre puntos

```python
x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

dist = np.sqrt((x - y)**2)
print(dist)
```

Y también con matrices:

```python
X = np.array([[1,2,3],
              [4,5,6]])

Y = np.array([[10,20,30]])

print(X * Y)  # Broadcasting
```

---

## 📚 Ejemplo 3: restar la media de cada columna

Una operación muy habitual es **centrar los datos**: restar a cada columna su
propia media. Con broadcasting se hace en una línea:

```python
datos = np.array([[2.0, 10.0, 100.0],
                  [4.0, 20.0, 200.0],
                  [6.0, 30.0, 300.0]])

media_col = datos.mean(axis=0)   # forma (3,) -> media de cada columna
print("Media por columna:", media_col)

centrados = datos - media_col    # broadcasting: se resta por cada fila
print("Datos centrados:\n", centrados)
```

Si quieres centrar **por fila** en vez de por columna, haz que la media tenga
forma `(n_filas, 1)` para que el broadcast se aplique por columnas:

```python
media_fila = datos.mean(axis=1, keepdims=True)   # forma (3,1)
print("Media por fila:\n", media_fila)
centrados_fila = datos - media_fila
print("Centrados por fila:\n", centrados_fila)
```

Darse cuenta de cuándo hace falta `keepdims=True` (o `[:, np.newaxis]`) para
controlar la dirección del broadcast es una de las habilidades más útiles de NumPy.

---

## 📚 Ejemplo 4: normalizar los datos (min-max)

```python
x = np.array([3, 1, 4, 1, 5, 9, 2, 6])

minimo = x.min()
maximo = x.max()

# (x - minimo) / (maximo - minimo) -> cada valor se escala a [0, 1]
norm = (x - minimo) / (maximo - minimo)
print("Normalizados:", norm)
print("Rango resultado:", norm.min(), norm.max())
```

## 📚 Ejemplo 5: escalar cada columna por su desviación

```python
X = np.random.default_rng(0).normal(size=(4, 3))
desv = X.std(axis=0)                     # (3,)
estandar = X / desv                      # se divide cada columna por su desv
print("Columnas con desviación 1:\n", estandar)
print("Desv de cada columna:", estandar.std(axis=0))
```

## 📚 Ejemplo 6: rejillas con multiplicación externa

Combinar un vector columna y un vector fila construye una tabla:

```python
a = np.array([1, 2, 3])
b = np.array([10, 100, 1000])

tabla = a[:, np.newaxis] * b[np.newaxis, :]   # (3,1) * (1,3) -> (3,3)
print("Tabla de productos:\n", tabla)
```

Esto es la base de `np.outer` y también de construir rejillas de coordenadas
para gráficos o simulaciones.

## 📚 Ejemplo 7: comparar cada fila con un vector

```python
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
limite = np.array([5, 5, 5])

# compara elemento a elemento cada fila con el vector
supera = X > limite
print("Qué supera el límite:\n", supera)
print("Nº de celdas que lo superan por fila:", supera.sum(axis=1))
```

## 📚 Ejemplo 8: matriz de distancias por parejas

Distantcias entre puntos de un conjunto usando broadcasting:

```python
puntos = np.array([[0., 0.],
                   [3., 4.],
                   [6., 8.]])

# diferencias por parejas: diferencias[i,j] = puntos[i] - puntos[j]
diferencias = puntos[:, np.newaxis, :] - puntos[np.newaxis, :, :]
distancias = np.sqrt((diferencias ** 2).sum(axis=-1))
print("Matriz de distancias:\n", distancias)
```

El resultado es simétrico y su diagonal vale 0. Esta misma idea aparece en
k-NN, clustering y otros algoritmos de IA.

---

## 🔬 Casos donde suele aparecer el broadcast

| Situación | Patrón habitual |
|---|---|
| Centrar / estandarizar columnas | `X - X.mean(axis=0)` o `X / X.std(axis=0)` |
| Añadir una constante o umbral | `X + 1`, `X > umbral` |
| Escalar filas | `X * pesos[:, np.newaxis]` |
| Escalar columnas | `X * pesos[np.newaxis, :]` |
| Construir rejillas | `a[:, None] * b[None, :]` |
| Sumar un vector a cada fila | `X + v` |
| Sumar un vector a cada columna | `X + v[:, None]` |

---

## 🎯 Ejercicios para practicar

1. `A = np.ones((4, 5))`; súmale un vector `v = [1, 2, 3, 4, 5]` y explica la forma.
2. Centra una matriz 3×4 de datos restando la media de cada **fila** (usa `keepdims=True`).
3. Normaliza cada **columna** de una matriz para que quede entre 0 y 1.
4. Construye con broadcasting la tabla de multiplicar del 9 (usando dos vectores).
5. Dados los puntos `[[0,0],[3,4],[6,8]]`, calcula y comprueba que la diagonal
   de la matriz de distancias es 0 y que la matriz es simétrica.
6. `a = np.array([1,2,3])` y `b = np.array([10,20])`: ¿por qué `a + b` da error?
   ¿Cómo harías su producto para obtener una forma (3,2)?

---

## 🧩 Resumen visual

| Forma A | Forma B | ¿Compatible? | Resultado                    |
| ------- | ------- | ------------ | ---------------------------- |
| (3,3)   | (3,)    | ✅            | Se expande el vector a (3,3) |
| (3,1)   | (1,3)   | ✅            | Resultado (3,3)              |
| (2,3)   | (3,2)   | ❌            | Incompatible                 |
| (5,1,4) | (1,3,1) | ✅            | Resultado (5,3,4)            |

---

## 🎓 En resumen

* NumPy **no copia** realmente los datos, solo “simula” que el array pequeño se repite.
* Ahorra **memoria y tiempo**.
* Es una de las razones por las que NumPy es tan rápido y eficiente.

---

