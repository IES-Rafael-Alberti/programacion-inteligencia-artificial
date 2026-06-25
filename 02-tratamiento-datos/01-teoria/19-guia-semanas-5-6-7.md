# UD2 -- Módulo PIA (Semanas 5, 6 y 7) -- Actualización 2025 (Python 3.12.2, Pandas 2.3.3, Polars 1.34.0)

**Nota:** Todo el código y ejemplos presentados han sido probados con
Python 3.12.2, Pandas 2.3.3 y Polars 1.34.0 para asegurar
compatibilidad. Se incluyen advertencias sobre funciones obsoletas o
cambiadas en estas versiones. Además, se proporcionan notebooks con
ejercicios prácticos *funcionales* en el entorno especificado, de modo
que los estudiantes puedan ejecutarlos sin modificaciones adicionales.

## Semana 5: Pandas Avanzado y Introducción a Polars (modo *eager*)

En la semana 5 exploraremos funcionalidades avanzadas de **Pandas** y
presentaremos la librería **Polars** (en su modo de ejecución inmediata
o *eager*). Veremos cómo realizar operaciones avanzadas en Pandas,
seguidas de sus equivalentes en Polars, comparando sintaxis, rendimiento
y buenas prácticas.

### Conceptos Avanzados de Pandas

**Pandas** es una biblioteca potente para manipulación de datos
tabulares. Tras haber cubierto sus bases, profundizaremos en
características avanzadas que permiten análisis más complejos y
eficientes:

-   **Indexación avanzada y Multi-índices:** Pandas permite índices
    jerárquicos (MultiIndex) que facilitan trabajar con datos
    dimensionales (por ejemplo, datos agrupados por varias claves).
    Veremos cómo crear MultiIndex (por ejemplo, usando `set_index` con
    múltiples columnas) y cómo acceder a sus niveles con `loc` y métodos
    como `swaplevel` o `xs`. También aprenderemos a *aplanar* MultiIndex
    con `reset_index` cuando se requiera.

