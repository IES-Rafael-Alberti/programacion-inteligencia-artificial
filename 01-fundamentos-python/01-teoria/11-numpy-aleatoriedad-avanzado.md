# Aleatoriedad y números aleatorios avanzados con NumPy

Este documento profundiza en la generación de números aleatorios más allá de lo
visto en [`06-numpy-avanzado.md`](06-numpy-avanzado.md) (donde se introdujo
`default_rng` y `normal`). Aquí se trabajan las **distribuciones de probabilidad**, la
selección y permutación, la reproducibilidad y patrones útiles para simulación y ML.

> Material **avanzado**: presupone el uso de `default_rng` con semilla. No repite la
> introducción; amplía las distribuciones, sus usos y buenas prácticas.

## 1. La API moderna: `Generator` y `default_rng`

NumPy recomendó abandonar la API global antigua (`np.random.rand`, `np.random.normal`)
en favor del objeto `Generator` creado con `np.random.default_rng`.

```python
import numpy as np

rng = np.random.default_rng(2026)   # semilla fija -> reproducible
print(rng.normal(size=5))
```

Ventajas de `Generator`:

- **Aislado**: los cambios de semilla no modifican el estado global del módulo.
- **Más rápido** y con mejores algoritmos en varias distribuciones.
- **Consistente**: mismo objeto, misma secuencia si las llames en el mismo orden.

## 2. Distribuciones continuas

Cada método del `Generator` produce muestras de una distribución. Se usan para crear
datos sintéticos, inicializar pesos, añadir ruido o simular escenarios.

```python
rng = np.random.default_rng(0)

uniformes  = rng.uniform(low=0, high=10, size=5)     # U(0,10)
normales   = rng.normal(loc=5, scale=2, size=5)      # N(5, 2)
exponencial = rng.exponential(scale=1.0, size=5)     # Exp(1)
print(\"uniforme:\", uniformes)
print(\"normal:\", normales)
print(\"exponencial:\", exponencial)
```

| Método | Distribución | Uso típico |
|---|---|---|
| `uniform` | uniforme continua | ruido, coordenadas, parámetros |
| `normal` | gaussiana | errores, datos sintéticos, pesos |
| `exponential` | exponencial | tiempos entre eventos |
| `beta` | beta | proporciones, prior en Bayes |
| `gamma` | gamma | tiempos de vida, escalas |

## 3. Distribuciones discretas

```python
rng = np.random.default_rng(1)

enteros  = rng.integers(low=0, high=10, size=8)      # 0..9
binomial = rng.binomial(n=10, p=0.5, size=8)          # nº de éxitos en 10 pruebas
poisson  = rng.poisson(lam=3.0, size=8)               # conteos con media 3
print(\"enteros:\", enteros)
print(\"binomial:\", binomial)
print(\"poisson:\", poisson)
```

| Método | Distribución | Uso típico |
|---|---|---|
| `integers` | uniforme discreta | índices, muestreo, datos categóricos |
| `binomial` | binomial | nº de éxitos en pruebas |
| `poisson` | poisson | conteos de eventos por intervalo |
| `multinomial` | multinomial | extraer de categorías |

## 4. Selección y permutación: `choice`, `shuffle`, `permutation`

Para dividir datos, barajar conjuntos o elegir subconjuntos al azar:

```python
rng = np.random.default_rng(7)
datos = np.arange(10)

barajado = rng.permutation(datos)             # copia barajada
rng.shuffle(datos)  # o baraja in-place (modifica datos)
muestra  = rng.choice(np.arange(20), size=5, replace=False)  # sin repetición
print(\"permutación:\", barajado)
print(\"choice sin repetición:\", muestra)
```

`rng.shuffle(arreglo)` modifica el array en el sitio; `rng.permutation(arreglo)`
devuelve una copia barajada. Con `replace=True` (por defecto `True` en `choice` según
versión; especifícalo siempre) se permite repetir elementos.

Selección con probabilidades:

```python
categorias = np.array([\"a\", \"b\", \"c\"])
probs = np.array([0.5, 0.3, 0.2])
eleccion = rng.choice(categorias, size=1000, p=probs)
print(\"frecuencias (aprox.):\", np.unique(eleccion, return_counts=True)[1] / 1000)
```

## 5. Reproducibilidad: la semilla y el orden de las llamadas

Una misma semilla reproduce la misma secuencia **si llamas a los métodos en el mismo
orden**.

```python
r1 = np.random.default_rng(42)
r2 = np.random.default_rng(42)
print(np.array_equal(r1.normal(size=4), r2.normal(size=4)))  # True
```

Puntos a tener en cuenta:

- La reproducibilidad es **determinística en el mismo entorno**, no entre plataformas
  ni versiones de NumPy.
- Un cambio de versión de NumPy puede alterar las secuencias.
- Para reproducir exactamente un experimento conviene fijar la semilla al inicio de la
  práctica y documentarla.

## 6. Semillas por proceso o por bloque

En experimentos largos puede ser útil crear un `Generator` por bloque en lugar de uno
por celda:

```python
def experimento(semilla):
    rng = np.random.default_rng(semilla)
    return rng.normal(loc=0, scale=1, size=1000).mean()

medias = [experimento(s) for s in range(5)]
print(medias)
```

Esto permite que cada ejecución sea reproducible e independiente del resto.

## 7. Aplicación: dividir un dataset en entrenamiento y test

Una división típica consiste en barajar índices y partir:

```python
rng = np.random.default_rng(10)
n = 100
indices = rng.permutation(n)
proporcion = 0.8
punto = int(n * proporcion)
train_idx, test_idx = indices[:punto], indices[punto:]
print(\"train:\", len(train_idx), \"test:\", len(test_idx))
```

En el módulo usarás directamente `train_test_split` (scikit-learn) en UD3, que por
dentro hace algo parecido; entender este patrón aclara la reproducibilidad del split
(`random_state` es la semilla).

## 8. Errores frecuentes

1. Usar la API global (`np.random.rand`) mezclada con `Generator`; fija uno solo.
2. Olvidar la semilla y no poder reproducir el experimento.
3. Barajar el dataset **y sus etiquetas por separado** (se pierde la correspondencia).
4. No distinguir `shuffle` (in-place) de `permutation` (copia).
5. Llamar métodos en distinto orden entre dos copias con la misma semilla y esperar
   idéntico resultado.
6. Suponer que la media/desviación empírica de una muestra pequeña coincide con los
   parámetros de la distribución (depende del tamaño).

## 9. Ejercicios

1. Con semilla `0`, genera 1000 `uniform(0,1)` y comprueba que la media ≈ 0.5.
2. Genera 1000 `poisson(3)` y compara su media con 3.
3. Tira 10 veces una moneda (binomial) 1000 veces y guarda la proporción de caras.
4. Divide un array de 120 índices en 80/20 con la misma semilla dos veces y verifica
   que ambas divisiones coinciden.
5. Con `choice` y `p`, selecciona 1000 valores de tres categorías y compara frecuencias.
6. Baraja un dataset de 2D conservando la correspondencia fila-etiqueta (baraja un
   único vector de índices).
7. Explica por qué no debes barajar características y etiquetas por separado.

## Referencias

- Wes McKinney, *Python for Data Analysis* (3.ª ed.), cap. 4.2 *Pseudorandom Number
  Generation*.
- [Documentación de `numpy.random`](https://numpy.org/doc/stable/reference/random/index.html).
- [Guía de buenas prácticas para generación de números aleatorios de NumPy](https://numpy.org/doc/stable/reference/random/generator.html).
