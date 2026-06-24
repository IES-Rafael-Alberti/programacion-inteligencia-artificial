# Recuperación avanzada para RAG

## Introducción

En muchos proyectos se explica RAG como una secuencia simple: fragmentar documentos, generar embeddings, guardarlos en una base vectorial y recuperar los fragmentos más parecidos. Ese enfoque funciona, pero no siempre es el mejor. En documentos largos, técnicos o muy estructurados, el `chunking` puede romper el contexto y empeorar la recuperación.

Esta unidad presenta alternativas y extensiones al RAG clásico para que el alumnado conozca más opciones y pueda investigar si alguna encaja mejor en su proyecto.

---

## RAG clásico

### Flujo habitual

```text
Documento -> chunking -> embeddings -> índice vectorial -> recuperación -> LLM -> respuesta
```

### Ventajas

- Fácil de entender.
- Muy extendido.
- Compatible con muchos frameworks y bases vectoriales.

### Limitaciones

- El `chunking` puede romper contexto.
- Puede mezclar fragmentos poco relevantes.
- No siempre respeta bien la estructura lógica del documento.
- En documentos largos o normativos, la respuesta puede perder precisión.

---

## Alternativas y mejoras al RAG clásico

### 1. Recuperación jerárquica

En vez de tratar el documento como una lista plana de fragmentos, se representa como una estructura en árbol con secciones, subsecciones y páginas.

Ventajas:

- Mantiene mejor la estructura del documento.
- Reduce ruido en la recuperación.
- Permite navegar por secciones antes de bajar al detalle.

### 2. Búsqueda híbrida

Combina búsqueda vectorial y búsqueda léxica.

Ventajas:

- Recupera tanto por significado como por coincidencia exacta.
- Suele mejorar resultados en documentación técnica y normativa.

### 3. Reranking

Después de recuperar varios candidatos, un modelo adicional los reordena según relevancia.

Ventajas:

- Mejora la calidad final del contexto enviado al LLM.
- Útil cuando la recuperación inicial devuelve resultados aceptables pero no óptimos.

### 4. Recuperación contextual o multi-step

El sistema recupera, analiza, reformula la búsqueda y vuelve a recuperar.

Ventajas:

- Más robusto en preguntas complejas.
- Encaja bien con agentes o pipelines avanzados.

---

## PageIndex

`PageIndex` es una herramienta de recuperación orientada a documentos largos y estructurados que evita el enfoque clásico de `chunking + vector database`. Según su documentación oficial, transforma documentos en un índice jerárquico y permite una recuperación basada en razonamiento sobre esa estructura, con citas por página y SDK de Python.  
Fuentes: [PageIndex Docs](https://docs.pageindex.ai/), [Python SDK](https://docs.pageindex.ai/sdk), [sitio oficial](https://www.pageindex.dev/).

### Qué aporta

- Índice jerárquico del documento.
- Recuperación sin base vectorial ni fragmentación clásica.
- Buen encaje en PDFs largos, informes y documentación compleja.
- SDK de Python y API.

### Qué problema intenta resolver

Cuando el chunking rompe la coherencia de una sección, el modelo recibe fragmentos dispersos y puede perder el hilo del documento. `PageIndex` intenta conservar la organización original y recuperar contexto más útil.

### Flujo general

```text
Documento -> índice jerárquico -> navegación razonada por el árbol -> contexto relevante -> respuesta con citas
```

### Ejemplo mínimo con el SDK de Python

```python
from pageindex import PageIndexClient

client = PageIndexClient(api_key="YOUR_API_KEY")

result = client.submit_document("./informe.pdf")
doc_id = result["doc_id"]

tree = client.get_tree(doc_id)
response = client.chat_completions(
    messages=[{"role": "user", "content": "Resume las conclusiones principales"}],
    doc_id=doc_id
)
```

### Cuándo puede tener sentido

- Documentación técnica larga.
- Informes financieros o jurídicos.
- Documentos donde importan mucho las secciones y la trazabilidad.

### Demo relacionada

En esta unidad tienes una demo específica para enseñar este enfoque en clase:

- [18-demo-pageindex-rag.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.md)
- [18-demo-pageindex-rag.ipynb](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.ipynb)
- [18-demo-pageindex-rag.ipynb.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.ipynb.md)

### Cuándo no hace falta

- Colecciones pequeñas y simples.
- Casos donde el RAG clásico ya funciona suficientemente bien.
- Proyectos muy cortos donde se busca solo una demo rápida.

---

## Otras herramientas y enfoques relacionados

### Haystack

- Útil para pipelines de recuperación, búsqueda híbrida y QA.

### LlamaIndex

- Muy adecuado para ingesta, recuperación y RAG sobre documentos.

### Rerankers

- Modelos o servicios que reordenan resultados recuperados.
- Muy útiles para mejorar precisión sin rehacer todo el stack.

### Bases vectoriales

- `Chroma`, `Qdrant`, `Weaviate`, `Milvus`, `FAISS`.
- Siguen siendo la opción más común en muchos proyectos.

---

## Comparación de enfoques

| Enfoque | Ventaja principal | Limitación |
|---------|-------------------|------------|
| RAG clásico con chunking | Sencillo y estándar | Puede romper contexto |
| Recuperación jerárquica | Conserva estructura documental | Menos estándar |
| Búsqueda híbrida | Combina significado y texto exacto | Más complejidad |
| Reranking | Mejora la relevancia final | Añade coste y latencia |
| Recuperación multi-step | Más robusta en preguntas complejas | Más complejidad técnica |

---

## Aplicación al proyecto

Conviene plantearse estas variantes si el proyecto:

1. Trabaja con documentos largos.
2. Necesita respuestas justificadas o con citas.
3. Obtiene malos resultados con el chunking básico.
4. Quiere comparar alternativas de recuperación.

En esta fase del curso no hace falta que el alumnado implemente todas estas técnicas. Basta con que entienda que existen, vea ejemplos y sepa justificar cuándo investigarlas más.

---

## Recomendaciones generales

| Caso | Recomendación |
|------|---------------|
| Primer RAG del proyecto | Chunking simple + base vectorial |
| Documentación técnica o normativa | Búsqueda híbrida o jerárquica |
| PDFs largos y estructurados | Explorar PageIndex |
| Recuperación razonable pero mejorable | Añadir reranking |
| Proyecto final con ambición | Probar variantes y comparar |

---

## Fuentes recomendadas

- Documentación oficial de PageIndex.
- SDK oficial de Python de PageIndex.
- Documentación oficial de LlamaIndex.
- Documentación oficial de Haystack.
- Documentación oficial de Qdrant, Chroma y Weaviate.

## Material complementario de la unidad

- [15-demo-rag-sencillo.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/15-demo-rag-sencillo.md)
- [17-demo-rag-ollama.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/17-demo-rag-ollama.md)
- [18-demo-pageindex-rag.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.md)
