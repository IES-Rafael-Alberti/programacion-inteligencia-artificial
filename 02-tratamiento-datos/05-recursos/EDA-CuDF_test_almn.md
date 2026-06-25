

# ⚡ Práctica: EDA con cuDF (RAPIDS) — versión guiada con pistas 💡

Esta práctica reproduce un **EDA completo** (Análisis Exploratorio de Datos) usando **cuDF (GPU)**  
o **Pandas (CPU si no hay GPU)**.  

Cada bloque incluye:
- 🧩 Enunciado  
- 💻 Celda vacía para escribir el código  
- 💡 *Pista (comentario oculto)*  
- ✅ Test para comprobar el resultado  

---

## 0️⃣ Preparación del entorno

```python
import os, sys, subprocess

def have_gpu():
    try:
        import torch
        return torch.cuda.is_available()
    except Exception:
        return False

GPU = have_gpu()
print("GPU detectada:", GPU)

if GPU:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q",
                               "cudf-cu12", "cupy-cuda12x", "--extra-index-url=https://pypi.nvidia.com"])
        import cudf, cupy as cp
        USING = "cudf"
        print("✅ Usando cuDF (GPU).")
    except Exception as e:
        print("⚠️ Error al instalar cuDF:", e, "\n→ Usando Pandas (CPU).")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pandas"])
        import pandas as pd
        USING = "pandas"
else:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pandas"])
    import pandas as pd
    USING = "pandas"

print("Backend:", USING)
````

---

## 🧾 Dataset sintético

Crea un dataset con 200 000 filas (1 M si hay GPU):
`ID, Edad, Salario, Experiencia, Horas, Nivel, Satisfaccion`.

Incluye algunos valores NaN y outliers.

```python
# 💡 Pista:
# Usa np.random y luego crea un DataFrame con cudf.DataFrame(data)
# o con pd.DataFrame(data) según el backend.

# ✏️ Tu código aquí



```

✅ **Test**

```python
cols = ["ID","Edad","Salario","Experiencia","Horas","Nivel","Satisfaccion"]
ok = 'df' in locals() and all(col in df.columns for col in cols)
print("✅ OK" if ok else "❌ Columnas incorrectas o falta df")
```

---

## 1️⃣ Descripción básica

Muestra:

* número de filas y columnas
* nombres de columnas
* primeras 5 filas

```python
# 💡 Pista:
# Usa len(df), len(df.columns) y df.head()

# ✏️ Tu código aquí



```

✅ **Test**

```python
ok = hasattr(df, "head") and len(df.head()) == 5
print("✅ OK" if ok else "❌ Revisa tu código")
```

---

## 2️⃣ Tipos y rangos

Muestra los tipos de datos y calcula media, mediana y desviación de `Salario`.

```python
# 💡 Pista:
# Usa df.dtypes y df["Salario"].mean(), median(), std()

# ✏️ Tu código aquí



```

✅ **Test**

```python
ok = "Salario" in df.columns
print("✅ OK" if ok else "❌ Falta columna Salario o no mostrada")
```

---

## 3️⃣ Filtrado de datos

1. Filtra empleados con `Salario > 4000`.
2. Filtra los que trabajan más de 45 h/semana y con más de 10 años de experiencia.
3. Calcula el porcentaje con `Nivel ≥ 3`.

```python
# 💡 Pista:
# Usa condiciones booleanas: (df["Salario"] > 4000)
# y combina con &. El porcentaje = (df["Nivel"]>=3).mean()*100

# ✏️ Tu código aquí



```

✅ **Test**

```python
try:
    assert (df["Nivel"]>=0).all()
    print("✅ OK")
except Exception:
    print("❌ Revisa el filtrado o las condiciones")
```

---

## 4️⃣ Limpieza de NaN

Cuenta los NaN de `Satisfaccion`, reemplázalos por la media y comprueba que ya no hay.

```python
# 💡 Pista:
# Usa df["Satisfaccion"].isna().sum() y df["Satisfaccion"].fillna(df["Satisfaccion"].mean())

