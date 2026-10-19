# Funciones universales y estadística avanzada con NumPy

Este documento amplía el trabajo con **ufuncs** y **estadística descriptiva** más allá
de lo visto en [`06-numpy-avanzado.md`](06-numpy-avanzado.md) y en la
[guía de casos prácticos](10-numpy-casos-practicos.md). Es material **avanzado**:
asume que ya manejas arrays, `axis`, máscaras y `np.where`.

## 1. Qué es una ufunc y qué aprovechar

Una *universal function* (ufunc) es una operación **vectorizada** que se aplica a cada
elemento de uno o más arrays al mismo tiempo, con soporte de *broadcasting* y salida
opcional. Está implementada en C, por lo que evita bucles de Python.

```python
import numpy as np

x = np.array([1., 2., 4.])
print(np.sqrt(x))      # raíz
print(np.exp(x))       # exponencial
print(np.log(x))       # logaritmo natural
```

`np.add`, `np.multiply`... son ufuncs, así como `np.sqrt`, `np.sin`, `np.exp`. Tienen
un método `.reduce`, `.accumulate` y `.outer` que los vuelven extremadamente útiles.

## 2. Reducciones y acumulaciones: `reduce`, `accumulate`, `outer`

```python
x = np.array([1, 2, 3, 4])
print(np.add.reduce(x))        # 1+2+3+4 = 10
print(np.multiply.accumulate(x))  # producto acumulado: [1,2,6,24]
print(np.outer(np.array([1,2]), np.array([10,20,30])))  # producto exterior
```

- `reduce`: combina todos los elementos con la operación.
- `accumulate`: guarda los resultados parciales.
- `outer`: combina cada par de elementos (tabla).

Estas operaciones aparecen en cálculo de probabilidades conjuntas, sumas parciales y
matrices de interacciones.

## 3. Redondeo y límites: `round`, `floor`, `ceil`, `clip`

Para controlar la precisión de resultados o restringir valores a un rango:

```python
x = np.array([1.234, 2.567, -0.5])
print(np.round(x, 1))   # [1.2, 2.6, -0.5]
print(np.floor(x))      # [1., 2., -1.]
print(np.ceil(x))       # [2., 3., -0.]

v = np.array([-2., 0.5, 3.9])
print(np.clip(v, 0, 1))  # acota a [0,1]: [0., 0.5, 1.]
```

`clip` es muy usado para limitar probabilidades o predicciones a un rango válido.

## 4. Estadística avanzada: percentiles, histograma y conteo

```python
datos = np.random.default_rng(5).normal(loc=10, scale=3, size=500)
print("percentiles:", np.percentile(datos, [25, 50, 75]))
print("min/max:", datos.min(), datos.max())

hist, bordes = np.histogram(datos, bins=10)
print("histograma (alturas):", hist)
```

- `percentile` da cuantiles; útil para describir distribución y outliers.
- `histogram` agrupa en intervalos; la base de muchas visualizaciones.
- `np.bincount` cuenta enteros no negativos (rápida para conteos):

```python
enteros = np.array([0, 1, 1, 3, 2, 1, 3])
print(np.bincount(enteros))   # [1, 3, 1, 2] : frecuencia de cada valor 0,1,2,3
```

## 5. `unique`, orden y selección de valores

```python
valores = np.array([3, 1, 3, 2, 1, 2, 3])
valores_unicos, cuentas = np.unique(valores, return_counts=True)
print(valores_unicos, cuentas)
```

Para clasificación y frecuencias de categorías, `unique(return_counts=True)` es
directo. Para estadística robusta, `median` y `percentile` son menos sensibles a
outliers que `mean`.

## 6. Correlación y covarianza

`np.corrcoef` y `np.cov` cuantifican asociación lineal. Recuerda `rowvar=False` para
que cada **columna** sea una variable:

```python
rng = np.random.default_rng(7)
horas = rng.uniform(0, 8, size=200)
resultado = 2.5 * horas + rng.normal(0, 2, size=200)
X = np.column_stack([horas, resultado])
print(np.corrcoef(X, rowvar=False).round(3))
print(np.cov(X, rowvar=False).round(2))
```

La correlación no implica causalidad; la covarianza depende de las unidades y la
correlación normaliza a `[-1, 1]`.

## 7. Funciones lógicas y comparaciones como ufuncs

Las comparaciones (`np.greater`, `np.less`, `np.equal`) son ufuncs que devuelven arrays
booleanos. Se combinan con `&`, `|`, `~` y paréntesis:

```python
x = np.array([1, 5, 9, 14])
print(np.greater(x, 7))
print((x > 3) & (x < 12))
print(np.logical_and(x > 3, x < 12))   # equivalente
```

## 8. Combinar en patrones prácticos

Normalizar a rango `[0,1]`, robusto a outliers, y etiquetar con `select`:

```python
rng = np.random.default_rng(2)
datos = rng.normal(loc=50, scale=15, size=100)
minimo, q1, mediana, q3, maximo = np.percentile(datos, [0, 25, 50, 75, 100])
print("resumen:", minimo, q1, mediana, q3, maximo)
```

Con `np.select` se clasifica en categorías:

```python
etiquetas = np.select(
    [datos < q1, datos < mediana, datos < q3],
    ["bajo", "medio", "alto"],
    default="muy alto",
)
print(np.unique(etiquetas, return_counts=True))
```

## 9. Errores frecuentes

1. Usar `np.round` esperando redondeo "a la mitad" idéntico a otras herramientas
   (NumPy usa redondeo de banquero en algunos casos).
2. Confundir `histogram` (devuelve conteos + bordes) con `bincount` (conteo de enteros).
3. Olvidar `rowvar=False` en `corrcoef`/`cov` cuando las variables son columnas.
4. Aplicar `mean` a datos con `nan` sin `nanmean` (o sin limpiar).
5. Usar `np.unique(..., return_counts=True)` olvidando desempaquetar dos valores.
6. No poner paréntesis en combinaciones lógicas con `&`/`|`.

## 10. Ejercicios

1. Calcula `sqrt`, `exp` y `log` de un array y compara su forma de entrada/salida.
2. Usa `multiply.accumulate` para el producto parcial de `[1..5]`.
3. Acota un array de probabilidades a `[0,1]` con `clip`.
4. Genera 1000 valores y obtén percentiles 5, 25, 50, 75, 95.
5. Cuenta frecuencias de un array de categorías con `unique(return_counts=True)`.
6. Calcula la correlación entre dos columnas relacionadas y entre dos independientes.
7. Clasifica un array en 4 tramos con `np.select` a partir de los cuartiles.

## Referencias

- Jake VanderPlas, *Python Data Science Handbook* (2.ª ed.), Parte II, caps. 6–7
  (ufuncs y agregaciones).
- Python NumPy For Beginners (AI Publishing), cap. 4 (estadística y trucos).
- [Documentación de rutinas estadísticas de NumPy](https://numpy.org/doc/stable/reference/routines.statistics.html).
