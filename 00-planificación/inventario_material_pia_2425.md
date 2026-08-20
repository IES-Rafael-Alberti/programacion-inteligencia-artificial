# Inventario del módulo: Programación de Inteligencia Artificial (curso 24-25)

> **Nota sobre las rutas:** todas las rutas son relativas a la raíz del módulo, que en el curso 24-25
> estaba en `/home/jmsa/IESRafaelAlberti24_25/Modulos/PIA/`. Algunas de estas rutas ya no existen
> en el árbol actual, que fue reorganizado en una estructura por UDs (ud1-fundamentos_programacion_IA,
> ud2-tratamiento-datos, UD3…UD9, UD_Proyecto, UD_Talleres). Este inventario documenta el estado del
> curso 24-25 para que la reorganización hacia 25-26 parta de datos fiables.

---

## 1. Resumen ejecutivo

### Qué tipo de materiales predominan

- **Apuntes y presentaciones** en múltiples formatos (Org-mode, PDF, LaTeX, Markdown). El profesor usa
  Org-mode como fuente principal y exporta a PDF y LaTeX de forma sistemática.
- **Notebooks Jupyter** como soporte práctico, especialmente en las unidades de programación (UD1),
  tratamiento de datos (UD2) y modelos (UD4/UD8).
- **Actividades interactivas H5P** integradas en Moodle, sobre todo para UD1 y UD2.
- **Material de herramientas**: tutoriales sueltos sobre NumPy, pandas, scikit-learn, Gradio, Poetry,
  RAPIDS, AutoML, etc., agrupados en una carpeta comodín (`06-10-Herramientas/`).
- **Planificaciones**: múltiples versiones de planificación temporal del curso (V1 a V5 + versiones
  de 16/28/32 semanas), lo que sugiere un proceso iterativo de ajuste de calendario.
- **Documentación normativa**: PDFs oficiales del módulo y de Sistemas de Aprendizaje Automático
  incrustados entre los materiales (no separados como referencia).

### Partes bien cubiertas

- **UD1 — Fundamentos de programación** (RA1): completa, con apuntes, ejercicios variados, H5Ps,
  notebooks, cuestionarios GIFT. Es la unidad más robusta.
- **UD2 — Tratamiento y transformación de datos**: cubierta desde dos ángulos complementarios
  (tratamiento y transformación), con casos prácticos, autoevaluaciones y ejercicios H5P.
- **UD4/UD8 — Redes neuronales básicas y avanzadas**: material abundante, incluyendo varios casos
  de regresión (housing, Boston housing, coches usados), ejercicios de clasificación, visión
  artificial y NLP.
- **UD5 — Cloud computing**: Bloque pequeño pero bien definido con apuntes, tareas y scripts AWS.
- **Uso de herramientas cloud y GPU**: RAPIDS, AWS, Poetry+uv — el módulo muestra conciencia de
  la infraestructura moderna.

### Partes dispersas, duplicadas o antiguas

- **Carpeta `06-10-Herramientas/`**: es un cajón de sastre que agrupa tutoriales de herramientas
  dispersas entre UD1 y UD9. La cobertura es fragmentaria y sin una progresión clara.
- **Planificaciones**: 7+ versiones del mismo plan sin un «fuente de verdad» identificado. Riesgo
  de que el docente use una versión y el inventario refleje otra.
- **ZIPs huérfanos**: múltiples archivos ZIP sin extraer ni documentar (ej. `PIA_S09.zip`,
  `PIA_S15 Codigo Fuente.zip`, `snake_rl_*.zip`) cuyo contenido duplica o complementa carpetas ya
  extraídas. Generan ruido en el inventario.
- **Duplicación de problemas de regresión**: `Housing/` y `BostonHousing/` en la misma unidad son
  esencialmente el mismo caso práctico con distinto dataset. Revisar si ambos se necesitan.
- **Blockchain**: un solo archivo `BlockChain.org` con dudas fundadas sobre su pertinencia en el módulo.
- **Seguridad en convergencia tecnológica**: carpeta vacía (`20-SeguridadEnConvergenciaTecnologica/`).
- **Mojo**: carpeta con material sobre un lenguaje experimental. Su continuidad debe decidirse.

### Elementos que conviene revisar antes del próximo curso

| Elemento | Riesgo | Acción sugerida |
|----------|--------|-----------------|
| Mojo/ | Lenguaje experimental, no consolidado | Decidir si se mantiene o se archiva |
| MCP (Model Context Protocol) | Material muy reciente, no evaluado pedagógicamente | Revisar pertinencia curricular |
| Blockchain (19-CasoEstudio…) | Contenido dudoso para PIA | Archivar o eliminar |
| 20-Seguridad…/ | Carpeta vacía | Decidir si se puebla o se elimina |
| Múltiples ZIPs snake_rl_* | Versiones duplicadas sin versión definitiva | Limpiar, conservar solo la versión final |
| 16-HerramientaGeneracionCodigo_IA/ | Contenido sin contexto claro (¿proyecto alumno?) | Verificar autoría y propósito |

---

## 2. Catálogo de materiales docentes

