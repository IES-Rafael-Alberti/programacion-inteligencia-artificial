---
title: "Deep Learning con PyTorch"
output: 
  pdf_document:
    toc: true
    toc_depth: 3
  engine: lualatex
   
---

# Deep Learning con PyTorch

PyTorch es un framework de deep learning desarrollado por Meta (Facebook), conocido por su flexibilidad y facilidad de depuración. Utiliza **grafos computacionales dinámicos**, lo que permite modificar la red en tiempo de ejecución.

## 1. Introducción a PyTorch

### 1.1 ¿Por qué PyTorch?

- **Grafo dinámico**: fácil depuración con breakpoints
- **Pythonic**: se integra naturalmente con Python
- **Popular en investigación**: dominan el ámbito académico
- **torchscript**: optimización para producción

### 1.2 Instalación

```bash
# CPU
pip install torch torchvision torchaudio

# Con CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

## 2. Tensores

### 2.1 Creación de Tensores

```python
import torch
import numpy as np

# Desde Python list
x = torch.tensor([1, 2, 3])

# Desde NumPy
np_array = np.array([1, 2, 3])
x = torch.from_numpy(np_array)

# Tensores especiales
x = torch.zeros(3, 3)
x = torch.ones(2, 4)
x = torch.full((3, 3), 7.0)
x = torch.eye(3)
x = torch.arange(0, 10, 2)  # 0, 2, 4, 6, 8
x = torch.linspace(0, 1, 10)

# Aleatorios
x = torch.rand(3, 3)        # Uniforme [0, 1)
x = torch.randn(3, 3)       # Normal(0, 1)
x = torch.randint(0, 10, (3, 3))  # Enteros
```

### 2.2 Operaciones con Tensores

```python
# Shape
x.shape
x.size()

# Indexación (como NumPy)
x[0, :]
x[:, 1:3]

# Operaciones matemáticas
y = x + 2
z = torch.matmul(x, y)
z = x @ y.T

# Cambiar forma
x.view(9, 1)
x.reshape(3, 3)
x.flatten()
x.unsqueeze(0)  # Añadir dimensión

# Mover a GPU/CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
x = x.to(device)
```

---

## 3. Autograd (Cálculo de Gradientes)

### 3.1 Gradientes Automáticos

```python
# Crear tensor que requiere gradiente
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x ** 2
z = y.mean()

# Calcular gradientes
z.backward()

# Ver gradientes
print(x.grad)  # d(z)/d(x) = [2/3, 4/3, 2]

# Desactivar gradiente (inferencia)
with torch.no_grad():
    result = x * 2

# Freeze pesos
for param in model.parameters():
    param.requires_grad = False
```

---

## 4. Redes Neuronales con nn.Module

### 4.1 Definición Básica

```python
import torch.nn as nn
import torch.nn.functional as F

class RedNeuronal(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RedNeuronal, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.dropout = nn.Dropout(0.3)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Instanciar modelo
model = RedNeuronal(784, 256, 10)
print(model)
```

### 4.2 Capas Comunes

```python
# Densa (Linear)
nn.Linear(in_features, out_features)

# Dropout
nn.Dropout(p=0.3)

# Batch Normalization
nn.BatchNorm1d(num_features)
nn.BatchNorm2d(num_features)

# Activaciones
F.relu(x)
F.sigmoid(x)
F.tanh(x)
F.softmax(x, dim=1)
F.leaky_relu(x, negative_slope=0.01)
```

### 4.3 Redes Convolucionales (CNN)

```python
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # Conv block 1
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        
        # Conv block 2
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        
        # Pooling
        self.pool = nn.MaxPool2d(2, 2)
        
        # Classifier
        self.fc1 = nn.Linear(64 * 8 * 8, 256)
        self.fc2 = nn.Linear(256, 10)
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x):
        # Conv block 1
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        # Conv block 2
        x = self.pool(F.relu(self.bn2(self.conv2(x))))
        
        # Flatten
        x = x.view(x.size(0), -1)
        
        # Classifier
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
```

### 4.4 Redes Recurrentes (RNN/LSTM/GRU)

```python
class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMClassifier, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.3
        )
        
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        # x shape: (batch, seq_len, input_size)
        lstm_out, (h_n, c_n) = self.lstm(x)
        # Usar la última timestep
        out = self.fc(lstm_out[:, -1, :])
        return out