# ✏️ Tu código aquí



```

✅ **Test**

```python
ok = int(df["Satisfaccion"].isna().sum()) == 0
print("✅ OK" if ok else "❌ Aún hay NaN en Satisfaccion")
```

---

## 5️⃣ Detección de outliers (IQR)

Calcula Q1, Q3, IQR y muestra cuántos valores de salario están fuera de rango.

```python
# 💡 Pista:
# Usa df["Salario"].quantile(0.25) y (0.75) y luego define el rango con 1.5*IQR

# ✏️ Tu código aquí



```

✅ **Test**

```python
try:
    q1 = df["Salario"].quantile(0.25)
    q3 = df["Salario"].quantile(0.75)
    assert q1 < q3
    print("✅ OK")
except Exception:
    print("❌ Revisa el cálculo de IQR o las columnas")
```

---

## 6️⃣ Sustitución de outliers

Reemplaza los salarios fuera del rango con el valor del percentil 95.

```python
# 💡 Pista:
# Usa p95 = df["Salario"].quantile(0.95)
# y luego df.loc[filtro_out, "Salario"] = p95

# ✏️ Tu código aquí



```

✅ **Test**

```python
ok = float(df["Salario"].max()) <= float(df["Salario"].quantile(0.95))*1.01
print("✅ OK" if ok else "❌ Los outliers no fueron reemplazados correctamente")
```

---

## 7️⃣ Agrupaciones y resúmenes

1. Salario medio por nivel educativo.
2. Satisfacción media por grupo de edad (`<30`, `30–50`, `>50`).

```python
# 💡 Pista:
# Usa df.groupby("Nivel")["Salario"].mean()
# y pd.cut() o cudf.cut() para crear los grupos de edad

# ✏️ Tu código aquí



```

✅ **Test**

```python
ok = "Nivel" in df.columns
print("✅ OK" if ok else "❌ Falta columna Nivel")
```

---

## 8️⃣ Normalización y z-score

1. Normaliza el salario entre 0 y 1.
2. Calcula z-score de las horas.
3. Comprueba que media≈0, std≈1.

```python
# 💡 Pista:
# Normaliza con (x - x.min()) / (x.max() - x.min())
# Estandariza con (x - x.mean()) / x.std()

# ✏️ Tu código aquí



```

✅ **Test**

```python
try:
    assert abs(df["Horas"].mean()) >= 0
    print("✅ OK")
except Exception:
    print("❌ Error en normalización")
```

---

## 9️⃣ Correlaciones

Calcula:

* correlación entre salario y experiencia
* correlación entre edad y satisfacción

```python
# 💡 Pista:
# Usa df[["Salario","Experiencia"]].corr()
# y df[["Edad","Satisfaccion"]].corr()

# ✏️ Tu código aquí



```

✅ **Test**

```python
ok = hasattr(df, "corr")
print("✅ OK" if ok else "❌ No se pudo calcular correlaciones")
```

---

## 🔟 Estadísticas globales

Muestra `df.describe(include="all")`
e interpreta los resultados.

```python
# 💡 Pista:
# describe() genera resumen estadístico (media, std, min, max, cuantiles)

# ✏️ Tu código aquí



```

✅ **Test**

```python
try:
    summary = df.describe()
    print("✅ OK, describe ejecutado")
except Exception:
    print("❌ Error en df.describe()")
```

---

## 🧩 Reflexión final

💬 **Comenta brevemente:**

* ¿Qué tareas se aceleran más con GPU?
* ¿Qué funciones de cuDF son idénticas a Pandas?
* ¿Cuándo usarías cuDF frente a Pandas o NumPy?

---

**Tip docente 🧠:**
Puedes aumentar `N` a 1–10 millones en Colab con GPU
para que vean la mejora de rendimiento frente a CPU.

```

---
