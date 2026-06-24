# Sesión separada - Planificación curso siguiente

Fecha: 2026-04-28

## Contexto del curso actual

En el curso actual se ha trabajado una base amplia de inteligencia artificial aplicada y herramientas de desarrollo.

### Contenidos ya vistos

- Fundamentos de programación en Python.
- NumPy.
- Alternativas a NumPy con menor profundidad.
- pandas.
- Alternativas a pandas con menor profundidad.
- DuckDB y FireDucks, vistos de forma introductoria.
- Parquet como formato habitual frente a CSV, por compresión y rapidez.
- Redes neuronales básicas.
- Redes convolucionales.
- LSTM.
- GRU.
- Transformers.
- Liquid models.
- Mamba.
- Herramientas cloud.
- Herramientas para construir, evaluar y desplegar aplicaciones de IA.
- Gradio.
- LangChain.
- DSPy.
- LlamaIndex.
- MLflow.
- FastAPI.
- Ollama.
- LangGraph.
- Herramientas adicionales de RAG, bases vectoriales, evaluación y proveedores de modelos.

### Contenidos ya vistos en módulos de Big Data

Estos contenidos no conviene duplicarlos en profundidad en IA, salvo como integración con proyectos:

- Airflow.
- Mage AI.
- PySpark.
- Airbyte.
- S3.
- MinIO.
- Sistemas de ingesta y almacenamiento de datos.
- Big Data aplicado.

## Proyecto actual del alumnado

El proyecto actual incluye, en mayor o menor medida:

1. Ingesta de datos desde varias fuentes.
2. Limpieza de datos.
3. Integración de datos.
4. Visualización.
5. Almacenamiento para modelos y dashboards.
6. Preparación para entrenamiento.
7. Entrenamiento.
8. Métricas.
9. Selección de modelo.
10. Despliegue.
11. Presentación del resultado.

## Diagnóstico

El stack actual es suficiente para cerrar el curso y permitir que el alumnado avance en el proyecto.

No parece recomendable añadir muchas más herramientas ahora. El siguiente paso natural sería profundizar en experimentación, reproducibilidad y MLOps, pero teniendo en cuenta que se ha aprobado un nuevo curso de especialización centrado precisamente en MLOps.

Por tanto, la propuesta para el curso siguiente debe organizarse como una progresión hacia MLOps, sin duplicar innecesariamente los módulos de Big Data.

## Flujo de aprendizaje recomendado para el curso siguiente

## Encaje de herramientas y conocimientos base

Antes de entrar en los bloques específicos de MLOps conviene ordenar qué papel juega cada grupo de herramientas dentro del itinerario.

### Bloque 0. Base de programación y análisis de datos

Este bloque funciona como prerrequisito o repaso inicial. No debería ocupar mucho tiempo si el alumnado ya lo ha trabajado, pero sí conviene usarlo como base común para los proyectos.

Contenidos:

1. Python aplicado a proyectos de IA.
2. Estructuras de datos, funciones, módulos y manejo de ficheros.
3. Entornos virtuales y gestión de dependencias.
4. NumPy para arrays, operaciones vectorizadas y tensores básicos.
5. pandas para limpieza, transformación y análisis tabular.
6. DuckDB para consultas SQL locales sobre CSV, Parquet y DataFrames.
7. FireDucks como alternativa/acelerador compatible con pandas.
8. Formato Parquet como formato preferente para datos intermedios.

Herramientas:

- Python.
- NumPy.
- pandas.
- DuckDB.
- FireDucks.
- Parquet.
- Jupyter/Colab.

Resultado esperado:

- Dataset limpio y preparado en Parquet.
- Notebook o script reproducible de análisis y preparación.
- Consultas SQL locales con DuckDB sobre datos tabulares.

Relación con Big Data:

- **[Big Data]** Si el volumen supera el uso cómodo de pandas/DuckDB, pasar a PySpark.
- **[Big Data]** Si los datos están en MinIO/S3, coordinar con los módulos de almacenamiento e ingesta.

### Bloque 0.5. Modelado clásico y deep learning

Este bloque recoge las herramientas de entrenamiento de modelos. Es la base técnica antes de entrar en tracking, versionado y despliegue.

Contenidos:

