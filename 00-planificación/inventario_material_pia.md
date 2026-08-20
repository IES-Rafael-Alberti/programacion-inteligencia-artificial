# Inventario del módulo: Programación de Inteligencia Artificial

## 1. Resumen ejecutivo

### Visión general

El módulo PIA cuenta con **∼35 500 ficheros** repartidos entre material docente real, entregas de alumnado, artefactos de corrección, versiones antiguas y residuos técnicos. La mayor parte del volumen (∼34 500 archivos) corresponde a la carpeta `UD4/tareas/`, que mezcla entregas de alumnado, correcciones, CSV de notas, feedback individual y prompts de corrección.

### Tipos de material predominantes

- **Notebooks Jupyter (`.ipynb`)** como formato principal de enseñanza-aprendizaje.
- **Guías y chuletas en Markdown (`.md`)** como material de referencia y consulta.
- **Documentos descriptivos (`.md`, `.docx`, `.pdf`)** para planificación, rúbricas y enunciados.
- **Archivos comprimidos (`.zip`)** con notebooks base, soluciones o empaquetados de tareas.
- **Ficheros de datos (`.csv`, `.pkl`, `.joblib`)** para prácticas y demostraciones.

### Partes bien cubiertas

- **UD1 (Fundamentos Python + NumPy + JAX)**: material muy completo, bien secuenciado, con chuletas, notebooks, soluciones con tests y actividades guiadas.
- **UD2 (Tratamiento de datos: pandas, Polars, DuckDB, R)**: cobertura amplia con notebooks, actividades comparativas y ejercicios seleccionados.
- **UD3 (ML clásico con scikit-learn, cuML, PyCaret)**: bien cubierto, incluye un capstone de películas con rúbrica y defensa oral.
- **UD8 (Visión artificial)**: material compacto pero muy enfocado (U-Net, Mask R-CNN, YOLOv8, tracking, LIME, SHAP, Grad-CAM).
- **UD_Talleres (Series temporales)**: unidad independiente muy completa con notebooks, datasets, scripts, presentaciones y un proyecto final.
- **Planificación y normativa**: el directorio `Docs/` contiene planificaciones, mapas RA-UD, guías de alumnos, mapeo RA-CE y documentación normativa.

### Partes dispersas, duplicadas o problemáticas

- **Desajuste entre la planificación oficial y la estructura real de directorios**: la `PIA_Unidades_Didacticas.md` describe una organización (UD1→UD9 con asignaciones semanales) que NO se corresponde con el contenido real de las carpetas `UD4/`, `UD5/`, `UD6/`, `UD8/` y `UD9/`. Por ejemplo: la UD4 oficial es "ML Tradicional" pero la carpeta `UD4/` contiene deep learning y frameworks; la UD5 oficial es "Deep Learning" pero la carpeta `UD5/` contiene cloud/MLOps; la UD8 oficial es "Automatización" pero la carpeta `UD8/` contiene visión artificial.
- **UD4/ es un vertedero**: 34 469 archivos donde conviven material docente, rúbricas, prompts de corrección, entregas de alumnado, CSV de notas, feedback individual y residuos técnicos.
- **Soluciones duplicadas**: múltiples versiones de soluciones para la misma práctica (`SOLUCIONES.ipynb`, `SOLUCIONES_TESTS.ipynb`, `SOLUCIONES.zip`) repartidas entre el flujo de trabajo y directorios de corrección.
- **Formatos duplicados**: muchos materiales existen como `.md` + `.html` + `.pdf`, a veces con diferencias de contenido.
- **Directorios `*_old/`**: `UD3_old/` a `UD7_old/` contienen material de cursos anteriores sin verificar.
- **Material Neurosimbólico no impartido**: `00-IA-NeuroSimbolica-Plan.md`, `01-UD-IA-NeuroSimbolica-I.md` y copia — planificados pero nunca impartidos.
- **ZIPs sin catalogar**: `PIA_S22/S23/S24 Codigo Fuente.zip`, `Pack_IA_Convergencia*.zip`, `Herramientas para IA-*.zip` — contenido no verificado.
- **Ficheros sensibles**: `openAI-API-Key.txt`, `PageIndez-ApiKey.txt`, `api-key_TheMovieDB.txt`, `hopsWorks-API-KEY.txt` visibles en el repositorio.

---

## 2. Catálogo de materiales docentes

> **Nota**: las rutas son relativas a `/home/jmsa/IESRafaelAlberti/RafaelAlberti25_26/Modulos/PIA/`.
> **⚠ Desajuste importante**: la numeración de directorios NO coincide con las unidades didácticas oficiales. Se indica el bloque real según el contenido de las carpetas.

### Bloque 1 — Fundamentos de programación (UD1 real)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `ud1-fundamentos_programacion_IA/UD1-Doc.md` | Guía docente | md | UD1 | Objetivos, contenidos, evaluación | Python | Completo | Bien alineado con RA1.a |
| `ud1-fundamentos_programacion_IA/pia-ud1.yml` | Entorno | yml | UD1 | Dependencias de Python | Python | Técnico | Soporte de ejecución |
| `ud1-fundamentos_programacion_IA/Sem01/` | Semana 1 (notebooks) | ipynb/md | UD1 | Variables, tipos, control de flujo, funciones, estructuras, introducción a R | Python, Jupyter, R | Completo | 18 notebooks + 2 guías. Incluye versiones base, solución y solución con tests. |
| `ud1-fundamentos_programacion_IA/Sem01/00_ChuletaLsts_Tupls_Diccs_Sets.md` | Chuleta Python | md | UD1 | Referencia rápida de estructuras de datos | Python | Completo | |
| `ud1-fundamentos_programacion_IA/Sem01/00_ChuletaPythonBasico.md` | Chuleta Python básico | md | UD1 | Sintaxis básica de Python | Python | Completo | |
| `ud1-fundamentos_programacion_IA/Sem01/Semana1_Guia.md` | Guía de semana | md/html | UD1 | Planificación de la semana 1 | — | Completo | También existe en HTML |
| `ud1-fundamentos_programacion_IA/Sem01/SemanaR_Guia.md` | Guía de R | md | UD1 | Planificación de la introducción a R | R | Completo | |
| `ud1-fundamentos_programacion_IA/Sem02/` | Semana 2 (notebooks) | ipynb/md | UD1 | NumPy, broadcasting, vectorización, JAX, chuletas | NumPy, JAX | Completo | 8 notebooks + guía. Misma estructura base/solución/tests. |
| `ud1-fundamentos_programacion_IA/Sem02/docs/` | Documentación broadcasting | md/ipynb/puml | UD1 | Apuntes y diagramas sobre broadcasting | Markdown, PlantUML | Completo | Material de apoyo conceptual |
| `ud1-fundamentos_programacion_IA/Sem02/actividadedes/` | Actividad EDA NumPy | ipynb/md | UD1 | Actividad guiada de EDA con NumPy + soluciones | NumPy | Completo | Nombre de carpeta con errata ("actividadedes") |
| `ud1-fundamentos_programacion_IA/Sem02/ejercicios/` | Ejercicios NumPy | ipynb/md | UD1 | Ejercicios de NumPy con tests y README | NumPy | Completo | Versión base y con tests |
| `ud1-fundamentos_programacion_IA/Sem02/NumPy-20251016/` | Tutoriales NumPy externos | ipynb/pdf/epub | UD1 | Material importado de tutoriales NumPy | NumPy | Complementario | Revisar si es necesario o duplicado |
| `ud1-fundamentos_programacion_IA/Sem02/NumPy-20251016.zip` | ZIP de tutoriales | zip | UD1 | Versión comprimida del material anterior | — | Complementario | Contenido duplicado con la carpeta extraída |
| `ud1-fundamentos_programacion_IA/Sem02/Semana2_Guia.md` | Guía de semana | md | UD1 | Planificación de la semana 2 | — | Completo | |

