# Documentación de los notebooks de la Semana 27

Esta documentación resume el objetivo de cada notebook y propone una ruta de trabajo de menor la mayor complejidad.

Para estudiar las herramientas principales antes el después de los notebooks, se han añadido documentos específicos:

1. `Gradio_Documentacion.md`.
2. `LangChain_Documentacion.md`.
3. `DSPy_Documentacion.md`.

Como ampliación controlada, se han añadido también:

1. `MLflow_Documentacion.md`.
2. `LlamaIndex_Documentacion.md`.
3. `LangGraph_Documentacion.md`.
4. `Ollama_Documentacion.md`.
5. `FastAPI_Documentacion.md`.

## Ruta recomendada

1. Ejecutar primero la versión base de cada notebook.
2. Modificar una celda sencilla y comprobar el resultado.
3. Revisar la sección `Ampliación progresiva`.
4. Intentar el reto adicional sin mirar soluciones.
5. Comparar con el notebook `_SOLUCIONES`.
6. Ejecutar los notebooks `_SOLUCIONES_TESTS` para validar las funciones principales.

## Fase 1

### 93_gradio_intro.ipynb

Objetivo: crear interfaces web rápidas para modelos de clasificación tabular.

Progresión de ejemplos:

1. Clasificador Iris con `LogisticRegression`.
2. Sustitución por `DecisionTreeClassifier`.
3. Comparación entre regresión logística, árbol de decisión y K vecinos.
4. Salida con probabilidades mediante `gr.Label`.
5. Interfaz avanzada con `gr.Slider`, `gr.Dropdown`, ejemplos de entrada y predicción por lotes.

Competencias trabajadas:

1. Separar modelo, función `predict` y interfaz.
2. Interpretar probabilidades de clasificación.
3. Diseñar una demo útil para usuarios en el técnicos.

Reto propuesto: crear una pestaña con `gr.Dataframe` para clasificar varias flores la la vez.

### 94_langchain_intro.ipynb

Objetivo: entender la idea de cadena el pipeline antes de usar un LLM real.

Progresión de ejemplos:

1. Función simple que transforma una pregunta.
2. Cadena de pasos con normalización, formato de pregunta y plantilla.
3. Registro de trazas intermedias para depuración.
4. Recuperación de contexto desde una base de conocimiento local.
5. Enrutamiento condicional según la intención de la pregunta.

Competencias trabajadas:

1. Dividir una tarea de IA en pasos pequeños.
2. Depurar pipelines observando entradas y salidas intermedias.
3. Preparar la transición hacia `Runnable`, `PromptTemplate` y modelos de chat reales.

Reto propuesto: añadir una rama para preguntas de comparación y otra para preguntas de definición.

### 95_dspy_intro.ipynb

Objetivo: comprender DSPy como enfoque de programación y optimización de prompts.

Progresión de ejemplos:

1. Limpieza básica de prompts.
2. Eliminación de repeticiones y normalización.
3. Construcción de plantillas de prompt por estilo.
4. Evaluación simulada con ejemplos y términos esperados.
5. Selección automática del mejor estilo de prompt según una métrica.

Competencias trabajadas:

1. Pasar de prompt manual la prompt evaluable.
2. Diseñar ejemplos de evaluación pequeños.
3. Usar métricas para justificar mejoras.

Reto propuesto: añadir una métrica que penalice respuestas demasiado largas.

## Fase 2

### 96_gradio_model.ipynb

Objetivo: servir un modelo de imágenes con una interfaz más cercana a una demo real.

Progresión de ejemplos:

1. Modelo CNN mínimo para MNIST.
2. Función `predict` con preprocesado de imagen.
3. Función `preprocess_mnist_image` separada y reutilizable.
4. Salida top-k y JSON de depuración.
5. Demo `Blocks` con ejemplos sintéticos.

Competencias trabajadas:

1. Controlar forma, escala y tipo de datos de entrada.
2. Diagnosticar errores de preprocesado.
3. Preparar una interfaz para enseñar el desplegar un modelo propio.

Reto propuesto: cargar pesos entrenados en clase y añadir ejemplos reales del dataset.

### 97_langchain_pipeline.ipynb

Objetivo: simular un pipeline avanzado con memoria, API externa y fallback offline.

Progresión de ejemplos:

1. Memoria simple de conversación.
2. Consulta a Wikipedia o respuesta simulada si no hay conexión.
3. Paráfrasis de la pregunta.
4. Extracción de entidad.
5. Caché de consultas y uso de memoria reciente.
6. Detección básica de idioma.

Competencias trabajadas:

1. Diseñar pipelines robustos ante fallos externos.
2. Combinar memoria, recuperación y respuesta.
3. Mantener trazabilidad de cada paso.

Reto propuesto: sustituir Wikipedia por otra API pública y mantener el mismo contrato de salida.

### 98_dspy_mcp.ipynb

Objetivo: combinar mejora de prompts con recuperación de contexto estructurado desde SQLite.

