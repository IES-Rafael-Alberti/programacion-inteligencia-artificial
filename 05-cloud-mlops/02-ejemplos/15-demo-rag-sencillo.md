# Demo técnica: RAG sencillo para clase

## Objetivo

Esta demo está pensada para enseñar en clase un flujo RAG mínimo y comprensible. No busca optimización ni producción. Busca que el alumnado vea cómo se conectan documentos, recuperación y generación.

## Qué enseña

- Cómo se cargan documentos.
- Cómo se fragmentan.
- Cómo se indexan.
- Cómo se recupera contexto.
- Cómo se genera una respuesta con ese contexto.

## Qué no enseña

- Observabilidad completa.
- Evaluación avanzada.
- Serving de producción.
- Recuperación jerárquica o `reranking`.

Esos temas pueden mencionarse después como ampliación.

---

## Stack recomendado para la demo

- Python
- `LlamaIndex`
- `Chroma` o almacenamiento vectorial en memoria
- `OpenAI` o proveedor equivalente
- Un conjunto pequeño de archivos `.txt` o `.md`

Si no quieres depender de una base vectorial externa, usa una opción simple en memoria o persistencia local.

---

## Duración orientativa

- Explicación: 10 minutos
- Ejecución de demo: 15-20 minutos
- Debate final: 10 minutos

---

## Guion de la demo

### Paso 1. Presentar el problema

Explicar algo como:

“Tenemos varios documentos. Queremos hacer preguntas sobre ellos. El modelo por sí solo no conoce estos documentos, así que primero debemos recuperar el contexto relevante.”

### Paso 2. Mostrar los documentos

Usa 2 o 3 documentos pequeños, por ejemplo:

- un resumen de proyecto,
- una guía técnica,
- unas preguntas frecuentes.

La idea es que el alumnado vea claramente de dónde sale la respuesta.

En esta unidad ya tienes una carpeta lista para la demo:

- [proyecto.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/documentos_demo/proyecto.md)
- [evaluacion.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/documentos_demo/evaluacion.md)
- [faq.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/documentos_demo/faq.md)

### Paso 3. Explicar el flujo

```text
Documentos -> fragmentación -> embeddings -> índice vectorial -> recuperación -> LLM -> respuesta
```

### Paso 4. Ejecutar la indexación

Mostrar que:

- se leen los documentos,
- se trocean,
- se transforman en embeddings,
- se guardan en un índice.

### Paso 5. Lanzar una consulta

Ejemplo:

- “¿Qué dice la documentación sobre el proceso de evaluación?”

Mostrar:

- qué fragmentos se recuperan,
- y cómo el modelo genera la respuesta con ese contexto.

### Paso 6. Mostrar una limitación

Hacer una pregunta que:

- necesite varias partes del documento,
- o dependa de una estructura larga.

Ahí puedes explicar:

- que el `chunking` a veces rompe el contexto,
- y enlazar con `12-recuperacion-avanzada-rag.md`.

---

## Mensajes clave para verbalizar en clase

- RAG no es “magia”, sino combinación de recuperación y generación.
- Lo importante no es solo el modelo, sino también qué contexto recibe.
- Una mala recuperación produce malas respuestas.
- Un stack sencillo suele ser mejor que uno excesivamente complejo para un proyecto final de aula.

---

## Variantes de la demo

### Variante 1. Muy simple

- 2 o 3 archivos.
- 1 consulta.
- 1 resultado bueno.
- 1 caso donde falla un poco.

### Variante 2. Algo más completa

- varias consultas,
- mostrar nodos recuperados,
- comparar una respuesta sin contexto y otra con contexto.

### Variante 3. Comparativa

- RAG sencillo,
- explicación conceptual de por qué una recuperación jerárquica o híbrida podría mejorar ese caso.

---

## Requisitos previos

- Tener clave API si se usa un proveedor externo.
- Tener instaladas las librerías necesarias.
- Tener una carpeta con documentos pequeños y limpios.

La carpeta recomendada para usar directamente en la demo es:

- [documentos_demo](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/documentos_demo)

---

## Librerías orientativas

```bash
pip install llama-index llama-index-llms-openai llama-index-embeddings-openai chromadb
```

Si usas otro proveedor, cambia las integraciones correspondientes.

---

## Pseudocódigo de la demo

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings

Settings.llm = OpenAI(model="gpt-4.1-mini")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

documents = SimpleDirectoryReader("../Documentacion/documentos_demo").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(similarity_top_k=3)
response = query_engine.query("¿Qué dice la documentación sobre la evaluación?")

print(response)
```

---

## Qué conviene enseñar en pantalla

1. La carpeta con documentos.
2. El código mínimo.
3. La consulta.
4. La respuesta.
5. Si es posible, los fragmentos recuperados.

---

## Cierre recomendado

Terminar con dos preguntas:

1. ¿Este enfoque sería suficiente para vuestro proyecto?
2. Si no lo fuera, ¿qué mejoraríais: recuperación, modelo o evaluación?
