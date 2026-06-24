# Deep Learning y Modelos Globales en Series Temporales

## Sesión 7: Del Médico de Pueblo al Hospital de Referencia

Hasta ahora hemos construido modelos que conocen a un único paciente en profundidad. El Random Forest de la sesión 5 aprendió los ritmos de una sola subestación eléctrica; el modelo de Feature Engineering de la sesión 6 extrajo toda la inteligencia posible de una sola serie de ventas. Estos son **Modelos Locales**: especialistas brillantes en un problema concreto.

Pero el mundo real no tiene un paciente. Tiene miles.

Imagina a un médico de pueblo que lleva 20 años tratando a los mismos vecinos. Conoce perfectamente a cada uno: sus alergias, sus estacionalidades (el señor García siempre empeora en invierno), sus recaídas. Si ese paciente es el consumo eléctrico de una sola subestación, este médico es imbatible. Pero el día que aparece un paciente nuevo, o que llega una pandemia global (un evento jamás visto), su experiencia limitada a un solo pueblo se queda corta.

El **Deep Learning** funciona como un gigantesco Hospital de Referencia. En lugar de estudiar a un paciente, analiza los historiales cruzados de cientos de miles de pacientes simultáneamente. Quizás no conoce a cada individuo con el mismo detalle inicial, pero ha visto *tantos patrones compartidos* que al ver los primeros síntomas (una pequeña ventana de datos), ya sabe reconocer la enfermedad porque la ha visto en otras ciudades, en otros sectores.

A esto se le llama **Cross-Learning**: la red aprende que "un pico de ventas seguido de una caída de temperatura" precede a una rotura de stock, sin importar de qué supermercado o ciudad hablemos. Ha aprendido la física del problema, no solo un único caso.

---

## Objetivos

Al terminar esta sesión deberías ser capaz de:

- **Distinguir** entre Modelos Locales (un modelo por serie) y Modelos Globales (un modelo para todas las series).
- **Entender** por qué las Redes Neuronales necesitan datos en formato 3D (Tensores) en lugar del formato 2D tabular que usan los árboles de decisión.
- **Construir** una clase `Dataset` de PyTorch que convierta un DataFrame en ventanas de tiempo listas para entrenar.
- **Comprender** la diferencia conceptual entre un MLP (con amnesia temporal) y una LSTM (con memoria a largo plazo).
- **Implementar** una red LSTM de forecasting usando PyTorch Lightning para evitar el código repetitivo de entrenamiento.
- **Razonar** sobre cuándo merece la pena la complejidad del Deep Learning y cuándo no.

## Requisitos técnicos

Para esta sesión necesitamos el entorno `pia-ud1` con las instalaciones correctas. Recuerda que las librerías de `torch` deben haberse instalado vía `pip` (no conda-forge) para evitar conflictos con los drivers NVIDIA:

```bash
pip install torch pytorch-lightning
```

Importaciones principales:

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

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as pl

