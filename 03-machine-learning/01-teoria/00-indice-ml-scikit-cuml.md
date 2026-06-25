# 📚 Índice: Documentación CuML vs. Scikit-learn

Esta documentación compara los algoritmos y la API de **scikit-learn (CPU)** con su equivalente acelerado por GPU, **CuML (NVIDIA RAPIDS)**.

## Navegación rápida

- [Cap. I - Introducción y Conceptos Fundamentales](01-ML-Scikit-CuML-Cap-I.md)
- [Cap. II - Aprendizaje Supervisado](02-ML-Scikit-CuML-Cap-II.md)
- [Cap. III - Aprendizaje No Supervisado](03-ML-Scikit-CuML-Cap-III.md)
- [Cap. IV - Apartados Transversales](04-ML-Scikit-CuML-Cap-IV.md)

## I. Introducción y Conceptos Fundamentales 🚀

1.1. Introducción: Propósito y Alcance.

1.2. **El Ecosistema RAPIDS:** CuML, cuDF, CuPy.

1.3. **Manejo de Datos y Memoria:** Arrays de NumPy vs. CuPy/cuDF.

1.4. Requisitos de Hardware y Software (CUDA Toolkit).

1.5. Consideraciones de Rendimiento: CPU vs. GPU.

1.6. **Instalación y Compatibilidad:** matrices de versiones CUDA/driver/RAPIDS, conda vs. contenedores.

1.7. **Checklist de Verificación:** detección de GPU y pruebas rápidas.

---

## II. Aprendizaje Supervisado (Supervised Learning) 🎯

### A. Clasificación (Classification)

2.A.1. Regresión Logística (`LogisticRegression`).

2.A.2. Clasificación de Vecinos Más Cercanos (k-NN, `KNeighborsClassifier`).

2.A.3. Máquinas de Vectores de Soporte (SVM) para Clasificación (`SVC`).

2.A.4. Árboles y Random Forest (`DecisionTreeClassifier`, `RandomForestClassifier`).

2.A.5. Gradient Boosting / HistGradientBoosting (nota sobre XGBoost/LightGBM GPU).

2.A.6. Naive Bayes (GaussianNB/MultinomialNB, soporte parcial en CuML).


### B. Regresión (Regression)

2.B.1. Regresión Lineal (Simple, Ridge, Lasso, `LinearRegression`).

2.B.2. Regresión de Vecinos Más Cercanos (`KNeighborsRegressor`).

2.B.3. Máquinas de Vectores de Soporte (SVM) para Regresión (`SVR`).

2.B.4. ElasticNet y regularización mixta.

2.B.5. Random Forest / ExtraTrees Regressor.

2.B.6. Gradient Boosting Regressor (y nota sobre XGBoost GPU).

---

## III. Aprendizaje No Supervisado (Unsupervised Learning) 🧩

### A. Clustering

3.A.1. K-Means (`KMeans`).

3.A.2. DBSCAN (`DBSCAN`).

### B. Reducción de Dimensionalidad

3.B.1. Análisis de Componentes Principales (PCA, `PCA`).

3.B.2. UMAP (Solo CuML, `UMAP`).

3.B.3. GaussianMixture / GMM (solo scikit-learn, alternativas en CuML con otras técnicas).

3.B.4. IsolationForest / LOF (detección de anomalías; soporte en sklearn, planes/limitaciones en CuML).

3.B.5. t-SNE (ausente en CuML) vs. UMAP acelerado.

---

## IV. Apartados Transversales y Especiales 🌟

4.1. **Modelos Ensemble Acelerados (XGBoost y LightGBM).**

4.2. Módulos de Preprocesamiento (`preprocessing`).

4.3. Métricas de Evaluación Aceleradas (`metrics`).

4.4. Consideraciones sobre Kernels.

4.5. Procesamiento de Datos Masivos (Out-of-Core ML con Dask).

4.6. **Persistencia y Serialización** (joblib/pickle vs. `cuml.common.serialize`).

4.7. **Interoperabilidad** (DLPack con PyTorch/TF, compatibilidad sklearn API, `cuml.experimental`).

4.8. **Troubleshooting y Limitaciones Conocidas** (sample_weight, sparse, VRAM, drivers).

4.9. **Benchmarks y Cuándo NO usar GPU** (reglas prácticas por tamaño/anchura de datos).

---

## V. Ejemplos Rápidos (CPU vs GPU)

- **Clasificación binaria**: Breast Cancer / Titanic — Regresión Logística sklearn vs CuML (tiempo y exactitud).
- **Regresión tabular**: California Housing / House Prices — RandomForestRegressor sklearn vs CuML; nota sobre `float32`.
- **Clustering**: K-Means en MNIST/fashion-MNIST embeddings — tiempo de ajuste y predicción.
- **Reducción de dimensionalidad**: PCA y UMAP en 100k filas — comparar tiempo de `.fit_transform`.
- **Dask multi-GPU**: KMeans o RandomForest distribuido con `LocalCUDACluster` para datasets que no caben en una GPU.
