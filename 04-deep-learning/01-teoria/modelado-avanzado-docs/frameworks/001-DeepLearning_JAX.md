---
title: "Deep Learning con JAX (Flax/Equinox)"
output: 
  pdf_document:
    toc: true
    toc_depth: 3
  engine: lualatex
   
---

# Deep Learning con JAX, Flax y Equinox

JAX es una biblioteca de computación numérica de Google que combina:
- **Autograd**: Derivadas automáticas
- **XLA**: Compilación a CPU/GPU/TPU
- **Just-In-Time (JIT)**: Compilación eager

A diferencia de PyTorch, JAX es **funcional e inmutable**.

## 1. Introducción a JAX

### 1.1 Filosofía

```python
# PyTorch: imperativo, mutable
model = nn.Linear(10, 5)
model.weight.data = new_weights  # mutable

# JAX: funcional, inmutable
def forward(params, x):  # params es un diccionario
    return x @ params['w'] + params['b']
```

### 1.2 Instalación

```bash
pip install jax jaxlib flax equinox
```

---

## 2. JAX Básico: Funciones Primitivas

### 2.1 Operaciones con jax.numpy

```python
import jax
import jax.numpy as jnp
from jax import grad, jit, vmap

# Tensores (JAX Arrays)
x = jnp.ones((3, 3))
x = jnp.zeros((2, 4))
x = jnp.random.normal((10, 10))

# Operaciones
y = x * 2
z = jnp.matmul(x, x.T)

# Indexación (similar a NumPy)
x[0, :]
x[:, 1:3]
```

### 2.2 Autograd

```python
def f(x):
    return x ** 2

# Derivada
df = grad(f)
print(df(3.0))  # 6.0

# Segunda derivada
d2f = grad(grad(f))
print(d2f(3.0))  # 2.0

# Gradiente con múltiples parámetros
def loss(params, x, y):
    pred = x @ params['w'] + params['b']
    return jnp.mean((pred - y) ** 2)

grad_loss = grad(loss, argnums=0)  # derivar respecto a params
```

### 2.3 JIT Compilation

```python
@jit  # Compila la función para XLA
def funcion_rapida(x, y):
    return jnp.matmul(x, y) @ x

# Equivalente a:
funcion_rapida = jit(funcion_rapida)
```

### 2.4 VMAP (Vectorized Map)

```python
# Sin vmap: loop
def predict(params, x_single):
    return x_single @ params['w'] + params['b']

# Con vmap: vectorizado
predict_batch = vmap(predict, in_axes=(None, 0))
# Ahora acepta batch de entradas
predictions = predict_batch(params, x_batch)
```

---

## 3. Flax: Neural Network Library para JAX

Flax es la librería oficial de Google para construir redes neuronales en JAX.

### 3.1 Estructura Básica

```python
import flax.linen as nn
from flax.training import train_state
import optax

class SimpleNN(nn.Module):
    hidden_dim: int
    num_classes: int
    
    @nn.compact
    def __call__(self, x):
        x = nn.Dense(self.hidden_dim)(x)
        x = nn.relu(x)
        x = nn.Dense(self.num_classes)(x)
        return x

# Crear modelo
model = SimpleNN(hidden_dim=256, num_classes=10)
dummy_input = jnp.ones((1, 784))
params = model.init(jax.random.key(0), dummy_input)
```

### 3.2 Entrenamiento con Flax

```python
from flax.training import train_state
import optax

# Crear estado de entrenamiento
def create_train_state(model, learning_rate):
    params = model.init(jax.random.key(0), jnp.ones((1, 784)))
    tx = optax.adam(learning_rate)
    return train_state.TrainState.create(
        apply_fn=model.apply,
        params=params,
        tx=tx
    )

# Bucle de entrenamiento
@jax.jit
def train_step(state, batch):
    def loss_fn(params):
        preds = state.apply_fn(params, batch['x'])
        return jnp.mean((preds - batch['y']) ** 2)
    
    grads = jax.grad(loss_fn)(state.params)
    state = state.apply_gradients(grads=grads)
    return state

# Training loop
for epoch in range(num_epochs):
    for batch in train_loader:
        state = train_step(state, batch)
```

