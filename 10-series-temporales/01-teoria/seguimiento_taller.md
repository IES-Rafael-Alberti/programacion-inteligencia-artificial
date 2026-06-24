# Seguimiento del Taller de Series Temporales

## Contexto

Se está preparando un taller de series temporales para el módulo de PIA. Este curso la parte de series temporales tendrá menos peso que en cursos anteriores porque se ha dedicado más tiempo a imagen, vídeo y NLP.

El material se está construyendo con ayuda del libro *Modern Time Series Forecasting with Python*, pero adaptado a un formato práctico para clase.

## Enfoque acordado

Se ha decidido usar un enfoque híbrido:

- Empezar con datos sintéticos para explicar conceptos básicos de forma controlada.
- Avanzar después hacia datos reales o semirrealistas ya preparados.
- Evitar que el taller dependa al principio de recoger datos reales desde cero, porque eso puede consumir demasiado tiempo en limpieza, APIs, formatos y errores.

La idea principal es que el alumnado entienda primero:

- Qué es una serie temporal.
- Por qué importa el orden temporal.
- Qué son tendencia, estacionalidad, ruido y ciclos.
- Cómo se preparan datos temporales.
- Cómo se visualizan y analizan antes de modelar.

## Organización prevista

El taller se desarrollará en varias sesiones:

- Primera sesión: introducción y generación de series temporales sintéticas.
- Segunda sesión: obtención, preparación y procesamiento de datos temporales.
- Tercera sesión: análisis visual, descomposición y detección de outliers.
- Sesiones posteriores: baselines, métricas, variables `lag`, medias móviles y modelos supervisados para forecasting.

La parte inicial del taller queda cerrada con los cuatro primeros documentos. A partir de ahí se abrirá un segundo bloque centrado en aprendizaje automático aplicado a series temporales.

## Documentos creados

### 1. Introducción a las series temporales

Archivo:

`01_introduccion_series_temporales.md`

Contenido principal:

- Qué es una serie temporal.
- Tipos de series temporales.
- Áreas de aplicación.
- Proceso generador de datos.
- Generación de series temporales sintéticas.
- Ruido blanco y ruido rojo.
- Señales cíclicas o estacionales.
- Señales autorregresivas.
- Mezcla de componentes.
- Series estacionarias y no estacionarias.
- Qué podemos predecir.
- Terminología básica de forecasting.
- Primera predicción baseline.
- Actividades de clase.

Nota:

El documento se creó inicialmente sin tildes por compatibilidad ASCII, pero se corrigió después a español cuidado con tildes y signos adecuados.

### 2. Obtención y procesamiento de datos

Archivo:

`02_obtencion_procesamiento_datos.md`

Contenido principal:

- Comprensión del dataset temporal.
- Preparación de un modelo de datos.
- Conversión de columnas a fechas con `pd.to_datetime`.
- Uso de `DatetimeIndex`.
- Accesor `.dt` y propiedades temporales.
- Indexación y slicing por fechas.
- Creación de secuencias temporales con `pd.date_range`.
- Tratamiento de valores perdidos.
- Conversión de datos por bloques a formato temporal.
- Formatos compacto, expandido/largo y ancho.
- Frecuencias regulares con `asfreq`.
- Remuestreo con `resample`.
- Unión de metadatos con `merge`.
- Guardado y carga de archivos CSV y Parquet.
- Tratamiento de huecos largos.
- Imputación con valor anterior.
- Perfil medio horario.
- Media horaria por día de la semana.
- Interpolación estacional.
- Actividades de clase.

### 3. Análisis y visualización de series temporales

Archivo:

`03_analisis_visualizacion_series_temporales.md`

Contenido principal:

