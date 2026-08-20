# Comparativa multi-curso del módulo: Programación de Inteligencia Artificial

## 1. Resumen ejecutivo

### Diagnóstico general

El curso **25-26 es estructural y pedagógicamente superior al 24-25** en casi todos los bloques técnicos (RA1, RA2). El material del 25-26 está mejor secuenciado, usa notebooks como formato principal (frente a org→pdf del 24-25), tiene guías de semana, soluciones con tests, y una progresión más coherente.

El curso **24-25 tiene dos fortalezas que el 25-26 ha perdido**:
1. **Actividades H5P interactivas** para Moodle (UD1, UD2) — el 25-26 apenas las usa.
2. **Apuntes org-mode/LaTeX/PDF** de alta calidad académica para RA1/RA2, que sirven como referencia teórica.
3. **Material de evaluación de resultados** (13-EvaluacionDeResultados/) con conformal prediction, calibración — contenido avanzado que el 25-26 no cubre como unidad independiente.

### Riesgos principales si se reorganiza solo el curso actual

1. **RA3 y RA4 siguen siendo el punto débil**: ni el 24-25 ni el 25-26 tienen material docente sólido. Ambos cursos delegaron estos RA en un trabajo de alumnado. La nota del profesor lo confirma: «el material que hay de otros años es... no sé cómo definirlo pero pésimo».
2. **La parte de "empresas/modelos de negocio" está desorientada**: los contenidos básicos oficiales hablan de estrategias corporativas, pero el profesor indica que hay que orientarlos a herramientas de programación de IA.
3. **Blockchain no tiene cabida**: ni en 24-25 ni en 25-26 se impartió. La nota del profesor es clara: «no lo veo para nada en esto».
4. **El material de H5P del 24-25 se perderá** si no se rescata expresamente.
5. **La evaluación de resultados (calibración, conformal prediction)** del 24-25 es avanzada y valiosa pero no está integrada en el 25-26.

### Nota del profesor: impacto en la decisión

La nota del profesor (líneas 45-47 de RA_CE-Programacion_IA.md) es EL factor determinante para RA3/RA4:

| Afirmación | Impacto en la decisión |
|---|---|
| «Los contenidos básicos oficiales están obsoletos» | No guiarse por los contenidos básicos para la estructura de unidades. Usar RA/CE como guía, no los contenidos. |
| «La parte de empresas/modelos de negocio hay que orientarla a herramientas de IA» | RA3/RA4 deben reenfocarse hacia herramientas de programación IA, no a teoría de negocio. |
| «El material existente de RA3/RA4 es pésimo» | No rescatar prácticamente nada de 17-20-* (24-25) ni de UD7 (25-26) como material base. |
| «Blockchain no se ha impartido ni parece relevante» | Excluir blockchain del temario. No conservar material. |
| «RA3 y RA4 se han cubierto con un trabajo» | El enfoque de "trabajo de alumnado" no es suficiente. Hay que crear material docente. |

---

## 2. Mapa de versiones comparadas

| Versión | Ruta base | Estado general | Observaciones |
|---|---|---|---|
| **24-25 (curso pasado)** | `01-04-Programacion/`, `05-ComputaNube/`, `06-10-Herramientas/`, `11-20-*`, etc. | Sólido en RA1, disperso en RA2, muy pobre en RA3/RA4 | Formato org→PDF. Buenas H5P. Evaluación de resultados destacable. Cajón de sastre en `06-10-Herramientas/`. |
| **25-26 (curso actual)** | `ud1-fundamentos_programacion_IA/`, `ud2-tratamiento-datos/`, `UD3/`…`UD9/` | Muy sólido en RA1/RA2. RA3/RA4 cubiertos con trabajo de alumnado. | Notebooks como formato principal. Mejor secuenciación. UD4 es un vertedero. UD5/UD6/UD7/UD8/UD9 NO coinciden con planificación oficial. |

---

## 3. Comparativa por unidad/bloque

### 3.1 RA1 — Fundamentos de programación (Python, NumPy, JAX)

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `ud1-fundamentos_programacion_IA/Sem01/` + `Sem02/` | 18+8 notebooks con base/solución/tests. Chuletas. Guías de semana. JAX incluido. Actividad EDA NumPy. | Sin actividades H5P. Sin apuntes org editables. | ✅ **Base principal** |
| **24-25** | `01-04-Programacion/Tema00/` a `Tema04/` + `Ejercicios/` + H5Ps | Apuntes org editables. 6 actividades H5P interactivas. Cuestionarios GIFT. Ejercicios variados. | Sin chuletas. Sin notebooks con tests. Mojo experimental (innecesario). | 🟡 **Rescatar H5P y GIFT** |

**Base recomendada:** `ud1-fundamentos_programacion_IA/` (25-26)

