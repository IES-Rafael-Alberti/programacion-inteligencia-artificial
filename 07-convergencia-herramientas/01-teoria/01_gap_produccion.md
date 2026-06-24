# F0 — El Gap de Producción: Del Notebook Aislado al Stack Convergente

**RA/CE**: RA3a, RA3e, RA4a  
**Duración**: 3h teoría  
**Prerrequisitos**: UD5 (concepto MLOps, feature store), UD6 (herramientas IA básicas)

---

## Problema: ¿Por qué mi notebook no sirve para producción?

Has pasado semanas desarrollando un clasificador de textos en un notebook. Funciona bien con tus datos de prueba, las métricas son prometedoras y hasta has probado algunos prompts con LangChain. Pero cuando llega el momento de ponerlo en producción —que usuarios reales lo usen, que se actualice con nuevos datos, que otro equipo pueda replicar tus resultados— todo se vuelve complicado.

**Escenario real**: Tu notebook tiene celdas ejecutadas fuera de orden, las rutas de los datos son absolutas en tu máquina, las dependencias están mezcladas entre experimentos, y no hay registro de qué hiperparámetros produjeron tu mejor modelo. El equipo de operaciones te pide una API, monitorización y un pipeline que se actualice solo.

Este **gap entre el notebook y la producción** es el problema central que resuelve la convergencia de herramientas.

---

## 1. Lo que funciona en el notebook... y lo que no

| Capacidad | Notebook | Producción |
|-----------|----------|------------|
| Exploración | ✅ Excelente | ❌ Insuficiente |
| Reproducibilidad | ❌ (celdas fuera de orden) | ✅ (pipelines versionados) |
| Escalado | ❌ (memoria única) | ✅ (distribuido/paralelo) |
| Monitorización | ❌ (no existe) | ✅ (dashboards + alertas) |
| Trazabilidad | ❌ (manual) | ✅ (automática por herramienta) |
| Colaboración | ❌ (conflictos merge) | ✅ (entornos aislados) |
| Serving | ❌ (no aplica) | ✅ (API con balanceo) |
| Seguridad | ❌ (código expuesto) | ✅ (autenticación, rate limiting) |

Cada una de estas carencias es una **herramienta** o un **proceso** que debemos integrar.

---

## 2. El Stack Convergente: Mapa Completo

La convergencia tecnológica consiste en **unificar procesos, servicios y herramientas** para que los datos fluyan sin fricción desde la idea hasta la producción.

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUJO CONVERGENTE                          │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ DATOS    │ FEATURES │ EXP.     │ ORQUEST. │ SERVING          │
│          │          │          │          │                  │
│ Fuentes  │ DVC      │ MLflow   │ Prefect  │ FastAPI          │
│ raw      │ Features │ Tracking │ Flujos   │ Endpoints        │
│ Pipeline │ Store    │ Registry │ CI/CD    │ Rate limit       │
│ ETL      │          │          │          │ Versionado       │
├──────────┴──────────┴──────────┴──────────┴─────────────────┤
│                                                               │
│  AGENTES (CrewAI) ───► OBSERVABILIDAD (Evidently)            │
│  RAG jerárq. (LlamaIndex) ─► Guardrails + SHAP              │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

Cada bloque representa una **fase de UD7** y una **herramienta concreta** que resuelve un aspecto del gap de producción.

---

## 3. Valor Empresarial de la Convergencia

La convergencia no es un ejercicio técnico: es una **ventaja competitiva** medible.

### 3.1 Trazabilidad → Mejores Decisiones (RA3e)

Cuando cada experimento, cada versión de modelo y cada predicción quedan registrados:

- **Los equipos de producto** pueden justificar decisiones con datos objetivos
- **Los auditores** pueden reconstruir qué modelo predijo qué y cuándo
- **Los científicos de datos** dejan de preguntarse "¿cuál era la configuración que mejor funcionó?"

### 3.2 Automatización → Escalado (RA4a)

Un pipeline manual requiere intervención constante. Un pipeline automatizado:

- Ejecuta entrenamientos nocturnos sin supervisión
- Re-entrena modelos cuando la deriva supera un umbral
- Despliega nuevas versiones con CI/CD
- Libera tiempo del equipo para tareas de mayor valor

### 3.3 Unificación → Eficiencia (RA3a)

Un stack convergente elimina **silos de herramientas**:

- Un mismo caso de uso recorre todo el pipeline sin cambiar de plataforma
- Los datos de entrenamiento son los mismos que los de producción
- Las métricas de experimentación se conectan con las de monitorización

### 3.4 Seguridad → Confianza (RA3d)

La convergencia permite:

- Control de acceso centralizado (API keys + rate limiting)
- Auditoría de quién usó qué modelo y cuándo
- Guardrails que previenen respuestas dañinas
- Explicabilidad de cada predicción

---

## 4. El Caso Unificador de UD7

A lo largo de esta unidad construiremos **un mismo proyecto** que atraviesa todas las fases:

**Clasificador de incidencias técnicas → RAG sobre knowledge base → Sistema multi-agente de soporte**

| Fase | Qué construimos | Herramienta |
|------|----------------|-------------|
| F1 | Esqueleto del pipeline asistido por IA | Copilot/Cursor/Claude |
| F2 | Pipeline ETL que procesa incidencias | Python + DVC |
| F3 | Experimentación con 3 modelos | MLflow |
| F4 | Orquestación del pipeline completo | Prefect |
| F5 | API para clasificar incidencias | FastAPI |
| F6 | Agente que consulta knowledge base jerárquica | CrewAI + LlamaIndex |
| F7 | Dashboard de monitorización | Evidently |
| F8 | Guardrails y explicabilidad | Guardrails AI + SHAP |

---

## 5. Referencias a UD5 y UD6

Esta fase asume que conoces:

**De UD5 (Cloud/MLOps)**:
- Qué es MLOps y sus fases (CRISP-ML(Q))
- Concepto de feature store
- DVC para versionado de datos

**De UD6 (LLM/Agentes)**:
- RAG básico visto en UD6 como prerrequisito; en UD7 F6 se usa CrewAI + LlamaIndex jerárquico
- Ollama para modelos locales
- MLflow como concepto

> Si alguno de estos conceptos no te resulta familiar, revisa los materiales de UD5 (`05-cloud-mlops/01-teoria/`) y UD6 (`06-llm-agentes/01-teoria/`) antes de continuar.

---

## Resumen y Claves

1. **El gap notebook→producción** es el problema que resuelve la convergencia: reproducibilidad, escalado, monitorización, seguridad.
2. **Un stack convergente** conecta datos, features, experimentación, orquestación y serving en un flujo único.
3. **El valor empresarial** se mide en trazabilidad (mejores decisiones), automatización (escalado), unificación (eficiencia) y seguridad (confianza).
4. UD7 construye un **único proyecto** que recorre todo el stack, fase a fase.
5. Cada fase se apoya en conceptos de UD5 y UD6 — no los repite, los **integra**.

**En la siguiente fase (F1)**: Usaremos asistentes de IA para generar el código del pipeline de clasificación, dando el primer paso del flujo convergente.