### 3.3 Capas en Flax

```python
class CNN(nn.Module):
    @nn.compact
    def __call__(self, x, training=False):
        # Conv + BatchNorm + ReLU
        x = nn.Conv(features=32, kernel_size=(3, 3))(x)
        x = nn.BatchNorm(use_running_average=not training)(x)
        x = nn.relu(x)
        x = nn.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
        
        # Segunda conv
        x = nn.Conv(features=64, kernel_size=(3, 3))(x)
        x = nn.BatchNorm(use_running_average=not training)(x)
        x = nn.relu(x)
        x = nn.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
        
        # Flatten + Dense
        x = x.reshape((x.shape[0], -1))
        x = nn.Dense(10)(x)
        return x
```

### 3.4 Dropout

```python
class ModelWithDropout(nn.Module):
    @nn.compact
    def __call__(self, x, training=False):
        x = nn.Dense(256)(x)
        x = nn.Dropout(rate=0.3, deterministic=not training)(x)
        x = nn.relu(x)
        x = nn.Dense(10)(x)
        return x

# En entrenamiento: training=True
# En inferencia: training=False
```

### 3.5 Regularización L2

```python
# Usar optax con weight decay
tx = optax.adamw(learning_rate=1e-3, weight_decay=1e-4)

# O añadir explícitamente
def l2_loss(params):
    return sum(jnp.sum(p ** 2) for p in jax.tree_util.tree_leaves(params))

def loss_fn(params, batch):
    preds = model.apply(params, batch['x'])
    return jnp.mean((preds - batch['y']) ** 2) + 0.01 * l2_loss(params)
```

---

## 4. Equinox: Alternative Neural Networks

Equinox es una librería más simple y "pythonic" para redes neuronales en JAX.

### 4.1 Concepto Clave: PyTree

```python
import equinox as eqx

# Equinox usa clases de Python como modelos
class Linear(eqx.Module):
    weight: jax.Array
    bias: jax.Array
    
    def __init__(self, in_features, out_features, key):
        w_key, b_key = jax.random.split(key)
        self.weight = jax.random.normal(w_key, (out_features, in_features)) * 0.01
        self.bias = jnp.zeros(out_features)
    
    def __call__(self, x):
        return x @ self.weight.T + self.bias
```

### 4.2 Modelo Completo

```python
class MLP(eqx.Module):
    layers: list
    
    def __init__(self, sizes, key):
        keys = jax.random.split(key, len(sizes))
        self.layers = [Linear(sizes[i], sizes[i+1], keys[i]) 
                      for i in range(len(sizes)-1)]
    
    def __call__(self, x):
        for layer in self.layers[:-1]:
            x = jax.nn.relu(layer(x))
        return self.layers[-1](x)

# Crear modelo
model = MLP([784, 256, 128, 10], key=jax.random.key(0))
```

### 4.3 Entrenamiento con Equinox

```python
import optax

@eqx.filter_jit
def train_step(model, opt_state, x, y):
    def loss_fn(model):
        pred = model(x)
        return jnp.mean((pred - y) ** 2)
    
    grads = eqx.filter_grad(loss_fn)(model)
    
    # Actualizar solo los pesos (no el optimizador)
    updates, opt_state = optimizer.update(grads, opt_state)
    model = eqx.apply_updates(model, updates)
    
    return model, opt_state

# Filtrar parámetros entrenables
params, static = eqx.partition(model, eqx.is_array)
optimizer = optax.adam(1e-3)
opt_state = optimizer.init(params)
```

### 4.4 Dropout con Equinox

