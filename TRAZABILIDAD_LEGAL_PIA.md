# Trazabilidad legal — Programación de Inteligencia Artificial

Este documento recoge una evidencia rápida de alineación entre los resultados de aprendizaje y criterios de evaluación del módulo **Programación de Inteligencia Artificial** y la organización real del curso 2026-2027.

Su objetivo es defensivo y operativo: demostrar que el curso cubre lo exigido por la normativa, aunque los materiales estén actualizados respecto a los índices editoriales disponibles.

## Fuente normativa verificada

- Real Decreto 279/2021, de 20 de abril, BOE-A-2021-7686.
- Módulo 5073: Programación de Inteligencia Artificial.
- Revisión detallada: [`REVISION_COBERTURA_REAL_DECRETO_PIA.md`](REVISION_COBERTURA_REAL_DECRETO_PIA.md).

## Veredicto rápido

El curso está **alineado con los RA/CE del módulo** y, en varios bloques, supera la cobertura que sugieren los índices editoriales revisados.

Los puntos que conviene hacer más explícitos no requieren rehacer el curso, sino añadir o reforzar evidencias documentales:

- comparación formal de lenguajes para IA;
- uso de formatos/lenguajes de marcado y serialización de datos;
- impacto de negocio, seguridad y toma de decisiones en la convergencia tecnológica;
- justificación de modelos de automatización industrial o de negocio.

## Tabla de trazabilidad

| Resultado de aprendizaje / criterio | Cobertura en el curso | Evidencias actuales | Estado | Refuerzo recomendado |
|---|---|---|---|---|
| **RA1. Caracteriza lenguajes de programación valorando su idoneidad en el desarrollo de IA.** | UD1 principalmente; apoyo en UD2, UD4, UD6 y UD9. | `01-fundamentos-python/` trabaja Python, estructuras, funciones, NumPy, JAX y R. UD2 trabaja herramientas de datos. UD4 compara frameworks de deep learning. UD6 y UD9 amplían el ecosistema con APIs, agentes, GPU y JAX. | **Cubierto** | Añadir una evidencia breve y explícita de comparación de lenguajes para IA. |
| CE RA1.a — estructura de un programa informático. | UD1. | Ejercicios de Python básico: sintaxis, variables, control de flujo, funciones y estructuras de datos. | **Cubierto** | Mantener como evidencia inicial. |
| CE RA1.b/c — características e idoneidad de lenguajes según la aplicación. | UD1, UD2, UD4, UD6, UD9. | Python como lenguaje base; R como complemento; JAX/RAPIDS para aceleración; FastAPI/Gradio para interfaces; frameworks Keras/PyTorch/JAX/TensorFlow. | **Cubierto parcialmente explícito** | Crear una mini-actividad o tabla comparativa: Python, R, JavaScript/Node, Java, JSON y casos de uso en IA. |
| CE RA1.d/e — características e idoneidad de lenguajes para IA. | UD1, UD3, UD4, UD9. | NumPy, Pandas, scikit-learn, PyCaret, Keras, PyTorch, JAX, RAPIDS/cuML. | **Cubierto** | Vincular explícitamente bibliotecas, rendimiento, soporte y ecosistema con la elección del lenguaje. |
| CE RA1.f — lenguajes de marcado y etiquetas. | UD1, UD3, UD5, UD6, UD12. | Uso transversal de JSON/YAML/Markdown/notebooks/configuración, APIs y documentación de proyectos. | **Cubierto de forma implícita** | Añadir una evidencia corta sobre JSON/YAML/Markdown/XML/HTML como formatos de intercambio, configuración, documentación y APIs en IA. |
| **RA2. Desarrolla aplicaciones de IA utilizando entornos de modelado.** | UD3, UD4, UD5, UD6, UD8, UD9, UD10 y UD12. | Scikit-learn, PyCaret, CuML, Keras, PyTorch, JAX, TensorFlow, cloud/MLOps, RAG, agentes, visión, series temporales y proyecto final. | **Muy cubierto** | No requiere ampliación estructural. |
| CE RA2.a — evaluar plataformas de IA. | UD5, UD6, UD7, UD12. | Comparativas cloud, herramientas de MLOps, APIs LLM, RAG, agentes, feature stores y herramientas convergentes. | **Cubierto** | Conservar tareas comparativas como evidencia. |
| CE RA2.b — caracterizar entornos de modelado de IA. | UD3, UD4, UD5, UD9, UD10. | Scikit-learn/PyCaret, TensorFlow/Keras/PyTorch/JAX, RAPIDS/cuML, notebooks, pipelines y entornos cloud. | **Cubierto** | Hacer visible en rúbricas que se evalúa la elección del entorno. |
| CE RA2.c — definir el modelo según el problema. | UD3, UD4, UD8, UD10, UD12. | Clasificación, regresión, deep learning, segmentación, tracking, XAI, forecasting y proyecto final con problema elegido. | **Cubierto** | Reforzar en entregas la justificación problema-modelo-métrica. |
| CE RA2.d — implementar aplicación de IA. | UD3, UD4, UD5, UD6, UD7, UD8, UD9, UD10, UD12. | Laboratorios, notebooks, APIs, dashboards, pipelines, agentes, proyectos integradores y proyecto final. | **Cubierto** | Ninguno prioritario. |
| CE RA2.e — evaluar resultados obtenidos. | UD3, UD4, UD6, UD7, UD8, UD9, UD10, UD12. | Rúbricas, cuestionarios GIFT, métricas, benchmarks, XAI, MLflow/Evidently, checklists y defensas. | **Cubierto** | Insistir en interpretación de métricas, no sólo ejecución técnica. |
| **RA3. Evalúa mejoras en los negocios integrando convergencia tecnológica.** | UD5, UD7, UD9 y UD12. | Cloud, MLOps, feature stores, APIs, orquestación, observabilidad, IA responsable, dashboards y proyecto final aplicado. | **Cubierto, pero debe hacerse más explícito** | Añadir evidencia de impacto empresarial y toma de decisiones en UD7/UD12. |
| CE RA3.a — ventajas de unificar procesos, servicios, herramientas, métodos y sectores. | UD5, UD7, UD12. | Stack convergente: datos, entrenamiento, tracking, serving, RAG, agentes, observabilidad y proyecto final. | **Cubierto** | Explicitar “mejora de productividad / proceso” en informes. |
| CE RA3.b/c — sistemas que facilitan conexión tecnológica y sus características. | UD5, UD7, UD9. | Cloud, APIs, FastAPI, Prefect, MLflow, LlamaIndex, CrewAI, RAPIDS/JAX, dashboards y pipelines. | **Cubierto** | Mantener como evidencia técnica principal. |
| CE RA3.d — seguridad en negocios mediante convergencia tecnológica. | UD5, UD6, UD7, UD12. | Buenas prácticas de credenciales, IA responsable, Guardrails, observabilidad, trazabilidad de uso de IA y control de entregas. | **Cubierto de forma parcial** | Añadir apartado obligatorio de riesgos, seguridad y límites en proyecto final o UD7. |
| CE RA3.e — mejora en toma de decisiones estratégicas. | UD7, UD9, UD10, UD12. | Dashboards, métricas, forecasting, benchmarks, evaluación de modelos e integración de fuentes de datos. | **Cubierto** | Pedir una conclusión ejecutiva basada en datos en proyectos. |
| **RA4. Evalúa modelos de automatización industrial y de negocio relacionándolos con resultados esperados.** | UD7 y UD12 principalmente; apoyo en UD5 y UD11 opcional. | Pipelines automatizados, orquestación, proyecto final con salida útil, integración de fuentes y defensa técnica. | **Cubierto, pero es el bloque más sensible formalmente** | Añadir evidencia empresarial obligatoria en proyecto final. |
| CE RA4.a — nuevas estrategias corporativas y modelos de negocio. | UD7, UD12. | Casos de uso aplicados, diseño de solución útil, defensa del proyecto y relación con problema real. | **Cubierto parcial** | Añadir apartado “modelo de negocio / proceso afectado / usuarios”. |
| CE RA4.b — relación empresa-cliente y gestión de activos/recursos. | UD12, apoyo en UD7. | Proyecto final con fuentes de datos, salida útil e impacto esperado. | **Cubierto parcial** | Pedir análisis explícito de usuarios, recursos, datos y valor entregado. |
| CE RA4.c — modelos de automatización para requerimientos industriales y de negocio. | UD5, UD7, UD12. | Orquestación con Prefect, tracking con MLflow, serving, APIs, dashboards y pipelines reproducibles. | **Cubierto** | Relacionar cada automatización con el requerimiento de negocio. |
| CE RA4.d — conveniencia de cada modelo para resultados esperados. | UD7, UD9, UD10, UD12. | Comparación de modelos, métricas, benchmarks, elección de herramientas y defensa final. | **Cubierto** | Añadir justificación coste-beneficio, riesgos y alternativa descartada. |

