# Guía Docente — UD7 Convergencia de Herramientas IA

## 1. Información General

| Campo | Valor |
|-------|-------|
| **Módulo** | PIA — Programación de IA |
| **Unidad** | UD7 — Convergencia de Herramientas IA |
| **Curso** | 2026–2027 |
| **Duración** | ~75h (31h teoría + 44h prácticas) |
| **RA cubiertos** | RA3 + RA4 (todos los CE) |
| **Peso en módulo** | ~20% (estimado) |

### Perfil del Alumno

- **Prerrequisitos**: UD5 (Cloud/MLOps) y UD6 (LLM/Agentes) completadas
- **Conocimientos previos**: Python intermedio, conceptos de ML, experiencia básica con APIs
- **Entorno**: Portátil con 8GB+ RAM, Python 3.10+, Ollama para modelos locales

---

## 2. Estructura de la Unidad

### 2.1 Mapa de Sesiones

| Sesión | Fase | Horas | Tipo | Contenido |
|--------|------|-------|------|-----------|
| 1 | F0 | 3h | Teoría | Gap de producción, valor empresarial de la convergencia |
| 2–3 | F1 | 8h | T+P | Desarrollo asistido por IA |
| 4–5 | F2 | 9h | T+P | Pipeline de datos automatizado |
| 6–7 | F3 | 9h | T+P | Experimentación con MLflow |
| 8–9 | F4 | 10h | T+P | Orquestación con Prefect |
| 10–11 | F5 | 10h | T+P | Serving y APIs |
| 12–13 | F6 | 10h | T+P | Agentes y RAG en producción |
| 14 | F7 | 7h | T+P | Observabilidad |
| 15 | F8 | 7h | T+P | IA Responsable |
| 16–19 | Proyecto | 12h | Práctica | Stack convergente completo |
| 20 | Examen | 2h | Evaluación | Examen teórico + defensas |

### 2.2 Alternancia Recomendada

Cada fase sigue el patrón: **1h teoría → 2h práctica**

```
Sesión tipo (3h):
┌─────────────────────────────────────────────┐
│ 15 min: Recordatorio UD5/UD6 + checkpoint   │
│ 45 min: Teoría de la fase (problema → solución)│
│ 15 min: Pausa                               │
│ 2h: Trabajo práctico en notebook            │
└─────────────────────────────────────────────┘
```

### 2.3 Opciones de Reducción (si <75h)

| Opción | Horas | Cambios |
|--------|-------|---------|
| **A** (~65h) | -10h | Eliminar F0 (integrar en F1), fusionar F2+F3 |
| **B** (~55h) | -20h | Eliminar F0, F8; proyecto optativo → examen más pesado |
| **C** (~50h) | -25h | Solo F1–F5 + proyecto (sin agentes ni observabilidad) |

---

## 3. Planificación Detallada por Fase

### F0 — Gap de Producción (3h teoría)

**Objetivo**: Situar al alumno en el problema que resuelve la unidad.

| Actividad | Duración | Recursos |
|-----------|----------|----------|
| Presentación del problema: del notebook a producción | 45 min | `01_gap_produccion.md` |
| Mapa del stack convergente + RA3/RA4 | 45 min | `00_RA_CE_UD7.md` |
| Discusión: ¿qué herramientas conocen de UD5/UD6? | 45 min | Pizarra / Miro |
| Checkpoint de autoevaluación | 45 min | Cuestionario rápido |

**Clave docente**: El objetivo de F0 es crear la necesidad —que el alumno sienta el "gap" como un problema real que la unidad va a resolver.

### F1 — Desarrollo Asistido por IA (4h T + 4h P)

**Objetivo**: Usar IA como asistente de desarrollo para generar código del pipeline.

| Actividad | Duración |
|-----------|----------|
| Teoría: asistentes de IA (Copilot, Cursor, Claude) | 2h |
| Demo: generar código de pipeline con asistente | 2h |
| Práctica P1: generar y refinar código con IA | 4h |

**Evaluación**: Notebook P1 — 8% nota.

**Prerrequisitos UD5/UD6**: Ninguno.

### F2 — Pipeline de Datos Automatizado (3h T + 6h P)

**Objetivo**: Construir pipeline ETL con validación automática.