**Piezas a rescatar del otro curso:**
- `01-04-Programacion/Ejer01-RA1.h5p` y hermanos (×6) — actividades H5P interactivas para Moodle. El 25-26 no tiene nada similar.
- `01-04-Programacion/Ejercicios-PIA_RA1-S01_04.gift` — cuestionario GIFT para Moodle.
- `01-04-Programacion/01_IntroProgramacionIA.org` — fuente org-mode editable si se quiere mantener ese flujo.
- `01-04-Programacion/Ejercicios/` — ejercicios variados que pueden complementar los notebooks.

**Material a archivar o descartar:**
- `01-04-Programacion/Mojo/` — lenguaje experimental no consolidado. Archivar como referencia histórica.
- `01-04-Programacion/Pandas, Seaborn, Matplotlib-20241002.zip` — contenido duplicado con Tema02 y con 25-26. Archivar si se verifica duplicación.
- `01-04-Programacion/AprendeIA_Python-EjerciciosMaterial_web.zip` y `PracticarPython*.zip` — origen externo no verificado. Pendiente de revisión.

**Huecos o mejoras necesarias:**
- Añadir actividades H5P al material del 25-26 (rescatando las del 24-25).
- Crear un cuestionario GIFT actualizado para RA1.
- Unificar las chuletas de Python en una sola (`00_ChuletaPythonBasico.md` y `00_ChuletaLsts_Tupls_Diccs_Sets.md` → fusionar).

---

### 3.2 RA2 — Tratamiento de datos: pandas, Polars, DuckDB (UD2 real)

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `ud2-tratamiento-datos/Sem03/` a `Sem06/` | Muy completo: pandas, cuDF, RAPIDS, visualización (matplotlib, Plotly, Altair, Seaborn, hvPlot), Polars, PyArrow, spaCy, ejercicios seleccionados. Guías de semana. Datasets incluidos. | Voluminoso. Cierta duplicación entre versiones. NLP_old (NLTK) obsoleto. | ✅ **Base principal** |
| **24-25** | `11-TratamientoDeDatos/` + `12-TransformacionDeDatos/` + `06-10-Herramientas/002-Pandas/` + `002-Graficas/` | H5P interactivos de transformación. Pipelines, imbalance, web scraping, grandes datasets. Guía integrada 11-12. | Disperso en 3+ ubicaciones. Sin notebooks modernos (Polars, PyArrow). Sin visualización moderna (Plotly, Altair). | 🟡 **Rescatar H5P y web scraping** |

**Base recomendada:** `ud2-tratamiento-datos/` (25-26)

**Piezas a rescatar del otro curso:**
- `12-TransformacionDeDatos/04-Pandas_Utilidad.h5p`, `01-RegresLineal-TransfObligato.h5p`, `02-TransfSegunGrafico.h5p`, `03-TransfSegunGrafico2.h5p` — actividades H5P sobre transformación de datos.
- `12-TransformacionDeDatos/WebScrapping/` — web scraping (requests, BeautifulSoup, Selenium). El 25-26 no cubre scraping.
- `12-TransformacionDeDatos/Imbalance/` — técnicas de datos desbalanceados. El 25-26 no lo cubre como tema independiente.
- `12-TransformacionDeDatos/LargeDataSets/` — trabajo con datasets grandes (Dask). Complementa Polars/PyArrow.
- `12-TransformacionDeDatos/Pipelines/` — pipelines de scikit-learn. Útil como puente a UD3.
- `12-TransformacionDeDatos/11-12_CreacionProcesamientoTransformacion.md` — guía integrada que unifica tratamiento+transformación.
- `06-10-Herramientas/002-Graficas/` — notebooks de matplotlib/seaborn (si aportan algo no cubierto en Sem04).

**Material a archivar o descartar:**
- `ud2-tratamiento-datos/Sem05/NLP_old/` — notebooks NLTK obsoletos. El 25-26 usa spaCy en Sem06.
- `06-10-Herramientas/002-Pandas/` y `001-NumPy/` — contenido ya integrado en las UDs correspondientes del 25-26.
- `ud2-tratamiento-datos/UD2_Semanas_5_6_7_Notebooks/` — versión integrada que solapa con Sem05+Sem06. Archivar si se confirma duplicación.
- `11-TratamientoDeDatos/S11-Trat-Datos.zip` — ZIP de contenido ya extraído. Eliminar.

**Huecos o mejoras necesarias:**
- Crear H5P adicionales para las nuevas herramientas (Polars, DuckDB, PyArrow) — rescatar el enfoque del 24-25 pero actualizado.
- Unificar `UD2_Semanas_5_6_7_Notebooks/` con Sem05+Sem06 o eliminar la versión integrada.
- Mover NLP_old a archivo histórico con nota de que fue reemplazado por spaCy.

---