# GRU
self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
```

---

## 5. Entrenamiento

### 5.1 Bucle de Entrenamiento

```python
import torch.optim as optim

# Hiperparámetros
learning_rate = 0.001
num_epochs = 30
batch_size = 32

# Modelo, pérdida, optimizador
model = RedNeuronal(784, 256, 10)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# DataLoader
from torch.utils.data import DataLoader, TensorDataset

train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Training loop
model.train()
for epoch in range(num_epochs):
    total_loss = 0
    for batch_x, batch_y in train_loader:
        # Forward pass
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    avg_loss = total_loss / len(train_loader)
    if (epoch + 1) % 5 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}')
```

### 5.2 Validación

```python
model.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for x, y in val_loader:
        outputs = model(x)
        _, predicted = torch.max(outputs.data, 1)
        total += y.size(0)
        correct += (predicted == y).sum().item()

accuracy = 100 * correct / total
print(f'Accuracy: {accuracy:.2f}%')
```

### 5.3 Guardar/Cargar Modelo

```python
# Guardar modelo completo
torch.save(model, 'modelo.pth')

# Guardar solo pesos (recomendado)
torch.save(model.state_dict(), 'modelo_pesos.pth')

# Cargar
model = RedNeuronal(784, 256, 10)
model.load_state_dict(torch.load('modelo_pesos.pth'))
```

---

## 6. Regularización

### 6.1 Dropout

```python
self.dropout = nn.Dropout(p=0.3)

# En forward
x = self.dropout(x)
```

### 6.2 Weight Decay (L2)

```python
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=0.01)
```

### 6.3 L1 Regularization (manual)

```python
def train_step(model, X, y):
    optimizer.zero_grad()
    output = model(X)
    loss = criterion(output, y)
    
    # L1 penalty
    l1_loss = 0
    for param in model.parameters():
        l1_loss += torch.sum(torch.abs(param))
    
    total_loss = loss + 0.001 * l1_loss
    total_loss.backward()
    optimizer.step()
```

---

## 7. Optimizadores

### 7.1 Optimizadores Disponibles

```python
# SGD con momentum
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Adam
optimizer = optim.Adam(model.parameters(), lr=0.001)

# AdamW (Adam con weight decay correcto)
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)

# RMSprop
optimizer = optim.RMSprop(model.parameters(), lr=0.01)

# Adagrad
optimizer = optim.Adagrad(model.parameters(), lr=0.01)
```

### 7.2 Learning Rate Scheduler

```python
# Reduce LR when loss plateaus
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', factor=0.5, patience=3, verbose=True
)

# Step LR
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

# Cosine annealing
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)

# Use en el training loop
for epoch in range(num_epochs):
    train()
    val_loss = validate()
    scheduler.step(val_loss)
```

### 7.3 Gradient Clipping

```python
# Clip por valor
torch.nn.utils.clip_grad_value_(model.parameters(), clip_value=1.0)

# Clip por norma
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

---

## 8. Early Stopping

```python
class EarlyStopping:
    def __init__(self, patience=10, min_delta=0):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_loss = float('inf')
        self.early_stop = False
    
    def __call__(self, val_loss):
        if val_loss < self.best_loss - self.min_delta:
            self.best_loss = val_loss
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        return self.early_stop

# Uso
early_stopping = EarlyStopping(patience=10)
for epoch in range(num_epochs):
    train()
    val_loss = validate()
    if early_stopping(val_loss):
        print("Early stopping!")
        break
```

---

## 9. Data Augmentation

```python
from torchvision import transforms

train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                        std=[0.229, 0.224, 0.225])
])

test_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                        std=[0.229, 0.224, 0.225])
])
```

### Usar con DataLoader

```python
from torchvision.datasets import CIFAR10

train_dataset = CIFAR10(root='./data', train=True, 
                       transform=train_transform, download=True)
test_dataset = CIFAR10(root='./data', train=False, 
                      transform=test_transform, download=True)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
```

