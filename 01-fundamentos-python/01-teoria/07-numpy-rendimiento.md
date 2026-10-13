# Rendimiento y vectorización con NumPy

Esta guía acompaña al [notebook de rendimiento con listas de Python y NumPy](../02-ejemplos/06_numpy_rendimiento.ipynb). El notebook permite repetir las mediciones; esta página fija los conceptos y los criterios para interpretarlas.

## Qué significa vectorizar

Vectorizar significa expresar una operación sobre un conjunto completo de datos mediante operaciones de array, evitando que un bucle Python visite los elementos uno a uno. El contraste no está sólo en cambiar el nombre de una función, sino en cambiar quién recorre los datos y cómo se expresa el cálculo.

En Python, este flujo expone el recorrido elemento a elemento al intérprete:

```python
values = [1.0, 2.0, 3.0]
scaled = []
for value in values:
    scaled.append(value * 10)
```

El flujo equivalente con un `ndarray` expresa la operación para todo el array:

```python
import numpy as np

values = np.array([1.0, 2.0, 3.0])
scaled = values * 10
print(scaled)
```

En `values * 10`, el recorrido sigue existiendo, pero lo realiza la implementación de NumPy sobre el bloque de datos, no el bucle Python escrito por la persona que programa. La misma idea se aplica a una reducción como `np.sum`:

```python
total = 0.0
for value in [1.0, 2.0, 3.0]:
    total += value
```

frente a:

```python
total = np.sum(values)
```

NumPy conoce el tipo y la disposición de los datos y puede delegar el recorrido en implementaciones compiladas y optimizadas. Esto reduce el trabajo repetido del intérprete; no significa que toda operación NumPy sea automáticamente más rápida.

Vectorizar tampoco significa simplemente «usar NumPy» ni implica ejecutar en una GPU. Una llamada NumPy puede contener un bucle Python alrededor de operaciones pequeñas, crear copias innecesarias o usar una ruta CPU; la GPU requiere otras bibliotecas y una transferencia de datos que también debe medirse.

## Qué no significa vectorizar

- No significa convertir cualquier código en una expresión de una sola línea.
- No significa eliminar todos los bucles: un bucle sobre pocas operaciones o lógica irregular puede ser más claro.
- No significa que construir el array sea gratis.
- No significa que una operación vectorizada sea siempre mejor: copias y arrays temporales pueden anular la ventaja.
- No es una promesa de una cifra fija de aceleración: depende de tamaño, tipos, operación, versiones, hardware y carga del sistema.

## Vectorización y broadcasting

El *broadcasting* permite combinar arrays de formas compatibles sin escribir manualmente un bucle para repetir valores. Es una herramienta relacionada con la vectorización, pero no son sinónimos:

```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
offset = np.array([10, 20])
print(matrix + offset)  # offset se aplica a cada fila
```

Si las formas no son compatibles, NumPy lanza `ValueError`; no conviene forzar el broadcasting con copias innecesarias. Consulta la [guía específica de broadcasting](07-broadcasting-numpy.md) para sus reglas.

## Cómo comparar implementaciones

El notebook compara suma, media, mediana y desviación estándar sobre una lista y sobre un array ya construido. Usa `perf_counter`, una ejecución de *warm-up* y varias repeticiones. Así no mezcla la conversión `list -> np.array` con el cálculo y reduce el peso de la inicialización en la primera llamada.

Una medición mínima reproducible puede seguir este patrón:

```python
from time import perf_counter

def benchmark(function, argument, repeats=5):
    function(argument)  # warm-up
    times = []
    for _ in range(repeats):
        start = perf_counter()
        function(argument)
        times.append(perf_counter() - start)
    return sum(times) / len(times)
```

Registra tamaño de entrada, tipo y `dtype`, versiones de Python/NumPy, hardware y qué trabajo queda fuera de la medición. Repite el experimento y observa la variabilidad, no sólo el promedio.

Una comparación sólo es justa si calcula el mismo resultado y usa datos equivalentes. El coste puede variar por el algoritmo, `ddof`, caché, memoria, otros procesos, tamaño y `dtype`. Los resultados del notebook son evidencia de ese entorno y esos tamaños, no cifras universales.

## Errores frecuentes

1. Medir la generación o conversión a array en una sola implementación.
2. Comparar funciones que no calculan exactamente la misma estadística.
3. Ejecutar una sola vez y concluir a partir de un valor ruidoso.
4. Usar arrays de `object` esperando el comportamiento de un `dtype` numérico.
5. Crear arrays temporales grandes sin considerar memoria.
6. Confundir una comprensión de listas con vectorización: su cuerpo sigue ejecutándose en Python.

## Checklist

- [ ] ¿La operación calcula el mismo resultado en ambas versiones?
- [ ] ¿Los datos se generan y convierten fuera de la región medida?
- [ ] ¿Se ha hecho *warm-up* y se han usado varias repeticiones?
- [ ] ¿Se han anotado tamaño, `dtype`, versiones y plataforma?
- [ ] ¿Se ha comprobado la corrección numérica antes de comparar tiempos?
- [ ] ¿La conclusión declara límites y evita generalizar una cifra concreta?
