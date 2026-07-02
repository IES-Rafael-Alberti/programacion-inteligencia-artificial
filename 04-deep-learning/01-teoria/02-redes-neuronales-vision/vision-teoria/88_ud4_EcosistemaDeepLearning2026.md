---
editor_options: 
  markdown: 
    wrap: 72
---

# Mapa del ecosistema moderno de IA (2026)

```text
Aplicaciones de IA 
│ 
├─ LangChain 
├─ DSPy 
├─ Gradio / Streamlit 
│
Motores de inferencia 
│ 
├─ vLLM 
├─ TensorRT 
├─ ONNX Runtime 
│
Entrenamiento a gran escala 
│ 
├─ DeepSpeed 
├─ FSDP 
├─ Ray 
│ Librerías de modelos 
│ 
├─ HuggingFace Transformers 
├─ timm 
├─ SuperGradients 
│
Frameworks de entrenamiento 
│ 
├─ PyTorch Lightning 
├─ fastai 
│ APIs de alto nivel 
│ 
├─ Keras 
│ Frameworks base 
│ 
├─ PyTorch 
├─ JAX 
└─ TensorFlow 
│ Hardware 
│ GPU / TPU / CPU
```
## 1. Hardware y aceleradores

![Image](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/04/a-server-rack-with-multiple-graphics-car_1697ruHRSMSTRoErrfi3cA_cJzZv9c1QISLI8olAbopcw.png)

![Image](https://storage.googleapis.com/gweb-cloudblog-publish/images/TPU_v5L_Pod_-_Front_View_-_Web.max-2600x2600.jpg)

![Image](https://res.cloudinary.com/momentum-media-group-pty-ltd/image/upload/v1702000762/Cyber%20Daily/AMD-Instinct-MI300X_csc_dyni8v.jpg)

![Image](https://www.amd.com/content/dam/amd/en/images/products/data-centers/2325906-amd-instinct-mi300x-product.jpg)

Base física donde se ejecutan los modelos.

Principales plataformas:

-   **NVIDIA** GPUs (A100, H100, etc.)
-   **Google** TPUs
-   **AMD** MI300
-   CPUs optimizadas para AI (AVX512, AMX)

Esto determina:

-   velocidad de entrenamiento
-   tamaño máximo del modelo
-   coste energético.

------------------------------------------------------------------------

# 2. Frameworks de bajo nivel

Los frameworks que gestionan:

-   tensores
-   autograd
-   kernels GPU
-   compilación

Los principales son:

-   **PyTorch**
-   **TensorFlow**
-   **JAX**

### Filosofías

| Framework  | Filosofía                            |
|------------|--------------------------------------|
| PyTorch    | imperativo, flexible                 |
| TensorFlow | pipeline industrial                  |
| JAX        | programación funcional + compilación |

Hoy en día:

-   **PyTorch domina en investigación**
-   **JAX domina en algunos laboratorios avanzados**
-   **TensorFlow se usa menos en investigación**

------------------------------------------------------------------------

# 3. Frameworks de entrenamiento

Aquí aparecen los frameworks que **organizan el training loop** y APIs
de alto nivel.

Principales ejemplos:

-   **PyTorch Lightning**
-   **fastai**
-   **SuperGradients**
-   **Keras**

Su función es simplificar:

-   training loops
-   callbacks
-   logging
-   checkpoints
-   distributed training.

Ejemplo conceptual:

```         
Modelo
 ↓
Training framework
 ↓
PyTorch
 ↓
CUDA
```

## El lugar de Keras

Keras es una API de alto nivel que se ejecuta sobre TensorFlow (y ahora
también sobre PyTorch y JAX) y simplifica la creación de modelos. Es muy
popular para:

-   prototipado rápido
-   educación
-   aplicaciones industriales.

Keras es útil para enseñar:

-   conceptos de arquitectura de redes neuronales
-   diseño de pipelines
-   entrenamiento de redes

conceptos que podemos transferir directamente a Pytorch o JAX.

## Keras es una API universal para definir modelos, mientras que Pytorch es el **motor de cálculo**.

# 4. Librerías de modelos

Aquí viven los **modelos preentrenados y pipelines completos**.

Las más importantes:

-   **Hugging Face Transformers**
-   **timm**
-   **SuperGradients**

Proporcionan:

-   arquitecturas
-   pesos preentrenados
-   datasets
-   pipelines de entrenamiento.

Ejemplo:

``` python
from transformers import AutoModel
```

------------------------------------------------------------------------

# 5. Frameworks de optimización y escalado

Cuando los modelos crecen aparecen herramientas para:

-   entrenar modelos enormes
-   paralelizar GPU
-   optimizar memoria

Principales:

-   **DeepSpeed**
-   **FSDP**
-   **Ray**

Se usan en:

-   entrenamiento de LLM
-   clusters GPU
-   modelos de cientos de miles de millones de parámetros.

------------------------------------------------------------------------

# 6. Frameworks de inferencia

Una vez entrenado el modelo, se necesitan motores de inferencia rápidos.

Ejemplos:

-   **vLLM**
-   **TensorRT**
-   **ONNX Runtime**

Objetivos:

-   baja latencia
-   alto throughput
-   menor consumo de memoria.

------------------------------------------------------------------------

# 7. Frameworks de aplicaciones de IA

Aquí se construyen **productos finales**.

Ejemplos:

-   **LangChain**
-   **DSPy**
-   **Gradio**
-   **Streamlit**

Se usan para:

-   agentes
-   chatbots
-   aplicaciones AI.

------------------------------------------------------------------------

# 8. Herramientas de ejecución local

Permiten ejecutar modelos localmente.

Ejemplos:

-   **Ollama**
-   **llama.cpp**
-   **MLX**

Importantes para:

-   edge computing
-   privacidad
-   desarrollo local.

------------------------------------------------------------------------

# Mapa completo simplificado

```         
Aplicaciones AI
│
├─ LangChain
├─ DSPy
├─ Gradio
│
Inferencia
│
├─ vLLM
├─ TensorRT
├─ ONNX
│
Optimización / Escalado
│
├─ DeepSpeed
├─ FSDP
├─ Ray
│
Modelos
│
├─ HuggingFace
├─ timm
├─ SuperGradients
│
Training frameworks
│
├─ Lightning
├─ fastai
│
Frameworks base
│
├─ PyTorch
├─ JAX
└─ TensorFlow
│
Hardware
│
GPU / TPU / CPU
```

------------------------------------------------------------------------

# Tendencias importantes (2025–2026)

### 1. PyTorch domina el ecosistema

La mayoría de librerías están construidas sobre PyTorch.

------------------------------------------------------------------------

### 2. HuggingFace se ha convertido en el “centro”

Proporciona:

-   modelos
-   datasets
-   tokenizers
-   pipelines.

------------------------------------------------------------------------

### 3. JAX está creciendo en investigación

Laboratorios como:

-   DeepMind
-   Google Research

lo usan mucho.

------------------------------------------------------------------------

### 4. Inferencia es el nuevo cuello de botella

Herramientas como:

-   vLLM
-   TensorRT

son cada vez más importantes.
