# II. Aprendizaje Supervisado (Supervised Learning) 🎯

Esta sección compara las implementaciones de los algoritmos de clasificación y regresión más comunes en **scikit-learn** y **CuML**.

### Tabla rápida de equivalencias y límites

| Algoritmo | scikit-learn | CuML | Notas/Limitaciones |
| :--- | :--- | :--- | :--- |
| LogisticRegression | Sí | Sí | CuML solo solvers GPU; kernel solo lineal. |
| KNN (clas/reg) | Sí | Sí | Gran aceleración en GPU. |
| SVM (SVC/SVR) | Sí (kernels RBF/polynomial) | Solo lineal | Usa XGBoost/NN para no linealidad en GPU. |
| Árboles / RandomForest | Sí | Sí | `sample_weight`/`class_weight` soporte parcial en CuML. |
| GradientBoosting / HGB | Sí (CPU) | No | Usar XGBoost/LightGBM GPU. |
| Naive Bayes | Sí | Parcial (según versión) | Gaussian/MultiNB en cuML. |
| ElasticNet / Ridge / Lasso | Sí | Sí | Paridad de API. |
| Baselines (Dummy, Voting, Stacking) | Sí | No | Combinar manualmente en GPU. |

## A. Clasificación (Classification)

La clasificación es la tarea de predecir una etiqueta categórica (p. ej., "fraude" o "no fraude", "perro" o "gato").

### 2.A.1. Regresión Logística (`LogisticRegression`)

La Regresión Logística es un modelo lineal fundamental para la clasificación binaria, aunque la API de scikit-learn también soporta la clasificación multiclase (OVR/multinomial).

| Característica | Scikit-learn (`sklearn.linear_model`) | CuML (`cuml.linear_model`) |
| :--- | :--- | :--- |
| **API** | `LogisticRegression()` | `LogisticRegression()` (Paridad de API) |
| **Solvers Disponibles** | Amplia gama: `lbfgs`, `liblinear`, `newton-cg`, etc. | Limitado, se enfoca en solvers optimizados para GPU como **L-BFGS** y **Proximal IRLS**. |
| **Parámetro `penalty`** | L1, L2, ElasticNet. | Soporte completo para penalizaciones L1 y L2 (regularización). |
| **Entrada de Datos** | Arrays **NumPy** o Pandas. | Arrays **CuPy** o DataFrames cuDF. |

#### ⚠️ Consideración Clave para CuML

El solver **Proximal IRLS** en CuML es típicamente el más rápido y eficiente para grandes conjuntos de datos en la GPU, superando a las implementaciones L-BFGS de la CPU. Sin embargo, si tu modelo de scikit-learn utiliza un solver que no está implementado en CuML (como `liblinear`), tendrás que cambiar el solver al migrar.

### 2.A.2. Clasificación de Vecinos Más Cercanos (k-NN, `KNeighborsClassifier`)

#### Ejemplo rápido (k-NN)

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from cuml.neighbors import KNeighborsClassifier
import cudf

X_np, y_np = load_wine(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X_np, y_np, test_size=0.2, random_state=42)

X_tr_gdf = cudf.DataFrame(X_tr)
X_te_gdf = cudf.DataFrame(X_te)
y_tr_gdf = cudf.Series(y_tr)

knn_gpu = KNeighborsClassifier(n_neighbors=5)
knn_gpu.fit(X_tr_gdf, y_tr_gdf)
pred = knn_gpu.predict(X_te_gdf)
```

El k-NN es un algoritmo de clasificación no paramétrico que se basa en el cálculo de distancias.

| Característica | Scikit-learn (`sklearn.neighbors`) | CuML (`cuml.neighbors`) |
| :--- | :--- | :--- |
| **API** | `KNeighborsClassifier(n_neighbors=5)` | `KNeighborsClassifier(n_neighbors=5)` |
| **Estrategia Principal** | Búsqueda exhaustiva o árboles de baja dimensionalidad (`BallTree`, `KDTree`). | Se centra en el uso de estructuras de datos optimizadas para GPU (como **algoritmos de fuerza bruta o aproximados**) para la búsqueda de vecinos, aprovechando su paralelismo masivo. |
| **Rendimiento** | Lento en conjuntos de datos y dimensiones grandes. | Aceleración **masiva**; uno de los mayores aumentos de rendimiento al migrar a CuML, ya que la búsqueda de distancias es altamente paralela. |
| **Métodos** | `.fit()`: entrena/almacena los datos. `.kneighbors()`: calcula las distancias. | `.fit()` y `.kneighbors()` son idénticos. |

### 2.A.3. Máquinas de Vectores de Soporte (SVM) para Clasificación (`SVC`)

#### Ejemplo rápido (SVM lineal GPU)

```python
import cupy as cp
from cuml.svm import LinearSVC
from sklearn.datasets import make_classification