1. Modelos clásicos supervisados y no supervisados.
2. División train/validation/test.
3. Preprocesado y pipelines de entrenamiento.
4. Métricas de clasificación, regresión y clustering.
5. Redes neuronales básicas.
6. CNN.
7. RNN, LSTM y GRU.
8. Transformers.
9. Liquid models.
10. Mamba.
11. Comparación entre modelos clásicos, deep learning y modelos generativos.

Herramientas:

- scikit-learn.
- PyTorch.
- PyTorch Lightning.
- TensorFlow/Keras, si se mantiene como alternativa.
- Hugging Face Transformers, si se trabaja con modelos preentrenados.

Resultado esperado:

- Varios modelos entrenados y evaluados con métricas comparables.
- Código de entrenamiento separado de la exploración inicial.
- Modelo candidato preparado para registrarse en MLflow.

Relación con bloques posteriores:

- Conecta directamente con el Bloque 3, `Tracking avanzado de experimentos`.
- Conecta con el Bloque 7, `Empaquetado y servicio de modelos`.
- Conecta con el Bloque 9, `Monitorización y mantenimiento`.

### Bloque 0.6. Cloud, almacenamiento y servicios gestionados

Este bloque debe tratarse como infraestructura transversal. Si ya se ha visto en una unidad de herramientas cloud, puede quedar como repaso aplicado al proyecto.

Contenidos:

1. Almacenamiento local frente a almacenamiento remoto.
2. Buckets tipo S3.
3. MinIO como alternativa local compatible con S3.
4. Servicios cloud para entrenamiento, almacenamiento o despliegue.
5. Gestión de credenciales.
6. Costes, cuotas y límites.
7. Buenas prácticas de uso de recursos cloud.

Herramientas:

- S3.
- MinIO.
- Servicios cloud vistos en el curso.
- Hugging Face Spaces.
- Notebooks cloud.
- APIs de proveedores de modelos.

Resultado esperado:

- Proyecto capaz de leer/escribir datos o artefactos desde almacenamiento local o compatible con S3.
- Separación clara entre código, configuración y credenciales.

Relación con Big Data:

- **[Big Data]** S3, MinIO, Airbyte, Airflow, Mage AI y PySpark deben coordinarse con los módulos de Big Data.
- En IA/MLOps se usarían como infraestructura consumida, no como contenido principal.

### Bloque 0.7. Herramientas de aplicación de IA

Este bloque cubre la capa que convierte modelos en aplicaciones utilizables.

Contenidos:

1. Interfaces interactivas.
2. APIs de inferencia.
3. Pipelines con LLM.
4. RAG.
5. Modelos locales y cloud.
6. Evaluación de respuestas generativas.
7. Orquestación de agentes.

Herramientas:

- Gradio.
- FastAPI.
- LangChain.
- LlamaIndex.
- DSPy.
- Ollama.
- LangGraph.
- Ragas.
- Chroma/FAISS como piezas internas de RAG.

Resultado esperado:

- Demo o API funcional conectada con un modelo entrenado o un sistema RAG.
- Presentación del resultado del proyecto.

Relación con MLOps:

- Esta capa alimenta el Bloque 7, `Empaquetado y servicio de modelos`.
- En proyectos con LLM/RAG conecta con el Bloque 10, `MLOps aplicado a IA generativa`.

### Bloque 1. Reproducibilidad de proyectos de IA

Objetivo: que cualquier proyecto pueda ejecutarse, entenderse y reproducirse en otro entorno.

Contenidos:

1. Estructura estándar de proyecto de IA.
2. Separación de código, datos, modelos, notebooks y configuración.
3. Entornos reproducibles con `requirements.txt`, `pyproject.toml` o Conda.
4. Variables de entorno y gestión de secretos.
5. Semillas aleatorias y control de fuentes de variabilidad.
6. Convenciones de nombres para datasets, modelos y experimentos.

Herramientas sugeridas:

- `venv`, Conda o Micromamba.
- `python-dotenv`.
- `pydantic-settings`.
- Plantillas de proyecto tipo Cookiecutter Data Science, si se quiere introducir.

Resultado esperado:

- Proyecto ejecutable desde cero con instrucciones claras.
- Entorno reproducible.
- Configuración separada del código.

