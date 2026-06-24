# IV. Apartados Transversales y Especiales 🌟

Esta sección cubre temas avanzados y consideraciones sobre el ecosistema necesarias para maximizar el rendimiento de ML, especialmente en el contexto de la GPU.

## 4.1. Modelos Ensemble Acelerados (XGBoost y LightGBM) 🌲

Aunque scikit-learn y CuML tienen implementaciones básicas de `RandomForest`, el estándar de la industria para los modelos de árbol de alto rendimiento son **XGBoost** y **LightGBM**.

| Característica | Scikit-learn (Ecosistema CPU) | CuML (Ecosistema GPU/RAPIDS) |
| :--- | :--- | :--- |
| **XGBoost** | Se entrena en CPU por defecto. Es rápido, pero limitado por el número de núcleos. | Soporte nativo de GPU (mediante el parámetro `tree_method='gpu_hist'`). Es la **opción de rendimiento preferida** de RAPIDS. |
| **LightGBM** | Se entrena en CPU por defecto. | También ofrece soporte para GPU, aunque **XGBoost con GPU** suele ser la opción más probada en el ecosistema RAPIDS. |
| **Integración con Datos** | Aceptan arrays de NumPy. | Aceptan directamente arrays de **CuPy** y **cuDF** (DataFrames acelerados por GPU), eliminando copias de memoria. |

**Recomendación Clave:** Si tu *pipeline* de scikit-learn utiliza `RandomForest` y quieres aceleración, migrar a **XGBoost con el *backend* de GPU** es el salto de rendimiento más significativo.

### Bagging, Stacking y Voting

- **Bagging genérico (sklearn):** `BaggingClassifier/Regressor` solo en CPU. En GPU, usa `RandomForest` de cuML como alternativa bagging acelerada.
- **Stacking (sklearn):** `StackingClassifier/Regressor` no existe en cuML. En GPU puedes combinar modelos cuML manualmente (apilar probabilidades/predicciones en CuPy/cuDF y entrenar un meta-modelo sencillo, p. ej. `LogisticRegression` cuML sobre esas features).
- **Voting (sklearn):** `VotingClassifier/Regressor` no está en cuML; combina promedios/votos de modelos cuML en GPU (usa CuPy para promediar probabilidades).

#### Ejemplo de stacking manual en GPU

```python
import cupy as cp
from cuml.linear_model import LogisticRegression as cuLogReg

# p1, p2 son probabilidades de dos modelos cuML (arrays CuPy shape [n_samples])
p1 = cp.random.rand(1000)
p2 = cp.random.rand(1000)
X_stack = cp.vstack([p1, p2]).T  # features del meta-modelo

y = (cp.random.rand(1000) > 0.5).astype('int32')
meta = cuLogReg().fit(X_stack, y)
meta_pred = meta.predict_proba(X_stack)
```

#### Ejemplo rápido (XGBoost GPU)

```python
import xgboost as xgb
import cudf

df = cudf.DataFrame({'x1':[1,2,3,4], 'x2':[0.1,0.2,0.3,0.4], 'y':[0,1,0,1]})
dtrain = xgb.DMatrix(df[['x1','x2']], label=df['y'])
params = {
    'objective': 'binary:logistic',
    'tree_method': 'gpu_hist',
    'max_depth': 4,
}
bst = xgb.train(params, dtrain, num_boost_round=50)
pred = bst.predict(dtrain)
```

## 4.2. Módulos de Preprocesamiento (`preprocessing`)

El preprocesamiento de datos (escalado, codificación, etc.) debe realizarse en la GPU para evitar las transferencias lentas.

| Función | Scikit-learn (`sklearn.preprocessing`) | CuML (`cuml.preprocessing`) |
| :--- | :--- | :--- |
| **Escalado** | `StandardScaler`, `MinMaxScaler`. | `StandardScaler`, `MinMaxScaler`. (Paridad de API) |
| **Codificación** | `OneHotEncoder`. | `OneHotEncoder`. (Paridad de API) |
| **Transformación** | `LabelEncoder`. | `LabelEncoder`. (Paridad de API) |

**Consideración de Flujo de Trabajo:** Un *pipeline* óptimo de CuML debe usar **cuDF** para la carga/manipulación de datos, y luego el módulo `cuml.preprocessing` para preparar los datos, asegurando que los datos **nunca salgan de la VRAM** hasta la predicción.

#### Ejemplo rápido (escalado + one-hot en GPU)

```python
import cudf
from cuml.preprocessing import StandardScaler, OneHotEncoder

df = cudf.DataFrame({
    'num1': [1.0, 2.0, 3.0],
    'cat': ['a', 'b', 'a']
})

scaler = StandardScaler()
df[['num1']] = scaler.fit_transform(df[['num1']])

ohe = OneHotEncoder()
cat_enc = ohe.fit_transform(df[['cat']])  # matriz sparse en GPU
```