### 2.1 UD1 — Fundamentos de programación (RA1)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `01-04-Programacion/Tema00/` | Tema 0: introducción, entorno | varios | UD1 | Setup del curso, conceptos básicos de programación y entorno | Python | Completo | Arranque del módulo. Contiene presentación, guías de instalación, configuración del entorno. |
| `01-04-Programacion/Tema01/` | Tema 1: fundamentos Python | varios | UD1 | Variables, tipos de datos, control de flujo, funciones | Python | Completo | Núcleo del RA1. Bien estructurado. |
| `01-04-Programacion/Tema02/` | Tema 2: NumPy, pandas, matplotlib | varios | UD1 | Librerías científicas, manipulación de datos | NumPy, pandas, matplotlib | Completo | Cobertura amplia. Algunos contenidos solapan con `06-10-Herramientas/001-NumPy/` y `002-Pandas/`. |
| `01-04-Programacion/Tema04/` | Tema 4: estructuras de datos avanzadas | varios | UD1 | Listas, diccionarios, conjuntos, comprensión de listas | Python | Completo | Sin observaciones destacables. |
| `01-04-Programacion/Ejercicios/` | Ejercicios RA1 | ipynb / h5p / org | UD1 | Colección de ejercicios variados del RA1 con tests | Python, H5P | Completo | Incluye formato H5P interactivo. Buena variedad de formatos. |
| `01-04-Programacion/Ejer01-RA1.h5p` | Ejercicios RA1 (H5P) | h5p | UD1 | Actividades interactivas H5P para Moodle (×6 ficheros: Ejer01 a Ejer08.4) | H5P | Completo | Formato H5P para Moodle. Se listan 6 ficheros; conviene agruparlos bajo un mismo epígrafe en la reorganización. |
| `01-04-Programacion/01_IntroProgramacionIA.org` | Apunte org-mode | org | UD1 | Introducción a la programación para IA | Emacs Org | Completo | Fuente editable. Sigue el flujo de trabajo Org → LaTeX → PDF del profesor. |
| `01-04-Programacion/Ejercicios-PIA_RA1-S01_02.org` | Ejercicios org | org | UD1 | Ejercicios del RA1, semanas 1-2 | Emacs Org | Completo | |
| `01-04-Programacion/Ejercicios-PIA_RA1-S01_04.gift` | Cuestionario GIFT | gift | UD1 | Cuestionario Moodle del RA1 | Moodle | Completo | Formato GIFT importable directamente a Moodle. |
| `01-04-Programacion/Ejercicios-PIA_RA1-S01_02.pdf` | PDF ejercicios | pdf | UD1 | Versión PDF de los ejercicios de las semanas 1-2 | — | Completo | |
| `01-04-Programacion/Mojo/` | Introducción a Mojo | varios | UD1 | Material sobre Mojo como lenguaje para IA | Mojo | Exploratorio | ⚠️ Lenguaje muy reciente, no consolidado. Decidir si se mantiene para 25-26. |
| `01-04-Programacion/Pandas, Seaborn, Matplotlib-20241002.zip` | ZIP librerías | zip | UD1 | Material empaquetado sobre pandas, seaborn, matplotlib | pandas, seaborn, matplotlib | Complementario | 🔍 Contenido sin verificar. Puede duplicar material ya extraído en Tema02/. |
| `01-04-Programacion/AprendeIA_Python-EjerciciosMaterial_web.zip` | ZIP ejercicios web | zip | UD1 | Ejercicios Python empaquetados | Python | Complementario | 🔍 Contenido sin verificar. Procedencia externa ("AprendeIA"). |
| `01-04-Programacion/PracticarPython1-2-20241002.zip` | ZIP práctica Python 1-2 | zip | UD1 | Práctica Python 1-2 empaquetada | Python | Complementario | 🔍 Contenido sin verificar. Podría ser material complementario o práctica de alumno. |
| `01-04-Programacion/PracticarPython3-4-20241002.zip` | ZIP práctica Python 3-4 | zip | UD1 | Práctica Python 3-4 empaquetada | Python | Complementario | 🔍 Contenido sin verificar. Misma procedencia que el anterior. |

### 2.2 UD2 — Tratamiento y transformación de datos

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `11-TratamientoDeDatos/S11-Trat-Datos/` | Tratamiento de datos | varios | UD2 | Contenido completo de la unidad de tratamiento de datos | pandas, NumPy | Completo | |
| `11-TratamientoDeDatos/caso_practico/` | Caso práctico | varios | UD2 | Caso práctico de tratamiento de datos con pandas | pandas | Completo | |
| `11-TratamientoDeDatos/Autoeval/` | Autoevaluación | varios | UD2 | Tests de autoevaluación de la unidad | — | Completo | |
| `11-TratamientoDeDatos/11-TratamientoDeDatos.md` | Apunte principal | md | UD2 | Documento principal de tratamiento de datos | pandas | Completo | |
| `11-TratamientoDeDatos/TransformacionDatos.md` | Transformación de datos | md | UD2 | Guía de transformación de datos | pandas | Completo | |
| `11-TratamientoDeDatos/11-TratamientoDeDatos-Resumen.org` | Resumen org | org | UD2 | Resumen editable del tema | Emacs Org | Completo | |
| `11-TratamientoDeDatos/11-TratamientoDeDatos-Resumen.pdf` | Resumen PDF | pdf | UD2 | Resumen en PDF del tema | — | Completo | |
| `11-TratamientoDeDatos/11-TratamientoDeDatos-Resumen.tex` | Resumen LaTeX | tex | UD2 | Fuente LaTeX del resumen | LaTeX | Completo | |
| `11-TratamientoDeDatos/movies_dataset.csv` | Dataset películas | csv | UD2 | Dataset de películas para prácticas | — | Completo | |
| `11-TratamientoDeDatos/ia_bd_m3_programacion_de_inteligencia_artificialTratDatos.pdf` | PDF normativa | pdf | UD2 | Documento oficial del módulo PIA (normativa) | — | Referencia | ⚠️ Documento normativo mezclado con material docente. Separar en la reorganización. |
| `11-TratamientoDeDatos/S11-Trat-Datos.zip` | ZIP unidad | zip | UD2 | Material empaquetado de la unidad S11 | — | Complementario | 🔍 Contenido duplicado con la carpeta `S11-Trat-Datos/` ya extraída. Revisar si ambos se necesitan. |
| `12-TransformacionDeDatos/Pipelines/` | Pipelines | varios | UD2 | Pipelines de transformación de datos | scikit-learn, pandas | Completo | |
| `12-TransformacionDeDatos/Imbalance/` | Imbalance | varios | UD2 | Técnicas para datos desbalanceados | imbalanced-learn | Completo | |
| `12-TransformacionDeDatos/LargeDataSets/` | Grandes datasets | varios | UD2 | Trabajo con datasets grandes | pandas, Dask | Completo | |
| `12-TransformacionDeDatos/WebScrapping/` | Web scraping | varios | UD2 | Técnicas de web scraping | requests, BeautifulSoup, Selenium | Completo | |
| `12-TransformacionDeDatos/ejemplo-tutoria/` | Ejemplo tutoría | varios | UD2 | Material de tutoría sobre transformación | pandas | Completo | |
| `12-TransformacionDeDatos/PIA_S12-Caso-Practico/` | Caso práctico S12 | varios | UD2 | Caso práctico de transformación de datos | pandas, scikit-learn | Completo | |
| `12-TransformacionDeDatos/Autoevaluacion/` | Autoevaluación | varios | UD2 | Tests de autoevaluación de transformación | — | Completo | |
| `12-TransformacionDeDatos/11-12_CreacionProcesamientoTransformacion.md` | Guía integrada | md | UD2 | Guía que integra las unidades 11 y 12 (tratamiento + transformación) | pandas | Completo | Buen indicador de que UD11 y UD12 deberían fusionarse en una sola unidad (UD2). |
| `12-TransformacionDeDatos/04-Pandas_Utilidad.h5p` | H5P pandas | h5p | UD2 | Actividad interactiva sobre utilidad de pandas | H5P | Completo | |
| `12-TransformacionDeDatos/01-RegresLineal-TransfObligato.h5p` | H5P regresión | h5p | UD2 | Actividad interactiva sobre regresión lineal y transformación | H5P | Completo | |
| `12-TransformacionDeDatos/02-TransfSegunGrafico.h5p` | H5P transformación | h5p | UD2 | Actividad interactiva: transformación según gráfico | H5P | Completo | |
| `12-TransformacionDeDatos/03-TransfSegunGrafico2.h5p` | H5P transformación II | h5p | UD2 | Actividad interactiva: transformación según gráfico (2) | H5P | Completo | |

