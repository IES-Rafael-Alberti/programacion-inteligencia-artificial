# Introducción a PyTorch Lightning

**PyTorch Lightning** es un framework de código abierto que simplifica el entrenamiento de modelos de deep learning construidos con PyTorch. Abstrae el código repetitivo y permite que los investigadores y desarrolladores se enfoquen en la lógica del modelo en lugar de en los detalles de implementación.

## ¿Por qué usar PyTorch Lightning?

### Problemas que resuelve

Sin PyTorch Lightning, el código de entrenamiento típico incluye:

- Loops de entrenamiento y validación manuales
- Gestión de dispositivos (CPU/GPU)
- Logging y checkpointing
- Sincronización de datos distribuidos
- Manejo de mixed precision training

Todo esto hace que el código sea **verbose, repetitivo y propenso a errores**.

### Ventajas principales

| Característica | Beneficio |
|---|---|
| **Código limpio** | Separa la lógica del modelo del código de entrenamiento |
| **Escalabilidad** | Entrena en múltiples GPUs o TPUs con cambios mínimos |
| **Reproducibilidad** | Manejo automático de seeds y configuración |
| **Logging integrado** | Compatible con TensorBoard, Weights & Biases, Neptune, etc. |
| **Checkpointing automático** | Guarda modelos automáticamente durante el entrenamiento |
| **Flexibilidad** | Mantiene el poder de PyTorch sin sacrificar control |

## Conceptos clave

### 1. LightningModule

Es la clase base donde defines tu modelo y la lógica de entrenamiento:

```python
import pytorch_lightning as pl
import torch
import torch.nn as nn
from torch.optim import Adam

class MiModeloLightning(pl.LightningModule):
    def __init__(self, input_size=784, hidden_size=128, num_classes=10):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, num_classes)
        )
        self.loss_fn = nn.CrossEntropyLoss()
    
    def forward(self, x):
        return self.model(x)
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y)
        self.log('train_loss', loss)
        return loss
    
    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y)
        preds = torch.argmax(logits, dim=1)
        acc = (preds == y).float().mean()
        self.log('val_loss', loss)
        self.log('val_acc', acc)
    
    def configure_optimizers(self):
        return Adam(self.parameters(), lr=1e-3)
```

### 2. Trainer

Maneja todo el loop de entrenamiento:

```python
from pytorch_lightning import Trainer

# Crear el modelo
modelo = MiModeloLightning()

# Crear el trainer
trainer = Trainer(
    max_epochs=10,
    accelerator='gpu',  # o 'cpu'
    devices=1,
    log_every_n_steps=10
)

# Entrenar
trainer.fit(modelo, train_dataloaders, val_dataloaders)
```

### 3. DataModule

Encapsula toda la lógica de datos:

```python
from pytorch_lightning import LightningDataModule
from torch.utils.data import DataLoader, TensorDataset

class MiDataModule(LightningDataModule):
    def __init__(self, batch_size=32):
        super().__init__()
        self.batch_size = batch_size
    
    def setup(self, stage=None):
        # Cargar datos aquí
        self.train_data = TensorDataset(X_train, y_train)
        self.val_data = TensorDataset(X_val, y_val)
    
    def train_dataloader(self):
        return DataLoader(self.train_data, batch_size=self.batch_size, shuffle=True)
    
    def val_dataloader(self):
        return DataLoader(self.val_data, batch_size=self.batch_size)
```

## Ejemplo completo: Clasificación MNIST