### 3.3 RA2 — Machine Learning clásico (UD3 real)

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD3/Sem07/` a `Sem10_a/` + `Recordatorio/` | Muy completo: scikit-learn, cuML, PyCaret, RAPIDS. Capstone de películas con rúbrica y defensa oral. Feature stores (Hopsworks). Lab1/Lab2/Lab3 para creación de datasets. Tarea Bank Marketing con GIFT. | Sem08 parece duplicar contenido de Sem07. Lab3 es esqueleto. | ✅ **Base principal** |
| **24-25** | `BibliotecasIA/` + `06-10-Herramientas/003-Scikit_Learn/` + `005-AutoML/` + `S09-BibliotecasIA/` | Apuntes org/pdf de calidad. Caso práctico de bibliotecas IA. AutoML. | Muy disperso (4 ubicaciones). Sin capstone integrado. Sin feature stores. Sin GPU (cuML/RAPIDS) salvo en `003-RAPIDS/`. | 🟡 **Rescatar solo si aporta algo nuevo** |

**Base recomendada:** `UD3/` (25-26)

**Piezas a rescatar del otro curso:**
- `06-10-Herramientas/005-AutoML/` — material sobre AutoML que complementa PyCaret.
- `13-EvaluacionDeResultados/003-Calibracion.org` + `.pdf` — calibración de modelos. El 25-26 no lo cubre como tema independiente.
- `13-EvaluacionDeResultados/004-ConformalPrediction.org` + `.pdf` — predicción conforme. Contenido avanzado de gran valor.
- `13-EvaluacionDeResultados/evalResulta.ipynb` — notebook de evaluación de resultados.
- `06-10-Herramientas/004-Poetry_uv/` — gestión de proyectos con Poetry+uv. El 25-26 lo usa en Lab1 pero sin tutorial dedicado.

**Material a archivar o descartar:**
- `UD3/Sem08/Tarea/` — tarea Bank Marketing duplicada de Sem07/Tarea. Verificar y archivar una.
- `BibliotecasIA/PIA_S09.zip` y `PIA_S09 Ejemplos Codigo.zip` — contenido no verificado.
- `06-10-Herramientas/003-poetry/` — superado por `004-Poetry_uv/`.
- `06-10-Herramientas/003-Scikit_Learn/` — contenido ya cubierto en UD3 del 25-26.
- `14-ModeladoRedesNeuronales/FicheroMarkDown.md` y `SiguientesParetes_ANN.txt` — material incompleto/informal. Archivar.

**Huecos o mejoras necesarias:**
- Integrar calibración y conformal prediction como temas avanzados dentro de UD3 o como apéndice.
- Desarrollar Lab3 (dataset propio) para que tenga el mismo nivel que Lab1 y Lab2.
- Crear enlace explícito entre feature stores (Hopsworks) y MLOps (UD5).

---

### 3.4 RA2 — Deep Learning y frameworks (UD4 real)

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD4/01-fundamentos/` a `04-modelado-avanzado/` | Incluye fundamentos DL, frameworks, laboratorios, NLP, visión básica. README.md como índice. | **VERTEDERO**: 34,469 archivos mezclando material docente con entregas y correcciones. Difícil evaluar calidad real. Numeración de UD incorrecta (debería ser UD4 si se reorganiza). | ✅ **Base, pero requiere limpieza profunda** |
| **24-25** | `14-ModeladoRedesNeuronales/` + `15-ModeladoAvanzadoDeRedesNeuronales/` (excepto Vision/ y NLP/) | Apuntes org/pdf bien estructurados. TensorFlow Playground como recurso visual. Variedad de casos: Housing, Boston Housing, UsedCars. Ejercicios de clasificación. NLP (Keras) y visión como temas separados. | Sin notebooks con tests. Documentación incompleta (FicheroMarkDown.md es esqueleto). Sin estructura de semana/guias. | 🟡 **Rescatar TF Playground y apuntes org** |

**Base recomendada:** `UD4/` (25-26) tras limpieza urgente del vertedero de `UD4/tareas/`.

**Piezas a rescatar del otro curso:**
- `15-ModeladoAvanzadoDeRedesNeuronales/TensorFlowPlayGround.org` + `.pdf` — recurso visual excelente para explicar arquitecturas DL.
- `15-ModeladoAvanzadoDeRedesNeuronales/UsedCars/` — caso alternativo de regresión (coches usados). Bueno para variedad respecto a housing.
- `15-ModeladoAvanzadoDeRedesNeuronales/001-Keras-NLP.md` — apunte de Keras para NLP. Útil si se mantiene NLP en UD4.
- `14-ModeladoRedesNeuronales/CuestionarioPercptMultiCapaYBackProp.org` — cuestionario sobre perceptrón multicapa.

**Material a archivar o descartar:**
- **TODO el contenido de `UD4/tareas/`** (34,000+ archivos) — separar a `03-entregas/` y `04-correccion/`. No debe mezclarse con material docente.
- `15-ModeladoAvanzadoDeRedesNeuronales/Housing/` o `BostonHousing/` — valorar si ambos son necesarios. Recomendación: mantener BostonHousing (canónico), archivar Housing.
- `15-ModeladoAvanzadoDeRedesNeuronales/SAA/` — material del módulo SBD/SAA. Mover a su árbol correspondiente.
- `14-ModeladoRedesNeuronales/FicheroMarkDown.md` — esqueleto incompleto.

