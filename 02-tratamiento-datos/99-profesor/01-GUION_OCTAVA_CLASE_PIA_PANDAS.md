# Guion de la octava clase de PIA — pandas desde cero y recordatorio final de R

> **Documento interno del profesorado. Solo repositorio docente; no publicar en `main` del alumnado, GitHub Pages ni Moodle.**

**Duración de referencia:** 3 horas (180 min).

**Continuidad real de la séptima clase (2 h):** estaba planteada con arranque de R (local o Colab), R base breve, la comparativa entregable y un repaso inicial de pandas (Series, DataFrame e inicio de indexación). **Antes de empezar, confirmar el punto real alcanzado** y ajustar:

- La comparativa **ya está encargada al alumnado y en curso**: hoy **no se reabre ni se le dedica tiempo de clase**; se recoge y corrige después desde `99-profesor/00-entregas-y-correcciones/`.
- Si R **no llegó a ejecutarse**, el bloque final de recordatorio y comparación con R se hace como **demostración proyectada** (o Colab), sin dedicar la clase a instalaciones.
- Si pandas **solo se vio hasta Series/DataFrame**, hoy se empieza de cero igualmente: la primera media hora reconstruye esa base y el resto avanza.

Pandas conserva solo lo ya presentado (Series, DataFrame e inicio de indexación). Por eso **se empieza de cero**, sin dar por sabido lo anterior.

## 1. Decisión de alcance: R al final, solo 10 minutos

- **R no es una herramienta principal del módulo.** Se ve ahora para **comparar** con pandas y, más adelante, para las **gráficas**, que es uno de sus puntos fuertes. No se enseña R en profundidad ni se convierte en una segunda línea de trabajo.
- **Pandas es el contenido nuevo y ocupa el grueso de la clase (unas dos horas y media).** Necesita la atención fresca del arranque; no conviene gastar los primeros minutos en un recordatorio de R que aún no tiene con qué compararse.
- **R se acaba de ver.** Un repaso aislado al principio se percibe como «otra clase de R» y rompe el hilo hacia pandas.
- **El recordatorio tiene más sentido al final**, cuando el alumnado ya ha hecho filtros, columnas derivadas y `groupby` en pandas: ahí el mismo problema resuelto en R y en pandas se lee de verdad. Además prepara la decisión ya tomada de comparar gráficas Python/R cuando llegue la visualización de UD2.
- **Formato del bloque final (10 min):** **recordatorio proyectado** con una tabla de correspondencias y **dos operaciones en vivo** (filtro y resumen por grupo), en R base (sin tidyverse) frente a pandas. El resto de equivalencias queda en el cuaderno `06_R_hazlo_tu.ipynb`. No es una clase nueva de R y no se recorre el temario de R.
- **Si el grupo llega sin R resuelto:** el bloque final se hace con **demostración proyectada** desde el equipo del profesor o con **Colab**; no se invierte tiempo en instalaciones.
- **Cierre administrativo:** en esos 10 min entra también **recordar la entrega de la comparativa** encargada; no se corrige en clase.

## 1b. Método de la sesión: notebook en directo con predicción antes de ejecutar (vigente)

- Se mantiene el patrón ya acordado: 1) formular la pregunta; 2) mostrar/rellenar la celda; 3) **chequeo de predicción** («¿qué salida esperas aquí?») antes de ejecutar; 4) ejecutar y comparar lo esperado con lo real; 5) interpretar en una frase.
- Cada alumno/equipo ejecuta **la misma celda a la vez** y **no se avanza hasta que la mayoría salga**.
- La teoría va dentro del notebook como **pequeños pasos ejecutables**, no como discurso previo.
- Refuerzo en la recámara: **celdas vacías** que el alumnado completa (patrón de `16-eda_numpy_edificios.ipynb`) si el grupo se dispersa.

## 1c. Estructura de cada bloque: teoría breve → notebook → «hazlo tú» (5 min)

Para reducir las desconexiones, **cada bloque de pandas tiene tres partes encadenadas** y no una lección seguida:

1. **Teoría mínima (3–5 min).** Un encuadre corto con una idea y un esquema simple en la pizarra o en una celda Markdown: qué problema resuelve, qué vocabulario usar y qué error típico evitar. No es volver a la clase magistral: en cuanto la idea está dicha, se pasa al notebook.
2. **Notebook en directo (10–15 min).** La misma idea se ejecuta celda a celda con el **chequeo de predicción** ya acordado («¿qué salida esperas?»). La teoría queda así «enganchada» al código que acaban de ver.
3. **«Hazlo tú» (5 min).** Una tarea pequeña y cerrada sobre el mismo DataFrame, con **resultado esperado** para autocorregirse. Se hace en pareja, se compara en voz alta y se pasa al bloque siguiente. No se corrige una a una: se pide a dos parejas que digan su resultado y se valida en pantalla.

El «hazlo tú» es deliberadamente corto: **una o dos líneas de código**, no un ejercicio largo. Su función es que el alumnado **escriba y ejecute** cada 15–20 minutos, no evaluar.

## 1d. Cuaderno «hazlo tú»: evidencia de asistencia y atención

- Hay **un cuaderno «hazlo tú» por notebook**: `02-tratamiento-datos/03-practicas/01_pandas_hazlo_tu.ipynb` (cinco bloques de pandas) y `01-fundamentos-python/03-practicas/06_R_hazlo_tu.ipynb` (R base y comparación). Están preparados de antemano: se usan los que correspondan a los notebooks que finalmente se impartan.
- Cada alumno resuelve en ellos las celdas de los bloques vistos y el ticket de salida.
- **Se entrega en Moodle al final de la clase** el/los cuadernos usados. Entregarlo **acredita asistencia**; que esté **completo acredita atención y seguimiento**.
- **Valoración binaria: hecho / no hecho.** No se corrige ejercicio a ejercicio ni se pone nota de acierto: se usa como **evidencia de seguimiento** para decidir si procede subir nota (participación, trabajo en clase), nunca como sustituto de una prueba.
- No hace daño a quien no lo termine: puede acabarlo en casa y subirlo igualmente; lo que se registra es la entrega y su grado de completitud, no la perfección.
- Las soluciones quedan en `02-tratamiento-datos/99-profesor/` (copia docente), no en el cuaderno público.

## 2. Material que conviene abrir antes de clase

Rutas relativas a la raíz del módulo:

| Uso | Ruta |
|---|---|
| Teoría de pandas (repaso del profesor) | `02-tratamiento-datos/01-teoria/01-pandas-introduccion.md` |
| Chuleta de pandas | `02-tratamiento-datos/01-teoria/03-pandas-chuleta.md` |
| Notebook principal de pandas | `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb` |
| Cuaderno de entrega «hazlo tú» — pandas (alumnado) | `02-tratamiento-datos/03-practicas/01_pandas_hazlo_tu.ipynb` |
| Cuaderno de entrega «hazlo tú» — R (alumnado) | `01-fundamentos-python/03-practicas/06_R_hazlo_tu.ipynb` |
| Soluciones docentes de ambos | `02-tratamiento-datos/99-profesor/01_pandas_hazlo_tu_SOLUCIONES.ipynb`, `01-fundamentos-python/99-profesor/03-practicas-soluciones/06_R_hazlo_tu_SOLUCIONES.ipynb` |
| Dataset de empleados (continuidad del EDA) | `01-fundamentos-python/03-practicas/09_eda_numpy.md` / `09_eda_numpy.ipynb` |
| Guía de R (solo para el bloque final) | `01-fundamentos-python/01-teoria/09-guia-r-complementario.md` |
| Notebook R (bloque final, opcional) | `01-fundamentos-python/02-ejemplos/06_introduccion_R_fundamentos.ipynb` |
| Soluciones docentes de pandas | `02-tratamiento-datos/99-profesor/practicas/01_pandas_fundamentos_SOLUCIONES.ipynb` |

Comprobar antes de entrar: que el entorno habitual importa `numpy` y `pandas`; que `pyarrow` está disponible si se enseña Parquet (si no, quedarse en CSV); y que el portátil del profesor puede proyectar el notebook R o abrir Colab.

### Precauciones concretas

