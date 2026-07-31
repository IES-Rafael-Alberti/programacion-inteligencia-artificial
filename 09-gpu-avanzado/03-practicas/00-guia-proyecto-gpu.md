# Proyecto Integrador GPU — Guía General

## 🎯 Objetivos
- Desarrollar un **proyecto grupal** que combine EDA → modelado → despliegue → interfaz/automatización.
- Fomentar **reproducibilidad** (entorno declarado, versiones fijadas y versionado de datos/código).
- Preparar **documentación** y **presentación** finales.

---

## 🖥️ Runtime requerido

La parte evaluable de aceleración requiere una **GPU NVIDIA**. Si tu equipo no dispone de una, utiliza **Google Colab con runtime GPU** como ruta canónica o el runtime cloud equivalente que indique el profesorado.

Antes de trabajar, completa el [preflight obligatorio con sus comandos](README.md#preflight-obligatorio-del-runtime). Incluye en la entrega la salida de `nvidia-smi`, el modelo de GPU, las versiones de las librerías y el backend/dispositivo utilizado.

Puedes adelantar o depurar en CPU las partes compatibles, pero una ejecución CPU **no demuestra** el uso de cuDF/cuML ni sustituye las mediciones del benchmark GPU.

---

## 📚 Entregables mínimos
1. **Código** del proyecto (notebooks + módulos auxiliares si los hay).
2. **Artefactos**: `artifacts/model.joblib`, métricas (`metrics.json`), datos procesados (`clean.csv`).
3. **Dashboard** ejecutable (Gradio o alternativa) con instrucciones para levantarlo.
4. **Pipeline** reproducible (Prefect/Airflow o versión Python pura).
5. **README** con pasos de ejecución y requisitos.
6. **Evidencia del runtime GPU** usado para la ejecución evaluable.

---

## 📂 Notebooks de apoyo
- `01_project_template.ipynb` → estructura base del proyecto (tabular sintético).
- `02_dashboard_template.ipynb` → interfaz/demostrador con Gradio.
- `03_pipeline_template.ipynb` → pipeline ETL (Prefect / Python puro).

> Están disponibles en versiones **base**, **soluciones** y **soluciones + autotests**.

---

## 🛠️ Rúbrica de evaluación (RA2, RA3, RA4)
- **Funcionalidad y calidad técnica (40%)**: prototipo ejecutable, métricas y artefactos consistentes.
- **Integración de herramientas (25%)**: uso coherente de librerías y pipeline reproducible.
- **Documentación y claridad (20%)**: README, guía de ejecución, decisiones justificadas.
- **Trabajo en equipo (15%)**: reparto equilibrado, control de versiones, coordinación.

---

## ✅ Consejos prácticos
- Fija las dependencias en el archivo de entorno indicado para el proyecto.
- Guarda *checkpoints* y evita *hard-coding* de rutas.
- Añade tests mínimos (véase notebooks **SOLUCIONES_TESTS**).
- Prepara una demo corta (3–5 minutos) con el dashboard.
