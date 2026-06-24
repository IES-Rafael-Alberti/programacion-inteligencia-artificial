# ⚡ Introducción a **cuDF (RAPIDS)**

---

## 📘 ¿Qué es cuDF?

**cuDF** es una biblioteca de **Python para análisis y manipulación de datos** desarrollada por **NVIDIA** dentro del ecosistema **RAPIDS**.  
Su propósito es ofrecer una **implementación acelerada por GPU de la API de Pandas**.

👉 En resumen:
> **cuDF = Pandas + GPU (CUDA)**

Está escrita en **C++/CUDA** y permite manejar grandes volúmenes de datos directamente en la GPU,  
usando la **misma sintaxis que Pandas**, lo que facilita la migración de código sin cambios.

---

## 🧠 Filosofía y objetivo

cuDF forma parte del proyecto **RAPIDS**, cuyo objetivo es trasladar el procesamiento de datos  
desde la **CPU (procesamiento secuencial)** a la **GPU (procesamiento masivo paralelo)**.

Esto permite acelerar tareas de:
- Limpieza y transformación de datos.  
- Análisis exploratorio (EDA).  
- Preparación de datasets para Machine Learning y Deep Learning.  
- Lectura y escritura de grandes volúmenes en formatos columnares (Parquet, Arrow, ORC…).

---

## 🧱 Estructuras principales

| Estructura | Descripción | Equivalente en Pandas |
|-------------|-------------|-----------------------|
| `cudf.Series` | Columna unidimensional con índice GPU | `pd.Series` |
| `cudf.DataFrame` | Tabla bidimensional en memoria GPU | `pd.DataFrame` |
| `cudf.Index` | Índice basado en GPU | `pd.Index` |

Ejemplo básico:

```python
import cudf

df = cudf.DataFrame({
    "Producto": ["A", "B", "C"],
    "Precio": [10.5, 12.3, 9.8],
    "Ventas": [100, 250, 300]
})

print(df)
print(df["Precio"].mean())
````

💡 **Importante:** todo el DataFrame se almacena en **memoria de la GPU (VRAM)**.

---

## ⚙️ Instalación

cuDF requiere una **GPU NVIDIA** con soporte **CUDA**.
Hay tres formas principales de instalación:

### 🧩 1. En Google Colab

```bash
!pip install -q cudf-cu12 --extra-index-url=https://pypi.nvidia.com
```

> Colab usa CUDA 12.x, por eso se instala `cudf-cu12`.

---

### 🐧 2. En Linux local con CUDA Toolkit

```bash
pip install cudf-cu12 dask-cudf --extra-index-url=https://pypi.nvidia.com
```

> Asegúrate de tener drivers NVIDIA y CUDA instalados.

---

### 🧱 3. En contenedor Docker

```bash
docker run --gpus all -it nvcr.io/nvidia/rapidsai/rapidsai:24.08-cuda12.2-runtime-ubuntu22.04-py3.11
```

💡 Esto descarga un entorno completo de RAPIDS con cuDF, cuML, cuGraph y cuIO listos para usar.

---

## 🧩 Arquitectura general de RAPIDS

```
┌────────────────────────────┐
│   Usuario (Python / API)   │
│     pandas-like (cuDF)     │
└────────────┬───────────────┘
             ▼
┌────────────────────────────┐
│   Librerías RAPIDS Core    │
│ cuDF  cuML  cuGraph  cuIO  │
└────────────┬───────────────┘
             ▼
┌────────────────────────────┐
│   CUDA + GPU (paralelismo) │
│ Miles de núcleos en GPU    │
└────────────────────────────┘
```

---

## 🧮 Ejemplo simple de comparación

```python
import pandas as pd
import cudf
import numpy as np
import time

N = 10_000_000
pdf = pd.DataFrame({"x": np.random.randn(N), "y": np.random.randn(N)})
gdf = cudf.from_pandas(pdf)

