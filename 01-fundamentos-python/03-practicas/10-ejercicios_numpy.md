# 🧮 Ejercicios de práctica con NumPy

Estos ejercicios te ayudarán a practicar operaciones con arrays NumPy: creación, indexado, álgebra lineal, estadística y manipulación de datos.

---

## 1️⃣ Crear un array y extraer la diagonal
Crea un array 4×4 con los números del 0 al 15 y extrae la diagonal principal.

```python

````

---

## 2️⃣ Generar valores normales y calcular media/desviación

Genera 1000 valores normales `N(0,1)` y calcula la media y la desviación estándar.

```python
```

---

## 3️⃣ Elevar al cuadrado sin bucles

Dado `x = [1,2,3,4,5]`, obtén un array con los cuadrados **sin usar bucles**.

```python
```

---

## 4️⃣ Estandarizar columnas (z-score)

Crea una matriz aleatoria 5×4 con `np.random.randn`. Calcula la media y desviación por columna y estandariza.

```python
```

---

## 5️⃣ Borde a 1, interior a 0

Crea una matriz 6×6 con los números del 0 al 35 y pon el borde a 1 y el interior a 0.

```python
```

---

## 6️⃣ Matriz de distancias por broadcasting

Dado `x = np.array([0, 3, 5, 9])`, construye una matriz `D` donde `D[i,j] = |x[i] - x[j]|`.

```python
```

---

## 7️⃣ Reordenar filas por la suma

Genera una matriz 4×5 con enteros aleatorios entre 0 y 9. Reordena las filas según la suma (descendente).

```python
```

---

## 8️⃣ Reemplazar outliers por la mediana

Crea `v` con 100 valores `N(0,1)` y añade 3 valores atípicos (10, -9, 8). Sustituye los outliers por la mediana.

```python
```

---

## 9️⃣ One-hot encoding

Dadas etiquetas `y = np.array([0, 2, 1, 2])` y `n_clases = 3`, crea la matriz one-hot.

```python
```

---

## 🔟 Media móvil con `np.convolve`

Crea una serie `s` con 20 valores `N(0,1)` y calcula la media móvil de ventana 5 (modo `'valid'`).

```python
```

---

## 11️⃣ Concatenar con padding

Dados `a = [1,2,3,4]`, `b = [5,6]`, `c = [7,8,9]`, crea una matriz 3×4 con ceros de relleno.

```python
```

---

## 12️⃣ Filtrar filas con valores grandes

Crea una matriz 5×5 con enteros aleatorios (0–20) y extrae las filas que tengan al menos un valor >15.

```python
```

---

## 13️⃣ Simular tiradas de dados

Simula 10 000 tiradas de dos dados y calcula la probabilidad de que la suma sea 7 o 11.

```python
```

---

## 14️⃣ Resolver sistema lineal

Genera `A` (3×3) y `b` (3×1). Resuelve `Ax = b` y calcula el residuo `||Ax - b||`.

```python
```

---

## 15️⃣ Tablero de ajedrez (damero)

Crea una matriz 10×10 que alterna 0 y 1 como un tablero de ajedrez.

```python
```

---

## 16️⃣ Función a trozos con `np.where`

Dado `x = np.linspace(-3, 3, 13)`, define `y`:

* `y = -1` si `x < -1`
* `y = x²` si `-1 ≤ x ≤ 1`
* `y = 1` si `x > 1`

```python
```

---

## 17️⃣ Top-k por columna

Crea `A` 6×4 con `N(0,1)`. Para cada columna, marca con `True` los 2 valores más grandes.

```python
```

---

## 18️⃣ Matriz de distancias euclídeas

Dada `X` 5×3, calcula la matriz de distancias euclídeas entre todas las filas.

```python
```


