
# 🎨 Infografía visual del Broadcasting en NumPy

El **broadcasting** permite que NumPy realice operaciones entre arrays de diferentes tamaños,
**expandiendo automáticamente** los más pequeños para que coincidan en forma.

---

## 🧩 Reglas del broadcasting

1️⃣ **Se comparan las formas desde el final hacia atrás.**  
2️⃣ Dos dimensiones son **compatibles** si:
   - Son **iguales**, o  
   - Una de ellas es **1**.  
3️⃣ Si no son compatibles → ❌ error.

---

## 🎯 Ejemplo 1: (3, 1) + (1, 4)

```python
import numpy as np
A = np.array([[1],
              [2],
              [3]])   # forma (3,1)

B = np.array([[10, 20, 30, 40]])  # forma (1,4)

C = A + B
````

Visualmente:

```
A.shape = (3,1)     → se repite a lo largo de columnas
B.shape = (1,4)     → se repite a lo largo de filas

Expansión:
[[1,1,1,1],
 [2,2,2,2],
 [3,3,3,3]]
+
[[10,20,30,40],
 [10,20,30,40],
 [10,20,30,40]]
=
[[11,21,31,41],
 [12,22,32,42],
 [13,23,33,43]]
```

✅ Resultado → forma final `(3,4)`

---

## 🎯 Ejemplo 2: (3, 3) + (3,)

```python
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])   # (3,3)
b = np.array([10,20,30])  # (3,)

A + b
```

```
b se expande por filas → broadcast vertical
Resultado:
[[11,22,33],
 [14,25,36],
 [17,28,39]]
```

✅ Resultado → `(3,3)`

---

## 🎯 Ejemplo 3: Escalar + Matriz

```python
A = np.array([[1,2,3],
              [4,5,6]])
A + 10
```

```
10 → se expande a toda la matriz
[[1,2,3],
 [4,5,6]]
+
[[10,10,10],
 [10,10,10]]
=
[[11,12,13],
 [14,15,16]]
```

✅ Resultado → `(2,3)`

---

## 🚫 Ejemplo NO compatible

```python
A = np.ones((3,4))
B = np.ones((2,1))
A + B
```

Comparación de formas:

```
(3,4)
(2,1)
 ↓ ↓
 3 ≠ 2  ❌
 4 ≠ 1  ❌
```

❌ **Error: formas incompatibles para broadcasting**

---

## 🧠 Regla rápida

| Forma A   | Forma B   | Compatible | Resultado |
| --------- | --------- | ---------- | --------- |
| (3, 1)    | (1, 4)    | ✅          | (3, 4)    |
| (3, 3)    | (3,)      | ✅          | (3, 3)    |
| (1, 3)    | (3, 1)    | ✅          | (3, 3)    |
| (2, 3)    | (3, 2)    | ❌          | —         |
| (4, 1, 5) | (1, 3, 1) | ✅          | (4, 3, 5) |

---

## 💡 En resumen

* Broadcasting = **expansión automática de dimensiones**
* No duplica datos → **más rápido y eficiente**
* Aplica reglas simples basadas en las **formas de los arrays**

---

🧾 **Consejo práctico:**
Si algo no funciona, imprime las formas:

```python
print(A.shape, B.shape)
```

Y si quieres “forzar” compatibilidad, usa `reshape()` o `np.newaxis`:

```python
A = np.arange(3)[:, np.newaxis]  # cambia (3,) → (3,1)
```

```

---

