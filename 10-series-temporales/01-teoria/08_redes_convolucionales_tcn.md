# Redes Convolucionales Temporales (TCN)

## Sesión 8: Mirando el tiempo a través de una rendija

En la sesión anterior aprendimos que las LSTMs tienen un superpoder: procesan el tiempo de forma secuencial, construyendo una memoria acumulada paso a paso. Pero este superpoder tiene un precio. **Las LSTMs son lentas.** Cada instante de tiempo tiene que esperar a que el anterior termine de procesarse antes de continuar. Cuando tu serie tiene millones de puntos, este procesamiento secuencial se convierte en un cuello de botella que puede hacer que el entrenamiento dure horas o días.

Existe una alternativa que lleva décadas dominando el mundo del procesamiento de señales de audio y vídeo, y que en los últimos años ha demostrado ser extremadamente competitiva en forecasting: las **Redes Convolucionales**. Estamos acostumbrados a asociarlas con las imágenes, pero una convolución no es otra cosa que un detector de patrones locales, y una serie temporal es una señal 1D repleta de patrones locales que conviene detectar.

Las **Temporal Convolutional Networks (TCNs)** son redes convolucionales adaptadas específicamente para el tiempo, con dos trucos matemáticos que resuelven los problemas que tendría una CNN normal al aplicarse a una señal temporal: la **causalidad** y la **dilatación**.

---

## Objetivos

Al terminar esta sesión deberías ser capaz de:

- **Entender** por qué las LSTMs son lentas y cuál es el precio de su memoria secuencial.
- **Explicar** qué es una convolución 1D y cómo puede usarse para detectar patrones en el tiempo.
- **Diferenciar** entre una convolución estándar y una convolución *causal*: por qué es imprescindible que una red temporal no "mire al futuro".
- **Comprender** el concepto de *Dilated Convolutions* y cómo permiten ver horizontes temporales muy lejanos con muy pocas capas.
- **Implementar** un bloque TCN y un modelo completo de forecasting usando PyTorch Lightning.
- **Comparar** TCN y LSTM y razonar cuándo usar cada arquitectura.

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

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import pytorch_lightning as pl

from sklearn.metrics import mean_absolute_error
from series_temporales import generar_consumo_electrico

from torch.utils.data import Dataset


class TimeSeriesDataset(Dataset):
    def __init__(self, df, target_col, window_size=24, forecast_horizon=1):
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

## 1. El Problema de la Secuencialidad

Vamos a hacer una pregunta incómoda: si las LSTMs son tan buenas "recordando" el pasado, ¿por qué necesitamos algo diferente?

El problema no es la precisión, es la **arquitectura de la computación**. Para calcular el estado oculto en el instante $t=500$, la LSTM necesita haber terminado de calcular el estado de $t=499$, que a su vez depende de $t=498$, y así sucesivamente. Este encadenamiento obliga a procesar la secuencia **en serie**, un paso tras otro.

Los procesadores modernos (GPUs) son máquinas diseñadas para hacer millones de operaciones **en paralelo**. Una LSTM los obliga a trabajar en fila, como a los alumnos más lentos de la clase. Una CNN, en cambio, puede aplicar todos sus filtros a todos los puntos de la ventana de forma simultánea: los procesadores trabajan al 100%.

> **La consecuencia práctica:** Entrenar una TCN de forecasting sobre un año de datos horarios puede ser entre 3 y 10 veces más rápido que entrenar una LSTM equivalente.

---

## 2. Las Convoluciones en el Tiempo

### 2.1 La Intuición: Un Detector de Patrones Deslizante

Imagina que tienes una lupa de tamaño 3 que se desplaza a lo largo de tu serie temporal. En cada posición, la lupa observa 3 puntos consecutivos y aplica una operación matemática (un producto escalar) para detectar si hay un patrón específico en esa ventana local.

Ese es exactamente el funcionamiento de una **convolución 1D**. El "patrón a detectar" está codificado en los pesos del filtro, y la red los aprende automáticamente durante el entrenamiento.