```python
class MLPWithDropout(eqx.Module):
    layers: list
    dropout_rate: float
    
    def __init__(self, sizes, dropout_rate, key):
        keys = jax.random.split(key, len(sizes))
        self.layers = [Linear(sizes[i], sizes[i+1], keys[i]) 
                      for i in range(len(sizes)-1)]
        self.dropout_rate = dropout_rate
    
    def __call__(self, x, key):
        for layer in self.layers[:-1]:
            x = jax.nn.relu(layer(x))
            # Dropout durante entrenamiento
            mask = jax.random.bernoulli(key, 1 - self.dropout_rate, x.shape)
            x = x * mask / (1 - self.dropout_rate)
        return self.layers[-1](x)

# Usar con keys diferentes cada vez
def train_step(model, x, y, key):
    subkeys = jax.random.split(key, 1)
    pred = model(x, subkeys[0])
    # ...
```

---

## 5. Transformadores con Flax

### 5.1 Multi-Head Attention

```python
class MultiHeadAttention(nn.Module):
    num_heads: int
    qkv_features: int
    
    @nn.compact
    def __call__(self, x, mask=None, training=False):
        batch, seq_len, embed_dim = x.shape
        assert embed_dim % self.num_heads == 0
        
        head_dim = embed_dim // self.num_heads
        
        # Proyecciones Q, K, V
        qkv = nn.Dense(features=self.qkv_features * 3)(x)
        q, k, v = jnp.split(qkv, 3, axis=-1)
        
        # Reshape para múltiples heads
        q = q.reshape(batch, seq_len, self.num_heads, head_dim).transpose(0, 2, 1, 3)
        k = k.reshape(batch, seq_len, self.num_heads, head_dim).transpose(0, 2, 1, 3)
        v = v.reshape(batch, seq_len, self.num_heads, head_dim).transpose(0, 2, 1, 3)
        
        # Attention scores
        attn_weights = jnp.matmul(q, k.transpose(0, 1, 3, 2)) / jnp.sqrt(head_dim)
        
        if mask is not None:
            attn_weights = attn_weights + mask
        
        attn_weights = jax.nn.softmax(attn_weights, axis=-1)
        attn_output = jnp.matmul(attn_weights, v)
        
        # Concatenar heads
        attn_output = attn_output.transpose(0, 2, 1, 3).reshape(batch, seq_len, embed_dim)
        
        return nn.Dense(features=embed_dim)(attn_output)
```

---

## 6. Guardar y Cargar Modelos

### 6.1 Flax

```python
# Guardar
from flax.training import checkpoints
checkpoints.save_checkpoint(ckpt_dir='./checkpoints', 
                           target=state, 
                           step=epoch, 
                           prefix='model_')

# Cargar
state = checkpoints.restore_checkpoint(ckpt_dir='./checkpoints', 
                                     target=state, 
                                     step=10)
```

### 6.2 Equinox

```python
import pickle

# Guardar
with open('model.eqx', 'wb') as f:
    pickle.dump(model, f)

# Cargar
with open('model.eqx', 'rb') as f:
    model = pickle.load(f)
```

---

## 7. Debugging y Troubleshooting

### 7.1 Ver gradientes

```python
grads = jax.grad(loss_fn)(params)
print(jax.tree_map(jnp.linalg.norm, grads))
```

### 7.2 Shapes debugging

```python
# Usar debug mode en Flax
model = SimpleNN(hidden_dim=256, num_classes=10)
variables = model.init(jax.random.key(0), jnp.ones((1, 784)), debug=True)
```

### 7.3 Problemas comunes

#### a) NaN en pérdida
```python
# 1. Verificar tipos
print(f"Type: {x.dtype}")  # Asegurar float32

# 2. Gradient clipping
grads = jax.lax.clamp(grads, -1.0, 1.0)

# 3. Debug con jax.debug.print
def loss_fn(params):
    jax.debug.print("x: {}", x)
    return compute_loss(params)

# 4. Disable JIT temporalmente
@jax.jit  # Comentar para debug
def train_step(params, batch):
    ...
```

#### b) Shapes mismatch
```python
# 1. Ver shapes
print(f"Expected: {expected.shape}, Got: {x.shape}")

# 2. Usar debug callback
from jax import debug

def forward(x):
    debug.print("x shape: {}", jnp.shape(x))
    return model(x)

# 3. Verificar con jax.make_array
jax.debug.breakpoint()  # Equivalent a pdb.set_trace()
```

