# Álgebra lineal avanzada con NumPy

Este documento amplía [`06-numpy-avanzado.md`](06-numpy-avanzado.md) y la
[guía de casos prácticos](07c-casos-practicos-numpy.md) con un bloque dedicado al
álgebra lineal: normas, productos de matrices, resolución de sistemas, autovalores,
descomposiciones y sus aplicaciones directas al machine learning.

> Este material es **avanzado**: presupone que manejas creación de arrays, `shape`,
> `dtype` y broadcasting. No sustituye los documentos de introducción; los
> complementa cuando necesitas operar sobre matrices y vectores de forma expresiva.

## 1. Por qué álgebra lineal en NumPy

Casi todo modelo estadístico o de ML se expresa en términos de operaciones lineales:
productos matriz-vector, matrices de covarianza, distancias, proyecciones, PCA o
resolución de mínimos cuadrados. El submódulo `numpy.linalg` agrupa las operaciones
numéricamente optimizadas (implementadas sobre BLAS/LAPACK) para estos problemas.

Los dos resultados que debes aprender a interpretar con rapidez:

- **Formas.** Una matriz `X` de forma `(n_muestras, n_características)` casi siempre
  multiplica a un vector de `n_características` y produce resultados de `n_muestras`.
- **Condición del problema.** No toda operación es estable ni está bien planteada;
  una matriz singular o casi singular da resultados sin sentido o errores.

## 2. Productos de matriz y vector: `dot` / `matmul` / `@`

En NumPy moderno la forma preferida de multiplicar es el operador `@` (equivale a
`np.matmul`). `np.dot` queda para casos concretos. La regla clave del producto de
matrices: el número de columnas de la izquierda debe coincidir con el de filas de la
derecha.

```python
import numpy as np

A = np.array([[1., 2., 3.],
              [4., 5., 6.]])          # (2, 3)
v = np.array([1., 0., -1.])           # (3,)
b = A @ v                             # (2,): combina las columnas con v
print(b.shape, b)
```

Producto de matrices:

```python
B = np.array([[1., 0.],
              [0., 1.],
              [2., 2.]])              # (3, 2)
C = A @ B                             # (2, 2)
print(C)
```

Diferencias importantes:

| Expresión | Significado | Resultado |
|---|---|---|
| `A @ v` | matriz por vector | vector |
| `A @ B` | matriz por matriz | matriz |
| `A * B` | **elemento a elemento** (si formas compatibles) | no es producto matricial |
| `np.dot(A, v)` | equivalente a `A @ v` | vector |

Un error clásico es usar `*` creyendo que multiplica matrices. `*` (y `np.multiply`)
hace el producto término a término o broadcasting; para producto matricial usa `@`.

## 3. Normas y distancia

`numpy.linalg.norm` calcula la norma de un vector (por defecto la euclídea `L2`) o de
una matriz (Frobenius por defecto). Es la base de las distancias en k-NN, clustering,
regularización y evaluación de errores.

```python
p = np.array([3., 4.])
print(np.linalg.norm(p))          # 5.0  (raíz de 3^2 + 4^2)
print(np.linalg.norm(p, ord=1))   # 7.0  (suma de valores absolutos)
print(np.linalg.norm(p, ord=np.inf))  # 4.0 (máximo absoluto)
```

Norma por filas de una matriz (ejes al final):

```python
X = np.array([[0., 0.],
              [3., 4.],
              [6., 8.]])
norms = np.linalg.norm(X, axis=1)
print(norms)                      # [0., 5., 10.]
```

La distancia euclídea entre dos puntos es la norma de su diferencia:

```python
a = np.array([1., 2.])
b = np.array([4., 6.])
d = np.linalg.norm(a - b)
print(d)
```

## 4. Resolver sistemas lineales: `solve`

El sistema lineal `A·x = b` (con `A` cuadrada e invertible) se resuelve con
`np.linalg.solve`, que es más preciso y rápido que calcular `inv(A) @ b`.

```python
A = np.array([[2., 1.],
              [1., 3.]])
b = np.array([8., 13.])
x = np.linalg.solve(A, b)
print(x)                         # solución del sistema
print(A @ x)                     # debe reproducir b (aprox.)
```

Regla: **usa `solve`, no `inv`**, para resolver sistemas. Invertir es más costoso y
numéricamente menos estable. `inv` tiene sentido sobre todo cuando necesitas la matriz
inversa por sí misma o para varias `b` con la misma `A`.

## 5. Inversa, determinante y traza

```python
A = np.array([[2., 1.],
              [1., 3.]])
print(np.linalg.inv(A))       # inversa
print(np.linalg.det(A))       # determinante
print(np.trace(A))            # traza (suma de la diagonal)
```

Una matriz con determinante 0 (singular) no tiene inversa y `inv` lanza
`LinAlgError`. En la práctica, los determinantes de matrices grandes o mal
condicionadas pueden desbordarse (inf) o volverse 0 por errores de redondeo; la norma
de la inversa y el número de condición suelen ser mejores indicadores de estabilidad.