## 4.2.1. Pipelines en GPU

- **scikit-learn:** `Pipeline` / `ColumnTransformer` (CPU).
- **cuML:** `cuml.Pipeline` ofrece composición básica de transformador + modelo en GPU. Para transformaciones fuera de cuML, usa cuDF/cuPy + funciones personalizadas.
- **Dask-cuML:** muchos estimadores distribuidos aceptan pipelines a través de composición manual (procesa en cuDF/dask_cudf y luego modelo dask-cuML).

```python
import cudf
from cuml.preprocessing import StandardScaler
from cuml.linear_model import LogisticRegression
from cuml import Pipeline

df = cudf.DataFrame({'x1':[1,2,3], 'x2':[0.1,0.2,0.3], 'y':[0,1,0]})
X, y = df[['x1','x2']], df['y']

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(max_iter=1000)),
])
pipe.fit(X, y)
pred = pipe.predict(X)
```

Limitación: no hay equivalente directo a `ColumnTransformer` completo; para columnas mixtas, prepara manualmente (ej. `OneHotEncoder` + concatenar) antes de pasar al pipeline.

## 4.3. Métricas de Evaluación Aceleradas (`metrics`)

La evaluación del modelo es el paso final que también puede beneficiarse del paralelismo de la GPU si el conjunto de prueba es grande.

* **scikit-learn (`sklearn.metrics`):** Calcula métricas en la CPU sobre arrays de NumPy.
* **CuML (`cuml.metrics`):** Ofrece implementaciones aceleradas por GPU para métricas comunes, incluyendo:
    * `accuracy_score`
    * `r2_score` (para regresión)
    * `roc_auc_score`
    * `mean_squared_error`

**Ventaja CuML:** Si has realizado la predicción en la GPU (el resultado es un array de CuPy), usar `cuml.metrics` evita tener que transferir el resultado de la predicción a la CPU solo para calcular la puntuación final.

#### Ejemplo rápido (métricas en GPU)

```python
import cupy as cp
from cuml.metrics import accuracy_score, roc_auc_score

y_true = cp.array([0,1,1,0,1])
y_pred = cp.array([0,1,0,0,1])
y_proba = cp.array([0.2,0.9,0.4,0.1,0.8])

acc = accuracy_score(y_true, y_pred)
auc = roc_auc_score(y_true, y_proba)
```

## 4.4. Consideraciones sobre Kernels

Los métodos de núcleo (kernels) son cruciales para algoritmos como SVM (`SVC`, `SVR`).

* **CuML y Kernels:** Como se señaló en la sección II, la principal limitación de CuML frente a scikit-learn es el **soporte limitado (o nulo)** para kernels no lineales como el RBF (Radial Basis Function) en algoritmos como SVM.
* **Razón:** Los kernels no lineales en SVM requieren un cálculo matricial complejo que no se paraleliza bien o de forma eficiente en la arquitectura actual de la GPU para grandes volúmenes de datos.
* **Solución RAPIDS:** Para problemas no lineales a gran escala, la recomendación de RAPIDS es casi siempre utilizar **Modelos Ensemble basados en árboles (XGBoost GPU)** o **Redes Neuronales Profundas (PyTorch/TensorFlow)**, en lugar de SVM con kernels no lineales.

#### Listado y ejemplo de kernels

- **Disponibles en cuML SVM**: `linear` (SVC/SVR). No hay `rbf`, `poly`, `sigmoid`.
- **Disponibles en sklearn**: `linear`, `rbf`, `poly`, `sigmoid`, `precomputed`.

Ejemplo en CuML (lineal):

```python
from cuml.svm import LinearSVC
import cupy as cp

X = cp.random.rand(1000, 20)
y = (cp.random.rand(1000) > 0.5).astype('int32')
svc = LinearSVC().fit(X, y)
```

Ejemplo en sklearn con kernel RBF (CPU):

```python
from sklearn.svm import SVC
svc_rbf = SVC(kernel='rbf', C=1.0, gamma='scale').fit(X_np, y_np)
```

## 4.5. Procesamiento de Datos Masivos (Out-of-Core ML con Dask)

La principal limitación de CuML es la **VRAM de la GPU**. Si el dataset excede el tamaño de la VRAM disponible, no se puede usar una sola GPU.

