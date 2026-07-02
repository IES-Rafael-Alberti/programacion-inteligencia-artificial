# Rúbrica de Evaluación — UD9: GPU Avanzado

## Instrumento de evaluación

Proyecto integrador individual/grupal que combina aceleración GPU (RAPIDS/JAX), orquestación de flujos (Prefect) y desarrollo de un pipeline completo con dashboard.

**Peso total en la UD**: 10 puntos
**Criterios de evaluación**: RA2 (b, d, e) y RA3 (a, b)

---

## Criterios y niveles

### 1. Aceleración GPU con RAPIDS y/o JAX (3 puntos)

| Nivel | Descripción | Puntos |
|-------|-------------|--------|
| **Insuficiente** | No se usa GPU de forma efectiva o el código falla al ejecutarse. No hay comparativa con CPU. | 0 – 1.2 |
| **Básico** | Se usa cuDF o JAX de forma básica (ejemplo copiado sin adaptar). La comparativa CPU/GPU existe pero no hay análisis de resultados. | 1.2 – 1.8 |
| **Adecuado** | Se emplea cuDF o JAX sobre datos del proyecto con adaptación real. Se incluye benchmark con tiempos medidos y reflexión sobre los resultados. | 1.8 – 2.4 |
| **Excelente** | Uso combinado de varias herramientas GPU (p. ej. cuDF + cuML, JAX con jit+grad). Análisis detallado de factores de aceleración, limitaciones y contexto de uso. | 2.4 – 3.0 |

---

### 2. Pipeline reproducible (Prefect u orquestación Python) (2 puntos)

| Nivel | Descripción | Puntos |
|-------|-------------|--------|
| **Insuficiente** | No hay pipeline o el código no es ejecutable. Ausencia de estructura modular. | 0 – 0.8 |
| **Básico** | Pipeline funcional con tasks básicos, pero sin gestión de errores, parámetros hardcodeados o dependencias no declaradas. | 0.8 – 1.2 |
| **Adecuado** | Pipeline con tasks bien definidos, parámetros externalizados, y logs suficientes para rastrear la ejecución. Funciona de principio a fin. | 1.2 – 1.6 |
| **Excelente** | Pipeline robusto con manejo de errores, retries, artefactos versionados (`artifacts/`) y documentación de cómo ejecutarlo. Reproducible en otra máquina. | 1.6 – 2.0 |

---

### 3. Dashboard / interfaz de demostración (2 puntos)

| Nivel | Descripción | Puntos |
|-------|-------------|--------|
| **Insuficiente** | No hay dashboard o no arranca. Sin instrucciones de lanzamiento. | 0 – 0.8 |
| **Básico** | Dashboard ejecutable que muestra algún resultado, pero con UI mínima o sin interactividad real. | 0.8 – 1.2 |
| **Adecuado** | Dashboard funcional con al menos un control interactivo, muestra métricas del modelo y permite explorar resultados. | 1.2 – 1.6 |
| **Excelente** | Dashboard pulido con múltiples visualizaciones, validación de inputs, instrucciones integradas y capacidad de demostración en vivo sin errores. | 1.6 – 2.0 |

---

### 4. Calidad técnica y artefactos (1.5 puntos)

| Nivel | Descripción | Puntos |
|-------|-------------|--------|
| **Insuficiente** | Sin métricas, sin modelo guardado, código no funcional o sin estructura coherente. | 0 – 0.6 |
| **Básico** | Métricas básicas presentes (accuracy, loss), modelo guardado pero sin versionado. Estructura parcial. | 0.6 – 0.9 |
| **Adecuado** | Métricas relevantes para el problema, `artifacts/model.joblib`, `metrics.json` y `clean.csv` presentes. Código modular. | 0.9 – 1.2 |
| **Excelente** | Métricas múltiples y justificadas, artefactos completos y versionados, tests mínimos ejecutables, decisiones de diseño documentadas en el README. | 1.2 – 1.5 |

---

### 5. Documentación y presentación (1.5 puntos)

| Nivel | Descripción | Puntos |
|-------|-------------|--------|
| **Insuficiente** | README mínimo o ausente. Sin justificación de decisiones técnicas. Presentación sin estructura. | 0 – 0.6 |
| **Básico** | README con pasos de ejecución básicos. Presentación que cubre el problema y la solución pero sin análisis. | 0.6 – 0.9 |
| **Adecuado** | README claro con instalación, uso y estructura del proyecto. Presentación con demo funcional, métricas y conclusiones. | 0.9 – 1.2 |
| **Excelente** | README completo con diagramas o esquemas. Presentación bien estructurada con narrativa técnica clara, análisis crítico de limitaciones y propuestas de mejora. | 1.2 – 1.5 |

---

## Resumen de ponderación

| Criterio | Peso |
|----------|------|
| 1. Aceleración GPU (RAPIDS/JAX) | 3.0 |
| 2. Pipeline reproducible | 2.0 |
| 3. Dashboard / interfaz | 2.0 |
| 4. Calidad técnica y artefactos | 1.5 |
| 5. Documentación y presentación | 1.5 |
| **Total** | **10.0** |

---

## Resultados de Aprendizaje evaluados

| Criterio | RA evaluado |
|----------|-------------|
| Aceleración GPU | RA2.b, RA2.d, RA2.e |
| Pipeline | RA3.a, RA3.b |
| Dashboard | RA3.b |
| Calidad técnica | RA2.d, RA3.a |
| Documentación | RA2.e, RA3.b |

---

## Notas de aplicación

- La rúbrica se aplica sobre el **proyecto final** entregado antes de la presentación.
- La evaluación individual puede matizarse mediante la **sesión de preguntas** de la presentación.
- El cuestionario [`cuestionario_rapids_jax.gift`](cuestionario_rapids_jax.gift) evalúa los conceptos teóricos de forma independiente.
