# Guion de la octava clase de PIA — pandas desde cero y comparación final con R

> **Documento interno del profesorado. Solo repositorio docente; no publicar en `main` del alumnado, GitHub Pages ni Moodle.**

**Duración de referencia:** 3 horas (180 min).

**Continuidad real de la séptima clase (2 h):** estaba planteada con arranque de R (local o Colab), R base breve, la comparativa entregable y un repaso inicial de pandas (Series, DataFrame e inicio de indexación). **Antes de empezar, confirmar el punto real alcanzado** y ajustar:

- La comparativa **ya está encargada al alumnado y en curso**: hoy **no se reabre ni se le dedica tiempo de clase**; se recoge y corrige después desde `99-profesor/00-entregas-y-correcciones/`.
- Si R **no llegó a ejecutarse**, el bloque final de comparación con R se hace como **demostración proyectada** (o Colab), sin dedicar la clase a instalaciones.
- Si pandas **solo se vio hasta Series/DataFrame**, hoy se empieza de cero igualmente: la primera media hora reconstruye esa base y el resto avanza.

Pandas conserva solo lo ya presentado (Series, DataFrame e inicio de indexación). Por eso **se empieza de cero**, sin dar por sabido lo anterior.

## 1. Decisión de alcance: R al final, no al principio

- **Pandas es el contenido nuevo y ocupa el grueso de la clase (unas dos horas).** Necesita la atención fresca del arranque; no conviene gastar los primeros minutos en un recordatorio de R que aún no tiene con qué compararse.
- **R se acaba de ver.** Un repaso aislado al principio se percibe como «otra clase de R» y rompe el hilo hacia pandas.
- **La comparación tiene más sentido al final**, cuando el alumnado ya ha hecho filtros, columnas derivadas y `groupby` en pandas: ahí el mismo problema resuelto en R y en pandas se lee de verdad. Además prepara la decisión ya tomada de comparar gráficas Python/R cuando llegue la visualización de UD2.
- **Formato del bloque final:** comparación **lado a lado sobre los mismos datos y las mismas operaciones** (filtro, columna nueva, resumen por grupo), en R base (sin tidyverse) y en pandas. No es una clase nueva de R.
- **Si el grupo llega sin R resuelto:** el bloque final se hace con **demostración proyectada** desde el equipo del profesor o con **Colab**; no se invierte tiempo en instalaciones.

## 1b. Método de la sesión: notebook en directo con predicción antes de ejecutar (vigente)

- Se mantiene el patrón ya acordado: 1) formular la pregunta; 2) mostrar/rellenar la celda; 3) **chequeo de predicción** («¿qué salida esperas aquí?») antes de ejecutar; 4) ejecutar y comparar lo esperado con lo real; 5) interpretar en una frase.
- Cada alumno/equipo ejecuta **la misma celda a la vez** y **no se avanza hasta que la mayoría salga**.
- La teoría va dentro del notebook como **pequeños pasos ejecutables**, no como discurso previo.
- Refuerzo en la recámara: **celdas vacías** que el alumnado completa (patrón de `16-eda_numpy_edificios.ipynb`) si el grupo se dispersa.

## 2. Material que conviene abrir antes de clase

Rutas relativas a la raíz del módulo:

| Uso | Ruta |
|---|---|
| Teoría de pandas (repaso del profesor) | `02-tratamiento-datos/01-teoria/01-pandas-introduccion.md` |
| Chuleta de pandas | `02-tratamiento-datos/01-teoria/03-pandas-chuleta.md` |
| Notebook principal de pandas | `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb` |
| Dataset de empleados (continuidad del EDA) | `01-fundamentos-python/03-practicas/09_eda_numpy.md` / `09_eda_numpy.ipynb` |
| Guía de R (solo para el bloque final) | `01-fundamentos-python/01-teoria/09-guia-r-complementario.md` |
| Notebook R (bloque final, opcional) | `01-fundamentos-python/02-ejemplos/06_introduccion_R_fundamentos.ipynb` |
| Soluciones docentes de pandas | `02-tratamiento-datos/99-profesor/01_pandas_fundamentos_SOLUCIONES.ipynb` |

