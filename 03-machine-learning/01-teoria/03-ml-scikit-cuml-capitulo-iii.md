# III. Aprendizaje No Supervisado (Unsupervised Learning) 🧩

El aprendizaje no supervisado se centra en encontrar patrones ocultos o estructuras intrínsecas en datos sin etiquetas (la variable de salida $Y$ no está definida).

## A. Clustering (Agrupamiento)

### 3.A.1. K-Means (`KMeans`)

K-Means es un algoritmo iterativo que agrupa puntos de datos en $k$ grupos, minimizando la inercia (la suma de las distancias al cuadrado dentro de cada grupo).

| Característica | Scikit-learn (`sklearn.cluster`) | CuML (`cuml.cluster`) |
| :--- | :--- | :--- |
| **API** | `KMeans(n_clusters=8, init='k-means++')` | `KMeans(n_clusters=8, init='k-means++')` |
| **Inicialización** | Soporta `random`, `k-means++`. | Soporta `random`, `k-means++`. CuML utiliza implementaciones de inicialización `k-means++` altamente paralelizadas en la GPU. |
| **Rendimiento** | La velocidad está limitada por la búsqueda de centroides en la CPU. | **Altamente acelerado**. La distancia y la reasignación de clústeres son cálculos vectorizados que se benefician masivamente del paralelismo de la GPU. |
| **Distancias** | Utiliza la distancia euclidiana estándar. | Implementa kernels de distancias en GPU para un cálculo extremadamente rápido. |

**Nota Importante:** K-Means es uno de los algoritmos que muestra una de las mayores ganancias de velocidad al migrar a CuML, especialmente con conjuntos de datos muy grandes.

#### Ejemplo rápido (KMeans GPU)

```python
import cudf
from cuml.cluster import KMeans
from sklearn.datasets import make_blobs

X_np, _ = make_blobs(n_samples=100000, centers=10, n_features=20, random_state=0)
X_gdf = cudf.DataFrame(X_np.astype('float32'))

km = KMeans(n_clusters=10, init='k-means++', max_iter=300)
km.fit(X_gdf)
labels = km.predict(X_gdf)
```

### 3.A.2. DBSCAN (`DBSCAN`)

DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*) agrupa puntos que están densamente conectados, siendo ideal para encontrar clústeres de forma irregular y detectar el ruido (outliers).

| Característica | Scikit-learn (`sklearn.cluster`) | CuML (`cuml.cluster`) |
| :--- | :--- | :--- |
| **API** | `DBSCAN(eps=0.5, min_samples=5)` | `DBSCAN(eps=0.5, min_samples=5)` |
| **Core del Algoritmo** | Depende en gran medida de algoritmos de búsqueda de vecinos basados en la CPU. | El cuello de botella de DBSCAN es la búsqueda de vecinos, que CuML acelera drásticamente utilizando sus eficientes algoritmos de búsqueda en la GPU (similares a k-NN). |
| **Escalabilidad** | El tiempo de ejecución escala mal con el tamaño de los datos. | El tiempo de ejecución se reduce considerablemente, haciendo que **DBSCAN sea viable para conjuntos de datos mucho mayores** que con scikit-learn. |

#### Ejemplo rápido (DBSCAN GPU)

```python
import cudf
from cuml.cluster import DBSCAN
from sklearn.datasets import make_blobs

X_np, _ = make_blobs(n_samples=50000, centers=5, n_features=10, random_state=0)
X_gdf = cudf.DataFrame(X_np.astype('float32'))

db = DBSCAN(eps=0.5, min_samples=5)
db.fit(X_gdf)
labels = db.labels_
```

---

## B. Reducción de Dimensionalidad (Dimensionality Reduction)

### 3.B.1. Análisis de Componentes Principales (PCA, `PCA`)

PCA es una técnica lineal fundamental que transforma los datos a un nuevo espacio de menor dimensión, reteniendo la mayor varianza posible.

| Característica | Scikit-learn (`sklearn.decomposition`) | CuML (`cuml.decomposition`) |
| :--- | :--- | :--- |
| **API** | `PCA(n_components=10)` | `PCA(n_components=10)` |
| **Método Principal** | Descomposición en valores singulares (SVD) en la CPU (usando LAPACK/SciPy). | SVD y Eigendecomposition **aceleradas por GPU** (usando la biblioteca **cuSOLVER**). |
| **Rendimiento** | Eficiente, pero limitado por el rendimiento de una sola CPU en operaciones de álgebra lineal densa. | **Extremadamente rápido** para matrices grandes y densas. Los cálculos matriciales subyacentes son la razón de ser de la GPU. |
| **Transformación** | El método `.transform()` (proyectar nuevos datos) es idéntico y altamente acelerado en CuML. |