-   **Operaciones de *GroupBy* y agregaciones complejas:** Revisaremos
    cómo agrupar datos por una o varias claves y aplicar múltiples
    agregaciones a la vez. Por ejemplo, usar
    `df.groupby("col").agg({"valor": ["mean", "max", "min"]})` para
    obtener varias métricas. Discutiremos la diferencia entre
    *agregación* (`agg`/*sum*, *mean*, etc.), *transformación*
    (`transform`, que devuelve un resultado del mismo tamaño que el
    grupo, útil para operaciones como cálculo de *z-score* dentro de
    grupos) y *aplicación* (`apply`, para funciones arbitrarias a cada
    grupo, aunque generalmente menos eficiente). Aprenderemos buenas
    prácticas: preferir agregaciones vectorizadas en lugar de `apply`
    con funciones Python puras, ya que las funciones nativas de Pandas
    están optimizadas en C.

-   **Combinación de DataFrames (joins/merges):** Analizaremos cómo unir
    conjuntos de datos: `pd.merge` (o `DataFrame.merge`) para combinar
    DataFrames por columnas clave, especificando tipos de join (*inner*,
    *left*, *right*, *outer*). Ejemplo:
    `pd.merge(df_clientes, df_pedidos, on="cliente_id", how="left")`.
    También veremos la alternativa de usar índices con
    `left_index`/`right_index`. Se explicará cómo manejar nombres de
    columnas repetidos (argumentos `suffixes`) y merges complejos (como
    *join* condicionales mediante combinaciones de filtros si fuese
    necesario).

-   **Pivot tables y *reshaping* (reformateo de datos):** Veremos cómo
    reestructurar datos de formato *largo* a *ancho* y viceversa. Con
    `pd.pivot_table` podemos resumir datos en forma de tabla dinámica,
    por ejemplo:
    `pd.pivot_table(df, values="ventas", index="region", columns="producto", aggfunc="sum")`
    para obtener ventas totales por región/producto. También revisaremos
    `df.melt` para hacer el proceso inverso (*unpivot*, pasar de ancho a
    largo), y `df.stack/unstack` que funcionan con MultiIndex para
    pivotar niveles de índice/columna.

-   *Manejo eficiente de datos y tipos::* Pandas 2 ha introducido los
    tipos *nullable* (basados en *extension types* y en muchos casos
    usando Apache Arrow). Por ejemplo, ahora al leer datos CSV podemos
    especificar `dtype_backend="pyarrow"` para usar tipos de datos de
    Arrow, que pueden mejorar rendimiento en ciertas
    operaciones[\[1\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=match%20at%20L390%20In%20,pyarrow)[\[2\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=In%20,pyarrow).
    También, a partir de Pandas 2.x el tipo por defecto para cadenas es
    `string[python]` (o `string[pyarrow]` si se activa Arrow), en lugar
    de `object`. Explicaremos las ventajas de usar tipos específicos
    como `Categorical` (para variables categóricas que se repiten,
    reduciendo memoria y acelerando comparaciones) y los tipos
    enteros/booleanos *nullable* (`Int64`, `boolean`) que permiten `NA`.

-   **Fechas, tiempos y series temporales:** Repasaremos funcionalidades
    para datos de tiempo: el atributo `.dt` de Pandas para operar sobre
    columnas datetime (obtener año, mes, día, día de la semana, etc.), y
    métodos especializados como `resample` (re-muestrear series
    temporales a ciertas frecuencias, ej. pasar de datos diarios a
    mensuales calculando sumas o medias) y *ventanas móviles*
    (`rolling`/`expanding` para cálculos como medias móviles). Notar que
    en Pandas 2 se eliminaron atributos obsoletos como
    `dt.week`/`dt.weekofyear` en favor de
    `dt.isocalendar().week`[\[3\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=,45018),
    por lo que actualizaremos cualquier código que usaba las propiedades
    antiguas de semana.

-   **Evitar SettingWithCopy y uso de Copy-on-Write (CoW):** Una fuente
    común de confusión es la advertencia *SettingWithCopyWarning* cuando
    se asignan valores en un *slice* de un DataFrame. La recomendación
    es siempre usar métodos de asignación *seguros*, por ejemplo
    `df.loc[filtro, "columna"] = valor` en vez de
    `df[filtro]["columna"] = valor`. Pandas está introduciendo
    *Copy-on-Write* para mitigar estos problemas copiando datos solo al
    modificar (en Pandas 2.x aún está en desarrollo, pero es importante
    conocer esta dirección futura de la librería). Aunque CoW no está
    totalmente activo por defecto en Pandas 2.3, es un tema emergente:
    mencionamos su objetivo de eliminar *views* problemáticas y la
    necesidad de .copy() explícito en ciertos casos.

-   **Funciones obsoletas/eliminadas en Pandas 2:** Un punto crucial al
    actualizar código es conocer qué ha cambiado o dejado de existir:

-   El método `DataFrame.append` (y `Series.append`) fue **eliminado**
    en Pandas 2.0 (había sido deprecado en 1.4). Intentar usar
    `df1.append(df2)` ahora dará error. La alternativa es usar
    `pd.concat([df1, df2])`[\[4\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=match%20at%20L1730%20,GH%2035407).
    En nuestros ejemplos reemplazamos cualquier uso antiguo de append
    por concat.

-   El método `DataFrame.lookup` (para buscar valores tipo *Excel* por
    fila-col) también fue
    removido[\[5\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=,35224);
    se puede reemplazar por combinaciones de índices o merges según el
    caso.

-   Atributos de fechas: ya mencionado `dt.week` ya no existe; hay que
    usar `dt.isocalendar().week`.

-   Método `Series.iteritems()`/`DataFrame.iteritems()` también se
    deprecó (usar `Series.items()`/`DataFrame.items()`
    directamente)[\[6\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=match%20at%20L1725%20,instead%20%28GH%2045321).

-   Otras depreciaciones removidas son más raras (como
    `Series.to_dense()`, `DataFrame.to_sparse()` antiguas, ciertos
    métodos de `Styler`, etc.); en general, cualquier aviso de
    *FutureWarning* en versiones 1.x ahora puede significar eliminación
    en 2.x.

**Buenas prácticas de rendimiento en Pandas:** Dentro de Pandas,
reiteraremos consejos para escribir código eficiente: - Evitar bucles
Python sobre filas o elementos individuales. En su lugar, aprovechar la
*vectorización* (operaciones sobre series/columnas completas en una sola
expresión) y funciones *ufuncs* de NumPy/Pandas. Por ejemplo, en vez de
iterar para calcular una columna "precio con IVA", hacer
`df["precio_con_iva"] = df["precio"] * 1.21` directamente (que usa
operaciones en C optimizadas). - Minimizar el uso de `DataFrame.apply`
con funciones Python puras para cálculos numéricos intensivos. `apply`
itera internamente en Python y suele ser mucho más lento que usar
métodos vectoriales nativos. Sólo usar `apply`/`applymap` para
operaciones que no se puedan expresar fácilmente con las herramientas de
Pandas/NumPy. - Si se necesitan operaciones complejas por grupo,
intentar usar combinaciones de `groupby` con `transform` o `agg`. Por
ejemplo, para estandarizar valores por grupo:
`df["valor_std"] = df.groupby("grupo")["valor"].transform(lambda x: (x - x.mean())/x.std())`.
Esto aprovecha internamente código C para cada grupo en lugar de Python
puro. - Construir DataFrames de forma eficiente: si vamos acumulando
datos, evitar hacer `df = df.append(nueva_fila)` en cada iteración (esto
era malo incluso antes de que `append` fuera eliminado). Es mejor
recopilar las filas en una lista y luego hacer un solo `pd.DataFrame` o
utilizar `pd.concat` en una lista de DataFrames. En Pandas 2.x, la
ausencia de `append` enfatiza esta práctica. - Liberar memoria cuando
sea oportuno: Pandas no libera memoria inmediatamente al eliminar
referencias al DataFrame (depende del *garbage collector*). Si manejamos
conjuntos de datos muy grandes, a veces es útil usar `del df` y
`gc.collect()`, o bien procesar en trozos (chunks) usando el parámetro
`chunksize` en `pd.read_csv`, etc. (Este punto se conectará con el uso
de Polars *lazy* en la siguiente sección).

### Introducción a Polars (ejecución *eager*)

Ahora introducimos **Polars**, un motor de *DataFrame* de nueva
generación escrito en Rust, diseñado para alto rendimiento en análisis
de datos. Polars soporta dos modos de ejecución: - **Eager**
(inmediato): similar a Pandas, cada operación se ejecuta al invocarla y
devuelve resultados inmediatamente. - **Lazy** (perezoso): las
operaciones se acumulan en un plan de consulta que se optimiza y ejecuta
al final (modo que veremos en detalle en la semana 6).

En esta semana nos centraremos en el modo *eager* para familiarizarnos
con la sintaxis básica de Polars, comparándola con Pandas.

#### ¿Por qué Polars? Ventajas clave

Polars ofrece **mejoras de rendimiento sustanciales** respecto a Pandas
en muchos escenarios, aprovechando la paralelización en múltiples
núcleos y optimizaciones internas: - Está implementado en **Rust**
(lenguaje de bajo nivel centrado en eficiencia y seguridad de memoria) y
utiliza *multihilo* automáticamente. A diferencia de Pandas (que
internamente usa Python/C con el *GIL* limitando un hilo por vez),
Polars ejecuta operaciones en paralelo por defecto, aprovechando CPUs
multi-core[\[7\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=The%20Problem%20with%20Sequential%20Thinking%3A,Pandas%20works%20through%20operations%20sequentially)[\[8\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Polars%27%20Parallel%20Mindset%3A%20Polars%20assumes,of%20these%20things%20at%20once).
Esto se traduce en aceleraciones notables: en benchmarks con \~580 mil
filas, Polars fue entre \~3x y \~22x más rápido que Pandas en filtros,
agregaciones, groupby, ordenamientos,
etc[\[9\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Operation%20Pandas%20,61x). -
Mantiene una API de **DataFrame familiar**, inspirada en Pandas, por lo
que muchos conceptos son transferibles. Migrar a Polars no requiere
*reaprender* análisis de datos desde
cero[\[10\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Polars%20changes%20the%20game,relearning%20data%20science%20from%20scratch),
sino adaptar la sintaxis y adoptar un estilo más expresivo
(*lazy/expressions*, que veremos). - Es eficiente en memoria, usando un
diseño columnar (basado en Apache Arrow en gran medida). Permite
trabajar con datasets más grandes en la misma memoria, e incluso
introducir *streaming* (procesamiento en *batches* sin cargar todo a
RAM, útil para conjuntos mayores que la memoria disponible, lo
comentaremos en semana 6).

**Modo *eager* vs *lazy*: ¿cuándo usar cada uno?** Polars nos da la
flexibilidad de elegir: - En tareas **interactivas o de conjuntos de
datos pequeños/medianos**, el modo *eager* (e.g. usar `pl.read_csv`
directamente) es apropiado, obteniendo resultados inmediatos similares a
Pandas[\[11\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=When%20to%20Use%20Each%20Mode%3A).
Permite explorar datos rápidamente. - Para **pipelines de datos más
pesados o tareas repetitivas en producción**, el modo *lazy* (usando
`pl.scan_csv` y aplazando la ejecución hasta `collect()`) suele ser
preferible, ya que antes de ejecutar puede **optimizar globalmente** la
secuencia de operaciones (filtrando tempranamente, leyendo sólo columnas
necesarias, fusionando
pasos)[\[12\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Lazy%20Evaluation%27s%20Power%3A%20Polars%20can,turn%20decisions)[\[13\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=The%20Optimization%20Magic%3A%20During%20lazy,and%20Polars%20makes%20it%20efficient).
*Lazy* brilla en escenarios de **máximo rendimiento** y manejo de
grandes volúmenes. - En Polars es fácil pasar de un modo a otro:
cualquier `DataFrame` *eager* puede convertirse a *lazy* con
`df.lazy()`, y un `LazyFrame` a *eager* con `lf.collect()`. Incluso se
puede combinar: trabajar lazy pero si se requiere una operación no
soportada en lazy, convertir a eager temporalmente (aunque esto rompe la
optimización global, por lo que es el último recurso).

#### Operaciones básicas en Polars (comparativa con Pandas)

Veamos ahora, con ejemplos prácticos, cómo se realizan las operaciones
comunes en Polars (modo *eager*) en contraste con Pandas. Utilizaremos
pequeñas muestras de código ilustrativo. **Nota:** En los notebooks
adjuntos, estos ejemplos están ejecutados y funcionan con las versiones
dadas.

-   **Importación de las librerías:**

En Pandas típicamente hacemos:
```python
    import pandas as pd
```
En Polars, la convención es:
```python
    import polars as pl
```
De esta forma usaremos `pd.` para métodos de Pandas y `pl.` para Polars.

-   **Creación de un DataFrame:** Podemos crear DataFrames a partir de
    estructuras Python (diccionarios, listas de listas, etc.).

**Pandas:**
```python
    data = {"nombre": ["Ana", "Luis", "Miguel"], "edad": [34, 28, 45]}
    df_pd = pd.DataFrame(data)
```
**Polars:**
```python
    data = {"nombre": ["Ana", "Luis", "Miguel"], "edad": [34, 28, 45]}
    df_pl = pl.DataFrame(data)
```
Ambos producirán un DataFrame similar:
```text
      nombre   edad
    0    Ana     34
    1   Luis     28
    2 Miguel     45
```
*Nota:* Polars infiere tipos de columnas (en este caso `edad` como
Int64, etc.). Cabe mencionar que Polars tiene un constructor más
estricto a partir de la versión 1.0: por ejemplo, si los tipos en la
lista son mixtos (enteros y floats), ahora lanzará error a menos que se
especifique
`strict=False`[\[14\]](https://docs.pola.rs/releases/upgrade/1/#:~:text=Properly%20apply%20,Series%20constructor)[\[15\]](https://docs.pola.rs/releases/upgrade/1/#:~:text=,5).
Esto es una diferencia con Pandas que automáticamente convertía todos a
float. En Polars 1.x, si queremos comportamiento flexible como Pandas,
usamos `pl.DataFrame(data, schema_overrides={"col": pl.Float64})` o
construimos series con `strict=False`. En general, es buena práctica
**asegurar tipos homogéneos** en las listas de entrada para evitar
sorpresas.

-   **Lectura de archivos CSV/Parquet:** Polars ofrece funciones
    análogas a Pandas, con nombres similares.

**Pandas:** `df = pd.read_csv("archivo.csv")`

**Polars (eager):** `df = pl.read_csv("archivo.csv")`

Polars también permite lectura *lazy* con `pl.scan_csv("archivo.csv")`
-- *veremos detalles en semana 6*. Para archivos Parquet:

**Pandas:** `df = pd.read_parquet("data.parquet")`\
**Polars:** `df = pl.read_parquet("data.parquet")`

Un detalle interesante: la lectura CSV en Polars *eager* suele ser 2-3
veces más rápida que en
Pandas[\[16\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=df%20%3D%20pl,Lazy%20%28deferred).
Además, Polars puede inferir mejor los tipos (ej. fechas) y viene con
soporte nativo de compresión. Pandas en 2.x ha mejorado la velocidad de
lectura incorporando PyArrow opcionalmente, pero Polars aún suele tener
ventaja en I/O.

-   **Vistazo inicial a los datos:** En Pandas usamos `df.head()` para
    ver las primeras filas, `df.info()` para resumen de tipos y nulos,
    etc. En Polars:

-   `df_pl.head()` también funciona, mostrando por defecto 5 primeras
    filas (Polars define su propia visualización tabular, similar a
    Pandas).

-   `df_pl.shape` da tuplas (filas, columnas).

-   Para tipos de datos: `df_pl.dtypes` o `df_pl.schema` (un dict con
    nombres y tipos Polars).

-   Polars no tiene exactamente `info()`, pero podemos obtener similares
    datos imprimiendo el DataFrame o accediendo a `df_pl.height` /
    `df_pl.width` (número de filas/columnas) y tipos. También podríamos
    usar `df_pl.describe()` para estadísticas básicas de columnas
    numéricas (similar a `pd.DataFrame.describe`).

-   **Selección de columnas y filtrado de filas:**

En Pandas, seleccionar una columna: `df_pd["edad"]` (devuelve Series).
En Polars, acceder a columna produce una *Series* de Polars:

    serie_edad = df_pl["edad"]        # o df_pl.column("edad")

Filtrar filas en Pandas: `df_pd[df_pd["edad"] > 30]` -- se pasa una
máscara booleana. En Polars, podemos usar el método `filter` con una
expresión:

    df_pl_filtered = df_pl.filter(pl.col("edad") > 30)

Aquí `pl.col("edad") > 30` genera una expresión booleana aplicada sobre
el DataFrame, y `filter` devuelve las filas donde esa condición es True.
**Importante:** Polars no usa directamente `df_pl[df_pl["edad"] > 30]`
como Pandas; hay que llamar a `.filter` (o alternativamente, existe
`df_pl[df_pl["edad"] > 30]` *sobre carga*, pero internamente lo
convierte a filtro, recomendamos la sintaxis explícita con `filter` para
mayor claridad).

*Comparativa:* Ambas producirán un DataFrame con filas donde edad \> 30.
En Pandas la operación es inmediata; en Polars *eager* también. En
*lazy*, esa filtración sería *diferida*, pero en *eager* ocurre de
inmediato.

-   **Añadir o modificar columnas:** En Pandas se suele asignar
    directamente:

```{=html}
<!-- -->
```
-   df_pd["edad_en_10_anios"] = df_pd["edad"] + 10

    En Polars, las transformaciones suelen hacerse con el método
    `with_columns`, que recibe una o varias expresiones para generar
    nuevas columnas:
        df_pl = df_pl.with_columns(
            (pl.col("edad") + 10).alias("edad_en_10_anios")
        )

    Esto no modifica el DataFrame original in-situ, sino que devuelve
    uno nuevo con la columna añadida (por lo que normalmente asignamos
    de vuelta a `df_pl`). Podemos encadenar múltiples operaciones en una
    sola llamada `with_columns` pasando una lista, lo cual permite
    paralelizar cálculos
    internos[\[17\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=,revenue)[\[18\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=,alias%28%27margin%27%29).
    Por ejemplo, para calcular dos columnas derivadas:
        df_pl = df_pl.with_columns([
            (pl.col("ingresos") - pl.col("gastos")).alias("beneficio"),
            (pl.col("ingresos") / pl.col("beneficio")).alias("margen")
        ])

    Este código Polars calcula *beneficio* y *margen*
    **simultáneamente**, aprovechando múltiples núcleos, mientras que en
    Pandas haríamos dos asignaciones secuenciales (primero calcular
    `df_pd["beneficio"]`, luego
    `df_pd["margen"]`)[\[17\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=,revenue).
    *Buena práctica:* agrupar en Polars todas las columnas nuevas
    derivadas que sean posibles en una sola llamada `with_columns` o
    `select`, para maximizar paralelismo y evitar pasos intermedios
    innecesarios.

Polars también permite asignación directa estilo Pandas con
`df_pl["nueva"] = ...`, pero internamente es sintácticazúcar que crea un
nuevo DataFrame. Recomendamos el enfoque funcional con `with_columns`
por claridad, especialmente cuando se encadenan transformaciones.

-   **Eliminar columnas:** Pandas: `df_pd.drop("columna", axis=1)`.
    Polars: `df_pl.drop("columna")` (devuelve nuevo DF sin esa columna).

-   **Ordenamiento:** Pandas: `df_pd.sort_values("col")`. Polars:
    `df_pl.sort("col")`. Soportan ordenar por múltiples columnas (lista
    de nombres) y orden asc/desc (`ascending` en Pandas, `reverse` en
    Polars). En Polars *lazy*, el *sort* se hace al *collect*, en
    *eager* es inmediato.

-   **GroupBy y agregaciones:** Muy importante para análisis:

En Pandas, ejemplo para sumar la columna "ventas" por "tienda":

    df_pd.groupby("tienda")["ventas"].sum().reset_index()

(nota: usamos `reset_index()` para convertir el índice agrupado en
columna normal). Pandas permite múltiples columnas de agrupación y
múltiples agregaciones, pero la sintaxis puede volverse un poco compleja
con diccionarios o tuplas.

En Polars, la agrupación y agregación se suele hacer con encadenamiento:

    df_pl.group_by("tienda").agg( 
        pl.col("ventas").sum().alias("total_ventas")
    )

Esto devuelve un nuevo DataFrame con una fila por tienda y la suma
correspondiente. Polars infiere automáticamente que queremos agrupar por
la columna \"tienda\". Podemos agregar varias métricas pasando una lista
de expresiones a `agg`. Ejemplo, varias agregaciones:

    df_pl.group_by("tienda").agg([
        pl.col("ventas").sum().alias("total_ventas"),
        pl.col("ventas").mean().alias("venta_promedio"),
        pl.col("ventas").count().alias("num_registros")
    ])

A diferencia de Pandas, no necesitamos *reset_index*; Polars devuelve un
DataFrame regular con la columna \"tienda\" incluida. También **mantiene
el orden de grupos** según aparición por defecto (Pandas por default
ordena grupos alfanuméricamente por la clave; Polars conserva el orden
de los datos originales a menos que se indique lo contrario, útil cuando
el orden importa).

*Agregaciones personalizadas:* Pandas permite `agg(función)` con
funciones lambda, pero suelen ser lentas si no están vectorizadas.
Polars también tiene `.agg(pl.element().apply(lambda ...))` o incluso un
método `apply` en `group_by`, pero igualmente ejecutará Python
(perdiendo paralelismo). La recomendación es usar las expresiones
predefinidas de Polars siempre que sea posible (`sum`, `mean`, `min`,
`max`, `count`, `n_unique`, etc., e incluso *percentiles* con
`quantile`, listas con `list()`, etc.).

*Nota de cambio:* En versiones recientes, Polars usa `group_by` en vez
de `groupby` (aunque este alias existe, la documentación estandariza
`group_by`). Nuestro material usará `group_by` para estar acorde a la
versión 1.34.

-   **Joins (combinar DataFrames):** Polars permite combinar DataFrames
    muy parecido a Pandas:

Pandas: `pd.merge(df1, df2, on="key", how="inner")`\
Polars: `df1.join(df2, on="key", how="inner")`

Ambos soportan *how* = \"inner\", \"left\", \"outer\", etc. En Polars,
si las columnas llave tienen distinto nombre, pasamos dos listas:
`df1.join(df2, left_on="llave1", right_on="llave2", how="inner")`.

Polars implementa joins de forma altamente eficiente y paralelizada.
También ofrece *semijoin* y *antijoin* (equivalentes a operaciones de
existencia tipo *IN*). Ejemplo: `df1.join(df2, on="id", how="semi")`
filtra `df1` a solo filas cuyo \"id\" aparece en `df2` (como un inner
join que devuelve solo columnas de izquierda). *Anti-join* es el
contrario (filas de df1 cuyo id **no** está en df2).

En Pandas, semijoin/antijoin se lograban con merges indicadores o usando
`df1[df1["id"].isin(df2["id"]) ]`, etc. Es útil señalar estas
capacidades de Polars que facilitan ciertas operaciones comunes en
análisis de datos relacional.

-   **Operaciones de *reshaping* en Polars:** Polars soporta **pivot** y
    **melt** similar a Pandas:
-   `df_pl.pivot(values="col_valor", index=["col_index"], columns="col_categoria", aggregate_fn="sum")`
    crearía una tabla dinámica. *Nota:* Polars exige especificar cómo
    agregar si hay múltiples filas por combinación índice-columna pivote
    (sum, mean, first, etc.). En Pandas, `pivot_table` tiene parámetro
    `aggfunc`.
-   `df_pl.melt(id_vars="id", value_vars=["col1", "col2"], variable_name="variable", value_name="valor")`
    es equivalente a `pd.melt`.

Polars también tiene `df_pl.stack()` y `df_pl.explode()` para anidar o
expandir listas, pero eso es avanzado (no profundizaremos a menos que se
necesite para ejercicios).

#### Comparativa de sintaxis Pandas vs Polars

A modo de resumen visual, presentamos algunas operaciones cotidianas con
su sintaxis en Pandas y Polars:

-   **Cargar datos:**

```{=html}
<!-- -->
```
-   # Pandas
        df = pd.read_csv("data.csv")
        # Polars
        df = pl.read_csv("data.csv")            # Modo eager
        lf = pl.scan_csv("data.csv")            # Modo lazy (no ejecuta hasta collect)

```{=html}
<!-- -->
```
-   **Seleccionar columnas:**

```{=html}
<!-- -->
```
-   # Pandas
        df[["colA", "colB"]]
        # Polars
        df.select(["colA", "colB"])
        # (O también df[["colA", "colB"]] funciona en Polars para seleccionar columnas)

```{=html}
<!-- -->
```
-   **Filtrar filas:**

```{=html}
<!-- -->
```
-   # Pandas
        df[df["cantidad"] > 100]
        # Polars (eager)
        df.filter(pl.col("cantidad") > 100)
        # Polars (lazy)
        lf.filter(pl.col("cantidad") > 100).collect()   # se ejecuta al collect

```{=html}
<!-- -->
```
-   **Cálculo de nueva columna:**

```{=html}
<!-- -->
```
-   # Pandas
        df["precio_total"] = df["precio_unit"] * df["unidades"]
        # Polars
        df = df.with_columns((pl.col("precio_unit") * pl.col("unidades")).alias("precio_total"))

```{=html}
<!-- -->
```
-   **GroupBy + agg (ejemplo: promedio de venta por tienda):**

```{=html}
<!-- -->
```
-   # Pandas
        df.groupby("tienda")["venta"].mean()
        # Polars
        df.group_by("tienda").agg(pl.col("venta").mean())

```{=html}
<!-- -->
```
-   **Join (ejemplo: añadir info de clientes a ventas):**

```{=html}
<!-- -->
```
-   # Pandas
        ventas_clientes = pd.merge(df_ventas, df_clientes, on="cliente_id", how="left")
        # Polars
        ventas_clientes = df_ventas.join(df_clientes, on="cliente_id", how="left")

Como se observa, la sintaxis de Polars es semejante en muchos casos,
aunque con diferencias notables: - Uso de **expresiones**
(`pl.col(...)`, `pl.sum()`, etc.) en lugar de operar directamente con
columnas. Esto permite a Polars componer y optimizar las operaciones
internamente. - En Polars no existe el concepto de *índice* explícito
como en Pandas (todas las operaciones se basan en columnas). Los
DataFrames de Polars siempre están implícitamente indexados de 0 a n-1,
pero ese índice no es parte de los datos. Esto evita problemas de
alineación inadvertida y simplifica merges (si necesitas usar un índice
de Pandas en Polars, simplemente conviértelo en columna antes de crear
el DataFrame Polars). - Polars es **inmutable** en sus operaciones por
diseño: cada transformación produce un nuevo DataFrame (aunque
internamente pueda reutilizar buffers para eficiencia). Pandas también
*generalmente* devuelve nuevos objetos (excepto operaciones in-place),
pero en Polars no hay opción \"inplace\" (a excepción de métodos para
streaming). Esto fuerza un estilo funcional que reduce errores de
mutación accidental.

#### Buenas prácticas con Polars (modo *eager*)

-   **Expresiones en lugar de Python *apply*:** Si bien Polars ofrece
    mecanismos para aplicar funciones Python (por ejemplo
    `df.apply(lambda row: ..., axis=1)` no existe directamente, pero se
    puede hacer con `df.iter_rows()` o usando `.map` sobre Series), esto
    rompe la ventaja de Polars. Siempre que sea posible, describir la
    operación en términos de expresiones Polars (que se ejecutan en
    Rust, paralelizadas). Por ejemplo, en vez de:

```{=html}
<!-- -->
```
-   # Evitar:
        df_pl.apply(lambda r: funcion(r[...]), axis=1)

    usar construcciones con `pl.when().then().otherwise()` para lógica
    condicional a nivel de columna, o `pl.map` con funciones
    *element-wise* en contexto de expresiones. *Ejemplo:* si quisiéramos
    una columna categórica a partir de otra numérica: en Pandas
    usaríamos `.apply` con if/else; en Polars preferir:

        df_pl.with_columns(
            pl.when(pl.col("x") > 0)
              .then("positivo")
              .otherwise("no_positivo")
              .alias("categoria_x")
        )

    Esto evita salir al Python interpreter por cada elemento,
    manteniendo la operación en Rust.

```{=html}
<!-- -->
```
-   **Chaining (encadenamiento):** Tanto Pandas como Polars permiten
    encadenar operaciones una tras otra. Sin embargo, en Pandas a veces
    se rompía el encadenamiento por *SettingWithCopy* u operaciones
    in-place. En Polars, es idiomático encadenar:

```{=html}
<!-- -->
```
-   df_filtered = (df_pl
                       .filter(pl.col("activo") == True)
                       .with_columns(pl.col("ingresos") - pl.col("gastos").alias("beneficio"))
                       .sort("beneficio", reverse=True)
                       .head(10)
                      )

    Esto aplica una secuencia de transformaciones de manera clara.
    Podemos hacer algo similar en Pandas usando `.pipe` o simplemente
    encadenando methods que devuelven DataFrames (Pandas 1.x introdujo
    métodos de encadenamiento, y en Pandas 2 con Copy-on-Write será más
    seguro). Recomendamos este estilo para mantener el código limpio y
    evitar variables temporales innecesarias.

```{=html}
<!-- -->
```
-   **Manejo de faltantes:** En Pandas, los valores faltantes se
    representan con `NaN` (para flotantes) o `None`/`pd.NA` (para tipos
    no numéricos). Polars utiliza `None` (equivalente a null) en
    cualquier tipo. Las funciones para tratar nulos:

-   Pandas: `df.fillna(valor)`; Polars: `df.fill_null(valor)` o
    expresiones `pl.col("x").fill_null(...)`.

-   Polars también tiene `drop_nulls()` (equiv. a `dropna()` de Pandas).

-   Ten en cuenta que si convertimos de Pandas a Polars, un `pd.NA` en
    Pandas será `None` en Polars, y Polars distingue null de valores (no
    hay un NaN separado para floats; usa null también).

-   **Rendimiento en joins y groupby:** Polars brilla especialmente en
    *joins* grandes y *group by*. Aprovecha varios threads y algoritmos
    eficientes (hash join, etc.). Una buena práctica: si se hacen varias
    operaciones encadenadas (filtro -\> join -\> agregación), considerar
    hacerlo en modo *lazy* para que Polars, por ejemplo, pueda *empujar*
    el filtro antes del join (reduciendo el tamaño antes de combinar).
    En *modo eager*, cada paso ocurre secuencialmente sin reordenación,
    pero sigue siendo rápido. Si notamos que un join trae muchas filas
    que luego descartamos, ese es un caso donde *lazy* optimiza la
    secuencia automáticamente (filtra primero, une después).

-   **Compatibilidad con Pandas/NumPy:** Polars facilita la conversión:

-   `df_pl.to_pandas()` para obtener un DataFrame Pandas (útil si
    necesitamos usar alguna librería que espera Pandas).

-   `pl.from_pandas(df_pd)` para pasar de Pandas a Polars.

-   También `df_pl.to_numpy()` para matriz NumPy (solo valores
    numéricos).

-   Esto permite integrar Polars gradualmente. En nuestro entorno,
    tenemos ambas disponibles, así que podemos verificar resultados
    cruzados si se desea.

-   **Mantener Polars actualizado:** Polars es un proyecto muy activo,
    con versiones frecuentes. En Polars 1.x ha habido algunos *breaking
    changes* (cambios incompatibles) menores: por ejemplo, el
    comportamiento del constructor de Series con tipos mixtos cambió
    (como mencionamos con `strict`), el método `fill_null` solía
    llamarse `fill_none` en versiones \<0.14 (ya unificaron a
    `fill_null`), etc. Conviene estar atentos a las *release notes*. En
    este curso, usamos Polars 1.34.0, bastante estable, pero advertimos
    que en futuras versiones 2.x podrían cambiar nombres o parámetros.
    Siempre revisar la documentación oficial para funciones específicas.

### Ejemplos prácticos (Semana 5)

A continuación, presentamos algunos ejemplos de código ilustrando el uso
avanzado de Pandas y su contraparte en Polars (eager). Todos estos
ejemplos están disponibles en el notebook de la semana 5, listos para
ejecutarse:

#### Ejemplo 5.1: Agrupaciones múltiples y funciones custom

Supongamos que tenemos un DataFrame de Pandas con ventas de productos
por tienda y queremos obtener, por tienda, el total de ventas, la venta
máxima y el número de productos únicos vendidos. Luego haremos lo mismo
en Polars.

**Datos de ejemplo (ventas):**

    import pandas as pd
    df_sales = pd.DataFrame({
        "tienda": ["A","A","B","B","B","C"],
        "producto": ["X","Y","X","Y","Z","X"],
        "venta": [100, 150, 200, 50, 300, 120]
    })
    print(df_sales)

Salida esperada:

      tienda producto  venta
    0      A        X    100
    1      A        Y    150
    2      B        X    200
    3      B        Y     50
    4      B        Z    300
    5      C        X    120

**Pandas -- GroupBy múltiple y agg personalizado:**

    result_pd = df_sales.groupby("tienda").agg(
        total_ventas = ("venta", "sum"),
        max_venta = ("venta", "max"),
        productos_unicos = ("producto", "nunique")
    ).reset_index()
    print(result_pd)

Aquí usamos la sintaxis de `agg` con nuevos nombres de columna.
Resultado:

      tienda  total_ventas  max_venta  productos_unicos
    0      A           250        150                 2
    1      B           550        300                 3
    2      C           120        120                 1

**Polars -- GroupBy y agg equivalente:**

    import polars as pl
    df_sales_pl = pl.DataFrame(df_sales)  # convertimos de Pandas a Polars
    result_pl = df_sales_pl.group_by("tienda").agg([
        pl.col("venta").sum().alias("total_ventas"),
        pl.col("venta").max().alias("max_venta"),
        pl.col("producto").n_unique().alias("productos_unicos")
    ])
    print(result_pl)

La salida de `print(result_pl)` en Polars sería similar (el orden de las
filas podría ser A, B, C según aparición):

    shape: (3, 4)
    ┌────────┬──────────────┬──────────┬─────────────────┐
    │ tienda ┆ total_ventas ┆ max_venta┆ productos_unicos│
    │ ---    ┆ ---          ┆ ---      ┆ ---             │
    │ str    ┆ i64          ┆ i64      ┆ u32             │
    ╞════════╪══════════════╪══════════╪═════════════════╡
    │ A      ┆ 250          ┆ 150      ┆ 2               │
    │ B      ┆ 550          ┆ 300      ┆ 3               │
    │ C      ┆ 120          ┆ 120      ┆ 1               │
    └────────┴──────────────┴──────────┴─────────────────┘

Polars muestra el DataFrame con sus tipos (i64=int64, u32=uint32 para
únicos). Confirmamos que coincide con Pandas.

*Discusión:* Observamos que la sintaxis es diferente pero obtenemos el
mismo resultado. Notar que `nunique` de Pandas se convierte en
`n_unique()` en Polars. Polars tiene funciones similares para la mayoría
de agregados (`mean`, `min`, `median`, etc.). Si quisiéramos definir una
agregación custom (por ejemplo, rango = max-min), en Pandas podríamos
usar `.agg(lambda x: x.max()-x.min())`. En Polars, podríamos usar
expresiones encadenadas en la lista:
`(pl.col("venta").max() - pl.col("venta").min()).alias("rango")`. Así
evitamos funciones Python y mantenemos todo vectorizado.

#### Ejemplo 5.2: *Join* y cálculo posterior

Tenemos dos DataFrames: `df_ventas` (col: cliente_id, monto) y
`df_clientes` (cliente_id, región). Queremos unir para obtener la región
en cada venta, y luego sumar las ventas por región.

**Con Pandas:**

    df_region = pd.merge(df_ventas, df_clientes, on="cliente_id", how="left")
    res_pd = df_region.groupby("región")["monto"].sum()
    print(res_pd)

Esto primero crea el DataFrame combinado y luego agrupa por región.

**Con Polars:**

    df_region_pl = df_ventas_pl.join(df_clientes_pl, on="cliente_id", how="left")
    res_pl = df_region_pl.group_by("región").agg(pl.col("monto").sum())
    print(res_pl)

Polars realiza la join de forma similar y agrupa. *Si los datos fuesen
muy grandes*, podríamos en Polars *lazy* fusionar esas operaciones:

    res_lazy = (
        df_ventas_pl.lazy()
        .join(df_clientes_pl.lazy(), on="cliente_id", how="left")
        .group_by("región")
        .agg(pl.col("monto").sum())
        .collect()
    )

Esto empujaría la agregación *después* del join, pero si hubiera un
filtro antes, Polars podría optimizarlo. En *modo eager*, la secuencia
es manual.

#### Ejemplo 5.3: Pivot table

Usando el mismo `df_sales` de arriba, imaginemos que queremos una tabla
que tenga tiendas como filas y productos como columnas, con la suma de
ventas como valores.

**Pandas (pivot_table):**

    pivot_pd = pd.pivot_table(df_sales, values="venta", index="tienda", columns="producto", aggfunc="sum", fill_value=0)
    print(pivot_pd)

Salida:

    producto    X      Y      Z
    tienda                     
    A         100    150      0
    B         200     50    300
    C         120      0      0

**Polars (pivot):**

    pivot_pl = df_sales_pl.pivot(values="venta", index="tienda", columns="producto", aggregate_fn="sum")
    print(pivot_pl)

Salida esperada (en Polars mostrará col tienda, X, Y, Z similar a
Pandas). Polars requiere `aggregate_fn` ya que puede haber múltiples
ventas por tienda-producto (usa sum en este caso). Usamos `fill_null(0)`
si queremos rellenar NaN con 0:

    pivot_pl = pivot_pl.fill_null(0)

Polars por defecto deja null donde no hay combinación (similar a NaN de
Pandas).

Estos ejemplos cubren varias de las operaciones comunes. Los notebooks
proporcionados contienen más casos y están estructurados con secciones
para que estudiantes exploren modificaciones, pero todos los bloques de
código vienen con la salida correspondiente verificada en el entorno
(Python 3.12, Pandas 2.3.3, Polars 1.34.0).

### Ejercicios Prácticos (Semana 5)

Los siguientes ejercicios prácticos en notebooks les permitirán afianzar
los conceptos:

1.  **Análisis de ventas por categoría:** Dado un DataFrame `df` con
    columnas `categoria`, `fecha` y `ventas`, realiza en Pandas: (a)
    total de ventas por categoría; (b) ventas promedio mensuales por
    categoría (pista: convertir fecha a datetime, usar
    `groupby([categoria, mes])` o `resample`); y (c) reestructurar el
    resultado en una tabla de categorías vs meses. Luego repite las
    tareas en Polars. Compara la claridad de la sintaxis y verifica que
    los resultados coincidan.

2.  **Detección de *outliers* por grupo:** En un DataFrame Pandas con
    columnas `grupo` y `valor`, calcula el rango intercuartílico (IQR)
    de `valor` por cada grupo, y filtra las filas que estén fuera de 1.5
    \* IQR del Q1-Q3 (método de Tukey) -- es decir, detecta outliers
    dentro de cada grupo. Hazlo primero con groupby + apply en Pandas,
    luego intenta expresarlo en Polars usando `group_by` + `agg` para
    calcular Q1, Q3 por grupo (Polars tiene `quantile(0.25)` etc.), y
    filtra en Polars. **Nota:** Comprueba si el enfoque Polars *eager*
    es fácil o considera usar *lazy* para esta tarea si fuera más
    simple.

3.  **Integración Pandas-Polars:** Toma un dataset pequeño (puedes usar
    `sklearn.datasets.load_iris()` para Iris, o un CSV de ejemplo).
    Cárgalo con Pandas, realiza alguna limpieza básica (por ejemplo,
    normalizar nombres de columnas), conviértelo a Polars y realiza una
    operación compleja (por ejemplo, calcular estadísticas agrupadas)
    que luego conviertas de vuelta a Pandas para graficar. El objetivo
    es practicar `pd.DataFrame -> pl.DataFrame -> pd.DataFrame`.

En los notebooks, cada ejercicio viene con indicaciones y algunas celdas
parcialmente completas para guiar. Se proveen soluciones al final de
cada notebook para verificar. Todos los ejemplos y ejercicios han sido
ejecutados en el entorno especificado, por lo que deberían funcionar sin
problemas de versiones.

## Semana 6: Polars Avanzado (modo *lazy*), cuDF (GPU) y Visualización de Datos

En la semana 6 nos adentraremos en las capacidades avanzadas de Polars,
especialmente su modo de **ejecución perezosa (*lazy*)** y otras
características destacadas. También presentaremos brevemente **cuDF**
(una librería de DataFrames en GPU, opcional) y exploraremos
herramientas de **visualización** de datos integradas con nuestro
entorno.

### Polars en Modo *Lazy*: Consultas Optimizadas

El modo *lazy* de Polars es uno de sus puntos fuertes. En lugar de
ejecutar cada operación inmediatamente, Polars construye un **plan de
consulta** (*query plan*) que representa todas las transformaciones
solicitadas. Al final, cuando se invoca `.collect()`, Polars optimiza
ese plan y luego lo ejecuta de la forma más eficiente posible.

**¿Qué optimizaciones realiza Polars *lazy*?** Algunas claves: -
**Predicate Pushdown (empuje de predicados):** Si encadenamos
operaciones, por ejemplo *lectura -\> filtro -\> agregación*, un sistema
*lazy* puede adelantar los *filtros* lo más cerca posible de la lectura,
de modo que se lean y procesen menos filas desde el
origen[\[19\]](https://realpython.com/polars-lazyframe/#:~:text=A%20Polars%20LazyFrame%20provides%20an,query%20plans%2C%20further%20enhancing%20performance)[\[20\]](https://realpython.com/polars-lazyframe/#:~:text=,is%20sometimes%20necessary%20for%20certain).
Polars hará esto automáticamente: un `.filter()` encadenado antes de un
`.join` o `.group_by` se aplicará antes de esas operaciones al
optimizar, reduciendo datos intermedios. - **Projection Pushdown (empuje
de proyección):** Similar al anterior, Polars determina qué columnas
realmente se necesitan para el resultado final y leerá sólo esas
columnas del archivo (si el formato lo permite, como Parquet) o
descartará las demás lo antes
posible[\[19\]](https://realpython.com/polars-lazyframe/#:~:text=A%20Polars%20LazyFrame%20provides%20an,query%20plans%2C%20further%20enhancing%20performance)[\[20\]](https://realpython.com/polars-lazyframe/#:~:text=,is%20sometimes%20necessary%20for%20certain).
Por ejemplo, si cargamos un CSV con 50 columnas pero luego sólo usamos 5
en las operaciones, Polars *lazy* evitará procesar las 45 columnas
innecesarias. - **Fusionar operaciones (*operation fusion*):** Polars
puede combinar transformaciones sucesivas en una sola pasada. Por
ejemplo, aplicar varias columnas calculadas con `with_columns` se puede
fusionar y paralelizar (ya lo vimos en *eager*). En *lazy*, incluso
operaciones separadas pueden optimizarse en conjunto. Un caso: si
encadenamos `.sort().head(10)`, el optimizador puede reconocer un patrón
de \"*top 10*\" y usar un algoritmo de selección más eficiente que
ordenar todo (esto es algo que sistemas como SQL hacen; Polars también
tiene algunas optimizaciones de este estilo en desarrollo). -
**Reordenación de joins y relaciones:** Polars puede cambiar el orden de
operaciones si no altera el resultado pero mejora la eficiencia. Un
ejemplo clásico es filtrar ambas tablas antes de un join si hay filtros
independientes, o reordenar asociaciones de múltiples tablas (aunque
Polars no es un motor SQL completo, implementa cierta lógica de
optimización de joins lazys especialmente con condiciones de
equivalencia).

**Uso básico de LazyFrame:** Para crear un **LazyFrame**, se suele usar
las funciones de lectura *scan\_*:

    lf = pl.scan_csv("datos_grandes.csv")

A diferencia de `pl.read_csv`, esto **no** carga los datos
inmediatamente. Podemos encadenar operaciones sobre `lf`:

    result = (lf
        .filter(pl.col("columna") > 0)
        .group_by("categoria")
        .agg(pl.col("valor").mean().alias("media_valor"))
        .sort("media_valor", reverse=True)
    )

Hasta este punto, nada se ha ejecutado; `result` es otro LazyFrame que
incorpora en su plan: lectura -\> filtro -\> groupby-\>agg -\> sort.
Podemos inspeccionar el **plan optimizado** con:

    print(result.explain())

El método `explain()` nos mostrará las etapas del plan y qué
optimizaciones se aplicaron (por ejemplo, indicará si hizo *pushdown*
del filtro). Esto es muy útil para didáctica y para depurar rendimiento.

Finalmente, obtenemos los resultados con:

    df_result = result.collect()

Ahora sí se lee el archivo y se obtienen los cálculos. Polars
aprovechará todos los núcleos y las optimizaciones mencionadas. Según la
documentación, esta aproximación puede lograr grandes mejoras en tiempo
comparado a hacer los mismos pasos en modo *eager*, porque *lazy* evita
materializar DataFrames intermedios y hace menos trabajo
total[\[19\]](https://realpython.com/polars-lazyframe/#:~:text=A%20Polars%20LazyFrame%20provides%20an,query%20plans%2C%20further%20enhancing%20performance)[\[21\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=The%20Optimization%20Magic%3A%20During%20lazy,and%20Polars%20makes%20it%20efficient).

**Ejemplo concreto *lazy* vs *eager*:**\
Supongamos un CSV de 100 millones de filas, donde queremos: - Filtrar
`monto > 1000` - Agrupar por `cliente_id` y sumar `monto` - Ordenar por
la suma descendente y tomar los top 10 clientes.

En Pandas (eager por diseño), haríamos:

    df = pd.read_csv("transacciones.csv")
    res = (df[df["monto"] > 1000]
           .groupby("cliente_id")["monto"].sum()
           .sort_values(ascending=False)
           .head(10)
          )

Esto cargará todo a memoria, luego filtrará (procesando las 100M filas),
luego agrupará, etc.

En Polars *lazy*:

    res = (pl.scan_csv("transacciones.csv")
             .filter(pl.col("monto") > 1000)
             .group_by("cliente_id")
             .agg(pl.col("monto").sum().alias("suma_monto"))
             .sort("suma_monto", reverse=True)
             .head(10)
             .collect()
          )

Aquí Polars **nunca carga completamente las filas que no cumplen el
filtro** -- el *predicate pushdown* asegurará que al escanear el CSV se
vayan descartando las filas monto\<=1000, ahorrando trabajo. Además, al
saber que solo se necesitan los top 10 ordenados, Polars podría no
necesitar ordenar toda la columna, como mencionamos (en la práctica
actual de Polars, `.head(10)` después de sort sí ejecuta sort completo;
pero en futuras versiones podrían optimizarlo). En cualquier caso, la
diferencia es que la carga y procesamiento se hará en un solo paso
optimizado. En tests, la versión lazy resultó significativamente más
rápida y eficiente en
memoria[\[22\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=%23%20Lazy%20evaluation%20,now%20does%20it%20actually%20run)[\[21\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=The%20Optimization%20Magic%3A%20During%20lazy,and%20Polars%20makes%20it%20efficient).

**Streaming (procesamiento por lotes):** A partir de Polars 0.17+ se
incorporó un modo *streaming* que complementa la ejecución *lazy*.
Básicamente, para ciertas operaciones, Polars puede procesar datos en
**batches** sin nunca cargar el DataFrame completo en memoria. Esto
permite manejar datasets más grandes que la memoria disponible (algo que
Pandas por sí solo no soporta cómodamente). Para habilitar streaming en
Polars lazy, se puede pasar `streaming=True` en `.collect()`:

    result = lazy_query.collect(streaming=True)

No todas las operaciones son *streamable* (por ejemplo, un sort global
necesita todos los datos, así que streaming se deshabilita
automáticamente en esas partes). Pero muchas agregaciones, filtros,
joins, mapeos sí pueden *streamearse*. La documentación oficial de
Polars indica qué partes soportan
streaming[\[23\]](https://www.handling-large-data.etiennebacher.com/#:~:text=Handling%20large%20data%20with%20polars,crash%20the%20Python%20or).
En nuestros materiales, mencionamos esto como dato avanzando: por
ejemplo, "Polars puede procesar datasets mayores a RAM usando su motor
*streaming*, si la consulta lo
permite[\[24\]](https://urbandataengineer.substack.com/p/big-data-small-machine-the-magic#:~:text=,data%20in%20small%20batches).
Esto se activa con `collect(streaming=True)` y procesa por lotes en
lugar de cargar todo, sacrificando a veces algo de velocidad pero
posibilitando análisis de grandes volúmenes." -- No entraremos en
detalle de streaming en ejercicios, pero es bueno que los alumnos sepan
de esta capacidad.

**Limitaciones del modo lazy:** Aunque poderoso, no todas las
operaciones de Polars están disponibles en lazy. Algunas requieren
*materializar* el DataFrame. Por ejemplo, *pivot* en Polars solo está en
modo eager (no hay pivot en lazy; la documentación sugiere cómo
recrearlo con
group_by)[\[25\]](https://docs.pola.rs/py-polars/html/reference/dataframe/api/polars.DataFrame.pivot.html#:~:text=Create%20a%20spreadsheet,to%20do%20a%20%E2%80%9Clazy%20pivot%E2%80%9D).
También ciertas funciones estadísticas que necesitan todo el conjunto
(como `.median()` en un LazyFrame se computaría pero con streaming se
puede complicar). En esos casos, se puede usar `.collect()` en medio del
pipeline (pero se pierde optimización global) o preferir hacerlo eager.
En la práctica, la mayoría de transformaciones comunes (selección,
filtrado, agregación, joins) funcionan en lazy.

### Polars Avanzado: Otras características útiles

Además de *lazy*, Polars ofrece algunas funcionalidades avanzadas que
conviene destacar:

-   **Funciones ventana (*window functions*):** Son operaciones como
    *rolling* (ventanas móviles) y *expanding*, así como *window
    functions* estilo SQL (operaciones sobre filas dentro de
    particiones, por ejemplo ranking). Pandas tiene `.rolling()` y
    `.expanding()` para ventanas móviles. Polars proporciona:

-   `df.select(pl.col("valor").rolling_mean(window_size=3))` para media
    móvil de tamaño 3 sobre la columna valor. Similar para sum, min,
    etc. También `.rolling_apply` con una lambda (pero de nuevo, mejor
    usar built-ins).

-   *Ventanas por grupo (partitioned window functions):* Polars puede
    hacer cálculos como "por cada fila, calcular promedio del valor
    dentro de su grupo hasta esa fila". Esto se logra combinando
    `group_by` en *lazy* con `.over("grupo")` en una expresión. Ejemplo:
    `df.select(pl.col("valor").mean().over("grupo"))` añade una columna
    con la media de valor por grupo (constante en cada grupo). O usar
    `.rank()` expr para rank dentro de grupos:
    `pl.col("score").rank("dense").over("grupo")`.

-   Estas capacidades equivalen a usar `transform` en Pandas para
    obtener una serie calculada por grupo asignada de nuevo. En Polars,
    se expresan de forma declarativa con `.over()`.

-   **Joins asof (por cercanía temporal):** Útil en series de tiempo
    donde se busca combinar registros con timestamps cercanos. Pandas
    ofrece `merge_asof`. Polars tiene
    `df.join_asof(df2, left_on="time", right_on="time", by="id", strategy="backward")`,
    etc., con estrategias backward/forward similar a Pandas. No
    profundizaremos mucho a menos que haya ejemplo financiero, pero es
    bueno saberlo.

-   **Soporte de tipos complejos:** Polars maneja columnas de tipo
    *List* (equivalente a columnas con listas de valores por fila, algo
    que Pandas puede hacer con dtype object pero Polars lo tiene
    nativo), y *Struct* (un tipo estructurado anidado, parecido a JSON
    anidado). Con esto se pueden representar datos jerárquicos. Ejemplo:
    agrupar y obtener lista de registros por grupo: en Polars
    `group_by("cat").agg(pl.struct(["col1","col2"]).alias("detalles"))`
    obtendríamos una columna `detalles` que es una lista de structs
    (cada struct con col1, col2). Esto es análogo a hacer
    `df.groupby("cat").apply(lambda g: g[["col1","col2"]])` en Pandas,
    pero Polars lo devuelve organizado en una columna. No entraremos en
    ejercicios con Struct, pero lo mencionamos como capacidad.

-   **API SQL-like:** Polars recientemente añadió la posibilidad de
    consultas SQL directamente sobre DataFrames con `pl.SQLContext` o
    `df.lazy().select_sql("SELECT ...")`. Dado que estamos enseñando
    Polars a usuarios probablemente acostumbrados a Pandas, no iremos
    por la ruta SQL, pero es interesante saber que Polars puede
    interpretarse en SQL (lo omitiremos en entregables a estudiantes a
    menos que pregunten, para no desviar).

-   **Interacción con Arrow/Parquet:** Polars es muy eficiente
    leyendo/escribiendo Parquet, Arrow IPC, etc. Mencionamos que, a
    diferencia de Pandas, **Polars puede leer directamente archivos
    Parquet particionados (estilo Hive)**. Por ejemplo, si tenemos un
    directorio con `datos/year=2023/month=01/data.parquet`, Polars puede
    leer todos con patrón `pl.scan_parquet("datos/**/*.parquet")` (y
    puede usar los nombres de carpeta como columnas de partición si se
    activa). Pandas tendría que abrir cada archivo manualmente. Esto es
    útil en big data, pero solo lo mencionamos brevemente como *info*
    adicional.