### 2.3 UD3 — Bibliotecas de IA y modelado (RA3/RA4)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `BibliotecasIA/BibliotecasModeladoIA.pdf` | Bibliotecas modelado IA | pdf | UD3 | Documento sobre bibliotecas de inteligencia artificial | scikit-learn, TensorFlow | Completo | |
| `BibliotecasIA/BibliotecasModeladoIA.org` | Bibliotecas modelado IA (org) | org | UD3 | Fuente Org-mode editable | Emacs Org | Completo | |
| `BibliotecasIA/BibliotecasModeladoIA.tex` | Bibliotecas modelado IA (tex) | tex | UD3 | Fuente LaTeX | LaTeX | Completo | |
| `BibliotecasIA/caso-practico/` | Caso práctico bibliotecas | varios | UD3 | Caso práctico de bibliotecas IA | scikit-learn | Completo | |
| `BibliotecasIA/PIA_S09.zip` | ZIP bibliotecas | zip | UD3 | Material empaquetado de la semana 9 | — | Complementario | 🔍 Contenido sin verificar. Posible duplicado de `caso-practico/`. |
| `BibliotecasIA/PIA_S09 Ejemplos Codigo.zip` | Código ejemplos | zip | UD3 | Ejemplos de código empaquetados | — | Complementario | 🔍 Contenido sin verificar. |
| `06-10-Herramientas/003-Scikit_Learn/` | Scikit-learn | varios | UD3 | Tutoriales y ejercicios de ML clásico con scikit-learn | scikit-learn | Completo | Contenido solapa parcialmente con `BibliotecasIA/`. Unificar criterio. |
| `06-10-Herramientas/005-AutoML/` | AutoML | varios | UD3 | Automatización de ML | AutoML, PyCaret | Completo | |
| `06-10-Herramientas/S09-BibliotecasIA/` | Bibliotecas IA | varios | UD3 | Librerías de IA: scikit-learn y otras | scikit-learn | Completo | Otra carpeta sobre bibliotecas IA. Misma temática que `BibliotecasIA/`. Riesgo de dispersión. |

### 2.4 UD3/UD4 — Evaluación y validación de resultados

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `13-EvaluacionDeResultados/001-EvaluacionValidacionResultados.org` | Evaluación y validación (org) | org | UD3/4 | Evaluación y validación de modelos | scikit-learn | Completo | |
| `13-EvaluacionDeResultados/001-EvaluacionValidacionResultados.pdf` | Evaluación y validación (pdf) | pdf | UD3/4 | Versión PDF del anterior | — | Completo | |
| `13-EvaluacionDeResultados/003-Calibracion.org` | Calibración de modelos (org) | org | UD3/4 | Calibración de modelos de clasificación | scikit-learn | Completo | |
| `13-EvaluacionDeResultados/003-Calibracion.pdf` | Calibración de modelos (pdf) | pdf | UD3/4 | Versión PDF del anterior | — | Completo | |
| `13-EvaluacionDeResultados/004-ConformalPrediction.org` | Predicción conforme (org) | org | UD3/4 | Predicción conforme (conformal prediction) | — | Completo | Tema avanzado. Valor pedagógico alto. |
| `13-EvaluacionDeResultados/004-ConformalPrediction.pdf` | Predicción conforme (pdf) | pdf | UD3/4 | Versión PDF del anterior | — | Completo | |
| `13-EvaluacionDeResultados/evalResulta.ipynb` | Notebook evaluación | ipynb | UD3/4 | Notebook de evaluación de resultados de modelos | scikit-learn | Completo | |
| `13-EvaluacionDeResultados/ia_bd_m2_sistemas_de_aprendizaje_automatico.pdf` | PDF normativa SAA | pdf | UD3/4 | Documento oficial del módulo Sistemas de Aprendizaje Automático | — | Referencia | ⚠️ Normativa de otro módulo. Separar en la reorganización. |

