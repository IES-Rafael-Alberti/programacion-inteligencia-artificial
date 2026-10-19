# Guion de la sexta clase de PIA — R, comparativa, EDA NumPy y pandas

> **Documento interno del profesorado. Solo repositorio docente; no publicar en `main` del alumnado, GitHub Pages ni Moodle.**

**Fecha prevista:** martes 20 de octubre de 2026.

**Duración de referencia:** 3 horas, incluida una pausa de 10 minutos.

**Continuidad real comunicada por el profesor:** NumPy está prácticamente terminado. Ya se presentaron las Series, el DataFrame como conjunto de columnas/Series y el comienzo de la indexación en pandas. Falta la introducción breve a R. Mañana se empieza por R y la actividad comparativa que el profesor quiere hacer en clase; después, EDA NumPy de cierre y continuación de pandas.

## 1. Decisión de alcance

- **R:** 15 minutos de R base (vectores, indexación desde 1, operaciones, `data.frame` y resumen), sin instalar paquetes ni abrir ahora un curso de R.
- **Comparativa de lenguajes y formatos:** 35 minutos en clase, usando el enunciado entregable y su plantilla. El breve R previo proporciona una referencia concreta para comparar con Python.
- **NumPy:** un único caso de EDA, de unos 30 minutos; las funciones se recuperan al utilizarlas, sin repetir los notebooks avanzados completos.
- **Pandas, imprescindible:** retomar etiquetas frente a posiciones, seleccionar filas/columnas, filtrar con condiciones y crear columnas calculadas.
- **Pandas, si se alcanza la base:** ausentes y resúmenes sobre los mismos datos. La agrupación es ampliación, no compromiso de mañana.
- **Consulta posterior:** álgebra lineal en UD3; JAX y ampliaciones de aleatoriedad/I/O mantienen su tratamiento anterior. No son nuevos objetivos de mañana.
- **Actividad entregable:** la comparativa ya existente, ahora preparada para el alumnado. El resto es demostración y mini-práctica; no se exige completar todo el banco NumPy ni todos los cuestionarios en clase.
- **Decisión para después:** cuando se vean gráficas en Python, hacer ejemplos equivalentes en R y comparar código y resultados con los mismos datos. Recuperar esa decisión al preparar visualización en UD2; no añadir gráficas al bloque breve de mañana.

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
| R base de referencia | `01-fundamentos-python/01-teoria/09-guia-r-complementario.md` |
| Notebook R existente | `01-fundamentos-python/02-ejemplos/06_introduccion_R_fundamentos.ipynb` |
| Enunciado entregable de la comparativa | `01-fundamentos-python/04-evaluacion/comparativa-lenguajes-formatos-ia.md` |

Preparar un notebook de trabajo en blanco para ejecutar los bloques de este guion en orden. Así se mantiene el mismo dataset durante la transición. El notebook de fundamentos de pandas sirve después como recorrido y repertorio de ejemplos; su dataset de clientes es distinto del de empleados.

Antes de entrar, comprobar que el entorno habitual importa `numpy` y `pandas`, que el alumnado puede abrir los recursos y que se dispone de una copia local. Preparar también R en el equipo del profesor: consola R, RStudio o kernel R ya instalado. Si los equipos del alumnado no tienen R listo, hacer demostración y lectura de resultados; no dedicar la clase a instalarlo. No se necesitan paquetes R adicionales ni descargas de datasets.

### Pendiente para mañana antes de clase: Moodle

