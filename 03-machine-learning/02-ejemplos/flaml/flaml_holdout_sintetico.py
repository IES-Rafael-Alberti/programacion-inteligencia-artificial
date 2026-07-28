"""Smoke test didáctico de FLAML: AutoML en entrenamiento y test reservado."""

from sklearn.datasets import make_classification
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

from flaml import AutoML

# Datos sintéticos solo para comprobar el flujo; no representan el capstone.
X, y = make_classification(
    n_samples=400,
    n_features=12,
    n_informative=6,
    n_redundant=2,
    weights=[0.6, 0.4],
    class_sep=1.0,
    random_state=42,
)

# El holdout no participa en la búsqueda ni en la selección de modelos.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

automl = AutoML()
automl.fit(
    X_train=X_train,
    y_train=y_train,
    task="classification",
    metric="f1",
    time_budget=20,
    # Evitamos lrl2: FLAML lo configura con parámetros que scikit-learn 1.9
    # marca como obsoletos y distraen en un ejemplo introductorio.
    estimator_list=["rf", "xgboost"],
    seed=42,
)

# Evaluación final: una vez cerrada la búsqueda sobre el entrenamiento.
y_pred = automl.predict(X_test)
print(f"Filas entrenamiento/test: {len(X_train)}/{len(X_test)}")
print(f"Mejor estimador: {automl.best_estimator}")
print(f"F1 del holdout (solo smoke test sintético): {f1_score(y_test, y_pred):.3f}")
