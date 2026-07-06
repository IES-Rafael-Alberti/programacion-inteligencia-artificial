# Pendientes de decisión — UD4 tras reorganización

Esta lista sustituye a la tabla inicial para la siguiente ronda de revisión. Ya no incluye lo que se ha movido claramente a UD6, UD8, UD10, frameworks, métricas o archivo.

## Veredicto actual

UD4 ya está separada en bloques claros:

- `01-fundamentos-redes-neuronales/`
- `02-frameworks-deep-learning/`
- `03-metricas-evaluacion/`

Lo que queda pendiente no debe moverse automáticamente: requiere decisión docente.

## Teoría / modelado avanzado cerrado — 2026-07-05

El residuo de `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/` queda resuelto. La carpeta antigua se ha eliminado al quedar vacía y no debe reaparecer como flujo activo.

| Decisión | Rutas afectadas | Resultado |
|---|---|---|
| Mantener una introducción conceptual RNN/LSTM en UD4. | `RedesRecurrentes.md`, `LSTM.org`, `LSTM.tex` | Se conserva un resumen activo en `01-teoria/01-fundamentos-redes-neuronales/Parte-II-RedesEspecializadas/RedesRecurrentes_y_LSTM_intro.md`; el desarrollo largo queda archivado. |
| Archivar fuentes antiguas `.org` y `.tex`. | `001-DeepLearningV1.*`, `001-DeepLearningV2.org`, `DeepLearningV2.tex`, `AjusteDeHiperParametros.org`, `GeneracionNumerAleatorios.org`, `LSTM.*` | Conservadas en `90-archivo/modelado-avanzado-docs/`, fuera del flujo activo. |
| Archivar duplicados o apoyos históricos de fundamentos. | `001-ChatGPT-GradDesc-Backprop.*`, `001-DeepLearningV2.md` | Archivados porque los fundamentos activos ya tienen capítulos específicos de pérdidas, gradiente y backpropagation. |
| Archivar guía general de proyecto ML. | `GUIA_PROYECTO_PYTHON_ML.md` | No se mueve a UD3 en esta pasada; queda como histórico porque no es específica de UD4 base. |
| Archivar notas laterales. | `Mas_alla_del_entrenamiento.md`, `notas_housing.txt`, `planTrabajoPytorch.txt` | Se separan del flujo activo: mezcla visión/LLM, nota histórica de housing y nota interna de PyTorch. |
| Conservar ZIP sin descomprimir. | `tareas/regularizacion_pack.zip` | Archivado como paquete histórico de regularización; no se introduce en teoría activa. |
| Eliminar basura inequívoca. | `002-Underfit-Overfit_BiasVariance.md~` | Eliminado porque existe fuente activa en `03-metricas-evaluacion/Underfit-Overfit_BiasVariance.md`. |

## Pendientes en proyectos prácticos

| Ruta | Qué contiene | Decisión / duda docente | Opciones razonables | Recomendación provisional |
|---|---|---|---|---|
| `03-practicas/modelado-proyectos/boston-housing/` | Scripts Keras/PyTorch/SciKeras y dataset local pequeño. | **Resuelto documentalmente 2026-07-06**: se mantiene en UD4 como regresión tabular con redes neuronales. | Mantener en UD4 · no mover a UD3 · corregir metodología sólo si se hace evaluable. | Hecho: README ampliado, dataset/rutas verificados y deuda técnica explícita. |
| `03-practicas/modelado-proyectos/euromillones/` | LSTM y notebooks sobre Euromillones. | **Resuelto 2026-07-05**: se conserva como actividad crítica, no como promesa predictiva. | Mantener como actividad crítica · enlazar desde series temporales cuando se trate no estacionariedad. | Hecho: añadido README de advertencia y encuadre docente. |
| `03-practicas/modelado-proyectos/house-prices-kaggle/` | Kaggle tabular, datos, rúbrica y materiales de regresión. | Parece más ML clásico/tabular que deep learning, salvo que aparezca una red neuronal clara. | Mover a UD3 · archivar · mantener sólo si se convierte en práctica NN. | Probable mover a UD3 o archivo; revisar si hay implementación DL antes de mover. |
| `03-practicas/modelado-proyectos/used-cars/` | Notebooks Keras/PyTorch/PyCaret, datos pesados y posible MLflow. | **Resuelto 2026-07-04**: se separaron DL tabular, AutoML y visión. | UD4 · UD3 · UD8. | Hecho: Keras/PyTorch a `used-cars-dl-tabular`, PyCaret a UD3, `layersReuse` a UD8; datos/`mlruns` quedan fuera de Git. |

## Pendientes en recursos