X_np, y_np = make_classification(n_samples=5000, n_features=20, random_state=0)
X_cp, y_cp = cp.asarray(X_np), cp.asarray(y_np)

svc_gpu = LinearSVC(max_iter=1000)
svc_gpu.fit(X_cp, y_cp)
pred = svc_gpu.predict(X_cp)
```

Las SVM son modelos robustos que encuentran el hiperplano óptimo para separar clases.

| Característica | Scikit-learn (`sklearn.svm`) | CuML (`cuml.svm`) |
| :--- | :--- | :--- |
| **Implementación** | Basado en **libsvm**; soporta kernels lineales y no lineales (RBF, Polinomial). | Implementa algoritmos de **GPU altamente escalables** enfocados en la velocidad. |
| **Soporte de Kernels** | **Completo.** Los kernels son la característica definitoria de SVM. | Actualmente, CuML se enfoca casi exclusivamente en **SVM Lineal**. |
| **Motivo de la Diferencia** | La optimización de kernels no lineales a gran escala en paralelo para GPU es compleja y a menudo ineficiente. CuML prioriza la **escalabilidad lineal** sobre la flexibilidad del kernel. |

**Conclusión:** Para la SVM, si su caso de uso requiere un kernel no lineal (RBF) o es de pequeño a mediano tamaño, **scikit-learn** es la opción. Si necesita una SVM lineal para un conjunto de datos **masivo**, **CuML** es la alternativa más rápida.

#### Ejemplo rápido (CPU vs GPU)

```python
# Datos de ejemplo (pandas/NumPy en CPU)
from sklearn.datasets import load_breast_cancer
X_np, y_np = load_breast_cancer(return_X_y=True)

# CPU: sklearn
from sklearn.linear_model import LogisticRegression
log_cpu = LogisticRegression(max_iter=1000)
log_cpu.fit(X_np, y_np)

# GPU: CuML (convertir a CuPy)
import cupy as cp
from cuml.linear_model import LogisticRegression as cuLogReg
X_cp, y_cp = cp.asarray(X_np), cp.asarray(y_np)
log_gpu = cuLogReg(max_iter=1000)
log_gpu.fit(X_cp, y_cp)
```

### 2.A.4. Árboles y Random Forest

| Característica | Scikit-learn (`sklearn.tree`, `sklearn.ensemble`) | CuML (`cuml.ensemble`) |
| :--- | :--- | :--- |
| **API** | `DecisionTreeClassifier`, `RandomForestClassifier`, `ExtraTreesClassifier`. | `RandomForestClassifier` (paridad básica). |
| **Parámetros clave** | `max_depth`, `n_estimators`, `max_features`, `min_samples_leaf`. | Idénticos en nombre; algunos parámetros menos soportados (p.ej. `class_weight` parcial o no soportado según versión). |
| **Rendimiento** | CPU multi-hilo; escalado aceptable en conjuntos medianos. | Gran aceleración en bosques grandes; lectura de datos debe ser cuDF/CuPy. |
| **Limitaciones** | Soporte completo de `sample_weight`, `class_weight`. | `sample_weight`/`class_weight` pueden no estar soportados o estar en experimental. |

**Migración:** Cambia el import a `from cuml.ensemble import RandomForestClassifier` y usa datos en cuDF/CuPy. Ajusta `n_estimators` a valores mayores: la GPU amortiza el coste con más árboles.

#### Ejemplo rápido (Random Forest)

```python
import cudf
from cuml.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine

X_np, y_np = load_wine(return_X_y=True)
X_gdf = cudf.DataFrame(X_np)
y_gdf = cudf.Series(y_np)

