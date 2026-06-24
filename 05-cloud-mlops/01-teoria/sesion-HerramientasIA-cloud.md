# Herramientas Cloud para IA

Unidad 5 del módulo de Programación en Inteligencia Artificial.

## Introducción

Esta unidad presenta la cadena de herramientas cloud más habitual en proyectos de IA: almacenamiento, cómputo, frameworks, MLOps, APIs de modelos, orquestación y procesamiento de datos. El objetivo no es memorizar servicios, sino aprender a comparar alternativas y justificar decisiones técnicas para un proyecto real.

## Resultados de aprendizaje

Al finalizar la unidad, el alumnado deberá ser capaz de:

- Identificar las principales categorías de herramientas cloud usadas en proyectos de IA.
- Comparar varias alternativas dentro de cada categoría.
- Relacionar una herramienta con las necesidades de un proyecto concreto.
- Justificar una elección técnica con criterios de coste, complejidad, integración y escalabilidad.
- Integrar varias decisiones en una propuesta de arquitectura coherente.

---

## Contenido

### 1. Infraestructura y ciclo de vida

| Tema | Archivo | Descripción |
|------|---------|-------------|
| Feature Store | [01-feature-store.md](./Documentacion/01-feature-store.md) | Repositorio de variables y features para entrenamiento e inferencia |
| Compute Cloud | [02-compute-cloud.md](./Documentacion/02-compute-cloud.md) | Infraestructura de ejecución, GPUs y entornos gestionados |
| MLOps | [03-mlops.md](./Documentacion/03-mlops.md) | Seguimiento de experimentos, registro, despliegue y monitorización |
| Almacenamiento | [04-almacenamiento-ia.md](./Documentacion/04-almacenamiento-ia.md) | Almacenamiento orientado a datos y artefactos de IA |

### 2. Desarrollo y procesamiento

| Tema | Archivo | Descripción |
|------|---------|-------------|
| Frameworks ML | [05-frameworks-ml.md](./Documentacion/05-frameworks-ml.md) | Frameworks y librerías para entrenamiento e inferencia |
| APIs de LLM | [06-apis-llm.md](./Documentacion/06-apis-llm.md) | Servicios de modelos de lenguaje y embeddings |
| Orquestación y agentes | [07-orquestacion-agents.md](./Documentacion/07-orquestacion-agents.md) | Frameworks para RAG, cadenas, herramientas y agentes |
| Herramientas de datos | [08-herramientas-datos.md](./Documentacion/08-herramientas-datos.md) | Librerías y motores para procesamiento de datos |

### 3. Recuperación, evaluación y serving

| Tema | Archivo | Descripción |
|------|---------|-------------|
| Bases vectoriales | [09-bases-vectoriales-recuperacion.md](./Documentacion/09-bases-vectoriales-recuperacion.md) | Recuperación semántica, índices y bases vectoriales |
| Evaluación y observabilidad | [10-evaluacion-observabilidad-llm.md](./Documentacion/10-evaluacion-observabilidad-llm.md) | Calidad, trazas, métricas y análisis de aplicaciones con LLM |
| Serving de modelos abiertos | [11-serving-modelos-abiertos.md](./Documentacion/11-serving-modelos-abiertos.md) | Despliegue e inferencia de modelos open source |
| Recuperación avanzada para RAG | [12-recuperacion-avanzada-rag.md](./Documentacion/12-recuperacion-avanzada-rag.md) | Jerarquías documentales, búsqueda híbrida, reranking y PageIndex |

### 4. Material de apoyo para clase

| Tema | Archivo | Descripción |
|------|---------|-------------|
| Ejemplos de stacks | [13-ejemplos-stacks-ia.md](./Documentacion/13-ejemplos-stacks-ia.md) | Combinaciones típicas de herramientas para proyectos de IA |
| Guion de clase final | [14-guion-clase-recuperacion-stacks.md](./Documentacion/14-guion-clase-recuperacion-stacks.md) | Propuesta de 1-2 sesiones para contextualizar herramientas y stacks |
| Demo RAG sencillo | [15-demo-rag-sencillo.md](./Demos/15-demo-rag-sencillo.md) | Guion técnico de una demo breve de RAG para clase |
| Notebook-esqueleto | [16-demo-rag-sencillo.ipynb.md](./Demos/16-demo-rag-sencillo.ipynb.md) | Base de notebook o script para la demo de clase |
| Demo RAG con Ollama | [17-demo-rag-ollama.md](./Demos/17-demo-rag-ollama.md) | Variante local de la demo para usar modelos elegidos por el alumnado |
| Demo RAG con PageIndex | [18-demo-pageindex-rag.md](./Demos/18-demo-pageindex-rag.md) | Alternativa a chunking para documentos largos y estructurados |
| Notebook PageIndex | [18-demo-pageindex-rag.ipynb.md](./Demos/18-demo-pageindex-rag.ipynb.md) | Guion por celdas para explicar recuperación estructurada |
| Chuleta Ollama | [19-chuleta-modelos-ollama.md](./Documentacion/19-chuleta-modelos-ollama.md) | Guía rápida para elegir modelos según el equipo disponible |