**Huecos o mejoras necesarias:**
- **URGENTE**: Separar `UD4/tareas/` en sus componentes: entregas, correcciones y material docente.
- Definir qué parte de `UD4/04-modelado-avanzado/` pasa a UD8 (visión) y qué se queda en UD4.
- Crear guías de semana para UD4 (como tienen UD1, UD2, UD8).
- Añadir notebooks con tests (como en UD1/UD2/UD8).

---

### 3.5 RA2 — Visión artificial (UD8 real)

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD8/Sem22/` (U-Net, Mask R-CNN), `Sem23/` (YOLOv8, SORT), `Sem24/` (LIME, SHAP, Grad-CAM) | Compacto, muy enfocado, con notebooks base+solución+test. Guías de semana. Incluye XAI (explicabilidad). | Solo 3 semanas. Sin NLP en visión (solo LIME texto). | ✅ **Base principal** |
| **24-25** | `15-ModeladoAvanzadoDeRedesNeuronales/Vision/` + `NLP/` | Visión con TensorFlow/Keras/OpenCV. NLP con Keras+NLTK. | Sin segmentación, detección de objetos, tracking, YOLO. Sin XAI. Sin guías de semana. Tecnologías más antiguas. | 🟡 **Rescatar apuntes NLP si se mantiene en UD8** |

**Base recomendada:** `UD8/` (25-26)

**Piezas a rescatar del otro curso:**
- `15-ModeladoAvanzadoDeRedesNeuronales/NLP/` — si se decide que NLP sea parte de la unidad de visión/herramientas avanzadas.
- `15-ModeladoAvanzadoDeRedesNeuronales/001-Keras-NLP.md` — apunte de Keras para NLP.

**Material a archivar o descartar:**
- Material NLP antiguo de `ud2-tratamiento-datos/Sem05/NLP_old/` (NLTK).
- Visión con TensorFlow/Keras si está duplicado o superado por PyTorch en UD8.

**Huecos o mejoras necesarias:**
- Decidir si NLP se integra en UD8 (visión + NLP) o en UD4 (deep learning general).
- Añadir ejercicios de NLP con transformers (Hugging Face) si no existen.
- El material de XAI (LIME, SHAP, Grad-CAM) es excelente y único en el curso. Mantener y posiblemente ampliar.

---

### 3.6 RA2 — GPU computing, JAX, avanzado (UD9 real)

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD9/Sem26/` (RAPIDS, JAX, benchmarks), `Sem27/` (serving), `Sem28-30/` (consolidación) | JAX, RAPIDS, benchmarks GPU. Serving avanzado. | Mezcla GPU computing con serving/orquestación. Sem25 (neurosimbolica) no impartido. Sem25_old contenido ya cubierto en UD2. | ✅ **Base, pero requiere reestructuración** |
| **24-25** | `06-10-Herramientas/003-RAPIDS/` + `15-B-ReinforcementLearning/` | RL (Snake RL, Q-learning, DQN, CartPole) como unidad optativa completa. RAPIDS. | Sin JAX. Sin benchmarks GPU. RL es optativo/no impartido en 25-26. | 🟡 **Rescatar RL como optativo** |

**Base recomendada:** `UD9/` (25-26) para GPU computing y JAX.

**Piezas a rescatar del otro curso:**
- `15-B-ReinforcementLearning/` — material completo de RL (Snake RL, Q-learning, DQN, CartPole). Excelente como unidad optativa o taller avanzado.
- `06-10-Herramientas/003-RAPIDS/` — si aporta algo no cubierto en UD9/Sem26.

**Material a archivar o descartar:**
- `UD9/Sem25/` (IA Neurosimbólica) — no impartido. Decidir archivo o eliminación.
- `UD9/Sem25_old/` — contenido ya cubierto en UD2 (Polars, cuDF comparativas).
- `15-B-ReinforcementLearning/snake_rl_*.zip` — múltiples versiones. Conservar solo la definitiva.
- `06-10-Herramientas/003-poetry/` — superado por `004-Poetry_uv/`.

**Huecos o mejoras necesarias:**
- Decidir si UD9 se enfoca solo a GPU/JAX (separando serving a UD6) o se mantiene mixta.
- Separar Sem27 (serving) a UD6 donde encaja mejor.
- Añadir ejercicios prácticos de JAX que no sean solo benchmarks.

---

