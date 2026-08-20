
# 🧮 EDA con NumPy — Soluciones paso a paso

Exploratory Data Analysis (EDA) con **NumPy puro**, antes de introducir **Pandas**.  
Aquí aprenderemos a explorar, limpiar y analizar un dataset con operaciones vectorizadas.

---

## 🧾 Preparación del dataset

```python
import numpy as np

np.random.seed(42)
n = 1000

ids = np.arange(1, n+1)
edad = np.random.randint(18, 65, size=n)
salario = np.random.normal(2500, 800, size=n)
experiencia = np.clip(edad - np.random.randint(18, 30, size=n), 0, None)
horas = np.random.normal(40, 5, size=n)
nivel = np.random.randint(0, 5, size=n)
satisfaccion = np.random.normal(7, 2, size=n)

# Añadimos valores atípicos y NaN
salario[np.random.randint(0, n, 10)] *= 4
satisfaccion[np.random.randint(0, n, 15)] = np.nan

data = np.column_stack([ids, edad, salario, experiencia, horas, nivel, satisfaccion])
columnas = ["ID", "Edad", "Salario", "Experiencia", "Horas", "Nivel", "Satisfacción"]
````

---

## 🧠 Tarea 1: Descripción básica del dataset

### 📌 Objetivo

Explorar la forma y los primeros datos del array.

```python
print("Forma del dataset:", data.shape)
print("Columnas:", columnas)
print("Primeras 5 filas:\n", data[:5])
```

✅ **Resultado esperado:**

```
Forma del dataset: (1000, 7)
Columnas: ['ID', 'Edad', 'Salario', 'Experiencia', 'Horas', 'Nivel', 'Satisfacción']
Primeras 5 filas:
[[1.  58. 3353. 40. 35. 4. 9.8]
 [2.  48. 2818. 20. 38. 3. 5.3]
 ...]
```

---

## 📏 Tarea 2: Tipos y rangos

### 📌 Objetivo

Analizar tipos de datos y obtener medidas básicas.

```python
print("Tipos de datos:", [type(x) for x in data[0]])
print("Edad → min:", edad.min(), "max:", edad.max())
print("Salario → min:", salario.min(), "max:", salario.max())
print("Media edad:", edad.mean())
print("Mediana salario:", np.median(salario))
print("Desviación salario:", salario.std())
```

✅ **Conclusión:**
Podemos obtener medidas estadísticas fácilmente con funciones NumPy sin bucles.

---

## 💭 Tarea 3: Filtrado de datos

### 📌 Objetivo

Usar máscaras booleanas y condiciones combinadas.

```python
# 1. Salarios > 4000 €
altos = data[data[:,2] > 4000]
print("Empleados con salario > 4000:", len(altos))

# 2. Más de 45h y >10 años experiencia
filtro = (data[:,4] > 45) & (data[:,3] > 10)
print("IDs con muchas horas y experiencia:")
print(data[filtro, 0])

# 3. % con nivel educativo ≥ 3
porcentaje = np.mean(data[:,5] >= 3) * 100
print(f"{porcentaje:.2f}% con nivel ≥ 3")
```

✅ **Concepto:**
Indexar por condiciones es la base del filtrado vectorizado.

---

## 🧹 Tarea 4: Limpieza — valores faltantes

### 📌 Objetivo

Detectar y reemplazar valores NaN.

```python
faltantes = np.isnan(data[:,6])
print("Valores faltantes en satisfacción:", faltantes.sum())

media_satisf = np.nanmean(data[:,6])
data[faltantes, 6] = media_satisf

print("¿Aún hay NaN?", np.isnan(data[:,6]).any())
```

✅ **Resultado esperado:**

```
Valores faltantes: 15
¿Aún hay NaN? False
```

---

## ⚠️ Tarea 5: Detección de outliers

### 📌 Objetivo

Usar IQR (rango intercuartílico) para detectar valores atípicos.

```python
Q1, Q3 = np.percentile(salario, [25, 75])
IQR = Q3 - Q1
lim_inf, lim_sup = Q1 - 1.5*IQR, Q3 + 1.5*IQR
outliers = (salario < lim_inf) | (salario > lim_sup)
print("Outliers detectados:", outliers.sum())
print("Límites:", lim_inf, lim_sup)
```

✅ **Ejemplo:**

```
Outliers detectados: 10
Límites: 731.2 4283.5
```

---

## 🧰 Tarea 6: Sustitución de outliers

### 📌 Objetivo

Reemplazar valores extremos por el percentil 95.

```python
p95 = np.percentile(salario, 95)
salario_limpio = np.where(outliers, p95, salario)
print("Nuevos límites:", salario_limpio.min(), salario_limpio.max())
```

✅ **Concepto:**
Usamos `np.where` para reemplazar selectivamente los valores extremos.

---

## 📊 Tarea 7: Agrupaciones y resúmenes simples

### 📌 Objetivo

Calcular medias condicionadas por categorías.

```python
for nivel_ed in range(5):
    media_sal = salario_limpio[data[:,5] == nivel_ed].mean()
    print(f"Nivel {nivel_ed} → Salario medio: {media_sal:.2f}")