### 2.5 UD4 — Redes neuronales y deep learning

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `14-ModeladoRedesNeuronales/Documentacion/` | Documentación redes neuronales | varios | UD4 | Documentación sobre redes neuronales | TensorFlow, Keras | Completo | |
| `14-ModeladoRedesNeuronales/data/` | Datos | varios | UD4 | Datasets para prácticas de redes neuronales | — | Completo | |
| `14-ModeladoRedesNeuronales/images/` | Imágenes | varios | UD4 | Imágenes y gráficos de apoyo | — | Complementario | |
| `14-ModeladoRedesNeuronales/FicheroMarkDown.md` | Apunte redes neuronales | md | UD4 | Notas sobre redes neuronales | TensorFlow | Esqueleto | ⚠️ Parece incompleto. Revisar si se va a desarrollar o archivar. |
| `14-ModeladoRedesNeuronales/CuestionarioPercptMultiCapaYBackProp.org` | Cuestionario perceptrón | org | UD4 | Cuestionario sobre perceptrón multicapa y backpropagation | — | Completo | |
| `14-ModeladoRedesNeuronales/SiguientesParetes_ANN.txt` | Notas siguientes pasos | txt | UD4 | Notas informales sobre próximos pasos con ANN | — | Esqueleto | ⚠️ Contenido informal. Nombre de archivo con posible error tipográfico ("Paretes" → "Pasos"/"Partes"). Revisar si contiene información aprovechable. |
| `15-ModeladoAvanzadoDeRedesNeuronales/Housing/` | Housing | varios | UD4 | Problema de regresión de precios de vivienda | TensorFlow, Keras | Completo | ⚠️ Solapa con `BostonHousing/` (misma temática, distinto dataset). Valorar si ambos se necesitan. |
| `15-ModeladoAvanzadoDeRedesNeuronales/BostonHousing/` | Boston Housing | varios | UD4 | Problema de regresión (Boston Housing clásico) | TensorFlow, Keras | Completo | ⚠️ Solapa con `Housing/`. BostonHousing es el dataset canónico. |
| `15-ModeladoAvanzadoDeRedesNeuronales/UsedCars/` | Used Cars | varios | UD4 | Problema de regresión (precio coches usados) | TensorFlow, Keras | Completo | Caso alternativo a los de housing. Bueno para variedad. |
| `15-ModeladoAvanzadoDeRedesNeuronales/EjerciciosClasificacion/` | Ejercicios clasificación | varios | UD4 | Ejercicios de clasificación con redes | TensorFlow, Keras | Completo | |
| `15-ModeladoAvanzadoDeRedesNeuronales/SAA/` | SAA (Sist. Aprendizaje Automático) | varios | UD4 | Material sobre Sistemas de Aprendizaje Automático | scikit-learn | Completo | ⚠️ Material de otro módulo (SAA) mezclado. Separar. |
| `15-ModeladoAvanzadoDeRedesNeuronales/Documentacion/` | Documentación DL | varios | UD4 | Documentación de deep learning avanzado | — | Completo | |
| `15-ModeladoAvanzadoDeRedesNeuronales/001-Keras-NLP.md` | Apunte Keras NLP | md | UD4/8 | Keras para procesamiento de lenguaje natural | Keras, TensorFlow | Completo | |
| `15-ModeladoAvanzadoDeRedesNeuronales/TensorFlowPlayGround.org` | TensorFlow Playground (org) | org | UD4 | Actividad interactiva con TensorFlow Playground | TensorFlow | Completo | Recurso visual para explicar arquitecturas. |
| `15-ModeladoAvanzadoDeRedesNeuronales/TensorFlowPlayGround.pdf` | TensorFlow Playground (pdf) | pdf | UD4 | Versión PDF del anterior | — | Completo | |
| `15-ModeladoAvanzadoDeRedesNeuronales/tf-playground-datasets.ipynb` | Notebook TF Playground | ipynb | UD4 | Datasets para TF Playground | TensorFlow | Completo | |
| `15-ModeladoAvanzadoDeRedesNeuronales/RESUMEN_TRABAJO.md` | Resumen trabajo | md | UD4 | Resumen de trabajo del bloque de modelado avanzado | — | Completo | |
| `15-ModeladoAvanzadoDeRedesNeuronales/Tareas/` | Tareas evaluables | varios | UD4 | Enunciados y materiales de evaluación del bloque | — | Pendiente revisión | ⚠️ Requiere revisión: puede contener mezcla de enunciados docentes y entregas de alumnado. Separar. |
| `15-ModeladoAvanzadoDeRedesNeuronales/PIA_S15 Codigo Fuente.zip` | Código fuente S15 | zip | UD4 | Código fuente empaquetado de la semana 15 | — | Complementario | 🔍 Contenido sin verificar. |

### 2.6 UD8 — Visión artificial y NLP

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `15-ModeladoAvanzadoDeRedesNeuronales/Vision/` | Visión artificial | varios | UD8 | Computer vision con deep learning | TensorFlow, Keras, OpenCV | Completo | |
| `15-ModeladoAvanzadoDeRedesNeuronales/NLP/` | NLP | varios | UD8 | Procesamiento del lenguaje natural | TensorFlow, Keras, NLTK | Completo | |

### 2.7 UD9 — Reinforcement Learning (contenido complementario)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `15-B-ReinforcementLearning/Snake-RL.md` | Apunte RL Snake | md | UD9 | Tutorial de Reinforcement Learning con juego Snake | OpenAI Gym | Completo | |
| `15-B-ReinforcementLearning/Snake-RL.ipynb` | Notebook RL Snake | ipynb | UD9 | Implementación práctica de RL con Snake | OpenAI Gym, PyTorch | Completo | |
| `15-B-ReinforcementLearning/q_table_snake_tutorial.ipynb` | Q-table Snake | ipynb | UD9 | Tutorial de Q-learning con Snake | OpenAI Gym | Completo | |
| `15-B-ReinforcementLearning/dqn_snake_tutorial.ipynb` | DQN Snake | ipynb | UD9 | Tutorial de DQN con Snake | PyTorch, DQN | Completo | |
| `15-B-ReinforcementLearning/Q_Learning_CartPole.ipynb` | Q-learning CartPole | ipynb | UD9 | Q-learning con el entorno CartPole | OpenAI Gym | Completo | |
| `15-B-ReinforcementLearning/DQN_CartPole_PyTorch.ipynb` | DQN CartPole | ipynb | UD9 | DQN con CartPole en PyTorch | PyTorch, DQN | Completo | |
| `15-B-ReinforcementLearning/001-ReinfordementLearning.md` | Introducción a RL | md | UD9 | Apunte: introducción a Reinforcement Learning | — | Completo | |
| `15-B-ReinforcementLearning/comparativa_qtable_dqn_snake.pdf` | Comparativa Q-table vs DQN | pdf | UD9 | Comparativa entre Q-table y DQN en Snake | — | Completo | |
| `15-B-ReinforcementLearning/por_que_funcionan_refuerzos_castigos.pdf` | Por qué funciona RL | pdf | UD9 | Explicación de refuerzos y castigos en RL | — | Completo | |
| `15-B-ReinforcementLearning/snake_rl_*.zip` | Múltiples ZIPs Snake RL | zip | UD9 | Varias versiones empaquetadas del proyecto Snake RL | — | Complementario | ⚠️ Múltiples versiones. Identificar la versión definitiva y archivar el resto. |

