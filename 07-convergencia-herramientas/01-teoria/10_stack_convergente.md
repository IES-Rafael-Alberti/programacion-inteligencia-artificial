# Proyecto final de UD7 — Stack Convergente de Herramientas IA

**RA/CE**: RA3 (convergencia tecnológica) + RA4 (automatización industrial y de negocio)
**Duración**: 12h prácticas
**Peso en evaluación**: 40% de la nota interna de UD7
**Prerrequisitos**: F1–F8 completadas

> **Relación con el proyecto final de módulo**: este proyecto cierra UD7 y exige integrar al menos 5 herramientas del stack convergente. El proyecto final de módulo, documentado en `../../12-proyecto-integrado/01-teoria/proyecto.md`, es más amplio, de tema libre y exige al menos 2 fuentes de datos. El trabajo de UD7 puede servir como ensayo, checkpoint o base reutilizable del proyecto de módulo si se adapta a sus requisitos.

---

## 1. Visión General

Has recorrido las 8 fases de la unidad, cada una construyendo una pieza del stack convergente:

```
F1: Desarrollo asistido  →  Código del proyecto
F2: Pipeline de datos    →  Datos listos y validados
F3: MLflow               →  Experimentos registrados
F4: Prefect              →  Pipeline orquestado
F5: FastAPI              →  Modelo servido como API
F6: LlamaIndex + CrewAI  →  Indexación jerárquica y agentes inteligentes
F7: Evidently            →  Monitorización continua
F8: Guardrails + SHAP    →  Seguridad y explicabilidad
```

Ahora llega el momento de **integrarlo todo** en un único proyecto completo. El proyecto final de UD7 no es una fase más: es el momento cumbre de la convergencia, donde demuestras que dominas el flujo completo de principio a fin.

### Objetivos

1. **Integrar ≥5 herramientas** del stack en un flujo de producción real
2. **Construir un pipeline completo** desde los datos hasta la monitorización
3. **Aplicar IA responsable** (guardrails, equidad, explicabilidad)
4. **Documentar decisiones técnicas** con justificación RA3/RA4
5. **Presentar y defender** el proyecto ante el profesor

---

## 2. Descripción del Proyecto

### 2.1 Caso Base (Recomendado)

**Sistema de Clasificación y Soporte Técnico Multi-Agente**

Construir un sistema que:
1. Recibe incidencias técnicas desde una API
2. Las clasifica por categoría, urgencia y equipo responsable
3. Consulta una base de conocimiento (RAG) para proponer soluciones
4. Asigna la incidencia al agente humano adecuado
5. Monitoriza la calidad de las predicciones en producción
6. Protege el sistema con guardrails y proporciona explicaciones

### 2.2 Caso Alternativo

Si el caso base no se ajusta a tu contexto, puedes proponer un caso alternativo que debe ser **aprobado por el profesor** y cubrir los mismos requisitos de integración. Si ya tienes definido el proyecto final de módulo, puedes adaptar el proyecto de UD7 a ese mismo dominio siempre que mantenga las ≥5 herramientas del stack. Ejemplos válidos:

- **Sistema de recomendación de cursos** con perfilado de estudiantes
- **Asistente de generación de informes** educativos automatizados
- **Clasificador y enrutador de consultas** administrativas
- **Analizador de sentimiento** en feedback de estudiantes con monitorización de deriva

---

## 3. Requisitos Técnicos

### 3.1 Stack Mínimo (5 herramientas obligatorias)

| Herramienta | Fase | Función en el proyecto |
|-------------|------|----------------------|
| **FastAPI** | F5 | API de clasificación + endpoints de predicción |
| **MLflow** | F3 | Tracking de experimentos + Model Registry |
| **Prefect** | F4 | Orquestación del pipeline completo |
| **Evidently** | F7 | Monitorización y detección de drift |
| **SHAP o LIME** | F8 | Explicabilidad de predicciones |

### 3.2 Herramientas Adicionales (elegir 1–3)

| Herramienta | Fase | Bonus por incluirla |
|-------------|------|-------------------|
| CrewAI | F6 | Sistema multi-agente que enriquece la clasificación |
| NeMo Guardrails | F8 | Protección contra prompts maliciosos |
| LangSmith | F7 | Trazabilidad extremo a extremo |
| LlamaIndex + CrewAI | F6 | Recuperación jerárquica y sistema multi-agente sobre knowledge base |
| API Key + Rate Limiting | F5 | Seguridad profesional de API |

### 3.3 Requisitos Funcionales

