# Entrada y salida de datos con NumPy

Este documento amplía el trabajo con NumPy hacia la **persistencia de datos**: guardar
y cargar arrays en formato binario de NumPy, y leer/escribir archivos de texto como
CSV. Es material **avanzado** y complementa [`06-numpy-avanzado.md`](06-numpy-avanzado.md)
y la [guía de casos prácticos](10-numpy-casos-practicos.md).

> En este bloque se entiende cómo mover datos hacia y desde NumPy con eficiencia.
> Para estructuras tabulares con etiquetas y columnas heterogéneas, en UD2 se usará
> pandas, que a su vez se apoya internamente en mecanismos similares.

## 1. Guardar y cargar un array binario: `.npy`

`np.save` guarda un array en formato binario `.npy` (con metadatos de forma y dtype);
`np.load` lo recupera.

```python
import numpy as np

x = np.arange(12).reshape(3, 4)
np.save("matriz.npy", x)

y = np.load("matriz.npy")
print(y, y.shape, y.dtype)
```

El formato `.npy` es **rápido** y conserva exactamente forma y tipo. Es la opción
recomendada para datos NumPy intermedios que no necesitan ser legibles por otros
programas.

## 2. Varios arrays: `.npz` (y `np.savez_compressed`)

Para guardar varios arrays a la vez, `np.savez` y `np.savez_compressed` empaquetan en
un único archivo `.npz`. Al cargarlo, accedes por nombre.

```python
a = np.array([1, 2, 3])
b = np.ones((2, 2))
np.savez("datos.npz", arr=a, mat=b)

datos = np.load("datos.npz")
print(datos["arr"], datos["mat"])
```

`np.savez_compressed` aplica compresión (archivo más pequeño, algo más lento). El
objeto devuelto por `np.load` para `.npz` es un *lazy*: lee de disco cuando accedes.

## 3. Leer y escribir texto: `savetxt` / `loadtxt`

`np.savetxt` escribe arrays en texto legible; `np.loadtxt` los lee. Útil para CSV
sencillos y para datos que deban verse o editarse con un editor.

```python
# Escribir a CSV (delimitador coma, sin cabecera)
data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])
np.savetxt("data.csv", data, delimiter=",", fmt="%.3f")

# Leer de vuelta
leido = np.loadtxt("data.csv", delimiter=",")
print(leido)
```

Opciones típicas de `loadtxt`: `skiprows=n` para saltar filas de cabecera, `dtype=...`
para forzar tipo, y `delimiter=","` para CSV.

## 4. Datos heterogéneos y faltantes: `genfromtxt`

Cuando el archivo mezcla texto y números, tiene cabeceras o celdas vacías, `genfromtxt`
es más flexible que `loadtxt`. Algunos fallos de importación se salvan dejando `nan`.

```python
import numpy as np
from io import StringIO

contenido = """
id,edad,ciudad
1,32,Madrid
2,nd,Barcelona
3,45,Valencia
"""
buf = StringIO(contenido)
datos = np.genfromtxt(
    buf,
    delimiter=",",
    names=True,
    dtype=[("id", "i8"), ("edad", "f8"), ("ciudad", "U20")],
    missing_values="nd",
    filling_values=np.nan,
)
print(datos)
print(datos["edad"])
```

`names=True` toma la primera fila como nombres de campos; un `dtype` explícito por
columna permite que la edad sea `float` y acepte `nan`; `missing_values`/`filling_values`
convierten tokens (aquí `nd`) a `nan`. Si dejas `dtype=None` y hay un valor ausente en
una columna entera, `genfromtxt` falla al rellenar con `nan`; fija el `dtype` adecuado.

> `genfromtxt` es útil para datos sencillos. Para tablas complejas, missing-data
> avanzado o fechas, pandas (UD2) ofrece mucho más control.

## 5. Archivos binarios sin formato y memmap

NumPy puede leer arrays en **archivos binarios planos** heredados con `fromfile` /
`tofile`, y mapear en memoria con `memmap`. El primero sirve para datos binarios que no
llevan metadatos; el segundo permite trabajar con conjuntos mayores que la RAM.

```python
z = np.arange(9, dtype=np.float32)
z.tofile("plano.bin")

leido = np.fromfile("plano.bin", dtype=np.float32)
print(leido)
```

Estos casos suelen aparecer en datos científicos o señales. Para datos tabulares,
pandas o parquet (UD2) son más cómodos.

## 6. Reproducibilidad y ruta de trabajo

- Fija la carpeta o ruta al guardar; no uses rutas absolutas frágiles en prácticas.
- Al cargar, comprueba `shape` y `dtype` antes de operar.
- Para experimentos reproducibles, guarda también la semilla y los parámetros.

## 7. Errores frecuentes

1. Usar `loadtxt` sobre un archivo con cabecera y olvidar `skiprows`.
2. Guardar con `np.save` y cargar con `np.loadtxt` (formatos incompatibles).
3. Olvidar el `dtype` al leer binarios planos con `fromfile`.
4. Ignorar que `np.savez(...)` pide arrays; si pasas un objeto no array puede fallar.
5. Suponer que `.npy` es legible como texto (no lo es).
6. No separar la conversión de tipos de la lectura en genfromtxt que mezcla texto.

## 8. Ejercicios

1. Crea un array 4×5, guárdalo como `.npy`, cárgalo y comprueba forma y dtype.
2. Guarda dos arrays en un `.npz` y recupera ambos por nombre.
3. Escribe 10 filas de 3 columnas a un CSV y vuelve a leerlas con `loadtxt`.
4. Lee un CSV con cabecera y una columna de texto usando `genfromtxt(names=True)`.
5. Con `savez_compressed`, comprueba que el archivo ocupa menos que `np.savez`.
6. Explica cuándo preferirías `.npy` frente a CSV y al revés.

## Referencias

- Wes McKinney, *Python for Data Analysis* (3.ª ed.), cap. 4.5 *File Input and Output
  with Arrays*.
- Python NumPy For Beginners (AI Publishing), caps. 3.6 y 4.4 (save/load y CSV).
- [Documentación de NumPy I/O](https://numpy.org/doc/stable/reference/routines.io.html).
