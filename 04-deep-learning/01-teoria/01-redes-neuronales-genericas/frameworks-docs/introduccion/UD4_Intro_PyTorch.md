# UD4 - Introduccion a PyTorch (guia rapida y practica)

## 1. Que es PyTorch y para que sirve

PyTorch es un framework de deep learning con enfoque imperativo y control
explicito del entrenamiento.

Ventajas principales:
- Mucho control sobre el `forward` y el bucle de entrenamiento.
- Muy usado en investigacion y desarrollo de modelos.
- API flexible para experimentar.

Flujo tipico:
1. Preparar datos (`Dataset`/`DataLoader`).
2. Definir red (`nn.Module`).
3. Definir perdida y optimizador.
4. Bucle de entrenamiento manual.
5. Evaluacion e inferencia.
 
 ---

 ## 1.1 Preparar datos: `Dataset` y `DataLoader`

En PyTorch la preparación de datos se organiza en dos piezas clave:

- **`Dataset`**: representa una colección de muestras y etiquetas. Implementa al menos dos métodos: `__len__()` (nº de muestras) y `__getitem__(idx)` (devuelve la muestra nº `idx`). Existen alternativas:
    - `TensorDataset`: útil cuando ya tienes tensores `X` e `y` listos.
    - Subclase personalizada de `torch.utils.data.Dataset`: permite cargar imágenes, aplicar transformaciones o leer datos bajo demanda desde disco.

- **`DataLoader`**: itera sobre un `Dataset` y produce batches. Parámetros relevantes:
    - `batch_size`: tamaño del lote.
    - `shuffle=True` para mezclar los datos en entrenamiento.
    - `num_workers`: nº de procesos para cargar datos en paralelo (aumenta rendimiento en CPU multicore).
    - `pin_memory=True` (cuando se usa GPU) para acelerar la transferencia a CUDA.
    - `collate_fn`: función para unir muestras en un batch (útil con entradas de tamaño variable).

Ejemplos prácticos:

1) Tensores ya preparados:

```python
from torch.utils.data import TensorDataset, DataLoader
train_ds = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
```

2) Dataset de imágenes con `torchvision` y `transforms` (ideal para augmentations):

```python
from torchvision import datasets, transforms

transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
])
train_ds = datasets.FashionMNIST(root='data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_ds, batch_size=64, shuffle=True, num_workers=4, pin_memory=True)
```

Recomendaciones prácticas:
- Usa `TensorDataset` para ejemplos pedagógicos y cuando ya tengas tensores en memoria.
- Para entrenamiento real con imágenes, prefiere `torchvision.datasets` + `transforms` y `num_workers>0`.
- Ajusta `pin_memory` cuando entrenes en GPU para mejor rendimiento.
- Implementa un `Dataset` personalizado si necesitas lógica de carga/labeling específica.
 
### `collate_fn` y casos avanzados

El `DataLoader` usa internamente una función llamada `collate_fn` para juntar las muestras individuales en un batch. En la mayoría de los casos la función por defecto (`default_collate`) es suficiente (apila tensores en un lote), pero hay situaciones donde conviene personalizarla:

- Entradas de longitudes variables (p. ej. secuencias) que requieren padding.
- Estructuras de datos complejas (diccionarios, tuplas anidadas) que necesitan transformación específica.
- Conversión/normalización adicional que prefieres aplicar justo al crear el batch en lugar de en `__getitem__`.

Ejemplo de uso sencillo:

```python
def my_collate(batch):
    # `batch` es una lista de tuplas (x, y)
    xs = torch.tensor([b[0] for b in batch], dtype=torch.float32)
    ys = torch.tensor([b[1] for b in batch], dtype=torch.long)
    return xs, ys

loader = DataLoader(dataset, batch_size=64, collate_fn=my_collate)
```

#### Ejemplo de `collate_fn` con padding (secuencias de longitud variable)

Cuando las entradas son secuencias de distinta longitud (p. ej. texto o series temporales) conviene aplicar padding en el `collate_fn` para obtener batches con la misma forma. Ejemplo:

```python
def pad_collate(batch):
    # batch: lista de tuplas (seq, label), seq es un array 1D de longitud variable
    xs = [torch.tensor(b[0], dtype=torch.float32) for b in batch]
    lengths = torch.tensor([len(x) for x in xs], dtype=torch.long)
    maxlen = int(lengths.max())
    padded = torch.zeros(len(xs), maxlen, dtype=torch.float32)
    for i, x in enumerate(xs):
        padded[i, : x.size(0)] = x
    ys = torch.tensor([b[1] for b in batch], dtype=torch.long)
    return padded, lengths, ys

# Usa: DataLoader(dataset, batch_size=32, collate_fn=pad_collate)
```