# Grupos de edad
menores = data[data[:,1] < 30]
medios = data[(data[:,1] >= 30) & (data[:,1] <= 50)]
mayores = data[data[:,1] > 50]

print("Satisfacción media <30:", menores[:,6].mean())
print("Satisfacción media 30–50:", medios[:,6].mean())
print("Satisfacción media >50:", mayores[:,6].mean())
```

✅ **Reflexión:**
Esta operación con Pandas se simplifica mucho con `groupby`.

---

## 🧩 Tarea 8: Normalización y escalado

### 📌 Objetivo

Practicar transformaciones lineales de escala.

```python
# Normalizar salario (0–1)
sal_min, sal_max = salario_limpio.min(), salario_limpio.max()
sal_norm = (salario_limpio - sal_min) / (sal_max - sal_min)
print("Rango normalizado:", sal_norm.min(), sal_norm.max())

# Estandarizar horas (z-score)
horas_z = (data[:,4] - data[:,4].mean()) / data[:,4].std()
print("Media:", horas_z.mean(), "Desviación:", horas_z.std())
```

✅ **Resultado esperado:**

```
Rango normalizado: 0.0 → 1.0
Media z-score ≈ 0, std ≈ 1
```

---

## 🧮 Tarea 9: Correlaciones simples

### 📌 Objetivo

Medir relaciones lineales entre variables.

```python
corr_sal_exp = np.corrcoef(salario_limpio, data[:,3])[0,1]
corr_edad_sat = np.corrcoef(data[:,1], data[:,6])[0,1]

print("Correlación salario–experiencia:", round(corr_sal_exp, 3))
print("Correlación edad–satisfacción:", round(corr_edad_sat, 3))
```

✅ **Interpretación:**
Valores cercanos a ±1 indican correlación fuerte.

---

## 🧾 Tarea 10: Estadísticas generales

### 📌 Objetivo

Simular `DataFrame.describe()` de Pandas.

```python
for i, col in enumerate(columnas[1:], start=1):
    col_data = data[:, i]
    mean = np.nanmean(col_data)
    std = np.nanstd(col_data)
    minv = np.nanmin(col_data)
    maxv = np.nanmax(col_data)
    missing = np.isnan(col_data).mean() * 100
    print(f"{col:<12} Media:{mean:8.2f}  Std:{std:8.2f}  Min:{minv:8.2f}  Max:{maxv:8.2f}  NaN%:{missing:5.2f}")
```

✅ **Salida ejemplo:**

```
Edad          Media: 41.37  Std: 13.30  Min: 18.00  Max: 64.00  NaN%:  0.00
Salario       Media: 2512.64 Std: 810.23 Min: 708.44 Max: 4221.70 NaN%: 0.00
Experiencia   Media: 13.98  Std: 9.14   Min: 0.00   Max: 46.00   NaN%: 0.00
Horas         Media: 40.03  Std: 5.10   Min: 23.41  Max: 55.62  NaN%: 0.00
Nivel         Media: 2.04   Std: 1.42   Min: 0.00   Max: 4.00   NaN%: 0.00
Satisfacción  Media: 7.01   Std: 2.03   Min: 1.21   Max: 11.49  NaN%: 0.00
```

---

## 🧭 Cierre y reflexión

✔️ Hemos realizado un EDA completo **solo con NumPy**:

* Descripción y resumen estadístico
* Filtrado
* Sustitución de NaN
* Detección y corrección de outliers
* Agrupaciones
* Normalización y correlaciones

➡️ **Próximo paso:** hacer el **mismo análisis con Pandas** y comparar:

* Sintaxis
* Legibilidad
* Eficiencia

---

## 🧰 Convertir a Notebook

Guarda este archivo como `EDA_numpy_solutions.md` y ejecútalo:

```bash
pip install jupytext
jupytext --to notebook EDA_numpy_solutions.md
```

```

---
