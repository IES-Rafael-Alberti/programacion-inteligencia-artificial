# Guion de la quinta clase de PIA — retomar NumPy avanzado y puente a pandas

> **Documento interno del profesorado. No publicar en GitHub Pages ni en Moodle.**

**Duración:** 3 horas (180 min).
**Punto de continuidad:** en la cuarta clase se saltó la parte final de NumPy
(ufuncs/estadística y álgebra lineal) por falta de tiempo y se pasó antes de
tiempo a un primer vistazo de pandas. Hoy se retoma NumPy donde quedó, se cierra
con los bloques que de verdad sostienen el EDA, y se hace una transición **suave**
a pandas (Series, DataFrame construido por Series y arranque de indexación).

## Objetivos

Al terminar, el alumnado podrá:

- cerrar NumPy esencial: agregaciones y ufuncs, selección por condición,
  estadística descriptiva y generación aleatoria reproducible;
- aplicar esa base en un **análisis exploratorio (EDA) con NumPy** ya preparado
  (`09_eda_numpy`) sin depender de pandas;
- reconocer **Series** y **DataFrame** como la evolución natural de un `ndarray`
  con etiquetas, y que un `DataFrame` se construye a partir de Series;
- iniciar la **indexación** de pandas (por etiqueta y por posición) sin entrar
  aún en `loc`/`iloc` avanzados ni en transformaciones completas de UD2.

## Decisión de contenido (nuevos documentos avanzados 10-13)

| Documento | Tratamiento en clase | Motivo |
|---|---|---|
| `13-numpy-ufuncs-estadistica-avanzado.md` (+ nb 14) | **Esencial, se imparte** | reduce/accumulate, clip, percentiles, corrcoef, unique, select. Sostienen el EDA. |
| `11-numpy-aleatoriedad-avanzado.md` (+ nb 12) | **Esencial en parte**, resto consulta | default_rng, distribuciones, choice/shuffle, semilla. La parte de distribuciones específicas se deja como consulta. |
| `12-numpy-io-archivos-avanzado.md` (+ nb 13) | **Apuntes breves** | save/load, savetxt/loadtxt. Se menciona y se remite al material; el grueso se usa en UD2/UD3. |
| `10-numpy-algebra-lineal-avanzado.md` (+ nb 11) | **NO en clase: consulta** | norm/@/solve/eig/svd se activan en UD3 (kNN, clustering, PCA). Solo mención y enlace. |

> La cuarta clase dejó pendiente álgebra lineal y JAX. **No** se reintroduce
> ahora como bloque: el álgebra lineal se retoma con contexto en UD3, y JAX queda
> como ampliación (entorno `pia-ud1`) para quien quiera profundizar, sin peso en
> esta sesión.

## Estructura y ritmo

| Tiempo | Actividad | Resultado esperado |
|---|---:|---|
| 0–25 | Reencuentro y **repaso** de NumPy esencial: `ndarray`, `shape`/`axes`, indexado, máscaras, `where`, broadcasting, `keepdims`. Pedir dudas y recuperar dónde se quedó el bloque de NumPy avanzado. | El grupo reconecta con los conceptos que ya vio y identifica qué le falta cerrar. |
| 25–55 | **Ufuncs y estadística avanzada (13, esencial)**: `add.reduce`/`accumulate`, `round`/`clip`, `percentile`, `unique`, `corrcoef`, clasificación con `select`. Notebook guiado 14. | Elige el eje y la agregación correcta; resume con percentiles, acota con `clip` y relaciona con `corrcoef`. |
| 55–80 | **Aleatoriedad avanzada (11, esencial en parte)**: `default_rng`, `normal`/`uniform`/`integers`/`binomial`, `choice` con `p`, `shuffle`/`permutation`, semilla reproducible, split train/test. Notebook guiado 12. | Crea datos sintéticos reproducibles y divide datos; distingue `shuffle` (in-place) de `permutation` (copia). |
| 80–90 | **Álgebra lineal (10)**: solo **mención** (`@`, `norm`, `solve` existen; se usarán en UD3). Enlace al material de consulta. Mencionar JAX como ampliación. | Sabe que existe y dónde retomarlo; no gasta tiempo ahora. |
| 90–115 | **EDA con NumPy** — repaso guiado: `09_eda_numpy.md/.ipynb`. Recorrer las tareas 1–10 (descripción, rangos, filtrado, `nan`, outliers/IQR, normalización, agrupaciones simples, correlación, estadísticas). | Produce un resumen de datos con NumPy puro y conecta cada paso con la función NumPy que lo resuelve. |
| 115–140 | **Ejercicios NumPy agrupados**: `10-ejercicios_numpy.md/.ipynb`. Seleccionar ~6 que refuercen lo visto: one-hot (9), media móvil (10), simulación de dados (13), filtrar filas (12), función a trozos con `where` (16), distancias euclídeas (18). | Aplica NumPy a problemas variados sin depender de una librería superior. |
| 140–175 | **Transición suave a pandas**: Series, DataFrame construido por Series, y arranque de indexación (por etiqueta y posición). Notebook `01_pandas_fundamentos.ipynb` (secciones 1–3). | Entiende Series = `ndarray` + índice; DataFrame = colección de Series; inicia selección básica sin `loc`/`iloc` profundos. |
| 175–180 | Ticket de salida y continuidad | Cada estudiante resuelve una duda y afirma qué concepto de NumPy le falta reforzar para abordar pandas. |