Comprobar antes de entrar: que el entorno habitual importa `numpy` y `pandas`; que `pyarrow` está disponible si se enseña Parquet (si no, quedarse en CSV); y que el portátil del profesor puede proyectar el notebook R o abrir Colab.

### Precauciones concretas

- **No abrir** la celda interna `pd.get_option("mode.data_manager")` del notebook 01: depende de la versión y está obsoleta.
- El notebook `01_pandas_fundamentos.ipynb` usa un dataset de **clientes**; la clase usará el de **empleados** para enlazar con el EDA de NumPy. El de clientes queda como repertorio y para la práctica.
- No adelantar visualización, joins ni `pivot_table` avanzado salvo el `pivot_table` mínimo de recuento si sobra tiempo.
- En R, ceñirse a **R base** (`data.frame`, `$`, `aggregate`, `summary`); sin `dplyr` ni tidyverse.
- No afirmar que R sea siempre mejor para estadística ni que pandas sea siempre más rápido: depende de tarea, datos y herramientas.
- Si el grupo llega sin la comparativa entregada, no bloquear la clase: recordar la entrega en Moodle y seguir.

## 3. Ritmo de 180 minutos

| Minutos | Bloque | Comprobación |
|---|---|---|
| 0–10 | Arranque y objetivos; comprobar entorno (`import pandas`) y recuperar qué se vio de pandas. | Todo el mundo ejecuta una celda con `import pandas as pd`. |
| 10–40 | **Pandas desde cero (1):** Series, DataFrame, creación, carga y exploración (`head`, `info`, `describe`). | Distingue Series de DataFrame y lee `info()`/`describe()`. |
| 40–70 | **Pandas desde cero (2):** selección de columnas, `loc`/`iloc`, filtros simples y compuestos. | Elige `.loc` o `.iloc` con criterio y escribe un filtro compuesto. |
| 70–80 | **Descanso.** | — |
| 80–105 | **Pandas desde cero (3):** ordenación, columnas derivadas, `np.where`/`cut`, vectorizado frente a `apply`. | Explica por qué una operación vectorizada es preferible a `apply`. |
| 105–130 | **Pandas desde cero (4):** `groupby` y agregaciones (`mean`, `agg`, `size` frente a `count`). | Predice cuántos grupos salen y qué columnas quedan. |
| 130–147 | **Pandas desde cero (5):** valores ausentes (`isna`, `dropna`, `fillna`) y guardar/cargar CSV (Parquet si hay `pyarrow`). | Justifica si imputar o eliminar y por qué. |
| 147–167 | **Comparación final R ↔ pandas** sobre los mismos datos y operaciones (R base). | Reconoce el equivalente en la otra herramienta para cada operación. |
| 167–180 | **Mini-práctica y ticket de salida.** | Resuelve un filtro + columna derivada + resumen por grupo. |

**Límites de tiempo:** el bloque 2 (selección) debe cerrarse en el minuto 70; el `groupby` en el 130; la comparación con R en el 167. Si se acumula retraso, recortar el bloque de ausentes/I/O (5) y no el `groupby` ni la comparación final.

## 4. Arranque y pandas desde cero (1): estructuras y exploración (0–40 min)

### 4a. Arranque (0–10 min)

Objetivos de la sesión en una frase: *pasar de «mirar» datos a **seleccionar, transformar y resumir** con pandas, y cerrar comparando con R*.

Comprobar entorno:

```python
import sys
import numpy as np
import pandas as pd
print("Python", sys.version.split()[0], "| pandas", pd.__version__)
```

Preguntar antes de ejecutar: «¿qué versión de pandas esperas ver y por qué importa?» (compatibilidad de API y de motores como PyArrow).

### 4b. Series y DataFrame (10–40 min)

