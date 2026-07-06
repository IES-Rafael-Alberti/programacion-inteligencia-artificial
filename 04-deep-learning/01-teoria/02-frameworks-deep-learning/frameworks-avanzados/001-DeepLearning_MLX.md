# Guía de MLX (Apple Silicon)

MLX es el framework de deep learning de Apple, optimizado para Apple Silicon (M1, M2, M3). Ofrece una API similar a NumPy y PyTorch.

---

## 1. Instalación

```bash
# Requiere Apple Silicon (M1/M2/M3)
pip install mlx

# Versión nightly
pip install mlx-nightly
```

---

## 2. Conceptos Básicos

### Tensores

```python
import mlx.core as mx

# Crear tensores
x = mx.array([1.0, 2.0, 3.0])
print(x.shape)  # [3]

# Operaciones
y = mx.sum(x)
z = mx.matmul(x, x.T)
```

### Diferencias con NumPy

```python
import numpy as np
import mlx.core as mx

# NumPy: evaluación eager
np_x = np.array([1.0, 2.0])
result = np_x * 2  # Inmediato

# MLX: lazy por defecto
mlx_x = mx.array([1.0, 2.0])
result = mlx_x * 2  # Lazy, se evalúa cuando se necesita
print(result)  # Evaluado
```

---

## 3. Building Models

### Sequential

```python
import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.relu(),
    nn.Dropout(0.5),
    nn.Linear(256, 10)
)
```

### Custom Model

```python
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(784, 256)
        self.l2 = nn.Linear(256, 10)
    
    def __call__(self, x):
        x = mx.maximum(0, self.l1(x))  # ReLU
        return self.l2(x)

model = MyModel()
```

---

## 4. Training

```python
import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim

# Datos
X = mx.random.normal((1000, 784))
y = mx.random.randint(0, 10, (1000,))

# Modelo
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.relu(),
    nn.Linear(256, 10)
)

# Función de pérdida
def loss_fn(model, X, y):
    return nn.losses.cross_entropy(model(X), y)

# Optimizador
optimizer = optim.Adam(learning_rate=1e-3)

# Gradientes
grad_fn = mlx.value_and_grad(loss_fn)

# Training loop
for epoch in range(10):
    loss, grads = grad_fn(model, X, y)
    optimizer.update(model, grads)
    
    # Forzar evaluación
    mx.eval(model.parameters(), loss)
    print(f"Epoch {epoch}: Loss {loss.item()}")
```

---

## 5. Guardar/Cargar Modelos

```python
# Guardar
model.save('model.npz')

# Cargar
model = MyModel()
model.load('model.npz')
```

---

## 6. MLX para Transformers

```python
# Instalar mlx-nlp
pip install mlx-nlp

from mlx_nlp import generate

# Cargar modelo
model = mlx_nlp.load_model('mlx-community/llama-7b')

# Generar texto
output = generate(model, "Hello, how are you?")
print(output)
```

---

## 7. MLX LLM

```python
# Instalar mlx-lm
pip install mlx-lm

from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Llama-3.2-1B-Instruct-4bit")

response = generate(
    model,
    tokenizer,
    prompt="Write a short story",
    max_tokens=200
)
print(response)
```

---

## 8. MLX Vision

```python
import mlx_vision as vision
from mlx_vision import models, transforms

# Cargar modelo
vit = models.ViT()

# Preprocesar imagen
img = vision.load_image("image.jpg")
img = transforms.resize(img, (224, 224))
img = transforms.normalize(img)

# Inferencia
output = vit(img)
```

---

## 9. Conversión desde PyTorch

```python
# Modelos de PyTorch pueden convertirse a MLX
# Usar scripts de conversión o mlx.convert

# Ejemplo básico de equivalencias
# PyTorch -> MLX
torch.nn.Linear(in_features, out_features)  # -> nn.Linear(in_features, out_features)
torch.relu(x)                                # -> mx.maximum(0, x)
torch.optim.Adam(params, lr=lr)             # -> optim.Adam(lr=lr)
```

---

## 10. Benchmark (Apple Silicon)

```python
import time
import mlx.core as mx

# GPU M2 vs CPU
x = mx.random.normal((1024, 1024))

# Medir tiempo GPU
start = time.time()
for _ in range(100):
    y = mx.matmul(x, x)
mx.eval(y)
print(f"GPU: {time.time() - start:.3f}s")

# Para CPU
x_cpu = mx.array(x.tolist())
start = time.time()
for _ in range(100):
    y = mx.matmul(x_cpu, x_cpu)
mx.eval(y)
print(f"CPU: {time.time() - start:.3f}s")
```

---

## 11. Cuándo usar MLX

| Ventajas | Desventajas |
|----------|-------------|
| Rápido en Apple Silicon | Solo funciona en Mac |
| Bajo consumo energía | Menor ecosistema |
| Similar a PyTorch/NumPy | Comunidad más pequeña |
|Excelente para LLMs | Menos opciones deployment |

---

## 12. Recursos

- [MLX Documentation](https://ml-explore.github.io/mlx/)
- [MLX Examples](https://github.com/ml-explore/mlx-examples)
- [MLX LLM](https://github.com/ml-explore/mlx-lm)
- [mlx-nlp](https://github.com/Blaizzy/mlx-nlp)