## Recursos

- Teoría esencial:
  - `01-fundamentos-python/01-teoria/13-numpy-ufuncs-estadistica-avanzado.md`
  - `01-fundamentos-python/01-teoria/11-numpy-aleatoriedad-avanzado.md`
  - `01-fundamentos-python/01-teoria/12-numpy-io-archivos-avanzado.md` (apunte)
  - `01-fundamentos-python/01-teoria/10-numpy-algebra-lineal-avanzado.md` (consulta/UD3)
- Notebooks guiados:
  - `01-fundamentos-python/02-ejemplos/14_numpy_ufuncs_estadistica_avanzado.ipynb`
  - `01-fundamentos-python/02-ejemplos/12_numpy_aleatoriedad_avanzado.ipynb`
  - `01-fundamentos-python/02-ejemplos/11_numpy_algebra_lineal_avanzado.ipynb` (consulta)
- EDA y ejercicios:
  - `01-fundamentos-python/03-practicas/09_eda_numpy.md` y `09_eda_numpy.ipynb`
  - `01-fundamentos-python/03-practicas/10-ejercicios_numpy.md` y `10-ejercicios_numpy.ipynb`
- Pandas (transición):
  - `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb` (secciones 1–3)
  - `02-tratamiento-datos/01-teoria/01-pandas-introduccion.md` (tabla Series/DataFrame, sección de Series y DataFrame)

## Comprobación del entorno

- Confirmar que los notebooks de NumPy avanzado y el EDA están visibles en Moodle
  (o indicar cómo abrirlos desde el repositorio local).
- El entorno `default` de Pixi basta para NumPy y pandas (no requiere JAX hoy).
- Usar la misma semilla (`default_rng`) en los ejemplos para que los resultados
  salgan iguales en todos los equipos.
- No instalar dependencias durante la sesión.

## Bloque de transición a pandas (140–175)

Mensaje central: *un `ndarray` es potente pero anónimo; pandas le pone etiquetas a
filas y columnas.*

1. **Series** = `ndarray` (los datos) + `index` (las etiquetas) + `name`.
   Mostrar `pd.Series([...], index=[...], name="..."`. Comparar con un array: mismo
   bucle de fondo, pero con índices etiquetados.
2. **DataFrame construido por Series**: pasar un `dict` de Series (o de listas)
   a `pd.DataFrame` y observar que cada columna es una Series con su propio
   `name`. Señalar que, por debajo, puede apoyarse en NumPy (columnas homogéneas).
3. **Arranque de indexación** (sin `loc`/`iloc` en profundidad, pero presentarlos):
   - selección por etiqueta con `df["columna"]` (devuelve una Series);
   - selección de filas con `.loc[etiqueta]` y posición con `.iloc[pos]`;
   - observar `df.index` y `df.columns`.
4. No entrar en `set_index`, `groupby`, `merge`, `pivot` ni limpieza: pertenecen a
   UD2 y se retomarán ahí con calma.

Actividad breve del bloque: cargar un DataFrame pequeño en memoria (por ejemplo,
tres Series: nombre, nota, horas) y hacer `df.info()`, `df.head()`, `df["columna"]`
y dos `.loc`/`.iloc` sencillos, para que la transición termine con práctica
realizada, no solo teoría.

## Criterio de salida

- Elige el `axis` correcto en una reducción y resume con `percentile`/`unique`.
- Crea datos reproducibles con `default_rng` y divide en train/test con semilla.
- Completa (al menos parcialmente) el EDA con NumPy sin pandas.
- Explica Series como `ndarray` con índice y DataFrame como conjunto de Series.
- Hace una selección básica de pandas por etiqueta/posición (`loc`/`iloc` simples).

## Si el tiempo se reduce

- Recorta la aleatoriedad avanzada a `default_rng`, `choice` y split train/test
  (déjalo claro y remite el resto al notebook 12).
- En el EDA, prioriza las tareas 1–5 y 8–10 (descripción, filtrado, nan, outliers,
  normalización, estadísticas); deja 6–7 como refuerzo autónomo.
- Reduce los ejercicios a 3 (one-hot, simulación de dados, función a trozos).
- No sacrifiques la transición a pandas completa si se ha consolidado NumPy:
  es el enganche hacia la siguiente unidad.

## Si el grupo avanza con soltura

- Entra un poco más en `loc`/`iloc` y en crear columnas calculadas con `assign`.
- Muestra `groupby(...)[...].mean()` como anticipo motivador de UD2.
- Sugiere completar los ejercicios 4, 7 y 17 del banco de NumPy como tarea.

## Cierre

- Ticket de salida: una función o técnica de NumPy que le haya resultado útil hoy
  y una duda que le quede antes de abordar pandas con profundidad en UD2.
- Registrar el avance real en `ESTADO_ACTUAL_Y_PENDIENTES.md` y ajustar el paquete
  Moodle si procede.
