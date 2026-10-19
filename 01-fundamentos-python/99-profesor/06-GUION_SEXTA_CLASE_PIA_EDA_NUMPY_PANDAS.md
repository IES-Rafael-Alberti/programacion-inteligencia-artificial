# Guion de la sexta clase de PIA — cierre con EDA NumPy y pandas

> **Documento interno del profesorado. Solo repositorio docente; no publicar en `main` del alumnado, GitHub Pages ni Moodle.**

**Fecha prevista:** martes 20 de octubre de 2026.

**Duración de referencia:** 3 horas, incluida una pausa de 10 minutos.

**Continuidad real comunicada por el profesor:** NumPy está prácticamente terminado. Ya se presentaron las Series, el DataFrame como conjunto de columnas/Series y el comienzo de la indexación en pandas. La sesión siguiente cierra NumPy con un ejemplo integrado de EDA y dedica el grueso del tiempo a pandas.

## 1. Decisión de alcance

- **NumPy:** un único caso de EDA, de unos 35 minutos; las funciones se recuperan al utilizarlas, sin repetir los notebooks avanzados completos.
- **Pandas, imprescindible:** retomar etiquetas frente a posiciones, seleccionar filas/columnas, filtrar con condiciones y crear columnas calculadas.
- **Pandas, si se alcanza la base:** ausentes, resúmenes y una agrupación sencilla sobre los mismos datos.
- **Consulta posterior:** álgebra lineal en UD3; JAX y ampliaciones de aleatoriedad/I/O mantienen su tratamiento anterior. No son nuevos objetivos de mañana.
- **Actividad de aula:** demostración guiada y mini-práctica de consolidación. No se abre una nueva entrega evaluable ni se asigna todo el banco de NumPy para esta sesión.

## 2. Material que conviene abrir antes de clase

Rutas relativas a la raíz del módulo:

| Uso | Ruta |
|---|---|
| Enunciados del EDA de empleados | `01-fundamentos-python/03-practicas/09_eda_numpy.md` |
| Cuaderno EDA existente, como referencia | `01-fundamentos-python/03-practicas/09_eda_numpy.ipynb` |
| Teoría de pandas | `02-tratamiento-datos/01-teoria/01-pandas-introduccion.md` |
| Ejemplos de consulta | `02-tratamiento-datos/01-teoria/02-pandas-ejemplos-guia.md` |
| Notebook principal para continuar pandas | `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb` |
| Refuerzo NumPy, fuera del recorrido principal | `01-fundamentos-python/03-practicas/15-ejercicios_numpy_completo.ipynb` |

Preparar un notebook de trabajo en blanco para ejecutar los bloques de este guion en orden. Así se mantiene el mismo dataset durante la transición. El notebook de fundamentos de pandas sirve después como recorrido y repertorio de ejemplos; su dataset de clientes es distinto del de empleados.

Antes de entrar, comprobar que el entorno habitual importa `numpy` y `pandas`, que el alumnado puede abrir los recursos y que se dispone de una copia local. No se necesitan descargas de datasets ni nuevas dependencias.

### Precauciones concretas con los cuadernos existentes

- En el EDA, `data` es un array NumPy homogéneo: **no tiene nombres de columnas**. El ejemplo de array estructurado `data2` es independiente. No usar `[x.dtype.names for x in data[0]]` para obtener nombres: devolverá `None`.
- `column_stack` promociona las columnas numéricas a un tipo común; distingue el significado de una variable (ID, categoría, medida) de su tipo físico almacenado.
- La generación con índices aleatorios repetidos puede insertar menos ausentes o atípicos de los previstos. Contar los realmente presentes; el ejemplo de abajo elige índices sin reemplazo.
- La tarea 6 antigua propone sustituir atípicos por el percentil 95: no afirmar que eso elimina necesariamente todos los casos según IQR. Mañana **se detectan e interpretan**; no se corrigen automáticamente.
- El cuaderno EDA contiene una celda final `%%bash` para convertir con Jupytext un fichero que no forma parte de la actividad. No ejecutarla en clase; usar el recorrido de este guion.
- En pandas, omitir la celda de inspección interna `pd.get_option("mode.data_manager")`: depende de la versión, está obsoleta en versiones recientes y no aporta al objetivo de hoy.
- En selección, explicar que `.loc[4]` significa **etiqueta 4**, no quinta fila. La coincidencia con posiciones en un índice por defecto puede ocultar el concepto.

