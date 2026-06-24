# Cheatsheet del Stack Convergente — UD7

Referencia rápida de todas las herramientas, comandos y conexiones del stack convergente.

---

## 1. Mapa del Stack

```
F2: Datos ──► F3: MLflow ──► F4: Prefect ──► F5: FastAPI ──► F6: CrewAI ──► F7: Evidently ──► F8: Guardrails+SHAP
(pandas)      (tracking)      (orquestación)   (serving)       (agentes)       (monitorización)   (IA responsable)
```

---

## 2. Herramientas — Comandos Esenciales

### MLflow (F3)

```bash
# Iniciar UI de tracking
mlflow ui --port 5000

# Registrar modelo en Registry
mlflow.register_model "runs:/<RUN_ID>/model" "TicketClassifier"

# Promover modelo a Production
# Desde MLflow UI: Stage → Production
# O vía API:
from mlflow.tracking import MlflowClient
client = MlflowClient()
client.transition_model_version_stage(
    name="TicketClassifier",
    version=2,
    stage="Production"
)

# Cargar modelo desde Registry
mlflow.sklearn.load_model("models:/TicketClassifier/Production")
```

**Tracking**: `mlflow.start_run()`, `mlflow.log_param()`, `mlflow.log_metric()`, `mlflow.log_artifact()`

### Prefect (F4)

```python
from prefect import flow, task

@task(retries=2, retry_delay_seconds=30)
def load_data():
    ...

@task
def train_model(data):
    ...

@flow(log_prints=True)
def pipeline():
    data = load_data()
    model = train_model(data)

pipeline()
```

```bash
# Iniciar servidor Prefect (opcional)
prefect server start

# Ejecutar flujo localmente
python pipeline.py

# Ver UI
# http://localhost:4200
```

### FastAPI (F5)

```python
from fastapi import FastAPI, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from slowapi import Limiter
from pydantic import BaseModel

app = FastAPI(title="API Clasificador")

# Modelos Pydantic
class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    predicted_class: str
    confidence: float

# Autenticación
api_key_header = APIKeyHeader(name="X-API-Key")

# Endpoint
@app.post("/v1/predict")
async def predict(req: PredictRequest, key: str = Security(api_key_header)):
    ...
```

```bash
# Iniciar
uvicorn src.api:app --reload --port 8000

# Probar
curl -X POST http://localhost:8000/v1/predict \
  -H "X-API-Key: sk-demo" \
  -H "Content-Type: application/json" \
  -d '{"text": "servidor caido"}'

# Docs
# http://localhost:8000/docs
```

### CrewAI (F6)

```python
from crewai import Agent, Task, Crew, Process

# Definir agente
agente = Agent(
    role="Clasificador",
    goal="Clasificar incidencias técnicas",
    backstory="Experto en soporte técnico",
    verbose=True
)

# Definir tarea
tarea = Task(
    description="Clasificar: {incidencia}",
    agent=agente,
    expected_output="Categoría y urgencia"
)

# Ejecutar crew
crew = Crew(
    agents=[agente],
    tasks=[tarea],
    process=Process.sequential
)
result = crew.kickoff(inputs={"incidencia": "texto"})
```

```bash
pip install crewai
```

### LlamaIndex hierarchical retrieval (F6)

```python
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import HierarchicalNodeParser, get_leaf_nodes
from llama_index.core.retrievers import RecursiveRetriever

# Índice multinivel: documento → sección → fragmento
node_parser = HierarchicalNodeParser.from_defaults(
    chunk_sizes=[2048, 512, 128]
)
nodes = node_parser.get_nodes_from_documents(documents)
leaf_nodes = get_leaf_nodes(nodes)

vector_index = VectorStoreIndex(leaf_nodes)
base_retriever = vector_index.as_retriever(similarity_top_k=4)

retriever = RecursiveRetriever(
    "vector",
    retriever_dict={"vector": base_retriever},
    node_dict={node.node_id: node for node in nodes},
    verbose=True,
)

results = retriever.retrieve("¿Qué incidencias afectan al parking Centro?")
```

```bash
pip install llama-index llama-index-embeddings-huggingface
```

### Evidently (F7)

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.test_suite import TestSuite
from evidently.tests import TestShareOfDriftedColumns

# Reporte de drift
report = Report(metrics=[
    DataDriftPreset(stattest="ks", drift_share=0.3)
])
report.run(reference_data=ref, current_data=cur)
report.save_html("drift_report.html")

# Tests con alertas
tests = TestSuite(tests=[
    TestShareOfDriftedColumns(gte=0.3)
])
tests.run(reference_data=ref, current_data=cur)
if tests.as_dict()["tests"][0]["status"] == "FAILED":
    print("⚠️ Drift detectado")