```python
import pytorch_lightning as pl
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 1. Definir el modelo
class RedNeuronalMNIST(pl

# Ejemplo comentado: Lightning con CNN

## Objetivo

Vamos a entrenar una **CNN sencilla** para clasificar imágenes de dígitos manuscritos con **MNIST**.

Además vamos a usar dos cosas muy típicas en proyectos reales:

* **EarlyStopping** → parar si deja de mejorar
* **ModelCheckpoint** → guardar el mejor modelo

---

## Código completo comentado

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

from torchvision import datasets, transforms

import lightning as L
from lightning.pytorch.callbacks import EarlyStopping, ModelCheckpoint
from lightning.pytorch.loggers import CSVLogger


# ============================================================
# 1. Definimos el modelo como LightningModule
# ============================================================
class LitMNISTCNN(L.LightningModule):
    def __init__(self, lr=1e-3):
        """
        lr: learning rate del optimizador
        """
        super().__init__()

        # Guarda automáticamente los hiperparámetros en el checkpoint
        self.save_hyperparameters()

        # --------------------------------------------------------
        # Red convolucional sencilla:
        # Entrada: imágenes MNIST de 1x28x28
        # --------------------------------------------------------
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)

        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        # Tras dos maxpool:
        # 28x28 -> 14x14 -> 7x7
        # Canales finales: 32
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        """
        Forward pass:
        x tiene forma (batch_size, 1, 28, 28)
        """
        x = self.conv1(x)          # (batch, 16, 28, 28)
        x = F.relu(x)
        x = self.pool(x)           # (batch, 16, 14, 14)

        x = self.conv2(x)          # (batch, 32, 14, 14)
        x = F.relu(x)
        x = self.pool(x)           # (batch, 32, 7, 7)

        x = torch.flatten(x, 1)    # (batch, 32*7*7)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)            # (batch, 10)

        return x

    def training_step(self, batch, batch_idx):
        """
        Qué hacer en cada batch de entrenamiento.
        Lightning se encarga del resto:
        backward, optimizer.step(), zero_grad(), etc.
        """
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)

        # accuracy simple
        preds = torch.argmax(logits, dim=1)
        acc = (preds == y).float().mean()

        # self.log registra métricas
        # prog_bar=True hace que aparezcan en la barra de progreso
        self.log("train_loss", loss, prog_bar=True, on_step=False, on_epoch=True)
        self.log("train_acc", acc, prog_bar=True, on_step=False, on_epoch=True)

        return loss

    def validation_step(self, batch, batch_idx):
        """
        Qué hacer en validación.
        """
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)

        preds = torch.argmax(logits, dim=1)
        acc = (preds == y).float().mean()

        self.log("val_loss", loss, prog_bar=True, on_step=False, on_epoch=True)
        self.log("val_acc", acc, prog_bar=True, on_step=False, on_epoch=True)

    def test_step(self, batch, batch_idx):
        """
        Evaluación final sobre test.
        """
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)

        preds = torch.argmax(logits, dim=1)
        acc = (preds == y).float().mean()

        self.log("test_loss", loss, prog_bar=True, on_step=False, on_epoch=True)
        self.log("test_acc", acc, prog_bar=True, on_step=False, on_epoch=True)

    def configure_optimizers(self):
        """
        Aquí definimos optimizador y, si queremos, scheduler.
        """
        optimizer = torch.optim.Adam(self.parameters(), lr=self.hparams.lr)

        # También añadimos un scheduler para reducir LR si val_loss se estanca
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer,
            mode="min",
            factor=0.5,
            patience=2
        )

        return {
            "optimizer": optimizer,
            "lr_scheduler": {
                "scheduler": scheduler,
                "monitor": "val_loss",   # métrica que observa el scheduler
                "interval": "epoch",
                "frequency": 1
            }
        }


# ============================================================
# 2. Función principal
# ============================================================
def main():
    # --------------------------------------------------------
    # Transformación:
    # Convierte imagen PIL a tensor [0,1]
    # --------------------------------------------------------
    transform = transforms.ToTensor()

    # --------------------------------------------------------
    # Datasets
    # --------------------------------------------------------
    train_dataset = datasets.MNIST(
        root="./data",
        train=True,
        download=True,
        transform=transform
    )

    test_dataset = datasets.MNIST(
        root="./data",
        train=False,
        download=True,
        transform=transform
    )

    # --------------------------------------------------------
    # Dividimos train en train y validación
    # --------------------------------------------------------
    train_size = int(0.9 * len(train_dataset))
    val_size = len(train_dataset) - train_size

    train_dataset, val_dataset = torch.utils.data.random_split(
        train_dataset,
        [train_size, val_size]
    )

    # --------------------------------------------------------
    # DataLoaders
    # --------------------------------------------------------
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False, num_workers=4)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False, num_workers=4)

    # --------------------------------------------------------
    # Modelo
    # --------------------------------------------------------
    model = LitMNISTCNN(lr=1e-3)

    # --------------------------------------------------------
    # Callbacks
    # --------------------------------------------------------

    # Early stopping:
    # si val_loss no mejora durante 3 épocas, se para
    early_stopping = EarlyStopping(
        monitor="val_loss",
        mode="min",
        patience=3,
        verbose=True
    )

    # Guardar el mejor modelo según val_loss
    checkpoint_callback = ModelCheckpoint(
        monitor="val_loss",
        mode="min",
        save_top_k=1,
        filename="best-mnist-cnn-{epoch:02d}-{val_loss:.4f}"
    )

    # Logger a CSV para guardar métricas
    logger = CSVLogger(save_dir="logs", name="mnist_cnn_lightning")

    # --------------------------------------------------------
    # Trainer
    # --------------------------------------------------------
    trainer = L.Trainer(
        max_epochs=15,
        accelerator="auto",   # usa GPU si la hay, si no CPU
        devices="auto",
        logger=logger,
        callbacks=[early_stopping, checkpoint_callback]
    )

    # --------------------------------------------------------
    # Entrenamiento
    # --------------------------------------------------------
    trainer.fit(model, train_loader, val_loader)

    # --------------------------------------------------------
    # Evaluación final
    # Se carga automáticamente el mejor checkpoint al usar ckpt_path="best"
    # --------------------------------------------------------
    trainer.test(model, dataloaders=test_loader, ckpt_path="best")

    print("\nMejor checkpoint guardado en:")
    print(checkpoint_callback.best_model_path)


if __name__ == "__main__":
    main()
```

