---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #f8f9fa
style: |
  section {
    font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  }
  h1 {
    color: #2b3a4a;
    border-bottom: 3px solid #8e44ad;
    padding-bottom: 10px;
  }
  h2 { color: #34495e; }
  strong { color: #e74c3c; }
  table { font-size: 0.85em; }
---

# Deep Learning y Modelos Globales
## Taller de Forecasting Práctico con Python

**Sesión 07** · Del Médico de Pueblo al Hospital de Referencia.

---

# El Límite de los Modelos Locales

Hasta la sesión 06, entrenamos un modelo para **una sola serie temporal**.

Funciona bien... hasta que aparece un paciente nuevo o una pandemia.

**El Médico de Pueblo** conoce perfectamente a sus 50 vecinos de siempre.
Si llega alguien nuevo o un virus desconocido, su experiencia es insuficiente.

---

# Modelos Globales y Cross-Learning

**El Hospital de Referencia** ha tratado a cientos de miles de pacientes.

Cuando ve los primeros síntomas, ya reconoce la enfermedad porque la vio en otra ciudad, en otro año.

En Forecasting: entrenamos **una sola red con miles de series**.
La red aprende que "pico + caída de temperatura → rotura de stock", sin importar el producto ni la tienda.

A esto se llama **Cross-Learning**.

---

# Gimnasia Tensorial: De 2D a 3D

**Modelos clásicos (Random Forest):**
```
DataFrame 2D: [Filas × Columnas]
```

**Redes Neuronales:**
```
Tensor 3D: [Batch, Secuencia, Features]
```

Cada "elemento del batch" es una **película de 24 horas**, no una fotografía de un instante.

---

# El Dataset de PyTorch

Creamos una clase que sabe deslizar una ventana sobre la serie:

```python
class TimeSeriesDataset(Dataset):
    def __getitem__(self, idx):
        X = features[idx : idx + window_size]   # [Seq, Feat]
        y = target[idx + window_size]            # escalar
        return torch.from_numpy(X), torch.tensor(y)
```

Con `window_size=24` y una serie de 1000 puntos → **976 ventanas** para entrenar.

---

# MLP vs LSTM: La Amnesia vs La Memoria

**MLP (Perceptrón):**
Aplana la ventana en un vector 1D → pierde el orden temporal.
El dato de hace 24h y el de hace 1h pesan igual.
*Amnesia Total.*

**LSTM (Long Short-Term Memory):**
Lee la secuencia **paso a paso**.
Mantiene un "estado oculto" que se actualiza con cada nuevo instante.
Como leer una novela: el final se entiende gracias a todo lo anterior.

---

# PyTorch Lightning ⚡

Sin Lightning, hay que escribir bucles de entrenamiento de 50 líneas.

Con Lightning, solo defines la arquitectura:

```python
class LSTMForecaster(pl.LightningModule):
    def training_step(self, batch, _):
        x, y = batch
        return self.loss_fn(self(x), y)

trainer = pl.Trainer(max_epochs=20, accelerator="auto")
trainer.fit(modelo, train_loader, val_loader)
```

El `Trainer` gestiona GPU, logging y checkpoints automáticamente.

---

# ¿Cuándo NO usar Deep Learning?

| Situación | Recomendación |
| :--- | :--- |
| 1 serie, pocos datos | **Seasonal Naive o Random Forest** |
| Muchas series similares | **Deep Learning (Cross-Learning)** |
| Horizonte corto y ciclo fuerte | **Holt-Winters o Naive** |
| Series de retail con miles de SKUs | **LSTM/TCN Global** |

> El arte no es usar la red más profunda, sino **saber cuándo no usarla**.

---

# Escalado sin Leakage

En redes neuronales, escalar suele ser obligatorio.

*   `fit` del scaler solo con train.
*   `transform` en validación y test.
*   Nunca usar la media/desviación del futuro.

El preprocesamiento también puede mirar al futuro.

---

# 🚀 ¡A las Redes!

Abre el notebook `07_deep_learning_intro.ipynb`

**Misiones:**
1. Inspeccionar la forma `[32, 24, 3]` de un batch real.
2. Comparar MLP vs LSTM: ¿cuál converge antes?
3. ¿Logra la LSTM batir al Seasonal Naive con solo 180 días de datos?
4. Revisar dónde se ajusta el escalador y por qué.