- Componentes de una serie temporal.
- Tendencia.
- Estacionalidad.
- Ciclos.
- Componente irregular.
- Gráficos de líneas.
- Gráficos estacionales.
- Boxplots estacionales.
- Mapas de calor de calendario.
- Gráfico de autocorrelación.
- Descomposición de series temporales.
- Eliminación de tendencia.
- Medias móviles.
- LOESS.
- Eliminación de estacionalidad.
- Medias ajustadas por periodo.
- Series de Fourier.
- `seasonal_decompose`.
- STL.
- Fourier decomposition.
- MSTL.
- Detección de outliers con desviación estándar.
- Detección de outliers con IQR.
- Detección de outliers con Isolation Forest.
- ESD y S-ESD como métodos avanzados.
- Tratamiento de outliers.
- Actividades de clase.
- Referencias y lecturas recomendadas.

### 4. Baselines y evaluación de forecasting

Archivo:

`04_baselines_evaluacion_forecasting.md`

Contenido principal:

- Preparación de un entorno de evaluación.
- Separación temporal en train, validación y test.
- Métricas MAE, RMSE y MAPE.
- Predicción naive.
- Predicción por media móvil.
- Seasonal naive.
- Suavizado exponencial simple.
- Holt-Winters.
- Introducción conceptual a ARIMA.
- Theta forecast como referencia conceptual.
- TBATS como modelo avanzado para estacionalidades complejas.
- Box-Cox, Fourier, ARMA y optimización de parámetros.
- MSTL para múltiples estacionalidades.
- Evaluación conjunta de baselines.
- Evaluación final en test.
- Ideas sobre predictibilidad de una serie temporal.
- Coeficiente de variación y residuos.
- Entropía espectral y métrica de Kaboudan como conceptos avanzados.
- Actividades de clase.

## Decisiones didácticas tomadas

- Priorizar ejemplos interpretables: ventas, consumo eléctrico, visitas web.
- Usar datos sintéticos al inicio para controlar los componentes de la serie.
- Usar consumo eléctrico como hilo conductor principal de los notebooks.
- Introducir datasets reales o semirrealistas después de que el alumnado entienda los conceptos.
- Mantener los documentos en Markdown para que puedan convertirse después en apuntes, notebooks o material de aula.
- Crear un notebook por documento, en lugar de un único notebook largo.
- Crear primero generadores reutilizables y después notebooks de demostración.
- Incluir código ejecutable en Python, pero acompañado de explicación conceptual.
- Evitar modelos avanzados antes de trabajar bien visualización, limpieza, frecuencia temporal y baselines.

## Generadores y datos sintéticos

Se ha creado un módulo Python reutilizable para generar datos sintéticos de consumo eléctrico.

Archivos creados:

- `src/series_temporales/__init__.py`
- `src/series_temporales/generador_consumo.py`
- `scripts/generar_datos_demo.py`
- `requirements.txt`

El generador principal es:

`generar_consumo_electrico`

Permite generar escenarios progresivos:

- Serie básica de consumo eléctrico horario.
- Serie con meteorología simulada.
- Serie con eventos simulados.
- Serie realista con huecos y outliers.

Componentes incluidos en la serie básica:

- Tendencia suave.
- Patrón diario.
- Efecto de fin de semana.
- Estacionalidad anual suave.
- Ruido aleatorio.

Variables contextuales opcionales:

- Temperatura simulada.
- Festivos simulados.
- Campaña especial simulada.
- Ola de calor simulada.

Problemas de datos opcionales:

- Valores perdidos aislados.
- Hueco temporal más largo.
- Outliers positivos y negativos.

CSV generados en la carpeta `datos/`:

- `consumo_basico.csv`
- `consumo_con_meteo.csv`
- `consumo_con_eventos.csv`
- `consumo_realista.csv`

Validación realizada:

- Se instaló el entorno mínimo desde `requirements.txt`.
- Se ejecutó `PYTHONPATH="src" python "scripts/generar_datos_demo.py"`.
- Se generaron correctamente cuatro CSV de 4320 filas cada uno.
- Se corrigió la frecuencia horaria de `H` a `h` para evitar avisos de pandas.

Nota de entorno:

- El entorno previsto para clase es el entorno conda/mamba `pia-ud1`.
- Conviene instalar ahí las dependencias del fichero `requirements.txt`.
- Si el entorno local da problemas de versiones, se valorará usar Google Colab.

## Próximos pasos sugeridos

- Preparar notebooks separados a partir de los documentos Markdown.
- Crear primero el notebook `01_introduccion_series_temporales.ipynb` usando `consumo_basico.csv`.
- Crear después el notebook `02_obtencion_procesamiento_datos.ipynb` usando `consumo_realista.csv`.
- Decidir si se usará un dataset real concreto en la última parte del taller.

## Bloque posterior pendiente

Cuando se retome el taller después de la parte inicial, el siguiente bloque será aprendizaje automático para series temporales.

Orden previsto:

- Primero, aprendizaje automático clásico.
- Después, redes neuronales.

Temas previstos para aprendizaje automático clásico:

- Transformar una serie temporal en un problema supervisado.
- Crear variables `lag`.
- Crear medias móviles y variables agregadas por ventana.
- Añadir variables de calendario.
- Añadir variables externas como temperatura y eventos simulados.
- Evitar fugas de información temporal.
- Entrenar modelos como `LinearRegression`, `RandomForestRegressor`, `GradientBoostingRegressor` o modelos equivalentes.
- Comparar modelos de ML contra los baselines del documento 4.

Temas previstos para redes neuronales:

- Preparar ventanas de entrada y salida.
- Modelos densos sencillos.
- Modelos recurrentes como RNN, GRU o LSTM si encajan con el tiempo disponible.
- Modelos 1D CNN para secuencias si se considera conveniente.
- Comparación realista frente a baselines y ML clásico.

Decisión didáctica:

- No pasar a redes neuronales hasta que el alumnado haya entendido bien baselines, métricas, separación temporal y construcción de variables supervisadas.

## Refactorización Pedagógica (Sesiones 02 a 06)

Tras una auditoría del material, se identificó que las sesiones 02 a 06 pecaban de ser excesivamente técnicas y carecían de un "alma" didáctica. Se ha procedido a una **Reescritura Total** de estos documentos para alinearlos con la altísima calidad narrativa de la Sesión 01.

Mejoras clave introducidas:
- **Sesión 02 (Procesamiento):** Se ha explicado profundamente el peligro de los "huecos silenciosos" y la filosofía detrás de la imputación (interpolar vs perfil medio).
- **Sesión 03 (Visualización):** Se han introducido analogías del mundo real (el océano, las mareas) para explicar Tendencia y Estacionalidad, y el concepto del "Eco" para la Autocorrelación.
- **Sesión 04 (Baselines y Evaluación):** Se ha atacado el *Data Leakage*, explicando por qué `train_test_split` es un pecado capital en forecasting temporal, y se ha dado contexto de negocio a las métricas (MAE vs RMSE).
- **Sesión 05 (Forecasting como Regresión):** Se ha visualizado el cambio de paradigma de 1D a 2D y se han creado actividades "trampa" donde el alumno comete fugas de información a propósito usando `rolling` sin `shift`.
- **Sesión 06 (Feature Engineering):** Se ha incorporado la distinción entre media simple y EWMA, y se ha introducido la trigonometría temporal (Seno/Coseno) para modelar los ciclos continuos de horas y días.

### Paridad funcional (Markdown y Jupyter)
Los archivos `.md` actúan como apuntes completos y los `.ipynb` como versión ejecutable de clase. No son copias literales: los notebooks priorizan celdas ejecutables, ejemplos autocontenidos y comprobaciones prácticas.

Correcciones incorporadas posteriormente:
- Imports robustos a `src` desde el directorio del taller.
- Notebooks avanzados autocontenidos para `TimeSeriesDataset` y datos de ejemplo.
- Corrección de variables no definidas en sesiones 02, 07, 08, 09 y 10.
- Añadido backtesting, intervalos empíricos de incertidumbre, multi-horizonte, escalado sin fuga de información y coste-beneficio.
- Añadido `HistGradientBoostingRegressor` como extensión tabular fuerte sin dependencias externas, con mención opcional a XGBoost, LightGBM y CatBoost.
- Actualizadas las presentaciones de apoyo para reflejar backtesting/incertidumbre, modelos tabulares fuertes, multi-horizonte, escalado sin leakage y coste-beneficio.
- Actualizado `requirements.txt` para incluir `torch` y `pytorch-lightning`, necesarios en las sesiones 07-10.

