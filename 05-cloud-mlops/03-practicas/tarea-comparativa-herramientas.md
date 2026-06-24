# Tarea: Comparativa de Herramientas Cloud para IA

## Objetivo

Analizar y comparar herramientas cloud para IA con el fin de decidir cuáles encajan mejor en el proyecto del grupo.

## Forma de trabajo

Trabajo en grupo con reparto por categorías. Cada miembro se responsabiliza de una categoría y el equipo consolida después una propuesta conjunta.

## Categorías de trabajo

| # | Tipo de herramienta |
|---|---------------------|
| 1 | Feature Store |
| 2 | Compute Cloud |
| 3 | MLOps |
| 4 | Frameworks de ML |
| 5 | APIs de LLM |
| 6 | Orquestación y agentes |
| 7 | Herramientas de datos |
| 8 | Almacenamiento |

Si el grupo tiene más o menos miembros, se pueden redistribuir categorías, pero todas deben quedar cubiertas en el documento final de grupo.

---

## Descripción del proyecto

Antes de empezar, cada grupo debe definir de forma breve:

```text
Proyecto: ...
Fuentes de datos: ...
Problema a resolver: ...
Usuarios o contexto de uso: ...
```

Esta descripción debe aparecer tanto en los documentos individuales como en el documento grupal.

---

## Qué debe hacer cada miembro

Cada miembro analiza una categoría concreta y entrega un documento individual.

### En cada documento individual debe aparecer

1. Una breve descripción del proyecto del grupo.
2. Al menos 2 alternativas comparadas, preferiblemente 3 si la categoría lo permite.
3. Un análisis de aplicación al proyecto concreto.
4. Una herramienta elegida o, si no aplica, una justificación de por qué no se usará.
5. Un ejemplo de uso, configuración o fragmento de código relacionado.
6. Las fuentes principales consultadas.

---

## Qué debe hacer el grupo

El grupo entregará además un documento consolidado con:

1. La descripción común del proyecto.
2. Un resumen de las decisiones tomadas en cada categoría.
3. La justificación de conjunto de la solución elegida.
4. Una arquitectura simple o flujo de componentes.
5. Una explicación de por qué las herramientas elegidas son coherentes entre sí.

El documento grupal no debe ser una simple copia de los documentos individuales. Debe sintetizar y justificar la solución final.

---

## Orientaciones por categoría

### 1. Feature Store

- Investigar alternativas como Feast, Tecton, Hopsworks o servicios equivalentes de plataformas cloud.
- Comparar coste, complejidad, latencia, integración y utilidad para entrenamiento e inferencia.
- Valorar si el proyecto necesita features reutilizables, en tiempo real o compartidas entre modelos.

### 2. Compute Cloud

- Investigar alternativas como EC2, SageMaker, Vertex AI, Azure ML, Lambda Labs o Paperspace.
- Comparar precio, disponibilidad de GPU, facilidad de uso y nivel de gestión.
- Valorar si el proyecto necesita GPU, escalado o simplemente un entorno gestionado.

### 3. MLOps

- Investigar alternativas como MLflow, Weights & Biases, ClearML o plataformas integradas.
- Comparar tracking, registro de modelos, despliegue y monitorización.
- Valorar si el proyecto necesita trazabilidad, versionado o paso a producción.

### 4. Frameworks de ML

- Investigar alternativas como PyTorch, TensorFlow, scikit-learn o Hugging Face.
- Comparar curva de aprendizaje, comunidad, integración cloud y adecuación al tipo de modelo.
- Valorar qué framework encaja mejor con el problema y los datos del proyecto.

### 5. APIs de LLM

- Investigar alternativas como OpenAI, Anthropic, Google o Cohere.
- Comparar coste, modelos disponibles, tamaño de contexto, embeddings y limitaciones.
- Valorar si el proyecto necesita generación de texto, clasificación, resumen o RAG.

### 6. Orquestación y agentes

- Investigar alternativas como LangChain, LangGraph, LlamaIndex, AutoGen o CrewAI.
- Comparar facilidad, comunidad, enfoque y casos de uso.
- Valorar si el proyecto necesita RAG, herramientas, cadenas complejas o agentes.

### 7. Herramientas de datos

- Investigar alternativas como Polars, Dask, Spark o DuckDB.
- Comparar rendimiento, facilidad de uso, escala y compatibilidad con el flujo de datos.
- Valorar el tamaño de los datos y el tipo de procesamiento necesario.

### 8. Almacenamiento

- Investigar alternativas como S3, GCS, Azure Blob, Delta Lake o Iceberg.
- Comparar precio, formato, integraciones y operaciones habituales.
- Valorar si el proyecto necesita versionado, tablas transaccionales o almacenamiento barato.

---

## Formato de entrega individual

Cada documento individual puede seguir esta plantilla:

```markdown
# Comparativa: [Categoría]

## Proyecto
- Proyecto: ...
- Fuentes de datos: ...
- Problema a resolver: ...
- Contexto de uso: ...

## 1. Alternativas investigadas
| Herramienta | Coste | Dificultad | Ventajas | Inconvenientes |
|-------------|-------|------------|----------|----------------|
| Herramienta A | ... | ... | ... | ... |
| Herramienta B | ... | ... | ... | ... |
| Herramienta C | ... | ... | ... | ... |

## 2. Análisis para el proyecto
[Explicar cómo aplica o no aplica al proyecto del grupo]

## 3. Herramienta elegida
[Herramienta seleccionada o "No aplica"]

## 4. Justificación
[Explicar por qué se elige]

## 5. Ejemplo de uso
[Código, configuración o ejemplo breve]

## 6. Fuentes consultadas
- Fuente 1
- Fuente 2
```

---

## Formato de entrega grupal

El documento consolidado puede seguir esta estructura:

```markdown
# Proyecto: [Nombre]

## 1. Descripción del proyecto
- Fuentes de datos
- Problema a resolver
- Usuarios o contexto

## 2. Decisiones por categoría
| Categoría | Herramienta elegida | Justificación breve |
|-----------|---------------------|---------------------|
| Feature Store | ... | ... |
| Compute | ... | ... |
| MLOps | ... | ... |
| Framework | ... | ... |
| APIs de LLM | ... | ... |
| Orquestación | ... | ... |
| Datos | ... | ... |
| Almacenamiento | ... | ... |

## 3. Coherencia de la solución
[Explicar cómo encajan las herramientas entre sí]

## 4. Arquitectura o flujo
[Diagrama simple o descripción]

## 5. Fuentes principales
- Fuente 1
- Fuente 2
```

---

## Recomendaciones

- No elegir una herramienta solo porque sea popular.
- Si una categoría no aplica al proyecto, justificarlo claramente.
- Evitar comparativas genéricas desconectadas del proyecto.
- Usar fuentes fiables y actualizadas.
- Mantener consistencia entre la parte individual y la propuesta grupal.
