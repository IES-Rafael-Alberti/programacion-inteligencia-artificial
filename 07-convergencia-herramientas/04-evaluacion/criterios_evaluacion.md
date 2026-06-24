# Criterios de Evaluación — UD7 Convergencia de Herramientas IA

## Distribución de la Nota

| Componente | Peso | Subcomponentes |
|-----------|------|----------------|
| **Prácticas** (8) | 40% | 8 prácticas de fase (5% cada una) |
| **Proyecto final de UD7** | 40% | Código 50%, Informe 30%, Defensa 20% |
| **Examen Teórico** | 20% | Preguntas de integración y justificación |

**Nota mínima**: 5/10 en cada componente para aprobar la unidad.

> **Alcance**: esta distribución corresponde a la **evaluación interna de UD7**. No debe confundirse con la evaluación del **proyecto final de módulo** en `12-proyecto-integrado`, que es una guía transversal, de tema libre y con seguimiento progresivo durante todo el curso.

---

## 1. Criterios de Evaluación — Prácticas (40%)

### 1.1 Estructura de Evaluación por Práctica

Cada práctica se evalúa sobre 10 puntos con la siguiente distribución:

| Aspecto | Peso | Descripción |
|---------|------|-------------|
| **Funcionalidad** | 40% | El notebook se ejecuta sin errores y produce los resultados esperados |
| **Comprensión** | 30% | Las celdas de análisis y reflexión demuestran comprensión conceptual |
| **Conexión con el stack** | 20% | El alumno identifica cómo esta práctica se conecta con las anteriores |
| **Calidad del código** | 10% | Código limpio, comentado, sin celdas huérfanas |

### 1.2 Criterios Específicos por Práctica

#### P1 — Desarrollo Asistido por IA
- **Objetivo**: Usar herramientas de IA (Copilot, Cursor, Claude Code) para generar código de un pipeline básico
- **Criterios**:
  - [ ] Genera código funcional usando asistentes de IA (40%)
  - [ ] Documenta los prompts utilizados y el proceso de refinamiento (30%)
  - [ ] Evalúa ventajas y limitaciones del desarrollo asistido (20%)
  - [ ] Código bien estructurado y comentado (10%)

#### P2 — Pipeline de Datos
- **Objetivo**: Construir un pipeline ETL automatizado con validación
- **Criterios**:
  - [ ] Pipeline ETL funcional: extracción, transformación, carga (40%)
  - [ ] Validación de datos con pandera o Great Expectations (30%)
  - [ ] Documentación de decisiones sobre transformaciones (20%)
  - [ ] Código modular y reutilizable (10%)

#### P3 — Experimentación con MLflow
- **Objetivo**: Registrar experimentos, comparar modelos y seleccionar el mejor
- **Criterios**:
  - [ ] Al menos 3 experimentos registrados con diferentes configuraciones (40%)
  - [ ] Comparación y selección del mejor modelo basada en métricas (30%)
  - [ ] Modelo registrado en Model Registry con stage (20%)
  - [ ] Trazabilidad: cada experimento tiene descripción y tags (10%)

#### P4 — Orquestación con Prefect
- **Objetivo**: Orquestar el pipeline de ML con Prefect
- **Criterios**:
  - [ ] Flujo Prefect funcional con 3+ tareas encadenadas (40%)
  - [ ] Gestión de dependencias y reintentos configurados (30%)
  - [ ] Captura de logging y estado de cada tarea (20%)
  - [ ] Código del flujo limpio y documentado (10%)

#### P5 — Serving y APIs
- **Objetivo**: Servir modelo con FastAPI profesional
- **Criterios**:
  - [ ] API funcional con endpoint de predicción (40%)
  - [ ] Autenticación con API Key y rate limiting implementados (30%)
  - [ ] Versionado de endpoints y documentación OpenAPI (20%)
  - [ ] Tests de la API con httpx (10%)