---

# Qué están aprendiendo aquí realmente

## 1. `LightningModule`

Esta clase encapsula todo lo importante del modelo:

* arquitectura
* forward
* entrenamiento
* validación
* test
* optimizador

Es decir, Lightning obliga a **organizar el código**.

---

## 2. `training_step`

Aquí escribimos la lógica del batch:

```python
x, y = batch
logits = self(x)
loss = F.cross_entropy(logits, y)
```

Y Lightning hace automáticamente:

* backward
* step
* zero_grad

Eso reduce mucho el código repetitivo.

---

## 3. `self.log(...)`

Muy importante porque enseña una forma profesional de registrar métricas.

Ejemplo:

```python
self.log("val_loss", loss, prog_bar=True, on_epoch=True)
```

Esto sirve para:

* ver la barra de progreso
* guardar resultados
* usar callbacks como early stopping.

---

## 4. `configure_optimizers`

Aquí podemos ver que Lightning no “oculta” del todo PyTorch.

Siguen definiendo:

* optimizador
* scheduler

pero de forma más estructurada.

---

## 5. `EarlyStopping`

Si la validación deja de mejorar:

```python
patience=3
```

se para el entrenamiento.

Esto ayuda a explicar:

* sobreajuste
* regularización práctica
* entrenamiento eficiente

---

## 6. `ModelCheckpoint`

Guarda el mejor modelo según `val_loss`.

Esto es muy útil para mostrar una práctica realista:

> no siempre queremos el último modelo, sino el mejor.

---

# Hemos visto

### PyTorch puro

Te enseña el mecanismo.

### Lightning

Te enseña a **estructurar proyectos reales**.

---

# Qué ventajas tiene
Tenemos:

* CNN
* train / val / test
* scheduler
* early stopping
* checkpoint
* logging
* GPU automática

con bastante menos código que en PyTorch puro.

---

# Actividad de modificación:

## Variante 1

Cambiar la arquitectura:

* más filtros
* dropout
* otra capa fully connected

## Variante 2

Cambiar el optimizador:

* Adam
* SGD
* RMSprop

## Variante 3

Cambiar el criterio de parada:

* monitorizar `val_acc` en lugar de `val_loss`

---

# Idea final


> Lightning no reemplaza a PyTorch.
> Lightning es una forma de usar PyTorch de manera más organizada, escalable y profesional.

---
