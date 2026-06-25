# Guía Técnica: Estructura y Gestión de Proyectos Python para Machine Learning

## 1. Entorno de Desarrollo

### 1.1 Gestor de Paquetes: Conda/Mamba

Para proyectos de Deep Learning con GPU, **Conda** es la opción recomendada:

```bash
# Instalar Miniconda (más ligero que Anaconda)
# https://docs.conda.io/en/latest/miniconda.html

# Opcional: Instalar Mamba para mayor velocidad
conda install -n base -c conda-forge mamba
```

**Crear entorno:**

```bash
# Con Conda
conda create -n ml_project python=3.11
conda activate ml_project

# Con Mamba (más rápido)
mamba create -n ml_project python=3.11
mamba activate ml_project
```

**Instalar PyTorch con CUDA:**

```bash
# GPU NVIDIA
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

# CPU only (desarrollo sin GPU)
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

**Instalar TensorFlow/Keras con CUDA:**

```bash
# GPU NVIDIA (TensorFlow instala Keras automáticamente)
conda install tensorflow-gpu=2.15 -c conda-forge

# O instalar solo Keras (usando el backend de TensorFlow)
conda install keras=3 -c conda-forge

# CPU only
conda install tensorflow=2.15 cpuonly -c conda-forge
```

**Instalar individualmente (PyPI):**

```bash
# PyTorch con CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# TensorFlow/Keras
pip install tensorflow

# Keras 3单独
pip install keras
```

### 1.2 Entorno Base (environment.yml)

```yaml
name: ml_project
channels:
  - pytorch
  - nvidia
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pip
  - pip:
      - fastapi
      - uvicorn
      - scikit-learn
      - pandas
      - numpy
      - matplotlib
      - seaborn
      - jupyter
      - ipykernel
      - python-dotenv
      - tensorflow          # Keras con TensorFlow
      - keras               # Keras 3 (o usar tensorflow.keras)
```

```bash
# Crear entorno desde archivo
conda env create -f environment.yml

# Exportar entorno
conda env export > environment.yml

# Actualizar entorno
conda env update -f environment.yml
```

---

## 2. Estructura del Proyecto

```
mi_proyecto_ml/
├── .env                        # Variables de entorno (NO incluir en git)
├── .gitignore                  # Archivos/carpetas ignorados
├── README.md                   # Documentación del proyecto
├── requirements.txt            # Dependencias pip (backup)
├── environment.yml             # Entorno Conda
├── pyproject.toml              # Configuración del proyecto (opcional)
│
├── config/                     # CONFIGURACIÓN
│   ├── __init__.py
│   ├── settings.py             # Configuración principal
│   ├── model_config.yaml       # Parámetros del modelo
│   └── api_config.yaml         # Configuración de la API
│
├── data/                       # DATOS (raw y procesados)
│   ├── raw/                    # Datos originales (no modificar)
│   │   ├── train.csv
│   │   └── test.csv
│   ├── processed/              # Datos limpios/preparados
│   │   ├── train_processed.csv
│   │   └── test_processed.csv
│   └── external/               # Datos externos/descargados
│
├── notebooks/                  # EXPERIMENTACIÓN (Jupyter)
│   ├── 01_exploracion.ipynb    # EDA inicial
│   ├── 02_preparacion.ipynb    # Limpieza y transformación
│   ├── 03_entrenamiento.ipynb  # Entrenamiento de modelos
│   └── 04_evaluacion.ipynb     # Métricas y resultados
│
├── src/                        # CÓDIGO FUENTE (módulos)
│   ├── __init__.py
│   ├── models/                 # Definición de modelos
│   │   ├── __init__.py
│   │   ├── red_neuronal.py      # PyTorch
│   │   ├── red_neuronal_keras.py  # Keras/TensorFlow
│   │   └── transformer.py
│   ├── data/                   # Pipeline de datos
│   │   ├── __init__.py
│   │   ├── dataset.py          # PyTorch Dataset
│   │   └── keras_dataset.py    # Keras Dataset
│   ├── training/               # Entrenamiento
│   │   ├── __init__.py
│   │   ├── trainer.py          # PyTorch Trainer
│   │   ├── trainer_keras.py    # Keras Trainer
│   │   └── callbacks.py
│   ├── evaluation/             # Evaluación
│   │   ├── __init__.py
│   │   └── metrics.py
│   └── utils/                  # Utilidades
│       ├── __init__.py
│       └── helpers.py
│
├── api/                        # DESPLIEGUE (FastAPI)
│   ├── __init__.py
│   ├── main.py                 # Aplicación FastAPI
│   ├── routes/
│   │   ├── __init__.py
│   │   └── predictions.py
│   ├── models/                 # Modelos cargados para inferencia
│   │   └── __init__.py
│   └── schemas/
│       ├── __init__.py
│       └── request_response.py
│
├── scripts/                    # SCRIPTS AUXILIARES
│   ├── train_model.py          # Entrenamiento desde terminal
│   ├── evaluate_model.py       # Evaluación
│   ├── export_model.py         # Exportar modelo
│   └── download_data.py       # Descargar datasets
│
├── models/                     # MODELOS GUARDADOS
│   ├── checkpoints/            # Checkpoints durante entrenamiento
│   │   ├── best_model.pt       # PyTorch
│   │   └── best_model.keras   # Keras
│   ├── final/                  # Modelos finales
│   │   ├── best_model.pt       # PyTorch
│   │   └── best_model.keras   # Keras
│   └── export/                 # Modelos exportados (ONNX, etc.)
│
├── tests/                      # TESTS UNITARIOS
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_data.py
│   └── test_api.py
│
├── logs/                       # LOGS Y EXPERIMENTOS
│   ├── training.log
│   └── mlruns/                 # MLflow (si se usa)
│
└── docker/                     # DOCKER
    ├── Dockerfile
    ├── Dockerfile.api
    └── docker-compose.yml
