# Guía de ONNX para Deployment

ONNX (Open Neural Network Exchange) es un formato abierto para representar modelos de deep learning, permitiendo interoperabilidad entre frameworks.

---

## 1. ¿Qué es ONNX?

- **Formato estándar** para modelos de ML
- **Interoperabilidad**: PyTorch → TensorFlow → Keras → etc.
- **Optimización**: ONNX Runtime
- **Deployment**: Servidores, edge, mobile

---

## 2. Instalación

```bash
pip install onnx
pip install onnxruntime
pip install onnxoptimizer
pip install onnxsim
```

---

## 3. Exportar desde PyTorch

### Basic

```python
import torch

model = MyModel()
model.eval()

dummy_input = torch.randn(1, 3, 224, 224)

torch.onnx.export(
    model,
    dummy_input,
    'model.onnx',
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={
        'input': {0: 'batch_size'},
        'output': {0: 'batch_size'}
    }
)
```

### Con TorchScript

```python
# Tracing
traced = torch.jit.trace(model, dummy_input)
torch.onnx.export(
    traced,
    dummy_input,
    'model_traced.onnx',
    input_names=['input'],
    output_names=['output']
)
```

### Con control flow (Scripting)

```python
# Scripting para modelos con if/for
scripted = torch.jit.script(model)
torch.onnx.export(
    scripted,
    dummy_input,
    'model_scripted.onnx'
)
```

---

## 4. Exportar desde TensorFlow/Keras

```python
import tensorflow as tf

model = tf.keras.models.load_model('model.h5')

# Converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS
]
converter._experimental_lower_tensor_list_ops = False
tflite_model = converter.convert()

# Guardar
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```

### TensorFlow → ONNX

```python
# pip install tf2onnx
import tf2onnx

model = tf.keras.models.load_model('model.h5')
spec = (tf.TensorSpec((None, 784), tf.float32, name='input'),)

onnx_model, _ = tf2onnx.convert.from_keras(
    model,
    input_signature=spec,
    output_path='model.onnx'
)
```

---

## 5. Exportar desde JAX/Flax

```python
# pip install jax2tf
import jax2tf

# Convertir parámetros a función
model_fn = lambda params, x: model.apply({'params': params}, x)

# Convertir
converter = jax2tf.convert(model_fn, params, (jnp.ones((1, 784)),))
onnx_model = converter.onnx_model()

# Guardar
onnx.save(onnx_model, 'model.onnx')
```

---

## 6. Exportar desde ONNX

### Verificar

```python
import onnx

model = onnx.load('model.onnx')
onnx.checker.check_model(model)
print(onnx.helper.printable_graph(model.graph))
```

### Optimizar

```python
import onnxoptimizer

optimized_model = onnxoptimizer.optimize(
    'model.onnx',
    ['eliminate_deadend', 'eliminate_identity', 'fuse_bn_into_conv']
)
onnx.save(optimized_model, 'model_optimized.onnx')
```

### Simplificar

```python
# pip install onnxsim
import onnxsim

model = onnx.load('model.onnx')
simplified, check = onnxsim.simplify(model)
onnx.save(simplified, 'model_simple.onnx')
```

---

## 7. Inferencia con ONNX Runtime

### Basic

```python
import onnxruntime as ort
import numpy as np

# Cargar modelo
session = ort.InferenceSession('model.onnx')

# Input
input_data = np.random.randn(1, 3, 224, 224).astype(np.float32)

# Inferencia
output = session.run(None, {'input': input_data})
print(output[0].shape)
```

### Optimizado (GPU)

```python
# Sesión con GPU
session_options = ort.SessionOptions()
session_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL

session = ort.InferenceSession(
    'model.onnx',
    sess_options=session_options,
    providers=['CUDAExecutionProvider', 'CPUExecutionProvider']
)
```

### Probabilities

```python
# Obtener info de inputs/outputs
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

result = session.run([output_name], {input_name: input_data})
probabilities = result[0][0]  # Softmax output
predicted_class = np.argmax(probabilities)
```

---

## 8. Deployment en Producción

### REST API con FastAPI

```python
from fastapi import FastAPI
import onnxruntime as ort
import numpy as np

app = FastAPI()
session = ort.InferenceSession('model.onnx')

@app.post('/predict')
def predict(data: list):
    input_data = np.array(data, dtype=np.float32)
    result = session.run(None, {'input': input_data})
    return {'prediction': result[0].tolist()}
```

### Docker

```python
# Dockerfile
FROM python:3.9
RUN pip install onnxruntime
COPY model.onnx /model.onnx
COPY app.py /app.py
CMD ["python", "app.py"]
```

### Edge (iOS/Android)

```python
# iOS: usar CoreML para inferencia
# ONNX → CoreML: pip install onnxmltools

import onnxmltools
coreml_model = onnxmltools.convert.convert_onnx_to_coreml(onnx_model)
coreml_model.save('model.mlmodel')

# Android: usar ONNX Mobile Runtime
# app/build.gradle: implementation 'ai.onnxruntime:onnx-mobile:1.14.0'
```

---

## 9. Troubleshooting

### Problemas comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Unsupported operator | Op no soportada | Usar opset compatible |
| Shape mismatch | Input shape | Especificar dynamic_axes |
| ExecutionProvider not found | Sin GPU | Instalar onnxruntime-gpu |
| RuntimeError | Input type | Convertir a numpy tipo correcto |

### Depurar

```python
# Ver operaciones del modelo
import onnx
model = onnx.load('model.onnx')

for node in model.graph.node:
    print(f"{node.name}: {node.op_type} -> {node.output}")

# Probar con input específico
import onnxruntime as ort
session = ort.InferenceSession('model.onnx')

# Habilitar verbose
session_options = ort.SessionOptions()
session_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
```

---

## 10. Frameworks Soportados

| Framework | Exportar a ONNX |
|-----------|-----------------|
| PyTorch | ✅ nativamente |
| TensorFlow | ✅ tf2onnx |
| Keras | ✅ tf2onnx |
| JAX | ✅ jax2tf |
| MXNet | ✅ nativamente |
| Scikit-learn | ✅ skl2onnx |
| CoreML | ✅ onnxmltools |

---

## 11. Recursos

- [ONNX Documentation](https://onnx.ai/documentation/)
- [ONNX Runtime](https://onnxruntime.ai/)
- [ONNX Tutorials](https://github.com/onnx/tutorials)
- [ONNX Model Zoo](https://github.com/onnx/models)