### 3.7 RA2, RA3 — Infraestructura cloud, MLOps (UD5 real)

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD5/Documentacion/`, `Demos/`, `Tareas/`, `cuestionarios*.gift` | 14 documentos muy completos y actuales. Demos de RAG, Hopsworks, fraude. Cuestionarios GIFT. Tarea evaluable con rúbrica. | Cloud y MLOps en la misma unidad. Dependencia de servicios externos (Hopsworks, Ollama). ZIPs sin catalogar. | ✅ **Base principal** |
| **24-25** | `05-ComputaNube/C_Nube1/`, `C_Nube2/`, `AWS/` | AWS práctico con scripts y tareas. Enfoque más limitado pero más reproducible. | Solo AWS. Sin MLOps, feature stores, RAG, Ollama. Tecnológicamente más limitado. | 🟡 **Rescatar scripts AWS como alternativa on-premise** |

**Base recomendada:** `UD5/` (25-26)

**Piezas a rescatar del otro curso:**
- `05-ComputaNube/scriptAWS.sh` y `esqueletoAWS.py` — scripts AWS prácticos como alternativa cuando no se puedan usar otras plataformas cloud.
- `05-ComputaNube/01-AWS-Tarea_01.org` + `.pdf` — enunciado de tarea AWS. Útil como actividad alternativa.

**Material a archivar o descartar:**
- `UD5/herramientasCLoudPIA.zip` — pendiente de revisión. Descomprimir y catalogar.
- `UD5/hopsworks/` — revisar contenido. Si es material de prueba, archivar.
- `UD5/modelos-gpt-5.4.md` — contenido personal/docente. Archivar si no es material de clase.

**Huecos o mejoras necesarias:**
- Crear un tutorial de MLOps end-to-end que conecte UD3 (modelos) → UD5 (cloud) → UD6 (serving).
- Descomprimir y catalogar los ZIPs pendientes.
- Evaluar dependencia de servicios cloud gratuitos vs. alternativas locales (Ollama, MLflow local).

---

### 3.8 RA2, RA3 — LLMs, agentes, orquestación, interfaces (UD6 real)

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD6/Documentación/`, `Ejemplos Básicos/`, `Ejemplos más avanzados/`, `cuestionarios*.gift` | Stack moderno: LangChain, LangGraph, Ollama, FastAPI, MLflow, LlamaIndex, Gradio, DSPy. Notebooks progresivos (básico → avanzado). Cuestionarios GIFT. | Dependencia de APIs LLM externas. Material que puede quedar obsoleto rápidamente. | ✅ **Base principal** |
| **24-25** | `06-10-Herramientas/006-HerramientasGraficas/`, `007-Gradio/`, `008-MCP/` | Gradio, Streamlit, MCP. | Muy básico. Sin LangChain, DSPy, MLflow. MCP sin evaluar pedagógicamente. | 🟡 **Rescatar solo MCP si se considera útil** |

**Base recomendada:** `UD6/` (25-26)

**Piezas a rescatar del otro curso:**
- `06-10-Herramientas/008-MCP/` — MCP (Model Context Protocol). Material muy reciente. Evaluar si se integra como tema de frontera.
- `06-10-Herramientas/006-HerramientasGraficas/` — si hay contenido de Streamlit no cubierto en UD6.

**Material a archivar o descartar:**
- `06-10-Herramientas/007-Gradio/` — contenido ya cubierto en UD6 (Ejemplos Básicos incluye Gradio).
- `06-10-Herramientas/006-HerramientasGraficas/` — si está duplicado con UD6.

**Huecos o mejoras necesarias:**
- Crear una guía de costos/alternativas para APIs LLM (OpenAI vs Ollama local).
- Evaluar si LangChain sigue siendo relevante o si la tendencia va hacia enfoques más ligeros (DSPy, prompts directos).
- El cuestionario GIFT de UD6 (`cuestionario_1_interfaces_api_serving.gift`) está bien, crear más.

---

### 3.9 RA3, RA4 — Convergencia tecnológica, modelos de negocio (UD7)