### 2.8 UD5 — Cloud computing

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `05-ComputaNube/C_Nube1/` | Cloud computing I | varios | UD5 | Fundamentos de cloud computing | AWS | Completo | |
| `05-ComputaNube/C_Nube2/` | Cloud computing II | varios | UD5 | Servicios cloud avanzados | AWS | Completo | |
| `05-ComputaNube/AWS/` | AWS práctico | varios | UD5 | Laboratorios prácticos AWS | AWS, EC2, S3 | Completo | |
| `05-ComputaNube/01-AWS-Tarea_01.org` | Tarea AWS (org) | org | UD5 | Enunciado de tarea AWS en Org-mode | AWS | Completo | |
| `05-ComputaNube/01-AWS-Tarea_01.pdf` | Tarea AWS (pdf) | pdf | UD5 | Enunciado de tarea AWS en PDF | AWS | Completo | |
| `05-ComputaNube/01-AWS-Tarea_01.tex` | Tarea AWS (tex) | tex | UD5 | Fuente LaTeX de la tarea AWS | LaTeX | Completo | |
| `05-ComputaNube/scriptAWS.sh` | Script AWS | sh | UD5 | Script de automatización AWS CLI | AWS CLI | Completo | |
| `05-ComputaNube/esqueletoAWS.py` | Esqueleto Python | py | UD5 | Código base para la tarea AWS (boto3) | Python, boto3 | Esqueleto | Plantilla para el alumnado. |

### 2.9 UD6 — Herramientas de interfaz gráfica para IA

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `06-10-Herramientas/006-HerramientasGraficas/` | Herramientas gráficas | varios | UD6 | Interfaces gráficas para modelos de IA | Gradio, Streamlit | Completo | |
| `06-10-Herramientas/007-Gradio/` | Gradio | varios | UD6 | Tutoriales específicos de Gradio | Gradio | Completo | Solapa parcialmente con `006-HerramientasGraficas/`. |
| `06-10-Herramientas/008-MCP/` | MCP (Model Context Protocol) | varios | UD6 | Model Context Protocol | MCP | Nuevo | ⚠️ Material muy reciente. Evaluar su pertinencia pedagógica y madurez. |

### 2.10 UD7 — Convergencia tecnológica

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `17-IntroConvergenciaTecnológica/docker-compose.yaml` | Docker Compose | yaml | UD7 | Configuración de infraestructura para convergencia | Docker | Esqueleto | ⚠️ Solo un archivo. El bloque parece incompleto. |
| `18-SistemaConvergenciaTecnologica/TareaAutomatizacionDeTareas.org` | Tarea automatización (org) | org | UD7 | Enunciado de tarea de automatización | — | Completo | |
| `18-SistemaConvergenciaTecnologica/TareaAutomatizacionDeTareas.pdf` | Tarea automatización (pdf) | pdf | UD7 | Versión PDF del enunciado | — | Completo | |
| `18-SistemaConvergenciaTecnologica/DataPipelinesWithApacheAirflow.pdf` | Apache Airflow | pdf | UD7 | Pipelines de datos con Apache Airflow | Apache Airflow | Completo | |
| `19-CasoEstudioConvergenciaBlockChain/BlockChain.org` | Blockchain | org | UD7 | Apunte sobre blockchain | — | Esqueleto | ⚠️ Contenido dudoso para el módulo PIA. Solo un archivo. Según nota del profesor, probablemente no relevante. |
| `20-SeguridadEnConvergenciaTecnologica/` | Seguridad en convergencia | — | UD7 | Carpeta sin contenido | — | Vacío | ⚠️ Carpeta vacía. Decidir si se puebla o se elimina. |

### 2.11 Herramientas transversales (sin unidad fija)

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `06-10-Herramientas/001-NumPy/` | NumPy | varios | UD1/2 | Tutoriales y ejercicios de NumPy | NumPy | Completo | Solapa con `001-002-Numpy-Pandas_Curso/` y con Tema02 de UD1. |
| `06-10-Herramientas/001-002-Numpy-Pandas_Curso/` | Curso NumPy + Pandas | varios | UD1/2 | Curso completo de NumPy y pandas | NumPy, pandas | Completo | ⚠️ Curso completo que integra ambos. Podría absorber los tutoriales sueltos. |
| `06-10-Herramientas/002-Pandas/` | Pandas | varios | UD2 | Tutoriales y ejercicios de pandas | pandas | Completo | Solapa con `001-002-Numpy-Pandas_Curso/`. |
| `06-10-Herramientas/002-Graficas/` | Gráficas | varios | UD2 | Visualización con matplotlib y seaborn | matplotlib, seaborn | Completo | |
| `06-10-Herramientas/003-poetry/` | Poetry | varios | UD2/3 | Gestión de dependencias con Poetry | Poetry | Completo | |
| `06-10-Herramientas/003-RAPIDS/` | RAPIDS | varios | UD3/9 | GPU computing con RAPIDS (cuDF, cuML) | RAPIDS, cuDF, cuML | Completo | Contenido avanzado sobre GPU. Valor pedagógico alto pero dependencia hardware específica. |
| `06-10-Herramientas/004-Poetry_uv/` | Poetry + uv | varios | UD2/3 | Gestión de proyectos con Poetry y uv | Poetry, uv | Completo | Evolución de `003-poetry/`. Probablemente la versión que debe mantenerse. |
| `06-10-Herramientas/modelo_entrenado.pkl` | Modelo pickle | pkl | — | Modelo entrenado de ejemplo | scikit-learn | Complementario | |
| `06-10-Herramientas/modelo_iris.pkl` | Modelo iris | pkl | — | Modelo iris entrenado | scikit-learn | Complementario | |

### 2.12 Herramientas de generación de código con IA

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `16-HerramientaGeneracionCodigo_IA/016_mask_images/` | Imágenes máscara | varios | — | Dataset de imágenes para detección de mascarillas | OpenCV | Completo | 🔍 Origen dudoso: podría ser proyecto de alumno o material docente. Verificar. |
| `16-HerramientaGeneracionCodigo_IA/016_mask_model/` | Modelo máscara | varios | — | Modelo entrenado de detección de mascarillas | Keras, TensorFlow | Completo | 🔍 Misma duda que el anterior. |
| `16-HerramientaGeneracionCodigo_IA/cats_or_dogs/` | Clasificación gatos/perros | varios | — | Clasificación de imágenes gatos vs perros | TensorFlow, Keras | Completo | |
| `16-HerramientaGeneracionCodigo_IA/caraMascarllDetecKeras.py` | Detección mascarilla Keras | py | — | Script de detección de mascarillas con Keras | Keras, OpenCV | Completo | 🔍 Verificar si es material docente original o adaptado. |
| `16-HerramientaGeneracionCodigo_IA/caraMascarllDetecKerasOpenCV.py` | Detección mascarilla OpenCV | py | — | Script de detección de mascarillas con OpenCV | OpenCV | Completo | 🔍 Misma duda. |
| `16-HerramientaGeneracionCodigo_IA/snipetTensorFlowJs.html` | TensorFlow.js | html | — | Ejemplo de TensorFlow.js en navegador | TensorFlow.js | Completo | |