- **No abrir** la celda interna `pd.get_option("mode.data_manager")` del notebook 01: depende de la versión y está obsoleta.
- El notebook `01_pandas_fundamentos.ipynb` usa un dataset de **clientes**; la clase usará el de **empleados** para enlazar con el EDA de NumPy. El de clientes queda como repertorio y para la práctica.
- No adelantar visualización, joins ni `pivot_table` avanzado salvo el `pivot_table` mínimo de recuento si sobra tiempo.
- En R, ceñirse a **R base** (`data.frame`, `$`, `aggregate`, `summary`); sin `dplyr` ni tidyverse.
- No afirmar que R sea siempre mejor para estadística ni que pandas sea siempre más rápido: depende de tarea, datos y herramientas.
- Si el grupo llega sin la comparativa entregada, no bloquear la clase: recordar la entrega en Moodle y seguir.

## 2b. Checklist Moodle antes de la clase

**Obligatorio:**

- [ ] **Notebook principal** `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb` subido al tema de UD2 (o verificado si ya estaba). Es el que se proyecta; el alumnado debe poder abrirlo.
- [ ] **Cuaderno de entrega** `02-tratamiento-datos/03-practicas/01_pandas_hazlo_tu.ipynb` subido como archivo descargable, no solo enlazado desde GitHub.
- [ ] **Tarea «Hazlo tú — pandas»** creada: entrega de **archivo**, acepta `.ipynb`, cierre al final de la clase, reentrega permitida. Sin nota numérica: **completitud / registro binario** (hecho-no hecho) para participación.
- [ ] **Tarea de la comparativa** revisada: visible, con plazo y formatos admitidos; se recuerda en el bloque R (148–158) y no se corrige en clase.
- [ ] **Instrucciones de la tarea «Hazlo tú»** redactadas en Moodle: se entrega al salir; entregar acredita asistencia; completo acredita seguimiento; no se corrige acierto; quien no termine puede subirlo después.

**Opcional (solo si se quiere dejar material de apoyo):**

- [ ] `02-tratamiento-datos/01-teoria/03-pandas-chuleta.md` como página o PDF de consulta.
- [ ] `01-fundamentos-python/03-practicas/06_R_hazlo_tu.ipynb` y `01-fundamentos-python/02-ejemplos/06_introduccion_R_fundamentos.ipynb`, solo si se quiere que el alumnado tenga la referencia R; el bloque de 10 min es proyectado.

**No subir:**

- Soluciones de `99-profesor/` (son docentes).
- Dataset de empleados: se genera en el notebook con `np.random.default_rng(42)`.
- `16-eda_numpy_edificios.ipynb`: ya está publicado y pertenece al cierre de UD1.

**Comprobaciones técnicas antes de entrar:**

- [ ] `pixi run python -c "import pandas, numpy; print(pandas.__version__, numpy.__version__)"`.
- [ ] `pixi run python -c "import pyarrow"`: si falla, **no enseñar Parquet** y quedarse en CSV.
- [ ] El portátil del profesor proyecta el notebook R o abre Colab con kernel R.
- [ ] No abrir la celda `pd.get_option("mode.data_manager")` del notebook 01.

## 3. Ritmo de 180 minutos

Cada bloque de pandas repite el patrón **teoría (3–5) + notebook (10–15) + hazlo tú (5)**.

| Minutos | Bloque | Comprobación |
|---|---|---|
| 0–10 | Arranque y objetivos; comprobar entorno (`import pandas`) y recuperar qué se vio de pandas. | Todo el mundo ejecuta una celda con `import pandas as pd`. |
| 10–38 | **Pandas desde cero (1):** teoría Series/DataFrame/índice → notebook (creación, carga, `head`, `info`, `describe`) → **hazlo tú**. | Distingue Series de DataFrame y lee `info()`/`describe()`. |
| 38–66 | **Pandas desde cero (2):** teoría etiqueta/posición → notebook (`loc`/`iloc`, filtros simples y compuestos) → **hazlo tú**. | Elige `.loc` o `.iloc` con criterio y escribe un filtro compuesto. |
| 66–76 | **Descanso.** | — |
| 76–102 | **Pandas desde cero (3):** teoría vectorización → notebook (ordenación, columnas derivadas, `np.where`/`cut`, `apply`) → **hazlo tú**. | Explica por qué una operación vectorizada es preferible a `apply`. |
| 102–128 | **Pandas desde cero (4):** teoría split-apply-combine → notebook (`groupby`, `agg`, `size` frente a `count`) → **hazlo tú**. | Predice cuántos grupos salen y qué columnas quedan. |
| 128–148 | **Pandas desde cero (5):** teoría ausentes y tipos → notebook (`isna`, `dropna`, `fillna`, CSV; Parquet si hay `pyarrow`) → **hazlo tú breve**. | Justifica si imputar o eliminar y por qué. |
| 148–158 | **Recordatorio de R y comparativa** (10 min; R no es herramienta principal). | Reconoce el equivalente en pandas de un filtro y un resumen por grupo. |
| 158–180 | **Mini-práctica, ticket de salida y entrega.** | Resuelve un filtro + columna derivada + resumen por grupo. |