* **Scikit-learn con Dask (`dask-ml`):** Permite entrenar algoritmos de scikit-learn en paralelo a través de varios núcleos de CPU o máquinas (computación distribuida).
* **CuML con Dask (`dask-cuda` y `dask-ml`):** Permite el **aprendizaje automático distribuido multi-GPU**.
    * **Funcionamiento:** Los datos se dividen en fragmentos de cuDF/CuPy, y cada fragmento reside en la VRAM de una GPU diferente. CuML coordina el entrenamiento del modelo de forma distribuida.
    * **Ejemplo mínimo:**
      ```python
      from dask_cuda import LocalCUDACluster
      from dask.distributed import Client
      import dask_cudf
      from cuml.dask.cluster import KMeans

      cluster = LocalCUDACluster()
      client = Client(cluster)

      ddf = dask_cudf.read_csv('s3://.../*.csv')
      km = KMeans(n_clusters=10)
      km.fit(ddf)
      labels = km.predict(ddf)
      ```
    * **Monitoreo:** usa el dashboard de Dask para ver VRAM y tareas.

#### Ejemplo extra: RandomForest distribuido

```python
from cuml.dask.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=200, max_depth=12, random_state=42)
rf.fit(ddf.drop('label', axis=1), ddf['label'])
pred = rf.predict(ddf)
```

## 4.6. Persistencia y Serialización

- **scikit-learn:** `joblib.dump`/`load`, `pickle`.
- **CuML:** `cuml.common.serialize` permite serializar modelos GPU; algunos estimadores soportan `save_model`/`load_model`. Si necesitas portabilidad CPU↔GPU, convierte a sklearn (si existe) o exporta a ONNX/PMML desde CPU.

#### Ejemplo rápido (serializar CuML)

```python
from cuml.common import serialize, deserialize
from cuml.linear_model import LogisticRegression
import cupy as cp

X = cp.random.rand(1000, 10)
y = (cp.random.rand(1000) > 0.5).astype('int32')
log_gpu = LogisticRegression().fit(X, y)

buf = serialize(log_gpu)
log_loaded = deserialize(buf)
pred = log_loaded.predict(X)
```

## 4.7. Interoperabilidad

- **DLPack**: mover tensores entre CuPy/cuDF y PyTorch/TF sin copia (`torch.utils.dlpack`).
- **sklearn API**: muchos estimadores CuML siguen la API `fit/predict` y funcionan en pipelines de CuML (`cuml.Pipeline`). Compatibilidad con `sklearn` puro es limitada porque espera NumPy.
- **cuML experimental**: algunos algoritmos/soportes (`class_weight`, `sample_weight`) están en módulos experimentales; revisar la versión.

#### Ejemplo (CuPy → PyTorch via DLPack)

```python
import cupy as cp
import torch

X_cp = cp.random.rand(100, 20).astype(cp.float32)
dlpack = X_cp.toDlpack()
X_torch = torch.utils.dlpack.from_dlpack(dlpack)
# X_torch comparte memoria en GPU sin copia
```

## 4.8. Troubleshooting y Limitaciones Conocidas

- **VRAM insuficiente**: reduce `n_estimators`/`max_depth`, usa `float32`, o escala con Dask-CUDA.
- **Drivers/CUDA**: asegura compatibilidad de versiones (ver Cap I). Reinicia kernel tras actualizar drivers.
- **`sample_weight`/`class_weight`**: no siempre soportados en CuML; verifica documentación de tu versión.
- **Entrada `sparse`**: soporte parcial; en algunos estimadores se requiere `dense`.
- **Kernels no lineales**: no disponibles en SVM CuML; usa GPU XGBoost o NN para no linealidad.

#### Ejemplo de comprobación de memoria antes de entrenar

```python
import rmm
info = rmm.get_info()
print("Memoria libre (bytes):", info['free'])
```

## 4.9. Benchmarks y Cuándo NO usar GPU

- **Regla práctica de tamaño**: si <50k filas y <50 features, evalúa primero en CPU; la copia a GPU puede dominar.
- **Amplitud**: matrices muy anchas (pocas filas, muchas columnas) no siempre ganan en GPU si el coste de memoria es alto.
- **Comparativa**: medir siempre CPU vs GPU con la misma métrica; incluye tiempo de copia de datos.

## 4.10. Buenas prácticas finales

- Mantén el pipeline completo en GPU (cuDF → preprocessing CuML → modelo CuML → métricas CuML).
- Usa `float32` y tipos categóricos en cuDF para ahorrar VRAM.
- Mide y monitorea: `nvidia-smi`, dashboard Dask, `rmm` si está habilitado.

**Resumen:** Para datos que son demasiado grandes para una sola GPU, la solución es la misma que en el mundo CPU: **computación distribuida**, pero utilizando las herramientas de Dask optimizadas para GPU (Dask-CUDA).

---
