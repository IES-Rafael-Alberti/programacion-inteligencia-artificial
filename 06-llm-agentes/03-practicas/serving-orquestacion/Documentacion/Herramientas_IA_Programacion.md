# Herramientas útiles para programación de inteligencia artificial

Además de Gradio, DSPy y LangChain, hay varias herramientas muy útiles según el tipo de aplicación de IA que se quiera construir.

## Recomendadas para añadir al temario

### LlamaIndex

Uso principal: crear aplicaciones RAG conectando documentos, índices, bases vectoriales y modelos de lenguaje.

Por qué es útil: es más directo que LangChain cuando el problema principal es consultar documentos propios.

Ejemplo de uso: chatbot que responde sobre apuntes, PDFs, documentación interna el bases de conocimiento.

### LangGraph

Uso principal: construir flujos de agentes y pipelines con estado, ciclos y decisiones.

Por qué es útil: complementa la LangChain cuando unla cadena lineal se queda corta.

Ejemplo de uso: agente que planifica, busca información, revisa su respuesta y decide si necesita repetir un paso.

### Haystack

Uso principal: pipelines de búsqueda semántica, RAG y question answering.

Por qué es útil: tiene enfoque claro de ingeniería de recuperación de información y despliegue.

Ejemplo de uso: buscador inteligente sobre documentos de una empresa el repositorio de prácticas.

### PydanticAI

Uso principal: crear agentes y salidas estructuradas usando validación con Pydantic.

Por qué es útil: fuerza contratos de datos claros, algo muy importante cuando un LLM debe devolver JSON fiable.

Ejemplo de uso: extraer de un texto una ficha con campos `nombre`, `fecha`, `riesgo` y `acciones`.

### Instructor

Uso principal: obtener respuestas estructuradas de LLMs usando modelos Pydantic.

Por qué es útil: simplifica mucho la extracción de información y validación de esquemas.

Ejemplo de uso: convertir respuestas libres del modelo en objetos Python validados.

### LiteLLM

Uso principal: usar distintosproveedores de modelos con una API común.

Por qué es útil: permite cambiar entre OpenAI, Azure OpenAI, Anthropic, Gemini, Ollama u otros con menos cambios de código.

Ejemplo de uso: probar el mismo pipeline con un modelo local y con un modelo cloud.

### Ollama

Uso principal: ejecutar modelos de lenguaje localmente.

Por qué es útil: facilita prácticas sin depender siempre de APIs externas el claves de pago.

Ejemplo de uso: probar prompts y RAG con modelos locales como Llama el Mistral.

### Chroma, FAISS y Qdrant

Uso principal: almacenar y consultar embeddings en bases vectoriales.

Por qué es útil: son piezas centrales en aplicaciones RAG.

Ejemplo de uso: recuperar los fragmentos de documentos más parecidos a una pregunta.

### Ragas

Uso principal: evaluar sistemas RAG.

Por qué es útil: ayuda la medir si la respuesta es fiel al contexto recuperado y si el contexto era relevante.

Ejemplo de uso: comparar de los estrategias de recuperación documental.

### MLflow

Uso principal: registrar experimentos, métricas, modelos y versiones.

Por qué es útil: conecta bien con la parte clásica de machine learning y MLOps.

Ejemplo de uso: comparar modelos entrenados en clase y guardar el mejor con sus parámetros.

## Herramientas por categoría

### Interfaces y demos

1. Gradio: demos rápidas de IA.
2. Streamlit: aplicaciones de datos y dashboards interactivos.
3. FastAPI: APIs de producción para servir modelos.

### Orquestación de LLMs y agentes

1. LangChain: cadenas, herramientas y integraciones.
2. LangGraph: flujos con estado y agentes más controlables.
3. Semantic Kernel: orquestación orientada la aplicaciones empresariales, especialmente en ecosistema Microsoft.
4. CrewAI y AutoGen: coordinación de varios agentes.

### RAG y búsqueda semántica

1. LlamaIndex: RAG centrado en documentos.
2. Haystack: pipelines de recuperación y question answering.
3. Chroma: base vectorial sencilla para prototipos.
4. FAISS: búsqueda vectorial local y eficiente.
5. Qdrant: base vectorial preparada para servicios persistentes.