from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from series_temporales import generar_consumo_electrico
```

---

## 1. El Salto de Paradigma: De 2D a 3D

Para alimentar a un Random Forest (sesión 5), usábamos un DataFrame 2D donde cada fila era un instante de tiempo y cada columna era un `lag` o una variable de calendario. La filosofía era: *"Dame una fotografía del pasado y te diré qué ocurrirá"*.

Las Redes Neuronales funcionan de forma distinta. No miran una fotografía aislada: miran **una película completa** (una ventana de tiempo) de un solo vistazo.

Por eso, en lugar de un DataFrame 2D `[Filas, Columnas]`, necesitamos un **Tensor 3D** con la siguiente estructura:

```text
[Batch_Size, Sequence_Length, Features]
```

1. **Batch_Size (El Lote):** Cuántas "películas" (ventanas) le mostramos a la red de golpe antes de que actualice sus pesos. Un batch de 32 significa que la red ve 32 ventanas simultáneamente y promedia el aprendizaje de todas ellas. Esto estabiliza el entrenamiento.
2. **Sequence_Length (La Longitud de la Película):** Cuántos pasos hacia atrás mira la red en cada ventana. Si entrenamos con `sequence_length=24`, la red ve las últimas 24 horas antes de predecir.
3. **Features (Las Variables):** Cuántas columnas de información hay en cada instante. Si usamos consumo, temperatura y día de la semana, `features=3`.

*Visualización:* Imagina un mazo de cartas (el Batch). Cada carta es una pequeña tabla de 24 filas × 3 columnas, representando lo que ocurrió en las últimas 24 horas.

### Construyendo el Dataset para PyTorch

PyTorch nos obliga a encapsular el mecanismo de extracción de ventanas en una clase `Dataset`. Esta clase tiene que saber responder a dos preguntas: ¿Cuántas ventanas hay? (`__len__`) y ¿Cómo me das la ventana número N? (`__getitem__`).

```python
class TimeSeriesDataset(Dataset):
    def __init__(self, df, target_col, window_size=24, forecast_horizon=1):
        """
        Convierte un DataFrame temporal en ventanas 3D para PyTorch.

        Args:
            df: DataFrame con índice temporal y las columnas de features + target.
            target_col: Nombre de la columna que queremos predecir.
            window_size: Cuántos pasos del pasado mira la red (longitud de la ventana).
            forecast_horizon: Cuántos pasos hacia el futuro predecimos.
        """
        self.features = df.drop(columns=[target_col]).values.astype(np.float32)
        self.target = df[target_col].values.astype(np.float32)
        self.window_size = window_size
        self.forecast_horizon = forecast_horizon

        # El número total de ventanas que podemos construir sin salirnos del dataset
        self.length = len(df) - window_size - forecast_horizon + 1

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        # Ventana de Entrada X: [window_size, n_features]
        X = self.features[idx : idx + self.window_size]

        # Valor objetivo y: el dato que hay 'forecast_horizon' pasos después del final de la ventana
        target_idx = idx + self.window_size + self.forecast_horizon - 1
        y = self.target[target_idx]

        return torch.from_numpy(X), torch.tensor(y)
```

Usamos el `Dataset` con un `DataLoader` que se encarga de crear los batches automáticamente y de mezclar las ventanas de forma segura:

```python
# Preparamos datos de ejemplo
df = generar_consumo_electrico(
    fecha_inicio="2026-01-01",
    periodos=24*180,
    frecuencia="h",
    incluir_meteorologia=True,
)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").asfreq("h")

# Columnas que usaremos como features
feature_cols = ["consumo_kwh", "temperatura", "hora", "dia_semana"]
df_ml = df[feature_cols].copy().dropna()

# División temporal (sin barajar)
n = len(df_ml)
train_df = df_ml.iloc[:int(n * 0.8)]
val_df   = df_ml.iloc[int(n * 0.8):]

scaler = StandardScaler()
train_df = pd.DataFrame(
    scaler.fit_transform(train_df),
    index=train_df.index,
    columns=train_df.columns,
)
val_df = pd.DataFrame(
    scaler.transform(val_df),
    index=val_df.index,
    columns=val_df.columns,
)

train_ds = TimeSeriesDataset(train_df, target_col="consumo_kwh", window_size=24)
val_ds   = TimeSeriesDataset(val_df,   target_col="consumo_kwh", window_size=24)

train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
val_loader   = DataLoader(val_ds,   batch_size=64, shuffle=False)

# Inspeccionamos un batch
for X_batch, y_batch in train_loader:
    print(f"Shape de X: {X_batch.shape}")   # -> [32, 24, 3] (Batch, Secuencia, Features)
    print(f"Shape de y: {y_batch.shape}")   # -> [32]
    break