| Ruta | Qué contiene | Duda | Opciones razonables | Recomendación provisional |
|---|---|---|---|---|
| `05-recursos/modelado-datos/blackfriday/` | Dataset Black Friday local (`blkfri_train.csv`, `blkfri_test.csv`). | **Resuelto 2026-07-06**: no hay práctica activa enlazada; los CSV están ignorados por Git. | Mantener en UD4 como recurso opcional · no enlazar evaluación sin enunciado. | Hecho: añadido README; si se reactiva, preparar práctica reproducible con baseline y métricas de regresión. |
| `05-recursos/modelado-entornos/` | Entornos y scripts de instalación de frameworks. | **Resuelto 2026-07-06**: plantillas útiles pero no recetas verificadas de aula. | Mantener en UD4 como apoyo docente. | Hecho: añadido README, `set -euo pipefail`, activación robusta de conda, comillas en `keras>=3.0` y canal `nvidia` en `environment.yml`. |
| `05-recursos/captura.mp4` | Vídeo/captura sin referencia activa. | **Resuelto 2026-07-06**: no aparece enlazado desde materiales activos. | Archivar, no eliminar. | Movido a `90-archivo/recursos/captura.mp4`. |

## Pendientes en evaluación

| Ruta | Duda | Recomendación provisional |
|---|---|---|
| `04-evaluacion/rubrica.md` | **Revisada 2026-07-06**: centrada en los tres laboratorios base de UD4. | Sin cambios necesarios. |
| `04-evaluacion/cuestionario-deep-learning.gift` | **Revisado 2026-07-06**: retiradas preguntas canónicas de CNN/Transformer. | Ajustado a fundamentos, backpropagation, frameworks, regularización y arquitecturas puente. |
| `04-evaluacion/checklist-entrega.md` | **Revisado 2026-07-06**: mantiene sólo una nota de frontera para derivar visión/NLP a UD8/UD6. | Sin cambios necesarios. |

## Próxima decisión recomendada

Revisar primero `03-practicas/modelado-proyectos/`, porque define qué debe conservar UD4 como práctica real. Después se ajusta teoría y evaluación a esas prácticas.


## Decisiones docentes incorporadas — 2026-07-04

- `euromillones` se conserva como actividad crítica sobre límites de ML, patrones inexistentes, relaciones espurias y cambio de patrones en el tiempo.
- Los ficheros `.org` no se eliminan: pueden ser fuentes originales no migradas a Markdown.
- `LSTM`/RNN debe mantener una introducción en UD4, continuar en NLP y cerrarse en series temporales.
- `PyCaret` pertenece a AutoML; si está dentro de `used-cars`, debe separarse del bloque DL.
- `blackfriday` se conserva como recurso local opcional de regresión tabular con redes neuronales; no es práctica canónica evaluable mientras no tenga enunciado reproducible.

## Revisión específica — `used-cars` — 2026-07-04

Estado verificado:

- Tamaño local total: ~604 MB.
- Versionado en Git: sólo los 5 notebooks de `notebooks/`.
- No versionado/local:
  - `data/vehicles.zip` → contiene `vehicles.parquet` (~453 MB descomprimido).
  - `data/usedCars.zip` → contiene `vehicles.csv` (~1,45 GB descomprimido).
  - `mlruns/` → trazas pequeñas de MLflow/PyCaret (~308 KB).
  - `extras/Samoyedo.jpg` → recurso de imagen sin encaje claro en el proyecto de coches.

Clasificación provisional de notebooks:

| Notebook | Contenido detectado | Encaje recomendado |
|---|---|---|
| `keras_notebook2.ipynb` | Regresión de precio con Keras sobre `vehicles.csv`. | Mantener en UD4 como DL tabular. |
| `tf_keras_notebook.ipynb` | Lectura con PyArrow/Vaex/Parquet y modelo Keras. | Mantener en UD4 si se quiere ejemplo DL tabular con datos grandes; si no, archivar como variante pesada. |
| `pytorch_notebook.ipynb` | Regresión con PyTorch; también aparecen trazas de Keras/DEAP. | Mantener en UD4 sólo tras limpiar dependencias/confusión. |
| `vehiculoPycaret.ipynb` | AutoML con PyCaret, `setup(... target='price', log_experiment=True, experiment_name='vehicles')`. | Mover a UD3 como AutoML/tabular; `mlruns` asociado no debe quedar como práctica UD4. |
| `layersReuse.ipynb` | VGG16/ResNet50/ImageNet/transfer learning; no trata coches usados. | Mover a UD8 o archivar; no pertenece a `used-cars` ni a DL tabular. |

Decisión recomendada:

- Dividir `used-cars` en tres salidas:
  1. UD4: notebooks de regresión tabular con Keras/PyTorch, depurados.
  2. UD3: notebook PyCaret/AutoML.
  3. UD8 o archivo: `layersReuse.ipynb`, porque es transfer learning de visión.
- Mantener los ZIP de datos fuera de Git. Si se conserva la práctica, documentar origen/descarga en vez de versionar datos pesados.
- Archivar o ignorar `mlruns/`: es salida de ejecución, no material fuente docente.


## Movimiento ejecutado — `used-cars` — 2026-07-04

- Keras/PyTorch: movidos a `04-deep-learning/03-practicas/modelado-proyectos/used-cars-dl-tabular/`.
- PyCaret/AutoML: movido a `03-machine-learning/03-practicas/actividades/automl-used-cars/`.
- `layersReuse.ipynb`: movido a `08-vision-xai/03-practicas/modelado-notebooks-vision-ud4/transfer-learning/`.
- Datos grandes y `mlruns/`: no versionados; se mantienen fuera de Git.
- `Samoyedo.jpg`: movido con `layersReuse.ipynb` a UD8 como recurso de visión.

## Movimiento ejecutado — `boston-housing` — 2026-07-04

- Se mantiene en UD4 como práctica de regresión tabular con redes neuronales.
- Se archivó `nna-vs-traditional.ipynb` porque realmente era Iris/clasificación, no Boston Housing.
- Se añadió `README.md` y se ajustaron los scripts para leer `data/housing.csv` mediante ruta relativa.
- `boston-housing/data/housing.csv`: se versiona explícitamente por ser pequeño y necesario para reproducibilidad.

## Auditoría específica — `boston-housing` — 2026-07-06

Estado verificado sin ejecutar entrenamiento:

- `data/housing.csv` pesa ~49 KB, contiene 506 filas y queda permitido por excepción explícita en `.gitignore`.
- Los cuatro scripts cargan el CSV con ruta relativa robusta basada en `Path(__file__)`.
- `nna-vs-traditional.ipynb` ya no forma parte del flujo activo porque era Iris/clasificación.
- El README queda ampliado con objetivo docente, materiales incluidos, reproducibilidad, métricas esperadas, advertencia ética y deuda técnica.

Decisión:

- `boston-housing` se mantiene en UD4 como práctica de regresión tabular con redes neuronales.
- El saneamiento documental queda cerrado.
- No se marca como práctica evaluable canónica hasta corregir baseline, escalado antes del split, métricas en unidades originales y tratamiento de variables problemáticas del dataset.

Pendiente posterior:

- Si se va a usar con alumnado, preparar una versión metodológicamente limpia: split antes de escalar, baseline, MAE/RMSE/R² en unidades originales y reflexión ética explícita.

## Revisión específica — `house-prices-kaggle` — 2026-07-04

Estado verificado:

- Tamaño local total: ~69 MB.
- Versionado en Git: sólo `docs/conceptos.org`, `docs/rubrica.md` y los tres notebooks.
- Datos locales no versionados:
  - Kaggle House Prices: `train.csv`, `test.csv`, `sample_submission.csv`, `data_description.txt`, `house-prices-advanced-regression-techniques.zip`.
  - Datasets ajenos al proyecto: `winemag-data-130k-v2.csv`, `winemag-data-130k-v2.csv.zip`, `flavors_of_cacao.csv`.

Clasificación provisional:

| Elemento | Contenido detectado | Encaje recomendado |
|---|---|---|
| `notebooks/house_prices_advanced_regression2.ipynb` | EDA, pipelines y ML clásico sobre Kaggle House Prices; referencias a XGBoost/CatBoost/Random Forest, sin deep learning real. | Mover a UD3 como actividad de ML tabular/pipelines. |
| `notebooks/house_prices_advanced_regresionR.ipynb` | Notebook R incompleto; mezcla House Prices con `flavors_of_cacao.csv`. | Archivar o mover a material histórico, no activo. |
| `notebooks/prueba.ipynb` | Ejercicios básicos de pandas con datos de vino; no es House Prices. | Archivar o descartar como prueba. |
| `docs/conceptos.org` | Apuntes de estadística/preprocesado en Org, con origen de conversación Bing. | Conservar como fuente histórica o apoyo UD3; no eliminar por ser `.org`. |
| `docs/rubrica.md` | Rúbrica genérica de selección, entrenamiento y evaluación de modelos. | Puede moverse a UD3 o servir como base, pero habría que normalizarla. |
| `docs/rubricaSelecEntrenModel.odt` | ODT local no versionado. | Archivo/histórico si se conserva. |
| `data/winemag-*`, `data/flavors_of_cacao.csv` | Datasets ajenos a House Prices. | Sacar de este proyecto; no versionar. |