- **Subir/importar los tres GIFT NumPy actualizados** desde `01-fundamentos-python/04-evaluacion/`: `cuestionario-numpy.gift` (25), `cuestionario-eda-numpy.gift` (20) y `cuestionario-numpy-completo.gift` (18). Solo el docente importa las fuentes; no adjuntarlas como archivos visibles al alumnado.
- En el banco completo, conservar la categoría separada **Álgebra consulta UD3** (preguntas 13–15) fuera del repaso obligatorio. El núcleo de código contiene las otras 15 preguntas.
- Comprobar recuentos, categorías, respuestas, retroalimentación y acceso con rol de estudiante. La importación no equivale a crear/publicar un cuestionario: añadir las preguntas al recurso Moodle correspondiente, ajustar orden/mezcla y visibilidad. Al reimportar, comprobar que no se duplican preguntas anteriores.
- Activar el bloque EDA después de verlo; no es necesario resolver los tres cuestionarios enteros en clase mañana. Configurar la retroalimentación según el uso de práctica elegido.
- Subir el PDF/enunciado de la **comparativa de lenguajes y formatos** y crear o habilitar su tarea de entrega. Revisar en pantalla el plazo y los formatos aceptados antes de comenzar la actividad.
- La preparación local del paquete no acredita la importación ni la publicación en Moodle.

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
| 0–5 | Explicar objetivos, recursos Moodle y entrega de la comparativa. | El grupo conoce el producto que entregará. |
| 5–20 | R base: vector, filtro, resumen y `data.frame`; contraste breve con Python. | Dispone de un ejemplo real de R para la comparación. |
| 20–55 | Comparativa de lenguajes y formatos: tabla, decisión y marcado. | Trabaja y entrega la actividad prevista en clase. |
| 55–85 | EDA NumPy de empleados: estructura, ausentes, filtros, IQR y conclusión. | Se conserva el original y se interpreta lo observado. |
| 85–100 | Pasar **los mismos datos** a un DataFrame; recuperar Series/índice. | Comparar selección por número de columna con selección por nombre. |
| 100–110 | Pausa. | — |
| 110–140 | `loc`/`iloc`, listas, cortes y filtros compuestos. | Distinguir etiquetas/posiciones incluso tras ordenar filas. |
| 140–160 | Ordenación, columnas calculadas y asignación con `loc`; ausentes si hay margen. | Formular una pregunta y expresar la transformación sin un bucle. |
| 160–175 | Mini-práctica breve y puesta en común. | Explicar una selección y una transformación. |
| 175–180 | Ticket de salida y anotar el punto de continuidad. | Tres operaciones básicas y una duda identificada. |

**Límite de tiempo:** cerrar R en el minuto 20 y el EDA NumPy en el 85. La comparativa es el entregable de clase. Si se retrasa, reducir la ampliación de pandas (ausentes y agrupación), sin tratar de impartir todo al final.

## Bloque inicial: R y comparativa (5–55 min)

### R base en 15 minutos

Usar las secciones de variables y estructuras del notebook R existente, sin recorrer bucles y funciones completas. Mostrar este pequeño ejemplo y preguntar qué cambia respecto a Python:

```r
notas <- c(6, 8, NA, 9)
print(notas[1])
print(notas[!is.na(notas) & notas >= 7])
print(mean(notas, na.rm = TRUE))
alumnos <- data.frame(
  nombre = c("Ana", "Luis", "Marta", "Pablo"),
  nota = notas
)
print(alumnos)
print(summary(alumnos))
```

Equivalente breve, aprovechando NumPy ya conocido:

```python
import numpy as np
notas = np.array([6., 8., np.nan, 9.])
print(notas[0])
print(notas[~np.isnan(notas) & (notas >= 7)])
print(np.nanmean(notas))
```

Cinco ideas: asignación `<-`, vector con `c`, índice inicial 1, `NA` y funciones de resumen; un `data.frame` organiza columnas. Es una primera lectura/ejecución, no un dominio de R. No afirmar que R sea siempre mejor para estadística ni que Python sea siempre más rápido: depende de herramientas, tarea y contexto.

### Comparativa entregable en 35 minutos

Abrir el enunciado público **sin observación docente**. Mantiene la ruta habitual para no multiplicar versiones. Reparto sugerido: 5 minutos para interpretar el caso, 18 para la tabla, 8 para conclusión y marcado, 4 para revisar y entregar. Responder consultas durante el trabajo; la puesta en común puede ser breve al retomar.

