# Proyecto Final: Capstone Project

## Sesión 10: El Barro del Mundo Real — Torneo de Modelos

Ha llegado el momento de la verdad. Durante las nueve sesiones anteriores has construido un arsenal completo: sabes limpiar datos temporales, detectar estacionalidades, evitar la fuga de información, construir features sólidas, entrenar modelos clásicos como Random Forest y modelos de Deep Learning como LSTMs y TCNs. Incluso sabes por qué los Transformers a veces pierden contra dos capas lineales.

Ahora toca demostrar que has asimilado la diferencia entre un prototipo de laboratorio y un producto que funciona en el mundo real. En la industria, los datos nunca vienen en un único CSV limpio y listo. Vienen de sistemas distintos, a frecuencias distintas, con fallos, con días de cierre y con eventos inexplicables. Tu trabajo es integrarlos, razonar sobre ellos y elegir el modelo adecuado — no el más impresionante en un paper, sino el mejor para ese problema concreto.

Este proyecto tiene tres fases:
1. **Parte guiada:** Fusión de fuentes heterogéneas (Retail).
2. **Reto autónomo:** Fusión con downsampling (Energía).
3. **El Torneo:** Competición de modelos con tabla comparativa final.

---

## Requisitos técnicos

```python
import sys
import os

os.environ["USE_TF"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["LIGHTNING_DISABLE_TIPS"] = "1"

sys.path.append("src")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as pl


class TimeSeriesDataset(Dataset):
    def __init__(self, df, target_col, window_size=96, forecast_horizon=1):
        self.features = df.drop(columns=[target_col]).values.astype(np.float32)
        self.target = df[target_col].values.astype(np.float32)
        self.window_size = window_size
        self.forecast_horizon = forecast_horizon
        self.length = len(df) - window_size - forecast_horizon + 1

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        X = self.features[idx : idx + self.window_size]
        target_idx = idx + self.window_size + self.forecast_horizon - 1
        y = self.target[target_idx]
        return torch.from_numpy(X), torch.tensor(y)
```

---

## Parte 1: Caso Guiado — Retail y Tráfico Peatonal

### El Contexto

Trabajas como Data Scientist para una cadena de tiendas físicas. El Director Comercial quiere predecir las ventas del día siguiente para optimizar el stock y los turnos de personal. Tienes acceso a dos fuentes de datos:

- **Ventas diarias** (`datos/ventas_diarias.csv`): El software de caja exporta un resumen cada noche a las 23:59. Los domingos la tienda cierra y no hay registro.
- **Tráfico peatonal horario** (`datos/trafico_peatonal_horario.csv`): Un sensor láser en la puerta cuenta el número de personas que pasan cada hora, 24/7, incluso los domingos.

### 1.1 Cargando las dos realidades

```python
df_ventas = pd.read_csv("datos/ventas_diarias.csv")
df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"])
df_ventas = df_ventas.set_index("fecha")

df_trafico = pd.read_csv("datos/trafico_peatonal_horario.csv")
df_trafico["timestamp"] = pd.to_datetime(df_trafico["timestamp"])
df_trafico = df_trafico.set_index("timestamp")

print(f"Ventas:   {len(df_ventas)} registros | Frecuencia: {df_ventas.index.inferred_freq}")
print(f"Tráfico:  {len(df_trafico)} registros | Frecuencia: {df_trafico.index.inferred_freq}")
```

### 1.2 El desastre de la fusión en crudo

Antes de hacer cualquier cosa, intentemos lo "obvio":

```python
# Intento naïve: ¿qué pasa si simplemente unimos las dos tablas?
df_error = pd.merge(df_ventas, df_trafico, left_index=True, right_index=True, how="outer")
print(f"Filas resultantes: {len(df_error)}")
print(df_error.head(30))
```

Verás un resultado catastrófico: cientos de filas con NaNs masivos. Las ventas solo existen a las `00:00:00` de cada día, mientras que el tráfico existe a las `01:00`, `02:00`... Las filas simplemente no coinciden en el tiempo.

### 1.3 La solución: Agregación Temporal

No podemos "inventar" ventas horarias. Pero sí podemos **agregar** el tráfico horario hasta el nivel diario, sumando todos los peatones que pasaron en las 24 horas del día.

```python
# Comprimimos el tráfico horario a diario
df_trafico_diario = df_trafico.resample("D").sum()
df_trafico_diario.columns = ["trafico_peatonal_diario"]

# Ahora ambos están al mismo nivel temporal
df_unido = pd.merge(
    df_ventas, df_trafico_diario,
    left_index=True, right_index=True, how="outer"
)
print(df_unido.isna().sum())
```