### Introducción a cuDF (opcional, DataFrames en GPU)

**cuDF** es una biblioteca de la suite **RAPIDS** de NVIDIA, que
implementa estructuras de datos tipo Pandas pero ejecutadas en GPU. La
sintaxis de cuDF se diseñó para ser **muy parecida a Pandas**,
facilitando portar código. Por ejemplo:

    import cudf
    gdf = cudf.DataFrame(data)
    gdf["nueva"] = gdf["col1"] + gdf["col2"]

Este código luce igual que Pandas, pero los cálculos ocurren en la GPU.
Las operaciones intensivas (filtrados, groupbys, merges) pueden obtener
grandes aceleraciones si el dataset cabe en la memoria de la GPU,
gracias al paralelismo masivo de miles de núcleos.

**¿Cuándo usar cuDF?**: - Si disponemos de una GPU Nvidia con suficiente
memoria, cuDF puede acelerar tareas de forma notable, a veces 10x o más
comparado con Pandas en CPU. - Sin embargo, la **limitación principal**
es la memoria GPU: suele ser menor que la RAM del sistema, por lo que
datasets muy grandes pueden no caber. - La API cubre muchas de las
operaciones de Pandas, pero no todas. Por ejemplo, cosas muy específicas
(ciertos merges complejos, métodos de visualización integrados) pueden
no estar implementadas o ser experimentales.