**Límites de tiempo:** el bloque 2 (selección) debe cerrarse en el minuto 66; el `groupby` en el 128; el recordatorio de R en el 158. El «hazlo tú» **nunca se salta** en los bloques 1–4: si el reloj aprieta, se recorta la demostración del notebook, no la práctica. Si se acumula retraso, recortar el bloque 5 (ausentes/I/O) y no el `groupby` ni el recordatorio de R; este último puede bajar a 5 min, pero no desaparecer: incluye la entrega de la comparativa.

## 4. Arranque y pandas desde cero (1): estructuras y exploración (0–38 min)

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

### 4b. Series y DataFrame (10–38 min)

**Teoría mínima (4 min).** Escribir en la pizarra, junto al notebook:

- Una **Series** es una columna con **índice** (etiquetas) y un tipo; es 1-D.
- Un **DataFrame** es una tabla 2-D formada por **columnas que comparten el mismo índice** (como una hoja de cálculo o un diccionario de Series alineadas).
- Una fila se identifica por el **índice**; una columna, por su **nombre**. `dtypes` dice qué operaciones tienen sentido.

Enlazar con lo ya visto: en el EDA de NumPy `data[:, 2]` era «la tercera columna por posición»; en pandas `df["salario"]` es «la columna **por nombre**», y el índice añade etiquetas. Ese es el salto conceptual del bloque.

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

**Hazlo tú (5 min).** En el cuaderno de entrega, **cada uno en el suyo** (se trabaja en pareja), sobre `empleados`:

```python
# 1) Selecciona las columnas edad y salario y muestra las 3 primeras filas.
# 2) Imprime su forma (shape) y sus tipos (dtypes).
```

- **Resultado esperado:** 3 filas × 2 columnas; `edad` entera y `salario` decimal (`float64`).
- **Comprobación rápida:** si `shape` sale `(3, 2)`, han usado lista de columnas; si sale `(3,)` con `df[["..."]]` mal escrito, han seleccionado una sola columna y conviene señalarlo.
- **Puesta en común (1 min):** una pareja dicta el `shape` y otra los `dtypes`; se valida en pantalla.

**Chequeos de predicción:**
- Antes de `ventas.ndim`: «¿1 o 2 dimensiones?» → Series es 1-D; DataFrame es 2-D.
- Antes de `empleados.shape`: «¿cuántas filas y columnas esperas?» → 1000 filas.
- Antes de `empleados.info()`: «¿qué columna tendrá nulos y cuántos?» → `satisfaccion`, 15.
- Antes de `describe(...).drop(columns="id")`: «¿por qué quitamos `id`?» → no es una medida; sesga la lectura.

## 5. Pandas desde cero (2): selección, `.loc`/`.iloc` y filtros (38–66 min)

**Teoría mínima (4 min).** Tres ideas, escritas junto al notebook:

- **Etiqueta frente a posición:** el índice guarda etiquetas. Si el índice es `id` (1…1000), la **posición** `0` y la **etiqueta** `1` ya no coinciden.
- **`.loc` usa etiquetas y `.iloc` usa posiciones.** `.loc[1:3]` **incluye** el 3; `.iloc[0:3]` **excluye** la posición 3 (convención de Python).
- **Filtro booleano:** `df[condición]` devuelve las filas donde la condición es `True`. En condiciones compuestas cada parte va **entre paréntesis**: `(a) & (b)`, nunca `a & b` sin paréntesis.

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

**Hazlo tú (5 min).** En el cuaderno de entrega, **cada uno en el suyo** (se trabaja en pareja):

