# LlamaIndex: documentación práctica

LlamaIndex es un framework especializado en crear aplicaciones RAG sobre documentos propios. Su objetivo es facilitar la carga, división, indexación, recuperación y consulta de información para que un modelo de lenguaje responda usando contexto externo.

## Por qué no es lo mismo que LangChain

LangChain es más general: cadenas, herramientas, memoria y agentes. LlamaIndex está más centrado en datos y documentos.

| Aspecto | LangChain | LlamaIndex |
|---|---|---|
| Foco | Orquestación de componentes | RAG sobre documentos |
| Documentos | Integrables | Elemento central |
| Índices | Básicos o externos | Parte principal del framework |
| Recuperación | Retrievers generales | Recuperación avanzada y configurable |
| Consulta sobre documentos | Hay que componerla | Query engines ya preparados |

## Flujo típico de RAG

1. Cargar documentos.
2. Dividirlos en fragmentos.
3. Crear embeddings.
4. Guardarlos en un índice o base vectorial.
5. Recuperar fragmentos relevantes ante una pregunta.
6. Generar la respuesta usando esos fragmentos.
7. Mostrar fuentes o citas.

## Componentes principales

### Loaders

Cargan documentos desde carpetas, PDFs, Markdown, webs, bases de datos o herramientas externas.

```python
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("docs").load_data()
```

### Chunking

Divide documentos largos en fragmentos. El tamaño del fragmento afecta a la calidad de recuperación.

```python
from llama_index.core.node_parser import SentenceSplitter

splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
```

### Embeddings

Transforman texto en vectores numéricos.

```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

### Vector stores

LlamaIndex puede usar bases vectoriales como Chroma, FAISS, Qdrant, Pinecone o Weaviate.

```python
from llama_index.vector_stores.chroma import ChromaVectorStore
```

En esta unidad conviene tratar Chroma y FAISS como piezas internas del RAG, no como temas independientes.

### Query engine

Coordina recuperación y generación de respuesta.

```python
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(similarity_top_k=3)
response = query_engine.query("¿Qué dice el documento sobre evaluación?")
```

### Chat engine

Permite mantener conversación con contexto documental.

```python
chat_engine = index.as_chat_engine(chat_mode="context")
```

## Chroma y FAISS como piezas internas

### Chroma

Es una base vectorial cómoda para prototipos. Permite guardar colecciones de documentos y consultarlas por similitud.

### FAISS

Es una librería eficiente para búsqueda vectorial local. Es útil para explicar vecinos cercanos y recuperación por similitud.

## Evaluación de RAG

Un sistema RAG no es bueno solo porque responde. Hay que revisar:

1. Si recupera documentos relevantes.
2. Si la respuesta usa el contexto recuperado.
3. Si cita fuentes.
4. Si inventa información no presente en los documentos.
5. Si el tamaño de fragmento y `top_k` son adecuados.

## Relación con MLflow

MLflow puede registrar configuraciones de un sistema RAG:

1. Base vectorial usada.
2. Modelo de embeddings.
3. Tamaño de fragmento.
4. `top_k`.
5. Métricas de relevancia o fidelidad.

## Buenas prácticas

1. Empezar con pocos documentos y revisar los fragmentos recuperados.
2. Mostrar fuentes al usuario.
3. Separar recuperación y generación.
4. Ajustar `chunk_size`, `chunk_overlap` y `top_k`.
5. Evaluar respuestas con preguntas conocidas.

## Errores frecuentes

1. Pensar que RAG elimina las alucinaciones automáticamente.
2. Recuperar demasiados documentos irrelevantes.
3. No revisar el contexto que recibe el modelo.
4. Usar documentos sin limpiar.
5. No registrar qué configuración produjo cada resultado.

## Relación con los notebooks

El notebook `Fase2/100_mlflow_llamaindex_rag.ipynb` muestra un RAG mínimo con documentos locales y recuperación vectorial simulada para entender el patrón antes de usar LlamaIndex real.

## Cuándo usar LlamaIndex

Usa LlamaIndex si quieres crear un chatbot, buscador o asistente que responda sobre documentos propios.

No es necesario si solo necesitas una cadena simple o una llamada directa a un modelo sin documentos externos.

## Instalación

```bash
pip install llama-index
pip install llama-index-embeddings-huggingface
pip install llama-index-vector-stores-chroma
```

Documentación oficial: https://docs.llamaindex.ai/
