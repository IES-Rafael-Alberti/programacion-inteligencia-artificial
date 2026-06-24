# F5 — Serving y APIs para Modelos de IA

**RA/CE**: RA3d (soluciones basadas en IA)
**Duración**: 4h teoría + 6h práctica
**Prerrequisitos**: UD6 (FastAPI básico, Pydantic), F4 (orquestación Prefect), F3 (Model Registry MLflow)

---

## Problema: Tu modelo está en un archivo, no en producción

Tienes el mejor modelo de clasificación de incidencias: accuracy del 92%, registrado en MLflow con todos sus artefactos. Pero ahora viene la pregunta difícil: **¿cómo le damos acceso a ese modelo a los usuarios reales?**

- El equipo de soporte necesita enviar un texto y recibir la categoría —desde su aplicación, no desde un notebook
- La aplicación móvil debe clasificar incidencias en tiempo real
- Necesitas controlar **quién** usa el modelo y **cuánto** lo usa
- Cuando saques una versión mejorada del modelo, los clientes antiguos deben seguir funcionando

**Un archivo `.pkl` no es un servicio**. Necesitas una API profesional: con autenticación, límites de uso, versionado y documentación automática.

---

## 1. Del Notebook a la API

### 1.1 ¿Qué aporta FastAPI al stack convergente?

En UD6 viste FastAPI para crear endpoints básicos. En UD7 llevamos FastAPI a un nivel profesional: el modelo servido se convierte en un **producto software** con los mismos estándares que cualquier API en producción.

| Aspecto | Endpoint básico (UD6) | API profesional (UD7) |
|---------|----------------------|----------------------|
| Validación | Manual | Pydantic models con esquemas completos |
| Autenticación | Sin auth | API key via header |
| Rate limiting | Sin límite | slowapi con límites por cliente |
| Versionado | Sin versiones | `/v1/predict`, `/v2/predict` |
| Documentación | Sin docs | OpenAPI/Swagger automático |
| Carga del modelo | Desde archivo local | Desde MLflow Model Registry |
| Monitorización | Sin logs | Logging estructurado + métricas |

### 1.2 Conexión con F4: Orquestación → Serving

```
F4: Prefect ejecuta pipeline semanal
 │
 ├── Carga datos nuevos
 ├── Re-entrena modelo
 ├── Registra nueva versión en MLflow (Stage: Staging)
 │
 ▼
F5: Nuevo modelo disponible en Model Registry
 │
 ├── Evaluación: ¿mejora al actual?
 ├── Si sí → promote a Production
 │         → FastAPI sirve la nueva versión
 │         → Endpoint /v2/predict con nuevo modelo
 │         → Clientes migran gradualmente
 └── Si no → se queda en Staging para referencia
```

**Esto es RA3d**: una solución basada en IA no es solo el modelo —es el sistema completo que lo sirve, lo versiona, lo asegura y lo monitoriza.

---

## 2. API Profesional con FastAPI

### 2.1 Validación con Pydantic

Pydantic no es opcional —es la primera línea de defensa contra datos mal formados:

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class PredictRequest(BaseModel):
    """Esquema de entrada para predicción."""
    text: str = Field(..., min_length=1, max_length=10000,
                      description="Texto de la incidencia")
    top_k: Optional[int] = Field(3, ge=1, le=10,
                                  description="Número de predicciones a devolver")

class PredictResponse(BaseModel):
    """Esquema de salida de predicción."""
    predicted_class: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    probabilities: dict[str, float]
    model_version: str
```

**Conexión con F2**: El mismo esquema de validación que usaste en pandera para datos tabulares ahora se aplica a las peticiones API —mismo principio, distinto contexto.

### 2.2 Carga del Modelo desde MLflow

En lugar de cargar el modelo desde un archivo local, lo cargamos desde el Model Registry:

```python
import mlflow
from fastapi import FastAPI

app = FastAPI(title="Ticket Classifier API")

@app.on_event("startup")
def load_model():
    """Carga el modelo en producción desde MLflow Model Registry."""
    global model, vectorizer
    model = mlflow.sklearn.load_model(
        "models:/TicketClassifier/Production"
    )  # ← Se actualiza automáticamente cuando cambia el modelo en Production
    print(f"✅ Modelo cargado: TicketClassifier/Production")
```

**Ventaja**: cuando Prefect promueve una nueva versión a `Production` en MLflow, solo necesitas reiniciar la API para servir el nuevo modelo. Sin cambios de código.

### 2.3 Endpoint de Inferencia

```python
from fastapi import HTTPException
import numpy as np

