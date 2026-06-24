# MLOps

## Definición

MLOps es el conjunto de prácticas y herramientas que permiten gestionar el ciclo de vida completo de un sistema de machine learning: experimentación, versionado, registro, despliegue y monitorización.

## Ciclo de vida del ML

```text
Datos -> Entrenamiento -> Experimentos -> Registro -> Despliegue -> Monitorización
```

## Funciones clave

| Función | Descripción |
|---------|-------------|
| Seguimiento de experimentos | Guarda métricas, hiperparámetros, código y artefactos |
| Registro de modelos | Mantiene versiones y estados de los modelos |
| Despliegue | Publica modelos para inferencia o consumo por API |
| Monitorización | Detecta drift, fallos o degradación del modelo |

## Objetivo

Pasar de un experimento aislado en notebook a un proceso reproducible y mantenible.

---

## Seguimiento de experimentos

### MLflow

- Software libre y muy extendido.
- Buen punto de entrada para docencia y proyectos pequeños.
- Incluye tracking y registry.

### Weights & Biases

- SaaS con interfaz muy cuidada.
- Muy usado en investigación y equipos de deep learning.

### Neptune

- Fuerte orientación a metadatos y organización experimental.

### ClearML

- Opción flexible con enfoque más amplio que el mero tracking.

### Kubeflow

- Software libre orientado a pipelines y despliegue sobre Kubernetes.
- Útil para enseñar una aproximación abierta a MLOps, aunque es más complejo.

### DVC

- Software libre centrado en versionado de datos, experimentos y pipelines.
- Muy apropiado para proyectos docentes y flujos reproducibles sin una gran plataforma.

### Comparativa rápida

| Herramienta | Tipo | Ventaja principal | Limitación |
|-------------|------|-------------------|------------|
| MLflow | Software libre | Muy extendido y portable | Interfaz más básica |
| W&B | SaaS | Muy buena visualización | Dependencia de servicio |
| Neptune | SaaS | Organización de experimentos | Menos común en docencia |
| ClearML | Mixto | Más completo | Mayor complejidad inicial |
| Kubeflow | Software libre | Pipelines y despliegue abierto | Curva de aprendizaje alta |
| DVC | Software libre | Muy útil para reproducibilidad | Menos completo como plataforma total |

---

## Registro de modelos

El registro centraliza versiones y estados de un modelo.

| Servicio | Comentario |
|----------|------------|
| MLflow Model Registry | Sencillo y habitual |
| SageMaker Model Registry | Integrado en AWS |
| Vertex AI Model Registry | Integrado en GCP |
| Azure ML Registry | Integrado en Azure |
| Hugging Face Hub | Muy útil para modelos y artefactos de NLP |

### Uso típico

1. Entrenar un modelo.
2. Guardar métricas y artefactos.
3. Registrar una versión.
4. Promoverla a pruebas o producción.
5. Desplegar desde una versión controlada.

---

## Despliegue e inferencia

### Opciones gestionadas

| Plataforma | Servicio |
|------------|----------|
| AWS | SageMaker Endpoints |
| GCP | Vertex AI Endpoints |
| Azure | Azure ML Endpoints |
| Databricks | Model Serving |

### Opciones autogestionadas

- Ray Serve
- TorchServe
- Triton Inference Server
- FastAPI con contenedores
- BentoML

Las opciones gestionadas simplifican la operación. Las autogestionadas dan más control, pero requieren más trabajo.

---

## Monitorización y drift

### Qué se vigila

- Cambios en la distribución de entrada.
- Cambios en la relación entre variables y objetivo.
- Empeoramiento de métricas del modelo.

### Herramientas habituales

| Herramienta | Uso |
|-------------|-----|
| Evidently AI | Dashboards y análisis de drift |
| Fiddler | Monitorización comercial |
| SageMaker Model Monitor | Integrado en AWS |
| Vertex AI Model Monitoring | Integrado en GCP |
| WhyLabs | Observabilidad con opción gratuita inicial |

---

## Plataformas MLOps integradas

| Plataforma | Cobertura |
|------------|-----------|
| SageMaker | Entrenamiento, registro, despliegue y monitorización |
| Vertex AI | Entrenamiento, registro, despliegue y monitorización |
| Azure ML | Entrenamiento, registro, despliegue y monitorización |
| Databricks | Tracking, serving e integración con datos |
| MLflow | Tracking, registry y serving básico |
| Kubeflow | Pipelines y despliegue abierto sobre Kubernetes |
| DVC + MLflow | Combinación ligera y reproducible para docencia |

---

## Aplicación al proyecto

Un proyecto académico no siempre necesita una plataforma MLOps completa. Aun así, esta categoría sí es relevante si el grupo necesita:

- Reproducir entrenamientos.
- Comparar varios experimentos.
- Guardar versiones de modelos.
- Desplegar un endpoint.
- Explicar cómo pasaría el sistema a producción.

Si el proyecto es pequeño, una combinación simple como MLflow + almacenamiento de artefactos puede ser suficiente.

---

## Recomendaciones generales

| Caso | Recomendación |
|------|---------------|
| Proyecto académico sencillo | MLflow |
| Proyecto académico con repositorio Git | DVC + MLflow |
| Equipo muy orientado a visualización | W&B |
| Ecosistema AWS | SageMaker |
| Ecosistema GCP | Vertex AI |
| Ecosistema Azure | Azure ML |

---

## Fuentes recomendadas

- Documentación oficial de MLflow.
- Documentación oficial de Weights & Biases.
- Documentación oficial de ClearML.
- Documentación oficial de Kubeflow.
- Documentación oficial de DVC.
- Documentación oficial de BentoML.
- Documentación oficial de SageMaker, Vertex AI y Azure ML.
- Documentación oficial de Evidently AI.
