
---

# 📘 README — Proyecto de IA con datos meteorológicos ()

# 🌦️ Proyecto de IA — Dataset meteorológico

En este proyecto trabajarás con un **dataset de información meteorológica** para recorrer
todas las fases de un **proyecto real de Inteligencia Artificial**, desde el análisis de los datos
hasta la evaluación de un modelo.

El objetivo no es solo que el modelo funcione, sino que **entiendas el proceso completo
y sepas justificar cada decisión técnica**.

---

## 🧠 Qué vas a hacer

El proyecto se divide en **3 prácticas encadenadas**:

### 🧪 Práctica 1 — Análisis de datos (EDA)
- Explorar datos meteorológicos reales
- Detectar problemas de calidad (nulos, valores extremos, incoherencias)
- Analizar estacionalidad y patrones temporales
- Extraer conclusiones útiles para el modelado

📄 Archivo: `P1_EDA_meteo_base.md`

---

### 🤖 Práctica 2 — Modelado exploratorio (PyCaret)
- Definir el problema (regresión o clasificación)
- Probar distintos modelos automáticamente
- Comparar métricas (MAE, RMSE, etc.)
- Elegir un modelo y justificar la decisión

📄 Archivo: `P2_PyCaret_meteo_base.md`

---

### 🏗️ Práctica 3 — Modelo final
- Implementar el modelo elegido **sin AutoML**
- Ajustar hiperparámetros
- Evaluar el rendimiento
- Analizar limitaciones y posibles mejoras

📄 Archivo: `P3_Modelo_meteo_base.md`

---

## ⚡ Ampliación GPU (opcional)

Si dispones de GPU o acceso a GPU en la nube, puedes:
- usar **cuDF** para análisis de datos
- usar **cuML** para modelos acelerados
- comparar CPU vs GPU

👉 Es opcional y **no penaliza no realizarlo**.

---

## 🔁 Cómo trabajar con los archivos

Los materiales están en **Markdown**, pensados para convertirse a notebooks.

Conversión recomendada:

```bash
pip install jupytext
jupytext --to ipynb P1_EDA_meteo_base.md
````

---

## 📦 Qué tienes que entregar

* Los **3 notebooks completos**
* Un **documento final de conclusiones**

Formatos:

* Notebooks: `.ipynb`
* Documento final: `.md` o `.pdf`

---

## 🗣️ Defensa oral

Habrá una **defensa oral individual (5–10 minutos)** donde explicarás:

* el problema planteado
* las decisiones técnicas
* las conclusiones obtenidas

No se evalúa recitar código, sino **entender el proyecto**.

````

---

# 🧪 P1 — Análisis Exploratorio de Datos Meteorológicos  
## 📘 VERSIÓN ALUMNO  
**Archivo:** `P1_EDA_meteo_base.md`

```markdown
# Práctica 1 — Análisis Exploratorio de Datos Meteorológicos (EDA)

## Objetivo
Comprender el dataset meteorológico antes de aplicar modelos de IA.
No se entrenan modelos en esta práctica.

---

## 1. Contexto del dataset
Describe brevemente:
- de dónde proceden los datos (API, estación, organismo público…)
- qué representa cada fila (día, hora, medición)
- qué variables meteorológicas contiene

---

## 2. Carga del dataset

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

df = pd.read_csv("meteo.csv", parse_dates=["date"])
df.head()
````

---

## 3. Estructura del dataset

```python
df.shape
```

```python
df.info()
```

Comenta:

* número de registros
* tipos de datos
* variables numéricas y temporales

---

## 4. Calidad de los datos

```python
df.isna().sum()
```

```python
df.duplicated().sum()
```

Indica:

* si hay datos faltantes
* posibles mediciones erróneas
* decisiones de limpieza

---

## 5. Estadísticas descriptivas

```python
df.describe()
```

¿Qué valores llaman la atención?
¿Hay temperaturas extremas o precipitaciones anómalas?

---

## 6. Análisis temporal (muy importante)

```python
df.set_index("date")["temperature"].plot(figsize=(12,4))
plt.title("Evolución temporal de la temperatura")
plt.show()
```

Describe:

* tendencias
* estacionalidad
* periodos atípicos

---

## 7. Análisis de relaciones entre variables

```python
sns.scatterplot(data=df, x="humidity", y="temperature")
plt.show()
```

¿Existe relación entre variables meteorológicas?

---

## 8. Conclusiones del EDA

Redacta un apartado final con:

* variables más relevantes
* problemas detectados
* decisiones de limpieza
* qué variable crees que se puede predecir mejor

---

## 9. Anexo GPU (opcional)

```python
# import cudf
# gdf = cudf.from_pandas(df)
# gdf.head()
```

¿Aporta alguna ventaja usar GPU en esta fase?

```

---

# 🔁 Tabla de adaptación  
## Proyecto Películas → Proyecto Meteorológico

| Elemento | Películas | Meteorología |
|--------|-----------|--------------|
| Dominio | Entretenimiento | Medioambiental |
| Cada fila | Una película | Un día / hora |
| Variable temporal | Año de estreno | Fecha |
| Variables numéricas | Duración, rating | Temperatura, humedad, viento |
| Variables categóricas | Género | Estación, localización |
| Problema típico | Clasificación / regresión | **Regresión / series temporales** |
| Métricas comunes | Accuracy, F1 | MAE, RMSE |
| P1 (EDA) | Distribuciones y outliers | Estacionalidad y tendencias |
| P2 (PyCaret) | classification / regression | **regression / time_series** |
| P3 (modelo final) | RandomForestClassifier | RandomForestRegressor |
| GPU | Opcional, poco impacto | **Más sentido con datasets grandes** |
| Defensa oral | Decisiones sobre películas | Decisiones sobre predicción del tiempo |

---