| Actividad | Duración |
|-----------|----------|
| Teoría: ETL para ML, validación de datos con pandera | 3h |
| Práctica P2: construir pipeline ETL | 6h |

**Evaluación**: Notebook P2 — 8% nota.

**Prerrequisitos UD5/UD6**: DVC, feature engineering (UD5).

### F3 — Experimentación con MLflow (3h T + 6h P)

**Objetivo**: Registrar experimentos, comparar modelos, gestionar Model Registry.

| Actividad | Duración |
|-----------|----------|
| Teoría: MLflow Tracking + Model Registry | 3h |
| Práctica P3: experimentos, comparación, staging | 6h |

**Evaluación**: Notebook P3 — 8% nota.

**Prerrequisitos UD5/UD6**: MLflow conceptos básicos (UD5), práctica MLflow (UD6).

### F4 — Orquestación con Prefect (4h T + 6h P)

**Objetivo**: Orquestar el pipeline completo con Prefect.

| Actividad | Duración |
|-----------|----------|
| Teoría: Prefect flows, tasks, reintentos, logging | 4h |
| Práctica P4: pipeline F2+F3 orquestado | 6h |

**Evaluación**: Notebook P4 — 8% nota.

**Prerrequisitos UD5/UD6**: Concepto de orquestación (UD5).

### F5 — Serving y APIs (4h T + 6h P)

**Objetivo**: Servir modelo con FastAPI profesional.

| Actividad | Duración |
|-----------|----------|
| Teoría: FastAPI, API keys, rate limiting, versionado | 4h |
| Práctica P5: API con auth + rate limiting + versionado | 6h |

**Evaluación**: Notebook P5 — 8% nota.

**Prerrequisitos UD6**: FastAPI básico (práctica UD6 `103_fastapi_serving_modelos.ipynb`).

### F6 — Agentes y RAG en Producción (4h T + 6h P)

**Objetivo**: Sistema multi-agente con CrewAI + LlamaIndex e indexación jerárquica.

| Actividad | Duración |
|-----------|----------|
| Teoría: CrewAI, LlamaIndex e indexación jerárquica en producción | 4h |
| Práctica P6: CrewAI + LlamaIndex hierarchical indexing sobre el caso ParkingCorp | 6h |

**Evaluación**: Notebook P6 — 8% nota.

**Prerrequisitos UD5/UD6**: RAG básico de UD6 como recordatorio; UD7 usa LlamaIndex jerárquico como evolución avanzada.

### F7 — Observabilidad (3h T + 4h P)

**Objetivo**: Monitorizar modelos con Evidently.

| Actividad | Duración |
|-----------|----------|
| Teoría: Data drift, concept drift, Evidently, LangSmith | 3h |
| Práctica P7: detección de drift + dashboard | 4h |

**Evaluación**: Notebook P7 — 4% nota.

**Prerrequisitos UD5/UD6**: Concepto de observabilidad (UD5).

### F8 — IA Responsable (3h T + 4h P)

**Objetivo**: Guardrails, equidad, explicabilidad.

| Actividad | Duración |
|-----------|----------|
| Teoría: NeMo Guardrails, Fairlearn, SHAP, marco regulatorio | 3h |
| Práctica P8: guardrails en API + SHAP + Fairlearn | 4h |

**Evaluación**: Notebook P8 — 4% nota.

**Prerrequisitos UD5/UD6**: Ninguno nuevo.

### Proyecto final de UD7 (12h prácticas)

**Objetivo**: Integrar ≥5 herramientas del stack en un proyecto completo.

Ver `01-teoria/10_stack_convergente.md` para la guía completa del proyecto.

**Evaluación interna de UD7**: 40% nota — código (50%), informe (30%), defensa (20%).

**Relación con el proyecto final de módulo**: el proyecto de UD7 puede funcionar como ensayo o avance técnico del proyecto final progresivo (`../../12-proyecto-integrado/`), pero no sustituye automáticamente sus requisitos generales de tema libre, al menos 2 fuentes de datos y checkpoints.

---

## 4. Evaluación y Calificación

### 4.1 Distribución

| Componente | Peso | Instrumentos |
|-----------|------|-------------|
| Prácticas (8) | 40% | Notebooks P1–P8 |
| Proyecto final de UD7 | 40% | Rúbrica (ver `rubrica_proyecto.md`) |
| Examen teórico | 20% | Banco GIFT (ver `examen_teorico.gift`) |

