# I. Introducción y Conceptos Fundamentales 🚀

Este apartado establece la base para entender por qué y cómo CuML se compara con scikit-learn, centrándose en los requisitos de hardware y el crucial manejo de datos.

## 1.1. Introducción: Propósito y Alcance

* **Scikit-learn (El Estándar CPU):** Es la biblioteca de facto para el *Machine Learning* (ML) en Python. Está diseñada para el **cálculo de propósito general en CPU**, es fácil de usar y cuenta con una API madura y estable. Está optimizada para conjuntos de datos que caben en la RAM del sistema.
* **CuML (La Aceleración GPU):** Es la biblioteca central de ML del proyecto de código abierto **NVIDIA RAPIDS**. Su principal objetivo es proporcionar una **aceleración masiva** para los mismos algoritmos que scikit-learn, delegando la computación a las **GPUs de NVIDIA** mediante la arquitectura **CUDA**.
* **Filosofía de la API:** La documentación de CuML se esfuerza por mantener una **paridad de la API** con scikit-learn. Esto significa que la mayoría de los métodos y parámetros son idénticos, facilitando una transición fluida para los usuarios que buscan acelerar su código existente.

---

## 1.2. El Ecosistema RAPIDS: CuML, cuDF, CuPy

Para que CuML funcione eficientemente, necesita que todo el *pipeline* de datos (desde la carga hasta el preprocesamiento) también se ejecute en la GPU, minimizando las costosas transferencias de CPU a GPU. Esto se logra con el ecosistema RAPIDS:

| Herramienta | Función | Equivalente en el ecosistema CPU |
| :--- | :--- | :--- |
| **CuML** | Algoritmos de Machine Learning. | **Scikit-learn** |
| **cuDF** | DataFrames y manipulación de datos en GPU. | **Pandas** |
| **CuPy** | Arrays N-dimensionales en GPU (para manipulación de tensores). | **NumPy** |



**Nota:** Es crucial que los datos se carguen y permanezcan en formatos de RAPIDS (cuDF/CuPy) **antes** de llamar a `.fit()` de CuML.

---

## 1.3. Manejo de Datos y Memoria: NumPy vs. CuPy/cuDF

La principal diferencia operativa y de rendimiento radica en cómo se almacenan los datos.

* **Scikit-learn:** Acepta datos como **arrays de NumPy** o DataFrames de Pandas, que residen en la **RAM del sistema (memoria de la CPU)**.
* **CuML:** Acepta datos como **arrays de CuPy** o DataFrames de cuDF, que residen en la **VRAM (memoria de la GPU)**.

### Transferencia de Datos

Para que CuML pueda procesar tus datos, la transferencia entre la CPU y la GPU es inevitable si el origen de los datos está en la RAM.

| Origen/Destino | Clase de Datos | Ejemplo de Conversión (Python) |
| :--- | :--- | :--- |
| **CPU a GPU** | Array de NumPy a Array de CuPy | `cp_array = cupy.asarray(np_array)` |
| **GPU a CPU** | Array de CuPy a Array de NumPy | `np_array = cp_array.get()` |
| **CPU a GPU** | Pandas DataFrame a cuDF DataFrame | `cudf_df = cudf.from_pandas(pd_df)` |

**Advertencia:** Mover datos entre la CPU y la GPU es una **operación lenta**. La clave para un rendimiento óptimo con CuML es **minimizar estas transferencias** (idealmente, cargar y procesar los datos directamente en la GPU usando cuDF/CuPy).

---

## 1.4. Requisitos de Hardware y Software (CUDA Toolkit)

| Requisito | Scikit-learn (CPU) | CuML (GPU) |
| :--- | :--- | :--- |
| **Hardware** | Cualquier CPU moderna. | **Tarjeta Gráfica NVIDIA compatible con CUDA** (Generalmente arquitectura Pascal o superior). |
| **Software** | Python 3+, NumPy, SciPy. | **CUDA Toolkit** (versión específica, crucial), **Controladores (Drivers)** de NVIDIA, y las librerías de RAPIDS. |

**El Factor CUDA:** CuML depende fundamentalmente de la plataforma de computación paralela **CUDA de NVIDIA**. Sin el hardware y el *toolkit* de software de NVIDIA instalados y configurados correctamente, CuML **no se ejecutará**.

### 1.4.1. Instalación y Compatibilidad

