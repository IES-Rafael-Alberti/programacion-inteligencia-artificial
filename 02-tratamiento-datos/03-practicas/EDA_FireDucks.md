Perfecto 🔥
Vamos a hacer el **notebook de EDA con FireDucks** — el mismo que ya hicimos con **NumPy, Pandas, DuckDB y cuDF**,
pero ahora usando **FireDucks**, que acelera Pandas automáticamente con ejecución diferida y paralelización.

👉 Este notebook estará en formato **Markdown convertibles a `.ipynb`**,
e incluirá:

* instalación y detección del entorno,
* creación del dataset sintético,
* las **10 tareas del EDA**,
* **bloque de medición de tiempos** para comparar con Pandas,
* y una reflexión final sobre rendimiento, ventajas y límites.

---

````markdown
# 🔥 EDA con FireDucks — versión completa para aula

**FireDucks** es una librería que acelera el código de **Pandas** sin cambiar su sintaxis.  
Es compatible casi al 100% y utiliza un motor interno de **ejecución optimizada (lazy + parallel)**  
para mejorar el rendimiento en operaciones de filtrado, agregación y estadística.

---

## 0️⃣ Instalación y preparación

```python
!pip install -q fireducks

import time, numpy as np
import fireducks.pandas as pd  # sustituye pandas sin cambiar la API
print("🔥 FireDucks activado. Versión:", pd.__version__)
````

💡 *Puedes usar exactamente el mismo código que con Pandas.*
Internamente, FireDucks compila y paraleliza las operaciones.

---

## 1️⃣ Creación del dataset sintético

Usaremos el mismo formato que en los otros EDA (NumPy, Pandas, DuckDB, cuDF):

```python
np.random.seed(42)
N = 1_000_000  # tamaño grande para ver diferencia de rendimiento

ids = np.arange(1, N+1)
edad = np.random.randint(18, 65, size=N)
salario = np.random.normal(2500, 800, size=N)
experiencia = np.random.randint(0, 40, size=N)
horas = np.random.normal(40, 5, size=N)
nivel = np.random.randint(0, 5, size=N)
satisf = np.random.normal(7, 2, size=N)

