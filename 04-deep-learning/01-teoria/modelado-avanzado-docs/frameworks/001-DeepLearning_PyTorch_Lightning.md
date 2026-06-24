---
title: "Deep Learning con PyTorch Lightning"
output:
  pdf_document:
    toc: true
    toc_depth: 3
  engine: lualatex

---

# Deep Learning con PyTorch Lightning

PyTorch Lightning es una capa de alto nivel construida sobre PyTorch. Su objetivo es separar la **lógica científica** del modelo de la **infraestructura de entrenamiento**: bucles de entrenamiento, validación, callbacks, checkpoints, logging, entrenamiento distribuido y uso de aceleradores.

La idea clave es simple: **sigues usando PyTorch**, pero con una estructura más clara y menos código repetitivo.

## 1. ¿Qué aporta Lightning sobre PyTorch?

### 1.1 Ventajas principales

- **Menos boilerplate**: evita escribir a mano los bucles de entrenamiento y validación.
- **Código más mantenible**: organiza el proyecto en `LightningModule`, `DataModule`, callbacks y loggers.
- **Escala mejor**: CPU, GPU, multi-GPU, mixed precision y entrenamiento distribuido con pocos cambios.
- **Experimentación reproducible**: checkpoints, early stopping y logging integrados.
- **Sigue siendo PyTorch**: puedes usar tensores, `nn.Module`, optimizadores y schedulers estándar.

### 1.2 Cuándo usar Lightning

Lightning encaja especialmente bien cuando:

- vas a entrenar varios modelos y quieres código consistente;
- necesitas validación, logging y checkpoints desde el principio;
- quieres mover el mismo proyecto de CPU a GPU o multi-GPU sin reescribir el entrenamiento;
- el equipo trabaja mejor con convenciones claras.

### 1.3 Cuándo PyTorch puro puede ser mejor

PyTorch puro puede resultar más adecuado cuando:

- estás investigando una idea muy experimental con un loop muy poco estándar;
- necesitas control total de cada operación del entrenamiento;
- quieres minimizar la abstracción para enseñar los fundamentos internos;
- estás depurando un comportamiento muy fino del backward o del optimizador.

---

## 2. Instalación

```bash
pip install torch torchvision torchaudio
pip install lightning torchmetrics
```

En muchos proyectos modernos también se usa:

```bash
pip install tensorboard optuna
```

---

## 3. Estructura básica de un proyecto Lightning

En Lightning normalmente se separan estas piezas:

- **Modelo**: arquitectura y lógica de entrenamiento en un `LightningModule`.
- **Datos**: carga y preprocesado en un `LightningDataModule`.
- **Trainer**: ejecuta `fit`, `validate`, `test` y `predict`.
- **Callbacks y loggers**: early stopping, checkpoints, TensorBoard, CSV, etc.

Ejemplo de flujo:

```python
model = MiModeloLightning(...)
datamodule = MiDataModule(...)

trainer = L.Trainer(max_epochs=20)
trainer.fit(model, datamodule=datamodule)
trainer.test(model, datamodule=datamodule)
preds = trainer.predict(model, datamodule=datamodule)
```

---

## 4. `LightningModule`: redes, pérdida y optimización

### 4.1 Modelo básico para clasificación

```python
import lightning as L
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchmetrics

class ClasificadorMLP(L.LightningModule):
    def __init__(self, input_dim=784, hidden_dim=256, num_classes=10, lr=1e-3):
        super().__init__()
        self.save_hyperparameters()

        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes)
        )

        self.criterion = nn.CrossEntropyLoss()
        self.train_acc = torchmetrics.classification.Accuracy(
            task="multiclass", num_classes=num_classes
        )
        self.val_acc = torchmetrics.classification.Accuracy(
            task="multiclass", num_classes=num_classes
        )

    def forward(self, x):
        return self.net(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)
        acc = self.train_acc(logits, y)

        self.log("train_loss", loss, prog_bar=True, on_step=False, on_epoch=True)
        self.log("train_acc", acc, prog_bar=True, on_step=False, on_epoch=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)
        acc = self.val_acc(logits, y)

        self.log("val_loss", loss, prog_bar=True, on_step=False, on_epoch=True)
        self.log("val_acc", acc, prog_bar=True, on_step=False, on_epoch=True)

    def predict_step(self, batch, batch_idx, dataloader_idx=0):
        x, _ = batch
        logits = self(x)
        probs = torch.softmax(logits, dim=1)
        preds = torch.argmax(probs, dim=1)
        return preds

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.hparams.lr)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, mode="min", factor=0.5, patience=3
        )

        return {
            "optimizer": optimizer,
            "lr_scheduler": {
                "scheduler": scheduler,
                "monitor": "val_loss"
            }
        }
```

