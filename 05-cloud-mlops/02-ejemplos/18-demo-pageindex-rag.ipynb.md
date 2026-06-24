# Notebook-esqueleto: demo de RAG con PageIndex

Este notebook está pensado para enseñar una alternativa al RAG clásico cuando no queremos depender del `chunking` manual de documentos largos.

La idea no es competir con la demo de RAG sencillo, sino mostrar otro enfoque para documentos más estructurados.

## Celda 1. Instalación

```python
#!pip install pageindex
```

## Celda 2. Configuración

```python
import os

os.environ["PAGEINDEX_API_KEY"] = "TU_API_KEY"
```

## Celda 3. Imports

```python
from pageindex import PageIndexClient
```

## Celda 4. Crear cliente

```python
client = PageIndexClient(api_key=os.environ["PAGEINDEX_API_KEY"])
```

## Celda 5. Elegir documento

Usa un PDF o documento largo donde la estructura importe.

```python
document_path = "ML-TomMitchel-keyIdeas.pdf"
print(f"Documento seleccionado: {document_path}")

# obtener path absoluto del documento
import os
document_path = os.path.abspath(document_path)
print(f"Path absoluto del documento: {document_path}")
```

## Celda 6. Enviar documento para indexación

```python
if not os.path.exists(document_path):
    filename = os.path.basename(document_path)
    found = None

    for root in [os.getcwd(), os.path.dirname(os.getcwd())]:
        for dirpath, _, filenames in os.walk(root):
            if filename in filenames:
                found = os.path.join(dirpath, filename)
                break
        if found:
            break

    if found is None:
        raise FileNotFoundError(
            f"No se encuentra el PDF: {document_path}\n"
            f"Archivo buscado: {filename}"
        )

    document_path = os.path.abspath(found)
    print(f"Documento localizado en: {document_path}")

result = client.submit_document(document_path)
doc_id = result["doc_id"]

print("Documento enviado correctamente")
print(f"doc_id: {doc_id}")
```

## Celda 7. Primera consulta

```python
pregunta = "Resume las conclusiones principales del documento"

response = client.chat_completions(
    messages=[{"role": "user", "content": pregunta}],
    doc_id=doc_id,
)

for linea in response["content"]:
    print(linea, end="")
```

```python
respuesta=response["choices"][0]["message"]["content"]

for linea in respuesta:
    print(linea, end="")
```

## Celda 8. Segunda consulta orientada a estructura

```python
pregunta = "¿Qué requisitos aparecen en la sección de evaluación?"

response = client.chat_completions(
    messages=[{"role": "user", "content": pregunta}],
    doc_id=doc_id,
)

print(response)
```

```python
respuesta=response["choices"][0]["message"]["content"]

for linea in respuesta:
    print(linea, end="")
```

## Celda 9. Tercera consulta orientada a trazabilidad

```python
pregunta = "¿En qué páginas se describe el procedimiento principal?"

response = client.chat_completions(
    messages=[{"role": "user", "content": pregunta}],
    doc_id=doc_id,
)

print(response)
```

```python
respuesta=response["choices"][0]["message"]["content"]

for linea in respuesta:
    print(linea, end="")
```

## Celda 10. Comentario didáctico

```python
print("Observa si la respuesta conserva mejor la estructura del documento y si aparecen referencias útiles a páginas o secciones.")
```

## Celda 11. Comparación conceptual con RAG clásico

```python
print("RAG clásico: documento -> fragmentación -> embeddings -> índice vectorial -> recuperación -> respuesta")
print("PageIndex: documento -> índice jerárquico -> recuperación estructurada -> respuesta con trazabilidad")
```

## Celda 12. Actividad para el alumnado

```python
pregunta = "Escribe aquí una pregunta sobre una parte concreta del documento"

response = client.chat_completions(
    messages=[{"role": "user", "content": pregunta}],
    doc_id=doc_id,
)

print(response)
```

## Qué conviene comentar al ejecutar el notebook

- Aquí no estamos partiendo el documento en fragmentos manuales.
- La herramienta intenta apoyarse en la estructura del documento.
- Este enfoque puede tener más sentido en informes, manuales o normativas.
- No siempre compensa: para documentos pequeños, el RAG clásico suele bastar.

## Documento recomendado para clase

Conviene usar:

- un PDF largo,
- con secciones reconocibles,
- y preguntas que dependan de mantener contexto.

Ejemplos:

- informe técnico,
- memoria de proyecto,
- normativa,
- manual de uso extenso.

## Extensión opcional

Si quieres ampliar la demo:

- compara la misma pregunta en RAG clásico y en `PageIndex`,
- pide una respuesta con referencias explícitas,
- prueba preguntas sobre una sección muy concreta,
- o enlaza el debate con `12-recuperacion-avanzada-rag.md` y `14-guion-clase-recuperacion-stacks.md`.


---

## Alternativa local 1: treeRAG

`treeRAG` es la alternativa más cercana a la idea de PageIndex dentro de este notebook: construye una jerarquía documental y recupera usando navegación por árbol, sin base vectorial. Requiere un LLM para resumir y seleccionar nodos.

```python
#!pip install treerag langchain-ollama
```

```python
from treerag import index_document, make_summarizer, ask, make_retriever
from langchain_ollama import ChatOllama

TREE_MODEL = "nemotron-3-super:cloud"
llm = ChatOllama(model=TREE_MODEL)
print(f"Modelo treeRAG: {TREE_MODEL}")
```

