# Machine Learning para Series Temporales

## Sesión 5: Forecasting como un problema de regresión

Hasta ahora hemos tratado a las series temporales casi como seres místicos. Las hemos descompuesto, hemos mirado sus ciclos ocultos (estacionalidad) y hemos hecho predicciones asumiendo que el futuro siempre es un espejo del pasado (baselines). 

Pero la Inteligencia Artificial moderna, especialmente los algoritmos basados en árboles como Random Forest o XGBoost, no entienden de "tiempo". Para ellos, el tiempo no fluye; ellos solo ven filas y columnas independientes.

En esta sesión cruzaremos el puente más importante del forecasting moderno: **transformar una serie temporal pura en una tabla de Machine Learning Supervisado**. Aprenderemos a inyectarle "memoria" a las columnas para que algoritmos que no saben nada de tiempo puedan predecir el futuro con extrema precisión.

---

## Objetivos

Al terminar esta sesión deberías ser capaz de:

- **Cambiar el paradigma:** Entender cómo se transforma una secuencia 1D (tiempo) en una matriz 2D (Features vs Target).
- **Evitar el mayor pecado:** Comprender qué es la Fuga de Información (*Data Leakage*) ("leer el periódico de mañana hoy") y por qué destroza los proyectos de Data Science.
- **Crear memoria artificial:** Construir variables `lag` (valores pasados) de forma segura.
- **Destilar el pasado:** Crear "medias móviles" que resuman el contexto reciente sin hacer trampa.
- **Entrenar y comparar:** Construir un modelo real de Machine Learning y ver si realmente logra humillar a nuestros *baselines* de la sesión anterior.

## Requisitos técnicos

Usaremos `scikit-learn` para crear nuestros primeros modelos predictivos de Machine Learning.

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

Importaciones principales:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
```

---

## 1. El gran truco: Supervisión Artificial

Un modelo de Machine Learning supervisado clásico funciona así:

```text
Variables de entrada (X)  ->  Valor a predecir (y)
Metros cuadrados, Baños   ->  Precio de la casa
```

En *Forecasting*, el modelo NO recibe la serie como una secuencia. Tenemos que construir una tabla desde cero donde las "variables de entrada" sean instantáneas fotográficas del pasado.

Partimos de una serie pura:

```text
timestamp              consumo_kwh
2026-01-01 00:00       1.85
2026-01-01 01:00       1.66
2026-01-01 02:00       1.79
```

Queremos predecir el consumo actual (Nuestra `y`). La transformamos creando "Features temporales" (Nuestras `X`):

```text
timestamp              consumo_hora_anterior   hora_actual   dia_semana   y (Target)
2026-01-01 01:00       1.85                    1             Jueves       1.66
2026-01-01 02:00       1.66                    2             Jueves       1.79
```

¡Magia! Ahora cada fila es independiente. Si le pasas esta tabla a un Random Forest, el algoritmo aprenderá que "cuando la hora anterior fue alta y es de noche, el Target tiende a bajar".

---

## 2. Time Delay Embedding (El poder del Lag)

`Time delay embedding` suena a física cuántica, pero simplemente significa "representar el estado actual usando copias retrasadas de la serie". En Python, esto se hace con la función mágica `.shift()`.

```python
df_ejemplo = pd.DataFrame({
    "consumo_kwh": np.arange(200, dtype=float),
})

