# Mapa de Mini-Proyectos — PIA

## Resumen

El curso se organiza con dos carriles paralelos:

| Carril | Función | Evaluación |
|---|---|---|
| **Mini-proyectos comunes** | Aprender herramientas y conceptos con un caso guiado | Mínimos comunes por bloque |
| **Proyecto final progresivo** | Aplicar lo aprendido a un tema libre del equipo | Entregas parciales + defensa final |

Cada mini-proyecto debe terminar con una transferencia al proyecto final: el alumnado aplica la misma técnica, herramienta o criterio a su propio caso.

## Regla de trabajo

Cada bloque sigue esta secuencia:

1. **Caso guiado común**: todo el grupo trabaja sobre el mismo problema.
2. **Técnica o herramienta**: se introduce solo cuando hace falta para avanzar.
3. **Aplicación al proyecto final**: cada equipo adapta lo aprendido a su proyecto.
4. **Checkpoint breve**: se revisa si el proyecto final sigue siendo viable.

## Mapa por bloques

| Bloque | Mini-proyecto común | Qué aprende el alumnado | Aplicación al proyecto final |
|---|---|---|---|
| 01. Fundamentos Python | Analizador simple de datos de incidencias | Lectura de datos, estructuras, funciones, scripts reproducibles | Preparar estructura inicial del repositorio y primer script de carga |
| 02. Tratamiento de datos | Limpieza e integración de dos fuentes de incidencias | Limpieza, unión de fuentes, validación, detección de nulos y duplicados | Definir y probar las dos fuentes de datos del proyecto propio |
| 03. Machine Learning | Clasificador base de incidencias | Train/test split, baseline, métricas, comparación de modelos | Crear primer modelo base o primera métrica inteligente del proyecto |
| 04. Deep Learning | Clasificador o extractor con red neuronal sencilla | Cuándo aporta valor una red neuronal y cuándo no | Decidir si el proyecto necesita deep learning o si basta ML clásico |
| 05. Cloud/MLOps | Registro de experimentos y artefactos | MLflow, versionado, trazabilidad de experimentos | Registrar experimentos propios y documentar la mejor configuración |
| 06. LLM y agentes | Asistente básico sobre documentación conocida | Prompting, herramientas, agentes, límites de LLM | Valorar si el proyecto necesita LLM/agente o si sería forzado |
| 07. Convergencia herramientas | Stack integrado: Prefect + FastAPI + LlamaIndex jerárquico + CrewAI + observabilidad | Conectar piezas: pipeline, API, RAG jerárquico, monitorización, IA responsable | Integrar al menos una pieza de producción: API, pipeline, observabilidad o RAG/agente |
| 08. Visión/XAI | Explicación y análisis de errores | Interpretabilidad, explicación de predicciones, comunicación de resultados | Añadir explicación, análisis de errores o justificación de decisiones del modelo |
| 09. GPU avanzado | Optimización o inferencia eficiente | Coste, rendimiento, límites de recursos | Evaluar si el proyecto necesita optimización o puede ejecutarse en local |
| 10. Series temporales | Predicción de evolución temporal | Fechas, ventanas, tendencia, estacionalidad, validación temporal | Aplicar si el proyecto tiene dimensión temporal; si no, justificar que no aplica |
| 11. Anexos | Extensión opcional | RL/neurosimbólica si encaja | Solo para proyectos avanzados o ampliaciones voluntarias |
| 12. Proyecto integrado | Cierre del proyecto propio | Integración, documentación, defensa | Entrega final y defensa |

## Checkpoints del proyecto final

| Momento | Entrega | Evidencia mínima |
|---|---|---|
| CP0 — Idea inicial | Propuesta breve | Problema, usuarios, utilidad, primera idea de datos |
| CP1 — Datos | Fuentes confirmadas | Al menos dos fuentes viables y diferenciadas |
| CP2 — Integración | Dataset integrado | Unión real entre fuentes, no concatenación artificial |
| CP3 — Baseline | Primer resultado | Modelo simple, métrica o análisis inteligente inicial |
| CP4 — Trazabilidad | Experimentos registrados | MLflow u hoja técnica equivalente con resultados comparables |
| CP5 — Producto mínimo | Salida útil | API, dashboard, informe, asistente, recomendador o ranking |
| CP6 — Calidad | Evaluación y límites | Métricas, errores, sesgos, explicabilidad o monitorización |
| CP7 — Defensa | Entrega final | Repositorio, informe y presentación |

## Familias de proyecto recomendadas

| Familia | Posibles fuentes | Resultado útil |
|---|---|---|
| Videojuegos multijugador | Historial de partidas, mapas, personajes, estadísticas de equipo | Recomendador de estrategias, composición de equipo o rutas de ataque |
| Deportes | Estadísticas de rendimiento, salarios, valor de mercado, lesiones | Detección de jugadores infravalorados o predicción de rendimiento |
| Aparcamiento inteligente | Matrículas, entradas/salidas, tarifas, ocupación, incidencias | Facturación, localización de vehículos, alertas de ocupación |
| Recomendación | Catálogo, interacciones de usuarios, valoraciones | Recomendador de productos, contenidos, cursos o recursos |
| Demanda y precios | Ventas históricas, calendario, clima, eventos | Predicción de demanda o precios dinámicos |
| Soporte/incidencias | Tickets, logs, base de conocimiento, tiempos de resolución | Clasificación, priorización o asistente de soporte |
| Educación | Calificaciones, entregas, asistencia, recursos consultados | Detección temprana de riesgo, recomendación de refuerzo |
| Servicios urbanos | Datos abiertos, incidencias ciudadanas, clima, tráfico | Priorización de recursos o análisis de zonas problemáticas |

## Qué no es suficiente

| Propuesta insuficiente | Por qué no vale | Cómo mejorarla |
|---|---|---|
| Un CSV + un notebook | No hay integración real ni producto | Añadir segunda fuente y salida útil |
| Dashboard descriptivo | Puede no tener IA/ML | Añadir predicción, clasificación, ranking o alertas |
| Chatbot genérico | No está grounded en datos propios | Conectar a documentos/datos del proyecto y evaluar respuestas |
| Copia de Kaggle | No demuestra integración ni decisiones propias | Adaptar problema, añadir fuentes y justificar cambios |
| Modelo sin uso final | No hay producto ni usuario | Crear API, informe, ranking, dashboard o asistente |

## Uso docente recomendado

- Mantener los mini-proyectos guiados como mínimos evaluables.
- No permitir que el proyecto final empiece tarde: debe avanzar desde el primer tercio del curso.
- Devolver propuestas flojas cuanto antes, no en la entrega final.
- Permitir temas libres, pero exigir integración real y una salida útil.
- Usar ejemplos de proyectos de años anteriores como referencia, señalando qué estaba bien y qué hubo que reforzar.

## Relación con la guía principal

Este documento concreta el mapa de trabajo. La guía completa del proyecto final está en:

- [`proyecto.md`](proyecto.md)

Para la transferencia desde UD7, usar como referencia el proyecto de stack convergente: [`../../07-convergencia-herramientas/01-teoria/10_stack_convergente.md`](../../07-convergencia-herramientas/01-teoria/10_stack_convergente.md).