## 6. Autovalores y autovectores: `eig`

La factorización `A·v = λ·v` aparece en PCA, análisis de sistemas dinámicos,
PageRank y muchas áreas. `np.linalg.eig` devuelve los autovalores `w` y una matriz de
autovectores `v` (por columnas).

```python
A = np.array([[4., -2.],
              [1.,  1.]])
w, v = np.linalg.eig(A)
print("autovalores:", w)
print("autovectores:\n", v)
```

Para matrices **simétricas** (caso habitual en matrices de covarianza) conviene usar
`eigh`, que explota la simetría, es más estable y devuelve autovalores reales.

`svd` (descomposición en valores singulares) es la herramienta más robusta y se usa
para pseudoinversa, PCA y compresión; la veremos como descomposición al final.

## 7. Descomposición `svd` y su conexión con PCA

La **descomposición en valores singulares** (`svd`) factoriza cualquier matriz `X`
como `X = U·Σ·Vᵀ`. En datos con `X` de forma `(n, m)` (muestras, características), las
columnas de `V` son las direcciones de máxima varianza. Esto es la base no centrada
del análisis de componentes principales.

```python
X = np.random.default_rng(0).normal(size=(50, 4))
U, S, Vt = np.linalg.svd(X)
print("U:", U.shape, "s:", S.shape, "Vt:", Vt.shape)
print("valores singulares:", S)
```

Los **valores singulares** `S` (ordenados de mayor a menor) indican cuánta varianza
captura cada dirección. El cuadrado de `S` se relaciona con los autovalores de la
matriz de covarianza `XᵀX`. Una proyección PCA sobre las `k` primeras direcciones
reduce la dimensión conservando la mayor varianza posible.

Ejemplo: reconstruir `X` con las dos primeras componentes (PCA de bajo rango):

```python
k = 2
X_aprox = (U[:, :k] * S[:k]) @ Vt[:k, :]
print("error (Frobenius):", np.linalg.norm(X - X_aprox))
```

El error mide cuánta variabilidad se pierde al quedarse con 2 de 4 dimensiones. Esta
misma intuición aparece en reducción de dimensionalidad (UD3) y en visualización.

## 8. Aplicación: normalización de datos

Con `norm` y el eje correcto se normalizan filas (muestras) a norma 1, operación típica
antes de medir similitud por coseno o usar kernels:

```python
X = np.random.default_rng(1).normal(size=(5, 3))
norms = np.linalg.norm(X, axis=1, keepdims=True)
X_norm = X / norms
print("normas resultantes:", np.linalg.norm(X_norm, axis=1))
```

`keepdims=True` conserva la dimensión para que el broadcasting divida fila a fila.

## 9. Número de condición y matrices mal condicionadas

El número de condición (`np.linalg.cond`) dice cuán sensible es la solución a pequeños
cambios en los datos. Valores altos → problema mal condicionado:

```python
A = np.array([[1., 1.],
              [1., 1. + 1e-8]])
print("cond:", np.linalg.cond(A))   # enorme: casi singular
```

Ante matrices casi singulares, considera `pinv` (pseudoinversa de Moore-Penrose) o
métodos de regularización.

## 10. Errores frecuentes

1. Usar `*` en vez de `@` para productos de matrices.
2. No respetar la compatibilidad de dimensiones (intercambiar filas y columnas).
3. Resolver sistemas con `inv(A) @ b` en vez de `solve(A, b)`.
4. Calcular `det(A)` para decidir invertibilidad en matrices grandes o mal condicionadas.
5. Olvidar `keepdims=True` al normalizar por filas/columnas y fallar el broadcasting.
6. Asumir que `eig` devuelve siempre autovalores reales (mejor `eigh` en simétricas).

## 11. Ejercicios

1. Dadas `A (3,2)` y `B (2,4)`, comprueba que `(A @ B).shape == (3,4)` y que `B @ A` falla.
2. Calcula las distancias de cada fila de `X (5,3)` al origen con `np.linalg.norm(axis=1)`.
3. Resuelve el sistema `2x + y = 8`, `x + 3y = 13` con `solve` y verifica `A @ x ≈ b`.
4. Calcula `det`, `inv` y `trace` de una matriz 3×3 y comprueba `A @ inv(A) ≈ I`.
5. Obtén `eig` de una matriz simétrica 2×2 y confirma que los autovalores son reales.
6. Usa `svd` sobre `X (50,4)` y calcula el error al reconstruir con `k=1` y `k=3`; interpreta.
7. Normaliza las filas de `X` a norma 1 y comprueba el resultado.

## Referencias

- Wes McKinney, *Python for Data Analysis* (3.ª ed.), cap. 4.6 *Linear Algebra*.
- Hadrien Jean, *Essential Math for Data Science*, cap. 4 *Linear Algebra*.
- [Documentación de `numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html).
