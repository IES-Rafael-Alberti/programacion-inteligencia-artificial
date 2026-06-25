# 🧮 Actividad: Análisis exploratorio con NumPy

*(EDA sin Pandas — antesala a Pandas y JAX NumPy)*

---

## 🧾 Contexto del dataset

Se trabajará con un dataset sintético que simula **información de empleados**:

* ID
* Edad
* Salario mensual
* Años de experiencia
* Horas de trabajo por semana
* Nivel educativo (0 a 4)
* Satisfacción (0–10, con valores faltantes o atípicos)

Generaremos los datos con `np.random`, así todos tendrán el mismo formato.

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
```

---

## 🧩 Estructura de la sesión (por tareas)

Cada tarea dura unos minutos y se corrige en grupo.
Puedes mostrar el resultado en pantalla o que ellos lo expliquen.

---

### 🧠 **Tarea 1: Descripción básica del dataset**

1. Muestra el número de filas y columnas del array `data`.
2. Muestra los nombres de las columnas.
3. Obtén los primeros 5 registros.

➡️ Objetivo: entender cómo están dispuestos los datos y su estructura.

---

### 📏 **Tarea 2: Tipos y rangos**

1. Identifica los tipos de datos de cada columna (`int`, `float`, etc.).
2. Muestra el valor mínimo y máximo de cada variable numérica.
3. Calcula la media, mediana y desviación típica de **edad** y **salario**.

➡️ Objetivo: practicar operaciones estadísticas básicas.

---

### 💭 **Tarea 3: Filtrado de datos**

1. Obtén todos los empleados con salario mayor a 4000 €.
2. Obtén los IDs de quienes trabajan más de 45 h/semana y tienen más de 10 años de experiencia.
3. Calcula el porcentaje de empleados con **nivel educativo ≥ 3**.

➡️ Objetivo: uso de indexado booleano y condiciones combinadas.

---

### 🧹 **Tarea 4: Limpieza — valores faltantes**

1. Cuenta cuántos valores faltantes (`np.nan`) hay en la columna **satisfacción**.
2. Sustituye los valores `NaN` por la **media** de satisfacción.
3. Comprueba que ya no hay valores faltantes.

➡️ Objetivo: manejo básico de `np.isnan()` y reemplazos condicionales.

---

### ⚠️ **Tarea 5: Detección de outliers**

1. Calcula los **cuartiles (Q1 y Q3)** del salario.
2. Calcula el **rango intercuartílico (IQR)**.
3. Encuentra los valores que están fuera de `Q1 - 1.5*IQR` o `Q3 + 1.5*IQR`.
4. Muestra cuántos outliers hay.

➡️ Objetivo: detección numérica de valores atípicos con operaciones vectorizadas.

---

### 🧰 **Tarea 6: Sustitución o corrección de outliers**

1. Sustituye los salarios outliers por el valor del **percentil 95**.
2. Verifica que ya no hay salarios fuera del rango esperado.

➡️ Objetivo: aplicar `np.where` y percentiles para limpiar valores extremos.

---

### 📊 **Tarea 7: Agrupaciones y resúmenes simples**

1. Calcula el salario medio por **nivel educativo (0–4)**.
2. Calcula la satisfacción media por **grupo de edad**:

   * Menores de 30
   * 30–50
   * Mayores de 50

➡️ Objetivo: practicar máscaras múltiples y operaciones por grupo con NumPy.

---

### 🧩 **Tarea 8: Normalización y escalado**

1. Normaliza la variable **salario** entre 0 y 1.
2. Estandariza (z-score) la variable **horas**.
3. Comprueba media ~0 y std ~1.

➡️ Objetivo: practicar transformaciones de escala (útil para ML más adelante).

---

### 🧮 **Tarea 9: Correlaciones simples**

1. Calcula la **correlación** entre salario y experiencia.
2. Calcula la correlación entre edad y satisfacción.

➡️ Objetivo: usar `np.corrcoef` e interpretar relaciones lineales.

---

### 🧾 **Tarea 10: Estadísticas generales**

1. Muestra para cada columna:

   * Media
   * Desviación estándar
   * Valor mínimo
   * Valor máximo
   * Porcentaje de valores faltantes

➡️ Objetivo: preparar el pensamiento para `df.describe()` y `df.info()` de Pandas.

---

## 💬 Cierre de la práctica

Tras completar todas las tareas:

* Comenta con el grupo **qué operaciones fueron más fáciles con NumPy**.
* Avanza la idea de que **Pandas** automatiza mucho de esto con estructuras **Series** y **DataFrames**, simplificando la limpieza y exploración.

---

## 🧰 Sugerencia para ti

Puedes guardar esta práctica como `EDA_numpy.md` y convertirla a notebook con:

```bash
jupytext --to notebook EDA_numpy.md
```

---

