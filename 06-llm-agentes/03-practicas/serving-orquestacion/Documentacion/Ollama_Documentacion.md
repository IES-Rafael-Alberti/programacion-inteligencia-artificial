# Ollama: documentación práctica

Ollama permite ejecutar modelos de lenguaje localmente. Es útil para practicar con LLMs sin depender siempre de APIs en la nube, claves privadas o coste por token.

## Por qué usar Ollama

| Aspecto | API en la nube | Ollama local |
|---|---|---|
| Coste | Pago por uso | Sin coste de API |
| Privacidad | Los datos salen del equipo | Los datos permanecen en local |
| Conexión | Requiere Internet | Puede funcionar sin conexión |
| Rendimiento | Depende del proveedor | Depende del hardware local |
| Modelos | Propietarios o gestionados | Modelos abiertos descargables |

## Instalación

Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

macOS:

```bash
brew install ollama
```

## Uso desde terminal

```bash
ollama pull llama3
ollama run llama3 "Explica qué es una red neuronal en tres frases"
ollama list
```

## Uso desde Python

```python
import ollama

response = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": "¿Qué es el sobreajuste?"}],
)

print(response["message"]["content"])
```

## API local

Ollama expone una API HTTP local en `http://localhost:11434`.

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3", "prompt": "Define RAG", "stream": False},
)

print(response.json()["response"])
```

## Integración con LangChain

```python
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")
respuesta = llm.invoke("Explica qué es MLflow")
print(respuesta.content)
```

## Integración con LlamaIndex

```python
from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama3")
# query_engine = index.as_query_engine(llm=llm)
```

## Ollama con RAG

Ollama puede usarse como generador final en un sistema RAG:

1. LlamaIndex o LangChain recuperan documentos.
2. Ollama recibe pregunta y contexto.
3. El modelo local genera la respuesta.
4. La aplicación muestra respuesta y fuentes.

## Ollama con MLflow

MLflow puede registrar qué modelo local se ha usado, con qué prompt y con qué métricas.

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("llm_provider", "ollama")
    mlflow.log_param("model", "llama3")
    mlflow.log_param("local", True)
```

## Buenas prácticas

1. Usar modelos pequeños si el equipo tiene poca RAM.
2. Registrar qué modelo y versión se han usado.
3. No asumir que un modelo local tendrá la misma calidad que uno grande en la nube.
4. Evitar enviar documentos enormes sin recuperación previa.
5. Probar prompts y tiempos de respuesta antes de usarlo en clase.

## Errores frecuentes

1. Intentar usar un modelo que no está descargado.
2. No tener el servicio de Ollama ejecutándose.
3. Usar un modelo demasiado grande para el equipo.
4. Confundir privacidad local con exactitud de respuesta.
5. No controlar el tiempo de generación.

## Cuándo usar Ollama

Usa Ollama para prácticas sin coste, prototipos locales, privacidad de datos y pruebas con modelos abiertos.

No es la mejor opción si necesitas máxima calidad, alta concurrencia o despliegue productivo a gran escala; en esos casos puede interesar una API cloud o vLLM.

Documentación oficial: https://ollama.com/
