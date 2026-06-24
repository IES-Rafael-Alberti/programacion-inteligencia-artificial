
# 📊 Comparativa de EDA con NumPy, Pandas y DuckDB

| Nº | Tarea | NumPy | Pandas | DuckDB (SQL) |
|----|--------|--------|---------|--------------|
| 1️⃣ | Descripción básica | 3–5 líneas (`shape`, slices) | 1 línea (`df.info()`, `head()`) | 1 SELECT + `PRAGMA table_info` |
| 2️⃣ | Tipos y rangos | `type()`, `min`, `max`, `mean`, `std` → manual | `df.describe()` o `agg()` | `SELECT MIN(), MAX(), AVG()` |
| 3️⃣ | Filtrado | máscaras booleanas `(a>0)&(b>0)` | expresiones claras `df[...]` | `WHERE` y `CASE` |
| 4️⃣ | Valores faltantes | `np.isnan`, `np.nanmean`, `np.where` | `isna()`, `fillna()` | `UPDATE ... WHERE IS NULL` |
| 5️⃣ | Outliers (IQR) | percentiles + condiciones | `quantile()`, `clip()` | `quantile_cont()`, `CASE` |
| 6️⃣ | Sustituir outliers | `np.where(cond, p95, x)` | `loc[filtro] = valor` | `UPDATE ... SET ... WHERE` |
| 7️⃣ | Agrupar y resumir | varias máscaras y medias | `groupby()`, `cut()` | `GROUP BY` |
| 8️⃣ | Normalización | `(x-min)/(max-min)` y z-score | igual pero directo con columnas | `UPDATE` con subconsultas |
| 9️⃣ | Correlaciones | `np.corrcoef()` | `df.corr()` | `corr(x,y)` |
| 🔟 | Estadísticas globales | bucles + `mean`, `std`, etc. | `df.describe()` | `UNION ALL` con funciones agregadas |

---

## 💬 Evaluación rápida

| Criterio | NumPy | Pandas | DuckDB |
|-----------|--------|---------|---------|
| **Nivel de abstracción** | Bajo | Medio | Alto |
| **Legibilidad** | 🟡 Regular (más código) | 🟢 Alta (columnas por nombre) | 🟢 Alta (SQL estándar) |
| **Facilidad de limpieza** | 🔴 Manual | 🟢 Muy sencilla (`fillna`, `replace`) | 🟡 Algo verbosa (`UPDATE ... WHERE`) |
| **Agrupaciones** | 🔴 Repetitivas | 🟢 Muy potentes (`groupby`) | 🟢 Muy claras con `GROUP BY` |
| **Rendimiento CPU** | 🟢 Excelente | 🟢 Muy bueno | 🟢 Muy bueno (motor vectorizado) |
| **Soporte GPU** | 🔴 No | 🟡 Indirecto (via cuDF) | 🔴 No (CPU only) |
| **Lectura de datos** | 🔴 Solo arrays | 🟢 CSV, Excel, SQL, Parquet... | 🟢 Directo desde CSV/Parquet/SQL |
| **Ideal para** | Cálculo numérico, ML | Análisis y limpieza de datos | SQL interactivo y OLAP embebido |

---

## ⚙️ Reflexión técnica sobre los motores

| Motor | Descripción | Ventajas |
|--------|--------------|-----------|
| **NumPy** | Motor nativo de arrays de Pandas (por defecto hasta 2.0) | Rápido, probado, C-optimizado |
| **PyArrow (Arrow)** | Motor alternativo de Pandas 2.x (`dtype_backend="pyarrow"`) | Soporta nulos nativos, tipos más precisos, interoperable con Polars, Spark, DuckDB |
| **DuckDB** | Motor SQL embebido, tipo “SQLite para analítica” | Usa Arrow y vectorización interna; lee CSV/Parquet directamente |
| **cuDF (RAPIDS)** | Motor tipo Pandas pero GPU (CUDA) | Procesa millones de filas con paralelismo masivo |

---

## 🧩 En resumen

| Stack | Ideal para | Fortalezas | Limitaciones |
|--------|-------------|-------------|---------------|
| 🧮 **NumPy** | Cálculo numérico puro | Velocidad, bajo nivel, control total | Poco expresivo para datos heterogéneos |
| 🐼 **Pandas** | EDA, limpieza y análisis | Sintaxis simple, integración, visualización | Limitado en datasets > RAM |
| 🦆 **DuckDB** | SQL analítico local | Eficiente, sin servidor, interoperable Arrow | Verboso para operaciones iterativas |
| ⚡ **cuDF** | Big Data en GPU | Paralelismo masivo, sintaxis tipo Pandas | Requiere GPU NVIDIA y RAPIDS entorno |

---

# ⚡ Próxima etapa: EDA con cuDF (RAPIDS)

---

## 💻 1. Entorno de instalación

En **Google Colab** o **WSL2 con CUDA**:

