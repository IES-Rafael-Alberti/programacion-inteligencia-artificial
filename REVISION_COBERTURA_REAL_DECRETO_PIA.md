# Revisión de cobertura frente al Real Decreto — PIA 2026-2027

**Norma de referencia:** Real Decreto 279/2021, de 20 de abril, por el que se establece el Curso de especialización en Inteligencia Artificial y Big Data y se fijan los aspectos básicos del currículo.

**Módulo revisado:** 5073. Programación de Inteligencia Artificial.

**Fuente principal:** BOE-A-2021-7686, Real Decreto 279/2021.
**Fuente secundaria:** índices editoriales disponibles en `../ParaLaRevision_IndicesLibros.md`.

## Veredicto ejecutivo

El curso reorganizado cubre los **RA/CE del Real Decreto** de forma suficiente para impartición, pero hay cuatro puntos que conviene reforzar documentalmente para que la defensa sea más limpia:

1. **RA1.b/c/f**: dejar más explícita la comparación de lenguajes y formatos/marcado.
2. **Contenidos básicos RA1**: mencionar explícitamente Java, JavaScript/NodeJS y JSON como lenguajes/formatos de comparación, aunque no se desarrollen en profundidad.
3. **RA3.d y RA3.e**: seguridad en convergencia tecnológica y toma de decisiones estratégicas deben aparecer como evidencia evaluable, no sólo como contenido técnico disperso.
4. **RA4.a/b/d**: automatización industrial/de negocio, relación empresa-cliente, gestión de recursos y conveniencia del modelo necesitan una evidencia empresarial obligatoria en UD7 o proyecto final.

La revisión no detecta una necesidad de rehacer el curso. Detecta, sobre todo, necesidad de **blindaje documental y evaluativo**.

## Lectura normativa usada

El Real Decreto identifica el curso como **Inteligencia Artificial y Big Data**, Grado Superior, familia Informática y Comunicaciones, 600 horas y 36 ECTS. La competencia general exige programar y aplicar sistemas inteligentes que optimicen la gestión de información y explotación de datos masivos, garantizando seguridad, accesibilidad, usabilidad, calidad y principios éticos/legales.

Dentro del anexo I, el módulo 5073 tiene 12 ECTS y cuatro resultados de aprendizaje:

| RA | Enfoque normativo |
|---|---|
| RA1 | Lenguajes de programación e idoneidad para IA. |
| RA2 | Desarrollo de aplicaciones de IA con entornos de modelado. |
| RA3 | Mejora de negocios mediante convergencia tecnológica. |
| RA4 | Modelos de automatización industrial y de negocio orientados a resultados empresariales. |

Los contenidos básicos del módulo incluyen, además de Python/R y entornos de IA, referencias explícitas a Java, JavaScript, NodeJS, JSON, lenguajes de marcado, cloud, IoT, blockchain, seguridad, estrategias corporativas, modelos de negocio, gestión de activos y modelos de automatización.

## Matriz de cobertura por RA/CE

