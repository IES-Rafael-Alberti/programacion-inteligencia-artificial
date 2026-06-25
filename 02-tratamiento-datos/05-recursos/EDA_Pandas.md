
# 🐼 EDA con Pandas — comparación con NumPy

En esta práctica repetimos el **mismo análisis exploratorio (EDA)** que hicimos con NumPy,  
pero ahora usando **Pandas**, para ver cómo cambia la sintaxis, el tiempo de desarrollo  
y las capacidades de análisis.

---

## 🧾 Preparación del dataset

```python
import numpy as np
import pandas as pd

np.random.seed(42)
n = 1000

df = pd.DataFrame({
    "ID": np.arange(1, n+1),
    "Edad": np.random.randint(18, 65, size=n),
    "Salario": np.random.normal(2500, 800, size=n),
    "Experiencia": np.clip(np.random.randint(0, 40, size=n), 0, None),
    "Horas": np.random.normal(40, 5, size=n),
    "Nivel": np.random.randint(0, 5, size=n),
    "Satisfacción": np.random.normal(7, 2, size=n)
})

# Añadimos outliers y NaN
df.loc[np.random.randint(0, n, 10), "Salario"] *= 4
df.loc[np.random.randint(0, n, 15), "Satisfacción"] = np.nan

df.head()
````

---

## 🧠 Tarea 1: Descripción básica

```python
df.shape
df.columns
df.head()
```

✅ **Más directo**: Pandas ya muestra etiquetas y formato de tabla.

---

## 📏 Tarea 2: Tipos y rangos

```python
df.dtypes
df[["Edad", "Salario"]].agg(["min", "max", "mean", "median", "std"])
```

✅ En una sola línea obtenemos estadísticas básicas.

---

## 💭 Tarea 3: Filtrado de datos

```python
# 1. Salarios > 4000 €
df[df["Salario"] > 4000]

# 2. Más de 45h y >10 años experiencia
df[(df["Horas"] > 45) & (df["Experiencia"] > 10)][["ID", "Edad", "Horas", "Experiencia"]]

# 3. Porcentaje nivel ≥ 3
(df["Nivel"] >= 3).mean() * 100
```

✅ Sintaxis más legible y declarativa.

---

## 🧹 Tarea 4: Limpieza — valores faltantes

```python
df["Satisfacción"].isna().sum()
df["Satisfacción"].fillna(df["Satisfacción"].mean(), inplace=True)
df["Satisfacción"].isna().any()
```

✅ Un único método `fillna()` evita usar máscaras.

---

## ⚠️ Tarea 5: Detección de outliers

```python
Q1 = df["Salario"].quantile(0.25)
Q3 = df["Salario"].quantile(0.75)
IQR = Q3 - Q1

filtro = (df["Salario"] < Q1 - 1.5*IQR) | (df["Salario"] > Q3 + 1.5*IQR)
df[filtro]
```

✅ `quantile()` y condiciones combinadas simplifican la detección.

---

## 🧰 Tarea 6: Sustitución de outliers

```python
p95 = df["Salario"].quantile(0.95)
df.loc[filtro, "Salario"] = p95
```

✅ Con `.loc[]` seleccionamos y sustituimos directamente.

---

## 📊 Tarea 7: Agrupaciones y resúmenes simples

```python
# Media por nivel
df.groupby("Nivel")["Salario"].mean()