La diferencia con respecto a las imágenes (2D) es simplemente que ahora la lupa solo se mueve en una dirección: el eje del tiempo.

### 2.2 El Primer Mandamiento: Causalidad

En una imagen, la lupa de tamaño 3 observa el píxel central y sus dos vecinos (uno a la izquierda, uno a la derecha). En el tiempo, eso sería un pecado: el vecino de la derecha del instante $t$ es el instante $t+1$, que es el **futuro que intentamos predecir**.

Una **Convolución Causal** resuelve esto con elegancia: simplemente añadimos un relleno (`padding`) al inicio de la secuencia para que la lupa, cuando esté en el instante $t$, solo pueda ver los instantes $t-2, t-1$ y $t$. Nunca el futuro.

```text
Convolución Normal (con padding centrado):
... [ t-1, t, t+1 ] ...   ← La lupa en t ve t+1. ILEGAL en forecasting.

Convolución Causal (con padding al inicio):
[ 0,  0, t-2, t-1, t, t+1, t+2 ] → aplicamos la lupa en t
            └── La lupa ve 0, t-2, t-1 o t-2, t-1, t. Nunca t+1. ✓
```

### 2.3 El Superpoder: Convoluciones Dilatadas

Una lupa de tamaño 3 solo ve 3 puntos. Para predecir el consumo eléctrico de mañana, necesitamos que la red "recuerde" lo que pasó hace una semana (168 horas). Con convoluciones causales normales, necesitaríamos una capa por cada hora adicional de contexto: 168 capas. Esto es inviable.

La solución es la **dilatación**: en lugar de mirar 3 puntos consecutivos, la lupa "salta" y mira cada N puntos, donde N es el factor de dilatación.

```text
Dilation=1 (lupa normal):   ● ● ●           → Ve hasta hace 3 pasos
Dilation=2 (salta de 2):    ●   ●   ●       → Ve hasta hace 5 pasos
Dilation=4 (salta de 4):    ●       ●       ●  → Ve hasta hace 9 pasos
```

Si apilamos capas con dilatación exponencial (`1, 2, 4, 8, 16...`), el **campo receptivo** (cuánto atrás puede "ver" la red) crece de forma exponencial con cada capa.

Con solo 8 capas de dilatación exponencial y filtros de tamaño 3, nuestra red puede ver hasta `2^8 * 2 = 512` pasos atrás. En datos horarios, eso son más de 3 semanas. Con 10 capas, más de 3 meses. **Con una profundidad de red completamente manejable.**

---

## 3. Implementación con PyTorch Lightning

Construimos la arquitectura TCN desde cero en dos piezas: el bloque convolucional reutilizable (`TCNBlock`) y el modelo completo de forecasting.

