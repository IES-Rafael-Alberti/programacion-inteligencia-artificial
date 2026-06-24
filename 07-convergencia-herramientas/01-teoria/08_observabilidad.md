# F7 — Observabilidad en Sistemas de IA

**RA/CE**: RA4c (evaluación de modelos de automatización industrial)
**Duración**: 3h teoría + 4h práctica
**Prerrequisitos**: F3 (MLflow Model Registry), F5 (serving APIs), F6 (agentes RAG)

---

## Problema: Tu modelo funciona... ¿o no?

Terminaste la F5: tu API sirve predicciones con autenticación, rate limiting y versionado. En F6 añadiste agentes inteligentes que responden consultas con RAG. Todo parece funcionar. Pero:

- **¿Cómo sabes si la calidad de las predicciones se mantiene en el tiempo?**
- **¿Los datos que llegan hoy se parecen a los datos con los que entrenaste?**
- **¿Un cambio silencioso en los datos de entrada está degradando el modelo sin que nadie lo note?**
- **¿Puedes reconstruir qué modelo predijo qué y cuándo para una incidencia de hace una semana?**

Sin observabilidad, tu sistema es una caja negra. Los modelos en producción **se degradan** —y sin métricas, te enterarás cuando los usuarios se quejen, no antes.

---

## 1. ¿Qué es Observabilidad en IA?

### 1.1 Más Allá del Monitoring Clásico

La observabilidad va más allá del monitoring tradicional porque no solo dice *qué* está mal, sino que permite entender *por qué*:

| Aspecto | Monitoring tradicional | Observabilidad (IA) |
|---------|----------------------|---------------------|
| **Pregunta** | ¿Está funcionando? | ¿Por qué se comporta así? |
| **Datos** | Métricas predefinidas (CPU, RAM, latencia) | Datos de entrada, predicciones, distribuciones |
| **Detección** | Umbrales fijos sobre infraestructura | Drift estadístico, cambios de distribución |
| **Investigación** | Dashboards pre-configurados | Exploración ad-hoc con datos de producción |
| **Alcance** | Servidor / aplicación | Modelo + datos + infraestructura + negocio |

### 1.2 Los Tres Pilares de la Observabilidad (RA4c)

```
┌─────────────────────────────────────────────────────────────┐
│                   OBSERVABILIDAD EN IA                       │
├─────────────────┬───────────────────┬───────────────────────┤
│  LOGS           │  MÉTRICAS         │  TRAZAS               │
│                 │                   │                       │
│ Registro        │ KPIs de modelo    │ Seguimiento de        │
│ estructurado de │ y datos:          │ peticiones a través   │
│ cada predicción │ accuracy, drift,  │ del pipeline:          │
│ con timestamp,  │ latencia,         │ F2→F3→F4→F5→F6       │
│ modelo, versión │ distribución      │                       │
│                 │                   │                       │
│ R4c:            │ R4c:              │ R4c:                  │
│ automatización  │ evaluación de     │ trazabilidad          │
│ del registro    │ modelos de        │ extremo a extremo     │
│                 │ automatización    │                       │
└─────────────────┴───────────────────┴───────────────────────┘
```

> **Conexión RA4c**: La observabilidad automatizada permite evaluar si los modelos de automatización implantados (pipelines Prefect, serving FastAPI, agentes CrewAI) están cumpliendo los resultados esperados —y detectar cuándo dejan de hacerlo.

---

## 2. Data Drift y Concept Drift

### 2.1 ¿Qué es el Drift?

El **drift** es el cambio silencioso que degrada los modelos en producción:

| Tipo | Qué cambia | Ejemplo |
|------|-----------|---------|
| **Data Drift** | La distribución de los datos de entrada | Los usuarios empiezan a escribir incidencias en un formato nuevo; el vectorizador no lo reconoce |
| **Concept Drift** | La relación entre entrada y salida | "Urgente" solía significar "servidor caído"; ahora significa "actualización de software necesaria" |
| **Prediction Drift** | La distribución de las predicciones | El modelo solía predecir 30% de incidencias como "críticas"; ahora predice 60% |

### 2.2 Detección Estadística con Evidently

Evidently es la herramienta principal para detectar drift. Compara dos conjuntos de datos (referencia vs. actual) usando tests estadísticos:

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Datos de referencia (training)
reference = pd.read_csv("data/training_data.csv")

# Datos actuales (producción)
current = pd.read_csv("data/production_batch.csv")

# Configurar reporte de drift
drift_report = Report(metrics=[
    DataDriftPreset(
        stattest="ks",          # Kolmogorov-Smirnov para numéricas
        cat_stattest="psi",     # Population Stability Index para categóricas
        drift_share=0.3         # Alarma si >30% de features tienen drift
    )
])