### 2.13 Datasets

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `Datasets/jena_climate_2009_2016.csv` | Dataset clima Jena | csv | Taller | Datos climáticos históricos para forecasting | — | Completo | Dataset público usado en talleres de series temporales. |
| `Datasets/jena_climate_2009_2016.csv.zip` | Dataset clima Jena (zip) | zip | Taller | Versión comprimida del dataset | — | Completo | Duplicado comprimido del mismo dataset. |
| `Datasets/housing.zip` | Dataset housing | zip | UD4 | Precios de vivienda en California (comprimido) | — | Completo | |

### 2.14 Planificación

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `Planificacion/PlanificacionUnidades24_25V1.md` | Planificación V1 | md | Planificación | Planificación de unidades 24-25, versión 1 | — | Completo | Primera versión. |
| `Planificacion/PIA_planV5.md` | Plan V5 | md | Planificación | Planificación versión 5 | — | Completo | ⚠️ Posible versión final. Confirmar. |
| `Planificacion/PIA_Planificacion_V2.org` | Plan V2 org | org | Planificación | Planificación versión 2 | Emacs Org | Completo | |
| `Planificacion/PIA_Planificacion_V3.org` | Plan V3 org | org | Planificación | Planificación versión 3 | Emacs Org | Completo | |
| `Planificacion/PIA_Planificacion_V4.org` | Plan V4 org | org | Planificación | Planificación versión 4 | Emacs Org | Completo | |
| `Planificacion/PIA_Planificacion_V5.org` | Plan V5 org | org | Planificación | Planificación versión 5 | Emacs Org | Completo | |
| `Planificacion/PIA_Planifiacion1_16sem24_25.org` | Plan 16 semanas | org | Planificación | Planificación de 16 semanas | Emacs Org | Completo | ⚠️ Posible borrador preliminar. |
| `Planificacion/PIA_Planifiacion2_28sem_4_25.org` | Plan 28 semanas | org | Planificación | Planificación de 28 semanas | Emacs Org | Completo | |
| `Planificacion/PIA_Planifiacion3_32sem_4_25.org` | Plan 32 semanas | org | Planificación | Planificación de 32 semanas | Emacs Org | Completo | ⚠️ 32 semanas parece la versión más completa. Confirmar como fuente de verdad. |

### 2.15 Proyecto integrador

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `Proyecto/Proyecto_PIA-SBD.md` | Proyecto PIA-SBD | md | Proyecto | Proyecto integrador entre PIA y SBD | — | Completo | ⚠️ El nombre sugiere un proyecto conjunto con el módulo Sistemas de Big Data. Aclarar límites. |
| `Proyecto/Proyecto_PIA-SBD.pdf` | Proyecto PIA-SBD (pdf) | pdf | Proyecto | Versión PDF del proyecto integrador | — | Completo | |
| `Proyecto/ProyectoPipelineForecastCripto.txt` | Proyecto forecasting cripto | txt | Proyecto | Proyecto de forecasting de criptomonedas | — | Esqueleto | ⚠️ Parece un esbozo o idea no desarrollada. Solo un fichero TXT. |

### 2.16 Cronograma

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `15-B-ReinforcementLearning/Cronograma_IA_BigData.xlsx` | Cronograma | xlsx | Planificación | Planificación temporal del módulo IA + BigData | — | Planificación | ⚠️ Archivo fuera de la carpeta Planificacion/. Mover en la reorganización. |

### 2.17 Libros y referencias

| Ruta | Elemento | Tipo | Bloque/Unidad | Descripción | Herramientas | Estado aparente | Observaciones |
|------|----------|------|---------------|-------------|--------------|-----------------|---------------|
| `Libros/ArtificialIntelligence_A-ModernApproach-GlobalEdition-2021.pdf` | AI: A Modern Approach | pdf | Referencia | Libro de referencia clásico de IA | — | Referencia | Stuart Russell. No incluir en catálogo docente pero mantener como referencia. |
| `Libros/ArtificialIntelligenceProgrammingWithPythonFromZero2Hero-2022.pdf` | AI Programming Zero2Hero | pdf | Referencia | Programación de IA con Python | Python | Referencia | |
| `Libros/ArtificialIntelligenceWithPythonCompleteGuide2BuildingIntelligentApps-2020.pdf` | AI with Python guide | pdf | Referencia | Guía completa de IA con Python | Python | Referencia | |
| `Libros/ArtificialIntelligenceAndMachineLearningFundamentals-2018.epub` | AI & ML Fundamentals | epub | Referencia | Fundamentos de IA y ML | — | Referencia | |
| `Libros/PythonMachineLearning4Beginners-2020.epub` | Python ML for Beginners | epub | Referencia | ML para principiantes con Python | Python, sklearn | Referencia | |
| `Libros/Deep-Learning-with-PyTorch.pdf` | Deep Learning with PyTorch | pdf | Referencia | Deep Learning con PyTorch | PyTorch | Referencia | |
| `Libros/ComputerVision_Szeliski_CVAABook_2ndEd.pdf` | Computer Vision (Szeliski) | pdf | Referencia | Visión por computador — libro de referencia | — | Referencia | Richard Szeliski. |
| `Libros/AprendeMachineLearning.pdf` | Aprende Machine Learning | pdf | Referencia | Introducción a ML (español) | — | Referencia | |
| `Libros/DSML.pdf` | Data Science and ML | pdf | Referencia | Data Science y Machine Learning | — | Referencia | |
| `Libros/Programacion/` | Programación | varios | Referencia | Libros de programación base | — | Referencia | Sin detalle de contenidos. Revisar si hay títulos relevantes. |
| `Libros/ML/` | ML libros | varios | Referencia | Libros de machine learning | — | Referencia | Sin detalle de contenidos. |
| `Libros/DeepLearning/` | Deep Learning libros | varios | Referencia | Libros de deep learning | — | Referencia | Sin detalle de contenidos. |
| `Libros/aima-python/` | AIMA Python | varios | Referencia | Código Python del libro AIMA | Python | Referencia | Código acompañante del libro de Russell. |
| `Libros/Artificial-Intelligence-with-Python/` | AI with Python code | varios | Referencia | Código del libro AI with Python | Python | Referencia | |
| `Libros/ProgrAIwithPythonZero2Hero-Example_Code.zip` | Código Zero2Hero | zip | Referencia | Ejemplos de código del libro Zero2Hero | Python | Complementario | |