| RA/CE del RD 279/2021 | Cobertura actual | Evidencia principal del curso | Riesgo documental | Acción recomendada |
|---|---|---|---|---|
| **RA1. Caracteriza lenguajes de programación valorando su idoneidad en IA.** | Cubierto | UD1, UD2, UD3, UD4, UD6, UD9; Python, R, Pandas, scikit-learn, PyCaret, Keras, PyTorch, JAX, RAPIDS, APIs. | Medio | Hacer explícita una comparación de lenguajes/formatos. |
| RA1.a estructura de un programa informático | Cubierto | UD1: sintaxis, control de flujo, funciones, estructuras de datos, NumPy. | Bajo | Mantener evidencia inicial. |
| RA1.b características de lenguajes según aplicación | Cubierto parcialmente explícito | Python como base; R como complemento; frameworks y librerías por contexto. | Medio | Tabla comparativa Python/R/Java/JavaScript/NodeJS/JSON. |
| RA1.c lenguaje apropiado para la aplicación | Cubierto parcialmente explícito | Decisiones prácticas en notebooks, pipelines, APIs y proyecto final. | Medio | Exigir justificación breve de elección tecnológica en prácticas clave. |
| RA1.d lenguajes para desarrollo de IA | Cubierto | Ecosistema Python/R/JAX/RAPIDS; frameworks IA y datos. | Bajo | Referenciar bibliotecas, rendimiento, soporte y comunidad. |
| RA1.e lenguaje apropiado para aplicación de IA | Cubierto | UD3/UD4/UD6/UD9/UD12, elección según problema, despliegue y rendimiento. | Bajo-medio | Añadir criterio de rúbrica: idoneidad del lenguaje/herramienta. |
| RA1.f lenguajes de marcado y etiquetas | Cubierto implícito | Markdown, YAML, JSON, notebooks, APIs, configuración, documentación. | Medio | Añadir microactividad/documento sobre JSON/YAML/Markdown/XML/HTML en IA. |
| **RA2. Desarrolla aplicaciones de IA utilizando entornos de modelado.** | Muy cubierto | UD3, UD4, UD5, UD6, UD7, UD8, UD9, UD10, UD12. | Bajo | No requiere reestructuración. |
| RA2.a plataformas de IA | Cubierto | Cloud/MLOps, APIs LLM, PyCaret, Hopsworks, MLflow, LlamaIndex, herramientas cloud. | Bajo | Conservar comparativas como evidencia. |
| RA2.b entornos de modelado | Cubierto | scikit-learn, PyCaret, TensorFlow/Keras, PyTorch, JAX, RAPIDS, notebooks, pipelines. | Bajo | Indicar en rúbricas que se evalúa elección del entorno. |
| RA2.c modelo según problema | Cubierto | Clasificación, regresión, visión, series temporales, LLM/RAG, proyecto final. | Bajo | Mantener justificación problema-modelo-métrica. |
| RA2.d implementación de la aplicación | Muy cubierto | Notebooks, APIs, dashboards, agentes, pipelines, proyecto integrado. | Bajo | Ninguna acción prioritaria. |
| RA2.e evaluación de resultados | Cubierto | Métricas, benchmarks, XAI, MLflow/Evidently, rúbricas, defensas. | Bajo | Insistir en interpretación, no sólo ejecución. |
| **RA3. Evalúa mejoras en los negocios integrando convergencia tecnológica.** | Cubierto, pero sensible | UD5, UD7, UD9, UD10, UD12. | Medio-alto | Convertir impacto empresarial/seguridad/decisión en evidencia obligatoria. |
| RA3.a ventajas de unificar procesos, servicios, herramientas, métodos y sectores | Cubierto | Stack convergente de datos, entrenamiento, tracking, serving, RAG, agentes y observabilidad. | Medio | Pedir mejora de proceso/productividad en informes. |
| RA3.b sistemas que facilitan la conexión tecnológica | Cubierto | APIs, cloud, Prefect, MLflow, LlamaIndex, CrewAI, RAPIDS/JAX, dashboards. | Bajo | Mantener evidencias técnicas. |
| RA3.c características de dichos sistemas | Cubierto | Comparativas de herramientas, arquitectura de pipelines, serving y observabilidad. | Bajo | Mantener comparativas. |
| RA3.d seguridad en negocios por convergencia tecnológica | Parcial | Seguridad de credenciales, IA responsable, trazabilidad, guardrails, observabilidad. | Alto | Añadir apartado evaluable de riesgos, seguridad, privacidad y límites. |
| RA3.e toma de decisiones estratégicas en negocio conectado | Cubierto parcial | Dashboards, métricas, forecasting, benchmarks y proyecto final. | Medio-alto | Exigir conclusión ejecutiva basada en datos. |
| **RA4. Evalúa modelos de automatización industrial y de negocio.** | Cubierto parcial formal | UD7 y UD12, apoyo UD5/UD10. | Alto | Es el bloque más importante a reforzar documentalmente. |
| RA4.a estrategias corporativas y modelos de negocio | Parcial | Proyecto final, casos aplicados y defensa. | Alto | Añadir apartado obligatorio “estrategia/modelo de negocio/proceso afectado”. |
| RA4.b relación empresa-cliente y gestión de activos/recursos | Parcial | Proyecto final con fuentes de datos, usuarios y salida útil. | Alto | Exigir usuarios, cliente/proceso, datos como activo y recursos afectados. |
| RA4.c modelos de automatización para requerimientos industriales/de negocio | Cubierto | Prefect, pipelines, APIs, dashboards, MLflow, serving, automatización de flujos. | Medio | Relacionar cada automatización con requerimiento concreto. |
| RA4.d conveniencia del modelo para resultados esperados | Cubierto parcial | Comparación de modelos, métricas, benchmarks y defensa. | Alto | Añadir coste-beneficio, riesgos y alternativa descartada. |

## Revisión por contenidos básicos del Real Decreto

