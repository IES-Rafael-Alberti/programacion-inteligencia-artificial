# 🐼 Introducción a **Pandas**

---

## 📘 ¿Qué es Pandas?

**Pandas** es una **biblioteca de Python para análisis y manipulación de datos**.  
Su nombre viene de *Panel Data* (datos estructurados en paneles o tablas multidimensionales).  
Proporciona estructuras de datos eficientes y potentes herramientas para:

- Limpieza de datos  
- Transformaciones  
- Análisis exploratorio (EDA)  
- Agrupaciones y estadísticas  
- Lectura y escritura en múltiples formatos (CSV, Excel, SQL, JSON, Parquet, etc.)

En esencia, Pandas te permite **trabajar con datos tabulares** (filas y columnas) de forma muy similar a una hoja de cálculo o una tabla SQL, pero **con la potencia de Python** y **la velocidad de NumPy**.

---

## 🧱 Estructuras de datos principales

| Estructura | Descripción | Equivalente conceptual |
|-------------|--------------|-------------------------|
| `Series` | Columna unidimensional con índice | Columna de Excel o vector |
| `DataFrame` | Tabla bidimensional con etiquetas de filas y columnas | Hoja de cálculo o tabla SQL |

Ejemplo básico:

```python
import pandas as pd

# Serie
s = pd.Series([10, 20, 30], name="Ventas")

# DataFrame
df = pd.DataFrame({
    "Producto": ["A", "B", "C"],
    "Ventas": [100, 250, 300],
    "Precio": [10.5, 12.3, 9.8]
})
````

---

## ⚙️ Motores internos: NumPy y PyArrow

Desde **Pandas 2.0**, se introdujo el concepto de **"motores de ejecución" o *backends*** para manejar internamente los datos.
Pandas puede funcionar sobre dos motores principales:

| Motor       | Descripción                                                              | Ventajas                                                                                                                       |
| ----------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **NumPy**   | Motor clásico (por defecto) basado en arrays homogéneos en memoria.      | Rápido, probado, compatible con casi todo el ecosistema científico de Python.                                                  |
| **PyArrow** | Motor moderno basado en **Apache Arrow**, formato columnares optimizado. | Soporta nulos nativos, tipos más precisos (string, timestamp, categoricals), interoperabilidad con DuckDB, Polars, Spark, etc. |

Ejemplo: comprobar el motor actual

```python
import pandas as pd
pd.options.mode.dtype_backend
# 'numpy' o 'pyarrow'
```

Cambiar motor:

```python
pd.set_option("mode.dtype_backend", "pyarrow")
```

---

### 🧩 Diferencias entre NumPy y PyArrow

| Característica         | Motor NumPy                                       | Motor PyArrow                                            |
| ---------------------- | ------------------------------------------------- | -------------------------------------------------------- |
| Tipo nulo              | `NaN` (solo float)                                | `null` (nativo en cualquier tipo)                        |
| Representación interna | Arrays NumPy (C)                                  | Columnas Arrow (columnares)                              |
| Compatibilidad         | 100% retrocompatible                              | Requiere Pandas ≥ 2.0                                    |
| Precisión en tipos     | Limitada (ej. object/string)                      | Total (UTF-8, decimal, timestamp, etc.)                  |
| Interoperabilidad      | Con librerías científicas (NumPy, SciPy, Sklearn) | Con sistemas analíticos (DuckDB, Spark, Polars, Parquet) |

💡 **Consejo:**
Usa **NumPy backend** por defecto para análisis y ML local, y **PyArrow backend** si vas a trabajar con grandes volúmenes o integración con herramientas Big Data (DuckDB, Parquet, Spark, etc.).

---

## 🧰 ¿Para qué se utiliza Pandas?

Pandas se usa en prácticamente **todas las etapas del ciclo de análisis y ciencia de datos**.

### 🧮 1. Limpieza y preparación de datos

* Eliminar duplicados, valores nulos, outliers.
* Renombrar columnas, transformar tipos.
* Combinar, unir o pivotar tablas.

```python
df.dropna()
df.fillna(df.mean())
df.merge(otra_tabla, on="id")
```

---

### 📊 2. Exploración y análisis (EDA)

* Estadísticos básicos y visualización rápida.
* Agrupaciones (`groupby`).
* Correlaciones, distribuciones, resúmenes.

```python
df.describe()
df.groupby("categoria")["ventas"].mean()
df["precio"].corr(df["ventas"])
```

---

### 📈 3. Integración con librerías de IA y ML

Pandas se integra directamente con:

* **Scikit-learn** (modelos de Machine Learning)
* **TensorFlow / PyTorch** (entradas a tensores)
* **Matplotlib / Seaborn / Plotly** (visualización)
* **NumPy** (cálculo vectorizado)

Ejemplo:

```python
from sklearn.linear_model import LinearRegression
X = df[["Edad", "Salario"]]
y = df["Satisfacción"]
modelo = LinearRegression().fit(X, y)
```

---

### 💾 4. Entrada y salida de datos

Pandas soporta múltiples formatos de datos:

| Formato         | Lectura          | Escritura      |
| --------------- | ---------------- | -------------- |
| CSV             | `pd.read_csv()`  | `to_csv()`     |
| Excel           | `read_excel()`   | `to_excel()`   |
| JSON            | `read_json()`    | `to_json()`    |
| SQL             | `read_sql()`     | `to_sql()`     |
| Parquet / Arrow | `read_parquet()` | `to_parquet()` |

---

## 🚫 Cuándo **no** usar Pandas

Pandas es potente, pero no siempre la mejor opción.
Hay casos donde **otras herramientas son más adecuadas**:

| Situación                             | Alternativa recomendada                        |
| ------------------------------------- | ---------------------------------------------- |
| Dataset muy grande (RAM insuficiente) | **Dask**, **Vaex**, **cuDF (GPU)**, **DuckDB** |
| Consultas SQL complejas               | **DuckDB**, **PostgreSQL**, **SparkSQL**       |
| Procesamiento distribuido             | **PySpark**, **Dask**, **Ray**                 |
| Trabajo puramente numérico/matricial  | **NumPy**, **JAX**                             |
| Pipelines productivos o escalables    | **Polars** (DataFrame optimizado en Rust)      |

---

## ✅ Ventajas de Pandas

| Ventaja                         | Descripción                                                       |
| ------------------------------- | ----------------------------------------------------------------- |
| 🧩 **Simplicidad**              | Sintaxis intuitiva y expresiva, ideal para análisis rápidos.      |
| ⚙️ **Integración**              | Compatible con NumPy, Matplotlib, Scikit-learn, TensorFlow, etc.  |
| 🧠 **Potencia analítica**       | Operaciones vectorizadas, agrupaciones, pivotes, joins, etc.      |
| 📚 **Ecosistema maduro**        | Amplia documentación, soporte y comunidad.                        |
| 💾 **Flexibilidad de formatos** | Lee y escribe casi cualquier tipo de archivo de datos.            |
| 🧮 **Compatibilidad Arrow**     | Con PyArrow, interoperable con herramientas modernas de Big Data. |

---

## ⚠️ Inconvenientes de Pandas

| Inconveniente                                    | Explicación                                                       |
| ------------------------------------------------ | ----------------------------------------------------------------- |
| 🧠 **Consumo de memoria alto**                   | Carga todos los datos en RAM (no apto para datasets muy grandes). |
| 🕒 **Procesamiento secuencial**                  | No aprovecha varios núcleos por defecto.                          |
| 🔢 **Tipos inconsistentes**                      | Con NumPy, los valores nulos obligan a usar floats u objetos.     |
| 🧰 **Limitaciones en Big Data**                  | No diseñado para clusters o paralelismo nativo.                   |
| 🐢 **Rendimiento decrece con millones de filas** | Puede volverse lento sin optimización.                            |

---

## 💡 Buenas prácticas

1. ✅ Usa **tipos adecuados** (`category`, `int32`, `float32`) para reducir memoria.
2. ⚡ Convierte datos grandes a **Parquet / Arrow** para mayor eficiencia.
3. 🧹 Evita bucles `for`: usa operaciones vectorizadas (`apply`, `map`, `assign`).
4. 🧾 Guarda los resultados limpios con `df.to_parquet()` o `df.to_pickle()` para uso rápido.
5. 🔄 Si necesitas escalar: pasa a **cuDF**, **Dask** o **Polars** sin reescribir todo el código.

---

## 🧠 Casos de uso típicos

| Área                  | Ejemplo práctico                                               |
| --------------------- | -------------------------------------------------------------- |
| Ciencia de datos      | Análisis exploratorio (EDA) de datasets (Titanic, COVID, etc.) |
| IA y Machine Learning | Preparar features y targets antes del modelado                 |
| Negocios              | Limpieza y agregación de datos de ventas o clientes            |
| Finanzas              | Series temporales, retornos y correlaciones                    |
| Educación             | Enseñar fundamentos de análisis de datos antes de SQL o Spark  |

---

## 🚀 Casos de no uso

| Situación                          | Motivo                                    | Alternativa                      |
| ---------------------------------- | ----------------------------------------- | -------------------------------- |
| Dataset > RAM (100 GB, 1 TB, etc.) | Pandas no gestiona memoria fuera de RAM   | Dask / cuDF / DuckDB / Polars    |
| Análisis en tiempo real            | Pandas no es streaming                    | Apache Kafka + Spark Streaming   |
| Modelos productivos                | Pandas no está optimizado para despliegue | PyArrow Dataset / Parquet / DBMS |
| Cálculos intensivos GPU            | Pandas usa CPU                            | RAPIDS (cuDF/cuML) o PyTorch     |

---

## 🔬 Ejemplo final: mini EDA con Pandas

```python
import pandas as pd