### Bloque 2 — Tratamiento de datos (UD2 real)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `ud2-tratamiento-datos/UD2-Doc.md` | Guía docente | md | UD2 | Objetivos, contenidos, evaluación | Python, R, pandas, json, xml | Completo | Bien definido |
| `ud2-tratamiento-datos/00-EDA-todos-los-Pasos.md` | Guía EDA completa | md | UD2 | Flujo completo de EDA | pandas | Complementario | Resumen transversal |
| `ud2-tratamiento-datos/Sem03/` | Semana 3 (notebooks + docs) | ipynb/md/html | UD2 | pandas fundamentos, EDA, visualización, cuDF, RAPIDS | pandas, cuDF, RAPIDS | Completo | Muy didáctico. Incluye actividades EDA con DuckDB, FireDucks, CuDF. |
| `ud2-tratamiento-datos/Sem03/Documentacion/` | Docs EDA y modelado | md/html/ipynb | UD2 | Guías de EDA, preparación de datos, modelado | pandas, scikit-learn | Completo | Incluye notebooks Titanic/HousePrices |
| `ud2-tratamiento-datos/Sem03/Semana3_Guia.md` | Guía de semana | md | UD2 | Planificación de la semana 3 | — | Completo | |
| `ud2-tratamiento-datos/Sem04/` | Semana 4 (visualización) | ipynb/md/html | UD2 | matplotlib avanzado, Plotly, Altair, Seaborn, hvPlot | matplotlib, Plotly, Altair, Seaborn, hvPlot | Completo | Muy completo, incluye datasets y chuletas |
| `ud2-tratamiento-datos/Sem04/alternativas/` | Alternativas visualización | ipynb/md | UD2 | Chuletas Altair, hvPlot, Panel | Altair, hvPlot, Panel | Completo | Versiones alumno y docente |
| `ud2-tratamiento-datos/Sem04/MatplotLib/` | Notebooks matplotlib | ipynb/md/py | UD2 | Varias versiones de notebooks matplotlib | matplotlib | Completo | Posible duplicación entre versiones |
| `ud2-tratamiento-datos/Sem04/Seaborn/` | Notebooks Seaborn + datos | ipynb/md/csv/parquet/zip | UD2 | Prácticas de visualización con Seaborn | Seaborn, pandas | Completo | Incluye dataset Spotify 2023 |
| `ud2-tratamiento-datos/Sem04/datasets/` | Datasets para prácticas | csv | UD2 | flights, penguins, titanic | — | Completo | Buenos para prácticas |
| `ud2-tratamiento-datos/Sem04/Semana4_Guia.md` | Guía de semana | md | UD2 | Planificación de la semana 4 | — | Completo | |
| `ud2-tratamiento-datos/Sem05/` | Bloque de Polars (varios) | ipynb/md/html/zip | UD2 | Polars, pandas avanzado, R, ejercicios, NLP_old | Polars, pandas, R, PyArrow | Completo | Material muy voluminoso. Incluye Polars, ejercicios seleccionados, R con Titanic |
| `ud2-tratamiento-datos/Sem05/Polars/` | Notebooks Polars | ipynb/md/html | UD2 | Introducción y operaciones con Polars | Polars, pandas, PyArrow | Completo | Muy útil y actual |
| `ud2-tratamiento-datos/Sem05/PandasAvanzado/` | Notebooks pandas avanzado | ipynb/md | UD2 | pandas avanzado, Polars vs PyArrow | pandas, Polars | Completo | |
| `ud2-tratamiento-datos/Sem05/Ejercicios_Seleccionados/` | Colección ejercicios pandas | ipynb | UD2 | 10 ejercicios con soluciones (Getting&Knowing, Filtering, Grouping, Apply, Merge, Stats, Viz, etc.) | pandas | Completo | Muy voluminoso pero útil |
| `ud2-tratamiento-datos/Sem05/r_exercises_titanic_with_tests/` | Ejercicios R con Titanic | Rmd/md | UD2 | Ejercicios con tests en R (filter, group, merge, timeseries, visualization) | R | Completo | Versiones alumno y profesor |
| `ud2-tratamiento-datos/Sem05/NLP_old/` | NLP antiguo (NLTK) | ipynb | UD2 | Notebooks antiguos de NLP con NLTK | NLTK | Obsoleto | Carpeta marcada como `_old`. Revisar si se conserva. |
| `ud2-tratamiento-datos/Sem05/UD2-Guia-sems_5_6_70.md` | Guía semanas 5-6-7 | md/docx/html | UD2 | Planificación extendida | — | Completo | |
| `ud2-tratamiento-datos/Sem05/Semana5_Guia.md` | Guía de semana | md | UD2 | Planificación de la bloque de Polars | — | Completo | |
| `ud2-tratamiento-datos/Sem06/` | Bloque de transformación avanzada (spaCy) | ipynb/md | UD2 | Introducción a spaCy: lemas, POS, entidades, pipeline | spaCy | Completo | 4 notebooks con ejercicios progresivos |
| `ud2-tratamiento-datos/Sem06/Semana6_Guia.md` | Guía de semana | md | UD2 | Planificación de la bloque de transformación avanzada | — | Completo | |
| `ud2-tratamiento-datos/UD2_Semanas_5_6_7_Notebooks/` | Notebooks integrados | ipynb | UD2 | Versión integrada de semanas 5-6-7 | pandas, Polars | Completo | Posible solapamiento con Sem05 y Sem06 |