---

## 10. Transfer Learning

### 10.1 Modelo Preentrenado

```python
import torchvision.models as models

# Cargar modelo preentrenado
model = models.resnet50(weights='IMAGENET1K_V1')

# Congelar capas base
for param in model.parameters():
    param.requires_grad = False

# Reemplazar capa final
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)  # 10 clases

# Fine-tuning: descongelar últimas capas
for param in model.layer4.parameters():
    param.requires_grad = True
```

### 10.2 Feature Extraction

```python
# Usar modelo como extractor de features
model = models.vgg16(weights='IMAGENET1K_V1')
model.classifier = nn.Identity()  # Quitar classifier

# Extraer features
features = model(image)  # Shape: (1, 4096)
```

---

## 11. Distributed Training

### 11.1 DataParallel (Multi-GPU)

```python
if torch.cuda.device_count() > 1:
    model = nn.DataParallel(model)

model = model.to(device)
```

### 11.2 DDP (Distributed Data Parallel)

```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
import torch.multiprocessing as mp

# Inicializar proceso
dist.init_process_group(backend='nccl')

# Envolver modelo
model = DDP(model, device_ids=[local_rank])

# Training loop con sincronización
```

### 11.3 Distributed Training Completo

```python
import os
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data import DistributedSampler
from torch.utils.data import DataLoader
import torch.multiprocessing as mp

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    dist.init_process_group("nccl", rank=rank, world_size=world_size)
    torch.cuda.set_device(rank)

def cleanup():
    dist.destroy_process_group()

def train_ddp(rank, world_size):
    setup(rank, world_size)
    
    # Modelo con GPU
    model = MyModel().to(rank)
    model = DDP(model, device_ids=[rank])
    
    # Dataset y DataLoader con sampler
    train_dataset = MyDataset()
    train_sampler = DistributedSampler(
        train_dataset,
        num_replicas=world_size,
        rank=rank,
        shuffle=True
    )
    train_loader = DataLoader(
        train_dataset,
        batch_size=32,
        sampler=train_sampler
    )
    
    # Optimizador
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    # Training loop
    for epoch in range(10):
        train_loader.sampler.set_epoch(epoch)
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(rank), target.to(rank)
            
            optimizer.zero_grad()
            output = model(data)
            loss = F.cross_entropy(output, target)
            loss.backward()
            optimizer.step()
            
            if rank == 0 and batch_idx % 10 == 0:
                print(f"Epoch {epoch}, Batch {batch_idx}, Loss {loss.item()}")
    
    cleanup()

# Lanzar en múltiples GPUs
world_size = torch.cuda.device_count()
mp.spawn(train_ddp, args=(world_size,), nprocs=world_size, join=True)
```

### 11.4 FSDP (Fully Sharded Data Parallel)

```python
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp import ShardingStrategy
from torch.distributed.fsdp import MixedPrecision
from torch.distributed.fsdp.wrap import transformer_auto_wrap_policy

# Wrapping automático por tipo de capa
model = FSDP(
    model,
    sharding_strategy=ShardingStrategy.FULL_SHARD,
    auto_wrap_policy=transformer_auto_wrap_policy,
    device_id=torch.cuda.current_device(),
    mixed_precision=MixedPrecision(
        param_dtype=torch.float16,
        reduce_dtype=torch.float16,
        buffer_dtype=torch.float16
    )
)

# O con CPU offload
from torch.distributed.fsdp import CPUOffload
model = FSDP(model, cpu_offload=CPUOffload(offload_params=True))
```

### 11.5 Multi-GPU con DataParallel (más simple)

```python
from torch.nn import DataParallel

# Múltiples GPUs (más simple que DDP)
model = DataParallel(model, device_ids=[0, 1, 2, 3])

# Training normal
output = model(input)
```

### 11.6 Distributed con PyTorch Lightning

```python
import pytorch_lightning as pl

class LitModel(pl.LightningModule):
    def training_step(self, batch, batch_idx):
        return self(batch)
    
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)

# Trainer con multi-GPU automático
trainer = pl.Trainer(
    accelerator='gpu',
    devices=4,
    strategy='ddp'  # o 'fsdp'
)
trainer.fit(model, datamodule)
```