```python
# 1) Con empleados_idx (índice = id), obtén edad y salario de las etiquetas 2 a 5.
# 2) Filtra los empleados con nivel == 4 y salario > 3000; muestra edad, salario y nivel.
```

- **Resultado esperado (1):** 4 filas (etiquetas 2, 3, 4 y 5), columnas `edad` y `salario`.
- **Resultado esperado (2):** solo filas que cumplen **las dos** condiciones; el número de filas debe ser pequeño frente al total.
- **Error frecuente a cazar:** `empleados.loc[2:5]` sí funciona por etiqueta; `empleados.iloc[2:5]` daría **3** filas (posición 5 excluida). Preguntar a una pareja cuántas filas le salen y por qué.
- **Puesta en común (1 min):** proyectar una solución con `.loc` y otra con `.iloc` y contrastar el número de filas.

**Chequeos de predicción:**
- Antes de `type(empleados["salario"])` frente a `type(empleados[["salario"]])`: «¿los dos son lo mismo?».
- Antes de `empleados_idx.loc[1, ...]` frente a `empleados_idx.iloc[0, ...]`: «¿devuelven la misma fila?».
- Antes de `loc[1:3]` frente a `iloc[0:3]`: «¿cuántas filas salen en cada uno?» → 3 y 3, pero por motivos distintos.
- Antes del filtro compuesto: «¿qué pasa si quito los paréntesis?».
- Antes de `query`: «¿devuelve lo mismo que el filtro compuesto?».

## 6. Descanso (66–76 min)

## 7. Pandas desde cero (3): ordenación, columnas derivadas y transformaciones (76–102 min)

**Teoría mínima (4 min).** Dos ideas:

- **Vectorizado frente a fila a fila:** `df["salario"] * 12` opera sobre **toda la columna a la vez** (rápido, en C). `apply` recorre fila a fila en Python: se usa solo cuando no hay alternativa vectorizada.
- **Tres formas de crear una columna:** asignación directa (`df["nueva"] = ...`), decisión por fila con `np.where(cond, a, b)` y tramos con `pd.cut` (bordes fijos) o `pd.qcut` (cuantiles). `assign` crea una copia transformada sin tocar el original.

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

**Hazlo tú (5 min).** En el cuaderno de entrega, sobre `empleados`:

```python
# 1) Crea salario_miles = salario / 1000.
# 2) Crea tramo_horas con pd.cut sobre horas: [0, 35, 42, 60] -> ["parcial", "completa", "extra"].
# 3) Cuenta cuántos empleados hay en cada tramo.
```

- **Resultado esperado:** una columna nueva decimal y un `value_counts()` con tres tramos; la suma de los tres recuentos es 1000.
- **Comprobación rápida:** si la suma no da 1000, hay valores fuera de los bordes (revisar `horas` negativas o extremas).
- **Puesta en común (1 min):** una pareja dicta el tramo mayoritario y se valida en pantalla.

**Chequeos de predicción:**
- Antes de `sort_values` con dos claves: «¿qué desempata cuando hay empate en `nivel`?».
- Antes de `np.where`: «¿cuántos `sí` esperas, aproximadamente?».
- Antes de `pd.cut`: «¿en qué tramo cae una persona de 45 años?» → depende de los bordes; leerlo antes de ejecutar.
- Antes de `assign`: «¿se modifica `empleados` original?» → no.
- Antes de `apply`: «¿por qué es más lento que una operación vectorizada?».

## 8. Pandas desde cero (4): `groupby` y agregaciones (102–128 min)

**Teoría mínima (4 min).** **Dividir–aplicar–combinar:** `groupby` parte las filas en grupos según una o varias columnas, aplica un cálculo a cada grupo y vuelve a combinar el resultado. Dos consecuencias prácticas:

- La columna por la que se agrupa pasa a ser el **índice** del resultado (salvo `as_index=False`).
- `size()` cuenta **filas**; `count()` cuenta **valores no nulos**. Con ausentes, no coinciden.

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

**Hazlo tú (5 min).** En el cuaderno de entrega:

```python
# 1) Media de salario por senior (sí/no).
# 2) Para satisfaccion, muestra size() y count() por nivel y explica la diferencia.
```