| Componente | Versión típica | Notas |
| :--- | :--- | :--- |
| **Driver NVIDIA** | >= versión recomendada por la release de RAPIDS | Debe ser **mayor o igual** que la de CUDA Toolkit instalada. |
| **CUDA Toolkit** | 11.x / 12.x según release | RAPIDS publica matrices de compatibilidad por versión. |
| **RAPIDS/cuML** | `conda install -c rapidsai -c conda-forge rapids=XX.X python=3.10 cuda-version=11.8` | Usa entorno `conda` separado. |
| **Docker** | `rapidsai/rapidsai` | Alternativa lista para usar, conveniente en Colab/Kaggle con GPU. |

### 1.4.2. Verificación Rápida del Entorno

```python
import cuml
import cudf
import cupy as cp
print("cuML", cuml.__version__)
print("cuDF", cudf.__version__)
print("GPU disponible?", cp.cuda.runtime.getDeviceCount() > 0)
```

Si `getDeviceCount()` es 0, revisa drivers/CUDA. En Dask-CUDA (`LocalCUDACluster`) también se detectan GPUs.

### 1.4.3. Tabla rápida de compatibilidad (ejemplo)

| RAPIDS/cuML | CUDA Toolkit | Driver NVIDIA (mín.) | Python |
| :--- | :--- | :--- | :--- |
| 24.02 | 12.2 | >= 535.x | 3.10/3.11 |
| 23.12 | 11.8 | >= 525.x | 3.10 |

Consulta siempre la matriz oficial de la release usada.

---

## 1.5. Consideraciones de Rendimiento: CPU vs. GPU

La principal ventaja de CuML es el rendimiento, pero este depende de la naturaleza del algoritmo y el tamaño del dataset.

| Factor | Scikit-learn (CPU) | CuML (GPU) |
| :--- | :--- | :--- |
| **Paralelismo** | Limitado al número de núcleos de la CPU (decenas). | Alto paralelismo (miles de núcleos) para operaciones masivas. |
| **Tamaño de Datos** | Ideal para datasets medianos (caben en RAM). | Ideal para **datasets grandes** donde el paralelismo supera la sobrecarga de la GPU. |
| **Cuello de Botella** | La velocidad de un solo núcleo o la RAM. | La **VRAM** (si el dataset excede la VRAM, el proceso falla o debe ser distribuido). |

**Regla General:** Para datasets pequeños o medianos, la sobrecarga de la transferencia a la GPU puede hacer que CuML sea más lento que scikit-learn. **CuML brilla cuando los datasets son lo suficientemente grandes** como para justificar el poder de la GPU.

### 1.6. Buenas Prácticas de Datos y Memoria

- **Mantén los datos en GPU**: carga con cuDF (`cudf.read_csv`) o convierte temprano (`cudf.from_pandas`), evita idas y vueltas CPU↔GPU.
- **Usa `float32` por defecto**: duplica la capacidad en VRAM frente a `float64`; muchos modelos de CuML trabajan en `float32`.
- **Batching/Chunking**: si estás cerca del límite de VRAM, procesa en lotes o usa Dask-CUDA para distribuir.
- **Columnas categóricas**: preferir `CategoricalDtype` en cuDF; ahorra memoria y acelera `OneHotEncoder` de CuML.
- **Medición**: `cudf.utils.dtypes.may_have_object` para detectar columnas que requieren conversión; `rmm.get_info()` (si usas RMM) para memoria.

### 1.7. Flujo de Trabajo Patrón (CPU→GPU mínimo)

1) **Carga directa a cuDF**: `df = cudf.read_csv(...)`.
2) **Preprocesa en GPU**: `cuml.preprocessing.StandardScaler`, `OneHotEncoder` (evita sklearn en CPU).
3) **Modelo CuML**: `.fit`/`.predict` con estimadores CuML.
4) **Métricas en GPU**: `cuml.metrics` para evitar copiar resultados a CPU (o `to_pandas()` si el set es pequeño).

### 1.8. Cuándo NO usar GPU

- Dataset pequeño/estrecho (<50k filas y pocas columnas): la sobrecarga de copia puede ser mayor que el beneficio.
- Falta de soporte de algún parámetro crítico (p.ej. kernel RBF en SVM): mantén sklearn o usa alternativa (XGBoost GPU).
- Entornos sin GPU NVIDIA/driver adecuado.

### 1.9. Regla práctica CPU vs GPU (tamaño)

| Filas x columnas | Recomendación |
| :--- | :--- |
| < 50k filas y < 50 cols | Prueba primero CPU (sklearn). |
| 50k – 1M filas | Evalúa ambos; mide incluyendo copia de datos. |
| > 1M filas o mucha ingeniería de features | GPU (cuDF + CuML); considera Dask si no cabe en VRAM. |

***