## Bloque de Deep Learning y Modelos Avanzados (Sesiones 07 a 09)

Se ha estructurado un bloque completo de Deep Learning que cubre desde los fundamentos hasta el estado del arte y sus críticas. Los tres documentos fueron reescritos completamente para igualar la calidad narrativa y pedagógica de las sesiones 01-06, con objetivos explícitos, requisitos técnicos, preguntas de discusión y actividades de clase.

### Sesión 07: Introducción al Deep Learning y Modelos Globales
Archivos: `07_deep_learning_intro.md` / `.ipynb` / `presentaciones/07_dl_intro_slides.md`
- Narrativa de apertura: Analogía del "Médico de Pueblo" vs "Hospital de Referencia" (Cross-Learning).
- Gimnasia Tensorial: Explicación detallada de tensores `[Batch, Sequence, Features]` con analogía del "mazo de cartas".
- Implementación completa de `TimeSeriesDataset` de PyTorch con comentarios didácticos.
- MLP vs LSTM: Contraste práctico entre "amnesia temporal" y "memoria a largo plazo".
- Evaluación comparativa LSTM vs Seasonal Naive con código completo.
- Tres actividades: Autopsia del Tensor, MLP vs LSTM, Efecto del `window_size`.

### Sesión 08: Redes Convolucionales Temporales (TCN)
Archivos: `08_redes_convolucionales_tcn.md` / `.ipynb` / `presentaciones/08_tcn_slides.md`
- Narrativa: El precio del procesamiento secuencial y el paralelismo de las GPU.
- Convolución 1D como "lupa deslizante" sobre la señal temporal.
- Causalidad: Padding al inicio para evitar mirar al futuro.
- Convoluciones Dilatadas con diagrama textual y crecimiento exponencial del campo receptivo.
- Función `calcular_campo_receptivo` con tabla de capas vs días.
- Implementación `TCNBlock` y `TCNForecaster` con conexiones residuales y dropout.
- Tabla comparativa TCN vs LSTM.
- Tres actividades: Campo receptivo, Benchmark de velocidad, Diseño para Renfe.

### Sesión 09: Transformers y el Debate de la Atención
Archivos: `09_transformers_series_temporales.md` / `.ipynb` / `presentaciones/09_transformers_slides.md`
- Narrativa crítica: Paper "Attention is All You Need" (2017) vs "Are Transformers Effective?" (2023).
- Explicación de Self-Attention (Q-K-V) con analogía de la ambigüedad de "banco".
- El problema del tokenismo punto a punto en series temporales.
- Implementación completa de DLinear (MovingAvgDecomposition + dos capas lineales).
- PatchTST: Explicación visual del parcheo con función `crear_parches`.
- Foundation Models: TimeGPT, Lag-Llama, Moirai, Chronos, con limitaciones prácticas.
- Experimento comparativo: Baseline vs DLinear vs LSTM vs TCN.
- Tres actividades: DLinear vs Naive, Visualización de la Matriz de Atención, Debate en clase.

## Cierre del Taller: Sesión 10 (Proyecto Final - Capstone Project)

El proyecto fue rediseñado como un Capstone integrador con narrativa profesional completa.

Archivo: `10_proyecto_final.md` / `.ipynb` / `presentaciones/10_proyecto_final_slides.md`