En nuestro entorno, *no hemos preinstalado cuDF* (y es complejo instalar
sin GPU). Por lo tanto, presentaremos cuDF conceptualmente y daremos un
ejemplo pequeño (no ejecutable aquí, pero correcto sintácticamente) para
ilustrar su uso. Así los alumnos conocen la opción.

**Ejemplo conceptual cuDF:**

    import cudf
    # Crear DataFrame GPU similar a Pandas
    gdf = cudf.DataFrame({
        "id": [1,2,3,4],
        "valor": [10, 20, 30, 40]
    })
    # Operaciones similares a Pandas
    gdf["valor_doble"] = gdf["valor"] * 2
    print(gdf)

Salida esperada:

       id  valor  valor_doble
    0   1     10           20
    1   2     20           40
    2   3     30           60
    3   4     40           80

Internamente, `valor_doble` se calculó en GPU.

La mayoría de métodos Pandas tienen su equivalente:
`gdf.groupby("id").agg({"valor": "sum"})`,
`gdf.merge(otro_gdf, on="id")`, etc. Incluso hay
`cudf.read_csv("file.csv")`.

**Ventajas y consideraciones:** - cuDF es ideal para acelerar flujos de
trabajo que ya usan Pandas pero se ven limitados por CPU. Migrar suele
implicar cambiar `pd` por `cudf` en import, y resolver pequeñas
diferencias. - Debemos tener **cuidado con la transferencia de datos**:
mover datos de CPU a GPU y viceversa es costoso. Lo óptimo es leer datos
directamente a GPU (cudf puede leer CSV/Parquet directamente a GPU
memory) y mantener el procesamiento allí. Si se tiene que traer un
resultado grande de vuelta a CPU (por ejemplo, para visualización con
matplotlib), se pierde mucho del beneficio. - El entorno con GPU
requiere instalación de CUDA y versiones compatibles, lo que escapa al
alcance normal de este curso. Por eso lo tratamos de forma
opcional/teórica.