### Bloque 2. Configuración de experimentos

Objetivo: evitar notebooks con parámetros dispersos y permitir comparar ejecuciones de forma ordenada.

Contenidos:

1. Archivos de configuración.
2. Parámetros de entrenamiento.
3. Parámetros de datos.
4. Parámetros de evaluación.
5. Configuraciones por entorno: local, aula, cloud.

Herramientas sugeridas:

- YAML o TOML.
- `Hydra`.
- `omegaconf`.
- `pydantic` para validar configuración.

Relación con lo ya visto:

- Complementa `MLflow`, porque MLflow registra qué se ejecutó, pero Hydra o Pydantic ayudan a definir de forma limpia con qué configuración se ejecuta.

Resultado esperado:

- Un mismo entrenamiento ejecutable con distintas configuraciones sin tocar código.

### Bloque 3. Tracking avanzado de experimentos

Objetivo: profundizar en MLflow más allá de registrar métricas básicas.

Contenidos:

1. Experimentos y runs.
2. Parámetros, métricas y artefactos.
3. Registro de modelos.
4. Versionado de modelos.
5. Comparación de runs.
6. Tracking de modelos clásicos, deep learning y RAG.
7. Uso de la interfaz de MLflow.

Herramientas sugeridas:

- `MLflow Tracking`.
- `MLflow Model Registry`.
- `MLflow Models`.

Resultado esperado:

- Selección justificada de un modelo mediante métricas y artefactos.
- Registro del modelo seleccionado.
- Preparación para servir el modelo.

### Bloque 4. Versionado de datos, modelos y artefactos

Objetivo: controlar qué datos y qué modelo produjeron cada resultado.

Contenidos:

1. Problema de versionar datasets grandes.
2. Versionado de datos procesados.
3. Versionado de modelos entrenados.
4. Relación entre Git, datos y artefactos.
5. Trazabilidad dataset-configuración-modelo-métrica.

Herramientas sugeridas:

- `DVC`.
- Git.
- MLflow artifacts.
- Almacenamiento local o remoto.

Posible integración con Big Data:

- **[Big Data]** Si se usa MinIO o S3 como backend de artefactos o datos versionados.
- **[Big Data]** Si se usan datasets particionados en Parquet.

Resultado esperado:

- Pipeline en el que se pueda saber qué versión de datos produjo qué modelo.

### Bloque 5. Validación y calidad de datos

Objetivo: detectar problemas antes de entrenar modelos.

Contenidos:

1. Validación de esquema.
2. Tipos de datos.
3. Rangos válidos.
4. Nulos.
5. Duplicados.
6. Cambios en distribución.
7. Validación antes y después de limpieza.

Herramientas sugeridas:

- `Pandera`.
- `Great Expectations`.
- `Pydantic` para contratos de datos.

Relación con lo ya visto:

- Complementa pandas, DuckDB y Parquet.
- Evita que la limpieza sea solo manual o visual.

Posible integración con Big Data:

- **[Big Data]** Validación de datasets grandes con Spark o Airflow/Mage AI.
- **[Big Data]** Validación de datos en MinIO/S3.

Resultado esperado:

- Tests automáticos de calidad de datos antes del entrenamiento.

### Bloque 6. Pipelines reproducibles de entrenamiento

Objetivo: pasar del notebook manual a una ejecución estructurada.

Contenidos:

1. Pipeline de preparación.
2. Pipeline de entrenamiento.
3. Pipeline de evaluación.
4. Pipeline de registro del modelo.
5. Ejecución local.
6. Parametrización.

Herramientas sugeridas:

- Scripts Python.
- `Makefile` o `nox`.
- `Hydra`.
- `MLflow`.
- `DVC`.

Posible integración con Big Data:

- **[Big Data]** Airflow, Mage AI o Prefect si se quiere orquestar la ejecución completa.
- **[Big Data]** PySpark si el dataset excede pandas/DuckDB.

Resultado esperado:

- Entrenar y evaluar con un comando reproducible.

### Bloque 7. Empaquetado y servicio de modelos

Objetivo: convertir un modelo seleccionado en algo consumible por una aplicación.

Contenidos:

1. Serialización de modelos.
2. Carga del modelo.
3. API de inferencia.
4. Validación de entrada.
5. Versionado del endpoint.
6. Pruebas básicas de la API.
7. Comparación Gradio frente a FastAPI.

Herramientas sugeridas:

- `FastAPI`.
- `Pydantic`.
- `MLflow Models`.
- `Docker`.
- `Gradio` para demos.

Resultado esperado:

- Modelo accesible mediante API REST.
- Demo visual opcional con Gradio.

### Bloque 8. Contenedores y despliegue

Objetivo: desplegar de forma reproducible.

Contenidos:

1. Dockerfile para API.
2. Variables de entorno.
3. Volúmenes para modelos o artefactos.
4. Imagen reproducible.
5. Despliegue local.
6. Despliegue cloud si procede.

Herramientas sugeridas:

- Docker.
- Docker Compose.
- FastAPI.
- MLflow.
- MinIO si se usa como almacenamiento local tipo S3.

Posible integración con Big Data:

- **[Big Data]** MinIO/S3 como almacenamiento de datos, modelos o artefactos.
- **[Big Data]** Orquestación de contenedores en entornos de datos.

Resultado esperado:

- API contenerizada y ejecutable en otro equipo.

### Bloque 9. Monitorización y mantenimiento

Objetivo: entender que un modelo desplegado puede degradarse.

Contenidos:

1. Logs de inferencia.
2. Latencia.
3. Errores de API.
4. Distribución de entradas.
5. Drift de datos.
6. Drift de predicción.
7. Alertas básicas.

Herramientas sugeridas:

- `Evidently AI`.
- `Prometheus` y `Grafana`, si se quiere profundizar.
- Logs estructurados.
- MLflow para comparar nuevas versiones.

Resultado esperado:

- Informe de monitorización básico.
- Decisión razonada sobre si reentrenar o no.

### Bloque 10. MLOps aplicado a IA generativa

Objetivo: aplicar los principios anteriores a LLMs y RAG.

Contenidos:

1. Versionado de prompts.
2. Versionado de documentos.
3. Configuraciones RAG.
4. Evaluación de respuestas.
5. Comparación de modelos locales y cloud.
6. Coste, latencia y calidad.
7. Registro de ejemplos de entrada/salida.

Herramientas sugeridas:

- `MLflow`.
- `LlamaIndex`.
- `LangChain`.
- `DSPy`.
- `Ollama`.
- `Ragas`, si se quiere evaluar RAG con más profundidad.

Resultado esperado:

- Sistema RAG versionado, evaluado y trazable.

## Secuencia recomendada

1. Reproducibilidad del proyecto.
2. Configuración de experimentos.
3. MLflow avanzado.
4. DVC y versionado de datos/modelos.
5. Validación de datos.
6. Pipelines de entrenamiento.
7. FastAPI y serving.
8. Docker.
9. Monitorización.
10. MLOps para RAG y LLMs.

## Herramientas prioritarias para el curso siguiente

Prioridad alta:

1. `MLflow` avanzado.
2. `DVC`.
3. `Hydra` o configuración con `Pydantic`.
4. `Pandera` o `Great Expectations`.
5. `FastAPI` aplicado a serving.
6. Docker aplicado a modelos.

Prioridad media:

1. `Evidently AI`.
2. `Ragas`.
3. `Prometheus` y `Grafana`.
4. `Prefect`, si no se quiere usar Airflow/Mage AI desde Big Data.

Herramientas que ya corresponden principalmente a Big Data:

1. **[Big Data]** Airflow.
2. **[Big Data]** Mage AI.
3. **[Big Data]** PySpark.
4. **[Big Data]** Airbyte.
5. **[Big Data]** S3.
6. **[Big Data]** MinIO.
7. **[Big Data]** Procesamiento distribuido y almacenamiento masivo.

## Nota docente

Si el nuevo curso de especialización de MLOps se imparte de forma independiente, conviene no saturar el cierre del curso actual. Lo más útil ahora es dejar al alumnado con una visión de conjunto y reservar para el curso siguiente la profundización en reproducibilidad, versionado, calidad de datos, pipelines, despliegue y monitorización.

## Ajuste por horas reales disponibles

Contexto horario:

- El curso completo tiene unas 600 horas.
- El periodo lectivo efectivo va aproximadamente de finales de septiembre o principios de octubre a finales de mayo.
- Hay clase de lunes a jueves, 5 horas al día.
- Para este módulo se dispone de unas 7 horas semanales.
- No se puede depender totalmente de que `scikit-learn`, PyTorch o fundamentos de entrenamiento se vean a tiempo en el módulo de Sistemas de Aprendizaje Automático, porque ese módulo dispone de menos horas y avanza despacio.

Conclusión: la planificación anterior es una hoja de ruta amplia, pero no puede impartirse completa dentro de este módulo. Hay que priorizar un camino mínimo viable para que el alumnado pueda hacer proyectos funcionales.

### Principio de ajuste

El módulo debe cubrir lo imprescindible para que el alumnado pueda:

1. Cargar y preparar datos.
2. Entrenar modelos básicos sin esperar a otro módulo.
3. Evaluar y seleccionar modelos.
4. Registrar experimentos.
5. Construir una demo o API.
6. Desplegar o presentar el resultado.
7. Entender dónde encajan RAG, LLMs y herramientas modernas sin profundizar en todas.

## Propuesta realista para 7 horas semanales

Si se estiman unas 28-30 semanas útiles, el módulo tendría aproximadamente 196-210 horas reales. Conviene reservar parte importante para proyecto, incidencias, repaso y entregas.

Distribución sugerida:

| Bloque | Horas aproximadas | Prioridad |
|---|---:|---|
| Python aplicado, NumPy, pandas, Parquet, DuckDB | 25-30 h | Alta |
| scikit-learn mínimo viable | 20-25 h | Alta |
| PyTorch mínimo viable | 25-30 h | Alta |
| Redes CNN/RNN/Transformers vistos de forma aplicada | 25-35 h | Alta |
| Herramientas de aplicación IA: Gradio, FastAPI, LangChain/LlamaIndex básico | 25-30 h | Alta |
| MLflow básico y reproducibilidad | 15-20 h | Alta |
| Proyecto integrado | 45-60 h | Muy alta |
| Ampliaciones: DSPy, Ollama, LangGraph, Ragas, DVC, monitorización | 10-20 h | Media/baja |

Esto obliga a dejar fuera o tocar solo de forma demostrativa:

- DVC profundo.
- Hydra profundo.
- Great Expectations/Pandera profundo.
- Evidently AI.
- Prometheus/Grafana.
- LangGraph avanzado.
- DSPy avanzado.
- Ragas avanzado.
- Serving productivo avanzado.

## Camino mínimo viable del módulo

### 1. Base de datos y preparación

Objetivo: que puedan trabajar con datasets reales sin atascarse.

Imprescindible:

- Python práctico.
- NumPy básico.
- pandas para limpieza.
- Parquet como formato de trabajo.
- DuckDB para consultar datos locales.
- Visualización básica.

No profundizar:

- Alternativas a pandas/NumPy más allá de demostración.
- Optimización avanzada.
- Arquitecturas de datos distribuidas, salvo conexión con Big Data.

### 2. Modelado mínimo con scikit-learn

Aunque exista un módulo de Sistemas de Aprendizaje Automático, aquí hace falta un bloque mínimo porque si no el proyecto no avanza.

Imprescindible:

- Train/test split.
- Preprocesado básico.
- Pipelines simples.
- Modelos de clasificación/regresión más usados.
- Métricas.
- Selección de modelo.
- Guardado del modelo.

Herramientas:

- scikit-learn.
- joblib.
- MLflow básico para registrar resultados.

### 3. Deep learning mínimo con PyTorch

No se puede hacer un curso completo de PyTorch, pero sí un mínimo operativo.

Imprescindible:

- Tensores.
- Dataset y DataLoader.
- Modelo `nn.Module`.
- Bucle de entrenamiento.
- Loss y optimizer.
- Evaluación.
- Guardado/carga de pesos.

PyTorch Lightning:

- Usarlo solo después de haber visto el bucle manual.
- Presentarlo como forma de ordenar entrenamiento, validación y logging.
- No convertirlo en bloque largo.

### 4. Arquitecturas de redes

Priorizar intuición y aplicación, no teoría exhaustiva.

Imprescindible:

- MLP.
- CNN.
- RNN/LSTM/GRU de forma comparativa.
- Transformers de forma aplicada.

Tocar solo como visión moderna:

- Liquid models.
- Mamba.

### 5. Herramientas para aplicaciones de IA

Imprescindible:

- Gradio para presentación rápida.
- FastAPI para API mínima.
- MLflow para experimentos básicos.
- LlamaIndex o LangChain para un RAG sencillo.

Como ampliación o demostración:

- DSPy.
- Ollama.
- LangGraph.
- Ragas.

### 6. Proyecto como eje del módulo

El proyecto debe absorber gran parte del aprendizaje. Cada bloque debe producir una pieza del proyecto:

1. Dataset preparado.
2. Datos limpios en Parquet.
3. Primer modelo baseline con scikit-learn.
4. Modelo neuronal si procede.
5. Métricas y comparación con MLflow.
6. Demo Gradio.
7. API FastAPI opcional.
8. Presentación final.

## Qué mover o coordinar con otros módulos

### Sistemas de Aprendizaje Automático

Este módulo puede profundizar en:

- Teoría de algoritmos.
- Comparación formal de modelos.
- Ajuste de hiperparámetros.
- Fundamentos de redes.

Pero este módulo necesita cubrir lo mínimo de `scikit-learn` y PyTorch para que el proyecto no dependa de que el otro módulo llegue a tiempo.

### Big Data

Mantener en Big Data:

- Airflow.
- Mage AI.
- PySpark.
- Airbyte.
- S3.
- MinIO.
- Procesamiento distribuido.
- Ingesta masiva.

En este módulo solo se usarían como infraestructura ya conocida.

### Curso de especialización MLOps

Reservar para ese curso:

- DVC profundo.
- Hydra profundo.
- Great Expectations/Pandera profundo.
- Evidently AI.
- Monitorización avanzada.
- CI/CD.
- Docker/Kubernetes más serio.
- Model registry avanzado.
- Despliegue productivo.

## Propuesta de secuencia reducida

### Tramo 1. Octubre

- Python aplicado a datos.
- NumPy y pandas.
- Parquet.
- DuckDB.
- Mini EDA.

Entrega: dataset limpio y documentado.

### Tramo 2. Noviembre

- scikit-learn mínimo.
- Pipelines simples.
- Métricas.
- Baseline del proyecto.

Entrega: primer modelo evaluado.

### Tramo 3. Diciembre-enero

- PyTorch mínimo.
- MLP y CNN.
- Entrenamiento y evaluación.
- Comparación con baseline.

Entrega: modelo neuronal o justificación de no usarlo.

### Tramo 4. Febrero

- Secuencias: LSTM/GRU.
- Transformers aplicados.
- Visión general de liquid models y Mamba.

Entrega: prueba comparativa o informe técnico.

### Tramo 5. Marzo

- MLflow básico.
- Reproducibilidad mínima.
- Registro de experimentos.
- Selección de modelo.

Entrega: experimento registrado y modelo seleccionado.

### Tramo 6. Abril

- Gradio.
- FastAPI básico.
- LlamaIndex/LangChain para RAG si encaja en el proyecto.
- Ollama/LangGraph/DSPy como ampliación.

Entrega: demo o API funcional.

### Tramo 7. Mayo

- Integración final.
- Documentación.
- Presentación.
- Defensa técnica.

Entrega: proyecto final completo.

## Resumen de priorización

Imprescindible en este módulo:

1. Python aplicado.
2. pandas, NumPy, Parquet, DuckDB.
3. scikit-learn mínimo.
4. PyTorch mínimo.
5. Métricas y selección.
6. MLflow básico.
7. Gradio.
8. FastAPI básico.
9. Proyecto integrado.

Importante pero reducible:

1. Transformers aplicados.
2. LlamaIndex/LangChain.
3. RAG.
4. PyTorch Lightning.

Solo demostración o ampliación:

1. DSPy.
2. LangGraph.
3. Ollama.
4. Ragas.
5. Liquid models.
6. Mamba.

Para otro curso o especialización MLOps:

1. DVC profundo.
2. Hydra profundo.
3. Great Expectations/Pandera profundo.
4. Evidently AI.
5. CI/CD.
6. Kubernetes.
7. Monitorización avanzada.
