# Rúbrica de Evaluación — UD9: GPU Avanzado

## Instrumento de evaluación

Proyecto integrador individual/grupal que combina aceleración GPU (RAPIDS/JAX), orquestación de flujos (Prefect) y desarrollo de un pipeline completo con dashboard.

**Peso total en la UD**: 10 puntos
**Criterios de evaluación**: RA2 (b, d, e) y RA3 (a, b)

---

## Criterios y niveles

### 1. Aceleración GPU con RAPIDS (3 puntos)

Este criterio requiere evidencia obtenida en una **GPU NVIDIA verificable** (local o mediante Google Colab/runtime cloud indicado por el profesorado): EDA con cuDF, entrenamiento con cuML y benchmark frente al baseline CPU. JAX es una ampliación o complemento y no sustituye ninguna de esas evidencias. El trabajo realizado solo en CPU puede apoyar el desarrollo, pero no acredita el criterio.

| Nivel | Descripción | Puntos |
|-------|-------------|--------|
| **Insuficiente** | No se aporta evidencia verificable de ejecución en GPU NVIDIA, falta el EDA con cuDF o el entrenamiento con cuML, el código GPU falla o no hay comparativa con CPU. | 0 – 1.2 |
| **Básico** | Se usan cuDF y cuML de forma básica. La comparativa CPU/GPU existe, pero no hay análisis de resultados. | 1.2 – 1.8 |
| **Adecuado** | Se emplean cuDF para el EDA y cuML para el entrenamiento sobre datos del proyecto. Se incluye benchmark con tiempos medidos y reflexión sobre los resultados. | 1.8 – 2.4 |
| **Excelente** | Uso sólido de cuDF y cuML, con benchmark reproducible y análisis detallado de aceleración, limitaciones y contexto de uso. JAX puede aportar una comparación adicional. | 2.4 – 3.0 |

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