---

## 12. TorchScript y Exportación

### 12.1 TorchScript

```python
# Tracing
example_input = torch.randn(1, 784)
traced_model = torch.jit.trace(model, example_input)
traced_model.save('model_traced.pt')

# Scripting
scripted_model = torch.jit.script(model)
scripted_model.save('model_scripted.pt')
```

### 12.2 TorchScript para Producción

```python
# 1. Guardar modelo entrenado
model.eval()
model.load_state_dict(torch.load('model_weights.pth'))

# 2. Tracing (para modelos sin control flow)
example_input = torch.randn(1, 3, 224, 224)
traced = torch.jit.trace(model, example_input)
traced.save('model_production.pt')

# 3. Scripting (para modelos con control flow)
scripted = torch.jit.script(model)
scripted.save('model_scripted.pt')

# 4. Cargar en producción
loaded = torch.jit.load('model_production.pt')
output = loaded(input_tensor)
```

### 12.3 Optimización para Producción

```python
# 1. Script + Optimize for mobile
model_scripted = torch.jit.script(model)
model_optimized = torch.jit.optimize_for_inference(torch.jit.freeze(model_scripted))
model_optimized.save('model_optimized.pt')

# 2. Quantization (reducir tamaño 4x)
model_int8 = torch.quantization.quantize_dynamic(
    model, {nn.Linear, nn.Conv2d}, dtype=torch.qint8
)

# 3. TorchServe compatible
torch.jit.trace(model, example_input).save('model.mar')
```

### 12.4 ONNX

```python
# Exportar a ONNX
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, 'model.onnx',
                 input_names=['input'],
                 output_names=['output'],
                 dynamic_axes={'input': {0: 'batch_size'}})

# Verificar modelo ONNX
import onnx
onnx_model = onnx.load('model.onnx')
onnx.checker.check_model(onnx_model)

# Usar con onnxruntime
import onnxruntime as ort
session = ort.InferenceSession('model.onnx')
output = session.run(None, {'input': numpy_input})
```

### 12.5 Deployment Options

| Método | Uso | Ventajas |
|--------|-----|----------|
| TorchScript | C++ / mobile | Rápido, sin Python |
| ONNX | Multi-plataforma | Universal |
| TensorRT | NVIDIA GPUs | Optimizado |
| TorchServe | Servidor | Escalable |
| Quantization | Mobile/Edge | Pequeño (4x) |

---

## 13. Debugging

### 13.1 Ver estructura del modelo

```python
print(model)
print(model.named_parameters())
```

### 13.2 Ver gradientes

```python
for name, param in model.named_parameters():
    if param.grad is not None:
        print(f"{name}: grad norm = {param.grad.norm().item():.4f}")
```

### 13.3 Problemas comunes y soluciones

#### a) NaN en loss
```python
# Posibles causas y soluciones:
# 1. Learning rate muy alto
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)  # Reducir

# 2. Overflow en operaciones
x = torch.clamp(x, min=-1e6, max=1e6)  # Limitar valores

# 3. División por cero
eps = 1e-8
loss = criterion(output + eps, target)

# 4. Log de cero
loss = torch.log(x + eps)
```

#### b) GPU out of memory
```python
# 1. Reducir batch size
batch_size = 16  # en lugar de 128

# 2. Limpiar caché
torch.cuda.empty_cache()
del variables_no_usadas
import gc
gc.collect()

# 3. Gradient checkpointing
from torch.utils.checkpoint import checkpoint_sequential

# 4. Mixed precision
scaler = torch.cuda.amp.GradScaler()
with torch.cuda.amp.autocast():
    output = model(x)
```

#### c) Shape mismatches
```python
# Añadir prints de debug
print(f"Input shape: {x.shape}")
print(f"Expected: {expected_shape}")

# Usar asserts
assert x.shape == (batch_size, 10), f"Got {x.shape}"

# Investigar con torchinfo
from torchinfo import summary
summary(model, input_size=(batch_size, 10))
```

