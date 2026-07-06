---
title: "Comparativa de Frameworks de Deep Learning"
output: 
  pdf_document:
    toc: true
    toc_depth: 3
  engine: lualatex
   
---

# Comparativa de Frameworks de Deep Learning

Esta guía presenta una comparativa de los principales frameworks y librerías de deep learning disponibles en 2025.

---

## 1. Tabla Comparativa General

| Framework | Nivel | Empresa | Pros | Contras | Mejor para |
|-----------|-------|---------|------|---------|------------|
| **Keras 3** | Alto | Google | Fácil uso, multi-backend | Menos flexible | Principiantes, prototipado rápido |
| **PyTorch** | Bajo-Medio | Meta | Gran ecosistema, investigación | GPU necesaria para algo serio | Investigación, producción |
| **JAX** | Bajo | Google | Alto rendimiento, XLA | Curva pronunciada, funcional | Investigación高性能, TPUs |
| **Flax** | Medio | Google | Estructura formal, activa | Comunidad más pequeña | Proyectos Google-style |
| **Equinox** | Medio | Comunidad | Simple, pythonic | Menor documentación | Simplicidad, prototipado |
| **TensorFlow** | Multi-nivel | Google | Ecosistema completo, TF Lite/TFS | Complejo, menos popular | Producción a escala |
| **ONNX** | Intercambio | Varios | Portabilidad | Limitado a ops soportadas | Deployment multiplataforma |
| **MLX** | Alto | Apple | Fácil, Apple Silicon | Solo Mac | Mac con MLX |
| **PaddlePaddle** | Multi-nivel | Baidu | Chin market | Docs en inglés limitados | Mercado chino |
| **MindSpore** | Multi-nivel | Huawei | Edge computing | Ecosistema limitado | Edge Huawei |
| **TinyGrad** | Bajo | Andrej Karpathy | Minimal, readable | No para producción | Aprendizaje, prototipado rápido |

---

## 2. Keras 3

### Ventajas
- **Multi-backend**: Funciona con TensorFlow, JAX, PyTorch, NumPy
- **Fácil de aprender**: API clara y bien documentada
- **Integración con TF**: Acceso completo al ecosistema TensorFlow
- **Perfecto para principiantes**: Curva de aprendizaje suave

### Inconvenientes
- **Menos flexible** que PyTorch o JAX para técnicas avanzadas
- **Rendimiento** puede ser menor en casos específicos
- **Dependencia** del backend elegido

### Casos de uso ideales
- Educación y aprendizaje de deep learning
- Prototipado rápido
- Proyectos donde la simplicidad es prioridad
- Cuando se necesita multi-backend

### Ejemplo rápido
```python
from keras.models import Sequential
from keras.layers import Dense

model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=10)
```

---

## 3. PyTorch

### Ventajas
- **Dominio académico**: Estándar en investigación
- **Grafo dinámico**: Fácil debugging con breakpoints
- **Ecosistema rico**: torchvision, torchaudio, transformers, etc.
- **Pythonic**: Se siente como Python nativo

### Inconvenientes
- **Deployment** requiere más trabajo (TorchScript, ONNX)
- **Mobile** no es tan maduro como TF Lite
- **Documentación** a veces dispersa

### Casos de uso ideales
- Investigación académica
- Prototipado de nuevas arquitecturas
- Producción media-grande
- Cuando necesitas debugging fácil

### Ejemplo rápido
```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(10, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())
```

---

## 4. JAX (con Flax/Equinox)

### Ventajas
- **Alto rendimiento**: Compilación XLA a GPU/TPU
- **Funciones puras**: Más fácil de razonar matemáticamente
- **Transformaciones**: grad, jit, vmap, pmap son poderosas
- **TPU support**: Primero en soporte para TPU

### Inconvenientes
- **Curva pronunciada**: Paradigma funcional diferente
- **Inmutabilidad**: Requiere cambiar forma de pensar
- **Debugging** más difícil (traced as XLA)

### Casos de uso ideales
- Investigación de alto rendimiento
- Grandes modelos (LLMs, diffusion models)
- TPU training
- Cuando necesitas máximo rendimiento

### Ejemplo rápido (Flax)
```python
import flax.linen as nn

class MLP(nn.Module):
    @nn.compact
    def __call__(self, x):
        x = nn.Dense(64)(x)
        x = nn.relu(x)
        return nn.Dense(1)(x)
```

---

## 5. TensorFlow + Keras

### Ventajas
- **Ecosistema completo**: TF Lite, TF.js, TF Serving, TFX
- **Producción robusta**: Líder en deployment
- **Keras integrado**: Facilidad de uso
- **Visualización**: TensorBoard es excellent

### Inconvenientes
- **API complejas**: Demasiadas formas de hacer lo mismo
- **Release cycle** rápido puede generar churn
- **Popularidad en declive** vs PyTorch

### Casos de uso ideales
- Deployment a producción a escala
- Mobile/Edge (TF Lite)
- Web (TF.js)
- Pipelines MLOps (TFX)

---

## 6. Flax vs Equinox

### Flax
- Diseño más formal y estructurado
- Mejor para equipos grandes
- Más features (NNX para estado mutable)
- Mantenido por Google

### Equinox
- Más simple y pythonic
- Mejor para aprendizaje y prototipado
- Mejor debugging
- Más comunidad independent

### Recomendación
- **Flax**: Si trabajas en Google o necesitas estructura
- **Equinox**: Si prefieres simplicidad y Python natural

---

## 7. Otras librerías mención

### ONNX (Open Neural Network Exchange)
- Formato interoperable entre frameworks
- Exportar de PyTorch/Keras a TF o viceversa
- **Uso**: Deployment multiplataforma