**⚠️ ATENCIÓN: Esta es la unidad más problemática según la nota del profesor.**

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD7/ConvergenciaTecnologica/` (6 PDFs + checklist + resumen) | 6 presentaciones PDF completas y bien maquetadas. Checklist y resumen. | **NO es material docente adecuado**: son PDFs de presentación, no material pedagógico. Blockchain incluido (no relevante). Enfoque de negocio tradicional, no orientado a herramientas IA. | ❌ **No usar como base. Crear material nuevo.** |
| **24-25** | `17-IntroConvergenciaTecnológica/`, `18-SistemaConvergenciaTecnologica/`, `19-CasoEstudioConvergenciaBlockChain/`, `20-Seguridad.../` | Muy poco. Docker Compose. Tarea automatización. | **Pésimo** (en palabras del profesor). Incompleto. Blockchain dudoso. 20-Seguridad vacío. Un único docker-compose.yaml. | ❌ **No rescatar** |

**Base recomendada:** **CREAR MATERIAL NUEVO DESDE CERO**

La nota del profesor es inequívoca:
- «El material existente de RA3/RA4 es pésimo»
- «La parte de empresas/modelos de negocio hay que orientarlos a las herramientas de programación de IA»
- «Blockchain no lo veo para nada en todo esto»

**Piezas a rescatar (muy limitado):**
- `01-tarea_presentacion_convergencia_IA.md` (raíz 25-26) — enunciado de tarea sobre convergencia. Puede servir como base para la actividad evaluable.
- `entrega_y_rubrica_presentacion_convergencia_IA.md` — rúbrica para la tarea de convergencia.
- `UD7/resumenes_S19_a_S24.md` — resumen temático que puede servir como índice para crear el nuevo material.

**Material a archivar:**
- `UD7/ConvergenciaTecnologica/` — completo. Conservar como referencia histórica pero NO como material docente base.
- `UD7/ConvergenciaTecnologica/S19_Blockchain.pdf` — archivar específicamente por ser blockchain, no relevante.
- `17-IntroConvergenciaTecnológica/` (24-25) — material pobre. Archivar.
- `18-SistemaConvergenciaTecnologica/` (24-25) — archivar.
- `19-CasoEstudioConvergenciaBlockChain/` (24-25) — archivar o eliminar (blockchain no relevante).
- `20-SeguridadEnConvergenciaTecnologica/` (24-25) — carpeta vacía. Eliminar.

**Huecos o mejoras necesarias (CREAR DESDE CERO):**
1. **Reenfocar RA3** (Convergencia tecnológica) hacia:
   - Herramientas de IA que unifican procesos (MLflow, LangChain, Hugging Face, etc.)
   - Conexión entre tecnologías: APIs, microservicios, RAG, MCP
   - Evaluación práctica de herramientas de IA, no teoría de negocio
   
2. **Reenfocar RA4** (Modelos de automatización) hacia:
   - Automatización con herramientas de IA: pipelines de datos, CI/CD para ML, MLOps
   - Modelos de despliegue: edge vs cloud, serverless, contenedores
   - Evaluación de herramientas de IA para automatización empresarial
   - Estrategias de adopción de IA en empresas desde la perspectiva técnica

3. Formato recomendado: Notebooks + guías prácticas con herramientas reales (MLflow, Airflow, LangChain, Hugging Face), no PDFs de presentación.

---

### 3.10 RA2 — Proyecto integrado

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD_Proyecto/proyecto.md`, `evaluacion.md`, `faq.md` | Bien definido. FAQ operativo. Criterios de evaluación. | Esqueleto. Breve. | ✅ **Base, pero desarrollar** |
| **24-25** | `Proyecto/Proyecto_PIA-SBD.md` + `.pdf` | Proyecto conjunto PIA-SBD. | Límites difusos entre módulos. ProyectoPipelineForecastCripto.txt es esqueleto. | 🟡 **Rescatar idea de proyecto conjunto** |

**Base recomendada:** `UD_Proyecto/` (25-26)

**Piezas a rescatar del otro curso:**
- Idea de proyecto conjunto con SBD (si aplica en 26-27).
- Metodología de defensa oral (de UD3 capstone películas) aplicable al proyecto.

**Material a archivar:**
- `Proyecto/ProyectoPipelineForecastCripto.txt` — esqueleto no desarrollado.
- `Proyecto/Proyecto_PIA-SBD.md` — archivar si el proyecto conjunto no sigue en pie.

**Huecos o mejoras necesarias:**
- Desarrollar el proyecto con más detalle (semanas, hitos, entregas parciales).
- Definir claramente el alcance individual vs. grupal.
- Conectar el proyecto con los contenidos de UD5 (cloud) y UD6 (serving).

---

### 3.11 RA2 — Taller de series temporales

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
|---|---|---|---|---|
| **25-26** | `UD_Talleres/SeriesTemporales/` | 11 notebooks muy completos: intro, datos, análisis, baselines, regresión, FE, DL, TCN, transformers, proyecto, despliegue. FAQ, seguimiento, requirements.txt. | Solo en 25-26. No existía como unidad independiente en 24-25. | ✅ **Mantener como taller** |
| **24-25** | No existe como unidad independiente. | — | — | — |

**Decisión:** Conservar íntegro. El taller de series temporales es material de alta calidad que no tiene equivalente en 24-25.

---

## 4. Propuesta de unidades ideales

Basada en el análisis comparativo y la nota del profesor.