```

---

## 3. Gestión de Datos

### 3.1 Organización

| Carpeta | Propósito | ¿En Git? |
|---------|-----------|----------|
| `data/raw` | Datos originales, sin modificar | No |
| `data/processed` | Datos limpiados/preparados | No |
| `data/external` | Datos externos descargados | No |
| `models/*` | Modelos entrenados | No |
| `logs/*` | Logs y experimentos | No |

### 3.2 .gitignore Recomendado

```
# Datos y modelos
data/
models/
*.pt
*.pth
*.h5
*.keras       # Keras 3
*.pkl
*.joblib
*.onnx
saved_model/  # TensorFlow SavedModel
```

---

## 4. Configuración

### 4.1 Estructura de Configuración

```python
# config/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar .env
load_dotenv()

# Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
CONFIG_DIR = BASE_DIR / "config"

# Configuración general
class Settings:
    # Datos
    DATA_RAW_DIR = DATA_DIR / "raw"
    DATA_PROCESSED_DIR = DATA_DIR / "processed"
    
    # Modelos
    MODEL_CHECKPOINT_DIR = MODELS_DIR / "checkpoints"
    MODEL_FINAL_DIR = MODELS_DIR / "final"
    
    # API
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    
    # Training
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", "32"))
    EPOCHS = int(os.getenv("EPOCHS", "100"))
    LEARNING_RATE = float(os.getenv("LEARNING_RATE", "0.001"))
    
    # Dispositivo
    DEVICE = "cuda"  # "cuda" o "cpu"

settings = Settings()
```

### 4.2 Archivo .env

```
# .env (NO incluir en git)
API_HOST=0.0.0.0
API_PORT=8000

# Training
BATCH_SIZE=32
EPOCHS=100
LEARNING_RATE=0.001

# Rutas (opcional)
MODEL_PATH=models/final/best_model.pt
DATA_PATH=data/processed/train.csv

# Secrets
API_KEY=REPLACE_ME
```

---

## 5. Notebooks para Experimentación

### 5.1 Configuración de Jupyter en el Entorno Conda

```bash
# Instalar kernel de Jupyter para el entorno
conda activate ml_project
python -m ipykernel install --user --name=ml_project --display-name="Python (ML Project)"

# Instalar extensiones útiles
pip install jupyterlab-nested-Collapse
```

### 5.2 Flujo de Trabajo

1. **01_exploracion.ipynb**: Análisis exploratorio de datos (EDA)
   - Estadísticas descriptivas
   - Visualizaciones
   - Detección de outliers y valores faltantes

2. **02_preparacion.ipynb**: Preprocesamiento
   - Limpieza de datos
   - Transformaciones
   - Feature engineering

3. **03_entrenamiento.ipynb**: Entrenamiento
   - Definición del modelo
   - Bucle de entrenamiento
   - Guardar checkpoints

4. **04_evaluacion.ipynb**: Evaluación
   - Métricas en test
   - Matrices de confusión
   - Comparación de modelos

### 5.3 Integración con Código Fuente

```python
# En notebooks, agregar al path
import sys
sys.path.append("..")

from src.models.red_neuronal import MiModelo
from src.data.dataset import MiDataset
from config import settings
```

---

## 6. Módulos del Programa

### 6.1 Estructura de un Módulo

```python
# src/models/__init__.py
from .red_neuronal import RedNeuronal
from .transformer import Transformer

__all__ = ["RedNeuronal", "Transformer"]
```

```python
# src/models/red_neuronal.py
import torch
import torch.nn as nn

class RedNeuronal(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size)
        )
    
    def forward(self, x):
        return self.layers(x)
```

### 6.2 Modelo con Keras 3 (TensorFlow Backend)

```python
# src/models/red_neuronal_keras.py
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class RedNeuronalKeras(keras.Model):
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        super().__init__()
        self.dense1 = layers.Dense(hidden_size, activation="relu", input_shape=(input_size,))
        self.dense2 = layers.Dense(hidden_size, activation="relu")
        self.output_layer = layers.Dense(output_size, activation="softmax")
    
    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        return self.output_layer(x)

# Alternative: Modelo secuencial más simple
def create_model(input_size: int, hidden_size: int, output_size: int) -> keras.Model:
    model = keras.Sequential([
        layers.Dense(hidden_size, activation="relu", input_shape=(input_size,)),
        layers.Dense(hidden_size, activation="relu"),
        layers.Dense(output_size, activation="softmax")
    ])
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model
```

**Keras con GPU:**

```python
# Verificar GPU
gpus = tf.config.list_physical_devices("GPU")
print(f"GPUs disponibles: {gpus}")

# Si hay GPU, configurar memoria dinámica
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
```

### 6.2 Pipeline de Datos

```python
# src/data/dataset.py
import torch
from torch.utils.data import Dataset

class MiDataset(Dataset):
    def __init__(self, data_path: str, transform=None):
        self.data = ...  # Cargar datos
        self.transform = transform
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        sample = self.data[idx]
        if self.transform:
            sample = self.transform(sample)
        return sample
```

### 6.3 Pipeline de Datos con Keras

```python
# src/data/keras_dataset.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import Sequence

class KerasDataset(Sequence):
    def __init__(self, data: np.ndarray, labels: np.ndarray, batch_size: int = 32, shuffle: bool = True):
        self.data = data
        self.labels = labels
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.indices = np.arange(len(self.data))
        self.on_epoch_end()
    
    def __len__(self):
        return int(np.ceil(len(self.data) / self.batch_size))
    
    def __getitem__(self, idx):
        batch_indices = self.indices[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_data = self.data[batch_indices]
        batch_labels = self.labels[batch_indices]
        return batch_data, batch_labels
    
    def on_epoch_end(self):
        if self.shuffle:
            np.random.shuffle(self.indices)

# Alternativa simple con tf.data.Dataset
def create_tf_dataset(data: np.ndarray, labels: np.ndarray, batch_size: int = 32, shuffle: bool = True):
    dataset = tf.data.Dataset.from_tensor_slices((data, labels))
    if shuffle:
        dataset = dataset.shuffle(buffer_size=len(data))
    return dataset.batch(batch_size).prefetch(tf.data.AUTOTUNE)
```

---

## 7. Despliegue con FastAPI

### 7.1 Estructura de la API

```python
# api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import predictions

app = FastAPI(
    title="API de Predicciones ML",
    description="API para inferencia de modelos de ML",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predictions.router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

### 7.2 Ruta de Predicciones

```python
# api/routes/predictions.py
from fastapi import APIRouter, HTTPException
from api.schemas.request_response import PredictionRequest, PredictionResponse
from api.models import model_loader
import torch

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        # Cargar datos
        input_data = torch.tensor(request.data)
        
        # Predicción
        model = model_loader.get_model()
        model.eval()
        with torch.no_grad():
            prediction = model(input_data)
        
        return PredictionResponse(
            prediction=prediction.tolist(),
            confidence=0.95
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**Ejemplo con Keras:**

```python
# api/models/model_loader.py
import tensorflow as tf
from pathlib import Path

_model = None

def get_model(model_path: str = "models/final/best_model.keras"):
    global _model
    if _model is None:
        _model = tf.keras.models.load_model(model_path)
    return _model

def load_keras_model(model_path: str):
    return tf.keras.models.load_model(model_path)
```

```python
# api/routes/predictions_keras.py
from fastapi import APIRouter, HTTPException
from api.schemas.request_response import PredictionRequest, PredictionResponse
from api.models.model_loader import get_model
import numpy as np

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        # Cargar datos
        input_data = np.array(request.data)
        
        # Predicción
        model = get_model()
        prediction = model.predict(input_data, verbose=0)
        
        return PredictionResponse(
            prediction=prediction.tolist(),
            confidence=float(np.max(prediction))
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 7.3 Esquemas

```python
# api/schemas/request_response.py
from pydantic import BaseModel
from typing import List

class PredictionRequest(BaseModel):
    data: List[List[float]]

class PredictionResponse(BaseModel):
    prediction: List[float]
    confidence: float
```

### 7.4 Ejecutar la API

```bash
# Desarrollo
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# Producción
uvicorn api.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 8. Docker

### 8.1 Dockerfile para API

```dockerfile
# docker/Dockerfile.api
FROM nvidia/cuda:12.1.0-base-ubuntu22.04

# Instalar Miniconda
RUN apt-get update && apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh

ENV PATH="/opt/conda/bin:${PATH}"

# Crear entorno
COPY environment.yml /app/
WORKDIR /app
RUN conda env create -f environment.yml

# Activar entorno y copiar código
ENV PATH="/opt/conda/envs/ml_project/bin:${PATH}"
COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 8.2 docker-compose.yml

```yaml
# docker/docker-compose.yml
version: '3.8'

services:
  api:
    build:
      context: ..
      dockerfile: docker/Dockerfile.api
    ports:
      - "8000:8000"
    environment:
      - MODEL_PATH=/app/models/final/best_model.pt
    volumes:
      - ../models:/app/models
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

---

## 9. Scripts de Entrenamiento

```python
# scripts/train_model.py
import sys
sys.path.append("..")

import torch
from torch.utils.data import DataLoader
from src.models.red_neuronal import RedNeuronal
from src.data.dataset import MiDataset
from config import settings

def main():
    # Cargar datos
    train_dataset = MiDataset(settings.DATA_PROCESSED_DIR / "train.csv")
    train_loader = DataLoader(train_dataset, batch_size=settings.BATCH_SIZE)
    
    # Modelo
    model = RedNeuronal(input_size=784, hidden_size=256, output_size=10)
    model = model.to(settings.DEVICE)
    
    # Optimizador
    optimizer = torch.optim.Adam(model.parameters(), lr=settings.LEARNING_RATE)
    criterion = torch.nn.CrossEntropyLoss()
    
    # Entrenamiento
    for epoch in range(settings.EPOCHS):
        model.train()
        for batch in train_loader:
            inputs, targets = batch
            inputs, targets = inputs.to(settings.DEVICE), targets.to(settings.DEVICE)
            
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
        
        print(f"Epoch {epoch+1}/{settings.EPOCHS}, Loss: {loss.item()}")
    
    # Guardar modelo
    torch.save(model.state_dict(), settings.MODEL_FINAL_DIR / "best_model.pt")

if __name__ == "__main__":
    main()
```

---

## 10. Entrenamiento Distribuido

### 10.1 Conceptos Clave

| Término | Descripción |
|---------|-------------|
| **DDP** | Distributed Data Parallel - replicas del modelo en cada proceso |
| **FSDP** | Fully Sharded Data Parallel - shards de parámetros entre procesos |
| **DataParallel** | Single-node multi-GPU (menos eficiente que DDP) |
| **torchrun** | Launcher para procesos distribuidos |
| **RANK** | Índice global del proceso |
| **LOCAL_RANK** | Índice local dentro del nodo |
| **WORLD_SIZE** | Total de procesos |

### 10.2 Entrenamiento Multi-GPU (Single-Node)

#### DataParallel (más simple)

```python
# scripts/train_dataparallel.py
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.nn import DataParallel

model = MiModelo()
model = DataParallel(model)  # Wrapea el modelo
model = model.cuda()

# Datos se dividen automáticamente entre GPUs
for inputs, labels in dataloader:
    inputs, labels = inputs.cuda(), labels.cuda()
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    loss.backward()
```

#### DDP (recomendado)

```python
# scripts/train_ddp.py
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data import DistributedSampler
import argparse

def setup(rank, world_size):
    dist.init_process_group("nccl", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

class MiModelo(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 10)
        )
    
    def forward(self, x):
        return self.layers(x)

def train(rank, world_size):
    setup(rank, world_size)
    
    # Crear modelo y envolver con DDP
    model = MiModelo().to(rank)
    model = DDP(model, device_ids=[rank])
    
    #Sampler para datos distribuidos
    train_sampler = DistributedSampler(
        dataset, 
        num_replicas=world_size, 
        rank=rank
    )
    train_loader = DataLoader(
        dataset, 
        batch_size=32, 
        sampler=train_sampler
    )
    
    for epoch in range(num_epochs):
        train_sampler.set_epoch(epoch)  # Para shuffles consistentes
        for batch in train_loader:
            inputs, labels = batch.to(rank), labels.to(rank)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
    
    cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--local_rank", type=int)
    args = parser.parse_args()
    
    torch.cuda.set_device(args.local_rank)
    train(args.local_rank, torch.cuda.device_count())
```

**Ejecución:**

```bash
# Single-node multi-GPU
torchrun --nproc_per_node=4 scripts/train_ddp.py
```

### 10.3 Entrenamiento Multi-Nodo

#### Configuración con torchrun

```bash
# Nodo Master (rank 0)
torchrun \
  --master_addr=192.168.1.10 \
  --master_port=29500 \
  --nnodes=2 \
  --node_rank=0 \
  --nproc_per_node=4 \
  scripts/train_ddp.py

# Nodo Worker (rank 1) - ejecutar en otra máquina
torchrun \
  --master_addr=192.168.1.10 \
  --master_port=29500 \
  --nnodes=2 \
  --node_rank=1 \
  --nproc_per_node=4 \
  scripts/train_ddp.py
```

#### Con Rendezvous (elástico)

```bash
# Genera endpoint automáticamente
torchrun \
  --rdzv_endpoint=192.168.1.10:29500 \
  --nnodes=2 \
  --nproc_per_node=4 \
  scripts/train_ddp.py
```

#### Con SLURM (clusters HPC)

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:4

srun torchrun \
  --nnodes=2 \
  --nproc_per_node=4 \
  scripts/train_ddp.py
```

### 10.4 FSDP (Fully Sharded Data Parallel)

Para modelos muy grandes que no caben en una GPU:

```python
# scripts/train_fsdp.py
import torch
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp import ShardingStrategy, MixedPrecision
from torch.distributed.fsdp.wrap import transformer_auto_wrap_policy

def train_fsdp():
    # Política de wrapping automático
    auto_wrap_policy = functools.partial(
        transformer_auto_wrap_policy,
        transformer_layer_cls={TransformerEncoderLayer}
    )
    
    # Mixed precision (FP16)
    mixed_precision_policy = MixedPrecision(
        param_dtype=torch.float16,
        reduce_dtype=torch.float16,
        buffer_dtype=torch.float16
    )
    
    model = MiModeloGrande()
    
    model = FSDP(
        model,
        sharding_strategy=ShardingStrategy.FULL_SHARD,
        auto_wrap_policy=auto_wrap_policy,
        mixed_precision=mixed_precision_policy,
        device_id=torch.cuda.current_device()
    )
    
    # Guardar modelo
    if rank == 0:
        torch.save(model.state_dict(), "modelo_fsdp.pt")

# Ejecución
torchrun --nproc_per_node=4 scripts/train_fsdp.py
```

### 10.5 Requisitos de Red

| Requisito | Descripción |
|-----------|-------------|
| **Conectividad TCP** | Los nodos deben verse entre sí |
| **Puerto abierto** | MASTER_PORT (ej. 29500) en firewall |
| **Mismas versiones** | CUDA, NCCL, PyTorch idénticos |
| **Network interface** | IB (Infiniband) para clusters grandes |

**Verificar conectividad:**

```bash
# Desde el nodo worker al master
nc -zv 192.168.1.10 29500

# Ver interfaz de red
ip route get 192.168.1.10

# Debug NCCL
export NCCL_DEBUG=INFO
```

### 10.6 Checklist de Debugging

```
❌ El job cuelga en "Waiting for children"
  └─> Verificar MASTER_ADDR y MASTER_PORT

❌ Error de timeout
  └─> Comprobar conectividad de red

❌ NCCL timeout
  └─> Usar export NCCL_DEBUG=INFO para ver errores

❌ Gradientes incorrectos
  └─> Asegurar que todos los nodos tienen los mismos datos de entrenamiento

❌ OOM en algunos nodos
  └─> Verificar que todas las GPUs tienen la misma memoria
```

### 10.7 Comparativa de Estrategias

| Estrategia | Uso | Ventajas | Desventajas |
|------------|-----|----------|-------------|
| **DataParallel** | 1 nodo, múltiples GPUs | Simple | Menos eficiente |
| **DDP** | Multi-nodo | Eficiente, estándar | Más complejo |
| **FSDP** | Modelos muy grandes | Escala a modelos huge | Overhead de comunicación |

---

## 11. Resumen: Flujo de Trabajo

```
┌─────────────────────────────────────────────────────────────────┐
│                     FLUJO DE TRABAJO                           │
└─────────────────────────────────────────────────────────────────┘

  1. CREAR ENTORNO
     └─> conda env create -f environment.yml

  2. EXPERIMENTAR (Notebooks)
     └─> jupyter notebook
     └─> 01_exploracion → 02_preparacion → 03_entrenamiento → 04_evaluacion

  3. DESARROLLAR MÓDULOS
     └─> src/models/*.py
     └─> src/data/*.py
     └─> src/training/*.py

  4. CREAR SCRIPTS
     └─> scripts/train_model.py
     └─> scripts/evaluate_model.py

  5. IMPLEMENTAR API
     └─> api/main.py
     └─> api/routes/predictions.py

  6. DOCKERIZAR
     └─> docker/Dockerfile.api
     └─> docker-compose.yml

  7. DESPLEGAR
     └─> docker-compose up --build
```

---

## 12. Recomendaciones Adicionales

| Aspecto | Recomendación |
|---------|---------------|
| **Entornos** | Usar Conda/Mamba para todo el proyecto |
| **Versionado** | Git para código, DVC para datos grandes |
| **Experimentos** | MLflow o Weights & Biases |
| **Testing** | pytest para tests unitarios |
| **Calidad código** | black, isort, ruff |
| **Documentación** | Docstrings y README.md |

---

*Esta guía proporciona una estructura sólida y escalable para proyectos Python de Machine Learning con Deep Learning.*