- **Resultado esperado (1):** dos filas (`no`, `sí`) con su salario medio.
- **Resultado esperado (2):** `size()` suma 1000; `count()` suma 985 (15 nulos).
- **Comprobación rápida:** si las dos columnas suman lo mismo, han usado mal `count()` o no quedan nulos en su DataFrame.
- **Puesta en común (1 min):** preguntar «¿por qué no coinciden?» y validar con el dato de 15 ausentes.

**Chequeos de predicción:**
- Antes del primer `groupby`: «¿cuántos grupos esperas?» → niveles 0–4, cinco.
- Antes de `agg(["mean","median","count"])`: «¿qué columnas saldrán?».
- Antes de `size()` frente a `count()`: «¿coinciden? ¿por qué no?» → hay 15 NaN.
- Antes de `as_index=False`: «¿cómo cambia la forma del resultado?».

## 9. Pandas desde cero (5): ausentes y guardar/cargar (128–148 min)

**Teoría mínima (3 min).** Un ausente (`NaN`) **no es un cero**: es «no sabemos». Por eso:

- Se **diagnostica** primero (`isna().sum()` y la proporción con `isna().mean()`).
- Se **decide** entre eliminar (`dropna`) o imputar (`fillna`); no hay una respuesta universal: depende de cuántos sean y de si faltan al azar.
- Al **guardar**, CSV no conserva tipos ni nulos con fidelidad; Parquet sí (si hay `pyarrow`).

**Notebook en directo (12 min).** Ejecutar el bloque en el notebook proyectado, con los chequeos de predicción antes de cada operación. No abrir Parquet si `pyarrow` no está disponible.

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

**Hazlo tú breve (3 min).** En el cuaderno de entrega:

```python
# 1) Cuenta los ausentes por columna.
# 2) Crea satisfaccion_imp imputando con la mediana y comprueba que ya no quedan nulos.
```

- **Resultado esperado:** solo `satisfaccion` tiene 15; tras imputar, 0 en `satisfaccion_imp`.
- **Puesta en común (1 min):** preguntar «¿por qué la mediana y no la media?» (atípicos).

**Chequeos de predicción:**
- Antes de `isna().sum()`: «¿en qué columna habrá 15?».
- Antes de `dropna(subset=...)`: «¿cuántas filas se pierden?».
- Antes de `fillna(median)`: «¿cuántos nulos quedan?» → cero en la columna imputada.
- Antes de `to_csv`/`read_csv`: «¿los tipos se conservan igual?» → normalmente no.

## 10. Recordatorio de R y comparativa (148–158 min)

**No es una clase de R.** R no es una herramienta principal del módulo: ahora se usa para comparar y, más adelante, para las gráficas. En estos 10 minutos:

1. **Recordar la comparativa** encargada y su entrega en Moodle (1 min).
2. **Proyectar la tabla de correspondencias** (3 min).
3. **Ejecutar solo dos operaciones** en R y en pandas: un filtro y un resumen por grupo (4 min). No recorrer los dos bloques de código enteros.
4. **Cerrar** con «no hay ganador universal; depende del ecosistema» (2 min).

El código completo queda como **referencia para el profesor** y en el cuaderno `06_introduccion_R_fundamentos.ipynb`; el `06_R_hazlo_tu.ipynb` sirve para practicar. No se proyecta entero ni se copia en la pizarra. Si el grupo no tiene R listo, **proyectar** desde el equipo del profesor o abrir Colab con kernel R; no instalar.

**R base (solo filtro y resumen):**

```r
empleados <- data.frame(
  nombre  = c("Ana", "Luis", "Marta", "Pablo", "Elena"),
  edad    = c(34, 41, 29, 52, 38),
  salario = c(2400, 3100, 2200, 4200, 2800),
  nivel   = c(2, 3, 1, 4, 2)
)

# 1) Filtro
empleados[empleados$salario > 3000, c("nombre", "salario")]

# 2) Resumen por grupo
aggregate(salario ~ nivel, data = empleados, FUN = mean)
```

**Equivalente en pandas (solo filtro y resumen):**