```

```bash
pip install evidently
```

### NeMo Guardrails (F8)

```python
from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("config/guardrails")
rails = LLMRails(config)

response = rails.generate(
    messages=[{"role": "user", "content": prompt}]
)
```

```bash
pip install nemoguardrails
```

### SHAP (F8)

```python
import shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Explicación individual
shap.force_plot(
    explainer.expected_value[1],
    shap_values[1][0],
    X_test[0:1],
    feature_names=feature_names
)
```

```bash
pip install shap
```

### Fairlearn (F8)

```python
from fairlearn.metrics import demographic_parity_difference

dpd = demographic_parity_difference(
    y_true=y_test,
    y_pred=y_pred,
    sensitive_features=groups
)
print(f"Diferencia de paridad: {dpd:.3f}")
```

```bash
pip install fairlearn
```

---

## 3. Conexiones Clave entre Herramientas

| Origen → Destino | Conexión | Código clave |
|-----------------|----------|-------------|
| **MLflow → FastAPI** | Cargar modelo desde Model Registry | `mlflow.sklearn.load_model("models:/Nombre/Production")` |
| **Prefect → MLflow** | Registrar experimentos orquestados | `mlflow.log_metric()` dentro de tarea Prefect |
| **Prefect → FastAPI** | Notificar nuevo modelo | `requests.post(".../reload")` o reinicio de API |
| **FastAPI → Evidently** | Pasar predicciones a monitorización | Logging JSON → Evidently comparación batch |
| **FastAPI → Guardrails** | Proteger endpoint | NeMo Rails antes de llamar al modelo |
| **FastAPI → SHAP** | Endpoint de explicabilidad | `/explain` que calcula SHAP values |
| **Prefect → Evidently** | Orquestar generación de reportes | Flow que ejecuta `drift_report.run()` periódicamente |
| **CrewAI → Evidently** | Evaluar calidad de agentes | Faithfulness, relevance → Evidently dashboard |

---

## 4. Pipeline Completo (Script de Referencia)

```python
# pipeline_completo.py
# Dependencias: pip install prefect mlflow evidently pandas scikit-learn

from prefect import flow, task
import mlflow
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

@task(retries=2)
def load_and_validate():
    data = pd.read_csv("data/incidencias.csv")
    assert data.shape[0] > 0
    return data

@task
def train_and_track(data):
    with mlflow.start_run():
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
        model.fit(data.drop("target", axis=1), data["target"])
        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_metric("accuracy", model.score(...))
        mlflow.sklearn.log_model(model, "model")
        return model

@task
def monitor_drift(ref, cur):
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=cur)
    report.save_html("reports/drift_latest.html")

@flow(log_prints=True)
def pipeline_completo():
    data = load_and_validate()
    model = train_and_track(data)
    monitor_drift(data, data.sample(frac=0.5))

if __name__ == "__main__":
    pipeline_completo()
```

---

## 5. Resolución de Problemas Comunes

| Problema | Causa posible | Solución |
|----------|--------------|----------|
| MLflow no encuentra el modelo | Stage incorrecto | Verificar en UI: `models:/Nombre/Production` |
| Evidently no genera reporte | Datos de referencia vacíos | Asegurar `reference_data` tiene datos |
| FastAPI no arranca | Puerto ocupado | `uvicorn ... --port 8001` |
| Prefect no ejecuta tareas | Decorador olvidado | Asegurar `@task` y `@flow` |
| CrewAI no encuentra modelo | Ollama no corriendo | `ollama pull llama3.2 && ollama serve` |
| Guardrails no filtra | Configuración incompleta | Revisar `config.yml` y `rails.co` |
| SHAP tarda mucho | Muchas features | Reducir a top-5 features explicadas |
| `pip install` falla | Python < 3.10 | `python3.10 -m venv .venv` |

---

## 6. Checklist de Integración

- [ ] ¿MLflow tiene el modelo en Production?
- [ ] ¿Prefect orquesta el pipeline completo?
- [ ] ¿FastAPI carga desde MLflow Model Registry?
- [ ] ¿La API tiene autenticación y rate limiting?
- [ ] ¿CrewAI accede al modelo servido?
- [ ] ¿Evidently monitoriza las predicciones?
- [ ] ¿SHAP puede explicar predicciones individuales?
- [ ] ¿Hay guardrails protegiendo la API?
- [ ] ¿El pipeline completo se ejecuta con un solo comando?

---

## 7. Referencia Rápida de Comandos

```bash
# Entorno
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# MLflow
mlflow ui --port 5000

# Prefect
prefect server start  # opcional

# FastAPI
uvicorn src.api:app --reload --port 8000

# Ollama
ollama pull llama3.2
ollama serve

# Evidently
# (reporte se genera desde Python: report.save_html())

# Tests
pytest tests/ -v
```