df = pd.read_csv("empleados.csv")

# 1️⃣ Resumen general
print(df.shape, df.dtypes)

# 2️⃣ Limpieza rápida
df = df.drop_duplicates().fillna(df.mean(numeric_only=True))

# 3️⃣ Estadísticos
print(df.describe())

# 4️⃣ Agrupaciones
print(df.groupby("departamento")["salario"].mean())

# 5️⃣ Correlación
print(df[["edad", "salario"]].corr())
```

---

## 📎 Conclusión

Pandas es **una herramienta esencial** en el ecosistema de ciencia de datos y análisis en Python.
Es ideal para **análisis exploratorios, limpieza, transformación y preprocesamiento de datos**,
sirviendo como base antes de usar librerías más avanzadas como **scikit-learn**, **PyTorch**, **DuckDB** o **cuDF**.

> 🧭 En resumen:
>
> * **NumPy backend:** mejor para análisis tradicionales.
> * **PyArrow backend:** ideal para datos modernos, grandes o heterogéneos.
> * **Pandas sigue siendo el punto de partida** para cualquier proyecto de datos en Python.

```

---

¿Quieres que te prepare una **versión ampliada para aula** (con ejemplos prácticos ejecutables: `read_csv`, `groupby`, `merge`, `apply`, etc.) o una **versión resumida tipo ficha teórica A4** para entregar a los alumnos como guía rápida?
```