---

## 3. Materiales de corrección detectados

| Ruta | Elemento | Uso probable | Unidad/Bloque | Observaciones |
|------|----------|-------------|---------------|---------------|
| — | No se detectaron | — | — | El curso 24-25 documentado no incluye prompts, guías o instrucciones de corrección explícitos entre los materiales inventariados. Esto puede deberse a que: |
| | | | | (a) el docente usaba criterios no formalizados, |
| | | | | (b) los materiales de corrección estaban en otra ubicación (ej. `Correcciones/` en el árbol actual), |
| | | | | (c) el barrido inicial no los capturó. |

**Nota:** En el árbol actual existe una carpeta `Correcciones/` (en `/home/jmsa/IESRafaelAlberti/RafaelAlberti25_26/Modulos/PIA/Correcciones/`) que no fue capturada por el barrido original. De cara a la reorganización, conviene revisar su contenido e incorporar a este inventario cualquier prompt o guía reutilizable que contenga.

---

## 4. Elementos excluidos deliberadamente

| Categoría | Rutas o patrones detectados | Motivo de exclusión | Observaciones |
|-----------|---------------------------|---------------------|---------------|
| **Entregas de alumnado** | `01-04-Programacion/alumnos/`, `01-04-Programacion/repos/` | Repositorios y entregas de alumnado. Se eliminarán en fase posterior. | No inventariar como material docente. |
| **Residuos técnicos** | `.Rhistory`, `.idea/`, `.vscode/`, `.mypy_cache/`, `*.md~`, `*.unison.*` | Archivos de configuración local, backups automáticos. | Se filtran en la reorganización. |
| **Notas personales informales** | `SiguientesParetes_ANN.txt`, `FicheroDeTexto.txt` | Contenido no estructurado, probablemente notas personales del docente. | Revisar brevemente por si contienen ideas aprovechables, luego archivar. |
| **Alumnos/ completo** | `Alumnos/` | Calificaciones, listados, datos personales. | No inventariar en catálogo docente. |
| **Correcciones (evaluaciones completas)** | No detectado en 24-25, pero existe `Correcciones/` en el árbol actual | Artefactos de corrección — informes, CSVs de notas, feedback individual. | Archivar, pero no forman parte del catálogo docente. |
| **ZIPs de dudosa procedencia** | Varios ZIPs en `01-04-Programacion/`, `15-B-ReinforcementLearning/`, `BibliotecasIA/` | Posibles entregas de alumnado o materiales sin verificar. | Incluidos en el catálogo como "Complementario" con advertencia 🔍 hasta verificar. |

---

## 5. Riesgos, duplicidades y material dudoso

### 5.1 Duplicidades confirmadas

| Elemento A | Elemento B | Tipo de duplicidad | Recomendación |
|-----------|-----------|-------------------|---------------|
| `06-10-Herramientas/001-NumPy/` | `06-10-Herramientas/001-002-Numpy-Pandas_Curso/` y `01-04-Programacion/Tema02/` | Contenido NumPy en tres ubicaciones distintas | Unificar en la UD que corresponda tras decidir si NumPy es UD1 o UD2. |
| `06-10-Herramientas/002-Pandas/` | `06-10-Herramientas/001-002-Numpy-Pandas_Curso/` y `01-04-Programacion/Tema02/` | Contenido pandas en tres ubicaciones | Misma recomendación. |
| `06-10-Herramientas/003-poetry/` | `06-10-Herramientas/004-Poetry_uv/` | Poetry: un tutorial y su evolución con uv | Mantener solo `004-Poetry_uv/`. |
| `06-10-Herramientas/006-HerramientasGraficas/` | `06-10-Herramientas/007-Gradio/` | Gradio aparece en ambas | Mantener `007-Gradio/` como tutorial específico, unificar referencia en la carpeta general. |
| `15-ModeladoAvanzadoDeRedesNeuronales/Housing/` | `15-ModeladoAvanzadoDeRedesNeuronales/BostonHousing/` | Mismo tipo de problema (regresión vivienda) con distinto dataset | Valorar si ambos son necesarios o si uno es evolución del otro. |
| `11-TratamientoDeDatos/S11-Trat-Datos/` | `11-TratamientoDeDatos/S11-Trat-Datos.zip` | Carpeta extraída y su ZIP | Eliminar el ZIP una vez verificado que la carpeta contiene todo. |
| `Datasets/jena_climate_2009_2016.csv` | `Datasets/jena_climate_2009_2016.csv.zip` | Dataset y su comprimido | Mantener solo el comprimido o solo el CSV (el que ocupe menos, según criterio). |

### 5.2 Material obsoleto, incompleto o dudoso

| Elemento | Riesgo | Acción |
|----------|--------|--------|
| `01-04-Programacion/Mojo/` | Lenguaje experimental. Puede que en 25-26 ya no tenga sentido. | Decisión humana: ¿se mantiene como exploración o se archiva? |
| `06-10-Herramientas/008-MCP/` | MCP es muy reciente. Valor pedagógico no evaluado. | Revisar pertinencia. |
| `19-CasoEstudioConvergenciaBlockChain/BlockChain.org` | Blockchain no está en el temario de PIA. Un solo archivo. | Archivar o eliminar. |
| `20-SeguridadEnConvergenciaTecnologica/` | Carpeta vacía. | Decidir si se puebla o se elimina. |
| `17-IntroConvergenciaTecnológica/docker-compose.yaml` | Solo un archivo para todo un bloque. | Desarrollar contenido o integrar en otro bloque. |
| `14-ModeladoRedesNeuronales/FicheroMarkDown.md` | Archivo MarkDown, estado esqueleto. | Completar o archivar. |
| `14-ModeladoRedesNeuronales/SiguientesParetes_ANN.txt` | Notas informales, nombre con posible error tipográfico. | Revisar y archivar. |
| `Proyecto/ProyectoPipelineForecastCripto.txt` | Esqueleto de proyecto, solo un TXT. | Desarrollar o archivar. |
| `16-HerramientaGeneracionCodigo_IA/` (varios archivos) | No está claro si es material docente o proyecto de alumno. | Verificar autoría y propósito. |
| `15-ModeladoAvanzadoDeRedesNeuronales/Tareas/` | Mezcla de enunciados y posibles entregas. | Separar materiales docentes de entregas. |
| `15-B-ReinforcementLearning/Cronograma_IA_BigData.xlsx` | Cronograma fuera de la carpeta Planificacion/. | Mover a planificación. |
| `Proyecto/Proyecto_PIA-SBD.md` | ¿Es proyecto de PIA o de SBD? ¿O conjunto? | Aclarar límites entre módulos. |

