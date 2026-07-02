# JAX — Programación GPU de Alto Rendimiento

## Qué es JAX

JAX es una librería de Google diseñada para computación numérica de alto rendimiento. Combina tres ideas centrales:

1. **Arrays estilo NumPy** que se ejecutan en CPU, GPU o TPU de forma transparente.
2. **Transformaciones funcionales** aplicadas sobre funciones Python puras.
3. **Compilación JIT** que convierte código Python en kernels optimizados de XLA.

```python
import jax.numpy as jnp
from jax import grad, jit

# Igual que NumPy, pero en GPU si hay una disponible
x = jnp.array([1.0, 2.0, 3.0])
print(jnp.sum(x ** 2))
```

## Transformaciones principales

### `jax.jit` — Compilación just-in-time

Convierte una función Python pura en un kernel XLA compilado. La primera llamada tarda más (compilación); las siguientes son muy rápidas.

```python
from jax import jit

@jit
def product_matrix(A, B):
    return jnp.dot(A, B)

# Primera llamada: compila
result = product_matrix(A, B)
# Siguientes llamadas: ya compiladas
result = product_matrix(A2, B2)
```

### `jax.grad` — Diferenciación automática

Calcula el gradiente de una función escalar respecto a sus argumentos. Base para optimización y redes neuronales.

```python
from jax import grad

def loss(w, x, y):
    pred = jnp.dot(x, w)
    return jnp.mean((pred - y) ** 2)

grad_fn = grad(loss)   # diferencia respecto a w (primer argumento)
gradient = grad_fn(w, x, y)
```

Para gradientes respecto a múltiples argumentos se usa `argnums`:

```python
grad(loss, argnums=(0, 1))  # gradientes de w y x
```

### `jax.vmap` — Vectorización automática

Vectoriza una función escrita para un solo ejemplo de forma que opere sobre un batch:

```python
from jax import vmap

def f_single(x):
    return jnp.sum(x ** 2)

f_batch = vmap(f_single)     # aplica f_single a cada fila
result = f_batch(X_matrix)   # shape: (n_samples,)
```

### `jax.pmap` — Paralelismo multi-GPU

Distribuye el cálculo sobre múltiples aceleradores:

```python
from jax import pmap
f_parallel = pmap(f_batch)
```

## Modelo de programación funcional

JAX exige que las funciones sean **puras** (sin efectos de lado, sin estado mutable). Esto es un requisito de XLA para poder compilarlas y diferenciarlas.

```python
# CORRECTO — función pura
def relu(x):
    return jnp.maximum(0.0, x)

# INCORRECTO con JAX — estado mutable global
counter = 0
def bad_fn(x):
    counter += 1   # JAX no puede trazar esto
    return x * 2
```

El estado (parámetros de una red, pesos de un modelo) se pasa explícitamente como argumentos.

## Ejemplo completo: descenso de gradiente

```python
import jax.numpy as jnp
from jax import grad, jit

def mse(params, X, y):
    w, b = params["w"], params["b"]
    pred = X @ w + b
    return jnp.mean((pred - y) ** 2)

grad_fn = jit(grad(mse))      # diferencia y compila

params = {"w": jnp.zeros(X.shape[1]), "b": 0.0}
lr = 0.01

for step in range(100):
    grads = grad_fn(params, X_train, y_train)
    params = {k: params[k] - lr * grads[k] for k in params}
```

## JAX vs PyTorch vs TensorFlow

| Característica | JAX | PyTorch | TensorFlow |
|----------------|-----|---------|-----------|
| API | Funcional pura | OOP con autograd | Mixta |
| Diferenciación | Transformaciones composables | `.backward()` | `tf.GradientTape` |
| JIT | XLA por defecto | `torch.compile` (Dynamo) | `@tf.function` |
| Investigación | Muy popular | Muy popular | Menos en investigación |
| Producción | Emergente | Muy extendido | Amplio deployment |

JAX destaca por la composabilidad de sus transformaciones: `jit(vmap(grad(f)))` funciona de forma natural.

## Ecosistema sobre JAX

Para uso práctico, existen librerías de alto nivel construidas sobre JAX:

| Librería | Para qué |
|----------|----------|
| **Flax** / **Haiku** | Redes neuronales |
| **Optax** | Optimizadores (Adam, SGD, etc.) |
| **Orbax** | Checkpointing de modelos |

## Resultados de Aprendizaje asociados

- **RA2.b**: Identificar librerías de IA de alto rendimiento y sus transformaciones funcionales.
- **RA2.d**: Implementar diferenciación automática y JIT para aceleración.
- **RA2.e**: Comparar tiempos de ejecución entre NumPy, PyTorch y JAX.

## Notebooks relacionados

- [02_jax_intro.ipynb](../02-ejemplos/02_jax_intro.ipynb) — Arrays, grad y jit.
- [03_gpu_benchmarks.ipynb](../02-ejemplos/03_gpu_benchmarks.ipynb) — Benchmarks comparativos.
