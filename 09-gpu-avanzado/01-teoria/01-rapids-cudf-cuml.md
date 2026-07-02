# RAPIDS: cuDF y cuML

## Qué es RAPIDS

RAPIDS es un ecosistema open-source de NVIDIA que lleva las operaciones de ciencia de datos y machine learning a la GPU. El objetivo es ofrecer la misma API que las herramientas de CPU clásicas (Pandas, scikit-learn) pero ejecutando el trabajo en CUDA.

Los dos componentes principales para este módulo son:

| Librería | Equivalente CPU | Para qué sirve |
|----------|-----------------|----------------|
| cuDF     | Pandas          | DataFrames en GPU |
| cuML     | scikit-learn    | Algoritmos ML en GPU |

## cuDF — DataFrames en GPU

cuDF replica la API de Pandas para que el código de análisis de datos se pueda trasladar con cambios mínimos:

```python
import cudf

# Igual que pd.read_csv, pero carga directamente en GPU
df = cudf.read_csv("datos.csv")

print(df["columna"].mean())
print(df.groupby("categoria")["valor"].sum())
```

Operaciones soportadas: selección, filtrado, join, groupby, merge, apply, etc.

### Cuándo usar cuDF vs Pandas

- **Usar cuDF** cuando el DataFrame supera los cientos de miles de filas y las operaciones son repetitivas (ETL, feature engineering en producción).
- **Seguir con Pandas** para conjuntos de datos pequeños, lógica muy personalizada con `.apply`, o cuando no hay GPU disponible.

### Limitaciones de cuDF

- No todas las funciones de Pandas están implementadas.
- El overhead de copiar datos CPU↔GPU puede superar la ganancia para DataFrames pequeños.
- Requiere hardware NVIDIA con soporte CUDA.

## cuML — Machine Learning en GPU

cuML implementa algoritmos clásicos de sklearn acelerados en CUDA:

```python
from cuml.linear_model import LogisticRegression
from cuml.model_selection import train_test_split
import cudf

df = cudf.read_csv("datos.csv")
X = df[["feature1", "feature2"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
```

Algoritmos disponibles (selección):

- Clasificación: Logistic Regression, Random Forest, SVM, KNN
- Clustering: K-Means, DBSCAN
- Reducción de dimensionalidad: PCA, UMAP, TSNE
- Preprocesamiento: StandardScaler, LabelEncoder, etc.

## Arquitectura RAPIDS

```
   Datos (CSV, Parquet, base de datos)
            │
        cuDF (GPU)
            │
       Feature Engineering
            │
        cuML (GPU)
            │
       Modelo entrenado
            │
    Inferencia / Exportación
```

Todos los pasos se mantienen en memoria GPU, evitando transferencias innecesarias al host.

## Comparación de rendimiento

Para cargas grandes, la aceleración típica sobre CPU es:

| Operación | Factor de aceleración (aprox.) |
|-----------|-------------------------------|
| read_csv a DataFrame | 5–20× |
| groupby + agg | 10–50× |
| K-Means (1M puntos) | 20–100× |
| PCA (alta dimensión) | 10–30× |

Los factores dependen del hardware, del tamaño del dataset y del nivel de paralelismo de la operación.

## Instalación (referencia)

```bash
# Requiere CUDA 11.x o 12.x según la versión de RAPIDS
pip install cudf-cu11 cuml-cu11 --extra-index-url=https://pypi.nvidia.com
# O vía conda (recomendado para entornos reproducibles):
conda install -c rapidsai -c nvidia -c conda-forge cudf cuml cudatoolkit=11.8
```

## Resultados de Aprendizaje asociados

- **RA2.b**: Identificar y caracterizar nuevas librerías de IA orientadas a GPU.
- **RA2.d**: Implementar ejemplos de aceleración de flujos de datos y modelos.
- **RA2.e**: Evaluar comparativamente el rendimiento CPU vs GPU.

## Notebooks relacionados

- [01_rapids_intro.ipynb](../02-ejemplos/01_rapids_intro.ipynb) — Introducción a cuDF y cuML.
- [03_gpu_benchmarks.ipynb](../02-ejemplos/03_gpu_benchmarks.ipynb) — Benchmarks comparativos.