```bash
# En Colab
!pip install cudf-cu12 --extra-index-url=https://pypi.nvidia.com

# O en Linux local con CUDA 12.x
pip install cudf-cu12 dask-cudf --extra-index-url=https://pypi.nvidia.com
````

> Requiere GPU NVIDIA con drivers + CUDA Toolkit 12.x

---

## 📊 2. Dataset y estructura

Usaremos el mismo esquema de columnas:
`["ID", "Edad", "Salario", "Experiencia", "Horas", "Nivel", "Satisfaccion"]`

Crearemos el DataFrame en **cuDF** directamente desde un DataFrame Pandas o NumPy:

```python
import cudf
import cupy as cp
import numpy as np
import pandas as pd

n = 1_000_000  # Escalamos a 1 millón para aprovechar GPU

np.random.seed(42)
pdf = pd.DataFrame({
    "ID": np.arange(1, n+1),
    "Edad": np.random.randint(18, 65, size=n),
    "Salario": np.random.normal(2500, 800, size=n),
    "Experiencia": np.random.randint(0, 40, size=n),
    "Horas": np.random.normal(40, 5, size=n),
    "Nivel": np.random.randint(0, 5, size=n),
    "Satisfaccion": np.random.normal(7, 2, size=n)
})
# Añadir outliers y NaN
pdf.loc[np.random.randint(0, n, 1000), "Salario"] *= 4
pdf.loc[np.random.randint(0, n, 2000), "Satisfaccion"] = np.nan

gdf = cudf.from_pandas(pdf)
```

---

## 🧠 3. Mismas 10 tareas del EDA con cuDF

*(idénticas a NumPy/Pandas/DuckDB, pero todas en GPU)*

| Tarea                        | Ejemplo cuDF                                                                  |
| ---------------------------- | ----------------------------------------------------------------------------- |
| 1️⃣ **Descripción**          | `gdf.info()` , `gdf.head()`                                                   |
| 2️⃣ **Estadísticos básicos** | `gdf.describe()`                                                              |
| 3️⃣ **Filtrado**             | `gdf[gdf.Salario > 4000]`                                                     |
| 4️⃣ **Valores faltantes**    | `gdf.Satisfaccion = gdf.Satisfaccion.fillna(gdf.Satisfaccion.mean())`         |
| 5️⃣ **Outliers**             | `q1,q3=gdf.Salario.quantile([0.25,0.75])`                                     |
| 6️⃣ **Sustitución**          | `gdf.loc[filtro, 'Salario'] = gdf.Salario.quantile(0.95)`                     |
| 7️⃣ **Agrupaciones**         | `gdf.groupby("Nivel").Salario.mean()`                                         |
| 8️⃣ **Normalización**        | `(gdf.Salario - gdf.Salario.min()) / (gdf.Salario.max() - gdf.Salario.min())` |
| 9️⃣ **Correlaciones**        | `gdf[['Salario','Experiencia']].corr()`                                       |
| 🔟 **Resumen global**        | `gdf.describe(include='all')`                                                 |

💡 **Igual sintaxis que Pandas**, pero cada operación se ejecuta **en GPU (CUDA)**.

---

## ⚡ 4. Ventajas y límites de cuDF

### ✅ Ventajas

* Procesa millones de filas en segundos gracias a **paralelismo masivo GPU**
* Misma sintaxis que Pandas
* Integración con **Dask-cuDF** para clusters GPU
* Lectura/escritura directa en **Parquet, ORC, Arrow**

### ⚠️ Desventajas

* Requiere **GPU NVIDIA + drivers CUDA**
* No todas las funciones Pandas están implementadas (especialmente I/O avanzadas)
* Mayor consumo de VRAM en operaciones intermedias

---

## 📈 5. Resumen final

| Stack  | CPU/GPU           | Ideal para                | Eficiencia                      |
| ------ | ----------------- | ------------------------- | ------------------------------- |
| NumPy  | CPU               | Matemática base, arrays   | 🔥 Alta                         |
| Pandas | CPU               | EDA, limpieza, tabular    | 🔥 Alta (RAM limitada)          |
| DuckDB | CPU (vectorizado) | SQL analítico, OLAP local | ⚡ Muy alta (columnares, Arrow)  |
| cuDF   | GPU (CUDA)        | Big Data, ML pipelines    | 🚀 Extremadamente alta (en GPU) |

---

## 🧩 Recomendación docente

👉 **Usa esta secuencia para que el alumnado vea la evolución conceptual:**

```
NumPy  ➜  Pandas  ➜  DuckDB  ➜  cuDF (GPU)
```

Y destaca:

* La **continuidad de sintaxis vectorizada**
* Cómo cambia el **nivel de abstracción**
* Qué **motor** usa cada uno:

  * NumPy: C nativo
  * Pandas: NumPy / PyArrow
  * DuckDB: Arrow + vectorización
  * cuDF: CUDA (GPU kernels)

```

---