## Comparación con los índices editoriales revisados

| Bloque de los índices | Situación en nuestro curso |
|---|---|
| Introducción a IA, historia, tipos y estado de la IA. | Cubierto como contexto inicial, pero el curso no se queda en teoría introductoria. |
| Lenguajes, Python, herramientas y datasets. | Cubierto en UD1, UD2 y UD3. Conviene reforzar la evidencia formal de idoneidad de lenguajes. |
| Machine learning clásico. | Cubierto de forma amplia en UD3, con prácticas, datasets y evaluación. |
| Deep learning y frameworks. | Cubierto en UD4 y ampliado con JAX/RAPIDS/GPU en UD9. |
| Visión artificial. | Cubierto en UD8 con segmentación, tracking y explicabilidad. |
| NLP, chatbots y LLM. | Cubierto de forma más actual en UD6 con LLM, RAG, agentes y herramientas modernas. |
| Análisis de datos y series temporales. | Cubierto en UD2 y UD10. |
| Cloud, entornos de modelado y herramientas de generación de código. | Cubierto en UD5, UD6 y UD7. |
| Convergencia tecnológica, automatización y negocio. | Cubierto en UD5, UD7 y UD12, aunque conviene explicitar más la evidencia empresarial. |

## Acciones mínimas recomendadas

Para blindar la trazabilidad legal sin rehacer el curso:

1. Añadir en UD1 una actividad breve de **comparativa de lenguajes y formatos para IA**.
2. Añadir en UD7 o UD12 un apartado evaluable de **impacto empresarial, seguridad, toma de decisiones y automatización**.
3. En el proyecto final, exigir una sección corta: **proceso afectado, usuarios, valor esperado, riesgos, alternativa descartada y criterio de conveniencia**.

Con esas tres evidencias, la alineación legal queda más fácil de defender ante revisión, reclamación o programación didáctica.
