# Notebook-esqueleto: demo de RAG sencillo

Este archivo sirve como guion de notebook o script dividido por celdas. Puedes copiarlo a un `.ipynb` o usarlo como base para un script de clase.

---

## Celda 1. Instalación

```bash
pip install llama-index llama-index-llms-openai llama-index-embeddings-openai chromadb
```

---

## Celda 2. Configuración

```python
import os

os.environ["OPENAI_API_KEY"] = "TU_API_KEY"
```

---

## Celda 3. Imports

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
```

---

## Celda 4. Configurar modelo y embeddings

```python
Settings.llm = OpenAI(model="gpt-4.1-mini")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
```

---

## Celda 5. Cargar documentos

```python
documents = SimpleDirectoryReader("../Documentacion/documentos_demo").load_data()
print(f"Documentos cargados: {len(documents)}")
```

---

## Celda 6. Crear índice

```python
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(similarity_top_k=3)
```

---

## Celda 7. Primera consulta

```python
pregunta = "¿Qué dice la documentación sobre la evaluación?"
response = query_engine.query(pregunta)

print(response)
```

---

## Celda 8. Segunda consulta

```python
pregunta = "Resume los pasos principales del proceso descrito en los documentos"
response = query_engine.query(pregunta)

print(response)
```

---

## Celda 9. Comentario didáctico

```python
print("Observa si la respuesta usa información concreta de los documentos o si generaliza demasiado.")
```

---

## Celda 10. Actividad para el alumnado

```python
pregunta = "Escribe aquí una pregunta relacionada con tus documentos"
response = query_engine.query(pregunta)

print(response)
```

---

## Sugerencia de carpeta de documentos

```text
../Documentacion/documentos_demo/
├── proyecto.md
├── evaluacion.md
└── faq.md
```

En esta documentación ya está creada esa carpeta con archivos de ejemplo.

---

## Sugerencia de contenidos

### proyecto.md

- Descripción breve de un proyecto.
- Objetivos.
- Usuarios.

### evaluacion.md

- Criterios de evaluación.
- Fases del trabajo.
- Entregables.

### faq.md

- Preguntas frecuentes sobre uso de la herramienta o proceso del proyecto.

---

## Extensión opcional

Si quieres ampliar la demo:

- compara una respuesta con RAG y otra sin RAG,
- baja o sube `similarity_top_k`,
- cambia la pregunta por una más compleja,
- o enlaza el debate con `12-recuperacion-avanzada-rag.md`.
