# Titanic – Preparación de datos para modelado

Después del EDA, prepararemos Titanic para modelar sin contaminar la evaluación. La regla que guía todo el flujo es simple: **separamos entrenamiento y prueba antes de ajustar cualquier transformación que aprenda de los datos**.

Esto evita la *fuga de datos*: si un imputador, escalador o codificador conoce estadísticas o categorías del conjunto de prueba durante el ajuste, la métrica deja de representar un caso nuevo. Esta fase corresponde a la preparación de datos de [CRISP-DM](05a-marco-crisp-dm.md).

## Carga y separación de objetivo

```python
import pandas as pd

# Dataset limpio tras el EDA; Survived es la variable objetivo.
df = pd.read_parquet("datos/titanic_limpio.parquet")
y = df["Survived"]
X = df.drop(columns=["Survived"])

print("Dimensiones de X:", X.shape)
print("Dimensiones de y:", y.shape)
```

## Separar antes de transformar

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print("Entrenamiento:", X_train.shape)
print("Prueba:", X_test.shape)
```

## Preparar columnas con un pipeline

`SimpleImputer`, `StandardScaler` y `OneHotEncoder` se ajustan con `X_train`. `X_test` se transforma con esos mismos parámetros; nunca se vuelve a ajustar.

```python
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

columnas_numericas = ["Age", "Fare"]
columnas_categoricas = ["Sex", "Embarked"]

transformador_numerico = Pipeline(
    steps=[
        ("imputador", SimpleImputer(strategy="median")),
        ("escalador", StandardScaler()),
    ]
)
transformador_categorico = Pipeline(
    steps=[
        ("imputador", SimpleImputer(strategy="most_frequent")),
        ("codificador", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocesado = ColumnTransformer(
    transformers=[
        ("numericas", transformador_numerico, columnas_numericas),
        ("categoricas", transformador_categorico, columnas_categoricas),
    ]
)

# ÚNICO ajuste: aprende medianas, medias/desviaciones y categorías del entrenamiento.
X_train_preparado = preprocesado.fit_transform(X_train)
# Solo aplica lo aprendido; no debe usarse fit_transform aquí.
X_test_preparado = preprocesado.transform(X_test)

print("Entrenamiento preparado:", X_train_preparado.shape)
print("Prueba preparada:", X_test_preparado.shape)
```

## Entrenar sin romper la regla

En la práctica, se recomienda encapsular preparación y modelo en un único `Pipeline`; así cada validación y predicción aplica el mismo flujo correctamente.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

modelo = Pipeline(
    steps=[
        ("preprocesado", preprocesado),
        ("clasificador", LogisticRegression(max_iter=1_000)),
    ]
)

modelo.fit(X_train, y_train)
print("Exactitud en test:", round(modelo.score(X_test, y_test), 3))
```

## Guardado reproducible

Si necesitas conservar el modelo y su preparación, guarda el pipeline completo, no solo el escalador ni los arrays ya transformados.

```python
import joblib

joblib.dump(modelo, "datos/titanic_pipeline.joblib")
print("Pipeline guardado correctamente.")
```

## Comprobación final

- [ ] `train_test_split` ocurre antes de `fit` o `fit_transform`.
- [ ] Imputación, codificación, escalado y selección de variables se ajustan solo con entrenamiento.
- [ ] El conjunto de prueba usa exclusivamente `transform` o `predict`.
- [ ] La métrica final se calcula sobre el conjunto de prueba sin reutilizarlo para decidir transformaciones.