```

> **Pregunta para discutir:** Si la ventana tiene `window_size=24` y `forecast_horizon=1`, ¿qué ocurre matemáticamente con los últimos 23 datos del conjunto de validación? ¿Podemos predecirlos? ¿Por qué aparece `self.length = len(df) - window_size - forecast_horizon + 1` en lugar de simplemente `len(df)`?

> **Nota metodológica:** El escalado se ajusta con `fit_transform` solo sobre `train_df` y se aplica con `transform` sobre `val_df`. Ajustar el escalador con toda la serie sería otra forma de fuga de información, porque la media y desviación del futuro entrarían indirectamente en el entrenamiento.

---

## 2. El Perceptrón Multicapa (MLP): El Caso de la Amnesia

La primera red neuronal que estudiaremos es el MLP (*Multi-Layer Perceptron*). Es la versión más básica: un conjunto de capas lineales encadenadas con funciones de activación no lineales (ReLU).

Su problema para las series temporales es la **amnesia temporal**: para poder aceptar el tensor 3D como entrada, primero aplana (`Flatten`) la ventana en un vector 1D larguísimo. Con `window_size=24` y `features=3`, ese vector tiene `24 × 3 = 72` dimensiones. El MLP las trata exactamente igual: el dato número 1 (hace 24 horas) y el dato número 71 (hace 1 hora) pesan exactamente lo mismo. El orden temporal ha desaparecido.

```python
class MLPForecaster(pl.LightningModule):
    def __init__(self, window_size, n_features, hidden_dim=64, lr=1e-3):
        super().__init__()
        self.lr = lr
        input_dim = window_size * n_features
        self.net = nn.Sequential(
            nn.Flatten(),                          # Aplana [Batch, Seq, Feat] -> [Batch, Seq*Feat]
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )
        self.loss_fn = nn.MSELoss()

    def forward(self, x):
        return self.net(x).squeeze()

    def training_step(self, batch, batch_idx):
        x, y = batch
        loss = self.loss_fn(self(x), y)
        self.log("train_loss", loss, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        loss = self.loss_fn(self(x), y)
        self.log("val_loss", loss, prog_bar=True)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.lr)
```

---

## 3. Redes Recurrentes (LSTM): La Cura de la Amnesia

Las LSTMs (*Long Short-Term Memory*) solucionan el problema del MLP con un mecanismo elegante: procesan la ventana temporal **paso a paso**, de principio a fin, manteniendo un **estado oculto** (una memoria interna) que se actualiza con cada nuevo instante.

Es literalmente como leer una novela. Al llegar a la última página, entiendes la trama no porque recuerdes literalmente cada palabra que leíste al principio, sino porque tu mente fue construyendo un **contexto acumulado**. La LSTM hace lo mismo con los datos temporales.

La LSTM tiene además dos mecanismos de control internos: una **"compuerta de olvido"** (que decide qué parte del pasado olvidar) y una **"compuerta de entrada"** (que decide qué información nueva añadir a la memoria). Esta complejidad adicional le cuesta velocidad de entrenamiento, pero le permite capturar dependencias a largo plazo que el MLP no puede ver.

```python
class LSTMForecaster(pl.LightningModule):
    def __init__(self, n_features, hidden_size=64, num_layers=2, dropout=0.1, lr=1e-3):
        super().__init__()
        self.save_hyperparameters()
        self.lr = lr

        # La capa LSTM recibe [Batch, Sequence, Features] gracias a batch_first=True
        self.lstm = nn.LSTM(
            input_size=n_features,
            hidden_size=hidden_size,
            num_layers=num_layers,
            dropout=dropout if num_layers > 1 else 0,
            batch_first=True,
        )
        # Proyección final: del último estado oculto a 1 valor de predicción
        self.head = nn.Linear(hidden_size, 1)
        self.loss_fn = nn.MSELoss()

    def forward(self, x):
        # x: [Batch, Sequence, Features]
        lstm_out, _ = self.lstm(x)
        # Tomamos solo la salida del último timestep: [Batch, hidden_size]
        last_out = lstm_out[:, -1, :]
        return self.head(last_out).squeeze()

    def training_step(self, batch, batch_idx):
        x, y = batch
        loss = self.loss_fn(self(x), y)
        self.log("train_loss", loss, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        loss = self.loss_fn(self(x), y)
        self.log("val_loss", loss, prog_bar=True)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.lr)
```

### Entrenando con PyTorch Lightning

Lightning nos proporciona el `Trainer`, que gestiona automáticamente los bucles de entrenamiento, el movimiento de datos a GPU, y el registro de métricas:

```python
n_features = len(feature_cols) - 1  # Todas las columnas menos el target

modelo = LSTMForecaster(n_features=n_features, hidden_size=64, num_layers=2)