### 4.2 Qué hace cada método

- `forward`: define el paso hacia delante.
- `training_step`: define cómo se calcula la pérdida en entrenamiento.
- `validation_step`: evalúa en validación.
- `predict_step`: especifica qué devolver al predecir.
- `configure_optimizers`: define optimizadores y schedulers.

---

## 5. `LightningDataModule`: preparar y servir datos

Lightning recomienda separar la gestión de datos del modelo.

```python
import lightning as L
import torch
from torch.utils.data import DataLoader, TensorDataset, random_split

class TabularDataModule(L.LightningDataModule):
    def __init__(self, X, y, batch_size=32):
        super().__init__()
        self.X = X
        self.y = y
        self.batch_size = batch_size

    def setup(self, stage=None):
        dataset = TensorDataset(self.X, self.y)
        n_total = len(dataset)
        n_train = int(0.7 * n_total)
        n_val = int(0.15 * n_total)
        n_test = n_total - n_train - n_val

        self.train_ds, self.val_ds, self.test_ds = random_split(
            dataset, [n_train, n_val, n_test]
        )

    def train_dataloader(self):
        return DataLoader(self.train_ds, batch_size=self.batch_size, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val_ds, batch_size=self.batch_size)

    def test_dataloader(self):
        return DataLoader(self.test_ds, batch_size=self.batch_size)

    def predict_dataloader(self):
        return DataLoader(self.test_ds, batch_size=self.batch_size)
```

Ventajas del `DataModule`:

- reutiliza la misma lógica de datos en entrenamiento, test e inferencia;
- facilita cambiar de dataset sin tocar el modelo;
- ayuda a mantener el proyecto ordenado.

---

## 6. Entrenamiento con `Trainer`

### 6.1 Entrenamiento básico

```python
import lightning as L

trainer = L.Trainer(
    max_epochs=20,
    accelerator="auto",   # cpu, gpu, tpu, mps...
    devices="auto"
)

trainer.fit(model, datamodule=datamodule)
```

### 6.2 Validación, test y predicción

```python
trainer.validate(model, datamodule=datamodule)
trainer.test(model, datamodule=datamodule)
predicciones = trainer.predict(model, datamodule=datamodule)
```

### 6.3 Mixed precision y GPU

```python
trainer = L.Trainer(
    max_epochs=30,
    accelerator="gpu",
    devices=1,
    precision="16-mixed"
)
```

Con muy pocos cambios puedes aprovechar hardware más potente sin reescribir el loop.

---

## 7. Callbacks habituales

### 7.1 Early stopping y checkpoints

```python
from lightning.pytorch.callbacks import EarlyStopping, ModelCheckpoint

early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=5,
    mode="min"
)

checkpoint = ModelCheckpoint(
    monitor="val_loss",
    mode="min",
    save_top_k=1,
    filename="mejor-modelo-{epoch:02d}-{val_loss:.3f}"
)

trainer = L.Trainer(
    max_epochs=50,
    callbacks=[early_stopping, checkpoint]
)
```

### 7.2 Logging

```python
from lightning.pytorch.loggers import TensorBoardLogger, CSVLogger

tb_logger = TensorBoardLogger("logs", name="experimento_mlp")
csv_logger = CSVLogger("logs", name="experimento_csv")

trainer = L.Trainer(
    logger=[tb_logger, csv_logger]
)
```

---

## 8. Guardar, cargar y reanudar entrenamiento

### 8.1 Guardar checkpoints

Lightning guarda checkpoints con:

- pesos del modelo;
- estado del optimizador;
- estado del scheduler;
- época y paso global;
- hiperparámetros guardados con `save_hyperparameters()`.

### 8.2 Cargar desde checkpoint

```python
modelo = ClasificadorMLP.load_from_checkpoint(
    "logs/experimento_mlp/version_0/checkpoints/mejor.ckpt"
)
```

### 8.3 Reanudar entrenamiento

```python
trainer.fit(modelo, datamodule=datamodule, ckpt_path="last")
```

---

## 9. Predicción e inferencia

### 9.1 Predicción por lotes

```python
preds = trainer.predict(modelo, dataloaders=predict_loader)
```