Empezar por lo mínimo, con un DataFrame diminuto, y crecer después al de empleados.

```python
# Series: una columna con nombre e índice
ventas = pd.Series([100, 250, 300], name="Ventas")
print(ventas)
print(ventas.dtype, ventas.shape, ventas.size, ventas.ndim)

# DataFrame: conjunto de columnas (Series) que comparten índice
productos = pd.DataFrame({
    "producto": ["A", "B", "C"],
    "ventas": [100, 250, 300],
    "precio": [10.5, 12.3, 9.8],
})
print(productos)
print(productos.dtypes)
```

Pasar al dataset de empleados (mismo que el EDA de NumPy, para continuidad):

```python
rng = np.random.default_rng(42)
n = 1000
empleados = pd.DataFrame({
    "id": np.arange(1, n + 1),
    "edad": rng.integers(18, 65, size=n),
    "salario": rng.normal(2500, 800, size=n).round(2),
    "experiencia": np.clip(rng.integers(18, 65, size=n) - rng.integers(18, 30, size=n), 0, None),
    "horas": rng.normal(40, 5, size=n).round(1),
    "nivel": rng.integers(0, 5, size=n),
    "satisfaccion": rng.normal(7, 2, size=n).round(2),
})
# atípicos y ausentes, como en el EDA
empleados.loc[rng.choice(n, 10, replace=False), "salario"] *= 4
empleados.loc[rng.choice(n, 15, replace=False), "satisfaccion"] = np.nan

print(empleados.shape)
print(empleados.head())
print(empleados.info())
print(empleados.describe(include=[np.number]).drop(columns="id"))
```

Cinco ideas: una columna es una Series; un DataFrame es una tabla con **índice común**; `info()` da tipos y nulos; `describe()` resume numéricas; `dtypes` revela tipos que luego condicionan operaciones.

**Chequeos de predicción:**
- Antes de `ventas.ndim`: «¿1 o 2 dimensiones?» → Series es 1-D; DataFrame es 2-D.
- Antes de `empleados.shape`: «¿cuántas filas y columnas esperas?» → 1000 filas.
- Antes de `empleados.info()`: «¿qué columna tendrá nulos y cuántos?» → `satisfaccion`, 15.
- Antes de `describe(...).drop(columns="id")`: «¿por qué quitamos `id`?» → no es una medida; sesga la lectura.

## 5. Pandas desde cero (2): selección, `.loc`/`.iloc` y filtros (40–70 min)

```python
# Una columna -> Series ; lista de columnas -> DataFrame
print(type(empleados["salario"]), type(empleados[["salario"]]))
print(empleados[["edad", "salario"]].head())

# Índice por etiqueta
empleados_idx = empleados.set_index("id")
print(empleados_idx.head(3))

# .loc por etiqueta, .iloc por posición
print(empleados_idx.loc[1, ["edad", "salario"]])     # etiqueta 1
print(empleados_idx.iloc[0, :2])                      # primera fila, dos primeras columnas
print(empleados_idx.loc[1:3, ["edad", "salario"]])   # incluye el extremo
print(empleados_idx.iloc[0:3, :2])                    # excluye el extremo

# Filtros
mayores = empleados[empleados["edad"] > 50]
print(mayores.shape)

# Filtro compuesto: paréntesis obligatorios
filtro = (empleados["salario"] > 3000) & (empleados["nivel"] >= 3) & (empleados["edad"] < 55)
print(empleados.loc[filtro, ["edad", "salario", "nivel"]].head())

# Alternativas
print(empleados[empleados["nivel"].isin([0, 4])].shape)
print(empleados.query("salario > 3000 and nivel >= 3").head(3))
```

Ideas clave: `df["col"]` es Series y `df[["col"]]` es DataFrame; con índice por etiqueta, **posición y etiqueta dejan de coincidir**; `.loc` incluye el extremo final y `.iloc` no; en filtros compuestos hay que **poner paréntesis** en cada condición.

