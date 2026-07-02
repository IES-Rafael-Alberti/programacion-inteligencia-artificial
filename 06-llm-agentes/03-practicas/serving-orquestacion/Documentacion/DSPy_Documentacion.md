# DSPy: documentación práctica

DSPy es un framework para programar y optimizar sistemas basados en modelos de lenguaje. Su idea principal es pasar de escribir prompts manualmente a declarar tareas, ejemplos, métricas y módulos que pueden evaluarse y mejorarse de forma sistemática.

## Por qué no es solo prompting

Con prompting manual se escribe una instrucción, se prueba con algunos casos y se modifica a mano. DSPy propone un enfoque más parecido al aprendizaje automático: definir una tarea, preparar ejemplos, medir resultados y optimizar.

| Aspecto | Prompting manual | DSPy |
|---|---|---|
| Unidad principal | Prompt | Módulo |
| Entrada/salida | Implícita | Declarada con signatures |
| Evaluación | A ojo | Métricas programables |
| Mejora | Manual | Optimización automática |
| Reproducibilidad | Baja | Alta |

## Componentes principales

### Signatures

Una `Signature` define el contrato de entrada y salida de una tarea.

```python
import dspy

class AnswerQuestion(dspy.Signature):
    """Responde una pregunta usando el contexto proporcionado."""
    question = dspy.InputField()
    context = dspy.InputField()
    answer = dspy.OutputField()
```

### Modules

Un módulo encapsula una parte del sistema. Puede contener una llamada al modelo, recuperación de contexto o varios pasos combinados.

```python
class QAModule(dspy.Module):
    def __init__(self):
        self.generate = dspy.Predict(AnswerQuestion)

    def forward(self, question, context):
        return self.generate(question=question, context=context)
```

### Examples

Los ejemplos permiten evaluar si una estrategia funciona.

```python
trainset = [
    dspy.Example(
        question="¿Qué es overfitting?",
        answer="Es cuando un modelo memoriza el entrenamiento y generaliza mal.",
    ).with_inputs("question")
]
```

### Metrics

Una métrica puntúa la calidad de una salida.

```python
def contains_expected_terms(example, prediction, trace=None):
    expected = ["entrenamiento", "generaliza"]
    answer = prediction.answer.lower()
    return all(term in answer for term in expected)
```

### Optimizers

Los optimizadores prueban variantes y seleccionan instrucciones o ejemplos que mejoran la métrica.

```python
optimizer = dspy.BootstrapFewShot(metric=contains_expected_terms)
# compiled = optimizer.compile(QAModule(), trainset=trainset)
```

## Ejemplo conceptual completo

```python
import dspy

class ClassifyIntent(dspy.Signature):
    """Clasifica la intención de un mensaje."""
    message = dspy.InputField()
    intent = dspy.OutputField(desc="consulta, queja o saludo")

class IntentClassifier(dspy.Module):
    def __init__(self):
        self.classify = dspy.Predict(ClassifyIntent)

    def forward(self, message):
        return self.classify(message=message)

def metric(example, pred, trace=None):
    return example.intent.lower() == pred.intent.lower()
```

## DSPy en RAG

DSPy puede combinarse con recuperación de contexto. Una arquitectura típica sería:

1. Recuperar documentos relevantes.
2. Pasar pregunta y contexto a un módulo DSPy.
3. Generar respuesta.
4. Evaluar si la respuesta usa el contexto y cumple el formato.
5. Optimizar el módulo con ejemplos.

## Diferencias con LangChain

| Herramienta | Foco |
|---|---|
| LangChain | Componer cadenas, herramientas, memoria y agentes |
| DSPy | Optimizar el comportamiento del LLM con ejemplos y métricas |
| LlamaIndex | Construir RAG sobre documentos propios |

## Buenas prácticas

1. Empezar con pocas signatures y ejemplos claros.
2. Definir métricas simples antes de optimizar.
3. Separar datos de entrenamiento, validación y prueba cuando el proyecto crezca.
4. No optimizar contra un único ejemplo.
5. Penalizar salidas que incumplen restricciones importantes, como longitud excesiva o ausencia de citas.

## Errores frecuentes

1. Pensar que DSPy es solo una colección de prompts.
2. Usar métricas que no reflejan el objetivo real.
3. No revisar los ejemplos de entrenamiento.
4. Optimizar una tarea sin conjunto de evaluación.
5. Usarlo para una demo simple donde un prompt fijo sería suficiente.

## Relación con los notebooks

### `Fase1/95_dspy_intro.ipynb`

Simula estilos de prompt, respuestas y métricas sin depender de APIs externas.

### `Fase2/98_dspy_mcp.ipynb`

Combina mejora de prompts con recuperación de contexto desde SQLite y validación de citas.

## Cuándo usar DSPy

Usa DSPy cuando tengas una tarea repetible, ejemplos de evaluación y necesidad real de mejorar prompts o módulos de forma medible.

No es necesario para una llamada puntual a un LLM o una demo básica sin evaluación.

## Instalación

```bash
pip install dspy
```

Documentación oficial: https://dspy.ai/
