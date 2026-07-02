# LangGraph: documentación práctica

LangGraph es una extensión del ecosistema LangChain para construir flujos de trabajo con estado, ciclos y decisiones. Es útil cuando una cadena lineal no basta y se necesita controlar cómo avanza un agente paso a paso.

## Por qué usar LangGraph

LangChain permite componer cadenas y agentes. LangGraph añade una estructura de grafo: nodos, aristas, estado compartido y rutas condicionales.

| Necesidad | LangChain | LangGraph |
|---|---|---|
| Cadena lineal | Sí | Sí |
| Decisiones condicionales | Limitado | Sí |
| Ciclos y reintentos | Difícil | Sí |
| Estado compartido | Manual | Integrado |
| Agentes complejos | Posible | Más controlable |
| Human-in-the-loop | Manual | Más natural |

## Conceptos principales

### Estado

El estado es la información compartida entre nodos: pregunta, mensajes, contexto, respuesta, número de intentos, etc.

```python
from typing import TypedDict

class AgentState(TypedDict):
    question: str
    context: list
    answer: str
    attempts: int
```

### Nodos

Un nodo es una función que recibe el estado y devuelve cambios en ese estado.

```python
def retrieve_node(state: AgentState):
    docs = retriever.invoke(state["question"])
    return {"context": docs}
```

### Aristas

Las aristas conectan nodos.

```python
workflow.add_edge("retrieve", "generate")
```

### Aristas condicionales

Permiten decidir la siguiente ruta según el estado.

```python
def route_after_validation(state):
    if state["attempts"] >= 3:
        return "finish"
    if not state["answer"]:
        return "retry"
    return "finish"
```

## Ejemplo básico

```python
from langgraph.graph import StateGraph, END

workflow = StateGraph(AgentState)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()
```

## Ejemplo con reintento

```python
def validate_node(state):
    valid = bool(state.get("answer")) and len(state.get("context", [])) > 0
    return {"valid": valid}

def route(state):
    if state["valid"]:
        return "finish"
    if state["attempts"] < 3:
        return "retry"
    return "finish"

workflow.add_conditional_edges(
    "validate",
    route,
    {"retry": "retrieve", "finish": END},
)
```

## LangGraph con herramientas

LangGraph puede combinarse con herramientas de LangChain.

```python
from langchain_core.tools import tool

@tool
def buscar_wikipedia(query: str) -> str:
    """Busca información en Wikipedia."""
    return "resultado simulado"
```

## Casos de uso

1. Agente que busca información, responde, valida y reintenta si la respuesta es débil.
2. Sistema RAG que cambia de estrategia si no encuentra contexto.
3. Flujo con revisión humana antes de publicar una respuesta.
4. Multiagente: un agente investiga, otro redacta y otro revisa.
5. Proceso con herramientas externas y límites de intentos.

## LangGraph frente a LangChain

Usa LangChain si el flujo es una cadena razonablemente lineal. Usa LangGraph si hay ciclos, estados compartidos, ramas condicionales o reintentos.

## Buenas prácticas

1. Definir un estado pequeño y claro.
2. Nombrar los nodos según la acción que realizan.
3. Limitar reintentos para evitar bucles infinitos.
4. Guardar trazas del camino seguido por el grafo.
5. Empezar con un grafo simple y añadir ramas solo si hacen falta.

## Errores frecuentes

1. Usar LangGraph para una cadena simple.
2. Crear demasiados nodos desde el principio.
3. No controlar el número máximo de reintentos.
4. Mezclar demasiada lógica dentro de un único nodo.
5. No documentar qué contiene el estado.

## Relación con los notebooks

El notebook `Fase2/99_herramientas_ia_integradas.ipynb` incluye una simulación de flujo con estado inspirado en LangGraph.

## Instalación

```bash
pip install langgraph
```

Documentación oficial: https://langchain-ai.github.io/langgraph/
