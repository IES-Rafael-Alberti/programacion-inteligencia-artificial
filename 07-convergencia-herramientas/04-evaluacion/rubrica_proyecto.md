# Rúbrica del Proyecto final de UD7 — Convergencia de Herramientas IA

## Estructura de la Rúbrica

Cada criterio se evalúa en 4 niveles. La nota final del proyecto se calcula como la media ponderada de todos los criterios, escalada a 10.

**Peso total del proyecto**: 40% de la nota de la unidad UD7.

> Esta rúbrica evalúa el proyecto integrador de UD7. La evaluación del proyecto final de módulo se documenta aparte en `12-proyecto-integrado/01-teoria/evaluacion.md` y puede usar pesos distintos.

---

## 1. Integración del Stack (Peso: 20%)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 4 | Integra ≥6 herramientas del stack con conexiones fluidas y justificadas. Cada herramienta cumple un rol claro y se comunica con las demás de forma documentada. |
| **Bien** | 3 | Integra 5 herramientas del stack correctamente. Las conexiones existen y son funcionales, aunque alguna podría estar mejor documentada. |
| **Mejorable** | 2 | Integra 5 herramientas pero las conexiones entre ellas son básicas o frágiles. Alguna herramienta está infrautilizada. |
| **Insuficiente** | 1 | Integra <5 herramientas o las herramientas están aisladas sin conexión entre ellas. |

**Indicadores específicos**:
- ¿MLflow se conecta con FastAPI para cargar el modelo?
- ¿Prefect orquesta el pipeline incluyendo experimentación y despliegue?
- ¿Evidently monitoriza datos que pasan por la API?
- ¿SHAP explica predicciones servidas por la API?

---

## 2. Pipeline y Orquestación (Peso: 15%)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 4 | Prefect orquesta el pipeline completo con tareas bien definidas, dependencias claras, reintentos configurados y logging estructurado. El pipeline es resiliente a fallos. |
| **Bien** | 3 | Prefect orquesta el pipeline completo con tareas y dependencias. Funciona correctamente aunque sin reintentos o logging avanzado. |
| **Mejorable** | 2 | Pipeline básico sin orquestación real (tareas secuenciales simples). Puede fallar sin recuperación. |
| **Insuficiente** | 1 | Sin pipeline automatizado. Las tareas se ejecutan manualmente o no hay flujo definido. |

**Indicadores específicos**:
- ¿El flujo Prefect incluye ≥3 tareas (carga, entrenamiento, evaluación)?
- ¿Las tareas tienen dependencias correctamente declaradas?
- ¿Hay reintentos configurados para tareas propensas a fallo?
- ¿El logging permite identificar dónde falla el pipeline?

---

## 3. API y Serving (Peso: 15%)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 4 | API completa: endpoints versionados, autenticación con API Key, rate limiting, documentación OpenAPI automática y tests con httpx. |
| **Bien** | 3 | API funcional con autenticación y documentación. Falta rate limiting o versionado. |
| **Mejorable** | 2 | API funcional pero sin autenticación ni rate limiting. Endpoint básico sin documentación. |
| **Insuficiente** | 1 | API no funcional o ausente. |

**Indicadores específicos**:
- ¿La API carga el modelo desde MLflow Model Registry?
- ¿Los esquemas Pydantic validan correctamente las entradas?
- ¿Devuelve códigos HTTP apropiados (200, 400, 401, 429, 500)?
- ¿Se puede probar desde Swagger UI?

---

## 4. Monitorización y Observabilidad (Peso: 15%)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 4 | Evidently genera dashboard HTML completo con tests estadísticos (KS, PSI) y alertas programáticas. El dashboard se interpreta correctamente y se extraen conclusiones accionables. |
| **Bien** | 3 | Evidently genera reporte de drift funcional. Se interpreta pero sin alertas automáticas. |
| **Mejorable** | 2 | Evidently instalado pero solo produce salidas básicas (sin dashboard interpretable). |
| **Insuficiente** | 1 | Sin monitorización o Evidently no produce resultados útiles. |

**Indicadores específicos**:
- ¿Se comparan datos de referencia (training) con datos actuales?
- ¿Se detecta drift en al menos una feature?
- ¿El dashboard es visualmente interpretable?
- ¿Hay algún mecanismo de alerta (consola, log, Slack)?

---