@app.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    """Clasifica un texto de incidencia."""
    try:
        # Vectorizar el texto de entrada
        X = vectorizer.transform([request.text])

        # Predecir
        pred_class = model.predict(X)[0]
        probs = model.predict_proba(X)[0]

        # Obtener top-k probabilidades
        top_indices = np.argsort(probs)[-request.top_k:][::-1]
        top_probs = {
            model.classes_[i]: float(probs[i])
            for i in top_indices
        }

        return PredictResponse(
            predicted_class=pred_class,
            confidence=float(probs[model.classes_.tolist().index(pred_class)]),
            probabilities=top_probs,
            model_version="production"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

---

## 3. Seguridad y Control de Acceso

### 3.1 Autenticación con API Key

Las API keys permiten controlar quién accede al modelo:

```python
from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

API_KEYS = {
    "sk-soporte-v1": "soporte",
    "sk-movil-v1": "app-movil",
    "sk-admin-v1": "admin",
}

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    """Verifica la API key y devuelve el cliente."""
    if api_key not in API_KEYS:
        raise HTTPException(
            status_code=401,
            detail="API Key inválida"
        )
    return API_KEYS[api_key]

@app.post("/predict")
async def predict(
    request: PredictRequest,
    client: str = Security(verify_api_key)
):
    # Loguear qué cliente usa el endpoint
    logger.info(f"Predict by {client}: {request.text[:50]}...")
    # ... lógica del endpoint
```

### 3.2 Rate Limiting

Protege tu API de abusos y asegura distribución equitativa del recurso:

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/predict")
@limiter.limit("100/minute")  ← Máximo 100 peticiones por minuto
async def predict(request: PredictRequest, api_key: str = Security(verify_api_key)):
    # ... lógica
```

**Estrategias de rate limiting comunes**:

| Estrategia | Ejemplo | Cuándo usarla |
|------------|---------|---------------|
| Por IP | `100/minute` | Clientes sin autenticar |
| Por API key | `1000/minute` | Clientes autenticados |
| Por endpoint | `10/minute` en `/predict` | Endpoints costosos |
| Global | `10000/hour` | Toda la API |

---

## 4. Versionado de Endpoints

### 4.1 Estrategia de Versionado

Los modelos mejoran con el tiempo. Necesitas que los clientes antiguos sigan funcionando mientras migras a la nueva versión:

```python
from fastapi import APIRouter

# Versión 1: modelo original
v1_router = APIRouter(prefix="/v1")

@v1_router.post("/predict")
async def predict_v1(request: PredictRequest):
    """Endpoint v1: modelo LogisticRegression."""
    model_v1 = mlflow.sklearn.load_model("models:/TicketClassifier/1")
    # ... lógica v1

# Versión 2: modelo mejorado con nuevo endpoint
v2_router = APIRouter(prefix="/v2")

@v2_router.post("/predict")
async def predict_v2(request: PredictRequest):
    """Endpoint v2: modelo XGBoost con categorías ampliadas."""
    model_v2 = mlflow.sklearn.load_model("models:/TicketClassifier/2")
    # ... lógica v2

app.include_router(v1_router)
app.include_router(v2_router)
```

**Esto habilita**:
- Clientes antiguos → `/v1/predict` (siguen funcionando sin cambios)
- Clientes nuevos → `/v2/predict` (beneficiándose del nuevo modelo)
- Migración gradual → los clientes se actualizan cuando pueden

### 4.2 Documentación Automática con OpenAPI

FastAPI genera automáticamente documentación interactiva:

```
/docs → Swagger UI: prueba todos los endpoints desde el navegador
/redoc → ReDoc: documentación estructurada alternativa
/openapi.json → Esquema OpenAPI para generación de clientes
```

Cada endpoint aparece con:
- Sus modelos Pydantic de entrada/salida
- Códigos de respuesta documentados (200, 401, 429, 500)
- Posibilidad de probar la API directamente desde el navegador

---

## 5. Puesta en Marcha

```bash
# Iniciar la API
uvicorn api.main:app --reload --port 8000

# Probar con curl (autenticado)
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -H "X-API-Key: sk-soporte-v1" \
  -d '{"text": "El servidor de producción no responde desde las 14:00"}'

# Probar sin API key (debe devolver 401)
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "test"}'

# Probar rate limiting (debe devolver 429 tras 100 peticiones/min)
for i in {1..101}; do
  curl -s -o /dev/null -w "%{http_code}\n" \
    -X POST http://localhost:8000/predict \
    -H "X-API-Key: sk-soporte-v1" \
    -H "Content-Type: application/json" \
    -d '{"text": "test"}'
done
```

---

## 6. Conexión con el Flujo Convergente

```
F4: Prefect orquesta re-entrenamiento semanal
 │
 ▼
MLflow: nueva versión del modelo en Staging
 │
 ▼
F5: FastAPI sirve el modelo
 ├── /v1/predict → modelo anterior (compatibilidad)
 ├── /v2/predict → modelo nuevo (early adopters)
 ├── API key + rate limiting → control de acceso
 └── Swagger UI → documentación viva
 │
 ▼
F7: Evidently monitorea predicciones en vivo
     Compara distribución actual vs. baseline
     Si hay drift → alerta → Prefect re-entrena
```

**Esta integración es RA3d en acción**: la solución basada en IA no es el modelo, es el sistema completo que lo sirve, controla su acceso, versiona sus versiones y se auto-corrige cuando la calidad baja.

---

## 7. Referencias a UD5 y UD6

**De UD6 (LLM/Agentes)**:
- `06-llm-agentes/03-practicas/103_fastapi_serving_modelos.ipynb` — Práctica de FastAPI con modelos
- Conceptos de Pydantic, endpoints REST, peticiones HTTP

**De UD5 (Cloud/MLOps)**:
- Concepto de API gateway y balanceo de carga

> Esta fase asume que conoces la sintaxis básica de FastAPI: decoradores de ruta, Path/Query parameters, y modelos Pydantic simples. Si necesitas repasar, revisa la práctica `103_fastapi_serving_modelos.ipynb` de UD6 antes de continuar.

---

## Resumen y Claves

1. **Una API profesional** no solo sirve predicciones —autentica, limita, versiona y documenta.
2. **Pydantic** es la primera línea de defensa: valida la entrada antes de que llegue al modelo.
3. **La carga desde MLflow Model Registry** permite cambiar de modelo sin modificar el código de la API.
4. **Las API keys** controlan quién accede al modelo; el **rate limiting** protege contra abusos.
5. **El versionado de endpoints** (`/v1`, `/v2`) permite migraciones graduales sin romper clientes.
6. **Swagger UI** (`/docs`) es la documentación viva de tu API —siempre actualizada.

**En la práctica F5**: Crearás una API FastAPI completa que carga un modelo desde MLflow, implementa autenticación con API key, rate limiting con slowapi, versionado de endpoints y la probarás con `httpx` desde el propio notebook.