# Satisfacción media por grupo de edad
bins = [0, 30, 50, 100]
labels = ["<30", "30–50", ">50"]
df["GrupoEdad"] = pd.cut(df["Edad"], bins=bins, labels=labels)
df.groupby("GrupoEdad")["Satisfacción"].mean()
```

✅ `groupby()` y `cut()` hacen triviales las operaciones por grupo.

---

## 🧩 Tarea 8: Normalización y escalado

```python
df["Salario_norm"] = (df["Salario"] - df["Salario"].min()) / (df["Salario"].max() - df["Salario"].min())
df["Horas_z"] = (df["Horas"] - df["Horas"].mean()) / df["Horas"].std()
df[["Salario_norm", "Horas_z"]].describe()
```

✅ Con Pandas, las operaciones vectorizadas siguen siendo de NumPy,
pero la sintaxis es más limpia y las columnas se guardan fácilmente.

---

## 🧮 Tarea 9: Correlaciones simples

```python
df[["Salario", "Experiencia"]].corr()
df[["Edad", "Satisfacción"]].corr()
```

✅ `corr()` calcula la matriz de correlación directamente.

---

## 🧾 Tarea 10: Estadísticas generales

```python
df.describe(include="all")
```

✅ Una sola línea genera resumen completo de medias, desvíos,
mínimos, máximos y cuantiles — igual a lo que hicimos en 30 líneas con NumPy.

---

## ⚖️ Comparación final: NumPy vs Pandas

| Aspecto                       | NumPy                                     | Pandas                                         |
| ----------------------------- | ----------------------------------------- | ---------------------------------------------- |
| **Estructura**                | Arrays homogéneos (solo números)          | DataFrames con columnas heterogéneas           |
| **Acceso a datos**            | Por índice numérico                       | Por nombre de columna                          |
| **Limpieza (NaN, outliers)**  | Manual, usando máscaras y `np.isnan()`    | Métodos directos (`fillna`, `replace`, `clip`) |
| **Agrupaciones**              | Manual, por filtrado repetido             | `groupby`, `cut`, `pivot_table`                |
| **Resúmenes**                 | Funciones separadas (`mean`, `std`, etc.) | `describe()`, `agg()` integrados               |
| **Eficiencia**                | Muy rápido (array plano)                  | Un poco más lento, pero flexible               |
| **Lectura de datos externos** | No                                        | CSV, Excel, SQL, Parquet, JSON…                |

---

## 🧠 Reflexión: cuándo usar cada uno

* 🧮 **NumPy**: ideal para **cálculos numéricos puros**, operaciones de álgebra, vectores, tensores o machine learning a bajo nivel.
* 🐼 **Pandas**: ideal para **análisis de datos reales** con valores faltantes, mezcla de tipos, y manipulación de columnas o tablas grandes.

En la práctica, **Pandas usa NumPy por debajo** para los cálculos numéricos,
pero aporta una capa de **semántica tabular y limpieza** que simplifica enormemente el trabajo.

---

## ⚙️ Pandas y sus motores internos

Desde **Pandas 2.0**, el DataFrame puede usar distintos **motores de ejecución**:

| Motor         | Descripción                                                 | Uso principal                                                                             |
| ------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 🧩 **NumPy**  | Motor tradicional basado en arrays NumPy (`dtype` clásico). | Por defecto en la mayoría de entornos.                                                    |
| ⚡ **PyArrow** | Motor alternativo basado en Apache Arrow (`dtype="arrow"`). | Mayor eficiencia, tipos nulos nativos, interoperabilidad con Parquet, DuckDB, Spark, etc. |

Puedes comprobar o cambiar el motor por defecto:

```python
import pandas as pd
pd.options.mode.dtype_backend
# 'numpy' o 'pyarrow'
```

Y cambiarlo así:

```python
pd.set_option("mode.dtype_backend", "pyarrow")
```

💡 **Ventajas de PyArrow**:

* Maneja nulos reales, no solo `NaN`
* Más rápido en operaciones columnares
* Reduce consumo de memoria
* Integración con otros frameworks (Arrow, Polars, DuckDB, etc.)

---

## 🧾 En resumen

| Característica | NumPy                                  | Pandas                       |
| -------------- | -------------------------------------- | ---------------------------- |
| Nivel          | Bajo nivel (arrays)                    | Alto nivel (tablas)          |
| Ideal para     | Cálculos numéricos, ML, algebra lineal | Limpieza, análisis, EDA, ETL |
| Falta de datos | Manejo limitado                        | Soporte completo             |
| Tipos de datos | Homogéneos                             | Heterogéneos                 |
| Motores        | —                                      | NumPy o PyArrow              |

---

## 🚀 Próximo paso

➡️ **Repite el EDA con Pandas y compara tiempos, líneas y legibilidad.**
➡️ Después exploraremos **visualización (Matplotlib / Seaborn)** para completar el análisis exploratorio.

```

---