trainer = pl.Trainer(
    max_epochs=20,
    accelerator="auto",     # Usa GPU si existe, si no, CPU
    log_every_n_steps=10,
    logger=False,
    enable_checkpointing=False,
)

trainer.fit(modelo, train_loader, val_loader)
```

### Evaluando frente al Seasonal Naive

```python
# Predicciones en validación
modelo.eval()
preds, actuals = [], []
with torch.no_grad():
    for X_batch, y_batch in val_loader:
        preds.extend(modelo(X_batch).numpy())
        actuals.extend(y_batch.numpy())

mae_lstm = mean_absolute_error(actuals, preds)

# Baseline Seasonal Naive (lo que pasó hace 7 días = 168 horas)
serie_val = val_df["consumo_kwh"]
serie_escalada = pd.concat([train_df, val_df])["consumo_kwh"]
pred_naive = serie_escalada.shift(168).loc[serie_val.index]
mae_naive = mean_absolute_error(serie_val.dropna(), pred_naive.dropna())

print(f"MAE Seasonal Naive:  {mae_naive:.4f}")
print(f"MAE LSTM:            {mae_lstm:.4f}")
```

> **Pregunta para discutir:** Si el MAE de la LSTM es ligeramente peor que el del Seasonal Naive con solo 180 días de datos de entrenamiento, ¿es eso una derrota? ¿Qué pasaría si tuvieras datos de 100 subestaciones distintas? ¿Cómo cambiaría la ecuación?

---

## 4. Actividades de clase

### Actividad 1: La Autopsia del Tensor
Antes de entrenar nada, extrae un único batch del `train_loader` e inspecciónalo. Imprime su `shape`. Luego extrae el primer elemento del batch (`X_batch[0]`) y compara su contenido con las primeras 24 filas del DataFrame original. ¿Coinciden? Esto te confirmará que has construido correctamente el flujo de ventanas.

### Actividad 2: MLP vs LSTM en Igualdad de Condiciones
Entrena el `MLPForecaster` con exactamente los mismos datos y el mismo número de épocas que el `LSTMForecaster`. Compara el `val_loss` final de ambos. ¿Cuál converge más rápido? ¿Cuál tiene un error final menor? ¿Observas algún signo de *overfitting* (que el `train_loss` baja pero el `val_loss` se estanca o sube)?

### Actividad 3: El Efecto de la Memoria
Reentrena la LSTM cambiando el parámetro `window_size` del Dataset a `12` horas y después a `168` horas (una semana completa). ¿Cómo cambia el error de validación? Intenta razonar por qué una ventana más larga no siempre es mejor (pista: más ventana = más ruido que la LSTM tiene que "memorizar").

---

## 5. Ideas clave

- **Local vs Global:** La gran revolución del Deep Learning en forecasting no está en la arquitectura, sino en el paradigma. Entrenar con miles de series simultáneamente permite que la red aprenda patrones universales que ningún modelo clásico puede capturar.
- **El Tensor 3D es el lenguaje:** `[Batch, Sequence, Features]` es la gramática universal de las redes neuronales para series temporales. Interiorizar esta forma de pensar es más importante que memorizar cualquier arquitectura concreta.
- **MLP = Amnesia, LSTM = Memoria:** El MLP trata el tiempo como una tabla desordenada. La LSTM lee el tiempo como una novela, construyendo un contexto acumulado paso a paso.
- **Lightning elimina el ruido:** PyTorch Lightning separa la arquitectura del entrenamiento, permitiéndote concentrarte en lo que importa: el diseño de la red.
- **Más parámetros ≠ Mejores resultados:** Con 180 días de una sola serie, una LSTM puede perder fácilmente contra el Seasonal Naive. El Deep Learning brilla cuando hay *muchos datos* y *muchas series*.

## Continuación

Ahora que entendemos las LSTMs y sus limitaciones, en la próxima sesión exploraremos las **Redes Convolucionales Temporales (TCNs)**: una arquitectura alternativa que resuelve el problema de la lentitud de las LSTMs usando convoluciones 1D con un truco matemático llamado *dilatación*. Las TCNs son paralelizables, más rápidas de entrenar y tienen un campo receptivo que podemos controlar con precisión matemática.
