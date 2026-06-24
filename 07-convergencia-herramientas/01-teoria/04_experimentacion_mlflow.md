# F3 — Experimentación y Registro con MLflow

**RA/CE**: RA4c (modelos de automatización), RA4d (evaluar conveniencia)
**Duración**: 3h teoría + 6h práctica
**Prerrequisitos**: UD5 (MLflow concepto, tracking básico), UD6 (MLflow práctica integradora)

---

## Problema: ¿Cuál de tus 20 experimentos fue el mejor?

Has entrenado múltiples modelos: una regresión logística, un random forest, un XGBoost. Cada uno con distintas configuraciones de hiperparámetros, diferentes splits de datos y métricas ligeramente distintas. Y eso es solo hoy —la semana pasada probaste otras combinaciones.

**El problema**: Cuando vuelves una semana después, no recuerdas:

- ¿Qué hiperparámetros usaste en el modelo que mejor accuracy dio?
- ¿Con qué versión de datos se entrenó cada modelo?
- ¿Dónde guardaste el mejor modelo? ¿Y el código que lo generó?
- ¿Qué configuración produjo ese gráfico de matriz de confusión?

Sin un sistema de **registro de experimentos**, cada entrenamiento es un agujero negro: consumes tiempo y recursos, pero el conocimiento se pierde.

---

## 1. MLflow como Sistema de Automatización (RA4c)

MLflow no es solo un "log con interfaz". Es una **herramienta de automatización de la experimentación** que responde a RA4c: evaluar modelos de automatización para requerimientos industriales.

### 1.1 Componentes de MLflow

| Componente | Función | Conexión RA4 |
|------------|---------|--------------|
| **Tracking** | Registrar parámetros, métricas, artefactos de cada run | RA4c — automatiza el registro de experimentos |
| **Model Registry** | Versionar modelos con estados (Staging, Production, Archived) | RA4d — evaluar qué modelo desplegar |
| **MLflow Projects** | Empaquetar código reproducible | RA4c — automatización de ejecución |
| **Model Serving** | Servir modelos como API | RA4d — evaluar conveniencia del despliegue |

### 1.2 Lo que aporta MLflow al flujo convergente

En UD5 y UD6 viste MLflow como herramienta individual —aprendiste a hacer tracking básico y a registrar artefactos. En UD7, MLflow es el **sistema nervioso que conecta experimentación con producción**:

```
F2: Pipeline datos → produce datasets versionados
                        │
                        ▼
F3: MLflow registra → cada entrenamiento con:
    │                    - Parámetros (modelo, hiperparámetros)
    │                    - Métricas (accuracy, F1, precision)
    │                    - Artefactos (modelo, confusion matrix)
    │                    - Versión de datos (hash de DVC)
    │
    ▼
F5: Model Registry → sirve el mejor modelo en producción
F7: Evidently → monitorea el modelo contra sus métricas baseline
```

---

## 2. Tracking de Experimentos

### 2.1 Anatomía de una Run

Cada ejecución de entrenamiento debe registrar:

```python
import mlflow

with mlflow.start_run(run_name="logistic_regression_v1"):
    # Parámetros (configuración)
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_param("C", 1.0)
    mlflow.log_param("max_iter", 1000)
    mlflow.log_param("vectorizer_max_features", 5000)

    # Métricas (resultados)
    mlflow.log_metric("accuracy", 0.87)
    mlflow.log_metric("f1_score", 0.85)
    mlflow.log_metric("precision", 0.88)
    mlflow.log_metric("recall", 0.83)

    # Artefactos (outputs)
    mlflow.log_artifact("models/confusion_matrix.png")
    mlflow.log_artifact("models/classification_report.txt")
    mlflow.sklearn.log_model(model, "model")
```

**¿Por qué es importante registrar parámetros y métricas juntos?**
Sin parámetros, una métrica alta no se puede reproducir. Sin métricas, no sabes si el modelo es bueno. La **pareja parámetros↔métricas** es la unidad mínima de conocimiento experimental.

### 2.2 Comparación de Runs (RA4d)

El valor real del tracking aparece cuando comparas runs:

```
Experiment: ticket_classifier
┌────────────────────┬──────────┬──────────┬──────────┐
│ Run                │ Accuracy │ F1 Score │ Modelo   │
├────────────────────┼──────────┼──────────┼──────────┤
│ logistic_v1 (C=1)  │   0.87   │   0.85   │ LogReg   │
│ logistic_v2 (C=10) │   0.86   │   0.84   │ LogReg   │
│ rf_v1 (n=100)      │   0.91   │   0.90   │ RF       │
│ rf_v2 (n=200)      │   0.92   │   0.91   │ RF       │ ← mejor
│ xgb_v1 (lr=0.1)    │   0.90   │   0.89   │ XGBoost  │
└────────────────────┴──────────┴──────────┴──────────┘
```

