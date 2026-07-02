# Benchmarking y Optimización de Modelos en GPU

## Por qué medir el rendimiento

Acelerar código sin medir primero es un error clásico. La optimización prematura lleva a:

- Cambios en partes del código que no son el cuello de botella.
- Pérdida de legibilidad sin ganancia real.
- Falsas conclusiones sobre qué tecnología es mejor.

**Medir primero, optimizar después.**

## Taxonomía de los cuellos de botella

```
Tiempo total de ejecución
├── CPU (Python puro, Pandas, NumPy)
│   ├── Serialización / parsing de datos
│   ├── Operaciones vectorizadas
│   └── Lógica de control (bucles Python)
├── Transferencia CPU ↔ GPU (PCIe)
│   ├── H2D (Host to Device)  ← caro, evitar repetir
│   └── D2H (Device to Host)
└── GPU
    ├── Lanzamiento de kernels (overhead fijo)
    ├── Ocupancia de los SM (streaming multiprocessors)
    └── Cómputo efectivo
```

El objetivo es maximizar el tiempo dentro de la GPU y minimizar las transferencias.

## Herramientas de medición

### `timeit` — medición básica en Python

```python
import timeit

stmt = "resultado = A @ B"
setup = "import numpy as np; A = np.random.rand(1000, 1000); B = np.random.rand(1000, 1000)"

tiempo = timeit.timeit(stmt=stmt, setup=setup, number=100)
print(f"Media: {tiempo / 100 * 1000:.2f} ms")
```

### `time.perf_counter` — cronómetro de alta resolución

```python
import time

inicio = time.perf_counter()
resultado = modelo.fit(X_train, y_train)
fin = time.perf_counter()
print(f"Tiempo: {(fin - inicio) * 1000:.1f} ms")
```

### CUDA Events — medición precisa en GPU

Las operaciones GPU son asíncronas. Sin sincronizar, `time.time()` mide la entrega del trabajo a la GPU, no su ejecución real.

```python
import torch

inicio = torch.cuda.Event(enable_timing=True)
fin = torch.cuda.Event(enable_timing=True)

inicio.record()
resultado = modelo(X_gpu)
fin.record()

torch.cuda.synchronize()
print(f"Tiempo GPU: {inicio.elapsed_time(fin):.2f} ms")
```

### `nvidia-smi` — monitoreo del hardware

```bash
# Monitoreo en tiempo real (refresco cada segundo)
nvidia-smi dmon -s u -d 1

# Métricas de utilización
nvidia-smi --query-gpu=utilization.gpu,utilization.memory,memory.used --format=csv -l 1
```

Columnas clave:
- `util.gpu`: % de utilización del procesador GPU.
- `mem.used`: memoria VRAM consumida.
- `temperature.gpu`: temperatura (importante para sesiones largas).

## Comparativa NumPy vs RAPIDS vs JAX

Para una multiplicación de matrices de 4096×4096:

| Operación | NumPy (CPU) | JAX (GPU, compilado) | cuDF (GPU) |
|-----------|-------------|----------------------|------------|
| Multiplicación matricial | ~800 ms | ~8 ms | N/A |
| Suma de columnas (1M filas) | ~12 ms | ~1.5 ms | ~0.8 ms |
| Entrenamiento KMeans (100k pts) | ~4 s | N/A | ~0.3 s |

Los valores son aproximados y dependen del hardware (GPU A100, CPU Xeon).

## Factores que limitan la aceleración

### Ley de Amdahl

Si una fracción `p` del programa puede paralelizarse:

$$S = \frac{1}{(1-p) + \frac{p}{N}}$$

Donde $N$ es el número de procesadores paralelos (simplificando para GPU). Si el 20% del código es secuencial, la aceleración máxima es ×5 aunque se usen infinitos núcleos.

### Memoria y ancho de banda

La GPU tiene memoria limitada (8–80 GB según modelo). Para datasets que no caben en VRAM:

- Usar **chunking**: procesar en lotes que sí caben.
- cuDF soporta backends fuera de memoria mediante **Dask + cuDF**.
- JAX lanza un `OOM` explícito — gestionar con `jax.device_put` y `block_until_ready`.

### Overhead de transferencia

Para datasets pequeños (< unos cientos de MB), el tiempo de copia CPU→GPU puede dominar:

```python
# MAL: muchas transferencias pequeñas
for batch in batches:
    gpu_batch = cudf.from_pandas(batch)   # transferencia en cada iter
    resultado = procesar(gpu_batch)
    resultados.append(resultado.to_pandas())

# BIEN: copiar una vez, iterar en GPU
df_gpu = cudf.from_pandas(df_completo)
for batch in chunks(df_gpu):
    resultado = procesar(batch)
```

## Perfilado con JAX

```python
import jax
import jax.numpy as jnp

# Forzar compilación antes de medir
f = jax.jit(lambda x: jnp.dot(x, x.T))
x = jnp.ones((1000, 1000))
f(x).block_until_ready()   # compilación

# Ahora medir
import time
inicio = time.perf_counter()
resultado = f(x).block_until_ready()
print(f"{(time.perf_counter() - inicio) * 1000:.2f} ms")
```

El `.block_until_ready()` es necesario porque JAX es asíncrono.

## Optimización: checklist

- [ ] Verificar que el modelo/tensor realmente está en GPU (`.device`, `cudf.is_cuda_available()`).
- [ ] Evitar `.to_pandas()` / `D2H` dentro de bucles de entrenamiento.
- [ ] Usar tipos de menor precisión (`float16`, `bfloat16`) cuando sea posible.
- [ ] Pre-cargar los datos completos antes de medir (excluir I/O del benchmark).
- [ ] Warmup: ejecutar una vez antes de cronometrar (activa la compilación JIT).
- [ ] Repetir el benchmark varias veces y tomar la mediana, no el mínimo.

## Resultados de Aprendizaje asociados

- **RA2.d**: Implementar y comparar experimentos de rendimiento CPU vs GPU.
- **RA2.e**: Evaluar cuantitativamente el impacto de la aceleración GPU con métricas reproducibles.

## Notebooks relacionados

- [03_gpu_benchmarks.ipynb](../02-ejemplos/03_gpu_benchmarks.ipynb) — Benchmarks comparativos RAPIDS, JAX, NumPy.
- [01_rapids_intro.ipynb](../02-ejemplos/01_rapids_intro.ipynb) — cuDF/cuML en práctica.
- [02_jax_intro.ipynb](../02-ejemplos/02_jax_intro.ipynb) — JAX jit y grad.
