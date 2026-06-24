# LangChain: documentación práctica

LangChain es un framework para construir aplicaciones basadas en modelos de lenguaje. Su función principal es organizar prompts, modelos, herramientas, memoria y recuperación de contexto como piezas conectadas dentro de un flujo de trabajo.

## Por qué no es solo llamar a un modelo

Una llamada directa a un LLM consiste en enviar un prompt y recibir una respuesta. LangChain aporta estructura cuando la aplicación necesita varios pasos, integración con datos externos o uso de herramientas.

| Necesidad | Llamada directa | LangChain |
|---|---|---|
| Prompt fijo | Sí | Sí |
| Plantillas reutilizables | Manual | Integrado |
| Memoria conversacional | Manual | Integrada |
| Herramientas externas | Manual | Integradas |
| RAG | Manual | Integrado |
| Agentes | Difícil | Soportado |
| Trazabilidad del flujo | Manual | Más estructurada |

## Componentes principales

### Prompt templates

Permiten crear prompts reutilizables con variables.

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Responde de forma breve a esta pregunta: {question}"
)

texto = prompt.format(question="¿Qué es una red neuronal?")
print(texto)
```

### Modelos de chat

LangChain permite cambiar de proveedor manteniendo una interfaz parecida.

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
respuesta = llm.invoke("Explica qué es el sobreajuste")
print(respuesta.content)
```

También puede integrarse con Ollama para modelos locales:

```python
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")
```

### Cadenas

Una cadena conecta varios pasos. En LangChain moderno se usan composiciones con `|`.

```python
chain = prompt | llm
respuesta = chain.invoke({"question": "¿Qué es RAG?"})
```

### Output parsers

Transforman la respuesta del modelo en un formato útil: texto, JSON, listas o modelos Pydantic.

```python
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

class Respuesta(BaseModel):
    answer: str
    confidence: float

parser = PydanticOutputParser(pydantic_object=Respuesta)
```

### Herramientas

Una herramienta es una función externa que el modelo o el agente puede usar.

```python
from langchain.tools import tool

@tool
def calcular(expresion: str) -> str:
    """Calcula una expresión matemática sencilla."""
    return str(eval(expresion))
```

### Memoria

La memoria guarda información de conversaciones anteriores.

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)
memory.save_context({"input": "Me llamo Ana"}, {"output": "Encantado, Ana"})
```

### RAG

RAG significa `Retrieval Augmented Generation`. El sistema recupera documentos relevantes y después genera una respuesta usando ese contexto.

Flujo típico:

1. El usuario pregunta.
2. Un recuperador busca documentos relacionados.
3. Se construye un prompt con pregunta y contexto.
4. El LLM responde usando ese contexto.
5. La aplicación puede devolver también las fuentes.

```python
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()
vectorstore = Chroma(embedding_function=embeddings, persist_directory="chroma_db")
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
```

### Agentes

Un agente decide qué herramienta usar y en qué orden. Es útil cuando el flujo no está completamente fijado.

```python
from langchain.agents import create_tool_calling_agent, AgentExecutor

# agent = create_tool_calling_agent(llm, tools, prompt)
# executor = AgentExecutor(agent=agent, tools=tools)
```

## LangChain frente a LlamaIndex y DSPy

| Herramienta | Foco principal |
|---|---|
| LangChain | Componer flujos con LLM, herramientas, memoria y agentes |
| LlamaIndex | Construir RAG sobre documentos propios |
| DSPy | Optimizar prompts y módulos con ejemplos y métricas |
| LangGraph | Orquestar flujos con estado, ciclos y decisiones |

## Buenas prácticas

1. Separar cada paso del pipeline: entrada, prompt, recuperación, modelo y parser.
2. Usar trazas para saber qué ha ocurrido en cada paso.
3. No enviar demasiado contexto al modelo.
4. Validar la salida cuando se espera JSON o una estructura concreta.
5. Manejar fallos de APIs externas con alternativas o mensajes claros.
6. Usar LangGraph si aparecen ciclos, reintentos complejos o estados compartidos.

## Errores frecuentes

1. Usar LangChain para una llamada simple que no lo necesita.
2. Mezclar toda la lógica en una sola función.
3. No separar recuperación y generación en sistemas RAG.
4. No guardar trazas, lo que dificulta la depuración.
5. Confiar en un agente sin limitar herramientas, iteraciones o permisos.

## Relación con los notebooks

### `Fase1/94_langchain_intro.ipynb`

Introduce la idea de cadena con funciones Python: normalización, plantilla, trazas y recuperación local.

### `Fase2/97_langchain_pipeline.ipynb`

Amplía el patrón con memoria, consulta externa, caché, extracción de entidad y fallback offline.

## Cuándo usar LangChain

Usa LangChain cuando necesites componer varios pasos alrededor de un LLM: prompts, memoria, herramientas, APIs, recuperación de contexto o agentes.

No es imprescindible si solo necesitas enviar un prompt fijo a un modelo y mostrar la respuesta.

## Instalación

```bash
pip install langchain langchain-openai langchain-community
```

Documentación oficial: https://python.langchain.com/
