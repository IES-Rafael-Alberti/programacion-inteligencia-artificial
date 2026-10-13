# NumPy avanzado: arrays como datos estructurados

Este documento continúa [`05-numpy-introduccion.md`](05-numpy-introduccion.md). El objetivo no es memorizar toda la API, sino razonar sobre forma, tipo y coste. El notebook [`09_numpy_avanzado.ipynb`](../02-ejemplos/09_numpy_avanzado.ipynb) acompaña cada bloque.

## 1. Tipo de dato y memoria

Un `ndarray` almacena elementos homogéneos. `dtype` fija su representación y `itemsize` sus bytes:

```python
import numpy as np
enteros = np.array([1, 2, 3], dtype=np.int32)
reales = np.array([1, 2, 3], dtype=np.float64)
print(enteros.dtype, enteros.itemsize, enteros.nbytes)
print(reales.dtype, reales.itemsize, reales.nbytes)
```

Usa el tipo mínimo que conserve la precisión necesaria, pero no conviertas sin más datos científicos a tipos pequeños: `int8` puede desbordarse y `float32` tiene menos precisión que `float64`.

## 2. `shape`, ejes y cambios de forma

`shape` describe el tamaño de cada eje; `ndim` cuenta ejes. En `(filas, columnas)`, `axis=0` produce un resultado por columna y `axis=1` uno por fila:

```python
x = np.arange(12).reshape(3, 4)
print(x.shape, x.ndim)
print(x.sum(axis=0))
print(x.sum(axis=1))
```

`reshape(-1, 2)` calcula una dimensión, pero debe conservar el número total de elementos. `transpose()` intercambia ejes; no es un simple `reshape`.

## 3. Indexado avanzado y máscaras

Las máscaras seleccionan los elementos que cumplen una condición. Los índices enteros permiten seleccionar posiciones concretas:

```python
datos = np.array([4, 11, 7, 15, 2])
print(datos[datos >= 10])
datos[datos < 10] = 0
matriz = np.arange(9).reshape(3, 3)
filas, columnas = np.array([0, 2]), np.array([1, 0])
print(matriz[filas, columnas])
```

Combina condiciones con `(datos > 3) & (datos < 12)`, `|` y `~`. No uses `and`/`or` con arrays.

## 4. Selección condicional

`where` elige elemento a elemento y `select` permite varias categorías:

```python
notas = np.array([4.5, 6.0, 8.5, 9.7])
print(np.where(notas >= 5, "apto", "no apto"))
rangos = np.select([notas < 5, notas < 7, notas < 9],
                   ["insuficiente", "aprobado", "notable"],
                   default="sobresaliente")
```

## 5. Agregaciones por eje

`sum`, `mean`, `min`, `max`, `std` y `argmax` aceptan `axis`. `keepdims=True` conserva el eje reducido y facilita normalizar:

```python
medidas = np.array([[10., 20., 30.], [12., 18., 33.]])
media_columna = medidas.mean(axis=0, keepdims=True)
centradas = medidas - media_columna
print(centradas.mean(axis=0))
```

Antes de agregar, decide qué representa cada eje. `argmax` devuelve el índice, no el valor. Para ausentes existen `nanmean` y la familia `nan*`, pero hay que documentar qué implica ignorarlos.

## 6. Copias y vistas

Un slice básico suele ser una vista que comparte memoria; el indexado avanzado y `.copy()` producen copias independientes:

```python
base = np.arange(6)
vista = base[1:4]
vista[0] = 99
copia = base[1:4].copy()
copia[0] = -1
print(base, copia)
print(np.shares_memory(base, vista), np.shares_memory(base, copia))
```

Usa `.copy()` cuando el resultado deba ser independiente; una vista ahorra memoria, pero exige controlar su ciclo de vida.

## 7. Aleatoriedad reproducible

Prefiere `Generator` y una semilla explícita frente a la API global antigua:

```python
rng = np.random.default_rng(2026)
muestra = rng.normal(loc=0, scale=1, size=5)
indices = rng.choice(10, size=3, replace=False)
```

La misma semilla y secuencia de llamadas producen resultados reproducibles en el mismo entorno. Reproducibilidad no significa aleatoriedad criptográfica.

## 8. Vectorización y rendimiento

Una operación vectorizada delega el bucle en código optimizado, en vez de iterar en Python. Mide antes de optimizar y evita temporales innecesarios cuando el tamaño sea importante:

```python
import time
x = np.arange(100_000, dtype=np.float64)
t0 = time.perf_counter()
y = x * x + 2 * x + 1
print(y[:3], time.perf_counter() - t0)
```

Vectorizar no corrige una forma incorrecta: comprueba siempre `shape`, dtype y resultado.

## 9. Puente hacia otras herramientas

- **pandas** añade etiquetas, índices, columnas heterogéneas y operaciones tabulares.
- **JAX** ofrece una API parecida para transformar funciones, compilar y usar aceleradores; sus arrays son inmutables.
- **PyTorch** trabaja con tensores, gradientes automáticos y GPU; sus dimensiones y operaciones por eje transfieren este razonamiento.

Elige NumPy para arrays densos, pandas para tablas etiquetadas, JAX para funciones transformables/aceleradas y PyTorch para entrenamiento con gradientes.

## Errores frecuentes

- Confundir `axis=0` con “primera fila”.
- Hacer `reshape` sin verificar el número de elementos.
- Usar `and`/`or` en vez de `&`/`|` con paréntesis.
- Modificar sin querer una vista.
- Usar semilla global o medir una sola ejecución.

## Checklist y ejercicios breves

¿Sé qué representa cada eje? ¿He comprobado `shape` y `dtype`? ¿La máscara está entre paréntesis? ¿Sé si comparto memoria? ¿La semilla está documentada? ¿He medido una versión razonable?

1. Crea 12 temperaturas `float32`, calcula media y máximo por día y normalízalas por columnas.
2. Selecciona mediciones entre 10 y 30 y clasifícalas con `select`.
3. Demuestra la diferencia entre slice, indexado avanzado y `.copy()`.
4. Genera 1000 valores con `Generator` y comprueba que la misma semilla repite el resultado.
5. Justifica cuándo elegirías NumPy, pandas, JAX o PyTorch.
