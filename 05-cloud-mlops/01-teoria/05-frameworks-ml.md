# Frameworks de ML en la nube

## Introducción

Los frameworks de machine learning no cambian por estar en la nube, pero sí cambia el modo de desplegarlos, escalarlos y gestionarlos. La elección del framework debe responder al tipo de problema y no solo a la plataforma.

---

## PyTorch

### ¿Qué es?

Framework de deep learning muy usado en investigación y prototipado avanzado.

### En la nube

| Servicio | Uso habitual |
|----------|--------------|
| SageMaker | Contenedores y jobs preconfigurados |
| Vertex AI | Contenedores personalizados o preconstruidos |
| Azure ML | Entornos y jobs |
| Plataformas GPU | Instalación directa por `pip` |

### Ejemplo de entrenamiento

```python
import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)
```

### Fortalezas

- Muy flexible.
- Gran comunidad.
- Muy presente en NLP y visión.

---

## TensorFlow y Keras

### ¿Qué es?

Framework maduro, muy extendido en producción y con fuerte integración histórica con el ecosistema de Google.

### En la nube

| Servicio | Uso habitual |
|----------|--------------|
| Vertex AI | Integración natural |
| SageMaker | Contenedores oficiales |
| Azure ML | Entornos y jobs |

### Ejemplo de entrenamiento

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(256, activation="relu", input_shape=(784,)),
    keras.layers.Dense(10, activation="softmax")
])
```

### Fortalezas

- Buen ecosistema para producción.
- TensorBoard y TFX como herramientas asociadas.

---

## scikit-learn

### ¿Qué es?

Biblioteca de referencia para machine learning clásico.

### Ejemplo básico

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
```

### Ventajas

- Curva de aprendizaje asequible.
- Excelente para clasificación, regresión y pipelines tabulares.
- Muy apropiado para proyectos docentes.

### Limitaciones

- No está pensado para deep learning.
- No aprovecha GPU de forma nativa.
- Escala peor en volúmenes muy grandes.

---

## Hugging Face Transformers

### ¿Qué aporta?

- Modelos preentrenados para NLP y otras tareas.
- Tokenizadores, pipelines y repositorios de modelos.
- Muy útil cuando el proyecto trabaja con texto, embeddings o transformers.

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")
```

### Opciones cloud

- Hugging Face Inference Endpoints
- SageMaker JumpStart
- Vertex AI Model Garden

---

## Otras alternativas libres y muy útiles

### XGBoost

- Software libre.
- Muy fuerte en problemas tabulares y competiciones.
- Buena opción cuando se necesita más rendimiento que con modelos básicos de scikit-learn.

### LightGBM

- Software libre.
- Especialmente útil en clasificación y regresión tabular con buen rendimiento.

### JAX

- Software libre.
- Interesante en investigación y computación numérica avanzada, aunque menos habitual en docencia básica.

---

## Comparativa

| Framework | Mejor encaje | Ventaja principal | Limitación |
|-----------|--------------|-------------------|------------|
| PyTorch | Deep learning e investigación | Flexibilidad | Mayor complejidad inicial |
| TensorFlow | Producción y pipelines | Ecosistema maduro | Menos cómodo para algunos prototipos |
| scikit-learn | ML clásico tabular | Simplicidad | No es para deep learning |
| Hugging Face | NLP y transformers | Modelos listos para usar | Dependencia de modelos preentrenados |
| XGBoost / LightGBM | Tabular con alto rendimiento | Muy competitivos | Menos adecuados para enseñanza inicial |

---

## Aplicación al proyecto

Antes de elegir un framework conviene responder:

1. ¿El problema es tabular, de texto, imagen o multimodal?
2. ¿Hace falta deep learning o basta con ML clásico?
3. ¿El equipo prioriza simplicidad o flexibilidad?
4. ¿Se entrenará desde cero, se hará ajuste fino o solo inferencia?

En muchos proyectos de aula, scikit-learn es suficiente si el problema es tabular. Para NLP o transformers, Hugging Face y PyTorch suelen tener más sentido.

---

## Recomendaciones generales

| Caso | Framework recomendado |
|------|-----------------------|
| ML clásico tabular | scikit-learn |
| ML tabular con más rendimiento | XGBoost o LightGBM |
| Deep learning general | PyTorch o TensorFlow |
| NLP con modelos modernos | Hugging Face |
| Proyecto docente sencillo | scikit-learn |
| Proyecto avanzado de investigación | PyTorch |

---

## Fuentes recomendadas

- Documentación oficial de PyTorch.
- Documentación oficial de TensorFlow y Keras.
- Documentación oficial de scikit-learn.
- Documentación oficial de Hugging Face.
- Documentación oficial de XGBoost, LightGBM y JAX.
- Documentación oficial de SageMaker, Vertex AI y Azure ML.
