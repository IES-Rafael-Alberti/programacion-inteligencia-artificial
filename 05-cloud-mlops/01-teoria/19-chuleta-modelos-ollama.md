# Chuleta rápida de modelos para Ollama

## Objetivo

Esta chuleta sirve para que cada alumno pueda elegir un modelo razonable al usar la demo local con Ollama, según la máquina que tenga disponible.

## Antes de empezar

Conviene comprobar primero qué modelos hay instalados:

```python
import ollama
print(ollama.list())
```

Los nombres exactos pueden variar entre equipos, así que esta chuleta debe usarse como orientación, no como lista cerrada.

---

## Opción 1. Equipos justos de recursos

### Modelos generativos recomendados

- `gemma2:2b`
- `qwen2.5:1.5b`
- `qwen2.5:3b`

### Modelos de embeddings recomendados

- `all-minilm`
- el modelo de embeddings más ligero disponible en el equipo

### Cuándo usar esta opción

- Portátiles modestos.
- Equipos sin GPU.
- Situaciones donde importa más que funcione que la calidad máxima.

### Ventajas

- Menor consumo de memoria.
- Respuesta más rápida en CPU.

### Inconvenientes

- Respuestas más limitadas.
- Peor seguimiento de instrucciones en algunos casos.

---

## Opción 2. Equipos normales

### Modelos generativos recomendados

- `gemma3`
- `qwen3`

### Modelos de embeddings recomendados

- `embeddinggemma`
- `qwen3-embedding`

### Cuándo usar esta opción

- Equipos de aula razonables.
- Portátiles o sobremesas modernos.
- La opción más equilibrada para una demo.

### Ventajas

- Buen equilibrio entre calidad y rendimiento.
- Suficiente para enseñar el flujo completo de RAG.

### Inconvenientes

- Puede ir más lento en máquinas muy justas.

---

## Opción 3. Equipos potentes o con GPU

### Modelos generativos recomendados

- `llama3.1`
- variantes más grandes de `qwen`
- cualquier modelo generativo superior que ya tengan descargado

### Modelos de embeddings recomendados

- `embeddinggemma`
- `qwen3-embedding`

### Cuándo usar esta opción

- Equipos con buena memoria.
- Máquinas con GPU.
- Comparativas entre modelos.

### Ventajas

- Mejor calidad de respuesta en general.
- Mejor comportamiento en preguntas algo más complejas.

### Inconvenientes

- Más memoria.
- Más tiempo de respuesta.

---

## Configuración recomendada para clase

Si no quieres complicar la sesión, una configuración razonable por defecto es:

```python
GEN_MODEL = "gemma3"
EMBED_MODEL = "embeddinggemma"
```

Y a partir de ahí:

- si va lento, bajar a un modelo más pequeño;
- si va sobrado, comparar con otro modelo generativo.

---

## Qué conviene comparar

Si varios alumnos usan modelos distintos, pueden fijarse en:

- velocidad de respuesta,
- claridad de la respuesta,
- fidelidad al contexto recuperado,
- tiempo de generación de embeddings,
- diferencia entre respuesta con y sin RAG.

---

## Recomendación didáctica

Para clase, no hace falta que todo el grupo use el mismo modelo. De hecho, puede ser útil que algunos prueben modelos distintos y comenten:

- cuál responde mejor,
- cuál consume menos,
- y cuál parece más adecuado para un proyecto final sencillo.

---

## Documentos relacionados

- [17-demo-rag-ollama.ipynb](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/17-demo-rag-ollama.ipynb)
- [17-demo-rag-ollama.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/17-demo-rag-ollama.md)
- [15-demo-rag-sencillo.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/15-demo-rag-sencillo.md)