### 1.4 El Dilema del Imputador: Reglas de Negocio vs Estadística

Después del merge aparecen NaNs en `ventas_euros` cada domingo. Un científico de datos sin experiencia buscaría rellenar estos huecos con la media o con interpolación.

```python
# MAL: Inventar ventas en un día de cierre
df_unido["ventas_euros"].fillna(df_unido["ventas_euros"].mean(), inplace=True)
```

Un profesional consulta al negocio: *"¿Cuánto se vendió el domingo pasado?"* La respuesta es: **cero**, porque la tienda estaba cerrada.

```python
# BIEN: Cero porque estaba cerrada, no porque el sensor falló
df_unido["ventas_euros"] = df_unido["ventas_euros"].fillna(0)
```

> ¿Son lo mismo un domingo cerrado y un martes con el sensor averiado? Matemáticamente son ambos NaN. Semánticamente son totalmente distintos. Un modelo entrenado con una media inventada aprenderá que los domingos se vende algo. Un modelo entrenado con cero aprenderá que los domingos no se vende nada. La diferencia puede costar miles de euros en sobre-stock.

---

## Parte 2: El Reto Autónomo — Energía y Clima

### El Contexto

Ahora trabajas en una empresa de distribución eléctrica. Tu objetivo es predecir el consumo de energía de una subestación **cada 15 minutos**. Sabes por física que la temperatura exterior es un driver crucial: cuando hace mucho calor, el uso de Aires Acondicionados dispara la demanda.

Tienes dos fuentes:
1. `consumo_energia_15min.csv`: Serie a 15 min. Contiene tres apagones masivos (NaNs).
2. `clima_horario.csv`: Temperatura de AEMET, solo disponible cada hora exacta.

### Tu Misión (Completa estos pasos de forma autónoma)

**Paso 1: Carga y diagnóstico**
```python
# Carga los dos archivos, convierte a DatetimeIndex y comprueba las frecuencias
df_consumo = pd.read_csv("datos/consumo_energia_15min.csv", parse_dates=["timestamp"])
df_consumo = df_consumo.set_index("timestamp").sort_index()

df_clima = pd.read_csv("datos/clima_horario.csv", parse_dates=["timestamp"])
df_clima = df_clima.set_index("timestamp").sort_index()

print(df_consumo.index.inferred_freq)
print(df_clima.index.inferred_freq)
```

**Paso 2: Downsampling del Clima**
El consumo dicta el ritmo (15 min). Hay que llevar el clima a esa granularidad.
```python
# Pista 1: Crea una rejilla de 15 minutos vacía
df_clima_15m = df_clima.resample("15min").asfreq()

# Pista 2: La temperatura cambia suavemente -> línea recta entre horas es aceptable
df_clima_15m = df_clima_15m.interpolate(method="time")
```

**Paso 3: Fusión y el Dilema del Apagón**
```python
# Une el consumo y el clima alineados
df_fusionado = pd.merge(df_consumo, df_clima_15m, left_index=True, right_index=True, how="left")

# Hay NaNs en consumo_kwh. ¿Deberías interpolarlos como el clima?
# REFLEXIONA antes de escribir código:
# Un apagón no es un sensor roto. El consumo real fue 0. Si interpolamos, le mentimos al modelo.
df_fusionado["consumo_kwh"] = df_fusionado["consumo_kwh"].fillna(0)
```

**Paso 4: Feature Engineering**
Construye las variables que usarás en el torneo:
- `lag_96`: Consumo de hace 24 horas exactas (96 pasos de 15 min).
- `lag_672`: Consumo de hace 7 días.
- Hora, día de la semana, es_fin_de_semana.
- `temperatura`: La columna que acabas de interpolar y fusionar.

```python
df_ml = df_fusionado.copy()

df_ml["lag_96"] = df_ml["consumo_kwh"].shift(96)
df_ml["lag_672"] = df_ml["consumo_kwh"].shift(672)
df_ml["hora"] = df_ml.index.hour
df_ml["dia_semana"] = df_ml.index.dayofweek
df_ml["es_fin_de_semana"] = (df_ml["dia_semana"] >= 5).astype(int)

features = ["lag_96", "lag_672", "hora", "dia_semana", "es_fin_de_semana", "temperatura"]
target = "consumo_kwh"
df_ml = df_ml.dropna(subset=features + [target])
print(df_ml.head())
```

**Paso 5: División temporal**
```python
n = len(df_ml)
train = df_ml.iloc[:int(n * 0.70)]
val   = df_ml.iloc[int(n * 0.70):int(n * 0.85)]
test  = df_ml.iloc[int(n * 0.85):]
```

---

## Parte 3: El Torneo de Modelos

