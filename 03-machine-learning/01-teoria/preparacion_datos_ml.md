# Titanic – Preparación de datos para modelado

En este notebook continuaremos con el análisis del famoso dataset *Titanic* después del Análisis Exploratorio de Datos (EDA). Supondremos que en el EDA anterior se limpió el conjunto de datos y se guardó en formato Parquet. Ahora, nuestro objetivo es preparar los datos para construir modelos de machine learning. Realizaremos los siguientes pasos:

- **Carga del dataset limpio:** leeremos el archivo Parquet con los datos ya limpios.  
- **Separación de características (X) y variable objetivo (y):** definiremos la matriz de características y el vector objetivo (`Survived`).  
- **Codificación de variables categóricas:** convertiremos variables categóricas en valores numéricos mediante técnicas de codificación (por ejemplo, *One-Hot Encoding* u *Ordinal Encoding*).  
- **Escalado de variables numéricas (opcional):** aplicaremos escalado a las variables numéricas si el modelo lo requiere (modelos sensibles a la escala).  
- **Separación en conjunto de entrenamiento y prueba:** dividiremos los datos preparados en un conjunto para entrenar el modelo y otro para evaluarlo.  
- **Guardado de los datos preparados:** almacenaremos los conjuntos de entrenamiento y prueba en disco para su uso posterior (por ejemplo, con `joblib`).

Cada sección irá acompañada de explicaciones para entender qué se está haciendo y por qué. ¡Comencemos!

## Carga del dataset limpio

Primero, cargaremos el dataset limpio que se guardó tras el EDA. Asumimos que el archivo Parquet resultante se encuentra en la ruta correspondiente (por ejemplo, `datos/titanic_limpio.parquet`). Utilizaremos **Pandas** para leer el archivo Parquet, aunque también podríamos emplear **Polars** de forma similar. 

Vamos a leer el dataset y a inspeccionar brevemente su contenido para asegurarnos de que se cargó correctamente (por ejemplo, viendo las primeras filas y las dimensiones del DataFrame).

```python
import pandas as pd

# Cargar el dataset limpio desde el archivo Parquet
df = pd.read_parquet('datos/titanic_limpio.parquet')

# Mostrar las primeras 5 filas para verificar
print("Primeras 5 filas del dataset:\n", df.head(), "\n")
# Mostrar la forma (dimensiones) del DataFrame
print("Dimensiones del dataset:", df.shape)
```

## Separación de características (X) y variable objetivo (y)

```python
# Definir la variable objetivo y las características
y = df['Survived']               # variable objetivo
X = df.drop(columns=['Survived'])  # todas las columnas excepto 'Survived'

# Verificar la separación
print("Dimensiones de X:", X.shape)
print("Dimensiones de y:", y.shape)
print("Columnas de X:", X.columns.tolist())
```

## Codificación de variables categóricas

```python
from sklearn.preprocessing import OneHotEncoder

columnas_categoricas = ['Sex', 'Embarked']
ohe = OneHotEncoder(sparse_output=False)
X_cat_encoded = ohe.fit_transform(X[columnas_categoricas])
nombres_ohe = ohe.get_feature_names_out(columnas_categoricas)
X_cat_encoded_df = pd.DataFrame(X_cat_encoded, columns=nombres_ohe, index=X.index)

X_numeric = X.drop(columns=columnas_categoricas)
X_encoded = pd.concat([X_numeric, X_cat_encoded_df], axis=1)

print("Columnas originales categóricas:", columnas_categoricas)
print("Columnas nuevas tras One-Hot Encoding:", nombres_ohe.tolist())
print("Dimensiones de X antes vs después de codificar:", X.shape, "->", X_encoded.shape)
```

## Escalado de variables numéricas (opcional)

```python
from sklearn.preprocessing import StandardScaler

columnas_numericas = ['Age', 'Fare']
scaler = StandardScaler()
X_encoded[columnas_numericas] = scaler.fit_transform(X_encoded[columnas_numericas])

print("Media de Age escalada:", X_encoded['Age'].mean().round(2))
print("Desviación estándar de Age escalada:", X_encoded['Age'].std().round(2))
print("Media de Fare escalada:", X_encoded['Fare'].mean().round(2))
print("Desviación estándar de Fare escalada:", X_encoded['Fare'].std().round(2))
```

## Separación del dataset en conjuntos de entrenamiento y test

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.20, random_state=42
)

print("Tamaño de X_train:", X_train.shape)
print("Tamaño de X_test:", X_test.shape)
print("Tamaño de y_train:", y_train.shape)
print("Tamaño de y_test:", y_test.shape)
```

## Guardado de los datos preparados

```python
import joblib

joblib.dump((X_train, X_test, y_train, y_test), "datos/titanic_datos_preparados.joblib")

print("Datos de entrenamiento y prueba guardados correctamente.")
```

---

Con esto concluimos la preparación de los datos: hemos cargado el dataset limpio, separado características y objetivo, codificado las variables categóricas, escalado las numéricas (si era necesario), dividido en entrenamiento y prueba, y guardado los resultados. Los datos están listos para la etapa de modelado predictivo. ¡Continuemos con el desarrollo del modelo en el siguiente notebook!