#### Ejemplo rápido (PCA GPU)

```python
import cudf
from cuml.decomposition import PCA
from sklearn.datasets import make_classification

X_np, _ = make_classification(n_samples=80000, n_features=50, random_state=0)
X_gdf = cudf.DataFrame(X_np.astype('float32'))

pca = PCA(n_components=10, whiten=False)
X_reduced = pca.fit_transform(X_gdf)
```

### 3.B.2. UMAP / T-SNE

Estos son algoritmos de incrustación (embedding) no lineal que se utilizan principalmente para la visualización de datos de alta dimensión.

| Característica | Scikit-learn (Ecosistema) | CuML (`cuml.manifold`) |
| :--- | :--- | :--- |
| **t-SNE** | Disponible (`sklearn.manifold.TSNE`). | **No disponible** en CuML directamente. Es un algoritmo difícil de paralelizar para GPU. |
| **UMAP** | No está en scikit-learn (es una librería externa: `umap-learn`). | **Implementación nativa y altamente acelerada**. |
| **Recomendación CuML** | Si necesita una incrustación no lineal, **UMAP** es la alternativa de CuML para t-SNE, siendo mucho más rápida y más escalable en la GPU. |

#### Ejemplo rápido (UMAP GPU)

```python
import cudf
from cuml.manifold import UMAP
from sklearn.datasets import load_digits

digits = load_digits()
X_gdf = cudf.DataFrame(digits.data.astype('float32'))

umap = UMAP(n_neighbors=15, min_dist=0.1, n_components=2)
embedding = umap.fit_transform(X_gdf)
```

### 3.B.3. GaussianMixture / GMM

| Característica | Scikit-learn (`sklearn.mixture`) | CuML |
| :--- | :--- | :--- |
| **API** | `GaussianMixture` (EM) | No implementado (a fecha de hoy). |
| **Alternativa** | Agrupamientos suaves no disponibles en CuML; considera **KMeans** + etiquetado probabilístico o modelos en PyTorch/TensorFlow si necesitas GPU. |

#### Ejemplo orientativo (suavizado post KMeans)

```python
# No hay GMM en CuML; aproximar probabilidades con distancias a centroides de KMeans
import cupy as cp
from cuml.cluster import KMeans

# Suponiendo X_cp (CuPy) y km entrenado
distances = km.transform(X_gdf)  # distancia a cada centro
proba_like = 1 / (1 + cp.asarray(distances))
proba_like = proba_like / proba_like.sum(axis=1, keepdims=True)
```

### 3.B.4. Detección de Anomalías (IsolationForest / LOF)

- **scikit-learn:** `IsolationForest`, `LocalOutlierFactor`.
- **CuML:** soporte limitado/experimental; en GPU, alternativas suelen ser **DBSCAN** para puntos ruido o modelos de autoencoders (DL). Para producción en GPU, considera cuML experimental o frameworks de deep learning.

#### Ejemplo práctico usando DBSCAN para outliers

```python
import cudf
from cuml.cluster import DBSCAN

# Si label = -1 en DBSCAN, se considera ruido/anomalía
db = DBSCAN(eps=0.3, min_samples=5).fit(X_gdf)
anomalies = X_gdf[db.labels_ == -1]
```

### 3.B.5. MiniBatchKMeans y escalado

- **scikit-learn:** `MiniBatchKMeans` para datasets grandes en CPU.
- **CuML:** KMeans ya está altamente paralelizado; usa `max_iter` y `batch_size` según VRAM. Para más grande aún, ver Dask-cuML KMeans distribuido.

### 3.B.6. Notas prácticas

- **t-SNE ausente** en CuML: usa UMAP como alternativa acelerada.
- **NearestNeighbors**: cuML tiene `NearestNeighbors`; útil como bloque base para DBSCAN/LOF-like en GPU.
- **Visualización**: tras reducción (PCA/UMAP), puedes convertir a pandas para graficar (`to_pandas()`), o usar librerías que acepten cuDF/CuPy directamente (limitado).

***