#### d) Modelo no aprende
```python
# 1. Verificar gradientes fluyen
for param in model.parameters():
    if param.grad is not None:
        print(f"Grad exists: {param.requires_grad}")

# 2. Verificar datos
print(f"X mean: {X.mean()}, std: {X.std()}")
print(f"y unique: {torch.unique(y)}")

# 3. Verificar loss
criterion = nn.CrossEntropyLoss()  # Para clasificación
# NO: criterion = nn.MSELoss() para clasificación

# 4. Verificar modo train/eval
model.train()  # Para entrenamiento
model.eval()   # Para evaluación
```

### 13.4 Herramientas de debugging

```python
# 1. torch.autograd.set_detect_anomaly
with torch.autograd.detect_anomaly():
    loss.backward()

# 2. debugger visual (Visual Studio Code)
import pdb; pdb.set_trace()

# 3. PyTorch Debuggger (torchdbg)
# pip install torchdbg

# 4.Profiler para bottlenecks
with torch.profiler.profile(
    activities=[torch.profiler.ProfilerActivity.CPU,
                torch.profiler.ProfilerActivity.CUDA],
    record_shapes=True
) as prof:
    output = model(x)
print(prof.key_averages().table(sort_by="cuda_time_total"))
```

### 13.5 Checklist de debugging

| Síntoma | Causa probable | Solución |
|---------|---------------|----------|
| Loss = NaN | LR muy alto | Reducir LR, añadir epsilon |
| Loss no baja | LR muy bajo / bug | Aumentar LR, revisar loss function |
| Accuracy = 50% | Modelo no aprende | Revisar arquitectura, datos |
| OOM errors | Batch muy grande | Reducir batch_size |
| Gradientes=0 | Frozen layers | Verificar requires_grad |
| GPU no usada | Device mismatch | .to(device) en tensores y modelo |

---

## 14. Métricas Personalizadas

```python
def calculate_accuracy(outputs, targets):
    _, predicted = torch.max(outputs, 1)
    correct = (predicted == targets).sum().item()
    total = targets.size(0)
    return 100 * correct / total

def calculate_f1(outputs, targets):
    from sklearn.metrics import f1_score
    _, predicted = torch.max(outputs, 1)
    return f1_score(targets.numpy(), predicted.numpy(), average='macro')
```

---

## 15. Best Practices

1. **Usar `.to(device)`** para mover tensores a GPU
2. **Usar `torch.no_grad()`** en inferencia
3. **Usar `model.train()` / `model.eval()`** para cambiar modo
4. **Usar DataLoader** con `shuffle=True` en entrenamiento
5. **Normalizar inputs** (media 0, std 1)
6. **Guardar checkpoints** durante entrenamiento largo
7. **Usar Mixed Precision** (`torch.cuda.amp`) para acelerar
8. **Fijar semillas** para reproducibilidad

```python
# Fijar semillas
torch.manual_seed(42)
torch.cuda.manual_seed_all(42)
```

---

## Apéndice A: Carga de Datos en PyTorch (torch.utils.data)

PyTorch requiere un proceso más manual que Keras para cargar datos. Aquí te explicamos todos los pasos.

### A.1 Comparativa: Keras vs PyTorch

```python
# Keras: Simple y directo
model.fit(X_train, y_train, epochs=10, batch_size=32)

# PyTorch: Más pasos necesarios
# 1. Crear Dataset
train_dataset = TensorDataset(X_train, y_train)
# 2. Crear DataLoader
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
# 3. Bucle manual
for epoch in range(10):
    for batch_x, batch_y in train_loader:
        # Training step
        ...
```

### A.2 La clase Dataset

```python
from torch.utils.data import Dataset, DataLoader

# Opción 1: Dataset desde tensores/arrays
from torch.utils.data import TensorDataset
train_dataset = TensorDataset(
    torch.tensor(X_train, dtype=torch.float32),
    torch.tensor(y_train, dtype=torch.long)
)

# Opción 2: Dataset personalizado
class MiDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

train_dataset = MiDataset(X_train, y_train)
```

### A.3 La clase DataLoader