Este es el núcleo del proyecto. Evaluarás tres paradigmas sobre los **mismos datos** y la **misma ventana de validación**.

### Contendiente 1: Seasonal Naive

```python
# El valor de hace 96 pasos (24h) como predicción
pred_naive = df_ml["consumo_kwh"].shift(96).loc[val.index]
mae_naive = mean_absolute_error(val["consumo_kwh"].dropna(), pred_naive.dropna())
print(f"MAE Naive: {mae_naive:.4f}")
```

### Contendiente 2: Random Forest con Feature Engineering

```python
features = ["lag_96", "lag_672", "hora", "dia_semana", "es_fin_de_semana", "temperatura"]
target = "consumo_kwh"

X_train, y_train = train[features].dropna(), train[target].loc[train[features].dropna().index]
X_val,   y_val   = val[features].dropna(),   val[target].loc[val[features].dropna().index]

inicio = time.time()
rf = RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
tiempo_rf = time.time() - inicio
mae_rf = mean_absolute_error(y_val, rf.predict(X_val))
print(f"MAE Random Forest: {mae_rf:.4f} | Tiempo: {tiempo_rf:.2f}s")
```

### Contendiente 3: Red Neuronal (LSTM o TCN con PyTorch Lightning)

Reutiliza las clases `TimeSeriesDataset`, `LSTMForecaster` o `TCNForecaster` de las sesiones 07 y 08. Eres libre de elegir la arquitectura que consideres más adecuada para datos a 15 minutos.

```python
# Configura el Dataset con la ventana que consideres apropiada
# (pista: ¿cuántos pasos de 15 min hacen falta para ver una semana?)
mae_dl = np.nan  # Se sustituye por el MAE real si entrenas LSTM/TCN.
WINDOW_SIZE = 96  # 24 horas de contexto en datos de 15 minutos.

train_ds = TimeSeriesDataset(train[features + [target]].dropna(), target, window_size=WINDOW_SIZE)
val_ds   = TimeSeriesDataset(val[features + [target]].dropna(),   target, window_size=WINDOW_SIZE)

train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)
val_loader   = DataLoader(val_ds,   batch_size=128, shuffle=False)

# Entrena aquí tu LSTM o TCN si decides incluir Deep Learning en el torneo.
# modelo = LSTMForecaster(n_features=len(features), hidden_size=64)
# trainer = pl.Trainer(max_epochs=15, accelerator="auto")
# trainer.fit(modelo, train_loader, val_loader)
# mae_dl = ...  # Calcula el MAE de validación con las predicciones del modelo.
```

### El Veredicto Final

Construye y comenta la tabla de resultados:

```python
resultados = pd.DataFrame({
    "Modelo":    ["Seasonal Naive", "Random Forest", "LSTM/TCN"],
    "MAE Val":   [mae_naive, mae_rf, mae_dl],
}).dropna().sort_values("MAE Val")

print("\n╔══════════════════════════════════════╗")
print("║       TORNEO FINAL - RESULTADOS      ║")
print("╠══════════════════════════════════════╣")
print(resultados.to_string(index=False))
print("╚══════════════════════════════════════╝")
```

---

## Reflexión Crítica (Obligatoria)

Responde razonadamente a estas preguntas como parte de tu entrega:

1. **¿Logró el Deep Learning batir al Random Forest?** Si no fue así, ¿a qué crees que se debe? (Pista: recuerda qué pasó con el Seasonal Naive en la sesión 09).
2. **¿Valió la pena la complejidad?** Considera el tiempo de entrenamiento y el tiempo de implementación: si la mejora es un 2% de MAE, ¿tiene sentido en producción?
3. **¿Cómo afecta la temperatura al error?** Compara el MAE de tu Random Forest con y sin la variable `temperatura`. ¿Justificó el esfuerzo de fusionar las dos fuentes de datos?
4. **El modelo campeón:** ¿Cuál elegiría el CEO y cuál elegiría el ingeniero de datos? ¿Son la misma persona?
5. **Coste-beneficio:** Añade a tu tabla el tiempo de entrenamiento. Si dos modelos empatan en MAE, elige el más simple, rápido y explicable.

---

> [!TIP]
> **El mensaje final del taller**
> El mundo real no premia al que usa el modelo más moderno. Premia al que entiende el problema, sabe de dónde viene cada NaN, no hace trampas con el tiempo y puede explicarle a alguien no técnico por qué su modelo se equivocó.
>
> Juntar tablas no es un problema de código, es un problema de lógica de negocio.
> Elegir el modelo no es un problema de benchmark, es un problema de contexto.
>
> Bienvenido al mundo real. ¡Buena suerte!
