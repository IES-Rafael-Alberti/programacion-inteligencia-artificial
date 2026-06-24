# FastAPI: documentación práctica

FastAPI es un framework web moderno para construir APIs con Python. En aplicaciones de IA es útil cuando una demo Gradio se queda corta y se necesita una API profesional, documentada y preparada para integrarse con otros sistemas.

## FastAPI frente a Gradio

| Aspecto | Gradio | FastAPI |
|---|---|---|
| Objetivo | Demo interactiva | API de producción |
| Interfaz visual | Integrada | No, expone endpoints |
| Validación de datos | Básica | Fuerte con Pydantic |
| Documentación automática | Básica | OpenAPI, Swagger y ReDoc |
| Autenticación | Limitada | API keys, OAuth2, JWT |
| Integración con otros sistemas | Media | Alta |
| Escalabilidad | Prototipos | Producción |

## Estructura básica

```python
from fastapi import FastAPI

app = FastAPI(title="API de modelo de IA")

@app.get("/")
def root():
    return {"status": "ok"}
```

## Modelos de entrada y salida

FastAPI usa Pydantic para validar datos.

```python
from pydantic import BaseModel, Field

class PredictInput(BaseModel):
    sepal_length: float = Field(..., ge=0, le=10)
    sepal_width: float = Field(..., ge=0, le=5)
    petal_length: float = Field(..., ge=0, le=7)
    petal_width: float = Field(..., ge=0, le=3)

class PredictOutput(BaseModel):
    prediction: str
    probabilities: dict[str, float]
```

## Endpoint de predicción

```python
@app.post("/predict", response_model=PredictOutput)
def predict(input_data: PredictInput):
    X = [[
        input_data.sepal_length,
        input_data.sepal_width,
        input_data.petal_length,
        input_data.petal_width,
    ]]
    pred = model.predict(X)[0]
    probs = model.predict_proba(X)[0]
    return PredictOutput(
        prediction=target_names[pred],
        probabilities={name: float(prob) for name, prob in zip(target_names, probs)},
    )
```

## Carga del modelo al iniciar

```python
@app.on_event("startup")
def load_model():
    global model
    model = cargar_modelo("modelo.pkl")
```

## Documentación automática

FastAPI genera documentación automáticamente:

1. `http://localhost:8000/docs`: Swagger UI.
2. `http://localhost:8000/redoc`: ReDoc.
3. `http://localhost:8000/openapi.json`: especificación OpenAPI.

## Autenticación sencilla con API key

```python
from fastapi import Header, HTTPException

def check_api_key(x_api_key: str = Header(...)):
    if x_api_key != "clave-secreta":
        raise HTTPException(status_code=401, detail="API key inválida")
```

## WebSockets y streaming

FastAPI puede servir respuestas progresivas, útil para LLMs.

```python
from fastapi import WebSocket

@app.websocket("/ws/generate")
async def generate(ws: WebSocket):
    await ws.accept()
    prompt = await ws.receive_text()
    for token in generar_tokens(prompt):
        await ws.send_text(token)
```

## Integración con MLflow

FastAPI puede cargar un modelo registrado en MLflow y exponerlo como API.

```python
import mlflow

model = mlflow.pyfunc.load_model("models:/IrisClassifier/Production")
```

## Despliegue

```bash
uvicorn main:app --reload --port 8000
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

Ejemplo de `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Buenas prácticas

1. Validar entradas con Pydantic.
2. Cargar el modelo una vez al iniciar, no en cada petición.
3. Separar lógica de inferencia y endpoints.
4. Añadir control de errores.
5. Proteger endpoints sensibles.
6. Registrar versión del modelo y fecha de despliegue.

## Cuándo usar FastAPI

Usa FastAPI cuando quieras que un modelo sea consumido por otras aplicaciones, servicios web, frontends o pipelines de producción.

No es necesario para una demo rápida de clase; en ese caso Gradio suele ser más directo.

## Instalación

```bash
pip install fastapi uvicorn
```

Documentación oficial: https://fastapi.tiangolo.com/
