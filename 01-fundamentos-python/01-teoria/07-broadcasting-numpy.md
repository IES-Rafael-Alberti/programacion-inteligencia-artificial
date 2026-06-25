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