### 4.2 Criterios de Corrección

Ver `criterios_evaluacion.md` para detalle completo.

### 4.3 Recomendaciones de Evaluación Continua

- **Checkpoint de bloque**: mini-evaluación del notebook del bloque (15 min)
- **Feedback inmediato**: las celdas de test en los notebooks permiten autoevaluación
- **Hitos de proyecto**: revisar diagrama de arquitectura (S1) y pipeline funcional (S2)
- **Recuperación**: repetir prácticas suspensas (nota máxima 7) o proyecto completo con entregas parciales

---

## 5. Conexión con UD5 y UD6

### 5.1 Mapa de Prerrequisitos

| Herramienta UD7 | Visto en UD5 | Visto en UD6 |
|----------------|-------------|-------------|
| FastAPI | — | Práctica `103_fastapi_serving_modelos.ipynb` |
| MLflow | Conceptos básicos | Práctica integradora |
| RAG básico | Conceptos | Práctica `101_rag_chromadb_ollama.ipynb` como prerrequisito |
| LlamaIndex jerárquico | — | Evolución avanzada en UD7 F6 |
| CrewAI / AutoGen | — | Concepto de agentes y patrones multi-agente |
| Prefect | Concepto orquestación | — |
| Evidently | Concepto observabilidad | — |
| SHAP / Fairlearn | — | — |

### 5.2 Estrategia Anti-Solapamiento

1. **No reintroducir conceptos básicos** —cada fase empieza con "recordatorio de 5 min + referencias a UD5/UD6"
2. **Checkpoint de autoevaluación** al inicio de cada fase: si el alumno falla, se le redirige al material de UD5/UD6
3. **Enlaces directos** a prácticas de UD5/UD6 en cada guía teórica
4. **Regla de oro**: si se cubrió en UD5/UD6 como concepto individual, UD7 lo trata como integrante de un flujo

---

## 6. Gestión del Aula

### 6.1 Errores Comunes de los Alumnos

| Error | Frecuencia | Cómo prevenirlo |
|-------|-----------|-----------------|
| Instalar dependencias incorrectas | Alta | Script `setup.sh` al inicio de la unidad |
| Confundir MLflow tracking con Model Registry | Media | Dejar claro en F3: tracking ≠ registry |
| Olvidar el decorador `@task` en Prefect | Alta | Plantilla con esqueleto Prefect pre-escrito |
| No cerrar la API antes de relanzarla | Media | Enseñar `Ctrl+C` y `lsof -i :8000` |
| No cargar datos de referencia en Evidently | Media | Template de notebook con datos de referencia precargados |
| SHAP no funciona por versión incorrecta | Baja | Pinned `shap==0.46.0` en requirements |
| Ollama no arranca o modelo no descargado | Media | Script de verificación de entorno al inicio |

### 6.2 Adaptaciones por Tamaño de Grupo

#### Grupos Pequeños (<15 alumnos)
- **Ventaja**: atención individualizada, cada alumno avanza a su ritmo
- **Enfoque**: mentoría intensiva en proyecto final, defensas individuales
- **Problema potencial**: menos diversidad en discusiones

#### Grupos Medianos (15–30 alumnos)
- **Ventaja**: equilibrio entre atención y diversidad
- **Enfoque**: parejas para prácticas, individual para proyecto
- **Problema potencial**: algunos alumnos se quedan atrás en fases iniciales

#### Grupos Grandes (>30 alumnos)
- **Ventaja**: múltiples perspectivas, discusiones ricas
- **Enfoque**: grupos de 3 para proyecto, defensas en grupo
- **Problema potencial**: difícil verificar progreso individual
- **Necesario**: 1–2 auxiliares para sesiones prácticas

### 6.3 Adaptaciones por Nivel

#### Alumnos con Base Débil en UD5/UD6
- Proporcionar **checkpoints de autoevaluación** al inicio de cada fase
- Ofrecer **sesiones de refuerzo** de 1h antes de F2, F5, F6
- **Material complementario**: enlaces directos a prácticas específicas de UD5/UD6

#### Alumnos Avanzados
- **Retos adicionales** en cada práctica (marcados como "Bonus")
- Opción de herramientas alternativas (AutoGen vs. CrewAI, LIME vs. SHAP)
- Posibilidad de caso de uso propio para el proyecto final