**Chequeos de predicción:**
- Antes de `type(empleados["salario"])` frente a `type(empleados[["salario"]])`: «¿los dos son lo mismo?».
- Antes de `empleados_idx.loc[1, ...]` frente a `empleados_idx.iloc[0, ...]`: «¿devuelven la misma fila?».
- Antes de `loc[1:3]` frente a `iloc[0:3]`: «¿cuántas filas salen en cada uno?» → 3 y 3, pero por motivos distintos.
- Antes del filtro compuesto: «¿qué pasa si quito los paréntesis?».
- Antes de `query`: «¿devuelve lo mismo que el filtro compuesto?».

## 6. Descanso (70–80 min)

## 7. Pandas desde cero (3): ordenación, columnas derivadas y transformaciones (80–105 min)

```python
# Ordenación por varias claves
ordenado = empleados.sort_values(["nivel", "salario"], ascending=[True, False])
print(ordenado[["nivel", "salario"]].head())

# Columna derivada vectorizada
empleados["salario_anual"] = empleados["salario"] * 12
print(empleados[["salario", "salario_anual"]].head())

# Clasificación con np.where (dos ramas)
empleados["senior"] = np.where(empleados["experiencia"] >= 10, "sí", "no")
print(empleados["senior"].value_counts())

# Tramos con pd.cut (rangos definidos) o pd.qcut (cuantiles)
empleados["tramo_edad"] = pd.cut(
    empleados["edad"], bins=[17, 30, 45, 65], labels=["joven", "medio", "mayor"]
)
print(empleados["tramo_edad"].value_counts())

# Transformación encadenada con assign (sin mutar el original)
resumen = (
    empleados.assign(salario_miles=empleados["salario"] / 1000)
    .rename(columns={"salario_miles": "salario_k"})
)
print(resumen[["salario", "salario_k"]].head(3))

# apply: existe, pero se evita si hay alternativa vectorizada
empleados["nivel_txt"] = empleados["nivel"].apply(lambda x: "alto" if x >= 3 else "bajo")
print(empleados[["nivel", "nivel_txt"]].head())
```

Ideas clave: las operaciones sobre columnas son **vectorizadas**; `np.where` equivale a un if/else por fila; `cut`/`qcut` crean tramos; `assign` devuelve una copia transformada; `apply` es la última opción porque recorre fila a fila y es más lenta.

**Chequeos de predicción:**
- Antes de `sort_values` con dos claves: «¿qué desempata cuando hay empate en `nivel`?».
- Antes de `np.where`: «¿cuántos `sí` esperas, aproximadamente?».
- Antes de `pd.cut`: «¿en qué tramo cae una persona de 45 años?» → depende de los bordes; leerlo antes de ejecutar.
- Antes de `assign`: «¿se modifica `empleados` original?» → no.
- Antes de `apply`: «¿por qué es más lento que una operación vectorizada?».

## 8. Pandas desde cero (4): `groupby` y agregaciones (105–130 min)

```python
# Media de salario por nivel
print(empleados.groupby("nivel")["salario"].mean())

# Varias métricas a la vez
print(empleados.groupby("nivel")["salario"].agg(["mean", "median", "count"]))

# Agregaciones distintas por columna
print(
    empleados.groupby("nivel").agg(
        salario_medio=("salario", "mean"),
        horas_medias=("horas", "mean"),
        n=("id", "count"),
    )
)

# size frente a count: count ignora NaN
print(empleados.groupby("nivel")["satisfaccion"].size())
print(empleados.groupby("nivel")["satisfaccion"].count())

# Volver a DataFrame plano
por_nivel = empleados.groupby("nivel", as_index=False)["salario"].mean()
print(por_nivel)
```

Ideas clave: `groupby` **divide–aplica–combina**; la columna agrupada pasa a índice salvo `as_index=False`; `size()` cuenta filas y `count()` cuenta valores no nulos; nombrar agregaciones en un diccionario deja columnas legibles.

