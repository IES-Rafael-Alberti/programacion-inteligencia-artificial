# Ejemplos de stacks típicos de herramientas para IA

## Introducción

El objetivo de este documento no es dar una arquitectura única correcta, sino mostrar combinaciones habituales de herramientas. Así el alumnado puede ver cómo encajan categorías distintas en un proyecto real.

---

## Stack 1: RAG sencillo para documentación

### Componentes

- Almacenamiento: S3, Blob o carpeta local
- Preparación de datos: Polars o pandas
- Embeddings: OpenAI o Cohere
- Base vectorial: Chroma o Qdrant
- Orquestación: LlamaIndex o LangChain
- LLM: OpenAI, Anthropic o Google
- Evaluación: Promptfoo o Ragas

### Flujo

```text
Documentos -> limpieza y partición -> embeddings -> base vectorial -> recuperación -> LLM -> respuesta
```

### Cuándo encaja bien

- Chat sobre apuntes o documentación.
- Proyectos finales con base documental pequeña o media.

---

## Stack 2: RAG documental más robusto

### Componentes

- Almacenamiento: S3 o MinIO
- Procesamiento: Polars
- Recuperación: búsqueda híbrida o jerárquica
- Herramienta documental: Haystack, LlamaIndex o PageIndex
- LLM: OpenAI, Anthropic o modelo abierto servido con vLLM
- Evaluación: Ragas
- Observabilidad: Arize Phoenix o LangSmith

### Flujo

```text
PDFs largos -> índice estructurado o híbrido -> recuperación -> reranking opcional -> LLM -> respuesta con citas
```

### Cuándo encaja bien

- Documentación técnica extensa.
- Informes largos.
- Casos donde el chunking simple da malos resultados.

---

## Stack 3: ML clásico tabular

### Componentes

- Datos: pandas, Polars o DuckDB
- Almacenamiento: Parquet en S3, GCS o local
- Framework: scikit-learn o XGBoost
- Compute: EC2, Vertex AI o máquina local
- MLOps: MLflow
- Despliegue: FastAPI, BentoML o endpoint gestionado

### Flujo

```text
Datos tabulares -> limpieza -> entrenamiento -> registro de experimento -> despliegue -> predicción
```

### Cuándo encaja bien

- Clasificación, regresión, recomendación sencilla.
- Proyectos de aula con datos estructurados.

---

## Stack 4: LLM con modelo abierto

### Componentes

- Modelo: Mistral, Llama o similar
- Serving: Ollama para pruebas o vLLM para API
- Orquestación: LangChain o PydanticAI
- Evaluación: Promptfoo o DeepEval
- Observabilidad: Helicone o Arize Phoenix

### Flujo

```text
Prompt o documento -> modelo abierto servido localmente o en GPU -> respuesta -> evaluación
```

### Cuándo encaja bien

- Proyectos con preocupación por privacidad.
- Casos donde se quiere aprender serving.
- Comparación entre API cerrada y modelo abierto.

---

## Stack 5: Pipeline completo de proyecto final

### Componentes

- Almacenamiento: S3 o MinIO
- Datos: Polars
- Feature engineering: tablas en Parquet o feature store si compensa
- Compute: EC2 o SageMaker
- Framework: scikit-learn, PyTorch o Hugging Face
- MLOps: MLflow
- Recuperación: Qdrant o PageIndex, según tipo documental
- LLM: OpenAI o modelo abierto
- Evaluación: Ragas, Promptfoo o LangSmith

### Idea clave

No todos los proyectos necesitan todas las capas. El buen criterio consiste en saber qué añadir y qué no añadir.

---

## Ejemplo de combinación razonable para clase

Si el grupo quiere algo práctico pero asumible en poco tiempo, una combinación equilibrada sería:

- `Polars` para preparar datos.
- `Chroma` o `Qdrant` para recuperación simple.
- `LlamaIndex` para montar el flujo RAG.
- `OpenAI` o `Anthropic` para generar respuesta.
- `Promptfoo` o pruebas manuales guiadas para evaluación.

Ese stack es suficientemente realista, pero no demasiado pesado para un proyecto final de aula.

---

## Qué debe aprender el alumnado de estos ejemplos

- Que una arquitectura de IA se compone de piezas distintas.
- Que no todas las herramientas tienen sentido en todos los proyectos.
- Que conviene elegir por necesidad y no por moda.
- Que siempre hay alternativas más simples y más complejas.