drift_report.run(reference_data=reference, current_data=current)
drift_report.save_html("reports/drift_report.html")
```

**Tests estadísticos comunes para drift**:

| Test | Tipo de feature | Cuándo usarlo |
|------|----------------|---------------|
| **KS (Kolmogorov-Smirnov)** | Numérica continua | Distribución general, sensible a cambios de forma |
| **Chi-cuadrado** | Categórica | Tablas de contingencia, cambios en frecuencias |
| **PSI (Population Stability Index)** | Categórica / binned | Estándar en banca, muy sensible |
| **JS (Jensen-Shannon)** | Distribuciones de probabilidad | Similar a KL pero simétrica y acotada |
| **Wasserstein** | Numérica | Detecta desplazamientos de distribución |

### 2.3 Umbrales y Alertas

Configurar alertas para detectar drift antes de que afecte al negocio:

```python
from evidently.test_suite import TestSuite
from evidently.tests import TestShareOfDriftedColumns

drift_tests = TestSuite(tests=[
    TestShareOfDriftedColumns(
        gte=0.3  # Alarma si >= 30% de features tienen drift
    )
])

drift_tests.run(reference_data=reference, current_data=current)
result = drift_tests.as_dict()

if result["tests"][0]["status"] == "FAILED":
    print("⚠️ ALERTA: Drift detectado en más del 30% de las features")
    # Disparar re-entrenamiento vía Prefect
    # requests.post("http://prefect:4200/api/retrain")
```

---

## 3. Conexión con el Stack Convergente

La observabilidad no es una fase aislada —es el **sistema nervioso** que conecta todas las fases anteriores:

```
F2: Pipeline datos         F3: MLflow tracking
 │                            │
 │  ¿Los datos de hoy se      │  ¿La accuracy del modelo
 │  parecen a los de          │  en prod coincide con
 │  entrenamiento?            │  la del registro?
 │                            │
 └──────────┬─────────────────┘
            ▼
      ┌──────────┐
      │  F7:     │ ← Evidently compara distribuciones
      │  Evidently│ ← LangSmith traza peticiones
      │  +       │ ← Dashboards de rendimiento continuo
      │  LangSmith│
      └──────────┘
            │
      ┌─────┴──────┬──────────┐
      ▼            ▼          ▼
   F4: Prefect   F5: API    F6: Agentes
   (re-entrena)  (versiona) (re-consulta KB)

  ¿Drift→re-entrenar?
  ¿API lenta→escalar?
  ¿Agentes alucinan→ajustar?
```

### 3.1 ¿Qué Monitorizar de Cada Fase?

| Fase | Qué monitorizar | Herramienta | Acción si alerta |
|------|----------------|-------------|-----------------|
| **F2 (datos)** | Data drift, valores nulos, distribuciones | Evidently | Reprocesar pipeline |
| **F3 (MLflow)** | Calidad del modelo, métricas en prod vs. training | MLflow + Evidently | Rollback a versión anterior |
| **F4 (Prefect)** | Duración de tareas, fallos, reintentos | Prefect UI | Notificar al equipo |
| **F5 (FastAPI)** | Latencia, throughput, errores 4xx/5xx | Logging + métricas | Escalar o rate limit |
| **F6 (agentes)** | Faithfulness, relevance, consultas fallidas | LangSmith | Re-indexar KB |
| **Stack completo** | Correlación entre métricas | Dashboard integrado | Decisión de negocio (RA4c) |

### 3.2 Trazabilidad con LangSmith

LangSmith proporciona trazabilidad extremo a extremo para sistemas LLM:

```python
from langsmith import Client
from langsmith.run_helpers import traceable

client = Client()

@traceable(project_name="ticket-classifier")
def classify_ticket(text: str) -> dict:
    """Registra cada paso como traza trazable."""
    # Paso 1: Vectorizar
    X = vectorizer.transform([text])

    # Paso 2: Predecir
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0].max()

    # Paso 3: Registrar
    return {
        "input_text": text,
        "prediction": pred,
        "confidence": float(proba),
        "model_version": "v2.1.0",
        "timestamp": datetime.now().isoformat()
    }

