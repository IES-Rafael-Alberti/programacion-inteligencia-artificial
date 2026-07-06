# UD4 - Introduccion a JAX (guia rapida y practica)

## 1. Que es JAX y para que sirve

JAX es una libreria para computacion numerica que combina:
- Numpy acelerado
- Derivacion automatica
- Compilacion JIT

Se usa mucho en investigacion y en escenarios de alto rendimiento.

Ideas clave:
- Programacion funcional (preferencia por funciones puras)
- Gradientes con `jax.grad`
- Compilacion con `jax.jit`
- Vectorizacion con `jax.vmap`

---

## 2. Enfoque mental en JAX

A diferencia de Keras/PyTorch orientados a objetos, en JAX suele hacerse:
1. Definir funciones (`forward`, `loss`).
2. Pasar parametros explicitamente.
3. Calcular gradientes de funciones.
4. Actualizar parametros de forma funcional.

---

## 3. Componentes mas usados

- `jax.numpy` (`jnp`) para operaciones numericas.
- `jax.grad` para derivadas.
- `jax.jit` para compilar funciones.
- `jax.random` para manejo funcional de aleatoriedad.

---

## 4. Ejemplo conceptual minimo

```python
import jax
import jax.numpy as jnp

def model(params, x):
    w, b = params
    return jnp.dot(x, w) + b

def loss_fn(params, x, y):
    pred = model(params, x)
    return jnp.mean((pred - y) ** 2)

grads = jax.grad(loss_fn)(params, x_batch, y_batch)
```

---

## 5. Activaciones y capas (en practica)

En JAX "puro" las capas y activaciones se expresan con funciones.
En ecosistemas sobre JAX (Flax/Haiku/Equinox), se usan abstracciones de capas.

Activaciones frecuentes:
- `jax.nn.relu`
- `jax.nn.sigmoid`
- `jax.nn.softmax`
- `jax.nn.tanh`

Regla de salida (igual que en otros frameworks):
- Regresion: lineal
- Binaria: sigmoid/logits
- Multiclase: softmax/logits

---

## 6. Perdida y optimizacion

Perdidas tipicas:
- Regresion: MSE / MAE
- Binaria: BCE
- Multiclase: CE

Optimizacion:
- Puede hacerse manual o con librerias como Optax.

Ejemplo conceptual de actualizacion:

```python
params = jax.tree_map(lambda p, g: p - lr * g, params, grads)
```

---

## 7. Regularizacion y normalizacion

- Regularizacion L2 en la funcion de perdida
- Dropout/BatchNorm via librerias de alto nivel (por ejemplo Flax)
- Data augmentation en pipeline de datos

---

## 8. Batches, epochs y compilacion

- `batch_size`: lotes de datos
- `epoch`: pasada completa
- `jit` puede acelerar mucho el entrenamiento tras compilacion inicial

Nota docente:
- Primera ejecucion de una funcion `jit` puede tardar mas (compila).
- Ejecuciones siguientes suelen ser mas rapidas.

---

## 9. CPU/GPU/TPU

Comprobacion:

```python
import jax
print(jax.devices())
```

JAX puede trabajar en CPU/GPU/TPU segun instalacion.
En docencia, CPU o GPU de Colab suele ser suficiente para ejemplos pequenos.

---

## 10. Errores frecuentes en JAX

- Esperar estilo orientado a objetos como Keras/PyTorch.
- Mutar estado "in place" (JAX favorece inmutabilidad).
- Olvidar que `jit` compila por forma/tipo de entrada.
- Mezclar mal aleatoriedad (manejo incorrecto de `PRNGKey`).

---

## 11. Plantilla minima recomendada

```python
@jax.jit
def train_step(params, x, y, lr):
    grads = jax.grad(loss_fn)(params, x, y)
    new_params = jax.tree_map(lambda p, g: p - lr * g, params, grads)
    return new_params
```

---

## 12. Resumen rapido para alumnado

- JAX es muy potente para derivacion automatica y rendimiento.
- Es ideal para ampliar nivel tras dominar Keras/PyTorch.
- Misma teoria de redes neuronales; cambia el estilo de implementacion.