# outliers (~0.5%)
out_idx = np.random.randint(0, N, size=N//200)
salario[out_idx] *= 4

# NaN (~1%)
nan_idx = np.random.randint(0, N, size=N//100)
satisf[nan_idx] = np.nan

df = pd.DataFrame({
    "ID": ids,
    "Edad": edad,
    "Salario": salario,
    "Experiencia": experiencia,
    "Horas": horas,
    "Nivel": nivel,
    "Satisfaccion": satisf
})

df.head()
```

---

## 2️⃣ Descripción básica

```python
t0 = time.time()
print("Filas x columnas:", df.shape)
print("Columnas:", list(df.columns))
display(df.head())
print("⏱️", time.time()-t0, "s")
```

---

## 3️⃣ Tipos y rangos

```python
t0 = time.time()
print(df.dtypes)
display(df[["Edad","Salario"]].describe())
print("⏱️", time.time()-t0, "s")
```

---

## 4️⃣ Filtrado de datos

```python
t0 = time.time()

altos = df[df["Salario"] > 4000]
cond2 = (df["Horas"] > 45) & (df["Experiencia"] > 10)
sel2 = df.loc[cond2, ["ID","Edad","Horas","Experiencia"]].head()

pct_nivel_ge3 = (df["Nivel"] >= 3).mean() * 100

print("Salarios >4000:", len(altos))
display(sel2)
print(f"% nivel ≥3: {pct_nivel_ge3:.2f}%")
print("⏱️", time.time()-t0, "s")
```

---

## 5️⃣ Limpieza de valores faltantes

```python
t0 = time.time()

nan_count = df["Satisfaccion"].isna().sum()
print("Valores nulos iniciales:", nan_count)
df["Satisfaccion"] = df["Satisfaccion"].fillna(df["Satisfaccion"].mean())
print("Nulos después:", df["Satisfaccion"].isna().sum())

print("⏱️", time.time()-t0, "s")
```

---

## 6️⃣ Detección de outliers (IQR)

```python
t0 = time.time()
q1 = df["Salario"].quantile(0.25)
q3 = df["Salario"].quantile(0.75)
iqr = q3 - q1
lim_inf, lim_sup = q1 - 1.5*iqr, q3 + 1.5*iqr
filtro_out = (df["Salario"] < lim_inf) | (df["Salario"] > lim_sup)
print("Outliers detectados:", filtro_out.sum())
print("⏱️", time.time()-t0, "s")
```

---

## 7️⃣ Sustitución de outliers (winsorizing)

```python
t0 = time.time()
p95 = df["Salario"].quantile(0.95)
df.loc[filtro_out, "Salario"] = p95
print("Nuevo máximo salario:", df["Salario"].max())
print("⏱️", time.time()-t0, "s")
```

---

## 8️⃣ Agrupaciones y resúmenes

```python
t0 = time.time()

salario_media_nivel = df.groupby("Nivel")["Salario"].mean()
print("Salario medio por Nivel:")
display(salario_media_nivel)

bins = [0,30,50,200]
labels = ["<30","30–50",">50"]
df["GrupoEdad"] = pd.cut(df["Edad"], bins=bins, labels=labels)
print("Satisfacción media por grupo de edad:")
display(df.groupby("GrupoEdad")["Satisfaccion"].mean())

print("⏱️", time.time()-t0, "s")
```

---

## 9️⃣ Normalización y z-score

```python
t0 = time.time()
df["Salario_norm"] = (df["Salario"] - df["Salario"].min()) / (df["Salario"].max() - df["Salario"].min())
df["Horas_z"] = (df["Horas"] - df["Horas"].mean()) / df["Horas"].std()

display(df[["Salario_norm","Horas_z"]].describe())
print("⏱️", time.time()-t0, "s")
```

---

## 🔟 Correlaciones y resumen global

```python
t0 = time.time()

print("Correlación salario–experiencia:")
display(df[["Salario","Experiencia"]].corr())

print("Correlación edad–satisfacción:")
display(df[["Edad","Satisfaccion"]].corr())

print("Resumen general:")
display(df.describe(include="all"))

print("⏱️", time.time()-t0, "s")
```

---

## 🚀 Medición de rendimiento frente a Pandas

Para comparar rendimiento con Pandas estándar:

```python
import pandas as pd_std
pdf = df.to_pandas() if hasattr(df, "to_pandas") else df.copy()

def bench(func, name):
    t0 = time.time()
    func()
    print(f"{name:<30} ⏱️ {time.time()-t0:.3f}s")

print("🔥 Benchmark: FireDucks vs Pandas")

bench(lambda: df["Salario"].mean(), "FireDucks mean")
bench(lambda: pdf["Salario"].mean(), "Pandas mean")

bench(lambda: df.groupby("Nivel")["Salario"].mean(), "FireDucks groupby")
bench(lambda: pdf.groupby("Nivel")["Salario"].mean(), "Pandas groupby")
```

💡 *FireDucks suele ser entre 2× y 10× más rápido según el tipo de operación.*

---

## 🧠 Reflexión final

| Criterio             | FireDucks                                  | Pandas            |
| -------------------- | ------------------------------------------ | ----------------- |
| API                  | Igual (totalmente compatible)              | Nativo            |
| Rendimiento          | 🔥 Muy alto (lazy + paralelo)              | Medio             |
| Escalabilidad        | Mejor con datasets medianos (RAM)          | Buena             |
| Curva de aprendizaje | Nula                                       | —                 |
| Soporte actual       | En desarrollo activo                       | Maduro            |
| Ideal para           | Acelerar EDA y pipelines Pandas existentes | Análisis estándar |

---

### 🧩 Conclusiones

* **FireDucks es el reemplazo directo más rápido de Pandas.**
* Permite ejecutar el mismo código sin modificaciones.
* Ofrece aceleración transparente mediante *lazy evaluation* y *multihilo*.
* No requiere aprender nuevas APIs (a diferencia de Polars o Dask).

> 🔬 *En el aula puedes ejecutar los mismos notebooks del EDA anterior cambiando solo la importación:*
>
> ```python
> import fireducks.pandas as pd
> ```
>
> y observar las diferencias en tiempos de ejecución.

```

---

```