df_ejemplo["lag_1"] = df_ejemplo["consumo_kwh"].shift(1) # Lo que pasó hace 1 hora
df_ejemplo["lag_24"] = df_ejemplo["consumo_kwh"].shift(24) # Lo que pasó hace 1 día
df_ejemplo["lag_168"] = df_ejemplo["consumo_kwh"].shift(24 * 7) # Lo que pasó hace 1 semana
df_ejemplo.tail()
```

**¿Por qué elegimos esos Lags?**
No se eligen al azar. Recuerda el gráfico de Autocorrelación (ACF) de la Sesión 3. Los picos de ese gráfico te chivan exactamente qué `Lags` tienen una conexión matemática fuerte con el presente.

---

## 3. El mayor peligro: Fuga de Información (Data Leakage)

Si cometes un error aquí, tu modelo sacará un error del 0% en entrenamiento y validación, serás aplaudido en tu empresa, y cuando lo pongas en producción provocará pérdidas millonarias.

La Fuga de Información ocurre cuando **le das al modelo información que sería IMPOSIBLE conocer en el mundo real en el momento de hacer la predicción.**

### Ejemplo de Fuga Mortal con Medias Móviles

Quieres decirle al modelo cómo está la "tendencia" de las últimas 24 horas usando una media móvil:

**El código que te despedirá:**
```python
# MAL: La ventana de 24h INCLUYE la hora actual que intentas predecir
df_ejemplo["media_24h_mal"] = df_ejemplo["consumo_kwh"].rolling(24).mean()
```

**El código correcto:**
```python
# BIEN: Primero "desplazas" el pasado 1 paso, y LUEGO calculas la media
df_ejemplo["media_24h"] = df_ejemplo["consumo_kwh"].shift(1).rolling(24).mean()
```

> **Pregunta para discutir:** Imagina que quieres incluir una variable de temperatura (meteorología). ¿Usarías la temperatura REAL de esa hora o la temperatura PREDICHA por el hombre del tiempo? ¿Qué implicaciones tiene esto en el Data Leakage?

---

## 4. Ensamblando el Dataset

Carguemos nuestra serie e inyectémosle inteligencia con una función creadora de features:

```python
df = pd.read_csv("datos/consumo_con_eventos.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").asfreq("h")

def crear_features(df):
    datos = df[["consumo_kwh"]].copy()

    # 1. Memoria directa (Lags)
    for lag in [1, 2, 24, 168]:
        datos[f"lag_{lag}"] = datos["consumo_kwh"].shift(lag)

    # 2. Resumen del pasado (Rolling Windows SIN FUGA)
    datos["media_24h"] = datos["consumo_kwh"].shift(1).rolling(24).mean()
    
    # 3. Contexto Estacional (Se conocen perfectamente en el futuro)
    datos["hora"] = datos.index.hour
    datos["dia_semana"] = datos.index.dayofweek
    datos["es_fin_de_semana"] = datos.index.dayofweek >= 5

    return datos.dropna() # Al hacer shift, los primeros días quedan como NaN

datos_ml = crear_features(df)
```

Separamos variables predictoras (X) de nuestra meta (y):

```python
target = "consumo_kwh"
features = [col for col in datos_ml.columns if col != target]

X = datos_ml[features]
y = datos_ml[target]
```

---

## 5. El Duelo: Baseline vs Machine Learning

Recordando la Sesión 4, separamos temporalmente (sin barajar):

```python
n = len(datos_ml)
fin_train = int(n * 0.70)
fin_validacion = int(n * 0.85)

X_train, y_train = X.iloc[:fin_train], y.iloc[:fin_train]
X_validacion, y_validacion = X.iloc[fin_train:fin_validacion], y.iloc[fin_train:fin_validacion]
X_test, y_test = X.iloc[fin_validacion:], y.iloc[fin_validacion:]
```

### 5.1 El Oponente: Seasonal Naive

```python
historia = y.copy()
# Predice usando exactamente lo que pasó hace 7 días
pred_seasonal_7d = historia.shift(168).loc[y_validacion.index]
```

### 5.2 El Aspirante: Random Forest

Un bosque aleatorio puede descubrir combinaciones complejas como *"Si es domingo por la tarde, y el Lag_1 es alto, pero la media de 24h es baja, entonces..."*

```python
modelo_rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
modelo_rf.fit(X_train, y_train)

pred_rf = pd.Series(
    modelo_rf.predict(X_validacion),
    index=y_validacion.index,
)
```

### 5.3 Extensión opcional: HistGradientBoostingRegressor

`HistGradientBoostingRegressor` es una implementación moderna de boosting con histogramas incluida en `scikit-learn`. Suele ser más rápida y competitiva que `GradientBoostingRegressor` clásico en datasets tabulares medianos o grandes, y no requiere instalar librerías externas.

```python
modelo_hgb = HistGradientBoostingRegressor(
    max_iter=300,
    learning_rate=0.05,
    max_leaf_nodes=31,
    random_state=42,
)
modelo_hgb.fit(X_train, y_train)

