# NumPy en profundidad: ejes, indexación, mas y máscaras

Guía de apoyo para ampliar la introducción a NumPy y llenar una sesión práctica.
Presupone haber trabajado `05-numpy-introduccion.md` y el notebook de fundamentos.

## Ejes y reducciones: el concepto más importante

Un `ndarray` tiene una forma `(filas, columnas, ...)`. Cada número de la forma es
un **eje**. Las operaciones de reducción (`sum`, `mean`, `min`, `max`, `std`) se
aplican **sobre**: un eje concreto, varios ejes o todos.

```python
import numpy as np

M = np.arange(12).reshape(3, 4)
print(M.shape)          # (3, 4)
print("M:\n", M)

# Sobre todo el array (resultado escalar)
print("Total:", M.sum())            # 66
print("Media global:", M.mean())    # 5.5

# Eje 0: recorre las filas -> reduce filas, conserva columnas
print("Suma por columna:", M.sum(axis=0))      # [12 15 18 21]
print("Media por columna:", M.mean(axis=0))    # [3. 4. 5. 6.]

# Eje 1: recorre las columnas -> reduce columnas, conserva filas
print("Suma por fila:", M.sum(axis=1))         # [ 6 22 38]
print("Media por fila:", M.mean(axis=1))       # [1.5 5.5 9.5]

# Varios ejes a la vez
print("Suma por filas de la transpuesta:", M.T.sum(axis=1))  # equivale a sum(axis=1)
```

> **Regla mental:** `axis=0` opera hacia abajo (entre filas); `axis=1` opera hacia
> la derecha (entre columnas). En arrays de más dimensiones, `axis=i` reduce la
> dimensión `i`.

### `keepdims` y `newaxis`

Cuando la reducción deja de existir el eje, a veces interesa conservarlo para
poder restar dividir con broadcasting sin que el array quede «aplanado».

```python
v = np.array([1, 2, 3, 4])
print(v.mean())            # escalar 2.5
print(v.mean(keepdims=True))  # array [2.5] con forma (1,)

M = np.arange(12).reshape(3, 4)
media_col = M.mean(axis=0, keepdims=True)   # forma (1,4)
print("media columna (filas=1):\n", media_col)
print("centrado por columna:\n", M - media_col)   # broadcast por columnas

media_fila = M.mean(axis=1, keepdims=True)   # forma (3,1)
print("centrado por fila:\n", M - media_fila)     # broadcast por filas
```

`None` (equivalente a `np.newaxis`) inserta un eje nuevo:

```python
u = np.array([1, 2, 3])
print(u[None, :].shape)    # (1,3)  vector fila
print(u[:, None].shape)    # (3,1)  vector columna
print(u[:, None] + u[None, :])   # suma exterior (3,3): tabla
```

## Indexación avanzada

Además de `array[i]`, `array[i:j]` y `array[:, k]`, NumPy permite indexar con
listas/arrays de índices y con máscaras booleanas.

### Indexación con listas de índices (fancy indexing)

```python
x = np.array([10, 20, 30, 40, 50])
print(x[[0, 2, 4]])        # [10 30 50] selecciona posiciones
print(x[[1, 1, 3]])        # repeticiones permitidas

M = np.arange(20).reshape(4, 5)
print(M[[0, 3]])           # filas 0 y 3
print(M[[0, 2], [1, 3]])   # pares (0,1) y (2,3)
```

### Máscaras booleanas

```python
datos = np.array([12, -3, 7, 0, 9, -1, 14])
positivos = datos[datos > 0]
pares = datos[datos % 2 == 0]
print("Positivos:", positivos)
print("Pares:", pares)

# Contar y filtrar combinando condiciones
suspensos = datos[(datos >= 0) & (datos < 10)]
print("No negativos y menores de 10:", suspensos)
```

> Usa `&` (y), `|` (o) y `~` (no) para combinar máscaras, y rodea cada condición
> entre paréntesis. `and`/`or` de Python daría error en arrays.

### Asignación con máscara

```python
notas = np.array([3, 8, 4, 7, 2, 9, 5])
# Sustituir todas las notas < 5 por 0
notas[notas < 5] = 0
print("Notas corregidas:", notas)

# Imputar a NaN la media de los válidos
valores = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
media = np.nanmean(valores)
valores[np.isnan(valores)] = media
print("Con NaN imputados:", valores)
```

## Funciones de selección y combinación

### `where`

`np.where(condición, a, b)` devuelve un elemento por posición eligiendo entre dos
arrays o valores.

```python
x = np.array([2, -5, 7, 0, -3])
print(np.where(x > 0, "positivo", "no positivo"))
print(np.where(x == 0, "cero", np.where(x > 0, "pos", "neg")))

# También sirve para obtener los índices que cumplen la condición
idx = np.where(x > 0)
print("Índices positivos:", idx[0])
```

### `clip`, `abs` y transformaciones rápidas

```python
x = np.array([-3.0, 0.0, 4.0, 7.0, 10.0])
print("abs:", np.abs(x))
print("clip a [0, 5]:", np.clip(x, 0, 5))

probas = np.array([-0.1, 0.2, 0.9, 1.3])
print("probas clip [0,1]:", np.clip(probas, 0, 1))

puntos = np.random.default_rng(1).normal(size=5)
print("signo:", np.sign(puntos))
```

