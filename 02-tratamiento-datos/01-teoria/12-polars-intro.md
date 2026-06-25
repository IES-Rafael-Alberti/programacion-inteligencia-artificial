# 🧊 Introducción a Polars
**Un DataFrame ultrarrápido para Data Science en Python**

## 1. ¿Qué es Polars?
**Polars** es un motor de procesamiento de datos **columnar y ultrarrápido**, escrito en **Rust**, que ofrece una API similar a pandas pero con un rendimiento mucho mayor, especialmente en:

- cargas de trabajo grandes
- operaciones complejas
- procesos en paralelo
- análisis en modo *lazy* (consulta diferida y optimizada)

Se ha convertido en una alternativa potente a pandas, con el objetivo de ser:

- ⚡ **Más rápido**
- 💾 **Más eficiente en memoria**
- 🧵 **Multihilo por defecto**
- 🌐 **Seguro y estable** (gracias a Rust)

---

## 2. ¿Por qué usar Polars?
### Polars destaca en tres aspectos:

### **2.1. Velocidad**
Polars puede ser entre **5× y 20× más rápido** que Pandas, gracias a:

- ejecución paralela
- vectorización real
- optimización de planes de consulta
- representación columnar Arrow

### **2.2. Lazy Execution (Ejecución diferida)**
Polars permite definir toda una serie de operaciones y **no ejecutarlas hasta el final**, optimizando:

- filtros
- proyecciones
- agregaciones
- fusiones

Esto evita operaciones innecesarias y acelera el procesamiento.

### **2.3. Modelo de datos moderno**
Polars usa internamente **Apache Arrow**, lo que lo hace interoperable con:

- PyArrow
- cuDF (GPU)
- DuckDB
- Spark
- DataFusion

---

## 3. Instalación
```bash
pip install polars
```

(En entornos con GPU NVIDIA puedes usar Polars + cuDF vía Arrow.)

---

## 4. Cargar datos con Polars

```python
import polars as pl

df = pl.read_csv("data.csv")
df.head()
```

Polars detecta tipos automáticamente e intenta optimizar la carga.

---

## 5. Estructuras básicas

### **5.1 DataFrame**

```python
df = pl.DataFrame({
    "nombre": ["Ana", "Luis", "Carmen"],
    "edad": [21, 32, 28],
    "nota": [7.5, 8.2, 9.1]
})
```

### **5.2 Series**

```python
s = pl.Series("edades", [21, 32, 28])
```

---

## 6. Selección y filtrado

```python
df.select("nombre", "nota")
```

```python
df.filter(pl.col("edad") > 25)
```

```python
df.select([
    pl.col("edad").mean(),
    pl.col("nota").max()
])
```

---

## 7. Operaciones típicas

### **7.1 Crear columnas**

```python
df = df.with_columns(
    (pl.col("nota") * 10).alias("nota_normalizada")
)
```

### **7.2 Agrupaciones**

```python
df.groupby("nombre").agg([
    pl.col("nota").mean(),
    pl.col("edad").max()
])
```

### **7.3 Ordenar**

```python
df.sort("edad", descending=True)
```

### **7.4 Tipos de datos**

```python
df.with_columns(
    pl.col("edad").cast(pl.Float64)
)
```

---

## 8. **Lazy mode** (la joya de Polars)

El modo *lazy* permite planificar una transformación sin ejecutarla inmediatamente.

```python
lazy_df = pl.scan_csv("data.csv")

resultado = (
    lazy_df
    .filter(pl.col("edad") > 25)
    .groupby("ciudad")
    .agg(pl.col("nota").mean())
    .sort("nota", descending=True)
    .collect()   # <- aquí se ejecuta todo
)
```

### Beneficios:

* Polars reorganiza operaciones para maximizar la eficiencia.
* Ejecuta solo lo necesario.
* Reduce memoria y tiempo.

---

## 9. Comparación rápida: Pandas vs Polars

### **Pandas**

```python
import pandas as pd
df = pd.read_csv("data.csv")
df[df["edad"] > 25]["nota"].mean()
```

### **Polars**

```python
import polars as pl
df = pl.read_csv("data.csv")
df.filter(pl.col("edad") > 25).select(pl.col("nota").mean())
```

### **Lazy Polars**

```python
pl.scan_csv("data.csv")\
  .filter(pl.col("edad") > 25)\
  .select(pl.col("nota").mean())\
  .collect()
```

---

## 10. Ventajas y desventajas

### ✔️ **Ventajas**

* Extremadamente rápido
* Bajo consumo de memoria
* Lazy execution
* Integración con Arrow y DuckDB
* Más seguro (Rust)
* API muy clara y expresiva

### ❌ **Desventajas**

* Menos conocido que Pandas
* Documentación más corta
* Ecosistema más pequeño
* Algunas librerías aún esperan DataFrames de Pandas

*(Aunque Polars convierte a Pandas fácilmente con `.to_pandas()`.)*

---

## 11. ¿Cuándo usar Polars?

Usa Polars cuando:

* trabajas con **datasets grandes**
* necesitas **mucha velocidad**
* haces **pipelines complejos de EDA**
* quieres **procesar en paralelo**
* quieres integrarlo con **DuckDB** o **Arrow**

---

## 12. Ejemplo completo de EDA en Polars

```python
import polars as pl

df = pl.read_csv("spotify.csv")

# Limpieza
df = df.filter(pl.col("popularity") > 0)

# Crear columnas nuevas
df = df.with_columns([
    (pl.col("duration_ms") / 1000).alias("duration_s")
])

# Agrupaciones
resumen = (
    df.groupby("genre")
      .agg([
          pl.col("popularity").mean().alias("media_popularidad"),
          pl.col("duration_s").mean().alias("duracion_media")
      ])
      .sort("media_popularidad", descending=True)
)

resumen.head()
```

---

## 13. Conversión a Pandas (si fuera necesario)

```python
df_pandas = df.to_pandas()
```

---

## 14. Conclusión

Polars es hoy una de las herramientas más potentes para análisis de datos en Python.
Su velocidad, modelo columnar, y su ejecución en modo lazy lo convierten en una alternativa ideal para:

* EDA
* preprocesamiento
* análisis repetitivos
* grandes volúmenes de datos

Es la herramienta perfecta para sustituir o complementar a Pandas en muchos casos.


Aquí va la **comparación clara y técnica** entre **Polars** y **Pandas con engine=“pyarrow”** (Pandas 2.x), porque mucha gente cree que “Pandas con Arrow ≈ Polars”, pero **no es así**.

---

# 🧩 1. ¿Qué significa “Pandas con Arrow”?

Desde Pandas 2.0, puedes usar:

```python
df = pd.read_csv("data.csv", engine="pyarrow")
```

o convertir columnas a Arrow:

```python
df = df.convert_dtypes(dtype_backend="pyarrow")
```

Esto NO convierte a Pandas en Polars.
Solo significa:

* Las **columnas** son Arrow arrays.
* Algunas operaciones usan kernels Arrow (muy rápidas).
* Pero **Pandas sigue siendo Pandas** (Python puro, sin paralelismo en su core).

---