### 6.4 Dependencia de APIs Externas

**Problema**: OpenAI, Anthropic y otras APIs pueden no estar disponibles en el aula.

**Solución**: **Ollama** como fallback local para todo el stack:

```bash
# Modelos recomendados para el aula
ollama pull llama3.2        # ~3GB — modelo generativo para agentes
ollama pull nomic-embed-text # ~0.5GB — embeddings para RAG
```

**Setup mínimo para aula sin internet**:
1. Script `setup_offline.sh` que descarga todo antes de la sesión
2. Datasets estáticos precargados
3. Modelos Ollama precargados
4. `requirements.txt` con versiones pinned

---

## 7. Recomendaciones Pedagógicas

### 7.1 Metodología

- **Workflow-based con problem-first**: cada fase comienza con un problema real
- **Caso unificador**: clasificador de incidencias técnicas → RAG → multi-agente
- **Conexión explícita con RA3/RA4**: cada guía teórica explicita qué RA/CE cubre
- **Alternancia teoría-práctica**: evitar bloques teóricos >1h

### 7.2 Ritmo Recomendado

| Bloque | Fase | Horas | Carga |
|--------|------|-------|-------|
| 1 | F0 + F1 | 11h | Teoría intensiva + primera práctica |
| 2 | F2 | 9h | Pipeline de datos |
| 3 | F3 | 9h | Experimentación MLflow |
| 4 | F4 | 10h | Orquestación Prefect |
| 5 | F5 | 10h | Serving y APIs |
| 6 | F6 | 10h | Agentes multi-agente |
| 7 | F7 + F8 | 14h | Observabilidad + IA Responsable |
| 8–9 | Proyecto | 12h | Stack convergente |
| 10 | Examen | 2h | Evaluación final |

**Total**: ~87h (incluye 12h de proyecto sobre las 75h planificadas)

### 7.3 Señales de Alarma

| Señal | Posible causa | Acción |
|-------|--------------|--------|
| Alumnos perdidos en F3 (MLflow) | No recuerdan UD6 | Sesión de refuerzo de 1h |
| Notebooks no se ejecutan | Dependencias incorrectas | Verificar `requirements.txt` |
| Alumnos copian código sin entender | Prácticas demasiado largas | Dividir en partes más pequeñas |
| Baja participación en proyecto | Falta de motivación | Permitir casos de uso propios |
| Confusión entre Prefect y MLflow | Solapamiento percibido | Reforzar: Prefect orquesta, MLflow registra |

### 7.4 Técnicas de Motivación

1. **Demo en vivo**: empezar cada fase mostrando el resultado final funcional
2. **Concurso de mejor proyecto**: el mejor proyecto integrado se destaca como ejemplo
3. **Caso real**: usar datos de incidencias reales del centro (anonimizados)
4. **Portfolio**: cada práctica es un entregable que construye el portfolio del alumno
5. **Invitados**: profesionales de IA que compartan cómo usan estas herramientas

---

## 8. Material de Aula

### 8.1 Estructura de Archivos

```
07-convergencia-herramientas/
├── README.md
├── 01-teoria/                    ← 10 guías teóricas (F0–F8 + proyecto)
│   ├── 00_RA_CE_UD7.md
│   ├── 01_gap_produccion.md
│   ├── 02_desarrollo_asistido.md
│   ├── 03_pipeline_datos.md
│   ├── 04_experimentacion_mlflow.md
│   ├── 05_orquestacion_prefect.md
│   ├── 06_serving_apis.md
│   ├── 07_agentes_rag.md
│   ├── 08_observabilidad.md
│   ├── 09_ia_responsable.md
│   └── 10_stack_convergente.md
├── 02-ejemplos/
│   └── pipeline_completo/
├── 03-practicas/                 ← 8 notebooks de prácticas
│   ├── P1_desarrollo_asistido.ipynb
│   ├── P2_pipeline_datos.ipynb
│   ├── P3_experimentacion_mlflow.ipynb
│   ├── P4_orquestacion_prefect.ipynb
│   ├── P5_serving_api.ipynb
│   ├── P6_agentes_rag.ipynb
│   ├── P7_observabilidad.ipynb
│   └── P8_ia_responsable.ipynb
├── 04-evaluacion/
│   ├── criterios_evaluacion.md
│   ├── rubrica_proyecto.md
│   └── examen_teorico.gift
├── 05-recursos/
│   ├── cheatsheet_stack_convergente.md
│   └── enlaces_referencia.md
├── 90-archivo/
└── 99-profesor/
    └── guia_docente.md           ← Este archivo
```