### Bloque 3 — Machine Learning clásico + feature stores (UD3 real)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD3/Sem07/` | Bloque de EDA aplicado (transición EDA→ML) | md/html/ipynb/pdf/datos | UD3 | EDA, preparación de datos, ML con scikit-learn y cuML | pandas, scikit-learn, RAPIDS, cuML | Completo | Incluye Titanic, California Housing, Bank Marketing |
| `UD3/Sem07/Tarea/` | Tarea Bank Marketing | ipynb/gift/md/html | UD3 | Actividad evaluable con cuestionario GIFT | scikit-learn | Completo | Incluye enunciado y cuestionario Moodle |
| `UD3/Sem07/Actividades/` | Actividades EDA+ML | ipynb/csv/pdf/docx | UD3 | EDA Titanic, Ames Housing, California, CuML vs Sklearn | pandas, scikit-learn, cuML | Completo | Datasets incluidos |
| `UD3/Sem07/scripts/` | Scripts auxiliares | py | UD3 | Script para ensuciar datos | Python | Completo | |
| `UD3/Sem07/datos/` | Datasets | csv/zip | UD3 | bank-additional, archive | — | Completo | |
| `UD3/Sem08/` | Semana 8 (preparación datos) | md/docx/pdf/png | UD3 | Preparación de datos para ML | — | Completo | Documentación, no notebooks |
| `UD3/Sem08/Tarea/` | Tarea Bank Marketing | ipynb | UD3 | Versión en Sem08 de la tarea Bank Marketing | — | Pendiente revisión | Posible duplicado de Sem07/Tarea |
| `UD3/Sem09/` | Semana 9 (creación datasets) | md/docx/ipynb/org/zip | UD3 | Creación de datasets propios con APIs, FastAPI, fuentes abiertas | FastAPI, requests, APIs | Completo | Muy práctico, orientado a producción |
| `UD3/Sem09/Laboratorios/Lab1/` | Lab1: Dataset películas | py/ipynb/md/toml/zip | UD3 | Proyecto estructurado con Poetry para crear dataset de películas | Poetry, Python, APIs TMDB/OMDB | Completo | Incluye rúbrica y enunciado. Muy buena práctica. |
| `UD3/Sem09/Laboratorios/Lab2/` | Lab2: Dataset meteorología | ipynb/md/zip | UD3 | Dataset meteorológico con OpenMeteo y AEMET | APIs clima | Completo | Incluye predicción |
| `UD3/Sem09/Laboratorios/Lab3/` | Lab3: Dataset propio | md/ipynb | UD3 | Creación de dataset propio | — | Esqueleto | Menos desarrollado que Lab1 y Lab2 |
| `UD3/Sem10_a/` | Semana 10 (capstone) | md/html/zip | UD3 | Proyecto guiado de películas con rúbrica, defensa oral | Python, PyCaret, RAPIDS | Completo | Muy rico para evaluación |
| `UD3/Sem10_a/MidtermCapstone/Peliculas/` | Capstone películas completo | md/ipynb/zip | UD3 | Proyecto completo: EDA → modelado PyCaret → modelo final → GPU/RAPIDS | PyCaret, RAPIDS | Completo | Incluye notebooks base y soluciones, rúbrica, defensa oral |
| `UD3/Recordatorio/` | Bloques de repaso | ipynb/md/zip | UD3 | Repaso de pandas, scikit-learn, PyCaret, Poetry, Streamlit | pandas, scikit-learn, PyCaret, Poetry, Streamlit | Completo | Material de refuerzo |
| `UD3/Hopsworks_FeatureStore_Ejemplo.ipynb` | Ejemplo feature store | ipynb | UD3 | Demo de Hopsworks Feature Store | Hopsworks | Complementario | Útil como introducción a MLOps |
| `UD3/Intro_Feature_Store_Hopsworks.md` | Introducción feature store | md | UD3 | Conceptos de feature store | Hopsworks | Complementario | Puente a MLOps |

### Bloque 4 — Deep Learning y frameworks (UD4 real)

> **⚠ UD4 real contiene deep learning, NLP y visión básica, NO ML tradicional como indican los documentos oficiales.**

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD4/README.md` | Índice de UD4 | md | UD4 | Entrada general | — | Completo | Útil como punto de partida |
| `UD4/01-fundamentos/` | Fundamentos DL | varios | UD4 | Material fundamental de deep learning | — | Completo | Requiere revisión detallada. Incluye subcarpetas: docs, notebooks, scripts, old |
| `UD4/02-frameworks/` | Frameworks DL | varios | UD4 | Frameworks de deep learning | varios | Completo | Incluye actividades, data, docs, notebooks |
| `UD4/03-laboratorios/` | Laboratorios | varios | UD4 | Laboratorios prácticos | varios | Completo | Laboratorios 1, 2, 3 |
| `UD4/04-modelado-avanzado/` | Modelado avanzado | varios | UD4 | NLP, visión, proyectos, tareas | varios | Completo | Núcleo técnico de la UD4. Incluye NLP y visión. |

### Bloque 5 — Infraestructura, cloud y MLOps (UD5 real)

> **⚠ UD5 real NO es Deep Learning como indica la planificación oficial.** Contiene infraestructura cloud, MLOps, feature stores y herramientas de datos.

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD5/Documentacion/` | Documentación teórica | md/html/pdf | UD5 | Compute, feature store, cloud, MLOps, almacenamiento, frameworks, APIs LLM, orquestación, vectores, observabilidad, serving | Docker, cloud, MLflow, Ollama, vector DBs | Completo | 14 documentos muy completos y actuales |
| `UD5/Demos/` | Demos prácticas | ipynb/md | UD5 | RAG sencillo, RAG con Ollama, PageIndex, fraude con Hopsworks | Hopsworks, Ollama, RAG | Completo | Demos de aula muy potentes |
| `UD5/Tareas/` | Tarea evaluable | md | UD5 | Comparativa de herramientas cloud/MLOps | Cloud, LLM, MLOps | Completo | Incluye rúbrica |
| `UD5/sesion-HerramientasIA-cloud.md` | Guía de sesión | md | UD5 | Planificación de clase sobre herramientas cloud | cloud tools | Completo | |
| `UD5/sesion_RAG_index.md` | Guía sesión RAG | md | UD5 | Planificación de clase sobre RAG | RAG | Completo | |
| `UD5/cuestionario_1_infraestructura_datos.gift` | Cuestionario Moodle | gift | UD5 | Evaluación rápida sobre infraestructura | Moodle | Completo | |
| `UD5/cuestionario_2_ia_generativa_rag.gift` | Cuestionario Moodle | gift | UD5 | Evaluación rápida sobre IA generativa y RAG | Moodle | Completo | |
| `UD5/quickstart_fraud_model/` | Demo modelo fraude | pkl | UD5 | Modelo XGBoost exportado para demo | XGBoost | Complementario | |
| `UD5/Ejemplos/` | Ejemplos comparativa | md/html | UD5 | Ejemplo de comparativa de herramientas | — | Complementario | |
| `UD5/modelos-gpt-5.4.md` | Notas modelos GPT | md | UD5 | Anotaciones sobre modelos GPT | — | Pendiente revisión | Posible contenido personal/docente |
| `UD5/hopsworks/` | Directorio Hopsworks | — | UD5 | Contenido no explorado | Hopsworks | Sin revisar | |
| `UD5/herramientasCLoudPIA.zip` | ZIP herramientas cloud | zip | UD5 | Material empaquetado sin verificar | — | Pendiente revisión | Descomprimir y catalogar |

