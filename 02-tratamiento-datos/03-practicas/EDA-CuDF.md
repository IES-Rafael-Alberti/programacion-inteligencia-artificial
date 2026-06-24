
> ```bash
> pip install jupytext
> jupytext --to notebook EDA_cuDF_colab.md
> ```

---


# ⚡ EDA con cuDF (RAPIDS) en Google Colab — con fallback a Pandas

Este cuaderno ejecuta un **EDA completo** sobre un dataset sintético grande usando **cuDF** (GPU).  
Si no hay GPU disponible, **cambia automáticamente a Pandas** (CPU) manteniendo el mismo flujo.

---

## 0) Entorno: instalar cuDF (solo si hay GPU)

> En Google Colab: `Entorno de ejecución → Cambiar tipo de entorno → GPU`

```python
import os, sys, subprocess, shutil

def have_gpu():
    try:
        out = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
        return out.returncode == 0
    except Exception:
        return False

GPU = have_gpu()
print("GPU detectada:", GPU)

if GPU:
    # Instalar cuDF para CUDA 12 (Colab moderno suele venir con CUDA 12.x)
    try:
        print("Instalando cuDF (puede tardar unos minutos)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q",
                               "cudf-cu12", "cupy-cuda12x", "rmm-cu12",
                               "--extra-index-url=https://pypi.nvidia.com"])
        import cudf, cupy as cp
        USING = "cudf"
        print("✅ cuDF instalado y listo.")
    except Exception as e:
        print("⚠️ No se pudo instalar cuDF. Se usará Pandas (CPU). Motivo:", e)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pandas", "pyarrow"])
        import pandas as pd
        USING = "pandas"
else:
    print("⚠️ No hay GPU: se usará Pandas (CPU).")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pandas", "pyarrow"])
    import pandas as pd
    USING = "pandas"

print("Backend en uso:", USING)
````

---

## 1) Dataset sintético (1M filas en GPU, 200k en CPU)

Columnas: `ID, Edad, Salario, Experiencia, Horas, Nivel, Satisfaccion`
Incluye **outliers** y **NaN** para practicar limpieza.

```python
import numpy as np, time

np.random.seed(42)
N = 1_000_000 if USING=="cudf" else 200_000  # escalamos según backend

# Generación en NumPy (rápida), luego convertimos a cuDF/Pandas
ids = np.arange(1, N+1)
edad = np.random.randint(18, 65, size=N)
salario = np.random.normal(2500, 800, size=N)
experiencia = np.random.randint(0, 40, size=N)
horas = np.random.normal(40, 5, size=N)
nivel = np.random.randint(0, 5, size=N)
satisf = np.random.normal(7, 2, size=N)