Contenido principal:
- **Parte 1 (Guiada - Retail):** Fusión ventas diarias + tráfico peatonal horario. Debate de negocio sobre los domingos cerrados.
- **Parte 2 (Reto Autónomo - Energía):** Downsampling de clima horario a 15 min. Dilema del apagón (NaN ≠ sensor roto).
- **Parte 3 (Torneo de Modelos):** Seasonal Naive vs Random Forest vs LSTM/TCN, con tabla de MAE.
- **Reflexión Crítica:** Cuatro preguntas obligatorias sobre complejidad, coste y explicabilidad.

## Presentaciones (Marp)

Se han generado 10 presentaciones en formato Marp en la carpeta `presentaciones/`. Cada una tiene un color de acento diferente en el título para que los alumnos perciban el avance visual. Las diapositivas de las sesiones 07-10 han sido reescritas con mayor detalle y tablas comparativas.

## Estado del Entorno de Desarrollo (`pia-ud1`)

- `torch` y `pytorch-lightning` instalados vía `pip` (no conda-forge, para evitar conflictos NVIDIA).
- `jupytext` para la paridad `.md` ↔ `.ipynb`.
- Datos sintéticos generados con `src/series_temporales/generador_consumo.py`.

## Auditoría final de ejecutabilidad y completitud

Se realizó una revisión posterior de los Markdown, notebooks, presentaciones y datasets del taller. Resultado general: el taller queda completo a nivel conceptual y práctico para impartirse, con una salvedad operativa en el bloque de Deep Learning: necesita que el entorno tenga instalados `torch` y `pytorch-lightning`.

Correcciones técnicas aplicadas:
- `sys.path.append("../src")` se sustituyó por `sys.path.append("src")` en los materiales que importan `series_temporales`.
- Sesión 02: el ejemplo de `merge` con `df_lecturas` dejó de ser conceptual incompleto y ahora define un DataFrame mínimo ejecutable.
- Sesión 04: `rmse` usa `np.sqrt(mean_squared_error(...))`, evitando incompatibilidades con versiones de `scikit-learn` donde `squared=False` no esté disponible.
- Sesión 05: los ejemplos introductorios de `lag` y `rolling` usan `df_ejemplo`, evitando depender de un `df` aún no cargado.
- Sesión 06: al añadir targets multi-horizonte (`y_t+1`, `y_t+6`, `y_t+24`), se corrigió la selección de `features_todas` para excluir cualquier columna objetivo futura y evitar leakage accidental.
- Sesión 07: se genera la temperatura con `incluir_meteorologia=True`, se añade `StandardScaler` ajustado solo sobre train y se evalúa el baseline en la misma escala.
- Sesión 08: el notebook incluye su propia clase `TimeSeriesDataset` y prepara `train_loader`/`val_loader`, por lo que ya no depende de haber ejecutado antes la sesión 07.
- Sesión 09: el notebook incluye `TimeSeriesDataset`, por lo que DLinear puede ejecutarse de forma autocontenida.
- Sesión 10: se define `TimeSeriesDataset`, se inicializa `mae_dl = np.nan` para que la tabla final no falle si no se entrena LSTM/TCN, y se mide el tiempo de entrenamiento de Random Forest.

Añadidos metodológicos aplicados:
- Sesión 04: backtesting/walk-forward y primer intervalo empírico de incertidumbre basado en residuos.
- Sesión 05: `HistGradientBoostingRegressor` como modelo tabular fuerte incluido en `scikit-learn`; XGBoost, LightGBM y CatBoost quedan como nota avanzada opcional.
- Sesión 06: estrategias multi-horizonte (`recursive`, `direct`, `multi-output`) y advertencia específica de leakage para horizontes largos.
- Sesión 07: escalado de features sin fuga de información.
- Sesión 10: reflexión coste-beneficio, incluyendo tiempo de entrenamiento, mantenimiento, explicabilidad y mejora real frente al baseline.

