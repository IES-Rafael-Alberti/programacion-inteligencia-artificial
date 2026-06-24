# APIs de LLM en la nube

## Introducción

Las APIs de modelos de lenguaje permiten incorporar capacidades de generación, resumen, clasificación, extracción de información y RAG sin entrenar un modelo desde cero.

## Cuándo tiene sentido usar una API de LLM

- Cuando el proyecto necesita comprensión o generación de texto.
- Cuando se quiere prototipar rápido.
- Cuando no se dispone de infraestructura para servir un modelo propio.
- Cuando compensa pagar por uso frente a mantener un modelo desplegado.

---

## OpenAI

### Perfil general

- Muy popular y bien documentado.
- Buen equilibrio entre facilidad de uso y calidad.
- Amplio ecosistema de SDKs y ejemplos.

### Uso básico

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")
```

### Cuándo encaja bien

- Chatbots.
- Asistentes.
- Resumen y clasificación.
- Prototipos con poca fricción.

### Azure OpenAI

Versión integrada en Azure con enfoque empresarial e integración con el ecosistema Microsoft.

---

## Anthropic

### Perfil general

- Muy valorado en tareas de redacción y análisis.
- Suele destacar por contexto amplio y buen comportamiento conversacional.

### Cuándo encaja bien

- Análisis de documentos largos.
- Asistentes con instrucciones complejas.
- Flujos donde importa mucho la calidad del texto generado.

---

## Google AI

### Perfil general

- Modelos con ventanas de contexto amplias.
- Integración natural con Vertex AI y el ecosistema de Google.

### Cuándo encaja bien

- Procesado de contexto largo.
- Proyectos ya situados en GCP.
- Casos donde interesa combinar IA generativa y servicios cloud de Google.

---

## Cohere

### Perfil general

- Fuerte orientación empresarial.
- Relevante en casos de RAG, embeddings y búsqueda semántica.

### Cuándo encaja bien

- Sistemas de búsqueda.
- Recuperación y generación apoyada en documentos.
- Soluciones con foco en embeddings.

## Alternativas abiertas o con acceso gratuito

### Hugging Face Inference API

- Permite usar modelos abiertos sin desplegarlos desde cero.
- Buena opción para experimentar con modelos de la comunidad.

### Together AI y Fireworks AI

- Proveen acceso a modelos abiertos hospedados.
- Útiles cuando se quiere trabajar con modelos open weight a través de API.

### APIs autogestionadas con modelos abiertos

- Si no se quiere depender de un proveedor cerrado, se pueden desplegar modelos abiertos con herramientas como `vLLM` o `Text Generation Inference`.
- Esta opción exige más infraestructura, pero reduce dependencia de proveedores y encaja mejor en un enfoque abierto.

---

## Comparación orientativa

| Proveedor | Fortalezas | Casos habituales |
|-----------|------------|------------------|
| OpenAI | Facilidad de uso, ecosistema y calidad general | Chat, resumen, asistentes |
| Anthropic | Buen rendimiento en redacción y contexto largo | Análisis documental |
| Google | Contexto amplio e integración cloud | Flujos en GCP y multimodalidad |
| Cohere | Embeddings y orientación a empresa | RAG y búsqueda semántica |
| Hugging Face | Acceso a modelos abiertos | Pruebas y prototipos con open source |
| Together AI / Fireworks | APIs para modelos abiertos | Inferencia sobre modelos open weight |

---

## Embeddings

Los embeddings convierten texto en vectores numéricos. Son fundamentales en:

- RAG
- Búsqueda semántica
- Recomendación basada en similitud
- Detección de documentos relacionados

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")
embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input="programación en inteligencia artificial"
)
```

---

## Aplicación al proyecto

Antes de elegir una API conviene responder:

1. ¿El proyecto necesita un LLM como parte central o solo como apoyo?
2. ¿Se usará para chat, clasificación, resumen o RAG?
3. ¿Importa más el coste, el contexto o la integración con otra nube?
4. ¿Se necesitan también embeddings?

Si el proyecto solo usa el LLM para una función secundaria, conviene optar por una API sencilla y barata. Si el proyecto depende de análisis documental o RAG, la calidad de embeddings y el coste por uso pasan a ser decisivos.

---

## Costes a tener en cuenta

1. Tokens de entrada.
2. Tokens de salida.
3. Uso de embeddings.
4. Número de llamadas a la API.
5. Coste de herramientas o almacenamiento adicionales en sistemas RAG.

El tamaño de la ventana de contexto no implica que siempre haya que llenarla. En la práctica, una buena selección de contexto suele ser más barata y más eficaz.

---

## Recomendaciones generales

| Necesidad | Recomendación general |
|-----------|-----------------------|
| Integración rápida | OpenAI |
| Contexto largo y análisis documental | Anthropic o Google |
| Ecosistema Azure | Azure OpenAI |
| RAG y embeddings | OpenAI o Cohere |
| Modelos abiertos o bajo coste | Hugging Face, Together AI o Fireworks |

---

## Fuentes recomendadas

- Documentación oficial de OpenAI.
- Documentación oficial de Azure OpenAI.
- Documentación oficial de Anthropic.
- Documentación oficial de Google AI y Vertex AI.
- Documentación oficial de Cohere.
- Documentación oficial de Hugging Face Inference API.
- Documentación oficial de vLLM y Text Generation Inference.