# Outliers en salario (~0.5%)
out_idx = np.random.randint(0, N, size=max(1, N//200))
salario[out_idx] *= 4

# NaN en satisfacción (~1%)
nan_idx = np.random.randint(0, N, size=max(1, N//100))
satisf[nan_idx] = np.nan

data = {
    "ID": ids,
    "Edad": edad,
    "Salario": salario,
    "Experiencia": experiencia,
    "Horas": horas,
    "Nivel": nivel,
    "Satisfaccion": satisf
}

if USING=="cudf":
    import cudf
    gdf = cudf.DataFrame(data)
    df = gdf  # alias homogéneo
else:
    import pandas as pd
    df = pd.DataFrame(data)

df.head()
```

---

## 2) Utilidades

```python
def tic():
    return time.perf_counter()

def toc(t0, label=""):
    dt = time.perf_counter()-t0
    print(f"{label} ⏱️ {dt:.3f}s")

def describe_cols(dframe, cols):
    return dframe[cols].describe()
```

---

## 3) Tarea 1 — Descripción básica

```python
t0 = tic()
shape = (len(df), len(df.columns)) if USING=="cudf" else df.shape
print("Filas x Columnas:", shape)
print("Columnas:", list(df.columns))
display(df.head())
toc(t0, "Descripción")
```

---

## 4) Tarea 2 — Tipos y rangos

```python
t0 = tic()
print("Tipos:\n", df.dtypes)
display(describe_cols(df, ["Edad","Salario"]))
toc(t0, "Tipos y rangos")
```

---

## 5) Tarea 3 — Filtrado de datos

```python
t0 = tic()
altos = df[df["Salario"] > 4000]
n_altos = len(altos)
print("Salario > 4000 €:", n_altos)

cond2 = (df["Horas"] > 45) & (df["Experiencia"] > 10)
sel2 = df.loc[cond2, ["ID","Edad","Horas","Experiencia"]].head()
print("IDs con >45h y >10 exp (muestra):")
display(sel2)

pct_nivel_ge3 = (df["Nivel"] >= 3).mean()*100
print(f"% nivel >=3: {pct_nivel_ge3:.2f}%")
toc(t0, "Filtrado")
```

---

## 6) Tarea 4 — Limpieza: valores faltantes

```python
t0 = tic()
nan_count = df["Satisfaccion"].isna().sum()
print("NaN en Satisfaccion:", int(nan_count))
mean_sat = df["Satisfaccion"].mean()
df["Satisfaccion"] = df["Satisfaccion"].fillna(mean_sat)
left_nan = int(df["Satisfaccion"].isna().sum())
print("NaN restantes:", left_nan)
toc(t0, "Limpieza NaN")
```

---

## 7) Tarea 5 — Detección de outliers (IQR)

```python
t0 = tic()
q1 = df["Salario"].quantile(0.25)
q3 = df["Salario"].quantile(0.75)
iqr = q3 - q1
lim_inf = q1 - 1.5*iqr
lim_sup = q3 + 1.5*iqr
filtro_out = (df["Salario"] < lim_inf) | (df["Salario"] > lim_sup)
n_out = int(filtro_out.sum())
print("Outliers detectados:", n_out)
print("Límites:", float(lim_inf), float(lim_sup))
toc(t0, "IQR")
```

---

## 8) Tarea 6 — Sustitución de outliers (winsorizing en p95)

```python
t0 = tic()
p95 = df["Salario"].quantile(0.95)
# asignación condicionada
df.loc[filtro_out, "Salario"] = p95
# comprobar nuevos extremos
mn = float(df["Salario"].min())
mx = float(df["Salario"].max())
print("Nuevos min/max salario:", mn, mx)
toc(t0, "Winsorizing")
```

---

## 9) Tarea 7 — Agrupaciones y resúmenes

```python
t0 = tic()
salario_media_nivel = df.groupby("Nivel")["Salario"].mean()
print("Salario medio por Nivel:")
display(salario_media_nivel)

# Grupo de edad: <30, 30–50, >50
bins = [0, 30, 50, 200]
labels = ["<30", "30–50", ">50"]
df["GrupoEdad"] = cudf.cut(df["Edad"], bins=bins, labels=labels) if USING=="cudf" else pd.cut(df["Edad"], bins=bins, labels=labels)

sat_media_grupo = df.groupby("GrupoEdad")["Satisfaccion"].mean()
print("Satisfacción media por grupo de edad:")
display(sat_media_grupo)
toc(t0, "Groupby")
```

---

## 10) Tarea 8 — Normalización y z-score

```python
t0 = tic()
df["Salario_norm"] = (df["Salario"] - df["Salario"].min()) / (df["Salario"].max() - df["Salario"].min())
df["Horas_z"] = (df["Horas"] - df["Horas"].mean()) / df["Horas"].std()

summary = describe_cols(df, ["Salario_norm","Horas_z"])
display(summary)
toc(t0, "Normalización")
```

---

## 11) Tarea 9 — Correlaciones

```python
t0 = tic()
corr1 = df[["Salario","Experiencia"]].corr()
corr2 = df[["Edad","Satisfaccion"]].corr()
print("Corr(Salario, Experiencia):")
display(corr1)
print("Corr(Edad, Satisfaccion):")
display(corr2)
toc(t0, "Correlaciones")
```

---

## 12) Tarea 10 — Estadísticas globales

```python
t0 = tic()
display(df.describe(include="all"))
toc(t0, "Describe global")
```

---

## 13) Notas finales ()

* En **GPU (cuDF)**, probad a subir `N` a 5–10 millones y comparar tiempos con CPU.
* Mismas APIs que Pandas → transición suave.
* *Winsorizing* y `cut`/`groupby` son muy similares; el **cambio real** es de **rendimiento** y tamaño de datos.

```
```

---

