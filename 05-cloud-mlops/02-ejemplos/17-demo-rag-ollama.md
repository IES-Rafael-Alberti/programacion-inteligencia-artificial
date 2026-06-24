# Demo local de RAG con Ollama

## Idea

Esta variante usa solo `Ollama` y Python. Es útil para clase porque cada alumno puede elegir:

- el modelo generativo que su equipo soporte,
- el modelo de embeddings que tenga instalado,
- y no depende de clave API externa.

## Ventajas

- Todo se ejecuta en local.
- Sirve para comparar modelos distintos.
- Hace más visible cómo funciona el RAG por dentro.

## Requisitos

- Tener Ollama instalado y ejecutándose.
- Tener descargado al menos:
  - un modelo generativo, por ejemplo `gemma3`, `qwen3` o `llama3.1`
  - un modelo de embeddings, por ejemplo `embeddinggemma`, `qwen3-embedding` o `all-minilm`

## Notebook

El notebook preparado está en:

- [17-demo-rag-ollama.ipynb](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/17-demo-rag-ollama.ipynb)

## Qué hace

1. Carga los documentos de ejemplo.
2. Los fragmenta.
3. Genera embeddings con Ollama.
4. Recupera los fragmentos más parecidos.
5. Construye un prompt con contexto.
6. Genera una respuesta final con un modelo local.

## Relación con la unidad

Este ejemplo encaja muy bien con:

- [12-recuperacion-avanzada-rag.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/12-recuperacion-avanzada-rag.md)
- [13-ejemplos-stacks-ia.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/13-ejemplos-stacks-ia.md)
- [15-demo-rag-sencillo.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/15-demo-rag-sencillo.md)