#### P6 — Agentes y RAG con Indexación Jerárquica
- **Objetivo**: Construir sistema multi-agente con CrewAI + indexación jerárquica LlamaIndex
- **Criterios**:
  - [ ] Sistema multi-agente funcional con 2+ agentes especializados (40%)
  - [ ] Índice jerárquico con `HierarchicalNodeParser` + `RecursiveRetriever` de LlamaIndex (30%)
  - [ ] Evaluación del sistema multi-agente (RA3e) (20%)
  - [ ] Código modular y reutilizable (10%)
- **Nota**: El RAG tradicional con embeddings + BD vectorial se cubre en el módulo Modelos de la IA. Aquí se avanza a indexación jerárquica.

#### P7 — Observabilidad
- **Objetivo**: Monitorizar modelo con Evidently y detectar drift
- **Criterios**:
  - [ ] Detección de data drift con Evidently y tests estadísticos (40%)
  - [ ] Dashboard HTML generado e interpretado (30%)
  - [ ] Alertas programáticas configuradas (20%)
  - [ ] Conexión explícita con fases anteriores del stack (10%)

#### P8 — IA Responsable
- **Objetivo**: Implementar guardrails, auditoría de sesgo y explicabilidad
- **Criterios**:
  - [ ] Guardrails funcionando sobre inputs/outputs del modelo (40%)
  - [ ] Auditoría de sesgo con Fairlearn (30%)
  - [ ] Explicación SHAP de una predicción individual (20%)
  - [ ] Reflexión sobre implicaciones éticas y regulatorias (10%)

### 1.3 Penalizaciones Comunes

| Incidencia | Penalización |
|------------|-------------|
| Notebook no ejecutable (errores no resueltos) | -3 puntos |
| Celdas de código sin ejecutar | -2 puntos |
| Sin referencias a UD5/UD6 cuando se requiere | -1 punto |
| Código copiado sin atribución | -5 puntos (y posible falta académica) |
| Sin conexión con el flujo convergente | -2 puntos |

---

## 2. Criterios de Evaluación — Proyecto final de UD7 (40%)

Ver `rubrica_proyecto.md` para la rúbrica detallada con niveles de desempeño.

Este proyecto es el cierre de la unidad UD7 sobre stack convergente. Puede reutilizarse o adaptarse como hito técnico del proyecto final de módulo si el tema del equipo lo permite, pero sus pesos y requisitos pertenecen a UD7.

### 2.1 Componentes del Proyecto

| Componente | Peso | Cobertura RA/CE |
|-----------|------|-----------------|
| **Código** | 50% (del 40%) | RA3a, RA3b, RA3c, RA3d, RA3e, RA4a, RA4c, RA4d |
| **Informe técnico** | 30% (del 40%) | RA3a, RA3e, RA4a |
| **Defensa oral** | 20% (del 40%) | RA3e (comunicación de decisiones) |

### 2.2 Requisitos Mínimos para Aprobar

- [ ] Integración de ≥5 herramientas del stack
- [ ] Pipeline ejecutable (Prefect orquestando)
- [ ] API funcional con al menos un endpoint
- [ ] Monitorización básica (Evidently)
- [ ] Explicabilidad (SHAP o LIME)
- [ ] README con instrucciones
- [ ] Informe técnico entregado

### 2.3 Penalizaciones

| Incidencia | Penalización |
|------------|-------------|
| <5 herramientas integradas | Suspenso directo |
| Pipeline no ejecutable | -30% del componente código |
| Sin monitorización | -20% del componente código |
| Sin explicabilidad | -15% del componente código |
| Informe sin justificación RA | -30% del componente informe |
| Sin defensa oral | Suspenso directo (proyecto) |

---

## 3. Criterios de Evaluación — Examen Teórico (20%)

### 3.1 Estructura del Examen

| Tipo de pregunta | Cantidad | Valor | Total |
|-----------------|----------|-------|-------|
| Opción múltiple | 10 | 0.5 puntos | 5 puntos |
| Verdadero/Falso | 5 | 0.4 puntos | 2 puntos |
| Respuesta corta | 3 | 1 punto | 3 puntos |