### 8.2 Dependencias Principales

```
# requirements.txt (core)
prefect>=2.0,<3.0
mlflow>=2.0
fastapi>=0.100
uvicorn
pydantic>=2.0
slowapi
evidently>=0.4
shap>=0.46
fairlearn>=0.10
crewai>=0.30
llama-index>=0.11
llama-index-embeddings-huggingface>=0.3
nemoguardrails  # opcional — fallback: guardrails-ai
# chromadb/langchain opcionales: legado de Modelos de la IA para repasar RAG plano, no herramienta principal de F6
pandas>=2.0
scikit-learn>=1.3
pandera>=0.18
```

### 8.3 Script de Setup

```bash
#!/bin/bash
# setup_ud7.sh — Preparar entorno UD7

echo "=== Setup UD7: Convergencia de Herramientas IA ==="

# Crear entorno virtual
python3.10 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Verificar instalaciones clave
python -c "import prefect; print('✅ Prefect', prefect.__version__)"
python -c "import mlflow; print('✅ MLflow', mlflow.__version__)"
python -c "import evidently; print('✅ Evidently', evidently.__version__)"
python -c "import shap; print('✅ SHAP', shap.__version__)"

# Opcional: descargar modelos Ollama
which ollama > /dev/null && {
    ollama pull llama3.2
    ollama pull nomic-embed-text
} || echo "⚠️  Ollama no instalado. Los agentes necesitan Ollama."

echo "=== Setup completo ==="
```

---

## 9. Preguntas Frecuentes

### 9.1 De los Alumnos

**P: ¿Puedo usar OpenAI en lugar de Ollama?**
R: Sí, pero el proyecto debe ser ejecutable localmente sin depender de APIs externas. Si usas OpenAI, proporciona también un fallback con Ollama.

**P: ¿Necesito saber todas las herramientas de memoria?**
R: No. El examen evalúa integración y conexiones, no memorización de APIs. El cheatsheet (`05-recursos/cheatsheet_stack_convergente.md`) es tu referencia rápida.

**P: ¿Puedo hacer el proyecto sobre un caso diferente al propuesto?**
R: Sí, con aprobación del profesor. Debe cumplir los mismos requisitos de integración (≥5 herramientas) y cubrir RA3+RA4. Si coincide con el proyecto final de módulo, debe respetar además sus requisitos propios: tema validado, al menos 2 fuentes de datos e integración real.

### 9.2 Del Profesor

**P: ¿Qué hago si un alumno no tiene UD5/UD6?**
R: Proporciona los checkpoints de autoevaluación al inicio de cada fase. Si falla más de 2, deriva a sesiones de refuerzo con materiales de UD5/UD6.

**P: ¿Puedo saltarme fases si tengo poco tiempo?**
R: Sí. Las fases reducibles son F0, F1 y F8. Las fases obligatorias para el proyecto son F3, F4, F5 y F7 (mínimo para stack funcional).

**P: ¿Cómo evalúo 40+ proyectos individuales?**
R: Agrupa defensas en sesiones de 30 min por grupo de 3. Usa la rúbrica (`rubrica_proyecto.md`) como checklist. El código se evalúa con la plantilla de tests.

---

## 10. Referencias para el Docente

| Recurso | Para qué |
|---------|----------|
| `criterios_evaluacion.md` | Criterios detallados de evaluación |
| `rubrica_proyecto.md` | Rúbrica para evaluar proyectos |
| `examen_teorico.gift` | Banco de preguntas para Moodle |
| `cheatsheet_stack_convergente.md` | Referencia rápida de comandos |
| `enlaces_referencia.md` | Enlaces a documentación oficial |
| `00_RA_CE_UD7.md` | Mapeo RA/CE de la unidad |

---

## Nota Final

Esta guía está diseñada para ser práctica y accionable. Si durante la impartición de la unidad encuentras ajustes necesarios (ritmo, contenido, evaluación), documéntalos para la próxima edición. La UD7 es una unidad nueva que irá refinándose con la experiencia.