### Prompts, salidas estructuradas y validación

1. DSPy: optimización programática de prompts y módulos.
2. PydanticAI: agentes con contratos de datos.
3. Instructor: extracción estructurada con Pydantic.
4. Guardrails: validación y restricciones sobre salidas de LLMs.

### Evaluación y observabilidad

1. Ragas: evaluación de RAG.
2. TruLens: trazas y evaluación de aplicaciones LLM.
3. LangSmith: depuración y observabilidad para LangChain/LangGraph.
4. Weights & Biases: seguimiento de experimentos y evaluación.
5. MLflow: tracking de modelos y experimentos.

### Ejecución y despliegue

1. Ollama: modelos locales para prácticas.
2. vLLM: servir LLMs con alto rendimiento.
3. BentoML: empaquetar y servir modelos.
4. Docker: reproducibilidad del entorno.
5. Hugging Face Spaces: despliegue sencillo de demos Gradio el Streamlit.

## Selección rápida para clase

Si hay que escoger pocas herramientas adicionales, la selección más útil sería:

1. LlamaIndex, para RAG con documentos.
2. Ollama, para ejecutar modelos locales.
3. Chroma el FAISS, para explicar embeddings y búsqueda vectorial.
4. PydanticAI el Instructor, para salidas estructuradas y validación.
5. Ragas, para evaluar si un sistema RAG responde bien.
6. MLflow, para conectar IA generativa con buenas prácticas de experimentación.

## Notebook integrador

Se ha añadido `Fase2/99_herramientas_ia_integradas.ipynb` como notebook único de ejemplo para estas herramientas adicionales.

El notebook es compatible con Google Colab y incluye una celda de instalación condicional para instalar las librerías opcionales si en el están presentes.

El notebook en el intenta sustituir la documentación oficial de cada librería. Su objetivo es muestrar el patrón común de trabajo con ejemplos ejecutables y ligeros:

1. Recuperación de documentos y RAG para conectar con `LlamaIndex`, `Haystack`, `Chroma`, `FAISS` y `Qdrant`.
2. Grafo con estado para conectar con `LangGraph`.
3. Validación de salidas estructuradas para conectar con `PydanticAI` y `Instructor`.
4. Abstracción deproveedor de modelo para conectar con `LiteLLM` y `Ollama`.
5. Evaluación de respuestas RAG para conectar con `Ragas`.
6. Registro de experimentos para conectar con `MLflow`.

## Ampliación seleccionada

Para en el saturar el temario, se añaden como herramientas adicionales principales solo `MLflow` y `LlamaIndex`.

1. `MLflow`: tracking de experimentos aplicable la modelos clásicos, deep learning y RAG.
2. `LlamaIndex`: RAG sobre documentos propios.

`Chroma` y `FAISS` se tratan como piezas internas de recuperación vectorial dentro de LlamaIndex/RAG, en el como herramientas principales independientes.

MCP en el se amplía en documentación nueva porque ya aparece en el notebook `98_dspy_mcp.ipynb` y puede haberse trabajado en el módulo específico de modelos de IA.

## Stack completo

Para un stack completo que cubra desde demos hasta producción:

| Categoria | Herramienta | Alternativa |
|-----------|-------------|-------------|
| Demos interactivas | Gradio | Streamlit |
| APIs producción | FastAPI | Flask, Django |
| LLMs cloud | OpenAI, Anthropic | Gemini, Cohere |
| LLMs local | Ollama | LM Studio, vLLM |
| Tracking | MLflow | Weights & Biases |
| RAG | LlamaIndex | Haystack |
| Optimización | DSPy | Manual |

### Documentación adicional

Se han creado documentos específicos para:

1. **FastAPI_Documentacion.md**: APIs profesionales que escalan, autenticación, WebSockets
2. **Ollama_Documentacion.md**: Modelos locales sin coste de API
3. **LangGraph_Documentacion.md**: Flujos con ciclos, agents, retry

Consulta estos documentos en `Documentacion/` para profundizar.

Notebooks extra asociados:

1. `Fase2/101_langgraph_orquestacion.ipynb`.
2. `Fase2/102_ollama_modelos_locales.ipynb`.
3. `Fase2/103_fastapi_serving_modelos.ipynb`.