# Media con Pandas
t0 = time.time(); pdf["x"].mean(); print("Pandas:", time.time()-t0, "s")

# Media con cuDF
t0 = time.time(); gdf["x"].mean(); print("cuDF:", time.time()-t0, "s")
```

⚡ En GPU la diferencia suele ser de **5× a 50× más rápido**,
dependiendo del tamaño del dataset y del tipo de operación.

---

## 🧰 ¿Para qué se utiliza cuDF?

### 1️⃣ **Análisis exploratorio de datos (EDA)**

* Cálculos estadísticos masivos.
* Limpieza, normalización y detección de outliers.
* Agrupaciones y resúmenes (groupby).

### 2️⃣ **Preparación de datos para Machine Learning**

* Codificación de variables (OneHot, Label).
* Normalización y estandarización.
* División en train/test y unión con datasets externos.

### 3️⃣ **Lectura y escritura eficiente**

cuDF incluye `cudf.read_csv`, `read_parquet`, `read_orc`,
optimizados para leer directamente en GPU.

### 4️⃣ **Integración con otras librerías RAPIDS**

* **cuML** → Machine Learning en GPU (equivalente a scikit-learn).
* **cuGraph** → análisis de grafos en GPU.
* **cuXfilter** → visualización interactiva GPU.
* **Dask-cuDF** → procesamiento distribuido en clusters GPU.

---

## ⚡ Casos de uso ideales

| Situación                             | Ventaja                                            |
| ------------------------------------- | -------------------------------------------------- |
| Datasets grandes (10M+ filas)         | Procesamiento en segundos, no en minutos.          |
| Pipelines de IA con GPU               | Evita transferencias CPU↔GPU al entrenar modelos.  |
| Integración con Spark/DuckDB/Arrow    | Compatible mediante Apache Arrow.                  |
| Entornos de investigación y formación | Facilita enseñar paralelización y computación GPU. |

---

## 🚫 Casos de **no uso**

| Situación                                                      | Motivo                                                             |
| -------------------------------------------------------------- | ------------------------------------------------------------------ |
| Sin GPU NVIDIA                                                 | cuDF no funcionará sin hardware CUDA.                              |
| Datasets pequeños (<100k filas)                                | El overhead de mover datos a GPU puede ser mayor que el beneficio. |
| Memoria GPU limitada (VRAM baja)                               | Los DataFrames grandes pueden exceder la capacidad de la GPU.      |
| Tareas altamente secuenciales o con funciones no vectorizables | Mejor en CPU (Pandas o DuckDB).                                    |

---

## ✅ Ventajas de cuDF

| Ventaja                          | Descripción                                                               |
| -------------------------------- | ------------------------------------------------------------------------- |
| ⚡ **Velocidad**                  | Acelera operaciones de Pandas por 5×–100× con ejecución paralela en GPU.  |
| 🧩 **Compatibilidad**            | Sintaxis idéntica a Pandas (código casi sin cambios).                     |
| 🧠 **Integración**               | Se conecta con cuML, cuGraph, cuDF I/O y Dask-cuDF.                       |
| 🔄 **Interoperabilidad Arrow**   | Lee y escribe datos directamente en formato columnares Arrow/Parquet.     |
| 💾 **Gran capacidad de lectura** | `read_csv` y `read_parquet` extremadamente rápidos.                       |
| 🧮 **Ideal para IA/ML**          | Evita transferencias CPU↔GPU al entrenar modelos en TensorFlow o PyTorch. |

---

## ⚠️ Inconvenientes

| Inconveniente                    | Explicación                                                    |
| -------------------------------- | -------------------------------------------------------------- |
| 🚫 **Dependencia de GPU NVIDIA** | No funciona en CPU ni con AMD.                                 |
| 🧠 **Consumo VRAM**              | El tamaño de los datos está limitado por la memoria de la GPU. |
| 🐛 **Compatibilidad parcial**    | Algunas funciones de Pandas aún no están implementadas.        |
| 🔄 **Transferencia CPU↔GPU**     | Pasar datos grandes entre CPU y GPU tiene coste.               |
| 🧩 **Instalación compleja**      | Requiere CUDA Toolkit y drivers específicos.                   |

---

## 💡 Buenas prácticas

1. **Evita mover datos entre CPU↔GPU** continuamente.

   * Crea los DataFrames directamente en GPU (`cudf.read_csv`).
2. **Aprovecha formatos columnares** (Parquet, ORC) para máxima velocidad.
3. **Usa Dask-cuDF** para datasets mayores que la VRAM.
4. **Convierte Pandas a cuDF** solo cuando el dataset sea lo bastante grande.

   ```python
   gdf = cudf.from_pandas(pdf)
   ```
5. **Verifica uso de memoria GPU**

   ```python
   import rmm
   print(rmm.get_info())
   ```

---

## 🧩 Ejemplo de flujo EDA

```python
import cudf

