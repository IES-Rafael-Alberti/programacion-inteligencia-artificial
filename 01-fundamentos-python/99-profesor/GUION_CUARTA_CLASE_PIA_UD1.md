# Guion de la cuarta clase de PIA — NumPy ampliado, JAX y R opcional

> **Documento interno del profesorado. No publicar en GitHub Pages ni en Moodle.**

**Duración:** 2 horas.
**Punto de continuidad:** en la anterior sesión se trabajó NumPy a nivel
introductorio y de broadcasting, pero el grupo pidió más contenido y más
ejemplos porque no alcanzó para una hora completa.

## Objetivo

Consolidar NumPy en profundidad con muchos ejemplos ejecutables (ejes,
reducciones, indexación avanzada, máscaras, `where`, álgebra lineal y
aplicaciones). Si el entorno lo permite, comparar NumPy con JAX (`jax.numpy`,
`jit`, `grad`, `vmap`). La introducción a R queda **opcional**: solo si el grupo
cierra NumPy/JAX con holgura y hay tiempo.

## Estructura

| Tiempo | Bloque |
|---|---|
| 0–10 | Recuperar la sesión anterior: qué es un `ndarray`, `shape`, operaciones vectorizadas. |
| 10–45 | **NumPy en profundidad**: ejes y `axis`, `keepdims`, `newaxis`, reducciones. |
| 45–75 | Mismo bloque: indexación avanzada, máscaras, `where`, `clip`, `argmax/argsort/unique`, uso con datos. |
| 75–90 | **Álgebra lineal** (`@`, `solve`, `det`, `inv`, `eig`) y utilidades. |
| 90–105 | **Aplicaciones** con broadcasting: estandarización, tabla de multiplicar, distancias por parejas, correlación. |
| 105–120 | **JAX** (si hay entorno), o pandas de preparación de datos (bloque opcional), o R opcional, y cierre. |

## Recursos

- Teoría: `01-fundamentos-python/01-teoria/05-numpy-avanzado.md`.
- Teoría broadcasting: `01-fundamentos-python/01-teoria/07-broadcasting-numpy.md`.
- Práctico: `01-fundamentos-python/02-ejemplos/09_numpy_avanzado.ipynb`.
- JAX: `01-fundamentos-python/01-teoria/08-guia-numpy-jax.md` y
  `01-fundamentos-python/02-ejemplos/08_introduccion_jax_comparativa.ipynb`.
- R opcional: `01-fundamentos-python/01-teoria/09-guia-r-complementario.md`.

## Comprobación del entorno

Antes de la clase:

- Confirmar que el notebook `09_numpy_avanzado.ipynb` está visible en
  Moodle si se trabaja desde ahí.
- Si está previsto JAX, comprobar `pixi run --environment ud1 jupyter lab` (o el
  entorno indicado) y que `import jax` funciona; si no, dejar JAX como demo o
  saltarlo.
- Preparar el tensor/generador `default_rng` para que los resultados de ejemplos
  salgan iguales en todos los equipos (usar la misma semilla).

## Criterio de salida

- El alumnado elige el `axis` correcto en una reducción.
- Puede filtrar con máscara booleana y usar `where`.
- Reproduce las aplicaciones de broadcasting (centrado, distancias, tabla).
- Se explica cuándo conviene JAX sobre NumPy (o queda como ampliación si no se
  dispone de entorno).

## Bloque opcional: pandas y preparación de datos (si sobra tiempo)

Si el grupo cierra NumPy/JAX con holgura y hay margen, se enlaza aquí un primer
vistazo a **pandas** como herramienta tabular que usa NumPy por debajo. No es
obligatorio impartirlo en esta clase: UD2 lo desarrolla por completo más adelante.
Su valor aquí es mostrar cómo NumPy es la base de `DataFrame`, cerrando el puente
hacia el tratamiento de datos.

Material ya existente en UD2 (revisado y suficiente, no hay que crearlo):

- `02-tratamiento-datos/01-teoria/01-pandas-introduccion.md`: qué es pandas,
  `Series`/`DataFrame`, motores NumPy/PyArrow, limpieza, `read_csv`, `groupby`,
  `merge`, formatos y mini-EDA.
- `02-tratamiento-datos/01-teoria/02-pandas-ejemplos-guia.md`: ejemplos
  frecuentes con DataFrame: filtrado, transformación de columnas, `fillna`/
  `dropna`, agregaciones, `pivot_table`, series temporales y exportación.
- (Opcional) `02-tratamiento-datos/01-teoria/05-preparacion-datos-ml.md`:
  orientación de preparación de datos hacia ML (imputación, codificación,
  escalado y partición), útil si se quiere anticipar el pipeline.

Actividad breve, solo si hay tiempo:

1. Crear un `DataFrame` pequeño en memoria (por ejemplo, ventas o notas).
2. Hacer `df.info()`, `df.head()`, `df.describe()`.
3. Filtrar filas por condición y crear una columna calculada con `assign`.
4. `df.groupby(...)["columna"].mean()` y un `pivot_table` sencillo.
5. Exportar a CSV en memoria o a Parquet si está disponible.

No entrar en UD2 en profundidad: es un enganche conceptual para que el alumnado
vea que el ecosistema numérico (NumPy) se apoya en pandas para datos tabulares.

## Cierre

- Ticket de salida: una aplicación de NumPy que le haya resultado útil y una
  duda que le quede.
- Si se saltó pandas o R, dejarlos explícitos como ampliación para más adelante;
  no forzar un bloque nuevo en una misma sesión si el grupo acaba de consolidar
  NumPy.