```python
treerag_doc = index_document(
    document_path,
    summarizer=make_summarizer(
        llm,
        system_prompt=(
            "Resume documentos técnicos en español. "
            "Conserva secciones, conceptos clave y referencias a páginas si aparecen."
        ),
    ),
    overwrite=True,
)

treerag_retriever = make_retriever(
    llm,
    answer_system_prompt=(
        "Responde solo con el contexto recuperado. "
        "Usa Markdown y separa las ideas en párrafos."
    ),
)
```

```python
pregunta = "Resume las conclusiones principales del documento"

treerag_result = ask(
    pregunta,
    treerag_doc,
    treerag_retriever,
    extra_context="Responde en español, con apartados breves y referencias si están disponibles.",
)

print(treerag_result.content)
print("\nReferencias:", getattr(treerag_result, "references", None))
```


---

## Alternativa local 2: TreeDex

`TreeDex` también busca RAG vectorless: indexa documentos como árbol navegable y consulta con un LLM. Para clase es interesante porque se parece mucho al objetivo de PageIndex, pero evita el cloud de PageIndex.

Si el PDF tiene tabla de contenidos clara, debería ser más estable. Si el PDF está mal estructurado, dependerá más del LLM y del parser.

```python
#!pip install treedex
```

```python
from treedex import TreeDex, OllamaLLM

TREEDEX_MODEL = "nemotron-3-super:cloud"
treedex_llm = OllamaLLM(
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    model=os.getenv("OLLAMA_MODEL", TREEDEX_MODEL),
)

print(f"Modelo TreeDex: {os.getenv('OLLAMA_MODEL', TREEDEX_MODEL)}")
```

```python
treedex_index = TreeDex.from_file(document_path, llm=treedex_llm)

# Útil para enseñar en pantalla qué estructura ha detectado.
treedex_index.show_tree()

# Persistencia simple para no reconstruir el índice en cada ejecución.
treedex_index.save("treedex_index.json")
```

```python
pregunta = "Resume las conclusiones principales del documento y cita páginas o secciones relevantes"

treedex_result = treedex_index.query(pregunta, agentic=True)

print(treedex_result.answer)
print("\nPáginas/secciones:", getattr(treedex_result, "pages_str", None))
```

```python
# Cargar un índice ya generado.
treedex_index_cargado = TreeDex.load("treedex_index.json", llm=treedex_llm)

resultado = treedex_index_cargado.query(
    "¿Qué técnicas principales aparecen en el documento?",
    agentic=True,
)

print(resultado.answer)
```


---

## Alternativa avanzada: Microsoft GraphRAG

`GraphRAG` no es una sustitución directa de PageIndex. Es más potente para colecciones y preguntas globales sobre temas, entidades y relaciones, pero también es bastante más pesado.

Puntos importantes para explicarlo bien:

- Construye un grafo de entidades, relaciones, claims y comunidades.
- La indexación consume bastantes llamadas al LLM.
- Por defecto trabaja con unidades de texto, tablas Parquet y puede usar embeddings/vector store.
- Encaja mejor en corpus de varios documentos que en una demo rápida sobre un único PDF.

Por eso lo dejamos como comparación conceptual o extensión avanzada, no como reemplazo limpio de PageIndex para esta sesión.

```python
#!pip install graphrag
```

```python
# GraphRAG se suele ejecutar como proyecto separado desde CLI.
# Este bloque prepara una carpeta mínima de trabajo a partir del texto extraído previamente.
# No se ejecuta automáticamente porque requiere configurar modelos y puede consumir muchos tokens.

from pathlib import Path
import shutil

graphrag_root = Path("graphrag_demo")
graphrag_input = graphrag_root / "input"
graphrag_input.mkdir(parents=True, exist_ok=True)

# Si ya tienes texto extraído del PDF, cópialo aquí como .txt.
# Ejemplo: shutil.copyfile("documento_extraido.txt", graphrag_input / "documento.txt")

print(f"Carpeta GraphRAG preparada: {graphrag_root.resolve()}")
print("Siguiente paso manual: graphrag init --root graphrag_demo")
```


Comandos orientativos para una prueba real de GraphRAG:

```bash
graphrag init --root graphrag_demo
# editar graphrag_demo/settings.yaml y graphrag_demo/.env
graphrag index --root graphrag_demo
graphrag query --root graphrag_demo --method global "¿Cuáles son los temas principales del documento?"
graphrag query --root graphrag_demo --method local "¿Qué dice sobre deep learning?"
```

Para esta unidad, GraphRAG sirve mejor como contraste: no todo lo que lleva “graph” resuelve el problema de PageIndex. Si el objetivo es RAG sin chunking y sin vector DB, `TreeDex`/`treeRAG` son más adecuados.


---

## Comparación rápida de alternativas

| Herramienta | Sin vector DB | Sin chunking clásico | Local | Encaje en esta demo |
|---|---:|---:|---:|---|
| PageIndex Cloud | Sí | Sí | No | Referencia principal |
| PageIndex self-host | Sí | Sí | Sí | Potente, pero más frágil de instalar |
| treeRAG | Sí | Bastante | Sí | Muy buena alternativa didáctica |
| TreeDex | Sí | Bastante | Sí | Candidata recomendada para probar |
| GraphRAG | No siempre | No claramente | Sí | Extensión avanzada, no sustituto directo |