Explicar antes de empezar que se comparan tecnologías con funciones distintas: lenguajes, intercambio, configuración, documentación y marcado. Java/JavaScript se comparan por su papel en la aplicación, sin exigir programarlos hoy. No pedir tidyverse, dplyr, RMarkdown ni gráficos todavía.

**Observación docente, solo aquí:** al retomar visualización en UD2, volver a esta comparativa con gráficos Python/R equivalentes. Puede revisarse entonces la elección inicial con más evidencias.

## 4. EDA NumPy: una pregunta y un recorrido breve

**Pregunta:** ¿cómo se distribuyen los salarios y la satisfacción, qué registros requieren revisión y cómo describimos el conjunto sin confundir asociación con causalidad?

Usar el caso de empleados de la práctica existente. El generador siguiente es una variante reproducible; no tiene por qué reproducir las cifras del cuaderno antiguo, que usa la API global de aleatoriedad.

### A. Crear e inspeccionar (55–65 min)

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

### B. Resumir y detectar problemas (65–75 min)

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

### C. Filtrar, marcar atípicos y cerrar (75–85 min)

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

## 5. Puente: los mismos empleados, ahora con etiquetas (85–100 min)

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

## 6. Indexación con intención (110–140 min)

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

## 7. Filtrar y transformar (140–160 min)

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

## 8. Ampliación si queda margen: ausentes y resumen por grupo

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

Este bloque no tiene un tramo obligatorio en el nuevo reparto: usarlo si el grupo avanza con soltura. Si cuesta seleccionar, continuar con máscaras. Exportación, joins, pivotes, agrupaciones en profundidad y visualización quedan para las sesiones siguientes de UD2. En visualización se compararán ejemplos Python/R con los mismos datos.

## 9. Mini-práctica por parejas (160–175 min)

Sobre el DataFrame de empleados que ya está en memoria, en celdas nuevas:

1. Seleccionar empleados de 30 a 50 años (ambos incluidos) y mostrar edad, salario y horas.
2. Ordenar ese resultado por salario y obtener sus cinco primeros registros. Explicar por qué se usa `head` o `iloc`, no `loc[:5]`.
3. Crear una columna booleana `jornada_larga` con horas mayores de 45.
4. **Si se vio el bloque de ausentes:** contarlos antes de imputar y explicar qué información cambia al rellenarlos.
5. **Ampliación:** salario medio y mediano por nivel educativo.

Dedicar 10 minutos a las tres primeras consultas y 5 a comparar soluciones. Los apartados 4–5 son ampliación. Para la corrección, comprobar formas, columnas e índices y pedir una interpretación, no solo leer código.

## 10. Cierre y ajuste al ritmo

**Ticket de salida:** escribir una selección por etiqueta, una por posición y un filtro compuesto; explicar en una frase por qué pandas facilita el EDA tabular respecto a columnas numeradas de NumPy.

**Si falta tiempo:** cerrar NumPy en el límite fijado; mantener el puente con los mismos datos y priorizar selección/filtros. Dejar agrupaciones y la ampliación de la mini-práctica para la siguiente sesión.

**Si sobra tiempo:** repetir un resumen del EDA con pandas y comparar legibilidad. No abrir JAX ni una práctica larga nueva. R ya tuvo su presentación inicial; los gráficos comparados quedan programados para visualización.

Al terminar, registrar la realización/entrega de la comparativa y qué se llegó a impartir de R, indexación, filtros, transformaciones, ausentes y agrupaciones. El guion previsto no acredita que se hayan impartido todos los bloques.

**Siguiente paso recomendado:** continuar UD2 desde el último bloque real de pandas; trabajar carga de datos y limpieza con más detalle antes del EDA visual.

## Referencias para el profesor

- [Selección e indexación en pandas](https://pandas.pydata.org/docs/user_guide/indexing.html).
- [Asignación y Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html).
