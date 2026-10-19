# Casos prácticos de NumPy

Esta guía acompaña la teoría de NumPy avanzado con patrones reutilizables para
analizar matrices, preparar features y comprobar resultados. Está pensada para
trabajarse junto con el notebook `10_numpy_casos_practicos.ipynb`.

## 1. Leer formas antes de operar

Antes de combinar arrays, imprime `shape`, `ndim` y `dtype`. Así puedes razonar
sobre las dimensiones y detectar incompatibilidades antes de que aparezca un
error.

```python
import numpy as np

X = np.arange(24, dtype=np.float32).reshape(4, 6)
print("forma:", X.shape, "ejes:", X.ndim, "tipo:", X.dtype)
```

En una matriz `X` con filas de muestras y columnas de variables, `axis=0`
normalmente resume cada variable; `axis=1` resume cada muestra. No memorices los
números aislados: pregunta qué eje quieres conservar.

## 2. Centrar y escalar columnas

Para restar la media de cada variable, la media debe conservar una fila. Para
centrar cada muestra, debe conservarse una columna. `keepdims=True` hace visible
la forma adecuada para broadcasting.

```python
rng = np.random.default_rng(10)
X = rng.normal(loc=[10, 100, 1000], scale=[2, 20, 200], size=(5, 3))

media = X.mean(axis=0, keepdims=True)  # (1, 3)
desv = X.std(axis=0, keepdims=True)    # (1, 3)
X_estandar = (X - media) / desv

print("media resultante:", X_estandar.mean(axis=0).round(6))
print("desviación resultante:", X_estandar.std(axis=0).round(6))
```

En datos reales, los parámetros de escalado se calculan solo con entrenamiento y
después se reutilizan en validación y test. Calcularlos sobre todo el dataset
antes de dividirlo produce fuga de información.

## 3. Aplicar límites y reglas elemento a elemento

`clip` limita valores a un intervalo; `where` elige entre dos resultados y
`select` permite varias categorías.

```python
probas = np.array([-0.2, 0.15, 0.52, 0.91, 1.3])
probas_validas = np.clip(probas, 0, 1)
etiquetas = np.where(probas_validas >= 0.5, 1, 0)
print(probas_validas)
print(etiquetas)

notas = np.array([3.5, 5.0, 6.8, 8.9, 9.5])
rangos = np.select(
    [notas < 5, notas < 7, notas < 9],
    ["insuficiente", "aprobado", "notable"],
    default="sobresaliente",
)
print(rangos)
```

## 4. Filtrar, contar y resumir

Las máscaras permiten seleccionar y modificar solo las posiciones que cumplen
una condición. Al combinar varias condiciones, usa `&`/`|` y paréntesis.

```python
temperaturas = np.array([18.2, 21.0, np.nan, 31.5, 24.1, np.nan])
validas = temperaturas[~np.isnan(temperaturas)]
print("válidas:", validas)
print("entre 20 y 30:", validas[(validas >= 20) & (validas <= 30)])
print("número de ausentes:", np.isnan(temperaturas).sum())
```

Para localizar máximos, ordenar posiciones o encontrar valores distintos:

```python
ventas = np.array([12, 8, 12, 20, 8, 15])
print("posición de la mayor:", ventas.argmax())
print("índices ordenados:", ventas.argsort())
print("valores y frecuencias:", np.unique(ventas, return_counts=True))
```

## 5. Construir combinaciones mediante `newaxis`

Insertar un eje explícitamente hace más fácil predecir el resultado del
broadcasting.

```python
ancho = np.array([1, 2, 3, 4])
alto = np.array([10, 20, 30])

tabla = alto[:, None] * ancho[None, :]
print("forma:", tabla.shape)  # (3, 4)
print(tabla)
```

Esto construye todas las combinaciones de valores. La misma idea puede generar
coordenadas, interacciones entre variables o una matriz de distancias.

### Distancias entre todos los pares de puntos

```python
puntos = np.array([[0., 0.], [3., 4.], [6., 8.]])
diferencias = puntos[:, None, :] - puntos[None, :, :]
distancias = np.sqrt((diferencias ** 2).sum(axis=-1))
print(distancias)
```

Comprueba dos propiedades: la matriz es simétrica y su diagonal contiene ceros.
Para miles de puntos, una matriz completa puede ocupar mucha memoria; el patrón
sirve para aprender y para conjuntos pequeños, mientras que algoritmos reales
usan métodos por bloques o estructuras específicas.

## 6. Elegir una operación estadística

```python
datos = np.array([2, 3, 3, 5, 8, 100])
print("media:", datos.mean())
print("mediana:", np.median(datos))
print("cuartiles:", np.percentile(datos, [25, 50, 75]))
```

La media reacciona mucho a valores extremos; la mediana suele ser más robusta.
La elección depende de la pregunta y de la distribución observada.

## 7. Generación aleatoria reproducible

Usa `default_rng` con semilla explícita para reproducir un experimento:

```python
rng = np.random.default_rng(42)
muestra = rng.normal(loc=0, scale=1, size=1000)
print(muestra[:5])
print("media/desviación:", muestra.mean(), muestra.std())
```

La media y desviación de una muestra finita no serán exactamente 0 y 1. Aumentar
el tamaño suele acercar los estadísticos a esos parámetros.

## 8. Correlación no significa causalidad

```python
rng = np.random.default_rng(7)
horas = rng.uniform(0, 8, size=200)
resultado = 2.5 * horas + rng.normal(0, 2, size=200)
otra = rng.normal(size=200)

X = np.column_stack([horas, resultado, otra])
print(np.corrcoef(X, rowvar=False).round(2))
```

`rowvar=False` indica que las columnas son variables. La matriz resume asociación
lineal: por sí sola no demuestra causalidad ni detecta toda relación no lineal.

## Ejercicios para el aula

1. Crea una matriz de 6 estudiantes × 4 asignaturas; calcula media por estudiante
   y por asignatura. Explica qué eje se reduce en cada caso.
2. Normaliza las columnas al intervalo `[0, 1]` usando `keepdims=True`.
3. Genera una máscara para notas aprobadas y devuelve las posiciones con
   `np.where`.
4. Construye una tabla de productos con dos vectores y explica sus formas antes
   de ejecutar el código.
5. Calcula distancias entre cuatro puntos 2D y comprueba simetría y diagonal.
6. Compara media y mediana cuando una observación es mucho mayor que las demás.
7. Repite una simulación con la misma semilla y verifica la reproducibilidad.
8. Explica por qué no se deben calcular los parámetros de escalado con el test.

## Qué parte resuelve NumPy y qué parte no

NumPy aporta arrays homogéneos, operaciones vectorizadas, reglas de broadcasting
y herramientas numéricas. No reemplaza el análisis del problema, la elección de
una representación apropiada ni el control de fuga de datos. Para tablas con
etiquetas y columnas heterogéneas se puede usar pandas (UD2); para transformaciones
de funciones y aceleración puede estudiarse JAX; PyTorch añade tensores y
gradientes para modelos de deep learning.