#### c) Performance issues
```python
# 1. Profile con JAXpr
from jax import profiler

# 2. Verificar GPU usage
print(f"Available devices: {jax.devices()}")

# 3. Verificar JIT compilation
print(jax.xla_computation(add)(1, 2).as_hlo_text())

# 4. Memory profiling
jax.profiler.save_device_memory_trace("memory.trace")
```

### 7.4 Debugging tips

```python
# 1. Disable JIT para debug
@jax.jit  # Quitar para debugging
def forward(x):
    return model(x)

# 2. Usar breakpoint
jax.debug.breakpoint()

# 3. Ver valores intermedios
from jax import latent_jvp, latent_vjp
jax.debug.callback(lambda: print("Reached!"))

# 4. Verificar pureza de funciones
# Funciones pasadas a JAX deben ser puras (sin side effects)
```

5 Errores comunes JAX### 7.

| Error | Causa | Solución |
|-------|-------|----------|
| TracerDictionary | Mutating arrays | Usar jax.lax.scatter o in_place |
| Shape mismatch | Dimensiones | Verificar con jnp.shape() |
| NaN | Overflow | Usar float32, gradient clipping |
| Slow | Sin JIT | Añadir @jit a funciones |
| Device mismatch | CPU/GPU | jax.devices() verificar |

---

## 8. Diferencias Clave JAX vs PyTorch

| Aspecto | PyTorch | JAX |
|---------|---------|-----|
| **Ejecución** | Eager (dinámica) | Eager por defecto, JIT opcional |
| **Estado** | Mutable (in-place) | Inmutable (funcional) |
| **Gradientes** | `.grad` | `jax.grad` |
| **Loop entrenamiento** | Manual | Manual o usando librerías |
| **Modelo** | `nn.Module` | `nn.Module` (Flax) / clase (Equinox) |
| **GPU** | `.to('cuda')` | `.to(device)` |

---

## 9. Cuándo Usar Qué

### Flax:
- Proyectos grandes de Google
- Necesitas estructura formal
- Feature: NNX para estado mutable

### Equinox:
- Prefieres estilo Pythonic
- Simplicidad
- Buen debugging

### JAX puro:
- Solo necesitas autograd
- Custom training loops
- Investigación de alto rendimiento

---

## 10. Ejemplo Completo: MNIST con Flax

```python
import jax
import jax.numpy as jnp
from flax import linen as nn
from flax.training import train_state, common_utils
import optax
from torch.utils.data import DataLoader, TensorDataset

# Modelo
class CNN(nn.Module):
    @nn.compact
    def __call__(self, x, training=False):
        x = nn.Conv(features=32, kernel_size=(3, 3))(x)
        x = nn.BatchNorm(use_running_average=not training)(x)
        x = nn.relu(x)
        x = nn.avg_pool(x, (2, 2))
        
        x = nn.Conv(features=64, kernel_size=(3, 3))(x)
        x = nn.BatchNorm(use_running_average=not training)(x)
        x = nn.relu(x)
        x = nn.avg_pool(x, (2, 2))
        
        x = x.reshape((x.shape[0], -1))
        x = nn.Dense(256)(x)
        x = nn.relu(x)
        x = nn.Dense(10)(x)
        return x

# Estado de entrenamiento
def create_train_state(learning_rate):
    model = CNN()
    params = model.init(jax.random.key(0), jnp.ones((1, 1, 28, 28)))
    tx = optax.adam(learning_rate)
    return train_state.TrainState.create(
        apply_fn=model.apply,
        params=params,
        tx=tx
    )

# Train step
@jax.jit
def train_step(state, batch):
    def loss_fn(params):
        preds = state.apply_fn(params, batch['x'], training=True)
        return jnp.mean(
            optax.softmax_cross_entropy_with_integer_labels(preds, batch['y'])
        )
    grads = jax.grad(loss_fn)(state.params)
    return state.apply_gradients(grads=grads)

# Training loop
state = create_train_state(1e-3)
for epoch in range(10):
    for batch in train_loader:
        state = train_step(state, {'x': batch[0], 'y': batch[1]})
```