**Chequeos de predicción:**
- Antes del primer `groupby`: «¿cuántos grupos esperas?» → niveles 0–4, cinco.
- Antes de `agg(["mean","median","count"])`: «¿qué columnas saldrán?».
- Antes de `size()` frente a `count()`: «¿coinciden? ¿por qué no?» → hay 15 NaN.
- Antes de `as_index=False`: «¿cómo cambia la forma del resultado?».

## 9. Pandas desde cero (5): ausentes y guardar/cargar (130–147 min)

```python
# Diagnóstico de ausentes
print(empleados.isna().sum())
print(empleados["satisfaccion"].isna().mean().round(3))   # proporción

# Eliminar solo donde falta la clave de análisis
sin_faltantes = empleados.dropna(subset=["satisfaccion"])
print(len(empleados), len(sin_faltantes))

# Imputar con la mediana (robusta a atípicos)
empleados["satisfaccion_imp"] = empleados["satisfaccion"].fillna(
    empleados["satisfaccion"].median()
)
print(empleados[["satisfaccion", "satisfaccion_imp"]].isna().sum())

# Guardar y cargar
empleados.to_csv("empleados_limpio.csv", index=False)
recargado = pd.read_csv("empleados_limpio.csv")
print(recargado.shape, recargado.dtypes.head())

# Parquet (si hay pyarrow): conserva tipos y es más rápido
# empleados.to_parquet("empleados_limpio.parquet", index=False)
# recargado_pq = pd.read_parquet("empleados_limpio.parquet")
```

Ideas clave: `isna().sum()` localiza huecos y `isna().mean()` da su proporción; eliminar o imputar es una **decisión**, no un reflejo; la mediana es más robusta que la media ante atípicos; CSV pierde tipos y Parquet los conserva (si `pyarrow` está instalado).

**Chequeos de predicción:**
- Antes de `isna().sum()`: «¿en qué columna habrá 15?».
- Antes de `dropna(subset=...)`: «¿cuántas filas se pierden?».
- Antes de `fillna(median)`: «¿cuántos nulos quedan?» → cero en la columna imputada.
- Antes de `to_csv`/`read_csv`: «¿los tipos se conservan igual?» → normalmente no.

## 10. Comparación final R ↔ pandas (147–167 min)

Mismos datos pequeños y mismas cuatro operaciones en las dos herramientas. Si el grupo no tiene R listo, **proyectar** desde el equipo del profesor o abrir Colab con kernel R; no instalar.

**R base:**

```r
empleados <- data.frame(
  nombre  = c("Ana", "Luis", "Marta", "Pablo", "Elena"),
  edad    = c(34, 41, 29, 52, 38),
  salario = c(2400, 3100, 2200, 4200, 2800),
  nivel   = c(2, 3, 1, 4, 2)
)

head(empleados)
summary(empleados)

# 1) Filtro
empleados[empleados$salario > 3000, c("nombre", "salario")]

# 2) Columna derivada
empleados$salario_anual <- empleados$salario * 12

# 3) Resumen por grupo
aggregate(salario ~ nivel, data = empleados, FUN = mean)

# 4) Ausentes (si los hubiera)
mean(empleados$salario, na.rm = TRUE)
```

**Equivalente en pandas:**

```python
empleados_r = pd.DataFrame({
    "nombre":  ["Ana", "Luis", "Marta", "Pablo", "Elena"],
    "edad":    [34, 41, 29, 52, 38],
    "salario": [2400, 3100, 2200, 4200, 2800],
    "nivel":   [2, 3, 1, 4, 2],
})

print(empleados_r.head())
print(empleados_r.describe())

# 1) Filtro
print(empleados_r.loc[empleados_r["salario"] > 3000, ["nombre", "salario"]])

# 2) Columna derivada
empleados_r["salario_anual"] = empleados_r["salario"] * 12

# 3) Resumen por grupo
print(empleados_r.groupby("nivel")["salario"].mean())

# 4) Ausentes
print(empleados_r["salario"].mean())   # con NaN: skipna=True por defecto
```