| Contenido básico del RD | Cobertura actual | Lectura crítica |
|---|---|---|
| Programa informático, etapas y lenguajes | Cubierto en UD1 | Correcto. |
| Características de lenguajes para IA: bibliotecas, rendimiento, herramientas, soporte | Cubierto, pero disperso | Conviene consolidar en una tabla o mini-informe. |
| Python, R, Java, JavaScript, NodeJS, JSON | Python/R cubiertos; JSON implícito; Java/JS/Node sólo contextual | No hace falta enseñar Java/Node a fondo, pero sí compararlos formalmente para cubrir RD. |
| Lenguajes de marcado e información de etiquetas | Implícito | Añadir evidencia explícita con Markdown/YAML/JSON/XML/HTML. |
| Plataformas IA, librerías y servicios | Muy cubierto | Curso actualizado respecto al RD. |
| Entornos de modelado y herramientas | Muy cubierto | Curso supera índices editoriales. |
| Modelado de redes neuronales | Cubierto en UD4/UD8/UD10 | Correcto. |
| Herramientas de generación de código inteligente | Cubierto parcialmente en UD6/UD7 | Puede documentarse mejor como uso responsable de asistentes/LLM. |
| Voz, datos, sonido, imágenes | Datos/imágenes muy cubiertos; voz/sonido menos | No es crítico para PIA si se justifica como ejemplos de conexión tecnológica. |
| Blockchain, IoT, Cloud | Cloud cubierto; IoT contextual; blockchain casi no aparece | Añadir una nota comparativa: blockchain como tecnología de convergencia, no como eje de IA. |
| Seguridad en convergencia tecnológica | Parcial | Reforzar con evidencia obligatoria. |
| Estrategias corporativas, modelos de negocio, gestión de activos, automatización | Parcial | Reforzar en UD7/UD12. |

## Comparación secundaria con índices editoriales

Los índices editoriales confirman que los manuales suelen organizar el módulo de forma muy cercana al Real Decreto:

- Marcombo separa explícitamente las unidades de RA1, RA2, RA3 y RA4.
- Ra-Ma amplía mucho la parte técnica de IA aplicada: ML, deep learning, visión, NLP, análisis de datos.

Comparado con esos índices, el curso reorganizado:

- supera la cobertura técnica moderna en ML, MLOps, LLM, RAG, agentes, XAI, GPU y series temporales;
- está más actualizado técnicamente que los índices revisados;
- necesita hacer más visible la parte formal de negocio/convergencia/automatización que los manuales sí suelen aislar en capítulos propios.

La comparación editorial no cambia el veredicto: **el criterio principal debe seguir siendo el Real Decreto**.

## Acciones recomendadas por prioridad

### Prioridad 1 — blindaje legal directo

1. Añadir en UD12/proyecto final una sección obligatoria:
   - proceso o negocio afectado;
   - usuarios/clientes;
   - datos como activo;
   - recursos implicados;
   - automatización propuesta;
   - resultado esperado;
   - alternativa descartada;
   - riesgos, seguridad y límites.

2. Añadir en UD7 una evidencia breve de convergencia tecnológica:
   - qué procesos/herramientas se integran;
   - qué mejora produce;
   - qué riesgo de seguridad aparece;
   - cómo ayuda a decidir.

### Prioridad 2 — RA1 formal

3. Añadir una mini-actividad o anexo de comparación de lenguajes y formatos:
   - Python;
   - R;
   - Java;
   - JavaScript/NodeJS;
   - JSON;
   - Markdown/YAML/XML/HTML;
   - criterios: librerías IA, rendimiento, integración, soporte, caso de uso y limitaciones.

### Prioridad 3 — contenidos básicos sensibles pero no centrales

4. Añadir una nota corta sobre Blockchain/IoT/Cloud:
   - Cloud: tecnología activa del curso;
   - IoT: ejemplo de fuente de datos/conexión tecnológica;
   - Blockchain: tecnología de convergencia a conocer, pero no eje práctico de programación de IA salvo caso justificado.

## Conclusión

El curso está **apto frente a RA/CE**, especialmente en RA2. El riesgo no está en la falta de contenidos técnicos, sino en que algunos CE de negocio/convergencia/automatización pueden quedar **implícitos** si no se exige una evidencia escrita.

La corrección recomendada es pequeña y muy rentable: añadir evidencias breves, evaluables y trazables en UD7/UD12, y una comparativa formal de lenguajes/formatos en UD1/UD2.
