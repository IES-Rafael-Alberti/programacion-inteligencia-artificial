# Bases de datos vectoriales y recuperación

## Introducción

Muchas aplicaciones de IA generativa no funcionan solo con un modelo. Necesitan recuperar información relevante antes de generar una respuesta. Para eso se usan embeddings, índices vectoriales y bases de datos orientadas a búsqueda semántica.

## Qué problema resuelven

- Buscar documentos similares por significado y no solo por palabras exactas.
- Implementar sistemas RAG.
- Recuperar fragmentos de texto, imágenes o productos similares.
- Escalar búsquedas semánticas sobre colecciones grandes.

---

## Conceptos clave

### Embedding

Representación numérica de un texto, imagen u otro objeto en forma de vector.

### Índice vectorial

Estructura que permite buscar de forma eficiente los vectores más parecidos.

### Recuperación

Proceso de obtener los elementos más relevantes antes de pasarlos al modelo o al sistema de recomendación.

---

## Alternativas habituales

### FAISS

- Biblioteca open source desarrollada por Meta.
- Muy rápida para índices vectoriales en local.
- Muy útil para aprendizaje, prototipos y experimentos.

### Chroma

- Base de datos vectorial open source muy usada en ejemplos de RAG.
- Fácil de integrar con LangChain y otros frameworks.

### Qdrant

- Base vectorial open source orientada a producción.
- Buena combinación entre facilidad de uso y capacidades avanzadas.

### Weaviate

- Plataforma open source con funcionalidades vectoriales y de búsqueda híbrida.
- Interesante para sistemas documentales más ricos.

### Milvus

- Base vectorial open source pensada para escala alta.
- Más habitual en despliegues de mayor tamaño.

### Servicios gestionados

| Servicio | Comentario |
|----------|------------|
| Pinecone | Muy popular en productos RAG |
| Vertex AI Vector Search | Integrado en GCP |
| Azure AI Search | Combina búsqueda clásica y vectorial |
| OpenSearch vector search | Útil si ya se trabaja con OpenSearch |

---

## Comparativa rápida

| Herramienta | Tipo | Mejor encaje | Limitación |
|-------------|------|--------------|------------|
| FAISS | Biblioteca open source | Prototipos y uso local | No es una base de datos completa |
| Chroma | Base vectorial open source | Docencia y RAG sencillo | Menos enfocada a gran escala |
| Qdrant | Base vectorial open source | Producción mediana | Requiere despliegue |
| Weaviate | Plataforma open source | Búsqueda híbrida y metadatos | Más compleja |
| Milvus | Base vectorial open source | Escala alta | Curva técnica mayor |
| Pinecone | Gestionada | Rapidez de puesta en marcha | Dependencia del proveedor |

---

## Búsqueda vectorial frente a búsqueda clásica

| Enfoque | Cuándo funciona mejor |
|---------|-----------------------|
| Búsqueda léxica | Palabras exactas, filtros simples |
| Búsqueda vectorial | Similitud semántica |
| Búsqueda híbrida | Sistemas documentales más robustos |

La combinación híbrida suele ser la opción más sólida cuando importa tanto el significado como la coincidencia exacta de términos.

---

## Aplicación al proyecto

Conviene plantearse esta categoría si el proyecto:

1. Trabaja con documentos, preguntas y respuestas o bases de conocimiento.
2. Necesita RAG.
3. Usa embeddings para recomendación o similitud.
4. Requiere recuperar ejemplos, registros o elementos parecidos.

Si el proyecto no necesita recuperación semántica, esta categoría puede no ser necesaria.

---

## Recomendaciones generales

| Caso | Recomendación |
|------|---------------|
| Primeros prototipos | FAISS o Chroma |
| Proyecto docente con RAG | Chroma o Qdrant |
| Producción open source | Qdrant o Weaviate |
| Gran escala | Milvus |
| Integración rápida gestionada | Pinecone o servicio cloud equivalente |

---

## Ejemplo mínimo

```python
import faiss
import numpy as np

vectors = np.array([
    [0.1, 0.2, 0.3],
    [0.9, 0.8, 0.7],
    [0.15, 0.18, 0.29]
], dtype="float32")

index = faiss.IndexFlatL2(3)
index.add(vectors)

query = np.array([[0.1, 0.2, 0.31]], dtype="float32")
distances, ids = index.search(query, k=2)
```

---

## Fuentes recomendadas

- Documentación oficial de FAISS.
- Documentación oficial de Chroma.
- Documentación oficial de Qdrant.
- Documentación oficial de Weaviate.
- Documentación oficial de Milvus.
- Documentación oficial de Pinecone.