El proyecto DEBE incluir:

1. **Pipeline ETL**: carga, limpieza y validación de datos (inspirado en F2)
2. **Experimentación**: al menos 3 experimentos registrados en MLflow con diferentes modelos o hiperparámetros
3. **Orquestación**: un flujo Prefect que automatice el pipeline completo (entrenamiento → evaluación → registro)
4. **API REST**: endpoint de predicción con:
   - Validación Pydantic
   - Autenticación (API Key o similar)
   - Documentación OpenAPI
5. **Monitorización**: dashboard de drift que compare datos de entrenamiento vs. producción
6. **Explicabilidad**: visualización SHAP o LIME para una predicción individual
7. **Tests**: al menos 3 tests unitarios que validen componentes críticos

### 3.4 Requisitos No Funcionales

- Código en Python 3.10+
- Dependencias en `requirements.txt` o `pyproject.toml`
- README con instrucciones de instalación y uso
- Ejecutable localmente (sin dependencia de cloud)
- Tiempo de ejecución del pipeline completo < 30 minutos

---

## 4. Entregables

| Entregable | Formato | Peso |
|-----------|---------|------|
| **Repositorio de código** | GitHub / GitLab / ZIP | 50% |
| **Informe técnico** | PDF (4–6 páginas) | 30% |
| **Defensa oral** | Presentación 10 min + preguntas | 20% |

### 4.1 Repositorio de Código

Estructura recomendada:

```
proyecto-stack-convergente/
├── README.md                    ← Instrucciones, requisitos, arquitectura
├── requirements.txt             ← Dependencias
├── data/
│   ├── raw/                     ← Datos originales
│   └── processed/               ← Datos procesados
├── notebooks/
│   ├── 01_exploracion.ipynb     ← Análisis exploratorio
│   └── 02_experimentos.ipynb    ← Experimentación con MLflow
├── src/
│   ├── pipeline.py              ← Pipeline Prefect
│   ├── api.py                   ← API FastAPI
│   ├── monitor.py               ← Monitorización Evidently
│   ├── explain.py               ← Explicabilidad SHAP/LIME
│   └── guardrails.py            ← (Opcional) Guardrails
├── tests/
│   ├── test_pipeline.py
│   ├── test_api.py
│   └── test_monitor.py
├── mlruns/                      ← MLflow tracking (ignorado en git)
└── reports/
    ├── drift_report.html        ← Dashboard Evidently
    └── shap_explanation.png     ← Visualización SHAP
```

### 4.2 Informe Técnico

Estructura sugerida:

1. **Introducción** (½ pág): problema que resuelve y enfoque
2. **Arquitectura** (1 pág): diagrama del stack convergente con todas las herramientas
3. **Decisiones técnicas** (1 pág): por qué elegiste cada herramienta y cómo se conectan
4. **Experimentación** (½ pág): modelos probados, métricas, selección final
5. **Monitorización y calidad** (½ pág): resultados de Evidently, decisiones basadas en datos
6. **IA Responsable** (½ pág): guardrails, equidad, explicabilidad
7. **Conclusiones** (½ pág): qué aprendiste, qué harías diferente

### 4.3 Defensa Oral

- **10 minutos de presentación**: demo en vivo del sistema funcionando
- **5 minutos de preguntas**: el profesor preguntará sobre decisiones técnicas y conexión RA3/RA4

---

## 5. Criterios de Evaluación

| Criterio | Excelente (9-10) | Notable (7-8) | Suficiente (5-6) | Insuficiente (0-4) |
|----------|-----------------|---------------|------------------|-------------------|
| **Integración** | ≥6 herramientas, conexiones fluidas | 5 herramientas bien integradas | 5 herramientas, conexiones básicas | <5 herramientas |
| **Pipeline** | Prefect orquesta todo, reintentos, logs | Pipeline completo y funcional | Pipeline básico sin orquestación | Sin pipeline automatizado |
| **API** | Versionada, auth, rate limiting, docs | Completa con auth | Endpoint básico funcional | Sin API o no funcional |
| **Monitorización** | Dashboard interactivo + alertas | Reporte de drift generado | Drift calculado sin dashboard | Sin monitorización |
| **IA Responsable** | Guardrails + SHAP + Fairlearn | SHAP funcional | SHAP básico | Sin componente de IA responsable |
| **Código** | Modular, testeado, documentado | Limpio y funcional | Funcional pero desordenado | No ejecutable |
| **Informe** | Justifica decisiones, conexión RA | Completo y claro | Básico | Incompleto |
| **Defensa** | Demo en vivo, responde todo | Presentación clara | Presentación básica | No defensa |