Decisión recomendada:

- Mover a UD3 sólo el núcleo útil: `house_prices_advanced_regression2.ipynb`, `docs/rubrica.md`, quizá `docs/conceptos.org` como apoyo histórico.
- Archivar `house_prices_advanced_regresionR.ipynb` y `prueba.ipynb` porque mezclan R/pandas/datasets ajenos.
- Mantener los datos grandes/no esenciales fuera de Git. Para Kaggle House Prices, decidir si se versionan `train.csv`/`test.csv` por reproducibilidad o se deja descarga vía Moodle/Kaggle.

## Movimiento ejecutado — `house-prices-kaggle` — 2026-07-04

- Núcleo útil movido a `03-machine-learning/03-practicas/actividades/house-prices-kaggle/`.
- Notebooks ajenos/incompletos archivados en `03-machine-learning/90-archivo/house-prices-kaggle/`.
- La carpeta antigua de UD4 queda sólo con datos locales no versionados, si existen.

## Reubicación complementaria — material ajeno de `house-prices-kaggle` — 2026-07-04

- Wine Reviews movido a `02-tratamiento-datos/05-recursos/datasets/wine-reviews/`.
- Cacao Flavors movido a `02-tratamiento-datos/05-recursos/datasets/cacao-flavors/`.
- Notebook R movido a `02-tratamiento-datos/90-archivo/alternativas-R/house-prices-r/`.
- Notebook de prueba pandas/vino movido a `02-tratamiento-datos/90-archivo/pandas-wine-reviews/`.
- Pendiente posible: valorar si se amplía R en UD2 para análisis estadístico y visualización EDA.

## Pendiente transversal añadido — 2026-07-05

- **Resuelto 2026-07-06**: R queda como itinerario opcional en `02-tratamiento-datos/03-practicas/r_exercises_titanic_with_tests/`, centrado en Titanic y comparación Pandas ↔ dplyr. No sustituye el eje Python/pandas/scikit-learn.

## Revisión específica — `euromillones` — 2026-07-05

Estado verificado:

- Material versionado en Git: 4 notebooks y 3 scripts.
- Datos locales: `data/Euromillones.csv` y `data/Euromillones-result.csv`, ignorados por la regla global `*.csv`.
- El notebook principal muestra entrenamiento con LSTM y validación débil; esto refuerza el uso como caso crítico.

Decisión:

- Mantener en UD4 como actividad opcional de pensamiento crítico sobre ML.
- No presentarla como práctica de predicción real.
- Añadir `README.md` explicando límites, uso docente y advertencias.
- Si se usa en clase, distribuir los CSV por Moodle o fuente controlada, no asumir que están en Git.

Pendiente posterior:

- Si se quiere convertir en tarea evaluable, crear enunciado específico y rúbrica de reflexión metodológica, no rúbrica de acierto predictivo.

## Revisión específica — `used-cars-dl-tabular` — 2026-07-05

Estado verificado sin ejecutar notebooks:

| Notebook | Resultado de auditoría | Decisión |
|---|---|---|
| `keras_notebook2.ipynb` | Regresión tabular de precio con Keras sobre `vehicles.csv`. Es el flujo más claro. | Mantener en UD4, revisando si se usa en clase que la evaluación sea con MAE/RMSE/R² y baseline, no `accuracy`. |
| `tf_keras_notebook.ipynb` | Variante Keras con PyArrow/Vaex/Parquet para datos grandes; conserva dependencias pesadas y bloque DEAP incompleto. | Mantener como variante avanzada o material de profesor; no usar como práctica mínima sin limpieza previa. |
| `pytorch_notebook.ipynb` | Importa PyTorch, pero el desarrollo principal sigue usando patrones/código Keras y dependencias mezcladas. | Pendiente concreto: refactorizar si se quiere una práctica PyTorch real; mientras tanto no venderlo como notebook PyTorch cerrado. |

Saneamiento aplicado:

- `README.md` reescrito para fijar objetivo docente, límites, datos no versionados, notebooks incluidos y criterios mínimos de evaluación honesta.
- Se confirma que no deben versionarse datasets grandes, `mlruns/`, modelos entrenados ni resultados generados.
- El bloque queda en UD4 como práctica de regresión tabular DL, con deuda técnica acotada en notebooks.

Pendiente concreto:

- Si se va a usar en clase como práctica evaluable, preparar una versión reducida/reproducible del dataset y refactorizar `pytorch_notebook.ipynb` para que sea PyTorch real o renombrarlo/archivarlo.