### 5.3 Riesgos estructurales

1. **La carpeta `06-10-Herramientas/` es un cajón de sastre.** Agrupa tutoriales y materiales
   de herramientas que deberían distribuirse entre las unidades correspondientes (UD1 a UD9).
   En la reorganización, cada tutorial debería integrarse en la unidad donde se use.

2. **Mezcla de normativa con material docente.** Los PDFs oficiales del módulo y de SAA están
   dentro de carpetas de contenido (`11-TratamientoDeDatos/`, `13-EvaluacionDeResultados/`).
   Deberían separarse a una carpeta `00-Normativa/` o similar.

3. **Material de otros módulos (SAA) dentro del árbol de PIA.** Varias carpetas
   (`15-ModeladoAvanzadoDeRedesNeuronales/SAA/`, `13-EvaluacionDeResultados/ia_bd_m2...pdf`)
   contienen material del módulo Sistemas de Aprendizaje Automático. Separar.

4. **Múltiples versiones de planificación sin fuente de verdad.** Sin un documento canónico
   que indique cuál es la planificación real ejecutada, es imposible saber qué se impartió.

5. **El proyecto integrador "PIA-SBD"** sugiere coordinación entre módulos pero no hay
   documentación de cómo se articula esa coordinación. Riesgo de solapamiento o lagunas.

---

## 6. Recomendaciones para la siguiente fase

### 6.1 Criterios para la estructura común entre módulos

1. **Numeración por UDs, no por carpetas temáticas arbitrarias.** La estructura actual del árbol
   reorganizado (`ud1-*`, `UD2`, `UD3`…`UD9`) es correcta. Debe mantenerse.

2. **Separar claramente:**
   - `XX-contenido/` → material docente (apuntes, ejercicios, notebooks)
   - `XX-evaluacion/` → rúbricas, enunciados de tareas, criterios
   - `XX-correccion/` → prompts de corrección, guías de revisión
   - `XX-entregas/` → solo si se archivan como muestra (anónimas)

3. **Establecer un convenio de nomenclatura:**
   - Apuntes: `UDXX-NombreTema.{org,md}`
   - Ejercicios: `UDXX-Ejercicios/`
   - Casos prácticos: `UDXX-Caso-Practico/`
   - Evaluación: `UDXX-Evaluacion/`
   - Autoevaluación: `UDXX-Autoevaluacion/`

4. **Archivos de planificación: mantener solo la versión ejecutada** más la planificación
   del próximo curso, con un nombre canónico (ej. `planificacion-25-26.md`).

5. **Los ZIPs deben tener una justificación clara** en su nombre o en un README dentro
   del mismo ZIP. Si son backups, mover a `_archivo/`.

### 6.2 Separación de materiales

| Función | Destino propuesto | Ejemplos |
|---------|------------------|----------|
| Apuntes, guías, tutoriales | `UDXX/` | Temas, resúmenes, org, pdf, md |
| Ejercicios prácticos | `UDXX/Ejercicios/` | Notebooks, scripts, enunciados |
| Evaluación (tareas, exámenes) | `UDXX/Evaluacion/` o `Evaluaciones/` | Rúbricas, criterios, enunciados |
| Corrección (prompts, guías) | `_correccion/` o `UDXX/Correccion/` | Prompts de revisión, checklists |
| Entregas de alumnado | `_archivo/entregas/` (o eliminar) | ZIPs, repositorios |
| Normativa | `_referencia/normativa/` | PDFs oficiales del módulo |
| Libros | `_referencia/libros/` | PDFs, epubs de referencia |
| Datasets | `_datasets/` | CSVs, archivos de datos |
| Planificación | `_planificacion/` | Cronogramas, programaciones |
| Material de otros módulos | Mover al árbol del módulo correspondiente | Contenido de SAA mezclado en PIA |

### 6.3 Preparación de la revisión curricular para 25-26

| Tema | Acción | Prioridad |
|------|--------|-----------|
| **Mojo** | Decidir si se mantiene como contenido exploratorio o se elimina. | Media |
| **MCP** | Evaluar si se incorpora formalmente al temario. | Baja |
| **Blockchain** | Eliminar del temario de PIA (confirmado por nota del profesor). | Alta |
| **Seguridad en convergencia** | Decidir si se desarrolla contenido o se elimina la unidad. | Media |
| **Proyecto PIA-SBD** | Definir límites claros y responsabilidades de cada módulo. | Alta |
| **Reinforcement Learning** | Evaluar si pasa a ser unidad obligatoria o se mantiene como complemento. | Media |
| **Herramientas gráficas (Gradio, Streamlit)** | Buena cobertura, mantener y actualizar. | Baja |
| **RAPIDS** | Verificar disponibilidad de GPUs para el próximo curso. Si no hay, replantear. | Media |
| **Airflow** | El material existe pero parece mínimo. Decidir profundidad. | Baja |
| **H5P** | Buen formato interactivo. Mantener y ampliar a otras UDs. | Baja |
| **Autoevaluaciones** | Presentes en UD2 pero ausentes en el resto. Extender. | Media |

### 6.4 Recomendación metodológica

1. **Establecer un "fuente de verdad" único** para cada contenido: un archivo Org-mode o Markdown
   desde el que se exporten el resto de formatos. Evitar mantener org, pdf, tex y md como fuentes
   independientes (riesgo de desincronización).

2. **Inventariar con etiquetas** (front matter YAML) en lugar de tablas externas. Cada archivo
   podría incluir metadatos de unidad, RA, criterio de evaluación, herramientas y estado.

3. **Archivar versiones antiguas** en una carpeta `_legacy/` con un README que explique qué
   contenían y por qué se archivan. No mantenerlas conviviendo con el material vigente.

4. **Establecer un ciclo de revisión anual** con checklist: (a) tecnologías obsoletas,
   (b) normativa actualizada, (c) feedback del alumnado, (d) resultados académicos.