## 3. Ritmo de 180 minutos

| Minutos | Bloque | Comprobación |
|---|---|---|
| 0–5 | Recuperar el avance real y presentar la pregunta del EDA. | El grupo sabe que NumPy queda como herramienta ya disponible. |
| 5–40 | EDA NumPy de empleados: estructura, rangos, ausentes, filtros, IQR y una conclusión. | Se conserva el original y se explica qué se ha observado. |
| 40–50 | Pasar **los mismos datos** a un DataFrame. | Comparar selección por número de columna con selección por nombre. |
| 50–65 | Recuperación breve de Series/DataFrame e índice; anticipar resultados antes de ejecutar. | Distinguir Series de DataFrame de una columna. |
| 65–95 | Selección por etiquetas/posiciones: `loc`, `iloc`, listas y cortes. | Resolver una consulta después de cambiar el orden de las filas. |
| 95–105 | Pausa. | — |
| 105–130 | Máscaras compuestas, ordenación y columnas calculadas; asignación con `loc`. | Formular una pregunta y expresar el filtro sin un bucle. |
| 130–150 | Ausentes y comparación de resúmenes; `groupby` sencillo si la selección está asentada. | Distinguir dato original, dato imputado y resumen. |
| 150–175 | Mini-práctica por parejas y puesta en común. | Explicar el resultado y justificar etiquetas/posiciones. |
| 175–180 | Ticket de salida y anotar el punto de continuidad. | Tres operaciones básicas y una duda identificada. |

**Límite de tiempo:** al minuto 40 se cierra el ejemplo NumPy aunque queden tareas del EDA antiguo. Lo restante queda para práctica posterior; el objetivo de mañana es avanzar de verdad en pandas.

## 4. EDA NumPy: una pregunta y un recorrido breve

**Pregunta:** ¿cómo se distribuyen los salarios y la satisfacción, qué registros requieren revisión y cómo describimos el conjunto sin confundir asociación con causalidad?

Usar el caso de empleados de la práctica existente. El generador siguiente es una variante reproducible; no tiene por qué reproducir las cifras del cuaderno antiguo, que usa la API global de aleatoriedad.

### A. Crear e inspeccionar (5–15 min)

```python
import numpy as np

rng = np.random.default_rng(42)
n = 1000
columnas = ["id", "edad", "salario", "experiencia", "horas", "nivel", "satisfaccion"]
edad = rng.integers(18, 65, size=n)
salario = rng.normal(2500, 800, size=n)
experiencia = np.clip(edad - rng.integers(18, 30, size=n), 0, None)
horas = rng.normal(40, 5, size=n)
nivel = rng.integers(0, 5, size=n)
satisfaccion = rng.normal(7, 2, size=n)
salario[rng.choice(n, 10, replace=False)] *= 4
satisfaccion[rng.choice(n, 15, replace=False)] = np.nan
data = np.column_stack([
    np.arange(1, n + 1), edad, salario, experiencia, horas, nivel, satisfaccion
])
original = data.copy()
print(columnas)
print(data.shape, data.dtype)
print(data[:5])
```

Preguntar antes de ejecutar: «¿Qué `dtype` tendrán los IDs dentro de `data`? ¿Dónde están los nombres?». Los nombres viven en una lista separada; el array no sabe que la columna 2 es el salario.

### B. Resumir y detectar problemas (15–25 min)

```python
print("Ausentes por columna:", np.isnan(data).sum(axis=0))
print("Mínimos:", np.nanmin(data, axis=0))
print("Máximos:", np.nanmax(data, axis=0))
print("Salario: media y mediana:", data[:, 2].mean(), np.median(data[:, 2]))
print("Satisfacción media válida:", np.nanmean(data[:, 6]))
fuera_escala = (data[:, 6] < 0) | (data[:, 6] > 10)
print("Satisfacción fuera de 0–10:", fuera_escala.sum())
```