```python
empleados_r = pd.DataFrame({
    "nombre":  ["Ana", "Luis", "Marta", "Pablo", "Elena"],
    "edad":    [34, 41, 29, 52, 38],
    "salario": [2400, 3100, 2200, 4200, 2800],
    "nivel":   [2, 3, 1, 4, 2],
})

# 1) Filtro
print(empleados_r.loc[empleados_r["salario"] > 3000, ["nombre", "salario"]])

# 2) Resumen por grupo
print(empleados_r.groupby("nivel")["salario"].mean())
```

**Referencia completa (no proyectar entera):** el bloque ampliado con columna derivada, ausentes y tabla de correspondencias está en el cuaderno `01-fundamentos-python/02-ejemplos/06_introduccion_R_fundamentos.ipynb` y en el guion de la séptima clase. Aquí basta con los dos casos.

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

**Chequeos de predicción (solo dos, para no gastar el bloque):**
- Antes del filtro en R: «¿el índice de las filas que salen es 2 y 4?».
- Antes de `aggregate`: «¿cuántas filas tendrá el resultado?» → una por nivel distinto (cuatro).

**Cierre comparativo:** preguntar «¿en cuál de las dos escribirías este análisis más rápido y por qué?» y dejar claro que **no hay ganador universal**: es contexto y ecosistema. Recordar que R vuelve cuando lleguen las gráficas.

## 11. Mini-práctica, ticket y entrega (158–180 min)

Sobre `empleados` (con `satisfaccion_imp` ya creada):

1. Filtrar empleados con `salario > 3000` y `nivel >= 3`; mostrar `edad`, `salario`, `nivel`.
2. Crear `coste_empresa = salario_anual * 1.3` (si no existe, calcular antes `salario_anual`).
3. Media de `horas` por `nivel` con `agg`, ordenada de mayor a menor.
4. Sobre el DataFrame original, contar ausentes por columna y justificar en una frase si imputar o eliminar `satisfaccion`.

Aplicar el chequeo de predicción antes de mostrar cada solución: cada pareja anticipa forma, columnas e índice del resultado y lo compara con lo real. Corregir comprobando **forma, columnas e índice**, y pedir interpretación, no solo lectura del código.

**Ticket de salida:** una frase que distinga `.loc` de `.iloc`, otra que explique qué hace `groupby`, y una comparación de una línea entre R y pandas para un filtro.

**Entrega (cierre de clase, 3 min).** El alumnado sube a la tarea de Moodle **antes de salir** el/los cuadernos «hazlo tú» usados (`01_pandas_hazlo_tu.ipynb` y, si se ha hecho R, `06_R_hazlo_tu.ipynb`). Se comprueba: (a) que el archivo se ha subido → **asistencia**; (b) que las celdas de los cinco bloques y el ticket están resueltas → **atención/seguimiento**. Registro **binario (hecho / no hecho)** para la valoración de participación, sin corregir aciertos. Quien no lo termine puede subirlo más tarde.

**Si sobra tiempo:** `pivot_table` mínimo de recuento (`pd.crosstab` o `pivot_table(index="nivel", columns="senior", aggfunc="size")`) y leer la tabla. No abrir visualización.

**Si falta tiempo:** recortar el bloque 5 (ausentes/I/O) a un `isna().sum()`; **no tocar** el `groupby`, el recordatorio de R ni la entrega del cuaderno (aunque sea incompleto, debe subirse).

## 12. Cierre y ajuste al ritmo

Al terminar, registrar: punto exacto alcanzado (selección, transformaciones, `groupby`, ausentes), si el recordatorio de R se hizo proyectado o local, y quién sigue sin entorno de pandas resuelto. Anotar también **quién entregó el cuaderno** (asistencia) y si estaba completo (atención), para la valoración binaria de participación.

**Siguiente paso recomendado:** continuar UD2 con carga/limpieza de un dataset realista y EDA con pandas (`02-pandas_eda_visualizacion.ipynb`), y entrar después en Matplotlib aplicando la decisión de comparar gráficas Python/R sobre los mismos datos. Dejar `pivot_table` avanzado, joins y visualización para sus bloques.

## Referencias para el profesor

- [Guía de indexación y selección en pandas](https://pandas.pydata.org/docs/user_guide/indexing.html).
- [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html).
- [Trabajar con datos ausentes](https://pandas.pydata.org/docs/user_guide/missing_data.html).
- [R base: `aggregate`](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/aggregate.html).