```python
class TCNBlock(nn.Module):
    """
    Bloque básico de una TCN: Convolución 1D Causal Dilatada + Residual Connection.
    """
    def __init__(self, in_channels, out_channels, kernel_size=3, dilation=1, dropout=0.2):
        super().__init__()
        # El padding causal se calcula para que la salida tenga la misma longitud que la entrada
        # y que la red no vea el futuro.
        self.padding = (kernel_size - 1) * dilation

        self.conv1 = nn.Conv1d(
            in_channels, out_channels, kernel_size,
            padding=self.padding, dilation=dilation
        )
        self.conv2 = nn.Conv1d(
            out_channels, out_channels, kernel_size,
            padding=self.padding, dilation=dilation
        )
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout)

        # Conexión residual: si los canales de entrada y salida son distintos,
        # usamos una convolución 1x1 para igualar las dimensiones.
        self.downsample = nn.Conv1d(in_channels, out_channels, 1) \
            if in_channels != out_channels else None

    def forward(self, x):
        # x: [Batch, Channels, Sequence]
        residual = x
        out = self.relu(self.conv1(x))
        # Recortar el padding sobrante del futuro (causalidad)
        out = out[:, :, :-self.padding] if self.padding > 0 else out
        out = self.dropout(out)
        out = self.relu(self.conv2(out))
        out = out[:, :, :-self.padding] if self.padding > 0 else out
        out = self.dropout(out)

        # Aplicar la conexión residual
        if self.downsample is not None:
            residual = self.downsample(x)
        return self.relu(out + residual)


class TCNForecaster(pl.LightningModule):
    """
    Modelo completo de Forecasting basado en TCN.
    """
    def __init__(self, n_features, num_channels=None, kernel_size=3, dropout=0.2, lr=1e-3):
        super().__init__()
        self.save_hyperparameters()
        self.lr = lr
        if num_channels is None:
            num_channels = [32, 64, 64]

        layers = []
        in_ch = n_features
        for i, out_ch in enumerate(num_channels):
            dilation = 2 ** i  # 1, 2, 4, 8... crecimiento exponencial del campo receptivo
            layers.append(TCNBlock(in_ch, out_ch, kernel_size=kernel_size,
                                   dilation=dilation, dropout=dropout))
            in_ch = out_ch

        self.network = nn.Sequential(*layers)
        self.head = nn.Linear(num_channels[-1], 1)
        self.loss_fn = nn.MSELoss()

    def forward(self, x):
        # PyTorch Conv1d espera [Batch, Channels, Sequence]
        # Nuestro Dataset entrega [Batch, Sequence, Channels] -> Transponemos
        x = x.permute(0, 2, 1)

        features = self.network(x)   # -> [Batch, Channels, Sequence]
        # Tomamos la "opinión" de la red en el último instante temporal
        out = self.head(features[:, :, -1])  # -> [Batch, 1]
        return out.squeeze()

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

### Entrenando la TCN

```python
df = generar_consumo_electrico(
    fecha_inicio="2026-01-01",
    periodos=24*180,
    frecuencia="h",
    incluir_meteorologia=True,
)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").asfreq("h")

feature_cols = ["consumo_kwh", "temperatura", "hora", "dia_semana"]
df_ml = df[feature_cols].dropna()

n = len(df_ml)
train_df = df_ml.iloc[:int(n * 0.8)]
val_df = df_ml.iloc[int(n * 0.8):]

train_ds = TimeSeriesDataset(train_df, target_col="consumo_kwh", window_size=168)
val_ds = TimeSeriesDataset(val_df, target_col="consumo_kwh", window_size=168)
train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)
val_loader = DataLoader(val_ds, batch_size=128, shuffle=False)

n_features = len(feature_cols) - 1
modelo_tcn = TCNForecaster(n_features=n_features, num_channels=[32, 64, 64])

trainer = pl.Trainer(
    max_epochs=20,
    accelerator="auto",
    logger=False,
    enable_checkpointing=False,
)
trainer.fit(modelo_tcn, train_loader, val_loader)
```

---

## 4. El Campo Receptivo: Visualizando Cuánto "Ve" la Red

El campo receptivo total de una TCN se puede calcular matemáticamente:

```text
Campo Receptivo = 1 + (kernel_size - 1) * Suma(dilations)
                = 1 + (3 - 1) * (1 + 2 + 4)  = 1 + 14 = 15  (con 3 capas)
                = 1 + (3 - 1) * (1 + 2 + 4 + 8) = 1 + 30 = 31 (con 4 capas)
```

Esto nos permite **diseñar la red** a partir del horizonte de contexto que queremos:

```python
def calcular_campo_receptivo(num_capas, kernel_size):
    """Calcula el campo receptivo de una TCN con dilatación exponencial."""
    suma_dilaciones = sum(2**i for i in range(num_capas))
    return 1 + (kernel_size - 1) * suma_dilaciones

for n_capas in [3, 4, 5, 6, 8, 10]:
    cr = calcular_campo_receptivo(n_capas, kernel_size=3)
    print(f"  {n_capas:2d} capas -> Campo Receptivo: {cr:5d} pasos ({cr/24:.1f} días)")