**Conexión RA4d**: Evaluar la conveniencia de cada modelo implica comparar no solo métricas, sino también tiempo de entrenamiento, tamaño del modelo, interpretabilidad y coste de inferencia.

### 2.3 Registro de la Versión de Datos

Cada run debe saber con qué versión de datos se entrenó:

```python
import mlflow
import subprocess

# Obtener hash actual de DVC (si se usa)
dvc_hash = subprocess.run(
    ["dvc", "hash", "data/raw/tickets.csv"],
    capture_output=True, text=True
).stdout.strip()

with mlflow.start_run():
    mlflow.log_param("data_version", dvc_hash)
    mlflow.log_param("data_path", "data/raw/tickets.csv")
```

Esto crea un **vínculo trazable** entre el modelo y sus datos de entrenamiento.

---

## 3. Model Registry: Versionado de Modelos en Producción

El Model Registry permite gestionar el ciclo de vida de los modelos:

```python
# Registrar un modelo en el registry
mlflow.register_model(
    "runs:/<run_id>/model",
    "TicketClassifier"
)

# Desde CLI
# mlflow models serve -m "models:/TicketClassifier/Production" -p 5000
```

**Estados del Model Registry**:

| Estado | Significado | Uso |
|--------|-------------|-----|
| `None` | Recién registrado | Evaluación inicial |
| `Staging` | En pruebas | Validación en pre-producción |
| `Production` | En producción | Sirviendo predicciones reales |
| `Archived` | Retirado | Histórico, no activo |

**Esto es automatización (RA4c)**: el paso de Staging a Production puede disparar CI/CD, ejecutar tests de integración y actualizar el endpoint de serving automáticamente.

---

## 4. MLflow en el Flujo Convergente de UD7

```
┌────────────────────────────────────────────────────┐
│                FLUJO MLflow en UD7                   │
├────────────────────────────────────────────────────┤
│                                                      │
│  F2: Pipeline datos ─────► Datos versionados        │
│                                                      │
│  F3: MLflow Tracking  ──► Registro de experimentos  │
│       ├── Parámetros                                │
│       ├── Métricas                                  │
│       ├── Artefactos                                │
│       └── Model Registry ───► F5: FastAPI usa       │
│                              el modelo registrado    │
│                                                      │
│  F7: Evidently compara métricas baseline            │
│      (registradas en MLflow) vs. rendimiento actual │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### 4.1 Buenas prácticas para el tracking en UD7

1. **Un experimento por problema**: `ticket_classifier` agrupa todos los modelos
2. **Nombres de run descriptivos**: `logistic_v1_C1`, `rf_n100_depth10`
3. **Siempre juntos**: parámetros + métricas + artefactos + versión de datos
4. **Modelo guardado siempre**: aunque sea peor que otros, puede ser útil como baseline
5. **Etiquetar runs fallidos**: no borrar runs con errores — documentan lo que no funciona

---

## 5. Referencias a UD5 y UD6

**De UD5 (Cloud/MLOps)**:
- `05-cloud-mlops/01-teoria/03-mlops.md` — MLflow en el contexto MLOps
- Concepto de tracking de experimentos (qué es, por qué sirve)

**De UD6 (LLM/Agentes)**:
- `06-llm-agentes/01-teoria/MLflow_Documentacion.md` — Documentación práctica de MLflow
- `06-llm-agentes/03-practicas/100_mlflow_llamaindex_rag.ipynb` — MLflow con RAG

> Esta fase no re-enseña MLflow desde cero. Asume que conoces la sintaxis básica de `log_param`, `log_metric`, `log_artifact` y la interfaz de MLflow UI. Si no es así, revisa los materiales de UD6 antes de la práctica de F3.

---

## Resumen y Claves

1. **MLflow Tracking** automatiza el registro de experimentos: cada entrenamiento queda documentado con parámetros, métricas y artefactos.
2. **La comparación de runs** (RA4d) permite seleccionar objetivamente el mejor modelo basándose en datos, no en intuición.
3. **El Model Registry** versiona modelos y gestiona su ciclo de vida: de desarrollo a producción.
4. **Cada run debe vincularse a la versión de datos** (DVC hash) para garantizar trazabilidad completa.
5. **MLflow es el sistema nervioso** del stack convergente: conecta la experimentación (F3) con el serving (F5) y la monitorización (F7).

**En la práctica F3**: Entrenarás 3 modelos (regresión logística, random forest, XGBoost), registrarás cada uno con MLflow, compararás resultados y promoverás el mejor al Model Registry.