rf_gpu = RandomForestClassifier(n_estimators=400, max_depth=12, random_state=42)
rf_gpu.fit(X_gdf, y_gdf)
pred_gpu = rf_gpu.predict(X_gdf)
```

### 2.A.5. Gradient Boosting / HistGradientBoosting

- **scikit-learn:** `GradientBoostingClassifier` (CPU), `HistGradientBoostingClassifier` optimizado CPU.
- **GPU recomendado:** usar **XGBoost** con `tree_method='gpu_hist'` (acepta cuDF/CuPy) o LightGBM-GPU. CuML no tiene un HGB nativo.

### 2.A.6. Naive Bayes

- **scikit-learn:** `GaussianNB`, `MultinomialNB`, `ComplementNB`.
- **CuML:** Implementaciones para Gaussian/MultiNB con API similar (dependiente de versión). Caso de texto vectorizado puede moverse a GPU con CuPy o cuDF.

-----

### B. Regresión (Regression)

La regresión es la tarea de predecir un valor numérico continuo (p. ej., precio de la vivienda, temperatura).

### 2.B.1. Regresión Lineal (Simple, Ridge, Lasso)

La base de los modelos predictivos, resolviendo el problema de mínimos cuadrados.

| Algoritmo | Scikit-learn (`sklearn.linear_model`) | CuML (`cuml.linear_model`) |
| :--- | :--- | :--- |
| **Regresión Lineal Simple** | `LinearRegression()` | `LinearRegression()` |
| **Ridge** | `Ridge()` | `Ridge()` |
| **Lasso** | `Lasso()` | `Lasso()` |
| **Solvers** | Utiliza optimizaciones de CPU (p. ej., LAPACK). | Utiliza algoritmos de álgebra lineal de GPU optimizados (p. ej., **cuBLAS** y **cuSOLVER**), lo que resulta en una gran aceleración. |

#### 🛠️ Ejemplo de Código Comparativo (Regresión Lineal)

Este ejemplo ilustra la paridad de la API y la necesidad de usar arrays de CuPy:

```python
# Scikit-learn (CPU)
import numpy as np
from sklearn.linear_model import LinearRegression

X_np, y_np = np.random.rand(1000, 10), np.random.rand(1000)
model_cpu = LinearRegression().fit(X_np, y_np)

# CuML (GPU)
import cupy as cp
from cuml.linear_model import LinearRegression

X_cp, y_cp = cp.asarray(X_np), cp.asarray(y_np)
model_gpu = LinearRegression().fit(X_cp, y_cp) 
# model_gpu predice sobre X_cp y retorna un array de CuPy
```

### 2.B.2. Regresión de Vecinos Más Cercanos (`KNeighborsRegressor`)

#### Ejemplo rápido (k-NN Regressor)

```python
from cuml.neighbors import KNeighborsRegressor
from sklearn.datasets import fetch_california_housing
import cudf

X_np, y_np = fetch_california_housing(return_X_y=True)
X_gdf = cudf.DataFrame(X_np.astype('float32'))
y_gdf = cudf.Series(y_np.astype('float32'))

knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_gdf, y_gdf)
preds = knn_reg.predict(X_gdf)
```

Análogo a k-NN para clasificación, pero predice el promedio (o mediana) de las etiquetas de sus vecinos.

  * **Paridad de API:** `KNeighborsRegressor()` es idéntico en scikit-learn y CuML.
  * **Ventaja de CuML:** La fase de entrenamiento es trivial (almacenar datos), pero la fase de predicción (cálculo de distancias y promedios) se beneficia de la misma **aceleración masiva de GPU** que se ve en el clasificador k-NN.

### 2.B.3. Máquinas de Vectores de Soporte (SVM) para Regresión (`SVR`)

SVR, al igual que SVC, utiliza el concepto de margen de tolerancia $(\epsilon)$ para la predicción.

  * **Soporte de Kernels:** Al igual que SVC, **CuML se centra en el SVR Lineal** para priorizar la escalabilidad en la GPU.
  * **scikit-learn** soporta kernels no lineales (RBF, Polinomial) para SVR.

#### Ejemplo rápido (Linear SVR GPU)

```python
import cupy as cp
from cuml.svm import LinearSVR
from sklearn.datasets import make_regression

X_np, y_np = make_regression(n_samples=8000, n_features=15, noise=0.1, random_state=0)
X_cp, y_cp = cp.asarray(X_np), cp.asarray(y_np)

svr_gpu = LinearSVR(max_iter=1000)
svr_gpu.fit(X_cp, y_cp)
pred = svr_gpu.predict(X_cp)
```

### 2.B.4. ElasticNet y regularización mixta

#### Ejemplo rápido (ElasticNet GPU)

```python
import cupy as cp
from cuml.linear_model import ElasticNet
from sklearn.datasets import make_regression

X_np, y_np = make_regression(n_samples=5000, n_features=30, noise=0.2, random_state=0)
X_cp, y_cp = cp.asarray(X_np), cp.asarray(y_np)