### `argmax`, `argmin`, `argsort`, `unique`

```python
notas = np.array([6, 9, 5, 8, 4])
print("Índice del máximo:", notas.argmax())      # 1
print("Índice del mínimo:", notas.argmin())      # 4
print("Orden de menor a mayor:", np.argsort(notas))

edades = np.array([18, 20, 18, 22, 19, 20, 18])
print("Únicos:", np.unique(edades))
print("Únicos con conteo:", np.unique(edades, return_counts=True))
```

### `cumsum`, `diff`, `round`

```python
flujo = np.array([100, 50, -30, 20])
print("Acumulado:", np.cumsum(flujo))
print("Diferencias:", np.diff(flujo))

precios = np.array([3.1415, 2.7182, 1.4142])
print("Redondeo 2:", np.round(precios, 2))
```

## Álgebra lineal básica y utilidades

```python
A = np.array([[1., 2.], [3., 4.]])
B = np.array([[5., 6.], [7., 8.]])

print("Producto punto:", A @ B)          # o np.matmul(A, B)
print("Producto escalar:", A * B)        # elemento a elemento
print("Transpuesta:\n", A.T)
print("Determinante:", np.linalg.det(A))
print("Inversa:\n", np.linalg.inv(A))

# Resolver sistema Ax = b
b = np.array([1., 2.])
x = np.linalg.solve(A, b)
print("Solución x:", x)

# Autovalores y autovectores
va, ve = np.linalg.eig(A)
print("Autovalores:", va)
```

Utilidades frecuentes:

```python
print("Ceroneces (3,3):\n", np.eye(3))
print("Identidad:\n", np.eye(3))
print("Diagonal de A:", np.diag(A))
print("Matriz de ceros/ones:\n", np.zeros((2,2)), "\n", np.ones((2,2)))
print("Linspace:", np.linspace(0, 1, 5))
print("Arange:", np.arange(0, 10, 2))
```

### `np.concatenate`, `hstack`, `vstack`, `stack`

```python
u = np.array([1, 2])
v = np.array([3, 4])
print("Concat:", np.concatenate([u, v]))
print("Stack eje 0:\n", np.stack([u, v]))          # (2,2)
print("Stack eje 1:\n", np.stack([u, v], axis=1))  # (2,2) transpuesta

A = np.ones((2, 3))
B = np.ones((2, 2))
print("hstack:\n", np.hstack([A, B]))   # columnas
C = np.ones((1, 3))
print("vstack:\n", np.vstack([A, C]))   # filas
```

## Aleatoriedad reproducible

```python
rng = np.random.default_rng(seed=7)
print("uniformes:", rng.random(4))
print("normales:", rng.normal(loc=0, scale=1, size=4))
print("enteros:", rng.integers(1, 7, size=10))   # como un dado
print("choice:", rng.choice(["a", "b", "c"], size=5, p=[0.5, 0.3, 0.2]))
print("shuffle de una copia:", rng.permutation(np.arange(6)))
```

> Con `default_rng(seed)` el resultado es reproducible. No uses la API antigua
> `np.random.seed(...)` salvo compatibilidad.

## Aplicaciones que combinan todo

### Estandarización de una matriz de datos

```python
X = np.random.default_rng(0).normal(size=(100, 4))   # 100 muestras, 4 variables
media = X.mean(axis=0)
desv = X.std(axis=0)
X_std = (X - media) / desv
print("Forma:", X_std.shape)
print("Media por variable ≈ 0:", X_std.mean(axis=0).round(5))
print("Desv por variable ≈ 1:", X_std.std(axis=0).round(5))
```

### Filtrar y agrupar por condición

```python
datos = np.array([12, 3, 20, 7, 15, 1])
grandes = datos[datos >= 10]
pequenos = datos[datos < 10]
print("Grandes:", grandes, "| pequeños:", pequenos)
```

### Matriz de correlación a partir de datos

```python
X = np.random.default_rng(2).normal(size=(200, 3))
corr = np.corrcoef(X, rowvar=False)   # columnas = variables
print("Correlaciones:\n", corr.round(3))
print("La diagonal vale 1:", np.diag(corr).round(0))
```

## Ejercicios finales

1. Dada `M = np.arange(24).reshape(4, 6)`, obtén la suma por fila, por columna y total.
2. Centra `M` restando la media de cada **fila** (usa `keepdims=True`).
3. Con `datos = np.array([5, 2, 9, 1, 7, 4])`, selecciona los valores mayores que
   su media.
4. Usa `np.where` para clasificar un array de notas en `"Aprobado"` / `"Pendiente"`.
5. Genera 1000 normales con `default_rng` y comprueba que media y desviación se
   acercan al valor pedido.
6. Construye una tabla de multiplicar 5×5 con broadcasting (`a[:, None] * a[None, :]`).
7. Dado un array de temperaturas, sustituye los valores `np.nan` por la media.
8. Calcula la matriz de distancias por parejas de `[[0,0],[3,4],[6,8]]` y verifica
   que es simétrica y con diagonal 0.
9. Con `corrcoef` comprueba que, si añades una columna idéntica a otra, la
   correlación entre ambas es exactamente 1.
