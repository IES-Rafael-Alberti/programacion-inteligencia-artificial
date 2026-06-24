# UD7 — Convergencia de Herramientas IA: Mapa RA/CE

## Resultados de Aprendizaje Cubiertos

| RA | Descripción | Fases UD7 |
|----|-------------|-----------|
| **RA3** | Evalúa las mejoras en los negocios integrando convergencia tecnológica | F0–F8 |
| **RA4** | Evalúa modelos de automatización industrial y de negocio relacionándolos con los resultados esperados por las empresas | F0, F3, F4, F7 |

---

## RA3 — Convergencia Tecnológica

### RA3a: Ventajas de unificar procesos, servicios, herramientas, métodos y sectores

| CE | Descripción | Fase | Contenido |
|----|-------------|------|-----------|
| a) | Se han identificado las ventajas que ofrece unificar procesos, servicios, herramientas, métodos y sectores | **F0** Gap de producción | Del notebook aislado al pipeline integrado: por qué unificar herramientas |
| | | **F1** Desarrollo asistido | Cómo la IA como asistente de desarrollo unifica ideación, código y depuración |
| | | **F5** Serving y APIs | Unificación de modelos en endpoints versionados |

**Caso UD7**: El clasificador de incidencias técnicas integra datos, experimentación, serving y monitoreo en un único flujo.

### RA3b: Sistemas que facilitan la conexión tecnológica

| CE | Descripción | Fase | Contenido |
|----|-------------|------|-----------|
| b) | Se han identificado sistemas que facilitan la conexión tecnológica | **F2** Pipeline datos | DVC, sistemas de versionado de datos y features, conectores ETL |

**Caso UD7**: Pipeline ETL que conecta fuentes de datos heterogéneas (CSVs, APIs, bases de datos) con el entrenamiento.

### RA3c: Características de sistemas de conexión tecnológica

| CE | Descripción | Fase | Contenido |
|----|-------------|------|-----------|
| c) | Se han evaluado las características de dichos sistemas | **F2** Pipeline datos | Evaluación de sistemas ETL: fiabilidad, escalabilidad, mantenibilidad |

**Caso UD7**: Comparativa de approaches de pipeline (manual vs. automatizado con validación).

### RA3d: Convergencia y seguridad en los negocios

| CE | Descripción | Fase | Contenido |
|----|-------------|------|-----------|
| d) | Se ha evaluado como la convergencia tecnológica aporta seguridad en los negocios | **F5** Serving y APIs | Rate limiting, API keys, autenticación en modelos servidos |
| | | **F8** IA Responsable | Guardrails, detección de sesgos, explicabilidad SHAP |

**Caso UD7**: API de clasificación con control de acceso, auditoría y protección contra usos indebidos.

### RA3e: Mejora en la toma de decisiones estratégicas

| CE | Descripción | Fase | Contenido |
|----|-------------|------|-----------|
| e) | Se ha evaluado la mejora en la capacidad de toma de decisiones estratégicas en un negocio conectado | **F0** Gap de producción | Cómo la trazabilidad y los datos objetivos mejoran las decisiones |
| | | **F6** Agentes y RAG | Sistemas multi-agente que sintetizan información para decisión |

**Caso UD7**: Dashboard de incidencias con recomendaciones generadas por agentes.

---

## RA4 — Automatización Industrial y de Negocio

### RA4a: Estrategias corporativas y modelos de negocio

| CE | Descripción | Fase | Contenido |
|----|-------------|------|-----------|
| a) | Se han identificado las nuevas estrategias corporativas y modelos de negocio en las empresas | **F0** Gap de producción | De la automatización de tareas a la automatización de decisiones |
| | | **F4** Orquestación Prefect | Estrategias de automatización de pipelines ML |

**Caso UD7**: Pipeline completo que automatiza desde la ingesta hasta el reporte semanal.

### RA4c: Modelos de automatización para requerimientos industriales

| CE | Descripción | Fase | Contenido |
|----|-------------|------|-----------|
| c) | Se han evaluado modelos de automatización para los nuevos requerimientos industriales y de negocio | **F3** MLflow | Tracking, registro y versionado de modelos como automatización de la experimentación |
| | | **F7** Observabilidad | Monitorización automática de deriva y rendimiento |

**Caso UD7**: MLflow registra cada experimento; Evidently monitoriza cada predicción.

### RA4d: Evaluar conveniencia de cada modelo

| CE | Descripción | Fase | Contenido |
|----|-------------|------|-----------|
| d) | Se ha evaluado la conveniencia de cada modelo para conseguir los resultados esperados por las empresas | **F3** MLflow | Comparación de runs, selección del mejor modelo basada en métricas |

**Caso UD7**: Comparar 3 modelos (regresión logística, random forest, XGBoost) y seleccionar el óptimo.

---

## Mapa de Evaluación por RA/CE

| RA | CE | Peso en UD7 | Cómo se evalúa |
|----|----|-------------|----------------|
| RA3 | a) | 20% | Prácticas F1, F5 + proyecto integrador |
| RA3 | b) | 8% | Práctica F2 (pipeline datos) |
| RA3 | c) | 8% | Práctica F2 (evaluación sistemas ETL) |
| RA3 | d) | 12% | Prácticas F5, F8 + proyecto |
| RA3 | e) | 12% | Prácticas F0, F6 + proyecto |
| RA4 | a) | 8% | Práctica F4 (orquestación) |
| RA4 | c) | 16% | Prácticas F3, F7 + proyecto |
| RA4 | d) | 8% | Práctica F3 (selección de modelo) |

**Total RA3**: 60% | **Total RA4**: 40%

---

## Flujo RA a través de las Fases

```
F0: RA3a, RA3e, RA4a
 │
 ├──► F1: RA3a
 │
 ├──► F2: RA3b, RA3c
 │
 ├──► F3: RA4c, RA4d
 │
 ├──► F4: RA4a
 │
 ├──► F5: RA3d
 │
 ├──► F6: RA3e
 │
 ├──► F7: RA4c
 │
 └──► F8: RA3d
      │
      ▼
Proyecto integrador: RA3 + RA4 (todos los CE)
```

> **Nota para el docente**: Este mapa es la guía de alineamiento. Cada guía teórica y cada notebook debe explicitar al inicio qué RA/CE cubre, para que el alumno entienda el "para qué" de cada fase.
