# Ejemplos frecuentes con Pandas

Este recorrido reúne diez bloques breves de operaciones habituales. Las salidas exactas de tablas pueden variar según la versión de pandas y el entorno.

## 1. Creación del DataFrame

La lista de diccionarios se convierte en un DataFrame y `to_datetime` transforma las fechas de texto en fechas manejables. La última expresión muestra el resultado, sin modificar las filas originales.

```python
import pandas as pd

ventas = [
    {"fecha": "2024-01-01", "tienda": "Norte", "producto": "A", "unidades": 10, "precio": 4.5},
    {"fecha": "2024-01-02", "tienda": "Sur", "producto": "B", "unidades": 7, "precio": 5.2},
    {"fecha": "2024-01-02", "tienda": "Norte", "producto": "A", "unidades": 5, "precio": 4.5},
    {"fecha": "2024-01-03", "tienda": "Sur", "producto": "C", "unidades": 3, "precio": 9.0},
]

df = pd.DataFrame(ventas)
df["fecha"] = pd.to_datetime(df["fecha"])
df
```

## 2. Importación y creación

`read_csv` lee un CSV externo usando `;` como separador; el archivo `ventas.csv` debe existir en la ruta indicada. `Series` crea una serie con índice y nombre, y `date_range` genera cinco fechas diarias.
```python
df_csv = pd.read_csv("ventas.csv", sep=";")
serie = pd.Series([1, 3, 5], index=["x", "y", "z"], name="valores")
fechas = pd.date_range(start="2024-01-01", periods=5, freq="D")
```

## 3. Exploración inicial

`head` muestra las primeras filas, `info` resume columnas y tipos, `describe` calcula estadísticas numéricas y `value_counts` cuenta cada producto. El formato de `info()` y `describe()` puede variar entre versiones; estos datos iniciales no contienen nulos.
```python
df.head(2)
df.info()
df.describe()
df["producto"].value_counts()
```

## 4. Selección y filtrado

Los dos primeros ejemplos seleccionan columnas y filas con etiquetas; `query` filtra con una expresión legible y `iloc` selecciona por posiciones. Devuelven vistas o nuevos objetos de selección, sin modificar `df` por sí solos.
```python
df[["tienda", "producto"]]
df.loc[df["tienda"] == "Norte", ["producto", "unidades"]]
df.query("unidades >= 5 and tienda == 'Sur'")
df.iloc[:2, 1:3]
```

## 5. Transformación y columnas

`assign` devuelve un DataFrame con la columna calculada, por eso se conserva en `df`. Las asignaciones directas crean o modifican columnas; `map` traduce categorías y `astype` devuelve una conversión de tipos sin sustituir `df` automáticamente.
```python
df = df.assign(ingresos=df["unidades"] * df["precio"])
df["categoria"] = df["producto"].map({"A": "consumo", "B": "consumo", "C": "lujo"})
df["ticket_medio"] = df["ingresos"] / df["unidades"]
df.astype({"unidades": "int32"})
```

## 6. Valores faltantes

`fillna` devuelve una copia con el precio faltante sustituido por la media, mientras que `dropna` devuelve las filas que conservan `producto`. En los datos iniciales no hay nulos, así que aquí no se elimina ni rellena ninguna fila.
```python
df_relleno = df.fillna({"precio": df["precio"].mean()})
df_sin_nulos = df.dropna(subset=["producto"])
```

## 7. Agrupaciones y agregaciones

`groupby` separa por tienda y las agregaciones calculan sumas o medias. El primer resultado es una serie de ingresos por tienda; el segundo devuelve un resumen por tienda y producto.
```python
df.groupby("tienda")["ingresos"].sum()
df.groupby(["tienda", "producto"]).agg(
    unidades_totales=("unidades", "sum"),
    ingresos_medios=("ingresos", "mean"),
)
```

## 8. Reorganización y combinaciones

`merge` añade la familia del catálogo mediante una combinación izquierda. `pivot_table` reorganiza los ingresos en filas y columnas y rellena con cero las combinaciones sin ventas; ambos métodos devuelven nuevos objetos.
```python
catalogo = pd.DataFrame({"producto": ["A", "B", "C"], "familia": ["consumo", "consumo", "lujo"]})
df.merge(catalogo, on="producto", how="left")

pivot = df.pivot_table(
    values="ingresos",
    index="tienda",
    columns="producto",
    aggfunc="sum",
    fill_value=0,
)
```

## 9. Series temporales y ventanas

`resample` agrupa por día tras usar la fecha como índice; `rolling(window=2)` calcula medias móviles de dos observaciones. Para `diff`, primero se ordena cronológicamente y después se calcula el cambio sobre ese orden: no se debe calcular en el orden original y realinearlo por índice.
```python
df.set_index("fecha").resample("D")["ingresos"].sum()
df.sort_values("fecha").rolling(window=2, on="fecha")["ingresos"].mean()
df_ordenado = df.sort_values("fecha")
df_ordenado = df_ordenado.assign(crecimiento=df_ordenado["ingresos"].diff())
```

## 10. Exportación

Los tres métodos escriben el DataFrame en CSV, Excel y Parquet; no se muestran aquí sus salidas porque dependen del sistema de archivos. `index=False` evita exportar el índice. Excel puede requerir `openpyxl`, y Parquet puede requerir `pyarrow` o `fastparquet`.
```python
df.to_csv("ventas_resumen.csv", index=False)
df.to_excel("ventas.xlsx", sheet_name="resumen", index=False)
df.to_parquet("ventas.parquet")
```