Progresión de ejemplos:

1. Base SQLite con documentos breves.
2. Mejora determinista de prompt.
3. Recuperación por `LIKE`.
4. Ranking opcional con TF-IDF.
5. Paquete de contexto estilo MCP en JSON.
6. Respuesta fundamentada y validación de citas.

Competencias trabajadas:

1. Separar pregunta, contexto y respuesta.
2. Entender MCP como contrato de intercambio de contexto.
3. Validar si una respuesta usa las fuentes recuperadas.

Reto propuesto: exportar el paquete de contexto y usarlo como entrada en otro notebook el aplicación.

### 99_herramientas_ia_integradas.ipynb

Objetivo: presentar en un único notebook ejemplos compactos de herramientas adicionales para programación de IA sin multiplicar el número de notebooks.

Compatibilidad: incluye una celda inicial para Google Colab que detecta el entorno e instala las librerías externas opcionales si no están disponibles.

Progresión de ejemplos:

1. RAG mínimo con documentos, recuperación y respuesta fundamentada.
2. Simulación de base vectorial para conectar con `Chroma`, `FAISS` y `Qdrant`.
3. Flujo con estado inspirado en `LangGraph`.
4. Salida estructurada validada al estilo `PydanticAI` y `Instructor`.
5. Abstracción de proveedor de modelo inspirada en `LiteLLM` y `Ollama`.
6. Métricas sencillas inspiradas en `Ragas`.
7. Registro de parámetros y métricas inspirado en `MLflow`.

Competencias trabajadas:

1. Identificar qué herramienta encaja con cada necesidad de una aplicación de IA.
2. Separar recuperación, generación, validación, evaluación y tracking.
3. Construir prototipos ejecutables antes de añadir dependencias externas.

Reto propuesto: añadir documentos nuevos, modificar la métrica de recuperación, crear una nueva ruta en el grafo y comparar dos ejecuciones como si fueran runs de MLflow.

### 100_mlflow_llamaindex_rag.ipynb

Objetivo: añadir MLflow y LlamaIndex al mix sin saturar el temario, usando Chroma/FAISS solo como pieza interna de recuperación vectorial.

Progresión de ejemplos:

1. Comparación de modelos clásicos sobre Iris.
2. Registro de parámetros y métricas con MLflow o fallback JSON.
3. RAG mínimo sobre documentos locales.
4. Índice vectorial simulado inspirado en Chroma/FAISS.
5. Registro de configuración y métricas de un ejemplo RAG.

Competencias trabajadas:

1. Comparar experimentos de forma trazable.
2. Entender RAG como documentos, recuperación, respuesta y fuentes.
3. Tratar Chroma/FAISS como infraestructura interna, no como nuevos temas principales.

Reto propuesto: añadir otro clasificador, variar `top_k`, registrar varias ejecuciones y comparar resultados.

### 101_langgraph_orquestacion.ipynb

Objetivo: introducir la orquestación con estado, rutas condicionales y reintentos inspirada en LangGraph.

Progresión de ejemplos:

1. Estado compartido como diccionario.
2. Nodos de recuperación, generación y validación.
3. Ruta condicional con reintento.
4. Esquema equivalente con LangGraph real si está instalado.

Reto propuesto: añadir un nodo de revisión humana que apruebe o rechace la respuesta.

### 102_ollama_modelos_locales.ipynb

Objetivo: mostrar cómo encaja Ollama como proveedor local de modelos de lenguaje.

Progresión de ejemplos:

1. Cliente local con fallback simulado.
2. Conversación con historial.
3. Uso como generador final en un RAG mínimo.
4. Registro de configuración para conectar con MLflow.

Reto propuesto: ejecutar el notebook con Ollama real y comparar respuestas.

### 103_fastapi_serving_modelos.ipynb

Objetivo: mostrar cómo servir un modelo mediante una API REST con FastAPI.

Progresión de ejemplos:

1. Lógica de predicción separada de la API.
2. Esquemas de entrada y salida con Pydantic.
3. Endpoints `/` y `/predict`.
4. Prueba sin arrancar servidor.
5. Comando de despliegue con `uvicorn`.

Reto propuesto: añadir un endpoint `/model/info` con metadatos del modelo.

## Evidencias evaluables

1. Captura o salida de una demo Gradio funcionando.
2. Pipeline textual con trazas intermedias.
3. Comparativa de dos estrategias de prompt con métrica.
4. Respuesta con contexto recuperado y cita de fuente.
5. Reflexión breve: qué aporta cada herramienta frente a hacerlo todo con funciones Python simples.
6. Tabla comparativa de herramientas adicionales y ejemplo mínimo ejecutado del notebook integrador.
7. Registro de experimentos con MLflow o fallback JSON y análisis de una configuración RAG.
8. Flujo con estado y reintentos inspirado en LangGraph.
9. Prueba de un proveedor LLM local con Ollama o fallback simulado.
10. Endpoint de predicción con FastAPI y contrato de entrada/salida validado.