### MLX (Apple)
- Framework de Apple para Apple Silicon
- Similar API a NumPy/PyTorch
- **Uso**: Mac con M1/M2/M3

### TinyGrad
- Implementación minimal por Andrej Karpathy
- ~1000 líneas de código
- Bueno para entender cómo funcionan los DL frameworks

### PaddlePaddle (Baidu)
- Popular en China
- Docs en chino mejores que en inglés
- **Uso**: Mercado chino

### MindSpore (Huawei)
- Diseño para edge y cloud
- Integración con hardware Huawei
- **Uso**: Ecosistema Huawei

---

## 8. Guía de Selección

### ¿Qué framework elegir?

```
¿Principiante?
├─ Sí → Keras 3
└─ No ↓
  ¿Investigación?
  ├─ Sí → PyTorch o JAX
  └─ No ↓
    ¿Producción a escala?
    ├─ Sí → TensorFlow o PyTorch + ONNX
    └─ No ↓
      ¿Alto rendimiento/TPU?
      ├─ Sí → JAX (Flax/Equinox)
      └─ No → PyTorch o Keras 3
```

### Por tipo de proyecto

| Proyecto | Recomendado |
|----------|-------------|
| Curso/Docencia | Keras 3 |
| Tesis/Investigación | PyTorch |
| Startup rápido | PyTorch |
| Enterprise producción | TensorFlow |
| High performance | JAX |
| Mobile | TF Lite / PyTorch Mobile |
| Web | TF.js |
| Apple Silicon | MLX |

---

## 9. Matriz de Features

| Feature | Keras 3 | PyTorch | JAX | TF |
|---------|---------|---------|-----|-----|
| API alto nivel | ✅ | ❌ | ❌ | ✅ |
| GPU support | ✅ | ✅ | ✅ | ✅ |
| TPU support | ✅ | ⚠️ | ✅ | ✅ |
| Mobile | ✅ | ⚠️ | ⚠️ | ✅ |
| Easy debugging | ✅ | ✅ | ⚠️ | ✅ |
| Research use | ⚠️ | ✅ | ✅ | ⚠️ |
| Production | ✅ | ✅ | ⚠️ | ✅ |
| Docs calidad | ✅ | ✅ | ⚠️ | ✅ |

Leyenda: ✅ Excelente | ⚠️ Limitado | ❌ No disponible/nativo

---

## 10. Migración entre Frameworks

### PyTorch → Keras
```python
# PyTorch
model = nn.Sequential(nn.Linear(10, 5), nn.ReLU())

# Keras equivalente
model = Sequential([Dense(5, activation='relu', input_shape=(10,))])
```

### Keras → PyTorch
```python
# Keras
model.add(Dense(64, activation='relu'))

# PyTorch
nn.Linear(64, 64), nn.ReLU()
```

### PyTorch → JAX (con Flax)
```python
# PyTorch
self.fc = nn.Linear(10, 5)

# Flax
nn.Dense(features=5)
```

---

## 11. Comparativa de Rendimiento

### Benchmarks aproximados (entrenamiento)

| Framework | GPU | Batch Size | Tiempo/epoch (MNIST) | Tiempo/epoch (CIFAR-10) |
|-----------|-----|------------|---------------------|------------------------|
| Keras 3 (TF) | RTX 3080 | 128 | ~2s | ~15s |
| Keras 3 (JAX) | RTX 3080 | 128 | ~1.5s | ~10s |
| Keras 3 (PyTorch) | RTX 3080 | 128 | ~1.8s | ~12s |
| PyTorch | RTX 3080 | 128 | ~1.8s | ~12s |
| JAX (JIT) | RTX 3080 | 128 | ~1.5s | ~10s |
| JAX (JIT) | TPU v4 | 512 | ~0.5s | ~3s |

### Factores que afectan el rendimiento

| Factor | Impacto | Recomendación |
|--------|---------|---------------|
| **JIT compilation** | +30-50% | Usar @jit en JAX |
| **Mixed precision** | +30% | float16 en GPUs modernas |
| **Batch size** | Variable | Aumentar hasta OOM |
| **Data loading** | +20% | DataLoader con workers>0 |
| **cuDNN auto-tune** | +10% | `torch.backends.cudnn.benchmark = True` |

### Cuándo es más rápido cada uno

```
Rápido para prototipado:
├── Keras 3: Código más simple, menos optimización needed
└── PyTorch Lightning: abstracts boilerplate

Rápido para entrenamiento:
├── JAX con TPU: Mejor en TPUs
├── PyTorch + DDP: Mejor en multi-GPU
└── JAX + pmap: Mejor en multi-GPU (más control)

Rápido para inferencia:
├── TorchScript + optimization: Mejor en producción
├── TensorRT: Mejor en NVIDIA GPUs
└── ONNX + ONNX Runtime: Multi-plataforma
```

### Tips de optimización

```python
# PyTorch
torch.backends.cudnn.benchmark = True  # Auto-tune
torch.set_float32_matmul_precision('high')

# JAX
x = jax.jit(x)  # Siempre JIT
x = jax.block_until_ready(x)  # Medir tiempo

# Keras 3
keras.mixed_precision.set_global_policy('mixed_float16')
```

---

## 12. Conclusión

- **Keras 3**: Mejor para aprender y prototipado rápido
- **PyTorch**: Estándar para investigación y producción media
- **TensorFlow**: Líder para deployment enterprise
- **JAX/Flax**: Máximo rendimiento, investigación puntera

La elección depende de tu caso de uso específico, experiencia previa y requisitos del proyecto.