Verificaciones realizadas:
- Todos los notebooks modificados son JSON válido.
- Todas las celdas de código de los notebooks compilan sintácticamente.
- El import `from series_temporales import generar_consumo_electrico` funciona desde el directorio del taller usando `sys.path.append("src")`.
- Ejecutados correctamente de forma completa los notebooks no neuronales modificados: `02_obtencion_procesamiento_datos.ipynb`, `04_baselines_evaluacion_forecasting.ipynb`, `05_forecasting_como_regresion.ipynb` y `06_feature_engineering_series_temporales.ipynb`.
- Comprobado que no quedan placeholders críticos como `WINDOW_SIZE = ...`, `modelo = ...`, `from sesion_07` ni imports antiguos a `../src`.
- Verificación final en `pia-ud1`: los 10 notebooks (`01` a `10`) ejecutan completos con `jupyter nbconvert --execute`, guardando las salidas de comprobación fuera del material de clase en `/tmp/opencode/series_temporales_nbcheck`.
- Sesión 10: se sustituyeron los placeholders ejecutables `df_consumo = ...` y `df_clima = ...` por una carga real de `consumo_energia_15min.csv` y `clima_horario.csv`; también se añadió la construcción completa de `df_ml` con `lag_96`, `lag_672`, calendario y temperatura para que el torneo final sea ejecutable de principio a fin.
- Sesiones 07-09: los entrenadores de PyTorch Lightning se configuraron con `logger=False` y `enable_checkpointing=False`, suficiente para clase y evita cargar integraciones auxiliares que disparaban avisos de TensorFlow/TensorBoard.

Resultados de prueba observados:
- En sesión 05, `HistGradientBoostingRegressor` quedó operativo y obtuvo un MAE de validación ligeramente mejor que Random Forest en la ejecución de prueba: `0.0866` frente a `0.0871`.
- En sesión 06, tras corregir la exclusión de targets futuros, la comparación final quedó sin leakage aparente: reloj `0.1293`, medias/EWMA `0.0910`, todas las features legales `0.0827`.

Pendiente por comprobar antes de impartir:
- Decidir si en clase se ejecutan las celdas de entrenamiento profundo completas o si se reducen épocas (`max_epochs`) para ajustarse al tiempo disponible.
- Si se regeneran notebooks automáticamente en el futuro, revisar o actualizar `scripts/crear_notebooks_taller.py`, porque el material actual ya contiene cambios manuales posteriores y el script histórico no representa todo el estado actual de las sesiones 06-10.

Avisos de entorno observados:
- `TqdmWarning: IProgress not found`: no es un error del taller. Indica que Jupyter no encuentra widgets de progreso interactivos. Se añadió `ipywidgets` a `requirements.txt`; si aparece en `pia-ud1`, reinstalar/actualizar con `pip install ipywidgets` o `mamba install ipywidgets`.
- Mensaje de migración de caché de `transformers`: es una operación única de la librería al detectar una caché antigua. No afecta al material y normalmente desaparece tras la primera ejecución.
- Avisos de TensorFlow sobre registro duplicado de `cuFFT`, `cuDNN` o `cuBLAS`: no indicaban que PyTorch estuviera fallando; Lightning usaba CUDA correctamente. Como el taller no usa TensorFlow, se añadió en las sesiones 07-10 una celda inicial con `USE_TF=0`, `TF_CPP_MIN_LOG_LEVEL=2` y `LIGHTNING_DISABLE_TIPS=1`; además, en las sesiones 07-09 se desactivaron logger y checkpoint automático de Lightning. Tras este cambio, las sesiones 07-09 ejecutan con `nbconvert` sin esos avisos de TensorFlow.

Tarea para la próxima sesión:
- Revisar el entorno `pia-ud1` antes de ejecutar los notebooks de Deep Learning.
- Instalar o actualizar `ipywidgets` si vuelve a aparecer `TqdmWarning: IProgress not found`.
- Reiniciar el kernel de Jupyter después de instalar `ipywidgets`.
- Ejecutar una celda mínima de importación (`torch`, `pytorch_lightning`, `tqdm`, `series_temporales`) para confirmar que los avisos no bloquean la clase.
- Si aparece la migración de caché de `transformers`, dejar que termine una vez; no requiere cambios en el código del taller.