`trainer.predict()` pone el modelo en modo evaluación y gestiona correctamente la inferencia.

### 9.2 Inferencia manual

También puedes usar el modelo como un `nn.Module` normal:

```python
modelo.eval()
with torch.no_grad():
    logits = modelo(x_nuevo)
    probs = torch.softmax(logits, dim=1)
    clase = probs.argmax(dim=1)
```

Esto es importante: **Lightning no sustituye PyTorch**, lo organiza.

---

## 10. CNN y otros tipos de red

Lightning no impone una arquitectura concreta. La red interna puede ser una MLP, CNN, LSTM, GRU o Transformer.

### 10.1 Ejemplo con CNN

```python
class LitCNN(L.LightningModule):
    def __init__(self, lr=1e-3, num_classes=10):
        super().__init__()
        self.save_hyperparameters()

        self.features = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(128, num_classes)
        )
        self.loss_fn = nn.CrossEntropyLoss()

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        return torch.optim.AdamW(self.parameters(), lr=self.hparams.lr)
```

---

## 11. Tuning de hiperparámetros

### 11.1 Qué hiperparámetros suele tener sentido ajustar

- `learning_rate`
- `batch_size`
- número de capas
- tamaño de capas ocultas
- `dropout`
- `weight_decay`
- tipo de optimizador
- scheduler

### 11.2 Preparar el modelo para tuning

El patrón habitual es exponer hiperparámetros en `__init__`:

```python
class ClasificadorMLP(L.LightningModule):
    def __init__(self, input_dim=784, hidden_dim=128, dropout=0.2, lr=1e-3):
        super().__init__()
        self.save_hyperparameters()
        ...
```

### 11.3 Ejemplo con Optuna

```python
import optuna
import lightning as L

def objective(trial):
    hidden_dim = trial.suggest_categorical("hidden_dim", [64, 128, 256])
    dropout = trial.suggest_float("dropout", 0.1, 0.5)
    lr = trial.suggest_float("lr", 1e-4, 1e-2, log=True)

    model = ClasificadorMLP(
        input_dim=784,
        hidden_dim=hidden_dim,
        num_classes=10,
        lr=lr
    )
    model.net[2].p = dropout

    trainer = L.Trainer(
        max_epochs=10,
        enable_checkpointing=False,
        logger=False,
        enable_progress_bar=False
    )
    trainer.fit(model, datamodule=datamodule)

    return trainer.callback_metrics["val_loss"].item()

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=20)

print(study.best_params)
```

### 11.4 Recomendación práctica

Para tuning serio:

- usa pocas épocas al principio para filtrar configuraciones;
- monitoriza `val_loss` o una métrica estable;
- guarda el mejor checkpoint;
- al final reentrena el mejor conjunto de hiperparámetros con más épocas.

---

## 12. Entrenamiento manual y optimización avanzada

Aquí está una de las preguntas más importantes: **si necesitamos tocar la base PyTorch, se puede**. Sí, y Lightning está pensado para permitirlo.

### 12.1 Optimización automática

Por defecto, Lightning hace:

- `optimizer.zero_grad()`
- `loss.backward()`
- `optimizer.step()`

Es decir, automatiza el patrón clásico de PyTorch.

### 12.2 Manual optimization

Si necesitas más control, puedes desactivar la optimización automática:

```python
class GANModule(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.automatic_optimization = False
        ...

    def training_step(self, batch, batch_idx):
        opt_g, opt_d = self.optimizers()
        x_real, _ = batch

        # Entrenar discriminador
        loss_d = self.compute_discriminator_loss(x_real)
        opt_d.zero_grad()
        self.manual_backward(loss_d)
        opt_d.step()

        # Entrenar generador
        loss_g = self.compute_generator_loss(x_real)
        opt_g.zero_grad()
        self.manual_backward(loss_g)
        opt_g.step()

        self.log("loss_g", loss_g)
        self.log("loss_d", loss_d)

    def configure_optimizers(self):
        opt_g = torch.optim.Adam(self.generator.parameters(), lr=1e-4)
        opt_d = torch.optim.Adam(self.discriminator.parameters(), lr=1e-4)
        return [opt_g, opt_d]
```

Esto es útil en:

- GANs;
- entrenamiento adversarial;
- varios optimizadores;
- acumulación o manipulación especial de gradientes;
- algoritmos no estándar.

### 12.3 Tocar la base PyTorch

Aunque uses Lightning, sigues pudiendo:

- definir cualquier `nn.Module`;
- usar cualquier optimizador de `torch.optim`;
- aplicar `gradient clipping`;
- congelar o descongelar capas;
- escribir pérdidas personalizadas;
- modificar el backward o la actualización de parámetros;
- usar operaciones de bajo nivel sobre tensores.

Ejemplo de congelación parcial:

```python
for param in self.backbone.parameters():
    param.requires_grad = False

for param in self.backbone.layer4.parameters():
    param.requires_grad = True
```

Ejemplo de clipping:

```python
trainer = L.Trainer(
    gradient_clip_val=1.0,
    gradient_clip_algorithm="norm"
)
```

### 12.4 Si Lightning no basta

Si una personalización extrema se vuelve incómoda, siempre puedes:

- bajar a PyTorch puro en ese proyecto;
- usar Lightning solo para parte del flujo;
- mantener la arquitectura en PyTorch y reescribir solo el loop.

No hay bloqueo técnico: Lightning **no te encierra**.

---

## 13. Comparación con PyTorch puro

### 13.1 PyTorch puro

En PyTorch puro tú escribes explícitamente:

- el `Dataset` y `DataLoader`;
- el modelo `nn.Module`;
- el loop de entrenamiento;
- el loop de validación;
- la lógica de logging;
- la gestión de checkpoints;
- el uso de GPU o multi-GPU.

Ejemplo típico:

```python
for epoch in range(num_epochs):
    model.train()
    for x, y in train_loader:
        optimizer.zero_grad()
        logits = model(x)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()
```

### 13.2 Lightning

En Lightning defines:

- el modelo;
- qué ocurre en `training_step`;
- qué ocurre en `validation_step`;
- optimizadores y schedulers;
- datos en un `DataModule`;
- configuración del `Trainer`.

### 13.3 Resumen de diferencias

| Aspecto | PyTorch puro | PyTorch Lightning |
|---|---|---|
| Control fino | Máximo | Muy alto, con algo más de estructura |
| Boilerplate | Alto | Bajo |
| Curva inicial | Media | Baja-media si ya conoces PyTorch |
| Depuración del loop | Muy directa | Directa, pero con capas adicionales |
| Escalado a GPU/distribuido | Más manual | Más automático |
| Reproducibilidad | Manual | Más integrada |
| Proyectos en equipo | Más heterogéneos | Más consistentes |

### 13.4 Regla práctica

- **Aprender fundamentos**: empieza por PyTorch puro.
- **Entrenar proyectos reales con orden y rapidez**: Lightning suele ser mejor.
- **Investigación muy experimental**: depende, pero PyTorch puro puede dar más libertad.

---

## 14. Transfer learning

```python
from torchvision.models import resnet18

class LitTransfer(L.LightningModule):
    def __init__(self, num_classes=2, lr=1e-3):
        super().__init__()
        self.save_hyperparameters()

        self.backbone = resnet18(weights="IMAGENET1K_V1")

        for param in self.backbone.parameters():
            param.requires_grad = False

        in_features = self.backbone.fc.in_features
        self.backbone.fc = nn.Linear(in_features, num_classes)
        self.loss_fn = nn.CrossEntropyLoss()

    def forward(self, x):
        return self.backbone(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.hparams.lr)
```

Para fine-tuning progresivo puedes descongelar capas concretas más adelante.

---

## 15. Buenas prácticas

- Usa `self.save_hyperparameters()` para registrar la configuración.
- Separa datos y modelo con `LightningDataModule`.
- Monitoriza siempre `val_loss` y alguna métrica de negocio.
- Guarda checkpoints y activa early stopping.
- Empieza con optimización automática; usa manual solo cuando haya una razón clara.
- Si algo no es estándar, recuerda que sigues teniendo toda la potencia de PyTorch.

---

## 16. Conclusiones

PyTorch Lightning es una forma muy eficiente de trabajar con PyTorch cuando quieres:

- construir redes neuronales con menos código repetitivo;
- entrenar, validar, testear y predecir con una API homogénea;
- hacer tuning de hiperparámetros y experimentación reproducible;
- escalar fácilmente a GPU, mixed precision o entrenamiento distribuido.

No reemplaza a PyTorch, sino que lo estructura. Y si necesitas optimizar algo tocando la base en PyTorch, normalmente **sí es posible**, ya sea mediante optimización manual, módulos personalizados o bajando temporalmente al nivel de PyTorch puro.