Si trabajas con imágenes o grandes datasets en disco recomendación práctica: combina un `Dataset` bien diseñado, `num_workers>0` y `pin_memory=True` cuando entrenes en GPU.
## 2. Estructura base en PyTorch

### 2.1 Definir modelo con `nn.Module`

```python
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_dim=784):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        return self.net(x)
```

### 2.2 Definir perdida y optimizador

```python
model = MLP()
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
```

### 2.3 Bucle minimo de entrenamiento

```python
model.train()
for xb, yb in train_loader:
    optimizer.zero_grad()
    logits = model(xb)
    loss = criterion(logits.squeeze(), yb.float())
    loss.backward()
    optimizer.step()
```

---

## 3. Tipos de capas mas usadas

### 3.1 Capas densas
- `nn.Linear`

### 3.2 Vision
- `nn.Conv2d`, `nn.MaxPool2d`, `nn.AdaptiveAvgPool2d`

### 3.3 Secuencias
- `nn.RNN`, `nn.LSTM`, `nn.GRU`

### 3.4 Regularizacion y normalizacion
- `nn.Dropout`
- `nn.BatchNorm1d` / `nn.BatchNorm2d`

---

## 4. Activaciones y salida

Activaciones frecuentes:
- `nn.ReLU()` en capas ocultas.
- `torch.sigmoid(...)` para salida binaria (si no usas logits directos).
- `softmax` para probabilidades multiclase en inferencia.

Reglas practicas:
- Binaria: salida logits + `BCEWithLogitsLoss`.
- Multiclase: logits + `CrossEntropyLoss`.
- Regresion: salida lineal + `MSELoss`/`L1Loss`.

---

## 5. "Tipos de neuronas" en practica

En PyTorch se trabaja por capas:
- Densas (`Linear`)
- Convolucionales (`Conv2d`)
- Recurrentes (`LSTM/GRU`)

La "neurona" individual es el calculo interno de esas capas.

---

## 6. Perdida, optimizador y metricas

### 6.1 Perdidas
- Binaria: `BCEWithLogitsLoss`
- Multiclase: `CrossEntropyLoss`
- Regresion: `MSELoss`, `L1Loss`

### 6.2 Optimizadores
- `Adam`
- `SGD` (con o sin momentum)
- `RMSprop`

### 6.3 Metricas
No vienen todas "listas" como en Keras; suelen calcularse manualmente o con
bibliotecas auxiliares.

---

## 7. Regularizacion y control de sobreajuste

- `Dropout`
- Weight decay (L2) en el optimizador
- Early stopping (implementado manualmente)
- Data augmentation

Ejemplo weight decay:

```python
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
```

---

## 8. Normalizacion

### 8.1 En entrada
- Escalar datos (por ejemplo imagenes /255.0)
- Estandarizar cuando procede

### 8.2 En red
- `BatchNorm` para estabilizar entrenamiento

---

## 9. Batches, epochs y modos del modelo

- `batch_size`: muestras por lote
- `epoch`: pasada completa por el dataset

Muy importante:
- `model.train()` durante entrenamiento
- `model.eval()` durante validacion/inferencia
- `with torch.no_grad()` para no calcular gradientes en evaluacion

---

## 10. Entrenamiento en CPU y GPU

Comprobacion basica:

```python
import torch
print(torch.cuda.is_available())
```

Mover a dispositivo:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

---

## 11. Errores frecuentes en PyTorch

- No mover tensores y modelo al mismo dispositivo.
- Olvidar `optimizer.zero_grad()`.
- Mezclar salida/funcion de perdida incorrecta (sigmoid + BCEWithLogits, etc.).
- No usar `model.eval()` en validacion.
- No usar `torch.no_grad()` al evaluar.

---

## 12. Plantilla minima recomendada

```python
model = MLP().to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(epochs):
    model.train()
    for xb, yb in train_loader:
        xb, yb = xb.to(device), yb.to(device)
        optimizer.zero_grad()
        logits = model(xb)
        loss = criterion(logits.squeeze(), yb.float())
        loss.backward()
        optimizer.step()
```

---

## 13. Resumen rapido

- PyTorch muestra con claridad como aprende una red:
  `forward -> loss -> backward -> step`.
- Si entiendes este ciclo, entiendes la base de entrenamiento en deep learning.
- Keras simplifica; PyTorch explicita.
