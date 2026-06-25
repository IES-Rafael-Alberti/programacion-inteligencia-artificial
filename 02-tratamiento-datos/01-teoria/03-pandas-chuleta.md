# Chuleta de Pandas

## Estructuras de datos básicas
- `pd.Series` – Vector unidimensional etiquetado.
- `pd.DataFrame` – Tabla de datos bidimensional.
- `pd.Index` / `pd.MultiIndex` – Ejes etiquetados para Series/DataFrame.
- `pd.Categorical` – Datos categóricos con vocabulario finito.
- `DatetimeIndex`, `TimedeltaIndex`, `PeriodIndex` – Ejes temporales especializados.

## Creación e importación de datos
- `pd.read_csv`, `pd.read_table`, `pd.read_excel`, `pd.read_json`, `pd.read_html`.
- `pd.read_sql`, `pd.read_parquet`, `pd.read_feather`, `pd.read_clipboard`.
- `pd.DataFrame(data, columns=..., index=...)`, `pd.Series(data, index=...)`.
- `pd.date_range`, `pd.period_range`, `pd.timedelta_range`.

## Inspección y exploración
- `df.head(n)`, `df.tail(n)` – Primeras/últimas filas.
- `df.info()`, `df.describe(include=...)`, `df.dtypes`.
- `df.shape`, `df.index`, `df.columns`, `df.memory_usage()`.
- `df.value_counts(normalize=..., dropna=...)`, `df.nunique()`.

## Selección y filtrado de datos
- Acceso rápido: `df["col"]`, `df.col`, `df[["col1","col2"]]`.
- Filtrado booleano: `df[df["col"] > valor]`, `df.query("col > valor")`.
- Posicional: `df.iloc[fila, columna]`, slicing con enteros.
- Etiquetas: `df.loc["fila", "col"]`, rangos inclusivos con etiquetas.
- `.at`, `.iat` – Acceso escalar rápido por etiqueta/posición.

## Indexación y alineación
- `df.set_index("col", drop=...)`, `df.reset_index(drop=..., inplace=...)`.
- `df.reindex(nuevo_index)`, `df.reindex_like(otro_df)`.
- `df.rename(columns=..., index=..., inplace=...)`.
- `df.sort_index(axis=..., ascending=...)`, `df.sort_values(by=..., ascending=...)`.

## Operaciones aritméticas y estadísticas
- Estadísticos: `df.mean()`, `median()`, `sum()`, `std()`, `var()`, `min()`, `max()`, `quantile()`.
- Cálculos fila/columna: `df.mean(axis=1)`, `df.sum(axis=1)`.
- Operaciones elemento a elemento: `df.add`, `sub`, `mul`, `div`, `pow`, `mod`.
- `df.corr()`, `df.cov()`.
- Métodos acumulados: `df.cumsum()`, `cumprod()`, `cummax()`, `cummin()`.
- `df.eval("nueva_col = col1 + col2")`.

## Gestión de valores faltantes
- Detección: `df.isna()`, `df.notna()`.
- Eliminación: `df.dropna(axis=..., how=..., subset=...)`.
- Relleno: `df.fillna(valor | método, inplace=...)`, `df.interpolate(method=...)`.
- Reemplazo: `df.replace({valor_viejo: valor_nuevo})`.

## Manipulación de columnas y filas
- `df.assign(nueva=...)`, `df["nueva"] = expresión`.
- `df.insert(pos, "col", valores)`, `df.pop("col")`.
- `df.drop(columns=..., index=..., inplace=...)`.
- `df.astype(tipo | {"col": tipo})`, `df.to_numpy()`, `df.clip(lower=..., upper=...)`.
- `df.sample(n=..., frac=..., random_state=...)`.

## Agrupaciones y agregaciones
- `df.groupby(keys, as_index=..., dropna=...)`.
- Agregados: `.agg(func)`, `.agg({"col": ["mean","sum"]})`, `.agg(total=("col","sum"))`.
- Funciones rápidas: `.sum()`, `.mean()`, `.size()`, `.count()`, `.first()`, `.last()`.
- Transformaciones: `.transform(func)`, `.apply(func)`.
- `pd.Grouper(key=..., freq=..., level=...)` para agrupar por fechas o niveles.

## Reorganización y combinaciones
- Concatenar: `pd.concat([df1, df2], axis=..., join=..., ignore_index=...)`.
- Union tipo SQL: `pd.merge(left, right, on=..., how=..., suffixes=...)`.
- Merge por índices: `left.join(right, on=..., how=...)`.
- Apilar/desapilar: `df.stack()`, `df.unstack(level=...)`.
- Pivot: `df.pivot(index=..., columns=..., values=...)`.
- Pivot con agregación: `df.pivot_table(values=..., index=..., columns=..., aggfunc=..., margins=...)`.
- `pd.melt(df, id_vars=..., value_vars=..., var_name=..., value_name=...)`.

## Series temporales y ventana móvil
- Conversión de fechas: `pd.to_datetime`, `df["fecha"].dt.year`, `.dt.month`.
- Resampleo: `df.resample("M").mean()`, `.sum()`, `.agg(...)`.
- Ventanas móviles: `df.rolling(janela).sum()`, `.mean()`, `.apply(func)`.
- Ventanas expansivas: `df.expanding().mean()`.
- Desplazamientos: `df.shift(periods=..., freq=...)`, `df.diff(periods=...)`.

## Aplicación de funciones y utilidades
- `df.apply(func, axis=0/1)`, `df.applymap(func)`, `series.map(func | dict)`.
- `df.pipe(func, *args, **kwargs)` para componer transformaciones.
- `df.where(condición, otro_valor)`, `df.mask(condición, otro_valor)`.
- `pd.cut`, `pd.qcut` para discretizar.
- `df.duplicated(subset=..., keep=...)`, `df.drop_duplicates(...)`.

## Entrada y salida de datos
- Escritura: `df.to_csv(path, index=...)`, `df.to_excel(path, sheet_name=...)`, `df.to_json(...)`, `df.to_sql(...)`, `df.to_parquet(...)`.
- Opciones de compresión: `df.to_csv("archivo.gz", compression="gzip")`.
- Guardar objetos: `df.to_pickle(path)` y cargar con `pd.read_pickle`.

## Configuración y opciones
- `pd.set_option("display.max_rows", valor)`, `pd.reset_option("all")`.
- `pd.get_option("display.precision")`.

> Recomendación: practicar estas funciones en un cuaderno interactivo (`.ipynb`) para fijar flujos de trabajo habituales con pandas.