df = cudf.read_csv("ventas.csv")

# 1️⃣ Limpieza
df = df.dropna().drop_duplicates()

# 2️⃣ Estadísticos
print(df.describe())

# 3️⃣ Agrupación
print(df.groupby("categoria")["importe"].mean())

# 4️⃣ Normalización
df["importe_norm"] = (df["importe"] - df["importe"].min()) / (df["importe"].max() - df["importe"].min())

# 5️⃣ Correlaciones
print(df[["edad","importe","satisfaccion"]].corr())
```

---

## 🧩 Integración con PyTorch y TensorFlow

Una de las grandes ventajas de cuDF es su interoperabilidad directa con frameworks de IA.

```python
import torch
import cudf

gdf = cudf.DataFrame({"x": [1,2,3], "y": [10,20,30]})
tensor = torch.as_tensor(gdf.to_cupy())  # convierte a tensor GPU
```

✅ Sin pasar por CPU → evita cuellos de botella en entrenamiento.

---

## 🧠 Comparativa general

| Criterio                | Pandas (CPU)               | cuDF (GPU)                   |
| ----------------------- | -------------------------- | ---------------------------- |
| Backend                 | NumPy / PyArrow            | CUDA                         |
| Hardware                | CPU                        | GPU NVIDIA                   |
| Rendimiento             | Medio                      | 5×–100× más rápido           |
| Tamaño ideal de dataset | Pequeño / mediano          | Grande                       |
| API                     | Pythonic                   | Pythonic (idéntica a Pandas) |
| Memoria                 | RAM del sistema            | VRAM GPU                     |
| Interoperabilidad       | NumPy, Arrow, DuckDB       | Arrow, cuML, cuGraph         |
| Ideal para              | Análisis general, docencia | Big Data y ML en GPU         |

---

## 🚀 Ecosistema RAPIDS

| Librería    | Función                   | Equivalente en CPU |
| ----------- | ------------------------- | ------------------ |
| `cuDF`      | Manipulación de datos     | Pandas             |
| `cuML`      | Machine Learning          | scikit-learn       |
| `cuGraph`   | Análisis de grafos        | NetworkX           |
| `cuIO`      | Entrada/salida de datos   | pandas.io          |
| `cuXfilter` | Visualización GPU         | Plotly/Dash        |
| `Dask-cuDF` | Procesamiento distribuido | Dask / Spark       |

---

## 🧩 Conclusión

* **cuDF** ofrece una alternativa de alto rendimiento a Pandas basada en GPU.
* Ideal para **datasets grandes** y **pipelines de IA o Big Data** donde la GPU ya está presente.
* Forma parte del ecosistema **RAPIDS**, por lo que se integra naturalmente con otras herramientas de Machine Learning y análisis acelerado.

> 🧭 En resumen:
>
> * Usa **Pandas** para exploración y datasets pequeños.
> * Usa **cuDF** cuando trabajes en GPU o con datos masivos.
> * Combina cuDF + cuML + cuGraph para un flujo completo 100% GPU.

```