```

> **Pregunta para discutir:** Si tus datos son horarios y la estacionalidad principal es semanal (168 horas), ¿cuántas capas de dilatación exponencial con `kernel_size=3` necesitas como mínimo para asegurarte de que la red tenga contexto suficiente para "ver" un ciclo completo de 7 días? ¿Coincide tu respuesta teórica con lo que muestra el código anterior?

---

## 5. Comparativa: TCN vs LSTM

| Característica | LSTM | TCN |
| :--- | :--- | :--- |
| **Procesamiento** | Secuencial (un paso tras otro) | Paralelo (todos los pasos a la vez) |
| **Velocidad de entrenamiento** | Lenta en secuencias largas | Rápida (paralelizable en GPU) |
| **Campo de contexto** | Teóricamente infinito, en práctica limitado por el *vanishing gradient* | Exactamente controlable mediante la dilatación |
| **Estabilidad del entrenamiento** | Propensa a gradientes explosivos/desvanecientes | Más estable (conexiones residuales) |
| **Interpretabilidad** | Baja: el estado oculto no es legible | Media: los filtros pueden visualizarse |
| **Cuándo usar** | Cuando el orden exacto y las dependencias largas son críticas | Cuando se necesita velocidad y el contexto es definible |

---

## 6. Actividades de clase

### Actividad 1: Visualizando el Campo Receptivo
Usando la función `calcular_campo_receptivo`, dibuja una gráfica donde el eje X sea el número de capas (de 1 a 12) y el eje Y sea el campo receptivo resultante (en días, para datos horarios). ¿En qué punto añadir una capa nueva ya no aportaría un contexto que no cubra la estacionalidad principal de la serie?

### Actividad 2: TCN vs LSTM en Velocidad
Entrena tanto el `LSTMForecaster` de la sesión anterior como el `TCNForecaster` durante 10 épocas sobre el mismo conjunto de datos. Usa `time.time()` para medir el tiempo real de entrenamiento de cada uno. Compara tiempos y MAE de validación. ¿Sale rentable la TCN?

### Actividad 3: Diseñando para el Negocio
Imagina que trabajas en Renfe y tienes datos de viajeros por tren cada 15 minutos. Sabes que la estacionalidad principal es semanal. Diseña (a papel y lápiz, sin código) una TCN con el mínimo número de capas necesario para que el campo receptivo cubra al menos 1 semana completa de datos a resolución de 15 minutos. Escribe la lista de dilaciones que usarías.

---

## 7. Ideas clave

- **Las LSTMs son secuenciales, las TCNs son paralelas:** Esta diferencia arquitectónica tiene un impacto enorme en la velocidad de entrenamiento, especialmente cuando tienes millones de puntos de datos.
- **La causalidad no es opcional:** Cualquier red temporal que "mire al futuro" durante el entrenamiento te dará un modelo que parece perfecto en validación y falla estrepitosamente en producción.
- **La dilatación es un diseño explícito:** A diferencia de la LSTM (donde la longitud del contexto "útil" depende de la inicialización aleatoria de los pesos), en una TCN el campo receptivo es una decisión de diseño que puedes calcular matemáticamente antes de entrenar.
- **Las conexiones residuales son el seguro de vida:** Permiten que el gradiente fluya directamente hacia las capas anteriores sin "atravesar" las capas convolucionales, evitando el problema del *vanishing gradient*.

## Continuación

Hemos explorado dos familias de redes neuronales para el tiempo: las recurrentes (LSTM) y las convolucionales (TCN). Pero existe una tercera familia que en los últimos años ha acaparado toda la atención del mundo del Deep Learning: los **Transformers**. En la próxima sesión los examinaremos con espíritu crítico, porque su aplicación al tiempo no es tan obvia como en el lenguaje, y existe un debate científico activo sobre si realmente aportan valor frente a modelos mucho más simples.
