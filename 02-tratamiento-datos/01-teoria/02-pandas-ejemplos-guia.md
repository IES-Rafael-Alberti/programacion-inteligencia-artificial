# Ejemplos frecuentes con Pandas

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

## Importación y creación
```python
df_csv = pd.read_csv("ventas.csv", sep=";")
serie = pd.Series([1, 3, 5], index=["x", "y", "z"], name="valores")
fechas = pd.date_range(start="2024-01-01", periods=5, freq="D")
```

## Exploración inicial
```python
df.head(2)
df.info()
df.describe()
df["producto"].value_counts()
```

## Selección y filtrado
```python
df[["tienda", "producto"]]
df.loc[df["tienda"] == "Norte", ["producto", "unidades"]]
df.query("unidades >= 5 and tienda == 'Sur'")
df.iloc[:2, 1:3]
```

## Transformación y columnas
```python
df.assign(ingresos=df["unidades"] * df["precio"])
df["categoria"] = df["producto"].map({"A": "consumo", "B": "consumo", "C": "lujo"})
df["ticket_medio"] = df["ingresos"] / df["unidades"]
df.astype({"unidades": "int32"})
```

## Valores faltantes
```python
df_relleno = df.fillna({"precio": df["precio"].mean()})
df_sin_nulos = df.dropna(subset=["producto"])
```

## Agrupaciones y agregaciones
```python
df.groupby("tienda")["ingresos"].sum()
df.groupby(["tienda", "producto"]).agg(
    unidades_totales=("unidades", "sum"),
    ingresos_medios=("ingresos", "mean"),
)
```

## Reorganización y combinaciones
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

## Series temporales y ventanas
```python
df.set_index("fecha").resample("D")["ingresos"].sum()
df.sort_values("fecha").rolling(window=2, on="fecha")["ingresos"].mean()
df.sort_values("fecha").assign(crecimiento=df["ingresos"].diff())
```

## Exportación
```python
df.to_csv("ventas_resumen.csv", index=False)
df.to_excel("ventas.xlsx", sheet_name="resumen", index=False)
df.to_parquet("ventas.parquet")
```
