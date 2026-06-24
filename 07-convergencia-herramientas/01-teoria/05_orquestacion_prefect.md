# F4 — Orquestación con Prefect

**RA/CE**: RA4a (estrategias corporativas basadas en datos)
**Duración**: 4h teoría + 6h práctica
**Prerrequisitos**: UD5 (orquestación conceptual), F2 (pipeline datos), F3 (MLflow experimentación)

---

## Problema: Tus pipelines siguen siendo manuales

Ya tienes un pipeline de datos que extrae, transforma y carga features listos para entrenar (F2). Y un sistema de experimentación que registra cada modelo con MLflow (F3). Pero todo funciona porque **tú estás sentado delante del ordenador ejecutando scripts en orden**.

El problema aparece cuando necesitas que esto ocurra:

- **Cada semana**: los datos nuevos llegan → el pipeline se ejecuta → el modelo se re-entrena → se registra en MLflow
- **Sin intervención manual**: nadie ejecuta `python clean.py` porque el sistema lo hace solo
- **Con recuperación automática**: si una tarea falla, se reintenta antes de notificar al equipo
- **Con trazabilidad**: cada ejecución queda registrada con sus métricas, duración y estado

Sin orquestación, tu pipeline es un castillo de naipes que depende de que alguien pulse el botón correcto en el momento correcto.

---

## 1. ¿Qué es la Orquestación de Pipelines?

### 1.1 Orquestación vs. Coreografía

| Concepto | Descripción | Analogía |
|----------|-------------|----------|
| **Orquestación** | Un coordinador central decide qué tarea se ejecuta, cuándo y qué hacer si falla | Director de orquesta |
| **Coreografía** | Cada componente sabe qué hacer y cuándo, sin coordinador central | Baile en grupo ensayado |

Para pipelines ML, la **orquestación** es el modelo adecuado: necesitas un director que garantice el orden, maneje fallos y proporcione visibilidad.

### 1.2 Prefect vs. Airflow

En UD5 viste el concepto de orquestación. En el ciclo de SBD/BDA se trabaja con **Apache Airflow**. Para este módulo usamos **Prefect**:

| Aspecto | Apache Airflow | Prefect |
|---------|---------------|---------|
| **Definición** | DAGs en Python, pero con mucha configuración | Flujos en Python puro, mínima configuración |
| **Setup inicial** | PostgreSQL, Redis, scheduler, workers | `pip install prefect` y listo |
| **Paradigma** | "Programar con restricciones" | "Python nativo con decoradores" |
| **Recuperación** | Compleja (requiereoperadores específicos) | Nativa: `retry`, `retry_delay_seconds` |
| **Observabilidad** | Airflow UI (logs, grafos) | Prefect UI + Orion + notificaciones |
| **Ideal para** | Equipos grandes, infraestructura dedicada | Equipos pequeños, prototipado, educación |

> **¿Por qué Prefect aquí?** Porque quieres orquestar pipelines ML sin montar un clúster. Prefect se instala con `pip`, sus flujos son funciones Python con decoradores, y la UI local (Prefect Orion) te da visibilidad inmediata. En SBD/BDA verás Airflow para entornos empresariales.

---

## 2. Conceptos Fundamentales de Prefect

### 2.1 Tasks y Flows

Prefect organiza el trabajo en dos niveles:

```python
from prefect import task, flow

@task
def load_data():
    """Carga los datos desde la fuente."""
    import pandas as pd
    df = pd.read_csv("data/raw/tickets.csv")
    print(f"Cargados {len(df)} registros")
    return df

@task
def clean_data(df):
    """Limpia y prepara los datos."""
    df = df.dropna(subset=["description", "category"])
    df["description"] = df["description"].str.lower()
    print(f"Limpios {len(df)} registros")
    return df

@task
def train_model(df):
    """Entrena el modelo y registra en MLflow."""
    import mlflow
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression

    with mlflow.start_run():
        vectorizer = TfidfVectorizer(max_features=5000)
        X = vectorizer.fit_transform(df["description"])
        y = df["category"]

        model = LogisticRegression(max_iter=1000)
        model.fit(X, y)

        mlflow.sklearn.log_model(model, "model")
        mlflow.log_param("max_features", 5000)
        mlflow.log_metric("samples", len(df))
        print("✅ Modelo entrenado y registrado")
        return mlflow.active_run().info.run_id

@flow
def pipeline_completo():
    """Orquesta las tareas del pipeline ML."""
    data = load_data()
    clean = clean_data(data)
    run_id = train_model(clean)
    print(f"Pipeline completado. Run ID: {run_id}")

# Ejecutar
if __name__ == "__main__":
    pipeline_completo()
```