# Cada llamada genera una traza en LangSmith
result = classify_ticket("El servidor no responde")
```

**Beneficios de la trazabilidad**:
- **Auditoría**: reconstruir qué modelo, qué versión y qué datos produjeron cada predicción
- **Depuración**: cuando un agente falla, puedes ver exactamente qué pasos siguió
- **Mejora continua**: identificar patrones de consultas fallidas para mejorar el sistema

---

## 4. Arquitectura de Monitorización

### 4.1 Pipeline de Observabilidad

```
                    ┌──────────────────┐
                    │  Producción       │
                    │  (usuarios reales)│
                    └────────┬─────────┘
                             │
                    Peticiones / predicciones
                             │
                             ▼
                    ┌──────────────────┐
                    │  Logger          │ ← JSON estructurado con
                    │  (archivo/DB)    │    todos los metadatos
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    │                  │
                    ▼                  ▼
            ┌──────────────┐  ┌──────────────┐
            │ Evidently    │  │ LangSmith    │
            │ (drift test) │  │ (traza LLM)  │
            └──────┬───────┘  └──────┬───────┘
                   │                 │
                   ▼                 ▼
            ┌──────────────┐  ┌──────────────┐
            │ Dashboard    │  │ Alertas      │
            │ (HTML/PDF)   │  │ (email/Slack)│
            └──────────────┘  └──────┬───────┘
                                     │
                          ¿Drift detectado?
                          │            │
                         Sí           No
                          │            │
                          ▼            ▼
                   ┌──────────┐   Continuar
                   │ Prefect  │   monitoreo
                   │ re-entrena│   normal
                   │ modelo   │
                   └──────────┘
```

### 4.2 Dashboard de Observabilidad

Un dashboard completo debe responder estas preguntas de un vistazo:

| Sección | Contenido | Frecuencia |
|---------|-----------|------------|
| **Salud del modelo** | Accuracy, precision, recall en producción vs. baseline | Tiempo real |
| **Drift** | % de features con drift, gráficos de distribución por feature | Por batch |
| **Rendimiento** | Latencia P50/P95/P99, throughput, tasa de error | Tiempo real |
| **Agentes** | Faithfulness, relevance, consultas sin respuesta | Por consulta |
| **Infraestructura** | CPU, RAM, número de réplicas, conexiones activas | Tiempo real |
| **Cumplimiento** | Volumen de predicciones auditadas, tiempo de retención | Diario |

### 4.3 Estrategia de Alertas

| Nivel | Condición | Acción | Canal |
|-------|-----------|--------|-------|
| **Info** | Drift en 1-2 features no críticas | Notificar al equipo | Log / Dashboard |
| **Warning** | Drift >30% features o accuracy cae >5% | Re-entrenamiento automático | Email + Slack |
| **Critical** | API caída o drift >50% features | Rollback a versión anterior + alerta on-call | Slack + SMS |

---

## 5. Conexión con la Práctica F7

En la práctica P7 implementarás:

```
Parte 1: Simular datos de producción con drift artificial
    │
Parte 2: Configurar Evidently para detectar data drift y concept drift
    │
Parte 3: Generar dashboard HTML con reporte de drift
    │
Parte 4: Configurar alertas programáticas (consola/log)
    │
Parte 5 (Bonus): Integrar LangSmith para trazabilidad de agentes F6
```

**Stack**: Evidently + pandas + numpy + LangSmith (opcional)

---

## 6. Referencias a UD5 y UD6

**De UD5 (Cloud/MLOps)**:
- Concepto de monitorización de sistemas (monitoring vs. observabilidad)
- Dashboards y alertas (conceptos generales)

**De UD6 (LLM/Agentes)**:
- Trazabilidad de cadenas LangChain (concepto de `callbacks`)
- LangSmith como plataforma de depuración LLM

> Esta fase asume que comprendes el flujo completo del stack convergente (F1-F6). La observabilidad cierra el círculo: no es un añadido, es el sistema que te dice si todo lo anterior sigue funcionando correctamente.

---

## Resumen y Claves

1. **La observabilidad** no es opcional —es lo que diferencia un sistema experimental de uno profesional.
2. **Data drift** y **concept drift** son las causas principales de degradación silenciosa de modelos.
3. **Evidently** proporciona tests estadísticos (KS, PSI, Chi-cuadrado) para detectar drift de forma automatizada.
4. **LangSmith** ofrece trazabilidad extremo a extremo para sistemas con LLM y agentes.
5. **Las alertas** deben ser graduales: info → warning → critical, cada una con su acción asociada.
6. **Conexión RA4c**: la observabilidad automatizada permite evaluar continuamente si los modelos de automatización cumplen los resultados esperados —y activar correcciones cuando dejan de hacerlo.
7. **Conexión con el stack**: F7 no es una fase aislada. Es el sistema nervioso que conecta F2 (datos), F3 (MLflow), F4 (Prefect), F5 (FastAPI) y F6 (agentes) en un bucle de mejora continua.

**En la práctica F7**: Implementarás un sistema de monitorización con Evidently que detecta drift en datos simulados, genera un dashboard HTML y configura alertas programáticas.