**Duración**: 60 minutos
**Material**: No se permite material, salvo hoja de fórmulas oficial del stack.

### 3.2 Áreas Evaluadas

| Área | % del examen | RA asociado |
|------|-------------|-------------|
| Integración del stack convergente | 30% | RA3a, RA3b |
| Conexiones entre herramientas | 25% | RA3c, RA4a |
| Seguridad e IA responsable | 20% | RA3d |
| Observabilidad y monitorización | 15% | RA4c |
| Automatización y orquestación | 10% | RA4a, RA4d |

### 3.3 Tipos de Pregunta

**Opción Múltiple**: Preguntas sobre integración y conexiones entre herramientas (NO sobre herramientas individuales).
- *Ejemplo*: "¿Qué herramienta del stack se encarga de detectar cambios en la distribución de los datos de entrada?"

**Verdadero/Falso**: Afirmaciones sobre el flujo convergente y dependencias entre fases.
- *Ejemplo*: "La monitorización con Evidently debe configurarse antes de desplegar la API de serving."

**Respuesta Corta**: Justificación de decisiones de integración y análisis de casos.
- *Ejemplo*: "Explica cómo se conectarían Prefect y MLflow en un pipeline de re-entrenamiento automático."

### 3.4 Penalizaciones

| Incidencia | Penalización |
|------------|-------------|
| Respuestas literales sobre herramientas sin contexto de integración | -25% del valor de la pregunta |
| Confundir herramientas entre fases | -50% del valor de la pregunta |

---

## 4. Cálculo de la Nota Final

```
Nota Final = (Media Prácticas × 0.40) + (Proyecto × 0.40) + (Examen × 0.20)
```

**Escala**:

| Nota | Calificación |
|------|-------------|
| 9.0–10 | Sobresaliente (SB) |
| 7.0–8.9 | Notable (NT) |
| 5.0–6.9 | Aprobado (AP) |
| 0.0–4.9 | Suspenso (SS) |

### 4.1 Condiciones para Aprobar

1. Nota final ≥ 5.0
2. Nota mínima en cada componente (prácticas, proyecto, examen) ≥ 5.0
3. Proyecto de UD7 entregado y defendido
4. Asistencia ≥ 80% a las sesiones prácticas

### 4.2 Recuperación

| Componente suspenso | Recuperación |
|-------------------|-------------|
| Prácticas | Repetir prácticas suspensas con nuevos datos (nota máxima 7) |
| Proyecto | Repetir proyecto completo con entregas parciales (nota máxima 7) |
| Examen | Examen escrito de recuperación (nota máxima 7) |

---

## 5. Mapeo RA/CE — Evaluación

| RA | CE | % Nota Final | Se evalúa en |
|----|----|-------------|-------------|
| RA3 | a) Unificación | 20% | Prácticas P1, P5 + Proyecto |
| RA3 | b) Conexión tecnológica | 8% | Práctica P2 |
| RA3 | c) Evaluación sistemas | 8% | Práctica P2 |
| RA3 | d) Seguridad en negocio | 12% | Prácticas P5, P8 + Proyecto |
| RA3 | e) Toma de decisiones | 12% | Práctica P6 + Proyecto + Defensa |
| RA4 | a) Estrategias corporativas | 8% | Práctica P4 |
| RA4 | c) Automatización industrial | 16% | Prácticas P3, P7 + Proyecto |
| RA4 | d) Evaluación conveniencia | 8% | Práctica P3 |

---

## 6. Recomendaciones para el Alumno

1. **No memorices herramientas aisladas** —concéntrate en cómo se conectan entre sí.
2. **Cada práctica construye sobre la anterior** —no la dejes para el final.
3. **El proyecto final es tu portfolio** —dedica tiempo a que esté bien documentado.
4. **Las preguntas del examen son de integración** —si solo sabes herramientas sueltas, no aprobarás.
5. **La defensa oral es importante** —practica la demo, prepara respuestas sobre tus decisiones técnicas.