### 5. Actividad y evaluación

| Tema | Archivo | Descripción |
|------|---------|-------------|
| Tarea | [tarea-comparativa-herramientas.md](./Tareas/tarea-comparativa-herramientas.md) | Instrucciones de la actividad individual y grupal |
| Rúbrica | [rubrica-tarea.md](./Tareas/rubrica-tarea.md) | Criterios de evaluación |

---

## Flujo de trabajo típico

```text
Datos y artefactos
        |
        v
Almacenamiento y herramientas de datos
        |
        v
Compute cloud + frameworks de ML
        |
        v
Experimentación y MLOps
        |
        +--> Feature store
        |
        +--> APIs de LLM / orquestación
        |
        v
Despliegue e inferencia
```

Este flujo no es lineal en todos los proyectos, pero ayuda a entender cómo se combinan las categorías estudiadas.

---

## Actividad de la unidad

La actividad principal consiste en analizar herramientas cloud para IA y seleccionar las más adecuadas para un proyecto del grupo.

### Productos de la actividad

- Un documento individual por tipo de herramienta.
- Un documento grupal consolidado con la propuesta final.

### Qué debe demostrar el alumnado

- Que ha investigado alternativas reales.
- Que sabe comparar herramientas con criterios técnicos.
- Que conecta la herramienta con el proyecto concreto.
- Que toma decisiones justificadas, no solo descriptivas.

### Relación con la evaluación

La tarea y la rúbrica están alineadas con la misma lógica:

- Parte individual: análisis de una categoría concreta.
- Parte grupal: integración coherente de las elecciones del equipo.

---

## Secuencia didáctica mínima

### 1. Activación

- Presentación breve del ecosistema cloud de IA.
- Revisión de las categorías de herramientas de la unidad.
- Identificación del proyecto del grupo y sus necesidades.

### 2. Desarrollo

- Lectura guiada de los documentos temáticos.
- Reparto de categorías entre los miembros del grupo.
- Investigación y comparación de alternativas por categorías.
- Puesta en común de hallazgos y dependencias entre herramientas.

### 3. Aplicación

- Redacción de los documentos individuales.
- Selección conjunta de una solución técnica coherente.
- Elaboración del documento grupal consolidado.

### 4. Cierre

- Presentación breve de las decisiones del grupo.
- Revisión de coherencia entre componentes.
- Autoevaluación con la rúbrica antes de la entrega.

---

## Orientaciones didácticas

- No todas las categorías tienen que ser imprescindibles para todos los proyectos.
- Si una categoría no aplica, debe justificarse con claridad.
- Se valora más una comparación razonada que una lista larga de servicios.
- Las decisiones deben apoyarse en el contexto del proyecto: datos, escala, coste, complejidad y mantenimiento.
- Como mejora futura, se puede preparar una versión breve para alumnado y otra ampliada para profesorado.

---

## Recursos y fuentes recomendadas

### Recursos generales

- Documentación oficial de AWS, Google Cloud y Microsoft Azure.
- Documentación oficial de MLflow, Weights & Biases y ClearML.
- Documentación oficial de PyTorch, TensorFlow, scikit-learn y Hugging Face.
- Documentación oficial de OpenAI, Anthropic, Google AI y Cohere.
- Documentación oficial de LangChain, LangGraph, LlamaIndex, AutoGen y CrewAI.
- Documentación oficial de Polars, Dask, Spark y DuckDB.

### Criterio para usar fuentes

- Priorizar documentación oficial y comparativas técnicas actualizadas.
- Evitar basar la decisión solo en blogs promocionales.
- Contrastar siempre coste, limitaciones y requisitos de integración.
