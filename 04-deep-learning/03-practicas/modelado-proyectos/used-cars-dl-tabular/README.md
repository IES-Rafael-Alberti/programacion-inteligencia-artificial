# Used Cars — regresión tabular con redes neuronales

Práctica de UD4 para revisar regresión de precio de vehículos usados con redes neuronales sobre datos tabulares. Se conserva aquí sólo la parte Keras/PyTorch del antiguo proyecto `used-cars`; AutoML/PyCaret se movió a UD3 y transfer learning de visión se movió a UD8.

## Objetivo docente

- Entrenar una red neuronal para una tarea de **regresión tabular**: estimar el precio de un vehículo usado.
- Comparar el flujo de trabajo con Keras/TensorFlow y PyTorch.
- Trabajar críticamente con limpieza de datos, partición entrenamiento/prueba, escalado, métricas de error y reproducibilidad.
- Detectar límites del enfoque: no basta con lanzar una red neuronal; hay que justificar baseline, variables, errores y posible fuga de datos.

## Notebooks incluidos

| Notebook | Encaje docente | Observaciones |
|---|---|---|
| `notebooks/keras_notebook2.ipynb` | Ejemplo principal de Keras sobre `vehicles.csv`. | Es el notebook más claro del bloque. Requiere revisar la celda de gráficas: en regresión no debe tratarse la `accuracy` como métrica principal. |
| `notebooks/tf_keras_notebook.ipynb` | Variante Keras/TensorFlow con lectura de datos grandes (`vehicles.csv` / `vehicles.parquet`). | Usa PyArrow/Vaex y deja un bloque de ajuste con DEAP incompleto. Debe tratarse como variante avanzada, no como flujo mínimo. |
| `notebooks/pytorch_notebook.ipynb` | Pendiente de refactor si se quiere una práctica real de PyTorch. | Aunque importa `torch`, el cuerpo conserva código Keras y dependencias mezcladas. No debe presentarse como notebook PyTorch acabado. |

## Datos y artefactos no versionados

Los datos grandes no se guardan en Git.

- `vehicles.csv`, `vehicles.parquet` o ZIP equivalentes deben distribuirse por Moodle, Kaggle u otra fuente controlada por el profesorado.
- `mlruns/`, modelos entrenados (`*.h5`, checkpoints) y salidas de ejecución son artefactos generados: no deben versionarse como material fuente.
- Si se ejecuta una práctica, el alumnado debe documentar de dónde salen los datos y qué versión o muestra se ha usado.

## Prerrequisitos y limitaciones

- Entorno Python con pandas, NumPy, scikit-learn y, según notebook, Keras/TensorFlow, PyArrow/Vaex o PyTorch.
- No instalar dependencias desde el notebook sin verificar antes el entorno del curso.
- Los notebooks no se han reejecutado durante este saneamiento para evitar procesos pesados y dependencias locales.
- El dataset original es grande: si se usa en clase, conviene preparar una muestra reproducible o un fichero reducido.

## Criterios mínimos de evaluación técnica

Antes de aceptar resultados como válidos, el informe o notebook entregado debe demostrar:

1. **Baseline**: comparación con una predicción sencilla, por ejemplo media/mediana o regresión lineal básica.
2. **Split correcto**: separación entrenamiento/validación/prueba antes de ajustar escaladores o transformaciones aprendidas.
3. **Sin leakage evidente**: revisión de columnas que puedan revelar directamente el precio o información posterior a la publicación.
4. **Métricas de regresión**: MAE, RMSE y/o R²; no usar accuracy como métrica principal.
5. **Reproducibilidad**: semilla, versión/muestra de datos, columnas usadas y parámetros principales.
6. **Análisis de errores**: ejemplos de fallos, outliers y límites del modelo.
7. **Conclusión honesta**: explicar si la red neuronal mejora realmente el baseline y qué coste/beneficio tiene frente a modelos tabulares clásicos.

## Qué NO hacer

- No subir datasets pesados, ZIPs, `mlruns/`, modelos entrenados ni checkpoints al repositorio.
- No presentar métricas aisladas como “verdad absoluta” sin baseline ni análisis de error.
- No mezclar AutoML/PyCaret o visión dentro de esta carpeta: esos bloques ya tienen su unidad correspondiente.
- No vender la práctica como predicción fiable de mercado sin validar sesgos, leakage, cobertura de datos y calidad del split.

## Estado de saneamiento

Auditoría documental cerrada el 2026-07-05. El bloque queda en UD4 como práctica de regresión tabular con redes neuronales, pero con una advertencia importante: `pytorch_notebook.ipynb` necesita refactor técnico si se quiere usar como práctica PyTorch real, y `tf_keras_notebook.ipynb` debe tratarse como variante avanzada/incompleta por sus dependencias y bloque DEAP.