pred_hgb = pd.Series(
    modelo_hgb.predict(X_validacion),
    index=y_validacion.index,
)
```

Nota avanzada: en proyectos reales también son frecuentes `XGBoost`, `LightGBM` y `CatBoost`. Son modelos tabulares muy fuertes, pero añaden dependencias externas y conviene tratarlos como extensión opcional del entorno, no como requisito base del taller.

### 5.4 Resultados

Comparamos usando MAE:

```python
def evaluar(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)

print("MAE Seasonal Naive:", evaluar(y_validacion, pred_seasonal_7d))
print("MAE Random Forest:", evaluar(y_validacion, pred_rf))
print("MAE HistGradientBoosting:", evaluar(y_validacion, pred_hgb))
```

*Si el Random Forest pierde, no te asustes. Significa que necesitamos hacer mejor Ingeniería de Características (Feature Engineering) en la siguiente sesión.*

---

## 6. Mirando dentro de la "Caja Negra"

A diferencia del Baseline, el Random Forest puede decirnos qué variables le han resultado más útiles para tomar sus decisiones.

```python
importancias = pd.Series(
    modelo_rf.feature_importances_,
    index=features,
).sort_values(ascending=True)

plt.figure(figsize=(10, 5))
importancias.plot(kind="barh", color="tab:green")
plt.title("¿Qué está mirando el modelo? (Feature Importance)")
plt.show()
```

Si el `lag_168` (hace una semana) domina el gráfico, el Random Forest ha "descubierto" la fuerte estacionalidad semanal de la energía eléctrica de forma completamente automática.

---

## 7. Actividades de clase

### Actividad 1: Cazando el Subajuste
Sustituye el `RandomForestRegressor` por un modelo excesivamente simple: `LinearRegression()`. Entrénalo con las mismas variables, evalúa su MAE y compara. ¿El modelo lineal logra superar al Baseline? ¿Qué te dice esto sobre la no-linealidad del consumo eléctrico?

### Actividad 2: El poder del contexto
Ve a la función `crear_features`. Comenta (borra) la línea que crea la variable `es_fin_de_semana`. Reentrena el Random Forest. ¿Empeora el error significativamente? Esto demuestra que dar contexto humano a los modelos es vital.

### Actividad 3: La Fuga de Información
Rompe la regla a propósito. Crea una variable `media_24h_MAL = datos["consumo_kwh"].rolling(24).mean()` (¡Sin el shift!). Añádela al entrenamiento del Random Forest. 
Verás que el error de validación baja casi a CERO de forma mágica. Celebra tu premio Nobel de Inteligencia Artificial durante 1 minuto, y luego explica en voz alta por qué este modelo es inútil en el mundo real.

---

## 8. Ideas clave

- **Forecasting como Regresión:** La magia está en crear una tabla donde cada fila tiene el contexto del pasado (`X`) para predecir el futuro (`y`).
- **Data Leakage es tu peor enemigo:** Si tu modelo usa información que no tendrás el día de mañana, estás construyendo un espejismo. El `shift(1)` te salva la vida.
- **La Inteligencia es Artificial, el Sentido Común es Tuyo:** El modelo descubre relaciones automáticamente (como qué lag es importante), pero eres tú quien decide qué variables construirle para que las analise.

## Continuación

Acabas de ver el flujo de trabajo real del Data Science aplicado al tiempo. Sin embargo, nuestras "features" han sido algo básicas. En la siguiente sesión subiremos de nivel: aprenderemos el verdadero Arte del **Feature Engineering**. Construiremos indicadores estacionales complejos, medias móviles exponenciales ponderadas (EWMA) y transformaciones matemáticas de Fourier para extraer hasta la última gota de información temporal sin cometer un solo "Data Leakage".