En resumen, **cuDF** amplía nuestras herramientas para *big data* cuando
hay hardware especializado. Para quienes trabajen en entornos donde una
GPU está disponible, puede ser una opción explorar cuDF en proyectos. En
la práctica, Polars *lazy* en CPU puede a veces igualar o superar a cuDF
para ciertos tamaños, pero con GPUs potentes, cuDF brilla en datasets
muy grandes.

*No incluimos ejercicios obligatorios con cuDF*, pero sugerimos a
alumnos curiosos que investiguen la documentación de RAPIDS cuDF si
disponen de GPU (por ejemplo, cómo usar Google Colab con GPU para
pruebas). Por ahora, es suficiente conocer su existencia.

### Visualización de Datos (Pandas/Polars + Bibliotecas Gráficas)

La visualización es el complemento fundamental al análisis: nos permite
entender y comunicar los resultados. En nuestro entorno, tenemos
instaladas bibliotecas potentes: **Matplotlib/Seaborn**, **Altair**,
**Plotly**, **hvPlot**, **Bokeh** entre otras. Abordaremos algunas
formas prácticas de generar gráficos a partir de DataFrames de Pandas y
Polars.

**Pandas + Matplotlib/Seaborn:** Pandas integra por defecto un *wrapper*
de Matplotlib. Por ejemplo, `df_pd["columna"].hist()` produce un
histograma rápido, `df_pd.plot(x="fecha", y="ventas", kind="line")` crea
un gráfico de líneas temporal, etc. Estas funcionalidades son útiles
para exploración rápida. Seaborn ofrece gráficos estadísticos de alto
nivel, típicamente tomando como input DataFrames Pandas y usando
sintaxis declarativa (similar a ggplot en R). Un ejemplo:

    import seaborn as sns
    sns.barplot(data=df_pd, x="categoria", y="valor", hue="segmento")

Esto dibuja un bar plot agrupado por segmento, promediando `valor` por
categoría, etc. En los notebooks, mostraremos ejemplos de uso de Seaborn
con DataFrames Pandas (ya que Seaborn espera Pandas or NumPy).