**¿Qué ha pasado aquí?**
- Cada función decorada con `@task` es una unidad de trabajo independiente
- La función decorada con `@flow` orquesta el orden de ejecución
- Prefect resuelve automáticamente las dependencias: espera que `load_data` termine antes de `clean_data`
- Cada tarea se monitoriza: duración, estado, logs

### 2.2 Dependencias y Flujo de Datos

Las dependencias se definen implícitamente: si una tarea necesita el resultado de otra, Prefect espera automáticamente:

```python
@task
def extract():
    return ["dato1", "dato2", "dato3"]

@task
def transform(item):
    return item.upper()

@task
def load(items):
    print(f"Cargando: {items}")

@flow
def etl_pipeline():
    raw = extract()
    # Mapeo: cada elemento se procesa en paralelo
    transformed = transform.map(raw)
    load(transformed)
```

**`map`**: permite paralelizar tareas - cada elemento del resultado de `extract` se procesa por separado en `transform`.

### 2.3 Recuperación ante Fallos

Una de las ventajas clave de la orquestación es que los pipelines se recuperan automáticamente:

```python
@task(
    retries=3,
    retry_delay_seconds=30,
    retry_delay_threshold=timedelta(minutes=10)
)
def inestable_task():
    """Tarea que puede fallar intermitentemente."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("Fallo simulado")
    return "Éxito"
```

| Parámetro | Significado |
|-----------|-------------|
| `retries=3` | Reintenta hasta 3 veces |
| `retry_delay_seconds=30` | Espera 30s entre reintentos |
| `retry_delay_threshold` | Tiempo máximo total de reintentos |

**¿Qué pasa si todas las reintentos fallan?** La tarea se marca como `FAILED`, el flujo se detiene y se puede configurar una notificación (email, Slack, webhook).

---

## 3. Prefect en el Flujo Convergente

### 3.1 Conectando F2 (Pipeline Datos) y F3 (MLflow)

Prefect orquesta el flujo completo desde los datos hasta el registro de modelos:

```
F4: Prefect orquesta
 │
 ├── Tarea 1: Ejecutar pipeline ETL (F2)
 │   ├── dvc pull data/raw/
 │   ├── python scripts/clean.py
 │   └── python scripts/features.py
 │
 ├── Tarea 2: Validar datos de entrada
 │   └── pandera schema validation
 │
 ├── Tarea 3: Entrenar modelo (F3)
 │   ├── sklearn / XGBoost
 │   └── MLflow tracking → metrics + artifacts
 │
 ├── Tarea 4: Registrar en Model Registry
 │   └── mlflow.register_model()
 │
 └── Tarea 5: Notificar resultado
     └── Email / Slack: "Nuevo modelo listo para staging"
```

Cada tarea es independiente, testeable por separado, y el flujo completo se ejecuta con un solo comando: `python flows/pipeline_ml.py`.

### 3.2 Programación y Disparadores

Prefect permite ejecutar flujos de forma programada:

```python
from prefect import flow
from prefect.schedules import CronSchedule

# Ejecutar cada lunes a las 8:00
schedule = CronSchedule("0 8 * * 1")

@flow
def pipeline_semanal():
    # ... tareas del pipeline
    pass

# En producción: desplegar como servicio
# prefect deployment build pipeline_semanal:main -n "semanal"
# prefect deployment apply pipeline_semanal-deployment.yaml
```

**Conexión RA4a**: La automatización de decisiones —de pasar de "un humano decide cuándo entrenar" a "el orquestador decide basándose en reglas y calendario"— es el corazón de RA4a. Prefect permite definir estrategias corporativas de automatización: cuándo re-entrenar, cómo responder a fallos, cómo escalar.

### 3.3 Notificaciones y Alertas

```python
from prefect import flow
from prefect.blocks.notifications import SlackWebhook

@flow
def pipeline_monitoreado():
    try:
        result = entrenar_modelo()
    except Exception as e:
        slack = SlackWebhook.load("ml-alerts")
        slack.notify(f"❌ Pipeline falló: {e}")
        raise
```