### Bloque 6 — LLMs, agentes y orquestación (UD6 real)

> **⚠ UD6 real NO es Big Data/GPU como indica la planificación oficial.** Contiene LangChain, LangGraph, Ollama, FastAPI, MLflow, LlamaIndex, Gradio, DSPy.

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD6/Documentación/` | Documentación de herramientas | md | UD6 | 11 documentos: LangChain, LangGraph, Ollama, FastAPI, MLflow, LlamaIndex, Gradio, DSPy, Herramientas IA | LangChain, LangGraph, Ollama, FastAPI, MLflow, LlamaIndex, Gradio, DSPy | Completo | Muy bien orientado a stack moderno |
| `UD6/Ejemplos Básicos/` | Notebooks introductorios | ipynb | UD6 | Introducción a Gradio, LangChain, DSPy con soluciones y tests | Gradio, LangChain, DSPy | Completo | Buena progresión didáctica |
| `UD6/Ejemplos más avanzados/` | Notebooks avanzados | ipynb/db | UD6 | Pipelines, serving, MCP, LangGraph, MLflow + LlamaIndex RAG | FastAPI, LangGraph, MLflow, LlamaIndex | Completo | Material avanzado de calidad |
| `UD6/cuestionario_1_interfaces_api_serving.gift` | Cuestionario Moodle | gift | UD6 | Evaluación rápida sobre APIs y serving | Moodle | Completo | |
| `UD6/cuestionario_2_orquestacion_rag_optimizacion.gift` | Cuestionario Moodle | gift | UD6 | Evaluación sobre orquestación y RAG | Moodle | Completo | |
| `UD6/Herramientas para IA-20260527.zip` | ZIP herramientas IA | zip | UD6 | Material empaquetado | — | Pendiente revisión | Descomprimir y verificar contenido |

### Bloque 7 — Convergencia tecnológica (UD7)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD7/ConvergenciaTecnologica/` | Núcleo UD7 | pdf/md/pptx/zip | UD7 | Blockchain, convergencia, estrategia corporativa, modelos de negocio, gestión activos, automatización | IA aplicada | Completo | 6 presentaciones PDF + checklist + resumen |
| `UD7/ConvergenciaTecnologica/S19_Blockchain.pdf` | Blockchain | pdf | UD7 | Presentación sobre blockchain | — | Completo | |
| `UD7/ConvergenciaTecnologica/S20_Convergencia.pdf` | Convergencia | pdf | UD7 | Presentación sobre convergencia tecnológica | — | Completo | |
| `UD7/ConvergenciaTecnologica/S21-EstrategiaCorporativa-ModeloDenegocioEtc.pdf` | Estrategia corporativa | pdf | UD7 | Estrategia y modelos de negocio | — | Completo | |
| `UD7/ConvergenciaTecnologica/S22-ModeloDeNegocio-e-IA.pdf` | Modelo de negocio e IA | pdf | UD7 | Impacto de la IA en modelos de negocio | — | Completo | |
| `UD7/ConvergenciaTecnologica/S23-GestionActivosyRecursos.pdf` | Gestión activos | pdf | UD7 | Gestión de activos y recursos | — | Completo | |
| `UD7/ConvergenciaTecnologica/S24-ModelosDeAutomatizacion-PIA.pdf` | Automatización | pdf | UD7 | Modelos de automatización | — | Completo | |
| `UD7/ConvergenciaTecnologica/checklist_convergencia_spotify.md` | Checklist | md | UD7 | Lista de verificación | — | Completo | |
| `UD7/ConvergenciaTecnologica/srcPIAs20.zip` | ZIP fuentes | zip | UD7 | Código fuente empaquetado | — | Pendiente revisión | |
| `UD7/resumenes_S19_a_S24.md` | Resumen temático | md/html | UD7 | Resumen de semanas 19 a 24 | — | Completo | Buen índice |

### Bloque 8 — Visión artificial (UD8 real)

> **⚠ UD8 real NO es Automatización/Despliegue como indica la planificación oficial.** Contiene segmentación, detección de objetos, tracking y explicabilidad.

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD8/Sem22/` | Segmentación y detección | ipynb/md/zip | UD8 | U-Net, Mask R-CNN, métricas de segmentación | PyTorch, torchvision | Completo | Notebooks base + soluciones + tests |
| `UD8/Sem23/` | Tracking | ipynb/md/zip | UD8 | YOLOv8 tracking, SORT, métricas de tracking | Ultralytics, SORT | Completo | Notebooks con soluciones y tests |
| `UD8/Sem24/` | Explicabilidad | ipynb/md/zip | UD8 | LIME (texto), SHAP (tabular), Grad-CAM (CNN) | LIME, SHAP, Grad-CAM | Completo | Muy útil pedagógicamente |
| `UD8/Sem22/Semana22_Guia.md` | Guía semana 22 | md | UD8 | Planificación | — | Completo | |
| `UD8/Sem23/Semana23_Guia.md` | Guía semana 23 | md | UD8 | Planificación | — | Completo | |
| `UD8/Sem24/Semana24_Guia.md` | Guía semana 24 | md | UD8 | Planificación | — | Completo | |

### Bloque 9 — GPU computing, JAX, consolidación (UD9 real)

> **⚠ UD9 real combina GPU computing (Polars, cuDF, JAX) con serving/orquestación y cierre de curso.**

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD9/Sem25/` | IA Neurosimbólica | md/html | UD9 | Material sobre IA Neurosimbólica (no impartido) | — | No impartido | Decidir si conservar o archivar |
| `UD9/Sem25_old/` | Semana 25 antigua | ipynb/md/zip | UD9 | Polars, cuDF, comparativas pandas (material desplazado) | Polars, cuDF | Obsoleto | Marcado como old. Contenido ya cubierto en UD2. |
| `UD9/Sem26/` | RAPIDS + JAX + benchmarks | ipynb/md/zip | UD9 | RAPIDS, JAX, benchmarks GPU | JAX, RAPIDS, cuDF | Completo | Técnico y avanzado |
| `UD9/Sem27/` | Serving y orquestación | md/zip | UD9 | Gradio, LangChain, DSPy, LangGraph, MLflow, FastAPI (guias + zips) | stack IA moderno | Completo | Muy potente. Incluye guías de sesión. |
| `UD9/Sem28/` | Consolidación | md/zip | UD9 | Consolidación de contenidos | varios | Completo | Probable cierre de curso |
| `UD9/Sem29/` | Continuación / cierre | md/zip | UD9 | Continuación del bloque | varios | Completo | |
| `UD9/Sem30/` | Plantillas finales | zip/md | UD9 | Plantillas para cierre | — | Pendiente revisión | Material administrativo/técnico |
| `UD9/herramientasPIA.zip` | ZIP herramientas | zip | UD9 | Material empaquetado sin verificar | — | Pendiente revisión | |

