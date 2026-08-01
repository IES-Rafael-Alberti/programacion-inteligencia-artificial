# Programación de Inteligencia Artificial — PIA 2026-2027

Material público del módulo **Programación de Inteligencia Artificial (PIA)** para el curso 2026-2027.

## Propósito

Centralizar el material del módulo en una estructura navegable por unidades, separando teoría, ejemplos, prácticas, evaluación y recursos de apoyo.

La reorganización parte principalmente del curso 2025-2026, con rescates selectivos del curso 2024-2025 y documentación nueva para UD7 y el proyecto integrado. El curso está **operativamente terminado / semicerrado**: es utilizable en el aula y solo quedan validaciones externas o mejoras que aconseje su uso real.

## Mapa de directorios

| Ruta | Contenido principal | Estado |
|------|---------------------|--------|
| `01-fundamentos-python/` | Fundamentos de Python, estructuras, NumPy y recursos iniciales. | Operativa; evaluación normalizada |
| `02-tratamiento-datos/` | Pandas, Matplotlib/Seaborn, Plotly, Polars, DuckDB, cuDF y transformación de datos. | Operativa; ruta evaluable definida |
| `03-machine-learning/` | Scikit-learn, PyCaret, feature stores, datasets propios y capstone intermedio. | Operativa; Pixi y capstone validados |
| `04-deep-learning/` | Fundamentos de deep learning, frameworks y laboratorios. | Operativa; ruta canónica saneada |
| `05-cloud-mlops/` | Cloud, MLOps, RAG, serving, observabilidad y herramientas de datos. | Operativa; tarea canónica definida |
| `06-llm-agentes/` | LLM, agentes, LangChain/LangGraph, Ollama, FastAPI, Gradio, DSPy y MCP. | Operativa; MCP integrado |
| `07-convergencia-herramientas/` | Stack convergente IA: datos, MLflow, Prefect, FastAPI, LlamaIndex, CrewAI, observabilidad e IA responsable. | Completa, verificada y archivada |
| `08-vision-xai/` | Visión por computador, segmentación, detección, tracking y explicabilidad. | Operativa; ruta evaluable definida |
| `09-gpu-avanzado/` | RAPIDS, JAX, benchmarks GPU y cierre avanzado. | Operativa; evidencia GPU definida |
| `10-series-temporales/` | Taller de series temporales y notebooks asociados. | Operativa; proyecto evaluable definido |
| `11-anexos/` | Material avanzado u optativo: neurosimbólica y aprendizaje por refuerzo. | Anexo opcional; fuera de la evaluación ordinaria |
| `12-proyecto-integrado/` | Mini-proyectos y proyecto final progresivo con integración de fuentes de datos. | Operativa; documentación completada |

## Cómo usar este repositorio

1. Empezar por la unidad correspondiente (`01-...` a `12-...`).
2. Dentro de cada unidad, usar la estructura común:
   - `01-teoria/`: apuntes y guías conceptuales.
   - `02-ejemplos/`: ejemplos, scripts y notebooks demostrativos.
   - `03-practicas/`: ejercicios, laboratorios y actividades.
   - `04-evaluacion/`: rúbricas, cuestionarios y materiales evaluables.
   - `05-recursos/`: datasets, chuletas, enlaces y material de apoyo.
   - `90-archivo/`: versiones antiguas o material pendiente de revisar.
   - `99-profesor/`: guías, soluciones o notas de uso docente.
3. Consultar `12-proyecto-integrado/` para el proyecto final y su seguimiento progresivo.
4. Usar las guías del proyecto integrado como referencia para entregas largas y defensa final.

## Decisiones clave

- La estructura usa nombres descriptivos y numeración de unidades para facilitar navegación y secuenciación.
- **Pixi** es el gestor operativo de entornos del módulo; cada actividad debe usar el entorno indicado en su guía, no un entorno universal.
- UD7 se considera cerrada y verificada.
- En UD7, la fase F6 se orienta a **LlamaIndex con indexación jerárquica + ParkingCorp + CrewAI**, no a un RAG plano con ChromaDB.
- **Prefect** queda como herramienta principal de orquestación; Airflow se mantiene solo como referencia comparativa.
- El proyecto integrado se redefine como un itinerario de mini-proyectos más un proyecto final libre, progresivo y con al menos dos fuentes de datos.

## Estado actual resumido

**Veredicto:** operativamente terminado / semicerrado y listo para uso docente.

Completado:

- Reorganización general en 12 unidades.
- Evaluación transversal normalizada en las unidades activas.
- Entornos operativos definidos con Pixi.
- MCP integrado como contenido activo de UD6.
- UD7 completa y verificada.
- Documentación del proyecto integrado completada.
- Criterios de proyecto y checkpoints del proyecto final añadidos.

Pendientes no bloqueantes:

- Validar los cuestionarios GIFT de UD1 y UD2 cuando Moodle esté disponible.
- Comprobar Pixi y los ejemplos seleccionados en Windows/macOS cuando haya equipos disponibles.
- Ajustar materiales concretos solo si la experiencia de aula revela una necesidad docente.

## Buenas prácticas de uso

- Los notebooks y scripts docentes deben usar únicamente placeholders como `TU_API_KEY` o `YOUR_API_KEY`.
- No subas credenciales, tokens, datos personales ni datasets no autorizados en entregas del alumnado.
- Las unidades pueden contener material ampliable: prioriza siempre las guías y prácticas indicadas por el profesorado.

## Enlaces útiles

- [UD7 — Convergencia de herramientas IA](07-convergencia-herramientas/README.md)
- [Proyecto integrado](12-proyecto-integrado/README.md)
- [Guía del proyecto final](12-proyecto-integrado/01-teoria/proyecto.md)
- [Evaluación del proyecto integrado](12-proyecto-integrado/01-teoria/evaluacion.md)
- [Checkpoints del proyecto final](12-proyecto-integrado/01-teoria/checkpoints_proyecto_final.md)
- [Manual de Pixi para PIA](docs/manual-pixi-pia.md)
- [Normas de entrega y uso de IA](docs/normas-entregas-y-uso-de-ia.md)
