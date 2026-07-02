# Rúbrica — UD6 LLM y agentes

Rúbrica sobre 10 puntos para entregas prácticas de la unidad. Ajustar solo si el enunciado concreto limita o amplía el alcance.

## Escala de desempeño

| Nivel | Referencia |
| --- | --- |
| Insuficiente | No cumple el criterio o no hay evidencia verificable. |
| Básico | Cumple parcialmente, con errores o justificación débil. |
| Adecuado | Cumple de forma correcta y revisable. |
| Excelente | Cumple con solidez, claridad y decisiones bien justificadas. |

## Criterios

| Criterio | Peso |
| --- | ---: |
| 1. Funcionamiento y reproducibilidad | 2,0 |
| 2. Diseño de prompts, pipeline y orquestación | 1,5 |
| 3. RAG, herramientas o agentes | 1,5 |
| 4. Serving, API o interfaz de usuario | 1,5 |
| 5. Evaluación, trazabilidad y MLflow si aplica | 1,0 |
| 6. Documentación técnica y explicación | 1,5 |
| 7. Uso responsable, seguridad y límites | 1,0 |
| **Total** | **10,0** |

## 1. Funcionamiento y reproducibilidad — 2,0 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | La solución no ejecuta o falta la parte principal de la entrega. |
| Básico | Ejecuta parcialmente, pero requiere correcciones manuales importantes o no queda claro el entorno. |
| Adecuado | Ejecuta el flujo principal con instrucciones suficientes y resultados verificables. |
| Excelente | Es reproducible, está ordenada y contempla errores comunes o casos límite. |

## 2. Diseño de prompts, pipeline y orquestación — 1,5 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | Usa llamadas aisladas sin estructura clara ni control del flujo. |
| Básico | Hay pipeline básico, pero con pasos poco conectados o prompts poco justificados. |
| Adecuado | El flujo está estructurado, con entradas/salidas claras y decisiones razonadas. |
| Excelente | La orquestación es mantenible, separa responsabilidades y gestiona estado o ramificaciones cuando procede. |

## 3. RAG, herramientas o agentes — 1,5 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No incorpora recuperación, herramientas o agentes cuando la práctica lo exige. |
| Básico | Integra componentes, pero sin justificar ingesta, recuperación, chunking, herramientas o estado. |
| Adecuado | Implementa RAG, herramientas o agentes con flujo comprensible y evidencias de respuesta. |
| Excelente | Justifica decisiones de recuperación/orquestación y muestra limitaciones, mejoras o comparativas. |

## 4. Serving, API o interfaz de usuario — 1,5 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay interfaz/API usable o no se puede probar. |
| Básico | La interfaz/API funciona de forma parcial o con contratos de datos débiles. |
| Adecuado | Expone la solución mediante Gradio, FastAPI u opción equivalente con entradas y salidas claras. |
| Excelente | Incluye validación, manejo de errores, documentación de endpoints o experiencia de uso cuidada. |

## 5. Evaluación, trazabilidad y MLflow si aplica — 1,0 punto

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay pruebas, ejemplos de validación ni evidencias de calidad. |
| Básico | Incluye pruebas manuales o capturas, pero con poca trazabilidad. |
| Adecuado | Aporta ejemplos, métricas, logs o seguimiento suficiente para revisar resultados. |
| Excelente | Usa evaluación sistemática, comparación de versiones, MLflow o registro equivalente cuando la práctica lo justifica. |

## 6. Documentación técnica y explicación — 1,5 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | Falta explicación o la entrega no permite entender qué se ha hecho. |
| Básico | Describe la solución de forma superficial o desordenada. |
| Adecuado | Explica objetivo, ejecución, estructura, decisiones y resultados principales. |
| Excelente | La documentación guía la revisión, anticipa problemas y conecta decisiones técnicas con el objetivo. |

## 7. Uso responsable, seguridad y límites — 1,0 punto

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | Publica secretos, ignora riesgos o presenta respuestas del modelo como siempre fiables. |
| Básico | Menciona límites de forma genérica, pero sin aplicarlos a la solución. |
| Adecuado | Protege claves, evita datos sensibles y advierte de limitaciones del modelo. |
| Excelente | Incluye controles, validaciones o recomendaciones de uso responsable adaptadas al caso. |

## Penalizaciones y revisión manual

- No duplicar penalizaciones por la misma causa.
- Redondear la nota al final.
- Si faltan dependencias o el entorno impide ejecutar, registrar la limitación y valorar solo evidencias inspeccionables.
- Marcar revisión manual ante dudas de autoría, entrega corrupta, secretos expuestos o discrepancias graves entre evidencias.