```python
from torch.utils.data import DataLoader

train_loader = DataLoader(
    dataset=train_dataset,
    batch_size=32,        # Samples por batch
    shuffle=True,        # Mezclar datos cada época
    num_workers=4,       # Procesos paralelos para cargar datos
    pin_memory=True,      # Faster GPU transfer
    drop_last=False      # Drop último batch si es incompleto
)

# Iterar
for batch_X, batch_y in train_loader:
    # batch_X shape: (32, features)
    # batch_y shape: (32,)
    ...
```

### A.4 Transformaciones (para imágenes)

```python
from torchvision import transforms

# Transformaciones de entrenamiento
train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),  # Convierte PIL a tensor [0,1]
    transforms.Normalize(mean=[0.5], std=[0.5])  # Normaliza
])

# Transformaciones de test
test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

# Aplicar a Dataset
train_dataset = datasets.CIFAR10(
    root='./data',
    train=True,
    download=True,
    transform=train_transform
)
```

### A.5 Datasets Predefinidos

```python
from torchvision import datasets

# MNIST
mnist_train = datasets.MNIST(root='./data', train=True, download=True, 
                             transform=transforms.ToTensor())
mnist_test = datasets.MNIST(root='./data', train=False, download=True,
                           transform=transforms.ToTensor())

# CIFAR-10/100
cifar10 = datasets.CIFAR10(root='./data', train=True, download=True)
cifar100 = datasets.CIFAR100(root='./data', train=True, download=True)

# Fashion-MNIST
fashion = datasets.FashionMNIST(root='./data', train=True, download=True)

# ImageFolder (tus propias imágenes)
# Estructura: root/class1/img1.jpg, root/class2/img2.jpg...
train_dataset = datasets.ImageFolder(
    root='./data/train',
    transform=train_transform
)
```

### A.6 train_loader y val_loader

```python
from torch.utils.data import random_split

# Dividir en train/val
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# Training loop con validación
model.train()
for batch_x, batch_y in train_loader:
    # Training step
    ...

model.eval()
with torch.no_grad():
    for batch_x, batch_y in val_loader:
        # Validation step
        ...
```

### A.7 DataLoader para NLP (Texto)

```python
from torch.utils.data import Dataset, DataLoader

class TextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts[idx]
        encoding = self.tokenizer(
            text,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'label': torch.tensor(self.labels[idx], dtype=torch.long)
        }

# Uso
dataset = TextDataset(texts, labels, tokenizer, max_len=128)
loader = DataLoader(dataset, batch_size=16, shuffle=True)
```

### A.8 Consejos de Rendimiento

```python
# 1. Usar num_workers > 0 para datasets grandes
loader = DataLoader(dataset, batch_size=32, num_workers=4)

# 2. pin_memory=True si usas GPU
loader = DataLoader(dataset, batch_size=32, pin_memory=True)

# 3. prefetch_factor para precargar batches
loader = DataLoader(dataset, batch_size=32, num_workers=4, 
                   prefetch_factor=2)

# 4. persistent_workers evita recrear procesos
loader = DataLoader(dataset, batch_size=32, num_workers=4,
                   persistent_workers=True)
```

### A.9 Ejemplo Completo: MNIST

```python
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 1. Transformaciones
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 2. Dataset
train_data = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('./data', train=False, download=True, transform=transform)

# 3. DataLoader
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)

# 4. Modelo simple
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)

# 5. Entrenamiento
optimizer = torch.optim.Adam(model.parameters())
criterion = nn.CrossEntropyLoss()

for epoch in range(5):
    model.train()
    for batch_x, batch_y in train_loader:
        optimizer.zero_grad()
        output = model(batch_x)
        loss = criterion(output, batch_y)
        loss.backward()
        optimizer.step()
    
    # Validación
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_x, batch_y in test_loader:
            output = model(batch_x)
            _, predicted = torch.max(output, 1)
            total += batch_y.size(0)
            correct += (predicted == batch_y).sum().item()
    print(f'Accuracy: {100*correct/total:.2f}%')
```

---

## 16. Recursos

- [PyTorch Official Docs](https://pytorch.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [PyTorch Examples](https://github.com/pytorch/examples)