Tabla de correspondencias para proyectar:

| Operación | R base | pandas |
|---|---|---|
| Acceso a columna | `df$salario` | `df["salario"]` |
| Filtro por filas | `df[df$salario > 3000, ]` | `df[df["salario"] > 3000]` |
| Columna nueva | `df$anual <- df$salario * 12` | `df["anual"] = df["salario"] * 12` |
| Resumen por grupo | `aggregate(salario ~ nivel, df, mean)` | `df.groupby("nivel")["salario"].mean()` |
| Ausente | `NA` + `na.rm = TRUE` | `NaN` + `skipna=True` por defecto |
| Índice | base 1 | base 0 |

Cinco contrastes: asignación `<-` frente a `=`; índice desde 1 frente a 0; `$` frente a `[...]`; fórmula `salario ~ nivel` frente a `groupby`; `NA`/`na.rm` frente a `NaN`/`skipna`. Ambos son vectorizados; la elección depende del ecosistema (informes reproducibles y estadística en R; ML y producción en Python).

**Chequeos de predicción:**
- Antes del filtro en R: «¿el índice de las filas que salen es 2 y 4?».
- Antes de `aggregate`: «¿cuántas filas tendrá el resultado?» → una por nivel distinto (cuatro).
- Antes de `mean(..., na.rm=TRUE)`: «¿qué pasa sin `na.rm`?» → devuelve `NA`.
- Antes de `describe()` en pandas: «¿qué columnas incluye?».

**Cierre comparativo:** preguntar «¿en cuál de las dos escribirías este análisis más rápido y por qué?» y dejar claro que **no hay ganador universal**: es contexto y ecosistema.

## 11. Mini-práctica y ticket de salida (167–180 min)

Sobre `empleados` (con `satisfaccion_imp` ya creada):

1. Filtrar empleados con `salario > 3000` y `nivel >= 3`; mostrar `edad`, `salario`, `nivel`.
2. Crear `coste_empresa = salario_anual * 1.3` (si no existe, calcular antes `salario_anual`).
3. Media de `horas` por `nivel` con `agg`, ordenada de mayor a menor.

Aplicar el chequeo de predicción antes de mostrar cada solución: cada pareja anticipa forma, columnas e índice del resultado y lo compara con lo real. Corregir comprobando **forma, columnas e índice**, y pedir interpretación, no solo lectura del código.

**Ticket de salida:** una frase que distinga `.loc` de `.iloc`, otra que explique qué hace `groupby`, y una comparación de una línea entre R y pandas para un filtro.

**Si sobra tiempo:** `pivot_table` mínimo de recuento (`pd.crosstab` o `pivot_table(index="nivel", columns="senior", aggfunc="size")`) y leer la tabla. No abrir visualización.

**Si falta tiempo:** recortar el bloque 5 (ausentes/I/O) a un `isna().sum()` y guardar el CSV para la próxima; **no tocar** el `groupby` ni la comparación con R.

## 12. Cierre y ajuste al ritmo

Al terminar, registrar: punto exacto alcanzado (selección, transformaciones, `groupby`, ausentes), si la comparación con R se hizo proyectada o local, y quién sigue sin entorno de pandas resuelto.

**Siguiente paso recomendado:** continuar UD2 con carga/limpieza de un dataset realista y EDA con pandas (`02-pandas_eda_visualizacion.ipynb`), y entrar después en Matplotlib aplicando la decisión de comparar gráficas Python/R sobre los mismos datos. Dejar `pivot_table` avanzado, joins y visualización para sus bloques.

## Referencias para el profesor

- [Guía de indexación y selección en pandas](https://pandas.pydata.org/docs/user_guide/indexing.html).
- [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html).
- [Trabajar con datos ausentes](https://pandas.pydata.org/docs/user_guide/missing_data.html).
- [R base: `aggregate`](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/aggregate.html).