La normal puede producir salarios negativos o satisfacción fuera de su escala declarada. Se señala como problema del dato sintético, sin ocultarlo con un recorte automático. No interpretar medias de IDs o categorías como medidas relevantes aunque NumPy pueda calcularlas.

### C. Filtrar, marcar atípicos y cerrar (25–40 min)

```python
mascara = (data[:, 4] > 45) & (data[:, 3] > 10)
print("IDs con más de 45 h y más de 10 años de experiencia:",
      data[mascara, 0].astype(np.int64)[:10])
print("Porcentaje con nivel educativo >= 3:", 100 * (data[:, 5] >= 3).mean())
q1, q3 = np.percentile(data[:, 2], [25, 75])
iqr = q3 - q1
atipicos = (data[:, 2] < q1 - 1.5 * iqr) | (data[:, 2] > q3 + 1.5 * iqr)
print("Salarios para revisar según IQR:", atipicos.sum())

# Ejemplo didáctico de imputación en una copia; se preserva el original.
limpios = data.copy()
faltan = np.isnan(limpios[:, 6])
limpios[faltan, 6] = np.nanmean(limpios[:, 6])
assert np.isnan(data[:, 6]).sum() == 15
assert not np.isnan(limpios[:, 6]).any()
assert np.array_equal(data, original, equal_nan=True)
```

Pedir dos conclusiones y una limitación: distribución sesgada por extremos, ausentes/valores fuera de escala y datos sintéticos. Un valor marcado por IQR no es necesariamente un error. Imputar con la media es una decisión didáctica que altera la distribución; en un flujo ML los parámetros se aprenderían solo con entrenamiento.

Si hay tiempo, mencionar `np.corrcoef(data[:, 2], data[:, 3])[0, 1]`: el generador no define una relación salarial causal con la experiencia. No abrir un bloque nuevo de correlación.

## 5. Puente: los mismos empleados, ahora con etiquetas (40–65 min)

```python
import pandas as pd

df = pd.DataFrame(original, columns=columnas)
df = df.astype({"id": "int64", "edad": "int64", "experiencia": "int64", "nivel": "int64"})
df = df.set_index("id")
print(df.head())
df.info()
print(type(df["salario"]), type(df[["salario"]]))
print(df["salario"].name, df["salario"].index[:3])
print(df[["salario", "satisfaccion"]].describe())
```

Recuperar lo ya visto en cinco minutos: cada columna es una Series; el índice aporta etiquetas. No repetir la introducción entera. El índice de IDs empieza en 1, de modo que la primera posición (`0`) y la primera etiqueta (`1`) ya no coinciden.

Mostrar el paso de `data[:, 2]` a `df["salario"]`. Cada columna puede tener su propio tipo; una Series también puede usar tipos de extensión de pandas, no necesariamente un `ndarray` convencional.

## 6. Indexación con intención (65–95 min)

```python
print(df.loc[1, ["edad", "salario"]])   # empleado con etiqueta 1
print(df.iloc[0, :2])                    # primera fila, dos primeras columnas
print(df.loc[1:3, ["edad", "salario"]])
print(df.iloc[0:3, :2])

ordenado = df.sort_values("salario", ascending=False)
print("Primer ID tras ordenar:", ordenado.index[0])
print("Primera fila:", ordenado.iloc[0])
print("Empleado 1:", ordenado.loc[1])
```

Preguntar «¿Sigue siendo el empleado 1 la primera fila?». Ordenar cambia las posiciones, pero conserva las etiquetas. `.loc` incluye ambos extremos del corte por etiquetas cuando procede; `.iloc` usa la convención de Python y excluye el extremo final. Practicar los cortes por etiqueta en el índice original ordenado, no en el DataFrame ordenado por salarios.

Microejercicios:

1. Empleados con IDs 2, 8 y 15: edad y horas.
2. Primeras cinco filas: dos primeras columnas.
3. Seleccionar solo salario como Series y como DataFrame, y explicar la diferencia.