---

## 11. Distributed Training en JAX

### 11.1 Multi-GPU básico con Flax

```python
import jax
import jax.numpy as jnp
from flax.training import train_state
import optax

# Verificar GPUs
print(f"Devices: {jax.devices()}")

# sharding de parámetros
def shard_params(params):
    return jax.tree_util.tree_map(
        lambda x: jax.device_put_replicated(x, jax.devices()),
        params
    )

# Ejemplo: train_step con pmap para múltiples GPUs
@jax.pmap
def train_step(state, batch):
    def loss_fn(params):
        preds = state.apply_fn(params, batch['x'])
        return jnp.mean(optax.squared_error(preds, batch['y']))
    
    grads = jax.grad(loss_fn)(state.params)
    grads = jax.lax.all_gather(grads, axis_name='batch')
    return state.apply_gradients(grads=grads)

# Sincronizar después de cada step
state = jax.pmap(lambda _: state)(state)
```

### 11.2 Distributed con MPI (jax.distributed)

```python
# Inicializar cluster distribuido
# jax.distributed.initialize()

# Ver devices disponibles
print(f"Total devices: {len(jax.devices())}")
```

### 11.3 Data Parallel con Flax

```python
from flax.jax_utils import replicate, unreplicate

# Replicar estado en todos los devices
state = replicate(state)

# Training loop
for batch in dataloader:
    # Dividir batch entre GPUs
    batch = jax.tree_util.tree_map(
        lambda x: x.reshape(len(jax.devices()), -1, *x.shape[1:]),
        batch
    )
    state = train_step(state, batch)

# Obtener parámetros (solo del primer device)
params = unreplicate(state.params)
```

### 11.4 Ejemplo completo multi-GPU

```python
import jax
import jax.numpy as jnp
from flax import linen as nn
from flax.training import train_state
import optax
import numpy as np

# Modelo
class SimpleMLP(nn.Module):
    @nn.compact
    def __call__(self, x):
        x = nn.Dense(256)(x)
        x = nn.relu(x)
        x = nn.Dense(10)(x)
        return x

# Inicializar con pmap
batch = np.random.randn(8, 784).astype(np.float32)
model = SimpleMLP()
variables = model.init(jax.random.key(0), batch)

# Replicar en todas las GPUs
n_devices = len(jax.devices())
params = replicate(variables['params'], devices=jax.devices())

# Training step con pmap
@jax.pmap
def train_step(params, x, y):
    def loss_fn(params):
        logits = model.apply({'params': params}, x)
        return jnp.mean(optax.softmax_cross_entropy_with_integer_labels(logits, y))
    
    grads = jax.grad(loss_fn)(params)
    return grads

#模拟数据
X = np.random.randn(32, 784).astype(np.float32)
y = np.random.randint(0, 10, 32).astype(np.int32)

# Dividir datos entre GPUs
X_batched = X.reshape(n_devices, -1, 784)
y_batched = y.reshape(n_devices, -1)

# Entrenar
grads = train_step(params, X_batched, y_batched)
print("Multi-GPU training working!")
```

### 11.5对比: JAX vs PyTorch Distributed

| Aspecto | PyTorch | JAX |
|---------|---------|-----|
| Multi-GPU | DDP, DataParallel | pmap, xmap |
| Multi-Machine | torchrun, Slurm | jax.distributed |
| Sharding | FSDP | jaxtyping + pjit |
| Communication | NCCL, Gloo | jax.lax.all_gather |

- [JAX Documentation](https://jax.readthedocs.io/)
- [Flax Documentation](https://flax.readthedocs.io/)
- [Equinox Documentation](https://docs.kidger.site/equinox/)
- [JAX Examples](https://github.com/google/jax/tree/main/examples)
