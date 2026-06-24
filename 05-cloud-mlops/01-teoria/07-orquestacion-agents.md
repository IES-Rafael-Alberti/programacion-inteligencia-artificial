# Orquestación y agentes

## Introducción

Los frameworks de orquestación permiten construir aplicaciones con LLM que van más allá de una llamada aislada a una API. Sirven para encadenar pasos, usar herramientas, consultar documentos, mantener estado y coordinar agentes.

## Cuándo hacen falta

- Cuando el proyecto usa RAG.
- Cuando hay varios pasos encadenados.
- Cuando el modelo debe usar herramientas externas.
- Cuando interesa separar tareas entre varios agentes o roles.

Si el proyecto solo necesita una llamada simple a un LLM, probablemente no hace falta añadir esta capa.

---

## LangChain

### Qué aporta

- Construcción de chains y pipelines.
- Integración con modelos, embeddings, vector stores y tools.
- Ecosistema muy amplio.

### Casos típicos

- Chatbots con contexto.
- Pipelines con varios pasos.
- Integración de herramientas y recuperadores.

---

## LangGraph

### Qué aporta

- Flujos con estado y ramificaciones.
- Mejor control para agentes y procesos no lineales.

### Casos típicos

- Agentes con memoria o revisión.
- Procesos donde un nodo decide el siguiente paso.

---

## LlamaIndex

### Qué aporta

- Enfoque muy orientado a RAG y consulta sobre documentos.
- Buenas utilidades para ingesta, indexación y recuperación.

### Casos típicos

- Chat sobre documentos.
- Bases de conocimiento.
- Preguntas y respuestas sobre archivos propios.

---

## AutoGen

### Qué aporta

- Enfoque multiagente.
- Interacción entre agentes con roles diferenciados.

### Casos típicos

- Sistemas colaborativos entre varios agentes.
- Flujos de generación, revisión y ejecución.

---

## CrewAI

### Qué aporta

- Modelo conceptual simple basado en agentes, tareas y equipo.
- Útil para organizar procesos de varios roles.

### Casos típicos

- Automatización por roles.
- Demostraciones docentes de multiagente.

## Otras alternativas abiertas

### Haystack

- Framework open source muy útil para RAG, búsqueda y pipelines de preguntas y respuestas.
- Buen contrapunto a LangChain cuando se quiere un enfoque más centrado en recuperación.

### DSPy

- Framework open source orientado a programar y optimizar pipelines con LLM.
- Interesante para un enfoque más cercano a programación declarativa de módulos.

### PydanticAI

- Opción open source con fuerte integración con Python y tipado.
- Útil para proyectos donde interesa simplicidad y control del código.

---

## Comparativa

| Herramienta | Enfoque | Mejor encaje |
|-------------|---------|--------------|
| LangChain | Generalista | Chains, tools, integración |
| LangGraph | Flujo con estado | Agentes y procesos complejos |
| LlamaIndex | RAG | Consulta documental |
| AutoGen | Multiagente | Interacción entre agentes |
| CrewAI | Multiagente orientado a tareas | Organización por roles |
| Haystack | RAG y búsqueda | Sistemas documentales |
| DSPy | Programación de pipelines LLM | Experimentación avanzada |
| PydanticAI | Integración Python tipada | Proyectos sencillos y controlados |

---

## Aplicación al proyecto

Antes de elegir un framework de orquestación conviene responder:

1. ¿El proyecto necesita RAG o solo una llamada simple al modelo?
2. ¿Hay herramientas externas que el LLM deba usar?
3. ¿Se necesita memoria, estado o varios pasos de decisión?
4. ¿Tiene sentido usar varios agentes o sería complejidad innecesaria?

En proyectos docentes es habitual que LangChain o LlamaIndex sean suficientes. Los sistemas multiagente deben justificarse bien, porque añaden complejidad técnica y conceptual.

---

## Recomendaciones generales

| Caso | Herramienta |
|------|-------------|
| RAG simple | LlamaIndex |
| RAG con foco en búsqueda | Haystack |
| Chains con herramientas | LangChain |
| Flujo con estado | LangGraph |
| Multiagente | AutoGen o CrewAI |
| Proyecto sencillo | Ninguna, si no aporta valor real |

---

## Ejemplo conceptual de RAG

```text
Documentos -> fragmentación -> embeddings -> índice vectorial -> recuperación -> LLM -> respuesta
```

Este patrón suele ser más importante que el framework concreto elegido.

---

## Fuentes recomendadas

- Documentación oficial de LangChain.
- Documentación oficial de LangGraph.
- Documentación oficial de LlamaIndex.
- Documentación oficial de AutoGen.
- Documentación oficial de CrewAI.
- Documentación oficial de Haystack.
- Documentación oficial de DSPy.
- Documentación oficial de PydanticAI.