## 7. Filtrar y transformar (105–130 min)

```python
seleccion = (df["horas"] > 45) & (df["experiencia"] > 10)
resultado = df.loc[seleccion, ["edad", "salario", "horas"]]
print(resultado.sort_values("salario", ascending=False).head())
df["salario_anual"] = df["salario"] * 12
df["salario_revisar"] = atipicos   # mismo orden que el array original
df["satisfaccion_invalida"] = (df["satisfaccion"] < 0) | (df["satisfaccion"] > 10)
df.loc[df["satisfaccion_invalida"], "satisfaccion"] = np.nan
```

La marca IQR se asigna antes de reordenar `df`; los arrays se asignan por posición. Una Series se alinea por índice: no son mecanismos intercambiables sin mirar el orden. Emplear `loc` para asignar con máscara; evitar `df[mascara]["columna"] = ...`.

No introducir `apply` para una operación que se expresa directamente con columnas. Mostrar la equivalencia del filtro con el del EDA NumPy.

## 8. Ausentes y primer resumen por grupo (130–150 min)

```python
print("Ausentes antes de imputar:", df.isna().sum())
df_limpio = df.copy()
df_limpio["satisfaccion"] = df_limpio["satisfaccion"].fillna(
    df_limpio["satisfaccion"].mean()
)
print(df_limpio[["salario", "satisfaccion"]].describe())
resumen = df.groupby("nivel").agg(
    empleados=("salario", "size"),
    salario_medio=("salario", "mean"),
    salario_mediano=("salario", "median"),
)
print(resumen)
```

Mostrar el conteo antes de imputar: incluye los 15 ausentes originales y los valores que se acaban de marcar fuera de escala. `describe()` y la media omiten ausentes, pero eso no equivale a que estén imputados. Comparar media/mediana por nivel sin atribuir diferencias a una causalidad que el generador no representa.

Si aún cuesta seleccionar, sustituir `groupby` por más práctica de máscaras. Exportación, joins, pivotes y visualización extensa quedan para las sesiones siguientes de UD2.

## 9. Mini-práctica por parejas (150–175 min)

Sobre el DataFrame de empleados que ya está en memoria, en celdas nuevas:

1. Seleccionar empleados de 30 a 50 años (ambos incluidos) y mostrar edad, salario y horas.
2. Ordenar ese resultado por salario y obtener sus cinco primeros registros. Explicar por qué se usa `head` o `iloc`, no `loc[:5]`.
3. Crear una columna booleana `jornada_larga` con horas mayores de 45.
4. Contar ausentes en satisfacción **antes** de imputar. Explicar qué información cambia al rellenarlos.
5. **Ampliación:** salario medio y mediano por nivel educativo.

Dedicar unos 15 minutos a resolver y 10 a comparar dos soluciones. Para la corrección, comprobar formas, columnas e índices y pedir una interpretación, no solo leer código.

## 10. Cierre y ajuste al ritmo

**Ticket de salida:** escribir una selección por etiqueta, una por posición y un filtro compuesto; explicar en una frase por qué pandas facilita el EDA tabular respecto a columnas numeradas de NumPy.

**Si falta tiempo:** cerrar NumPy en el límite fijado; mantener el puente con los mismos datos y priorizar selección/filtros. Dejar agrupaciones y la ampliación de la mini-práctica para la siguiente sesión.

**Si sobra tiempo:** repetir un resumen del EDA con pandas y comparar legibilidad. No abrir JAX, otra biblioteca ni una práctica larga nueva.

Al terminar, registrar qué se llegó a impartir (indexación, filtros, transformaciones, ausentes, agrupaciones) y qué microejercicio resultó difícil. El guion previsto no acredita que se hayan impartido todos los bloques.

**Siguiente paso recomendado:** continuar UD2 desde el último bloque real de pandas; trabajar carga de datos y limpieza con más detalle antes del EDA visual.

## Referencias para el profesor

- [Selección e indexación en pandas](https://pandas.pydata.org/docs/user_guide/indexing.html).
- [Asignación y Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html).