### Proyecto integrado

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD_Proyecto/proyecto.md` | Descripción del proyecto | md | Proyecto | Proyecto asistente de apoyo para la asignatura | documentación, QA | Esqueleto | Bien definido pero breve |
| `UD_Proyecto/evaluacion.md` | Criterios de evaluación | md | Proyecto | Criterios y errores frecuentes | — | Esqueleto | Útil para rúbrica |
| `UD_Proyecto/faq.md` | FAQ del proyecto | md | Proyecto | Decisiones sobre cloud/RAG/herramientas | RAG, vectores | Esqueleto | Muy operativo |

### Taller de series temporales

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `UD_Talleres/SeriesTemporales/` | Taller completo | ipynb/md/pdf/py/csv | Taller | 11 notebooks: intro, datos, análisis, baselines, regresión, FE, DL, TCN, transformers, proyecto, despliegue | Python, PyTorch Lightning, forecasting | Completo | Muy bien organizado. Material de alta calidad. |
| `UD_Talleres/SeriesTemporales/AGENTS.md` | Config agente | md | Taller | Configuración de agente AI para el taller | — | Complementario | |
| `UD_Talleres/SeriesTemporales/registro_errores_preguntas_respuestas.md` | FAQ del taller | md | Taller | Registro de errores y preguntas | — | Complementario | |
| `UD_Talleres/SeriesTemporales/seguimiento_taller.md` | Seguimiento | md | Taller | Seguimiento del taller | — | Complementario | |
| `UD_Talleres/SeriesTemporales/requirements.txt` | Dependencias | txt | Taller | Paquetes necesarios | Python | Completo | |
| `UD_Talleres/datos/` | Datasets adicionales | csv | Taller | clima, consumo, tráfico, ventas | — | Completo | Buenos para prácticas |

### Material transversal y de planificación

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `Docs/PIA_Unidades_Didacticas.md` | Unidades didácticas oficiales | md | Transversal | Descripción de UD1-UD9 con RA/CE, horas y contenidos | — | Completo | Documento OFICIAL pero NO coincide con la estructura real de directorios |
| `Docs/PIA_Mapeo_RA_CE_Semanas.md` | Mapeo RA-UD-semanas | md | Transversal | Tabla resumen RA → UD → Semanas | — | Completo | Útil para trazabilidad normativa |
| `Docs/PIA_Planificacion_Completa.md` | Planificación completa | md/docx/pdf/pptx/tex/org | Transversal | Planificación detallada del curso | — | Completo | Múltiples formatos del mismo contenido |
| `Docs/PIA_Guia_Global.md` | Guía global del módulo | md/pdf | Transversal | Guía general para el alumnado | — | Completo | |
| `Docs/PIA_Guia_Alumnos.pdf` | Guía del alumno | pdf/pptx/png | Transversal | Guía para estudiantes | — | Completo | |
| `Docs/PIA_Justificacion_Normativa.md` | Justificación normativa | md | Transversal | Justificación curricular | — | Completo | |
| `Docs/PIA_Resumen_Infografia.png` | Infografía resumen | png/pdf | Transversal | Resumen visual del módulo | — | Completo | |
| `Docs/PIA_Resumen_Interactivo.html` | Resumen interactivo | html | Transversal | Resumen navegable | — | Completo | |
| `Docs/PIA_Test_RA_CE_Alumnos.pdf` | Test RA-CE | pdf | Transversal | Test de autoevaluación para alumnos | — | Completo | |
| `Docs/PIA_Documentacion_Normativa.zip` | ZIP normativa | zip | Transversal | Documentación normativa empaquetada | — | Pendiente revisión | |
| `Docs/PIA_Unidades_Didacticas.zip` | ZIP unidades | zip | Transversal | Unidades empaquetadas | — | Pendiente revisión | |
| `Docs/PIA_Resumen_Ejecutivo.zip` | ZIP resumen | zip | Transversal | Resumen empaquetado | — | Pendiente revisión | |
| `Docs/CronogramaPIA_2025-2026.md` | Cronograma | md | Transversal | Cronograma del curso 2025-2026 | — | Completo | |
| `Docs/CalendarioEntregaMaterial.md` | Calendario entregas | md | Transversal | Fechas de entrega de materiales | — | Completo | |
| `Docs/SemanasPorUnidad.md` | Semanas por unidad | md | Transversal | Distribución semanal de UDs | — | Completo | |
| `Docs/PlanUsoMateriales.md` | Plan de uso | md | Transversal | Planificación de uso de materiales | — | Completo | |
| `Docs/CuestionarioRA_CE.gift` | Cuestionario RA-CE | gift | Transversal | Cuestionario Moodle sobre RA-CE | Moodle | Completo | |
| `Docs/HorarioBigData.pdf` | Horario | pdf | Transversal | Horario del módulo | — | Completo | |
| `Docs/Libros/BuildingMachineLearningPoweredApps.epub` | Libro de referencia | epub | Transversal | Building ML Powered Apps | — | Complementario | |
| `Docs/notebooks_sem1_a_4_y_R.zip` | ZIP notebooks | zip | Transversal | Notebooks semanas 1-4 empaquetados | — | Pendiente revisión | |

### Entornos virtuales y herramientas

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `EntornosVirtuales/HerramientasEntornosVirtuales1.md` | Guía entornos virtuales | md | Transversal | Guía de entornos virtuales | Python, venv, conda | Completo | |
| `EntornosVirtuales/A-GuiaEntorVirt_ChatGPT5.md` | Guía ChatGPT entornos | md | Transversal | Guía generada con ayuda de ChatGPT | ChatGPT | Completo | |
| `EntornosVirtuales/B-GuiaDespliegue_chatGpt5.md` | Guía despliegue | md | Transversal | Guía de despliegue | — | Completo | |
| `EntornosVirtuales/GuiaEntorVirt_Gemini.md` | Guía Gemini entornos | md | Transversal | Guía generada con Gemini | Gemini | Completo | Incluye backup (~) |
| `EntornosVirtuales/pia_entornos_indice.qmd` | Índice Quarto | qmd | Transversal | Índice de entornos en formato Quarto | Quarto | Complementario | |
| `EntornosVirtuales/pia_entornos.zip` | ZIP entornos | zip | Transversal | Entornos empaquetados | — | Pendiente revisión | |
| `Herramientas/manual_basico_knime.pdf` | Manual KNIME | pdf | Transversal | Manual básico de KNIME | KNIME | Complementario | KNIME aparece en los contenidos básicos oficiales |

### Libros de referencia

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `Libros/` | Biblioteca de referencia | pdf/epub/zip | Transversal | Colección de libros y notebooks sobre ML/DL | varios | Complementario | Incluye Hands-On ML 3ª ed (notebooks), Deep Learning with Python 3ª ed (2025), Grokking ML/DL, etc. |

### Archivos raíz

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `RA_CE-Programacion_IA.md` | RA y CE oficiales | md | Transversal | Resultados de aprendizaje y criterios de evaluación | — | Completo | Documento normativo fundamental |
| `pia-ud1-env.yml` | Entorno Python | yml | Transversal | Dependencias del módulo | Python, conda | Técnico | |
| `Portada-PIA.png` | Portada del módulo | png | Transversal | Imagen de portada | — | Complementario | |
| `Portada-PIA.xcf` | Fuente de portada | xcf | Transversal | Archivo fuente de GIMP | GIMP | Complementario | |
| `prompt_inventario_material_modulo.md` | Prompt de inventario | md | — | Prompt original para generar este inventario | — | Interno | No es material docente |
| `PIA_2026_2027_reorganizado/` | Directorio de reorganización | — | — | Contiene prompts base para reorganización y este inventario | — | En curso | Carpeta de trabajo para la reorganización |

### Material raíz NO incorporado a las UDs (pendiente de clasificar)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `00-IA-NeuroSimbolica-Plan.md` | Plan IA Neurosimbólica | md | — | Planificación de unidad no impartida | — | No incorporado | Decidir si mantener, archivar o eliminar |
| `01-UD-IA-NeuroSimbolica-I.md` | Unidad Neurosimbolica I | md | — | Contenido de unidad no impartida | — | No incorporado | Idem |
| `01-UD-IA-NeuroSimbolica-I (copia).md` | Copia de unidad | md | — | Copia del anterior | — | No incorporado | Eliminable si se decide archivar el original |
| `01-tarea_presentacion_convergencia_IA.md` | Tarea presentación | md | — | Enunciado de tarea sobre convergencia | — | No incorporado | Podría integrarse en UD7 |
| `02_Plantilla_Alumno.md` | Plantilla alumno | md | — | Plantilla para entregas | — | No incorporado | |
| `04_Presentacion_Base.md` | Presentación base | md | — | Base para presentaciones | — | No incorporado | |
| `entrega_y_rubrica_presentacion_convergencia_IA.md` | Rúbrica convergencia | md | — | Rúbrica para la tarea de convergencia | — | No incorporado | Podría integrarse en UD7 |
| `ConformalCalibration.md` | Calibración conforme | md | — | Notas sueltas sobre calibración | — | No incorporado | Requiere contexto |
| `nn.ipynb` | Notebook red neuronal | ipynb | — | Notebook suelto de redes neuronales | — | No incorporado | Sin contexto de unidad |
| `ConvergenciaTecnologica/` | Carpeta suelta | — | — | Parece duplicado de UD7/ConvergenciaTecnologica | — | Sin revisar | Verificar si es duplicado |
| `PresentacionModulo/` | Presentación del módulo | — | — | Material de presentación inicial | — | Sin revisar | Puede ir a recursos comunes |

---

## 3. Materiales de corrección detectados

Se incluyen SOLO aquellos prompts, guías, rúbricas o instrucciones reutilizables para procesos de corrección, no las entregas ni los resultados.

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Estado | Observaciones |
|------|----------|------|---------------|-------------|--------|---------------|
| `UD3/Sem10_a/MidtermCapstone/Peliculas/Practica_Peliculas_OK/docs/06-Rubrica_Peliculas.md` | Rúbrica capstone | md | UD3 | Rúbrica detallada para proyecto de películas con defensa oral | Reutilizable | Extraer a un directorio común de rúbricas |
| `UD3/Sem10_a/MidtermCapstone/Peliculas/DefensaOralPeliculas.md` | Guía defensa oral | md | UD3 | Guía para la defensa oral del capstone | Reutilizable | |
| `UD3/Sem10_a/MidtermCapstone/Peliculas/DefensaOralPeliculas-Chuleta.md` | Chuleta defensa | md | UD3 | Resumen para la defensa oral | Reutilizable | |
| `UD3/Sem10_a/MidtermCapstone/Peliculas/RubricaPeliculas.md` | Rúbrica películas (alternativa) | md | UD3 | Otra versión de rúbrica | Pendiente revisión | Posible duplicado de la anterior |
| `UD3/Sem09/Laboratorios/Lab1/rubrica_datasets_peliculas.md` | Rúbrica Lab1 | md | UD3 | Rúbrica para laboratorio de datasets | Reutilizable | |
| `UD5/Tareas/rubrica-tarea.md` | Rúbrica tarea UD5 | md | UD5 | Rúbrica para la tarea comparativa | Reutilizable | |
| `UD3/Sem09/Laboratorios/Lab1/Entrega_Proyecto_Dataset_Peliculas.md` | Enunciado entrega | md | UD3 | Instrucciones de entrega del proyecto | Reutilizable | |
| `UD3/Sem09/Laboratorios/Lab2/Entrega_Dataset_Meteo.md` | Enunciado entrega | md | UD3 | Instrucciones de entrega Lab2 | Reutilizable | |
| `UD3/Sem09/Laboratorios/Lab3/Entrega_Dataset_Propio.md` | Enunciado entrega | md | UD3 | Instrucciones de entrega Lab3 | Reutilizable | |
| `UD3/Sem09/Laboratorios/Lab2/MeteoPrediccion/Entrega_Prediccion_Meteo.md` | Enunciado entrega | md | UD3 | Instrucciones de entrega predicción | Reutilizable | |

**Nota sobre UD4/tareas/**: esta carpeta contiene múltiples rúbricas y prompts de corrección mezclados con 24 ZIPs de entregas, 42 CSVs de notas, feedback individual y resultados. Se requiere una extracción manual para separar los elementos reutilizables. No se listan aquí individualmente porque —sin una revisión humana— no se puede garantizar qué es reutilizable y qué es específico de un curso.

**Nota sobre UD7/tareas/presentacionesCorregidas/**: mismo problema que UD4. Contiene entregas de alumnado, feedback y resultados mezclados. Requiere extracción manual.

---

## 4. Elementos excluidos deliberadamente

### ZIPs de entregas de alumnado

- **UD4/tareas/**: ∼24 archivos ZIP con entregas de laboratorios y tareas.
- **UD7/tareas/presentacionesCorregidas/**: ZIPs con presentaciones entregadas.
- Varios ZIPs de prácticas en `UD3/Sem09/Laboratorios/` con nombre `mi_dataset_custom.zip`, `Practica_Peliculas_Completa.zip`, etc.

### Repositorios de alumnado

- `Alumnos/`: repositorios personales de estudiantes. Excluir completamente del catálogo docente.

### Descompresiones de tareas

- Directorios como `UD4/tareas/01-Byron/`, `UD4/tareas/01-SanchezNunyezJose/` y similares: resultados de descomprimir entregas de alumnado.

### Artefactos de corrección

- **Correcciones/**: contiene `medias_ud2_ud3_total_byron_jose.csv`, `media_total_por_alumno_pesos_ud1_ud2_ud3.csv`, `estado_general.md` — informes de notas y resultados.
- **UD4/tareas/**: ∼42 CSVs con notas, feedback individual, resultados intermedios.
- **UD7/tareas/presentacionesCorregidas/**: CSVs y MDs con feedback y resultados.

### Residuos técnicos

- `.Rhistory`, `.RData`, `.idea/`, `.vscode/`, `__MACOSX/`, `.pyc`: residuos de herramientas y sistema.
- `salida.csv`, `logs.log`: ficheros de salida de ejecuciones.
- `openAI-API-Key.txt`, `PageIndez-ApiKey.txt`, `hopsWorks-API-KEY.txt`, `charlaEstrategiaLLM.txt`: contenido privado/sensible.

### Cursos anteriores empaquetados

- `PIA_S22 Codigo Fuente.zip`, `PIA_S23 Codigo Fuente.zip`, `PIA_S24 Codigo Fuente.zip`: código fuente de cursos 2022/23/24.
- `UD3_old/`, `UD4_old/`, `UD5_old/`, `UD6_old/`, `UD7_old/`: versiones antiguas de unidades.
- `Pack_IA_Convergencia.zip`, `Pack_IA_Convergencia_v2.zip`: material empaquetado no verificado.

---

## 5. Riesgos, duplicidades y material dudoso

### Desajuste crítico: planificación oficial vs. estructura real

El mayor riesgo detectado es que el documento `Docs/PIA_Unidades_Didacticas.md` (oficial) describe una estructura UD1→UD9 que NO se corresponde con el contenido real de las carpetas:

| UD oficial (según planificación) | Contenido oficial | Contenido real de la carpeta |
|---|---|---|
| UD1 (Sem 1-2) | Fundamentos Python | ✅ Coincide |
| UD2 (Sem 3-6) | Prog. avanzada + R | Parcial: es "tratamiento datos" con pandas, Polars, R, visualización |
| UD3 (Sem 7-9) | EDA con Pandas | ✅ Coincide (incluye ML y feature stores) |
| UD4 (Sem 10-12) | ML Tradicional (sklearn) | ❌ Es Deep Learning, frameworks, NLP, visión |
| UD5 (Sem 13-15) | Deep Learning | ❌ Es infraestructura cloud, MLOps, feature stores |
| UD6 (Sem 16-19) | Big Data / GPU | ❌ Es LLMs, LangChain, Gradio, DSPy |
| UD7 (Sem 20-21) | Convergencia Tecnológica | ✅ Coincide |
| UD8 (Sem 22-24) | Automatización/Despliegue | ❌ Es Visión Artificial (segmentación, tracking, XAI) |
| UD9 (Sem 25-30) | Herramientas Emergentes | Parcial: mezcla GPU computing con serving/LLMs |

**Impacto**: cualquier proceso de reorganización debe decidir si se renumeran las carpetas para alinearlas con la planificación oficial, o si se actualiza la planificación oficial para reflejar la evolución real del módulo.

### Duplicidades detectadas

1. **Soluciones múltiples**: cada notebook tiene hasta 4 versiones: `_SOLUCIONES.ipynb`, `_SOLUCIONES_TESTS.ipynb`, y a veces también `_SOLUCIONES.zip` con los mismos notebooks empaquetados.
2. **Formatos duplicados**: contenido idéntico en `.md` + `.html` + `.pdf` (ej. la documentación de UD5 y las guías de taller).
3. **Tarea Bank Marketing duplicada**: existe en `UD3/Sem07/Tarea/` y `UD3/Sem08/Tarea/`.
4. **Guía EDA duplicada**: `00-EDA-todos-los-Pasos.md` aparece tanto en la raíz de `ud2-tratamiento-datos/` como en `UD3/Sem07/Actividades/`.
5. **Chuletas Python**: `00_ChuletaPythonBasico.md` y `00_ChuletaLsts_Tupls_Diccs_Sets.md` en Sem01 podrían unificarse.
6. **Capstone películas**: existe como ZIP (`Practica_Peliculas_Completa.zip`) y como carpeta descomprimida (`Practica_Peliculas_OK/`).
7. **Convergencia Tecnológica**: existe como carpeta raíz `ConvergenciaTecnologica/` y como `UD7/ConvergenciaTecnologica/`. Verificar si son duplicados.
8. **UD2_Semanas_5_6_7_Notebooks/**: parece una versión integrada cuyo contenido se solapa con `Sem05/` y `Sem06/`.

### Material obsoleto o pendiente de revisión

1. **UD9/Sem25_old/**: notebooks de Polars, cuDF, comparativas — contenido ya cubierto en UD2. Marcar para archivo histórico.
2. **ud2-tratamiento-datos/Sem05/NLP_old/**: notebooks antiguos de NLTK. La UD2 ahora usa spaCy en Sem06.
3. **UD3_old/ a UD7_old/**: material de cursos anteriores sin catalogar. Requiere revisión para determinar si contiene algo no duplicado.
4. **Material Neurosimbólico** (`00-IA-NeuroSimbolica-Plan.md`, `01-UD-IA-NeuroSimbolica-I.md`): planificado pero nunca impartido. Decidir archivo o eliminación.
5. **PIA_S22/S23/S24 Codigo Fuente.zip**: código fuente de cursos anteriores. Revisar antes de archivar o descartar.
6. **Pack_IA_Convergencia.zip**, **Pack_IA_Convergencia_v2.zip**: contenido no verificado.
7. **Herramientas para IA-*.zip** en UD6: contenido no verificado.
8. **herramientasCLoudPIA.zip** en UD5: contenido no verificado.
9. **herramientasPIA.zip** en UD9: contenido no verificado.
10. **KNIME** (`manual_basico_knime.pdf`): herramienta mencionada en los contenidos básicos oficiales pero sin uso aparente en el material actual. Pendiente de decidir si se integra o se archiva.

### Ficheros sensibles (⚠ riesgo de seguridad)

Se han detectado múltiples ficheros con claves de API visibles en el repositorio:
- `openAI-API-Key.txt`
- `PageIndez-ApiKey.txt`
- `UD5/hopsWorks-API-KEY.txt`
- `UD3/Sem09/Laboratorios/Lab1/caso_practico/api-key_TheMovieDB.txt`
- `UD3/Sem09/Laboratorios/Lab1/mi_dataset_peliculas/src/.env`

**Recomendación urgente**: eliminar del historial git (si existe) o al menos añadir a `.gitignore` y rotar las claves expuestas.

---

## 6. Recomendaciones para la siguiente fase

### 6.1 Resolver el desajuste planificación ↔ estructura real

Antes de reorganizar, hay que decidir:
- **Opción A**: Renombrar las carpetas `UD1/`…`UD9/` para que coincidan con la planificación oficial (implica mover todo el contenido de deep learning a UD5, visión a UD8, etc.).
- **Opción B**: Actualizar `PIA_Unidades_Didacticas.md` y `PIA_Mapeo_RA_CE_Semanas.md` para reflejar la estructura que realmente se impartió.
- **Opción C**: Abandonar la numeración UD1–UD9 y usar nombres descriptivos (ej. `fundamentos-python/`, `tratamiento-datos/`, `machine-learning/`, `deep-learning/`, `cloud-mlops/`, `llm-agentes/`, `convergencia/`, `vision-artificial/`, `gpu-avanzado/`).

**Recomendación**: la Opción C es la más limpia a largo plazo, pero requiere actualizar la programación didáctica oficial. La Opción B es más pragmática si se quiere mantener coherencia con la normativa.

### 6.2 Estructura común propuesta para todos los módulos

```
modulo/
├── 00-planificacion/          # Prompts, inventarios, guías de reorganización
├── 01-docentes/               # Material docente principal
│   ├── unidad-01/             # o bloque-tematico-01/
│   │   ├── docs/              # Documentación, teoría, chuletas
│   │   ├── notebooks/         # Notebooks base para alumnos
│   │   ├── soluciones/        # Notebooks resueltos (solo profesor)
│   │   └── datasets/          # Datos para prácticas
│   ├── unidad-02/
│   └── ...
├── 02-evaluacion/             # Materiales de evaluación
│   ├── rubricas/              # Rúbricas reutilizables
│   ├── examenes/              # Cuestionarios GIFT, enunciados
│   └── prompts-correccion/    # Prompts y guías para corregir
├── 03-entregas/               # (No visible en catálogo docente)
│   └── curso-2025-2026/       # ZIPs de alumnado, organizados por tarea
├── 04-correccion/             # (Archivo, no catálogo docente)
│   └── curso-2025-2026/       # CSVs de notas, feedback, informes
├── 05-archivo-historico/      # Cursos anteriores, versiones antiguas
│   ├── ud3_old/
│   ├── codigo-fuente-2024.zip
│   └── ...
├── 06-recursos-transversales/ # Material común a todo el módulo
│   ├── entornos-virtuales/
│   ├── libros/
│   ├── portada.png
│   └── guia-alumno.pdf
├── README.md                  # Descripción del módulo y estructura
└── RA_CE.md                   # Resultados de aprendizaje y criterios
```

### 6.3 Criterios específicos para PIA

1. **Separar urgentemente UD4/**: es la prioridad máxima. Extraer material docente (notebooks, docs) a `01-docentes/ud4-deep-learning/` y dejar entregas/correcciones en `03-entregas/`/`04-correccion/`.

2. **Unificar soluciones**: elegir un formato canónico (ej. `notebook_SOLUCIONES.ipynb` con tests inline) y eliminar/archivar las variantes redundantes.

3. **Eliminar duplicados de formato**: decidir un formato fuente (recomendado: `.md` o `.ipynb`) y archivar los derivados (`.html`, `.pdf`) solo si aportan valor adicional.

4. **Revisar ZIPs pendientes**: descomprimir y catalogar: `Herramientas para IA-*.zip`, `herramientasCLoudPIA.zip`, `herramientasPIA.zip`, `Pack_IA_Convergencia*.zip`, `PIA_S22/23/24 Codigo Fuente.zip`.

5. **Archivar o eliminar material Neurosimbólico**: no se impartió. Decidir si se conserva como referencia o se elimina.

6. **Limpiar ficheros sensibles**: eliminar claves de API del repositorio y rotarlas.

7. **Deshacer la carpeta raíz `ConvergenciaTecnologica/`**: si es duplicado de `UD7/ConvergenciaTecnologica/`, eliminar una copia.

8. **Actualizar la documentación oficial**: `PIA_Unidades_Didacticas.md` y `PIA_Mapeo_RA_CE_Semanas.md` deben reflejar la realidad del curso o la realidad debe ajustarse a ellos.

9. **Normalizar la nomenclatura de semanas**: las carpetas `Sem01/` a `Sem30/` son consistentes pero algunas semanas aparecen con nombres alternativos (`Sem10_a`, `Sem25_old`). Unificar criterio.

10. **Crear un índice de materiales**: un `README.md` por unidad que describa qué contiene, qué herramientas usa y qué RA/CE cubre.