| Unidad ideal | RA | Base principal | Piezas complementarias | Material a crear/actualizar | Riesgo |
|---|---|---|---|---|---|
| **U1: Fundamentos de programación Python** | RA1 | `ud1-fundamentos_programacion_IA/` (25-26) | H5P de 24-25, GIFT de 24-25 | Fusionar chuletas, añadir H5P | Bajo |
| **U2: Tratamiento y transformación de datos** | RA1, RA2 | `ud2-tratamiento-datos/` (25-26) | H5P de transformación (24-25), Web Scraping (24-25), Imbalance (24-25) | Crear H5P para Polars/DuckDB | Bajo |
| **U3: Machine Learning clásico** | RA2 | `UD3/` (25-26) | Calibración + Conformal Prediction (24-25), Poetry+uv (24-25) | Desarrollar Lab3, integrar calibración | Bajo |
| **U4: Deep Learning y frameworks** | RA2 | `UD4/` (25-26) tras limpieza | TF Playground (24-25), UsedCars (24-25), cuestionario perceptrón (24-25) | **LIMPIEZA URGENTE** de UD4/tareas/, crear guías de semana | **Alto** (vertedero) |
| **U5: Infraestructura cloud y MLOps** | RA2, RA3 | `UD5/` (25-26) | Scripts AWS (24-25) | Crear tutorial MLOps end-to-end, catalogar ZIPs | Medio |
| **U6: LLMs, agentes e interfaces** | RA2, RA3 | `UD6/` (25-26) | MCP (24-25, si procede) | Guía de costos APIs alternativas | Medio (obsolescencia) |
| **U7: Convergencia tecnológica y herramientas IA** | RA3, RA4 | **CREAR DESDE CERO** | Enunciado tarea convergencia (25-26), rúbrica | **CREAR**: material docente completo orientado a herramientas IA, no a teoría de negocio | **Alto** (parte más débil) |
| **U8: Visión artificial y XAI** | RA2 | `UD8/` (25-26) | NLP de 24-25 (si aplica) | Decidir si NLP va aquí o en U4 | Bajo |
| **U9: GPU computing y RL** | RA2 | `UD9/` (25-26) + `15-B-ReinforcementLearning/` (24-25) | — | Separar serving a U6, enfocar GPU/JAX + RL optativo | Medio |
| **Taller: Series temporales** | RA2 | `UD_Talleres/SeriesTemporales/` | — | Sin cambios | Bajo |
| **Proyecto integrado** | RA2 | `UD_Proyecto/` (25-26) | Defensa oral de capstone (25-26) | Desarrollar con más detalle, conectar con U5/U6 | Medio |

---

## 5. Recomendaciones para el prompt de reorganización

### Estructura final recomendada

Se recomienda la **Opción C** del inventario: **abandonar la numeración UD1–UD9** y usar nombres descriptivos. Esto elimina la confianza actual entre planificación oficial y estructura real de directorios.

```
PIA/
├── 00-planificacion/
├── 01-docentes/
│   ├── 01-fundamentos-python/         ← RA1 (antigua ud1-fundamentos_programacion_IA)
│   ├── 02-tratamiento-datos/          ← RA1, RA2 (antigua ud2-tratamiento-datos)
│   ├── 03-machine-learning/           ← RA2 (antigua UD3)
│   ├── 04-deep-learning/              ← RA2 (antigua UD4, tras limpieza)
│   ├── 05-cloud-mlops/               ← RA2, RA3 (antigua UD5)
│   ├── 06-llm-agentes/               ← RA2, RA3 (antigua UD6)
│   ├── 07-convergencia-herramientas/  ← RA3, RA4 (CREAR NUEVO)
│   ├── 08-vision-xai/                ← RA2 (antigua UD8)
│   ├── 09-gpu-avanzado/              ← RA2 (antigua UD9)
│   ├── taller-series-temporales/      ← RA2
│   └── proyecto-integrado/           ← RA2
├── 02-evaluacion/
│   ├── rubricas/
│   ├── examenes/
│   └── prompts-correccion/
├── 03-entregas/                       ← (solo ZIPs, no visible en catálogo docente)
├── 04-correccion/                     ← (CSVs, informes, no visible)
├── 05-archivo-historico/              ← Cursos anteriores, versiones antiguas
├── 06-recursos-transversales/
│   ├── entornos-virtuales/
│   ├── libros/
│   ├── chuletas/
│   └── guia-alumno.pdf
└── RA_CE.md
```

### Material que debe copiarse como ruta principal

| Origen | Destino en la nueva estructura | Razón |
|---|---|---|
| `ud1-fundamentos_programacion_IA/` | `01-docentes/01-fundamentos-python/` | Material más completo y mejor secuenciado para RA1 |
| `ud2-tratamiento-datos/` | `01-docentes/02-tratamiento-datos/` | Cobertura amplia y actual (pandas, Polars, DuckDB, visualización moderna) |
| `UD3/` | `01-docentes/03-machine-learning/` | Capstone, feature stores, GPU incluidos |
| `UD4/` (solo material docente) | `01-docentes/04-deep-learning/` | Único curso que tiene deep learning estructurado |
| `UD5/` | `01-docentes/05-cloud-mlops/` | Documentación moderna de cloud/MLOps |
| `UD6/` | `01-docentes/06-llm-agentes/` | Stack LLM moderno y completo |
| `UD8/` | `01-docentes/08-vision-xai/` | Visión compacta con XAI, bien secuenciada |
| `UD9/` (GPU/JAX) | `01-docentes/09-gpu-avanzado/` | JAX y RAPIDS. Separar serving a U6. |
| `UD_Talleres/SeriesTemporales/` | `01-docentes/taller-series-temporales/` | Taller completo de alta calidad |
| `UD_Proyecto/` | `01-docentes/proyecto-integrado/` | Esqueleto a desarrollar |

