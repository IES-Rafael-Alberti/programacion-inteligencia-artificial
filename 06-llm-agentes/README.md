# 06-llm-agentes

## Propósito
Cubre interfaces de API, serving de modelos, orquestación de agentes, RAG avanzado, optimización de LLMs, y herramientas de IA (Gradio, LangChain, DSPy, LangGraph, MLflow, LlamaIndex, FastAPI, Ollama).

## Ruta canónica del alumnado

| Paso | Material |
|---|---|
| Empieza aquí | `01-teoria/` como consulta dirigida por el profesorado; no es necesario recorrer todas las herramientas. |
| Práctica canónica | Ruta compuesta: [`100_mlflow_llamaindex_rag.ipynb`](03-practicas/100_mlflow_llamaindex_rag.ipynb) sirve como base de RAG, evaluación y trazabilidad; [`103_fastapi_serving_modelos.ipynb`](03-practicas/103_fastapi_serving_modelos.ipynb) muestra por separado un patrón FastAPI sobre Iris que el alumnado debe adaptar a su propia solución. `99_herramientas_ia_integradas.ipynb` es una introducción. |
| Entrega y evaluación | Un proyecto integrado por el alumnado: flujo RAG trazable, API o interfaz adaptada a ese flujo, instrucciones reproducibles y evidencias de consulta, evaluación y prueba del servicio. Los notebooks `100` y `103` son materiales de partida; el `103` no expone el RAG del `100`. Se corrige con [`04-evaluacion/rubrica.md`](04-evaluacion/rubrica.md) y [`04-evaluacion/checklist-entrega.md`](04-evaluacion/checklist-entrega.md). |
| Entorno real | Cada notebook contiene su preparación para Colab y el comando de dependencias opcionales para local. La entrega debe documentar el entorno realmente usado; no existe un entorno Pixi `ud6` en el manifiesto raíz. |

## Materiales incluidos
- **Material reorganizado desde UD4**: NLP clásico, embeddings, transformers, BERT, spaCy, tareas y ejemplos asociados se han movido aquí desde `04-deep-learning/` para que UD4 quede como deep learning base. Los modelos y zips de transformers quedan en `90-archivo/nlp-transformers-ud4/`.
- **01-teoria**: Documentación de herramientas (DSPy, FastAPI, Gradio, LangChain, LangGraph, LlamaIndex, MLflow, Ollama) + guías de notebooks
- **02-ejemplos**: Notebooks básicos de Gradio, LangChain, DSPy (con soluciones y tests)
- **03-practicas**: Notebooks avanzados (Gradio, LangChain pipeline, DSPy+MCP, herramientas integradas, MLflow+LlamaIndex RAG, LangGraph, Ollama, FastAPI). Incluye la subcarpeta `serving-orquestacion/` como material de apoyo
- **04-evaluacion**: Cuestionarios GIFT (interfaces API serving, orquestación RAG optimización)
- **05-recursos**: Material complementario, incluyendo refuerzo opcional de MCP con test inicial
- **90-archivo**: Material histórico no activo

## Prácticas asociadas
- **Canónica:** proyecto del alumnado construido desde la base RAG/trazabilidad del notebook `100` y adaptando el patrón FastAPI independiente del notebook `103`.
- **Introducción:** `99_herramientas_ia_integradas.ipynb`, con simulaciones para reconocer los patrones antes de implementar la entrega.
- **Específicas u opcionales:** Gradio, LangChain, DSPy/MCP, LangGraph y Ollama, según el foco que indique el profesorado.

## Pendientes
- El refuerzo MCP de `05-recursos/mcp-refuerzo/` se activa solo si el diagnóstico inicial del grupo lo aconseja; no bloquea la ruta canónica.