## 5. IA Responsable (Peso: 10%)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 4 | Guardrails funcionando (NeMo o Guardrails AI), auditoría de sesgo con Fairlearn, y explicabilidad SHAP con interpretación en lenguaje natural. |
| **Bien** | 3 | SHAP funcional con visualización interpretable. Falta guardrails o auditoría de sesgo. |
| **Mejorable** | 2 | SHAP básico o solo análisis superficial de sesgo sin guardrails. |
| **Insuficiente** | 1 | Sin componente de IA responsable. |

**Indicadores específicos**:
- ¿Los guardrails bloquean inputs/outputs no seguros?
- ¿Se ha calculado al menos una métrica de equidad?
- ¿La visualización SHAP es interpretable?
- ¿Se incluye una explicación en lenguaje natural de una predicción?

---

## 6. Calidad del Código (Peso: 10%)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 4 | Código modular, con funciones y clases bien definidas, comentarios significativos, type hints, y tests unitarios. README completo. |
| **Bien** | 3 | Código limpio y funcional, con comentarios básicos y estructura de proyecto clara. |
| **Mejorable** | 2 | Código funcional pero desordenado, sin modularidad ni comentarios. Difícil de seguir. |
| **Insuficiente** | 1 | Código no ejecutable, desorganizado, sin estructura de proyecto. |

**Indicadores específicos**:
- ¿Hay tests unitarios (≥3)?
- ¿El código sigue PEP 8?
- ¿Hay type hints en funciones públicas?
- ¿requirements.txt o pyproject.toml incluido?

---

## 7. Informe Técnico (Peso: 10%)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 4 | Informe completo (4-6 páginas) con diagrama de arquitectura, justificación de decisiones técnicas por RA/CE, resultados de experimentación, monitorización y conclusiones. |
| **Bien** | 3 | Informe claro y completo, aunque sin diagrama de arquitectura o con justificación RA superficial. |
| **Mejorable** | 2 | Informe básico que describe qué se hizo pero no justifica por qué. Sin conexión RA. |
| **Insuficiente** | 1 | Informe incompleto, sin estructura clara o no entregado. |

**Indicadores específicos**:
- ¿Incluye diagrama del stack convergente?
- ¿Justifica la elección de cada herramienta?
- ¿Conecta decisiones con RA3/RA4?
- ¿Incluye resultados de monitorización y explicabilidad?

---

## 8. Defensa Oral (Peso: 5%)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 4 | Demo en vivo funcionando, explica la arquitectura con claridad, responde todas las preguntas del profesor justificando decisiones técnicas. |
| **Bien** | 3 | Demo funcional, presentación clara, responde la mayoría de preguntas correctamente. |
| **Mejorable** | 2 | Demo con fallos menores, presentación básica, dificultad para responder preguntas. |
| **Insuficiente** | 1 | Sin demo, no responde preguntas o no se presenta a la defensa. |

**Indicadores específicos**:
- ¿La demo muestra el stack funcionando en vivo?
- ¿Explica la arquitectura y las decisiones de diseño?
- ¿Responde preguntas sobre conexiones entre herramientas?
- ¿Relaciona el proyecto con RA3 y RA4?

---

## Resumen de Pesos

| Criterio | Peso | RA/CE asociado |
|----------|------|---------------|
| 1. Integración del stack | 20% | RA3a, RA3b |
| 2. Pipeline y orquestación | 15% | RA4a, RA4c |
| 3. API y serving | 15% | RA3d |
| 4. Monitorización | 15% | RA4c |
| 5. IA Responsable | 10% | RA3d |
| 6. Calidad del código | 10% | — |
| 7. Informe técnico | 10% | RA3e, RA4a |
| 8. Defensa oral | 5% | RA3e |
| **Total** | **100%** | |

---

## Cálculo de la Nota

```
Puntuación total = Σ(Criterio_i × Peso_i)
Nota del proyecto = (Puntuación total / 4) × 10
```

**Ejemplo**:

| Criterio | Nivel | Puntos | Peso | Ponderado |
|----------|-------|--------|------|-----------|
| Integración | Excelente | 4 | 20% | 0.80 |
| Pipeline | Bien | 3 | 15% | 0.45 |
| API | Excelente | 4 | 15% | 0.60 |
| Monitorización | Bien | 3 | 15% | 0.45 |
| IA Responsable | Mejorable | 2 | 10% | 0.20 |
| Código | Bien | 3 | 10% | 0.30 |
| Informe | Excelente | 4 | 10% | 0.40 |
| Defensa | Bien | 3 | 5% | 0.15 |
| **Total** | | | **100%** | **3.35** |

`Nota = (3.35 / 4) × 10 = 8.38 → Notable`