### Material que debe ir a ampliación/archivo

| Origen | Destino | Razón |
|---|---|---|
| `UD3_old/` a `UD7_old/` | `05-archivo-historico/` | Versiones antiguas de unidades |
| `UD9/Sem25/` (Neurosimbólica) | `05-archivo-historico/` | No impartido |
| `UD9/Sem25_old/` | `05-archivo-historico/` | Contenido ya cubierto en UD2 |
| `01-04-Programacion/Mojo/` | `05-archivo-historico/` | Lenguaje experimental |
| `19-CasoEstudioConvergenciaBlockChain/` | `05-archivo-historico/` | No relevante |
| `ConvergenciaTecnologica/` (raíz) | `05-archivo-historico/` | Duplicado de UD7 (si se confirma) |
| `PIA_S22/S23/S24 Codigo Fuente.zip` | `05-archivo-historico/` | Código de cursos anteriores |
| `Pack_IA_Convergencia*.zip` | `05-archivo-historico/` una vez revisado | Contenido no verificado |
| `Herramientas para IA-*.zip` | Revisar antes de archivar | Contenido no verificado |
| `Correcciones/` | `04-correccion/` | Artefactos de corrección |
| `Alumnos/` | Excluir del catálogo docente | Repositorios de alumnado |

### Material docente interno (99-profesor)

Se recomienda crear un directorio `99-profesor/` o incluir en `00-planificacion/` para material de uso exclusivo del docente:

- `openAI-API-Key.txt` y similares → **ELIMINAR** del repositorio (riesgo de seguridad)
- `modelos-gpt-5.4.md` → notas personales del profesor
- `prompt_inventario_material_modulo.md` → prompts de trabajo (ya está en 00-planificación)
- `charlaEstrategiaLLM.txt` → notas personales
- Notas de calibración (`ConformalCalibration.md`) si se determina que no es material de clase

---

## 6. Pendientes antes de reorganizar

### Alta prioridad

- [ ] **Limpiar UD4/tareas/**: extraer material docente, mover entregas a `03-entregas/` y correcciones a `04-correccion/`. Es la tarea más urgente y voluminosa.
- [ ] **Eliminar ficheros sensibles** del repositorio: `openAI-API-Key.txt`, `PageIndez-ApiKey.txt`, `UD5/hopsWorks-API-KEY.txt`, `api-key_TheMovieDB.txt`. Rotar las claves expuestas.
- [ ] **Crear material nuevo para RA3/RA4** (U7: Convergencia tecnológica y herramientas IA). Según la nota del profesor, no hay material rescatable de ningún curso. Hay que diseñar desde cero.

### Media prioridad

- [ ] **Descomprimir y catalogar ZIPs pendientes**: `Herramientas para IA-*.zip` (UD6), `herramientasCLoudPIA.zip` (UD5), `herramientasPIA.zip` (UD9), `Pack_IA_Convergencia*.zip`.
- [ ] **Verificar duplicados**: `ConvergenciaTecnologica/` raíz vs `UD7/ConvergenciaTecnologica/`, `UD3/Sem07/Tarea/` vs `UD3/Sem08/Tarea/`, `15-ModeladoAvanzado.../Housing/` vs `BostonHousing/`.
- [ ] **Decidir numeración final**: ¿Opción C (nombres descriptivos) o mantener UD1-UD9 actualizando la planificación oficial?
- [ ] **Separar normativa de otros módulos**: material de SAA/SBD mezclado en el árbol de PIA.
- [ ] **Integrar H5P del 24-25**: rescatar actividades interactivas que el 25-26 perdió.
- [ ] **Integrar 13-EvaluacionDeResultados/** (calibración, conformal prediction) dentro de la unidad de ML (U3).

### Baja prioridad

- [ ] **Desarrollar Lab3** (dataset propio) en UD3 para que iguale el nivel de Lab1 y Lab2.
- [ ] **Desarrollar proyecto integrado** con más detalle y conexión a U5/U6.
- [ ] **Evaluar pertinencia de MCP** (Model Context Protocol) para incluirlo en U6.
- [ ] **Evaluar pertinencia de KNIME**: el contenido básico oficial lo menciona pero no se usa. Archivar o eliminar.
- [ ] **Unificar soluciones**: elegir formato canónico (recomendado: `notebook_SOLUCIONES.ipynb` con tests inline).
- [ ] **Eliminar formatos duplicados**: decidir formato fuente (`.md` o `.ipynb`) y archivar derivados (`.html`, `.pdf`).
- [ ] **Actualizar documentación oficial**: `PIA_Unidades_Didacticas.md` y `PIA_Mapeo_RA_CE_Semanas.md` deben reflejar la nueva estructura.
- [ ] **Resolver carpeta raíz suelta `nn.ipynb`**: determinar su origen y unidad de pertenencia.
