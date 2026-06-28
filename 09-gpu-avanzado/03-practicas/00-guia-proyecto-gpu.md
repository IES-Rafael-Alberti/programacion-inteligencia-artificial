# Semana 29 – Proyecto integrador

## 🎯 Objetivos
- Desarrollar un **proyecto grupal** que combine EDA → modelado → despliegue → interfaz/automatización.
- Fomentar **reproducibilidad** (entornos con conda/poetry/uv, versionado de datos/código).
- Preparar **documentación** y **presentación** finales.

---

## 📚 Entregables mínimos
1. **Código** del proyecto (notebooks + módulos auxiliares si los hay).
2. **Artefactos**: `artifacts/model.joblib`, métricas (`metrics.json`), datos procesados (`clean.csv`).
3. **Dashboard** ejecutable (Gradio o alternativa) con instrucciones para levantarlo.
4. **Pipeline** reproducible (Prefect/Airflow o versión Python pura).
5. **README** con pasos de ejecución y requisitos.

---

## 📂 Notebooks de apoyo
- `102_project_template.ipynb` → estructura base del proyecto (tabular sintético).
- `103_dashboard_template.ipynb` → interfaz/demostrador con Gradio.
- `104_pipeline_template.ipynb` → pipeline ETL (Prefect / Python puro).

> Están disponibles en versiones **base**, **soluciones** y **soluciones + autotests**.

---

## 🛠️ Rúbrica de evaluación (RA2, RA3, RA4)
- **Funcionalidad y calidad técnica (40%)**: prototipo ejecutable, métricas y artefactos consistentes.
- **Integración de herramientas (25%)**: uso coherente de librerías y pipeline reproducible.
- **Documentación y claridad (20%)**: README, guía de ejecución, decisiones justificadas.
- **Trabajo en equipo (15%)**: reparto equilibrado, control de versiones, coordinación.

---

## ✅ Consejos prácticos
- Bloquea dependencias (`environment.yml` o `pyproject.toml`/`poetry.lock`).
- Guarda *checkpoints* y evita *hard-coding* de rutas.
- Añade tests mínimos (véase notebooks **SOLUCIONES_TESTS**).
- Prepara una demo corta (3–5 minutos) con el dashboard.