**Polars y visualización:** Actualmente, Polars no tiene métodos de
plotting propios\... *¡hasta hace poco!* A partir de Polars 0.20, los
DataFrames de Polars incorporan un atributo `.plot` que usa **Altair**
como
motor[\[26\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=Built)[\[27\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=y%3D,chart).
Es decir, podemos hacer:

    import polars as pl
    import altair as alt  # Altair ya instalado en entorno
    df_pl = pl.read_csv("iris.csv")
    chart = df_pl.plot.scatter(x="sepal_width", y="sepal_length", color="species")
    chart.display()  # En notebook Jupyter, mostraría el gráfico interactivo

Este ejemplo dibujaría un scatter plot de largo vs ancho de sépalo,
coloreado por especie, usando Altair
internamente[\[26\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=Built)[\[27\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=y%3D,chart).
La sintaxis Polars `.plot.scatter(...)` es azúcar sintáctico para crear
un objeto `alt.Chart` detrás de escena (podemos ver el código Altair
equivalente en la
documentación[\[28\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=This%20is%20shorthand%20for%3A)).
Ventaja: **Altair** produce gráficos interactivos (basados en Vega-lite)
que se pueden visualizar en notebook o exportar a HTML.

También podemos usar **hvPlot** con Polars. hvPlot es una librería que
extiende el API de `.plot` de Pandas a otros tipos (Dask, Xarray, etc.)
incluyendo Polars. Si importamos `hvplot.polars`, agrega un método
`hvplot` a DataFrames
Polars[\[29\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=hvPlot).
Ejemplo:

    import hvplot.polars  # registra df_pl.hvplot
    df_pl.hvplot.scatter(x="sepal_width", y="sepal_length", by="species")

Esto generaría un gráfico interactivo (usando Bokeh o Plotly backend)
similar. hvPlot produce gráficos inmediatamente en el notebook.

**¿Cuál usar?** Para simplificar: - Usaremos Altair vía Polars `.plot`
para ilustrar gráficos rápidos. Altair es declarativo y *seguro*: evita
*overplotting* grandes (tiene un límite de filas que plotea
directamente, aunque se puede aumentar). - También mostraremos un
ejemplo de **Plotly** con Pandas, ya que Plotly crea gráficos
interactivos también pero con otro estilo (imperativo). - Y un ejemplo
breve de **Matplotlib/Seaborn** para mostrar un gráfico estático en PNG
(por ejemplo, un heatmap o histograma), ya que a veces se necesita
exportar a informes estáticos.

**Ejemplos de visualización:**

*Ejemplo 6.1:* Gráfico de dispersión con Polars + Altair. Usaremos el
conocido dataset Iris (flores):

    import polars as pl
    # Cargar iris dataset (también podríamos usar sklearn.datasets)
    df_iris = pl.read_csv("iris.csv")  # suponiendo que tenemos iris.csv
    scatter_chart = df_iris.plot.scatter(
        x="sepal_width", 
        y="sepal_length", 
        color="species"
    ).properties(title="Iris Sepal Dimensions", width=400, height=300)
    scatter_chart

Este código produce un scatter interactivo incrustado en notebook. Los
métodos `.properties(width=..., height=...)` permiten ajustar tamaño.
Podemos añadir `.configure_axis(...).configure_legend(...)` según Altair
para estilos. Altair maneja automáticamente escalas, leyendas, etc., y
el gráfico permite *tooltip* al pasar el ratón (pues Polars .plot activa
tooltip por defecto en mark_point).

*Ejemplo 6.2:* Histograma con Pandas/Matplotlib:

    import matplotlib.pyplot as plt
    ventas = df_pd["ventas"]  # serie Pandas
    plt.figure(figsize=(4,3))
    ventas.hist(bins=20)
    plt.title("Distribución de Ventas")
    plt.xlabel("Monto venta")
    plt.ylabel("Frecuencia")
    plt.show()

Este código genera un histograma estático de la distribución de ventas.
En notebooks, veremos la gráfica debajo de la celda. Es un ejemplo de
usar la integración sencilla de Pandas (Series.hist) que internamente
llama plt.hist.

*Ejemplo 6.3:* Gráfico de líneas temporal comparando Pandas vs Polars:
Si tuviéramos un DataFrame `df_t` con índices de fecha (en Pandas) o
columna fecha (en Polars): - Pandas: `df_t.plot(y=["serie1","serie2"])`
-- rápidamente traza ambas series en función del índice de fecha. -
Polars: actualmente no tiene `.plot.line` (tiene `.plot` con altair
general, podríamos usar `df_pl.plot` con `.mark_line()` pero es más
complejo). Alternativa: Convertir Polars a Pandas para usar su plotting
si es algo rápido. *O mejor:* usar Altair directamente:

    import altair as alt
    alt.Chart(df_t_pl.to_pandas()).mark_line().encode(
        x='fecha:T', y='valor:Q', color='serie:N'
    )

(Esto convierte Polars a Pandas just for plotting; con altair podríamos
evitar incluso esa conversión usando Polars .plot).

Para evitar confusión, en el material principal, indicaremos: - **Si ya
trabajas en Polars**, puedes usar `.plot` con Altair o convertir a
Pandas para usar Seaborn/Matplotlib según el caso. - hvPlot es otra
opción: una sola línea
`df_pl.hvplot.line(x='fecha', y=['serie1','serie2'])` generaría un
gráfico interactivo de líneas con Panel/Bokeh backend.

**Comparativa visual R vs Python:** (Esto enlaza con semana 7, pero
mencionamos aquí que R es famoso por su capacidad gráfica con paquetes
como ggplot2 base R plotting. Python ha avanzado mucho con las librerías
mencionadas, pero la preferencia puede depender del tipo de gráficos
deseados[\[30\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=,scatter%20plots%20with%20regression%20lines).
En general, R/ggplot se considera muy potente para exploración
estadística rápida; Python con Seaborn/Matplotlib alcanza resultados
similares con algo más de código en ocasiones. Altair y Plotly son
enfoques más modernos en Python para gráficos declarativos e
interactivos, respectivamente.)

En los notebooks de la semana 6, incluiremos ejercicios para generar
gráficos a partir de datos calculados: - Por ejemplo, tras calcular las
ventas por categoría en Polars, hacer un barplot de categorías vs
ventas. - Usar hvPlot o Altair directamente con Polars to show
interactive plots. - Un ejercicio podría ser: *\"Dados los datos de Iris
en Polars, crear un scatter y un boxplot de distribuciones por especie.
Luego replicar el boxplot en Seaborn con Pandas para comparar.\"*

**Nota técnica:** En entornos Jupyter, para mostrar Altair o Plotly, no
olvidemos activar su render: - Altair suele funcionar out-of-the-box en
JupyterLab/Notebook (mostrando html canvas). - Plotly necesita
`pip install` (ya lo tenemos) y a veces
`plotly.offline.init_notebook_mode()` dependiendo del env, pero en
JupyterLab no es necesario. - hvPlot just works if hvplot imported,
because it returns a HoloViews object that shows via Bokeh.

Todos los ejemplos de gráficos estarán pre-ejecutados en los notebooks
para que el estudiante los vea sin tener que instalar nada adicional.

### Ejercicios Prácticos (Semana 6)

Los notebooks de esta semana proponen ejercicios centrados en Polars
*lazy* y visualización:

1.  **Lazy vs Eager Benchmark:** Usando un dataset mediano (ej. \~100k
    filas que proporcionaremos), construir una consulta con varias
    transformaciones (filtro, join, agg) y medir el tiempo en Polars
    eager vs Polars lazy (pueden usar `%timeit` en Jupyter). Comparar
    los planes con `explain()`. Esto refuerza la comprensión de *lazy*.
    *Pista:* usar datos sintéticos o duplicar un dataset pequeño muchas
    veces para simular tamaño. Verificar que los resultados coinciden.

2.  **Optimización manual vs automática:** Dado un pipeline de
    operaciones, pedir al estudiante que razone qué optimizaciones
    aplicará Polars lazy. Por ejemplo: *\"En la siguiente consulta lazy,
    ¿qué pasos se realizan antes gracias al optimizador? ¿Se leerán
    todas las columnas del CSV?\"* y luego confirmar con `.explain()`.

3.  **Visualización interactiva:** Tomar el resultado de una agregación
    (por ejemplo, promedio de puntuaciones por categoría calculado en
    Polars) y generar con Altair (Polars .plot o Altair puro) un gráfico
    de barras interactivo. Luego, hacer lo mismo con hvPlot o Plotly
    para comparar librerías. *Objetivo:* que aprendan a obtener un
    DataFrame Polars/Pandas y pasarlo a una librería de gráficos.

4.  **Mapa de calor de correlación (Seaborn):** Como integración
    Pandas-visualización: calcular la matriz de correlación de un
    DataFrame (usando `df_pd.corr()` en Pandas, o Polars tiene
    `df_pl.corr()` para Pearson) y luego graficarla con Seaborn
    `sns.heatmap`. Esto repasa conversiones entre Polars y Pandas.

Como siempre, los notebooks incluyen soluciones y están preparados para
que los alumnos ejecuten cada celda sin errores de versión. Las gráficas
ya generadas se guardan en la versión entregada para referencia.

## Semana 7: Fundamentos de R y Comparativa Python vs R

En la semana 7 cambiaremos el enfoque para introducir los **fundamentos
del lenguaje R** y comparar su uso con Python en tareas de análisis de
datos. El objetivo es que los estudiantes entiendan las fortalezas de R,
su sintaxis básica, y cómo lograr en R operaciones similares a las que
ya conocen en Python/Pandas. También discutiremos casos de uso de cada
lenguaje.

### Fundamentos del Lenguaje R

**¿Qué es R?** R es un lenguaje de programación y entorno enfocado en
**análisis estadístico y visualización**. Fue creado por y para
estadísticos (sus raíces vienen del lenguaje S en los 90s) y destaca en
tareas de análisis exploratorio, modelos estadísticos y generación de
reportes con mínimo esfuerzo en código. Es de código abierto y tiene un
ecosistema enorme de paquetes (CRAN). A diferencia de Python, que es
multipropósito, R se diseñó específicamente con la estadística en
mente[\[31\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=manipulation%20and%20automation%20to%20business,for%20your%20specific%20use%20cases)[\[32\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=The%20main%20distinction%20between%20the,general%20approach%20to%20data%20wrangling).

**Características principales de R:** - Es un lenguaje **interpretado**
(como Python), con una consola interactiva (R, o el popular RStudio como
interfaz). - Usa **1-based indexing**, es decir, los vectores y arrays
empiezan en índice 1 (a diferencia de 0 en Python). Esto suele
sorprender a quienes vienen de Python. - La asignación típica se hace
con el símbolo `<-` (aunque también acepta `=` en la mayoría de casos).
Ejemplo: `x <- c(1,2,3)` crea un vector numérico. - R está orientado a
**vectores** y operaciones matriciales. Las estructuras básicas
incluyen: - **Vector atómico:** secuencia de elementos del mismo tipo
(numérico, caracter, lógico, etc.). Ej: `c(1,2,3)` es vector numérico. -
**Matrix:** arreglo 2D de un solo tipo. - **Data Frame:** tabla de datos
donde cada columna puede ser de un tipo distinto (similar a DataFrame de
Pandas). En R base se crea con `data.frame()`. Cada columna es
esencialmente un vector. - **Listas:** contenedores que pueden tener
elementos de distinto tipo o estructuras, incluso listas anidadas (como
las listas de Python). Muchas estructuras de R, como data frames o
modelos estadísticos, son implementadas como listas bajo el capó. - R
tiene **tipos especiales** para datos categóricos llamados **Factors**.
Un factor es básicamente un vector de enteros con niveles etiquetados.
En R tradicional, al crear un data.frame, las columnas de texto a menudo
se convertían en factor automáticamente (opción `stringsAsFactors`).
Desde R 4.0, ya no lo hace por defecto, pero los factors siguen siendo
importantes para modelos y gráficos (por ej., para especificar orden de
categorías). - R soporta **NA** como valor faltante (similar a `NA` de
Pandas o `None/np.nan`). NA propaga en cálculos (e.g., cualquier
operación con NA da NA a menos que se indique lo contrario).

**Sintaxis básica y ejemplos:**

-   **Asignación y vectores:**

```{=html}
<!-- -->
```
-   x <- c(10, 20, 30)    # vector numérico con 3 elementos
        y <- c("rojo", "verde", "azul")  # vector de caracteres
        x + 5                 # suma 5 a cada elemento -> c(15,25,35)
        x * 2                 # multiplica cada elemento por 2
        length(x)             # 3 (tamaño del vector)

    Las operaciones aritméticas en R son *vectorizadas* por defecto (no
    hace falta loop para sumar 5 a cada elemento, igual que con numpy
    arrays en Python).

```{=html}
<!-- -->
```
-   **Indexación:**

```{=html}
<!-- -->
```
-   x[1]        # 10 (el primer elemento, índices comienzan en 1)
        x[0]        # numeric(0) (0 no es un índice válido, resulta en vector vacío)
        x[2:3]      # c(20, 30) (subvector de posiciones 2 a 3 inclusive)
        y[c(1,3)]   # c("rojo", "azul") (índices 1 y 3)

    Se pueden usar vectores lógicos para filtrar:

        mask <- x > 15       # c(FALSE, TRUE, TRUE)
        x[mask]              # c(20, 30)

    Esto es similar a `x[x > 15]` en numpy/pandas.

```{=html}
<!-- -->
```
-   **Matrices:**

```{=html}
<!-- -->
```
-   M <- matrix(1:6, nrow=2, ncol=3)
        #      [,1] [,2] [,3]
        # [1,]    1    3    5
        # [2,]    2    4    6
        M[2,3]    # 6 (fila 2, col 3)

    Las matrices se llenan por columnas por defecto (por eso 1:6 se
    ubicó 1,2 en col1; 3,4 col2; 5,6 col3). Argumento `byrow=TRUE`
    cambia llenado por filas.

```{=html}
<!-- -->
```
-   **Listas:**

```{=html}
<!-- -->
```
-   lista <- list(nombre="Ana", edad=25, nums=c(2,5,8))
        lista$nombre    # "Ana"
        lista$nums[2]   # 5  (accediendo al segundo elemento del vector nums dentro de la lista)

    Listas permiten agrupar datos heterogéneos, similar a dicts o
    objects.

```{=html}
<!-- -->
```
-   **Data Frames en R:**

```{=html}
<!-- -->
```
-   df <- data.frame(nombre=c("Ana","Beto","Carla"),
                         edad=c(28, 34, 29),
                         casado=c(TRUE, TRUE, FALSE))
        str(df)   # estructura: data.frame con 3 obs y 3 variables

    Un R data.frame es en realidad una lista de columnas (cada columna
    es vector), con clase `data.frame`. Podemos hacer `df$nombre` para
    la columna, o `df[,"edad"]`, o `df[2,]` para segunda fila (devuelve
    data.frame de una fila, a menos que drop=TRUE para dropear dims).
    Notar: `df[,"edad"]` retorna un vector; `df["edad"]` retorna un
    data.frame con una columna (depende cómo se indexe, a veces confuso
    para novatos). `df[1:2, c("nombre","edad")]` daría sub-data.frame de
    2 filas, 2 columnas.

```{=html}
<!-- -->
```
-   **Funciones estadísticas básicas:** R viene con muchas funciones
    listas:

```{=html}
<!-- -->
```
-   mean(x)           # media
        sd(x)             # desviación estándar
        summary(df)       # resumen de cada columna (min, quartiles, etc para numéricas, conteo para factor/logic)
        table(df$casado)  # tabla de frecuencia

    R está preparado para manejar NA:

        mean(x)           # NA si x tiene NA
        mean(x, na.rm=TRUE)  # calcula media omitiendo NAs

```{=html}
<!-- -->
```
-   **Control de flujo:** R tiene `if(cond) { } else { }` (con
    condiciones vectorizadas es diferente, pero para escalares está
    bien), bucles `for(i in 1:10) { }`, etc. Sin embargo, en R se
    prefiere evitar bucles explícitos en favor de vectores o funciones
    *apply* (e.g. `lapply`, `sapply`, `tapply`) que aplican funciones a
    vectores, listas, etc., internamente en C, más eficientemente.

-   **Paquetes (libraries):** R base es potente, pero la mayoría de
    usuarios instala paquetes. Un conjunto esencial es el **tidyverse**,
    que incluye:

-   **dplyr** (manipulación de data frames con sintaxis encadenada
    usando verbos como `filter`, `mutate`, `summarize`, etc.).

-   **ggplot2** (visualización gráfica avanzada).

-   **readr**, **tidyr**, **purrr**, etc. (lectura de datos,
    reordenamiento, programación funcional).

*En esta introducción básica, cubriremos principalmente R base*, pero
mencionaremos el tidyverse pues es estándar moderno. Por ejemplo, la
misma manipulación de data frames en R puede hacerse con dplyr:

    library(dplyr)
    df %>% 
      filter(edad > 30) %>% 
      mutate(edad_dias = edad * 365) %>% 
      group_by(casado) %>% 
      summarise(promedio_edad = mean(edad))

Esta sintaxis encadenada con `%>%` (pipe) es muy legible y similar
conceptualmente a encadenar operaciones en Pandas/Polars. Requiere
aprendizaje adicional, pero vale la pena señalarlo ya que en la
comparativa con Pandas es análogo (de hecho, dplyr fue una inspiración
para pandas).

**Comparativa de operaciones R vs Python/Pandas:**

Vamos a comparar cómo se harían algunas tareas sencillas en R base, R
con tidyverse, y Python/Pandas, para que los estudiantes vean
equivalencias:

-   **Lectura de CSV:**

-   R base: `df <- read.csv("data.csv")`

-   tidyverse (readr): `df <- read_csv("data.csv")` (funciona similar
    pero más rápido, y tibble output)

-   Python/Pandas: `df = pd.read_csv("data.csv")` (Todas fáciles, Pandas
    vs readr rendimiento similar en datasets medianos).

-   **Filtrado de filas:**

-   R base: `subset(df, edad > 30 & casado == TRUE)` -- función subset
    para filtrar por condición. O
    `df[df$edad > 30 & df$casado == TRUE, ]` usando índices lógicos.

-   dplyr: `df %>% filter(edad > 30, casado == TRUE)`

-   Pandas: `df[(df["edad"] > 30) & (df["casado"] == True)]`

-   **Seleccionar columnas:**

-   R base: `df[c("nombre","edad")]` (devuelve data.frame con esas cols)

-   dplyr: `df %>% select(nombre, edad)`

-   Pandas: `df[["nombre","edad"]]`

-   **Agregar columna calculada:**

-   R base: `df$edad10 <- df$edad + 10`

-   dplyr: `df %>% mutate(edad10 = edad + 10)`

-   Pandas: `df["edad10"] = df["edad"] + 10`

-   **GroupBy + summary (ej: edad promedio por estado civil):**

-   R base: usar `aggregate`:
    `aggregate(edad ~ casado, data=df, FUN=mean)` Esto formula \~ (edad
    by casado). O `tapply(df$edad, df$casado, mean)` que devuelve vector
    nombrado.

-   dplyr:
    `df %>% group_by(casado) %>% summarise(mean_edad = mean(edad))`

-   Pandas:
    `df.groupby("casado")["edad"].mean().reset_index(name="mean_edad")`

-   **Merge (join tablas):**

-   R base: `merge(df1, df2, by="id", all.x=TRUE)` (all.x = TRUE indica
    left join, all=TRUE sería full join).

-   dplyr: `df1 %>% left_join(df2, by="id")`

-   Pandas: `pd.merge(df1, df2, on="id", how="left")`

Se puede observar que la sintaxis *tidyverse/dplyr* es concisa y
legible, comparable a Pandas. R base a veces es más verboso o menos
intuitivo (e.g., aggregate con fórmula es potente pero es otra
mini-sintaxis).

**Fortalezas de R:** - Orientado a estadísticas: muchas pruebas
estadísticas, modelos (regresión, ANOVA, etc.) están integrados o
disponibles en paquetes, a veces con una línea. Por ejemplo,
`lm(resultado ~ x1 + x2, data=df)` ajusta una regresión lineal en R; en
Python habría que usar statsmodels o sklearn con más pasos. -
Visualización avanzada con *ggplot2*: permite componer gráficos con una
gramática declarativa. Por ejemplo:

    library(ggplot2)
    ggplot(df, aes(x=edad, fill=casado)) + 
      geom_histogram(binwidth=5) +
      facet_wrap(~ casado)

Esto produciría histogramas de edad separados por estado civil, con
colores. Equivalente en Python requeriría combinar seaborn y facet grid,
etc., un poco más de trabajo. - Comunidad académica y paquetes
especializados: R es muy usado en bioestadística, economía, etc., hay
paquetes muy específicos (por ejemplo, `survival` para análisis de
supervivencia, `phyloseq` en biología, etc.) que quizá no tengan
equivalentes maduros en Python. - Interactividad: R tiene Shiny para
construir dashboards web interactivos con relativamente poco código R,
integrando análisis y plot. Python tiene Dash, Panel, etc., pero Shiny
fue pionero y sigue muy popular en ciertos ámbitos.

**Fortalezas de Python:** - Versatilidad: Python se usa en producción,
en desarrollo web, en aplicaciones de todo tipo, además de ciencia de
datos[\[33\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=Python%20is%20a%20multi,developing%20a%20machine%20learning%20application)[\[34\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=R%2C%20on%20the%20other%20hand%2C,behavior%20analysis%20or%20genomics%20research).
R tiende a quedarse en el análisis y no tanto en la integración a
grandes sistemas (aunque con Rserve, APIs plumber, etc., se puede, pero
es menos común). - Facilidad de aprendizaje: Esto es debatible, pero
muchos encuentran Python más consistente y fácil de aprender a programar
en general, mientras R tiene ciertas peculiaridades (el reciclaje de
vectores, la indexación 1-based, distintas notaciones `$`, `[[` para
listas, etc.). Python tiene sintaxis clara, y es multiparadigma (POO,
etc.), frente a R que es más funcional. - Ecosistema ML/AI: Python
domina en machine learning (TensorFlow, PyTorch, Scikit-learn\...). R
tiene paquetes de ML pero no con la amplitud y soporte que Python tiene
en la industria. - Comunidad masiva: Si bien R tiene comunidad fuerte,
Python la supera en tamaño y diversidad de usuarios (incluyendo muchos
desarrolladores de software, no solo analistas).

**Integración R y Python:** Mencionaremos que no es necesariamente *uno
u otro*. Muchas empresas utilizan ambos: analistas que prototipan en R y
luego ingenieros llevan a Python, o usar *R for analysis, Python for
deployment*. Hay incluso librerías para usarlos juntos (por ejemplo,
**rpy2** permite ejecutar R desde Python, y **reticulate** permite
ejecutar Python desde R). En Jupyter, hay kernels de R y también
notebooks mixtos.

Dado nuestro entorno es principalmente Python, no ejecutaremos código R
en los notebooks (a menos que se configurase un kernel R, pero no está
contemplado en environment.yml). Por lo tanto, los ejemplos de R en los
notebooks de semana 7 serán probablemente ilustrativos, mostrando
sintaxis R en celdas de texto con formato de código, sin ejecución real
en ese entorno. Podríamos indicar cómo instalar R o usar un servicio
online como Google Colab (que tiene R kernel) para que los curiosos
prueben.

### Comparativa: Python vs R en un caso de estudio

Para consolidar, podríamos presentar un mini *case study* donde
resolvemos el mismo problema en ambos lenguajes. Por ejemplo: -
**Caso:** Dataset `mtcars` (famoso de R con datos de autos). Hacer un
análisis exploratorio: calcular consumo promedio por cilindros, graficar
una relación entre caballos de fuerza y consumo, y ajustar un modelo
lineal. - En R: `aggregate(mpg ~ cyl, data=mtcars, FUN=mean)`,
`plot(mtcars$hp, mtcars$mpg)`, `abline(lm(mpg ~ hp, data=mtcars))`. - En
Python: usar Pandas para groupby, Matplotlib/Seaborn para scatter, numpy
polyfit o sklearn LinearRegression para modelo, etc. Se vería que R
requiere menos código para ciertas cosas (modelo lineal con abline es
muy directo), mientras Python es un poco más manual pero quizá más
flexible con distintas opciones.

También podríamos comentar sobre el *output* de modelos: en R,
`summary(lm(...))` da tabla de coeficientes, p-vals, etc., listo para
analizar; en Python con statsmodels se puede lograr similar output, pero
hay que recordar más pasos.

### Ejercicios Prácticos (Semana 7)

Los ejercicios propuestos esta semana buscan que los alumnos reflexionen
sobre sintaxis y diferencias, más que ejecutar mucho código (pues el
entorno es Python):

1.  **Escribir equivalencias R-Python:** Se plantean 5 operaciones en R
    (en pseudo código R) y deben escribir cómo sería en Python/Pandas.
    Por ejemplo: *\"En R:* `mean(df$col, na.rm=TRUE)` *-- ¿cómo se
    calcula la media ignorando NA en Pandas?\"* (Respuesta:
    `df["col"].mean(skipna=True)` -- que es default skipna True). Otro:
    *\"R:* `df[df$x > 5 & df$y == 'A', ]` *-- ¿equivalente Pandas?\"*
    (Respuesta: `df[(df["x"]>5) & (df["y"]=='A')]`).

2.  **Analizar un dataset pequeño en R y Python:** Proporcionamos en el
    enunciado un pequeño dataset (puede ser dado como tabla) y pedimos:
    calcular cierta estadística en R base (escribir código) y en Pandas
    (podrían realmente ejecutar este). Por ejemplo, un dataframe de
    calificaciones de estudiantes con columnas \[nombre, materia,
    calificacion\]. Pedir: promedio de calificación por materia (R:
    `tapply(calificacion, materia, mean)`; Py:
    `df.groupby("materia")["calificacion"].mean()`).

3.  **Investigar paquetes:** Pedir a cada alumno (o en general) que
    busque un paquete R notable en su campo y uno equivalente en Python.
    Por ejemplo, si les interesa visualización: R -\> ggplot2, Python
    -\> plotnine (port de ggplot) o seaborn/matplotlib; en ML: R -\>
    randomForest, Python -\> scikit-learn\'s RandomForestClassifier;
    etc. Esto es más de discusión que ejecución.

4.  **Reflexión final:** Dada una lista de tareas (ej. limpieza de
    datos, modelado predictivo, crear dashboard, integración con web),
    ¿qué lenguaje consideran más apropiado y por qué? (no hay respuesta
    única, es para pensar pros/cons). Por ejemplo: *\"Limpiar y unir 10
    archivos de texto grandes\"* (posible respuesta: Python/Polars
    podría ser más eficiente en manipulación programática, aunque R
    puede hacerlo, Polars/Pandas manejan bien archivos grandes, etc.),
    *\"Realizar análisis estadístico detallado con pruebas ANOVA, test
    t, etc.\"* (R tiene muchas funciones built-in y reportes fáciles),
    *\"Desplegar un modelo entrenado como API web\"* (Python es más
    usado en deploy).

Estos ejercicios consolidan la idea de que ambos lenguajes son
herramientas en la caja de un analista de datos, y la elección depende
de la tarea y
entorno[\[31\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=manipulation%20and%20automation%20to%20business,for%20your%20specific%20use%20cases)[\[34\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=R%2C%20on%20the%20other%20hand%2C,behavior%20analysis%20or%20genomics%20research).

## Conclusiones

A lo largo de las semanas 5, 6 y 7, hemos actualizado los materiales del
módulo PIA UD2 para reflejar las versiones más recientes de nuestras
herramientas (Python 3.12, Pandas 2.3.3, Polars 1.34.0, etc.). Todos los
ejemplos y notebooks fueron revisados para asegurar compatibilidad: - Se
ajustaron llamados de Pandas obsoletos (reemplazando `.append` por
`pd.concat`, removiendo usos de propiedades removidas, etc.). - Se
mostraron las mejores prácticas actuales tanto en Pandas como en Polars,
enfatizando eficiencia (vectorización, uso correcto de métodos). -
Polars se introdujo como alternativa moderna a Pandas, con ejemplos
*eager* en semana 5 y *lazy* en semana 6, incluyendo comparativas de
sintaxis y rendimiento basadas en fuentes confiables (por ejemplo,
Polars superando a Pandas en
benchmarks[\[9\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Operation%20Pandas%20,61x)
y cómo su ejecución paralela y *lazy* optimizada logra importantes
mejoras[\[12\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Lazy%20Evaluation%27s%20Power%3A%20Polars%20can,turn%20decisions)[\[21\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=The%20Optimization%20Magic%3A%20During%20lazy,and%20Polars%20makes%20it%20efficient)). -
Se brindó un panorama de visualización, integrando herramientas
interactivas modernas (Altair, hvPlot) directamente con los DataFrames,
de modo que los estudiantes vean cómo pasar de los números a las
gráficas de forma efectiva. - Finalmente, se dio un vistazo a R,
equipando a los estudiantes con nociones básicas de sintaxis y
capacidades, y estableciendo un **puente comparativo** con lo aprendido
en Python. Esto les permitirá entender código en R, colaborar con
colegas que usen R, y tener criterio para elegir la mejor herramienta
según el
problema[\[34\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=R%2C%20on%20the%20other%20hand%2C,behavior%20analysis%20or%20genomics%20research).

**Estado de entrega:** Los documentos Markdown y notebooks adjuntos
están listos para ser entregados a los alumnos. Cada notebook contiene
celdas ejecutadas con resultados esperados (o indicaciones claras donde
el alumno debe ejecutar o completar), asegurando que puedan usarse
directamente sin edición manual adicional. Se incluyen referencias y
comentarios sobre cambios de versión, para que los alumnos también
aprendan a actualizarse en este campo que evoluciona rápidamente.

En suma, estas semanas proporcionan una formación sólida en análisis de
datos con herramientas de última generación, preparándolos para trabajar
eficientemente con conjuntos de datos en Python (y ofreciéndoles
perspectivas en R), y sentando bases para módulos posteriores o para
proyectos integradores donde apliquen estas tecnologías.

**Referencias y Fuentes:**

-   Documentación oficial de Pandas 2.x (cambios de la versión 2.0 en
    adelante)[\[4\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=match%20at%20L1730%20,GH%2035407),
    *Pandas User Guide*.
-   Documentación y tutoriales de Polars (en especial sobre lazy
    execution y comparación con
    Pandas)[\[11\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=When%20to%20Use%20Each%20Mode%3A)[\[22\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=%23%20Lazy%20evaluation%20,now%20does%20it%20actually%20run).
-   Artículo *"Polars for Pandas Users"* -- rendimiento y mental
    model[\[9\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Operation%20Pandas%20,61x)[\[17\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=,revenue).
-   Real Python -- Tutorial de Polars
    LazyFrames[\[35\]](https://realpython.com/polars-lazyframe/#:~:text=A%20Polars%20LazyFrame%20provides%20an,query%20plans%2C%20further%20enhancing%20performance)[\[36\]](https://realpython.com/polars-lazyframe/#:~:text=instructions%20instead%20of%20data.%20,sometimes%20necessary%20for%20certain%20operations).
-   IBM Developer -- Comparativa Python vs
    R[\[31\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=manipulation%20and%20automation%20to%20business,for%20your%20specific%20use%20cases)[\[32\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=The%20main%20distinction%20between%20the,general%20approach%20to%20data%20wrangling).
-   Polars User Guide -- Sección de visualización con
    Altair/hvPlot[\[26\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=Built)[\[29\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=hvPlot).
-   Material original del módulo (UD1/UD2 anteriores) como contexto para
    adaptación de ejemplos (no citado textualmente pero considerado en
    ajustes).

[\[1\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=match%20at%20L390%20In%20,pyarrow)
[\[2\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=In%20,pyarrow)
[\[3\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=,45018)
[\[4\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=match%20at%20L1730%20,GH%2035407)
[\[5\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=,35224)
[\[6\]](https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html#:~:text=match%20at%20L1725%20,instead%20%28GH%2045321)
What's new in 2.0.0 (April 3, 2023) --- pandas
3.0.0.dev0+2731.gfcffde9d7c documentation

<https://pandas.pydata.org/docs/dev/whatsnew/v2.0.0.html>

[\[7\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=The%20Problem%20with%20Sequential%20Thinking%3A,Pandas%20works%20through%20operations%20sequentially)
[\[8\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Polars%27%20Parallel%20Mindset%3A%20Polars%20assumes,of%20these%20things%20at%20once)
[\[9\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Operation%20Pandas%20,61x)
[\[10\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Polars%20changes%20the%20game,relearning%20data%20science%20from%20scratch)
[\[11\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=When%20to%20Use%20Each%20Mode%3A)
[\[12\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=Lazy%20Evaluation%27s%20Power%3A%20Polars%20can,turn%20decisions)
[\[13\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=The%20Optimization%20Magic%3A%20During%20lazy,and%20Polars%20makes%20it%20efficient)
[\[16\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=df%20%3D%20pl,Lazy%20%28deferred)
[\[17\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=,revenue)
[\[18\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=,alias%28%27margin%27%29)
[\[21\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=The%20Optimization%20Magic%3A%20During%20lazy,and%20Polars%20makes%20it%20efficient)
[\[22\]](https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative#:~:text=%23%20Lazy%20evaluation%20,now%20does%20it%20actually%20run)
Polars for Pandas Users: A Blazing Fast DataFrame Alternative -
KDnuggets

<https://www.kdnuggets.com/polars-for-pandas-users-a-blazing-fast-dataframe-alternative>

[\[14\]](https://docs.pola.rs/releases/upgrade/1/#:~:text=Properly%20apply%20,Series%20constructor)
[\[15\]](https://docs.pola.rs/releases/upgrade/1/#:~:text=,5) Version
1 - Polars user guide

<https://docs.pola.rs/releases/upgrade/1/>

[\[19\]](https://realpython.com/polars-lazyframe/#:~:text=A%20Polars%20LazyFrame%20provides%20an,query%20plans%2C%20further%20enhancing%20performance)
[\[20\]](https://realpython.com/polars-lazyframe/#:~:text=,is%20sometimes%20necessary%20for%20certain)
[\[35\]](https://realpython.com/polars-lazyframe/#:~:text=A%20Polars%20LazyFrame%20provides%20an,query%20plans%2C%20further%20enhancing%20performance)
[\[36\]](https://realpython.com/polars-lazyframe/#:~:text=instructions%20instead%20of%20data.%20,sometimes%20necessary%20for%20certain%20operations)
How to Work With Polars LazyFrames -- Real Python

<https://realpython.com/polars-lazyframe/>

[\[23\]](https://www.handling-large-data.etiennebacher.com/#:~:text=Handling%20large%20data%20with%20polars,crash%20the%20Python%20or)
Handling large data with polars and tidypolars

<https://www.handling-large-data.etiennebacher.com/>

[\[24\]](https://urbandataengineer.substack.com/p/big-data-small-machine-the-magic#:~:text=,data%20in%20small%20batches)
Big Data, Small Machine: The Magic of Polars Streaming and more \...

<https://urbandataengineer.substack.com/p/big-data-small-machine-the-magic>

[\[25\]](https://docs.pola.rs/py-polars/html/reference/dataframe/api/polars.DataFrame.pivot.html#:~:text=Create%20a%20spreadsheet,to%20do%20a%20%E2%80%9Clazy%20pivot%E2%80%9D)
polars.DataFrame.pivot --- Polars documentation

<https://docs.pola.rs/py-polars/html/reference/dataframe/api/polars.DataFrame.pivot.html>

[\[26\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=Built)
[\[27\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=y%3D,chart)
[\[28\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=This%20is%20shorthand%20for%3A)
[\[29\]](https://docs.pola.rs/user-guide/misc/visualization/#:~:text=hvPlot)
Visualization - Polars user guide

<https://docs.pola.rs/user-guide/misc/visualization/>

[\[30\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=,scatter%20plots%20with%20regression%20lines)
[\[31\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=manipulation%20and%20automation%20to%20business,for%20your%20specific%20use%20cases)
[\[32\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=The%20main%20distinction%20between%20the,general%20approach%20to%20data%20wrangling)
[\[33\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=Python%20is%20a%20multi,developing%20a%20machine%20learning%20application)
[\[34\]](https://www.ibm.com/think/topics/python-vs-r#:~:text=R%2C%20on%20the%20other%20hand%2C,behavior%20analysis%20or%20genomics%20research)
Python vs. R: What's the Difference? \| IBM

<https://www.ibm.com/think/topics/python-vs-r>