---

## 4. CI/CD para Pipelines ML

Prefect también se conecta con CI/CD. Aunque no es el foco principal de F4, veamos cómo encaja:

```
Git push → GitHub Actions → Build → Test → Deploy
                                │
                                ▼
                         Prefect deployment update

Cada commit en main:
├── Ejecuta tests del pipeline (validación de datos, linting)
├── Si pasa → actualiza el deployment de Prefect
└── El orquestador usará la nueva versión en la próxima ejecución
```

### Ejemplo práctico: GitHub Actions para pipeline ML

Crea `.github/workflows/ml_pipeline.yml` en tu repositorio:

```yaml
name: ML Pipeline CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  validate-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Instalar dependencias
        run: |
          pip install -r requirements.txt
          pip install prefect pandas pandera scikit-learn

      - name: Validar datos
        run: python scripts/clean.py --input data/raw/incidencias.csv

      - name: Generar features
        run: python scripts/features.py --input data/clean/datos_limpios.csv

      - name: Entrenar y registrar modelo
        env:
          MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
        run: python scripts/train_and_register.py

      - name: Desplegar flujo Prefect
        env:
          PREFECT_API_URL: ${{ secrets.PREFECT_API_URL }}
        run: |
          prefect deploy flujo_entrenamiento.py:entrenamiento_flow \
            --name "pipeline-produccion" \
            --pool default
```

**Variables de entorno (secrets de GitHub)**:
- `MLFLOW_TRACKING_URI`: URL del servidor MLflow
- `PREFECT_API_URL`: URL del servidor Prefect

Este workflow ejecuta validación → features → entrenamiento → despliegue en cada push a main. Si algún paso falla, el deploy de Prefect no se actualiza, protegiendo producción.

En F7 (observabilidad) profundizarás en cómo el CI/CD se integra con la monitorización.

---

## 5. Prefect en Modo Local (Desarrollo)

Para las prácticas, usaremos Prefect en modo local:

```bash
# Instalación
pip install prefect

# Iniciar servidor local (Orion)
prefect server start

# En otro terminal, ejecutar el flujo
python flujo_entrenamiento.py
```

La UI local se abre en `http://localhost:4200` y muestra:
- Historial de ejecuciones con estado (Completed / Failed / Running)
- Duración de cada tarea
- Logs detallados por tarea
- Gráfico de dependencias del flujo

---

## 6. Referencias a UD5 y UD6

**De UD5 (Cloud/MLOps)**:
- `05-cloud-mlops/01-teoria/02-orquestacion.md` — Concepto de orquestación
- `05-cloud-mlops/01-teoria/03-mlops.md` — Pipeline MLOps y CI/CD

**De UD6 (LLM/Agentes)**:
- No hay referencias directas a orquestación en UD6 — Prefect es nuevo en UD7

> **Nota importante**: Airflow se estudia en el módulo de SBD/BDA con un enfoque empresarial. Aquí usamos Prefect porque es Python nativo, no requiere infraestructura externa y permite prototipar pipelines ML en minutos. Si vienes de SBD/BDA, notarás que el concepto de DAG es el mismo —lo que cambia es la ergonomía.

---

## Resumen y Claves

1. **La orquestación** convierte pipelines manuales en sistemas automatizados con recuperación, programación y trazabilidad.
2. **Prefect** usa decoradores `@flow` y `@task` para definir flujos en Python puro, sin configuración externa.
3. **Las dependencias** entre tareas se resuelven automáticamente: Prefect espera que una tarea termine antes de iniciar la siguiente.
4. **Los reintentos** (`retries`, `retry_delay_seconds`) hacen que los pipelines sean resilientes a fallos transitorios.
5. **Prefect conecta F2 y F3**: el orquestador ejecuta el pipeline de datos, desencadena el entrenamiento y registra el resultado en MLflow.
6. **RA4a**: la automatización de decisiones —cuándo re-entrenar, cómo responder a fallos— se materializa con Prefect.

**En la práctica F4**: Orquestarás el pipeline de datos (F2) y el entrenamiento con MLflow (F3) usando Prefect, con reintentos, programación semanal y notificaciones de fallo.
