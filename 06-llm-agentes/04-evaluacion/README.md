# Evaluación — UD6 LLM y agentes

Esta carpeta reúne los instrumentos para evaluar la unidad de interfaces, APIs, serving de modelos, orquestación, RAG y agentes. Los cuestionarios GIFT existentes se mantienen como evaluación teórica o complementaria; la entrega principal debe evidenciar una solución práctica y reproducible.

La entrega está sujeta a las [normas comunes de entrega y uso de IA](../../docs/normas-entregas-y-uso-de-ia.md). Deben declararse las herramientas utilizadas y aportarse evidencias de verificación, sin incluir secretos ni conversaciones completas.

## Camino rápido

1. Construye un proyecto integrado a partir de `03-practicas/100_mlflow_llamaindex_rag.ipynb` y adapta a ese proyecto el patrón de API de `03-practicas/103_fastapi_serving_modelos.ipynb`.
2. Entrega el código, notebooks y evidencias siguiendo `checklist-entrega.md`.
3. Revisa la calificación esperada con `rubrica.md`.
4. Realiza los cuestionarios GIFT si el profesorado los activa en Moodle.

## Qué se evalúa

| Bloque | Evidencia esperada |
| --- | --- |
| Funcionamiento de la solución | Notebook, script o aplicación que ejecuta el flujo principal sin errores relevantes. |
| Orquestación y RAG | Pipeline con prompts, recuperación documental, herramientas, agentes o grafos cuando proceda. |
| Serving e interfaz | Uso adecuado de Gradio, FastAPI u otra interfaz/API trabajada en la unidad. |
| Evaluación y trazabilidad | Pruebas manuales, métricas, registros, MLflow o evidencias equivalentes si la práctica lo incorpora. |
| Documentación y reproducibilidad | Instrucciones claras, estructura ordenada y explicación de decisiones técnicas. |
| Uso responsable | Gestión segura de claves, límites del modelo y advertencias sobre errores o alucinaciones. |

## Evidencias de entrega

- Código fuente o notebooks completados.
- Instrucciones de ejecución suficientes para reproducir la solución.
- Capturas, logs o ejemplos de entrada/salida que demuestren el funcionamiento.
- Breve explicación de arquitectura: componentes, flujo de datos y decisiones principales.
- Ficheros de configuración o dependencias si ya forman parte de la práctica.

No se deben entregar claves API, tokens, credenciales ni datos sensibles.

## Relación con prácticas y notebooks

La ruta canónica combina RAG, evaluación/trazabilidad y serving con:

- `100_mlflow_llamaindex_rag.ipynb`: base de recuperación sobre documentos, ejemplos de respuesta y registro de resultados.
- `103_fastapi_serving_modelos.ipynb`: patrón independiente de contrato de entrada y pruebas con una API de clasificación Iris. No sirve el RAG del notebook `100`; debe adaptarse al flujo construido por el alumnado.

`99_herramientas_ia_integradas.ipynb` sirve como introducción con ejemplos y fallbacks simulados; no sustituye por sí solo la entrega funcional. El resto de prácticas de `06-llm-agentes/03-practicas/` permiten ampliar o sustituir un bloque cuando el profesorado lo indique:

- `96_gradio_model.ipynb`: interfaz rápida para probar modelos.
- `97_langchain_pipeline.ipynb`: pipeline con LangChain.
- `98_dspy_mcp.ipynb`: optimización programática y MCP integrado.
- `99_herramientas_ia_integradas.ipynb`: introducción a herramientas y patrones integrados.
- `100_mlflow_llamaindex_rag.ipynb`: RAG con trazabilidad/evaluación cuando proceda.
- `101_langgraph_orquestacion.ipynb`: orquestación con grafos y estado.
- `102_ollama_modelos_locales.ipynb`: modelos locales.
- `103_fastapi_serving_modelos.ipynb`: serving profesional mediante API.

El entregable evaluable es el proyecto integrado por el alumnado, no la mera ejecución de ambos notebooks. El profesorado puede aceptar otra arquitectura que produzca las mismas evidencias. No todas las herramientas tienen que aparecer en una misma entrega.

## Cuestionarios disponibles

- `cuestionario_1_interfaces_api_serving.gift`: Gradio, FastAPI, serving e interfaces.
- `cuestionario_2_orquestacion_rag_optimizacion.gift`: LangChain, LangGraph, RAG, LlamaIndex, DSPy y optimización.

Estos cuestionarios sirven para comprobar comprensión conceptual, reforzar contenidos y preparar la corrección. No sustituyen automáticamente a la rúbrica práctica salvo decisión expresa del profesorado.

## Criterios de superación

- La entrega alcanza al menos 5 sobre 10 en la rúbrica.
- El flujo principal puede revisarse con evidencias verificables.
- No hay fallos críticos de seguridad, como publicación de claves o secretos.
- La solución está suficientemente documentada para que otra persona pueda ejecutarla o revisarla.

Si una entrega no ejecuta, se valorarán las partes inspeccionables, pero no se concederán puntos funcionales que dependan de una ejecución no verificada.

## MCP

MCP forma parte del contenido integrado de la unidad cuando aparece en las prácticas. Además, el material de `06-llm-agentes/05-recursos/mcp-refuerzo/` puede usarse como refuerzo opcional si el grupo lo necesita. No debe convertirse en una dependencia externa obligatoria de la entrega salvo que el enunciado concreto lo indique.