en_gpu = ElasticNet(alpha=0.1, l1_ratio=0.5, max_iter=1000)
en_gpu.fit(X_cp, y_cp)
pred = en_gpu.predict(X_cp)
```

| Característica | Scikit-learn (`ElasticNet`) | CuML (`ElasticNet`) |
| :--- | :--- | :--- |
| **Parámetros** | `alpha`, `l1_ratio`, `max_iter`, `tol`. | Mismos nombres; resolución en GPU. |
| **Uso** | `ElasticNet()` como compromiso L1/L2. | Idéntico, sobre datos CuPy/cuDF. |

### 2.B.5. Random Forest / ExtraTrees Regressor

Paridad similar a la sección de clasificación: importa desde `cuml.ensemble`, atención a soporte parcial de `sample_weight`.

#### Ejemplo rápido (RF Regressor)

```python
import cudf
from cuml.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing

X_np, y_np = fetch_california_housing(return_X_y=True)
X_gdf = cudf.DataFrame(X_np.astype('float32'))
y_gdf = cudf.Series(y_np.astype('float32'))

rf_reg = RandomForestRegressor(n_estimators=300, max_depth=16, random_state=42)
rf_reg.fit(X_gdf, y_gdf)
preds = rf_reg.predict(X_gdf)
```

### 2.B.6. Gradient Boosting Regressor

- **scikit-learn:** `GradientBoostingRegressor`, `HistGradientBoostingRegressor`.
- **GPU recomendado:** **XGBoost** (`tree_method='gpu_hist'`) para boostings con gran número de árboles. CuML no expone HGB nativo.

#### Ejemplo rápido (XGBoost GPU)

```python
import cudf
import xgboost as xgb
from sklearn.datasets import fetch_california_housing

X_np, y_np = fetch_california_housing(return_X_y=True)
X_gdf = cudf.DataFrame(X_np.astype('float32'))
y_gdf = cudf.Series(y_np.astype('float32'))

dtrain = xgb.DMatrix(X_gdf, label=y_gdf)
params = {
    'tree_method': 'gpu_hist',
    'objective': 'reg:squarederror',
    'max_depth': 8,
    'learning_rate': 0.1,
}
bst = xgb.train(params, dtrain, num_boost_round=200)
preds = bst.predict(dtrain)
```

### 2.B.7. Baselines y notas

- **Baselines (`DummyRegressor/Classifier`)** no existen en CuML; usa sklearn en CPU para referencia rápida.
- **PolynomialFeatures**: usa `cuml.preprocessing.PolynomialFeatures` para generar features en GPU antes de un modelo lineal CuML.

### Ejemplo de migración sklearn → CuML con Pipeline

```python
# scikit-learn (CPU)
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

pipe_cpu = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
pipe_cpu.fit(X_np, y_np)

# CuML (GPU)
import cudf
from cuml.preprocessing import StandardScaler as cuStandardScaler
from cuml.linear_model import LogisticRegression as cuLogReg
from cuml import Pipeline as cuPipeline

X_cudf = cudf.from_pandas(pd.DataFrame(X_np))
y_cudf = cudf.Series(y_np)

pipe_gpu = cuPipeline([
    ('scaler', cuStandardScaler()),
    ('model', cuLogReg(max_iter=1000)),
])
pipe_gpu.fit(X_cudf, y_cudf)
```

### Búsqueda de hiperparámetros en GPU (loop simple)

`GridSearchCV` de sklearn trabaja en CPU; en GPU puedes iterar manualmente sobre un espacio pequeño de hiperparámetros y medir una métrica en un *hold-out* o CV ligera.

```python
import cudf
from cuml.ensemble import RandomForestClassifier
from cuml.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Suponiendo X_np, y_np ya cargados
X_tr, X_va, y_tr, y_va = train_test_split(X_np, y_np, test_size=0.2, random_state=42, stratify=y_np)
X_tr_gdf, X_va_gdf = cudf.DataFrame(X_tr), cudf.DataFrame(X_va)
y_tr_gdf, y_va_gdf = cudf.Series(y_tr), cudf.Series(y_va)

param_grid = [
    {'n_estimators': 200, 'max_depth': 10},
    {'n_estimators': 400, 'max_depth': 12},
]

best_score, best_params = -1, None
for params in param_grid:
    model = RandomForestClassifier(random_state=42, **params)
    model.fit(X_tr_gdf, y_tr_gdf)
    preds = model.predict(X_va_gdf)
    score = accuracy_score(y_va_gdf, preds)
    if score > best_score:
        best_score, best_params = score, params

print('Mejor combinación:', best_params, 'accuracy:', float(best_score))
```

Para espacios más grandes usa `RandomizedSearch` en CPU con muestreo reducido o Dask-cuML para distribuir.

-----
