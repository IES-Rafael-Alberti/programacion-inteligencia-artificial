Perfecto ✅
Aquí tienes la **versión de los ejercicios de NumPy sin soluciones**, pero con una **celda de test automática después de cada ejercicio**, para que los alumnos puedan **comprobar si su código funciona correctamente**.

Las pruebas están pensadas para dar una **retroalimentación básica** (“✅ Correcto” / “❌ Revisa tu resultado”).
Puedes adaptarlas fácilmente si quieres que devuelvan mensajes más detallados o comparen con tolerancia numérica (`np.allclose`, etc.).

---

````markdown
# 🧮 Ejercicios de práctica con NumPy (versión con tests)

Estos ejercicios te ayudarán a practicar operaciones con arrays NumPy: creación, indexado, álgebra lineal, estadística y manipulación de datos.  
Cada ejercicio incluye una **celda de test** para comprobar tu solución.

---

## 1️⃣ Crear un array y extraer la diagonal
Crea un array 4×4 con los números del 0 al 15 y extrae la diagonal principal en una variable llamada `diag`.

```python
import numpy as np

# tu código aquí


````

✅ **Test**

```python
A = np.arange(16).reshape(4,4)
ok = np.allclose(diag, np.diag(A))
print("✅ Correcto" if ok else "❌ Revisa tu resultado")
```

---

## 2️⃣ Generar valores normales y calcular media/desviación

Genera 1000 valores normales `N(0,1)` en `x` y calcula `media` y `desv`.

```python
# tu código aquí


```

✅ **Test**

```python
ok = abs(media) < 0.1 and abs(desv - 1) < 0.1
print("✅ Correcto" if ok else "❌ Revisa los cálculos (usa N(0,1))")
```

---

## 3️⃣ Elevar al cuadrado sin bucles

Dado `x = [1,2,3,4,5]`, obtén un array con los cuadrados **sin usar bucles** y guárdalo en `y`.

```python
# tu código aquí


```

✅ **Test**

```python
ok = np.array_equal(y, np.array([1,4,9,16,25]))
print("✅ Correcto" if ok else "❌ Revisa la operación (usa vectorización)")
```

---

## 4️⃣ Estandarizar columnas (z-score)

Crea una matriz aleatoria 5×4 `A` con `np.random.randn`. Calcula su z-score columna a columna y guarda el resultado en `Z`.

```python
# tu código aquí


```

✅ **Test**

```python
ok = np.allclose(Z.mean(axis=0), 0, atol=1e-1) and np.allclose(Z.std(axis=0), 1, atol=1e-1)
print("✅ Correcto" if ok else "❌ Revisa la normalización por columnas")
```

---

## 5️⃣ Borde a 1, interior a 0

Crea una matriz 6×6 `M` con el borde a 1 y el interior a 0.

```python
# tu código aquí


```

✅ **Test**

```python
ok = (M[0,:].all() and M[-1,:].all() and M[:,0].all() and M[:,-1].all()) and not M[1:-1,1:-1].any()
print("✅ Correcto" if ok else "❌ Revisa el borde/interior de la matriz")
```

---

## 6️⃣ Matriz de distancias por broadcasting

Dado `x = np.array([0, 3, 5, 9])`, construye una matriz `D` donde `D[i,j] = |x[i] - x[j]|`.

```python
# tu código aquí


```

✅ **Test**

```python
ref = np.array([[0,3,5,9],[3,0,2,6],[5,2,0,4],[9,6,4,0]])
ok = np.array_equal(D, ref)
print("✅ Correcto" if ok else "❌ Revisa el broadcasting")
```

---

## 7️⃣ Reordenar filas por la suma

Genera una matriz 4×5 `A` con enteros aleatorios entre 0 y 9. Reordénala en `A_sorted` según la suma (descendente).

```python
# tu código aquí


```

✅ **Test**

```python
ok = np.all(np.diff(A_sorted.sum(axis=1)) <= 0)
print("✅ Correcto" if ok else "❌ Las filas no están ordenadas correctamente")
```

---

## 8️⃣ Reemplazar outliers por la mediana

Crea un vector `v` de 100 valores `N(0,1)` y reemplaza los valores con `|v - media| > 2*desv` por la mediana.

```python
# tu código aquí