---

## 6. Timeline (12h)

| Sesión | Horas | Actividad | Hito |
|--------|-------|-----------|------|
| **S1** | 3h | Planificación + configuración del entorno | Arquitectura definida, repo creado |
| **S2** | 3h | Pipeline ETL + experimentación MLflow | Pipeline funcional, 3 experimentos |
| **S3** | 3h | API FastAPI + orquestación Prefect | API sirviendo, Prefect orquestando |
| **S4** | 3h | Monitorización + IA Responsable + informe | Proyecto completo, informe entregado |
| **Defensa** | — | Presentación + preguntas | Nota final |

**Hitos de verificación**:
- Fin S1: diagrama de arquitectura aprobado por el profesor
- Fin S2: pipeline ejecutándose y experimentos en MLflow
- Fin S3: API funcional probada con curl
- Fin S4: entrega completa

---

## 7. Conexión con RA3 y RA4

| RA | CE | Cómo se demuestra en el proyecto |
|----|----|---------------------------------|
| **RA3** | a) Unificación | Integración de ≥5 herramientas en un flujo único |
| **RA3** | b) Conexión tecnológica | Conexiones entre herramientas: Prefect→MLflow, MLflow→FastAPI |
| **RA3** | c) Evaluación de sistemas | Comparativa de modelos en MLflow, selección justificada |
| **RA3** | d) Seguridad en negocio | Guardrails, API keys, explicabilidad de predicciones |
| **RA3** | e) Toma de decisiones | Dashboard de monitorización → decisiones basadas en datos |
| **RA4** | a) Estrategias corporativas | Automatización del pipeline completo con Prefect |
| **RA4** | c) Automatización industrial | Monitorización continua con Evidently, alertas automáticas |
| **RA4** | d) Evaluación de conveniencia | Selección del mejor modelo basada en métricas objetivas |

---

## 8. Consejos para el Éxito

### 8.1 Hazlo Iterativo

No intentes construir todo de golpe. Sigue este orden:

1. **Día 1**: que funcione un pipeline mínimo con una herramienta
2. **Día 2**: añade la segunda herramienta y haz que se comuniquen
3. **Día 3**: integra la tercera, cuarta, quinta...
4. **Día 4**: pule, añade tests, documenta

### 8.2 Prioriza la Integración

El objetivo NO es tener el mejor modelo del mundo —es demostrar que sabes **conectar herramientas**. Un modelo simple pero bien integrado puntúa más que un modelo complejo aislado.

### 8.3 Usa Datos Sintéticos si es Necesario

Si no tienes acceso a datos reales, genera datos sintéticos:

```python
import pandas as pd
import numpy as np

def generate_synthetic_tickets(n=1000):
    """Genera incidencias técnicas sintéticas."""
    categories = ["red", "servidor", "software", "hardware", "seguridad"]
    urgencies = ["baja", "media", "alta", "critica"]
    templates = [
        "El {recurso} no responde desde las {hora}",
        "Error al acceder a {recurso}: {error}",
        "Se requiere actualización de {recurso} en el departamento {dept}",
    ]
    # ... generar dataset
```

### 8.4 Checklist Final Antes de Entregar

- [ ] `pip install -r requirements.txt` funciona limpio
- [ ] `python src/pipeline.py` ejecuta sin errores
- [ ] `uvicorn src.api:app` levanta la API correctamente
- [ ] `curl -X POST localhost:8000/predict` devuelve una predicción
- [ ] MLflow UI muestra al menos 3 experimentos
- [ ] Evidently ha generado un reporte HTML
- [ ] SHAP ha generado una visualización interpretable
- [ ] README incluye arquitectura e instrucciones
- [ ] Informe técnico entregado en PDF

---

## Resumen y Claves

1. **El proyecto final de UD7** integra ≥5 herramientas del stack en un flujo de producción real.
2. **No se trata del mejor modelo** —se trata de la mejor integración entre herramientas.
3. **Trabaja iterativamente**: primero haz que funcione, luego añade complejidad.
4. **Documenta tus decisiones**: cada elección técnica debe estar justificada.
5. **Conexión RA3+RA4**: el proyecto demuestra tanto la convergencia tecnológica como la automatización de procesos.
6. **La defensa oral** es parte de la evaluación —prepara una demo en vivo que muestre el stack funcionando.

**¡Es el momento de demostrar todo lo que has aprendido!**