```

✅ **Test**

```python
m, s = v.mean(), v.std()
mask = np.abs(v - m) > 2*s
ok = not mask.any() or np.isclose(v[mask].mean(), np.median(v))
print("✅ Correcto" if ok else "❌ Revisa la sustitución de outliers")
```

---

## 9️⃣ One-hot encoding

Dadas etiquetas `y = np.array([0, 2, 1, 2])`, crea la matriz one-hot `onehot`.

```python
# tu código aquí


```

✅ **Test**

```python
ref = np.array([[1,0,0],[0,0,1],[0,1,0],[0,0,1]])
ok = np.array_equal(onehot, ref)
print("✅ Correcto" if ok else "❌ Revisa el indexado con np.eye()")
```

---

## 🔟 Media móvil con `np.convolve`

Crea una serie `s` con 20 valores `N(0,1)` y calcula la media móvil de ventana 5 en `mm`.

```python
# tu código aquí


```

✅ **Test**

```python
ok = len(mm) == len(s) - 5 + 1
print("✅ Correcto" if ok else "❌ Usa mode='valid' en np.convolve")
```

---

## 11️⃣ Concatenar con padding

Dados `a = [1,2,3,4]`, `b = [5,6]`, `c = [7,8,9]`, crea una matriz `M` 3×4 con ceros de relleno.

```python
# tu código aquí


```

✅ **Test**

```python
ok = M.shape == (3,4) and np.array_equal(M[0,:len(a)], a)
print("✅ Correcto" if ok else "❌ Revisa el relleno o el apilado vertical")
```

---

## 12️⃣ Filtrar filas con valores grandes

Crea una matriz 5×5 con enteros aleatorios (0–20) y extrae las filas que tengan al menos un valor >15.

```python
# tu código aquí


```

✅ **Test**

```python
ok = all((res <= 20).all(axis=1)) and all((res > 15).any(axis=1))
print("✅ Correcto" if ok else "❌ Verifica el filtrado con any(axis=1)")
```

---

## 13️⃣ Simular tiradas de dados

Simula 10 000 tiradas de dos dados y calcula `p7` y `p11`, las probabilidades de suma 7 y 11.

```python
# tu código aquí


```

✅ **Test**

```python
ok = 0.1 < p7 < 0.2 and 0.03 < p11 < 0.1
print("✅ Correcto" if ok else "❌ Revisa la simulación de dados o las probabilidades")
```

---

## 14️⃣ Resolver sistema lineal

Genera `A` (3×3) y `b` (3×1). Resuelve `Ax = b` en `x` y calcula el residuo `res`.

```python
# tu código aquí


```

✅ **Test**

```python
ok = res < 1e-10
print("✅ Correcto" if ok else "❌ El residuo no es suficientemente pequeño")
```

---

## 15️⃣ Tablero de ajedrez (damero)

Crea una matriz 10×10 que alterna 0 y 1 como un tablero de ajedrez, llamada `board`.

```python
# tu código aquí


```

✅ **Test**

```python
ok = board.shape == (10,10) and np.all((board == 0) | (board == 1))
print("✅ Correcto" if ok else "❌ Revisa el patrón (usa índices o módulo)")
```

---

## 16️⃣ Función a trozos con `np.where`

Dado `x = np.linspace(-3, 3, 13)`, define `y`:

* `y = -1` si `x < -1`
* `y = x²` si `-1 ≤ x ≤ 1`
* `y = 1` si `x > 1`

```python
# tu código aquí


```

✅ **Test**

```python
ok = np.all(y[x < -1] == -1) and np.all(y[x > 1] == 1)
print("✅ Correcto" if ok else "❌ Revisa las condiciones anidadas de np.where")
```

---

## 17️⃣ Top-k por columna

Crea `A` 6×4 con `N(0,1)`. Para cada columna, marca con `True` los 2 valores más grandes en `B`.

```python
# tu código aquí


```

✅ **Test**

```python
ok = np.all(B.sum(axis=0) == 2)
print("✅ Correcto" if ok else "❌ Cada columna debe tener 2 valores True")
```

---

## 18️⃣ Matriz de distancias euclídeas

Dada `X` 5×3, calcula la matriz de distancias euclídeas entre todas las filas (`D`).

```python
# tu código aquí


```

✅ **Test**

```python
ok = np.allclose(np.diag(D), 0)
print("✅ Correcto" if ok else "❌ Revisa el cálculo de distancias fila a fila")
```

---


