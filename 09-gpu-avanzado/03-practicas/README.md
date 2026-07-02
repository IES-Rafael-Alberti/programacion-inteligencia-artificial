# Prácticas — UD9: GPU Avanzado

## Visión general

Las tres prácticas de esta unidad forman un **proyecto integrador**: construir un sistema completo de ML desde el EDA hasta el despliegue, usando aceleración GPU donde corresponda.

Se trabaja con los tres notebooks plantilla. Cada uno es una pieza del mismo proyecto: los datos y artefactos que genera uno los consume el siguiente.

---

## Práctica 1 — Proyecto GPU: EDA, modelado y benchmarking

**Notebook**: `01_project_template.ipynb`
**Duración estimada**: 3–4 horas

### Contexto

Partirás de un dataset tabular sintético (incluido en el notebook). El objetivo es aplicar un flujo completo de ciencia de datos **acelerado en GPU** y compararlo cuantitativamente con la versión en CPU.

### Tareas obligatorias

1. **EDA con cuDF**
   - Carga el dataset con `cudf.read_csv` (o genera el sintético con cuDF).
   - Calcula estadísticas descriptivas (media, desviación, percentiles) por grupos.
   - Identifica y gestiona valores nulos.

2. **Feature engineering en GPU**
   - Aplica al menos 2 transformaciones sobre columnas (normalización, encoding, binning).
   - Mantén los datos en GPU durante todo el proceso (evita `.to_pandas()` innecesarios).

3. **Entrenamiento con cuML**
   - Entrena un modelo de clasificación o regresión con cuML.
   - Compara con el equivalente de scikit-learn en CPU.
   - Reporta accuracy o RMSE de ambos.

4. **Benchmark CPU vs GPU**
   - Mide el tiempo total de EDA + entrenamiento en CPU y GPU.
   - Usa `time.perf_counter` con warmup previo.
   - Escribe un párrafo de análisis: ¿cuánto se acelera? ¿qué lo limita?

### Entregables

- Notebook ejecutado de principio a fin sin errores.
- `artifacts/model.joblib` — modelo cuML guardado.
- `artifacts/metrics.json` — métricas del modelo (al menos accuracy/RMSE y tiempos).
- `artifacts/clean.csv` — dataset procesado listo para los pasos siguientes.
- Análisis escrito en la última celda (markdown) con conclusiones del benchmark.

---

## Práctica 2 — Dashboard de demostración

**Notebook**: `02_dashboard_template.ipynb`
**Duración estimada**: 2–3 horas

### Contexto

Construirás un dashboard interactivo con **Gradio** (o Streamlit) que permita demostrar el modelo entrenado en la Práctica 1 sin modificar código.

### Tareas obligatorias

1. **Carga del modelo**
   - Carga `artifacts/model.joblib` al inicio del notebook.
   - Verifica que el modelo carga sin errores antes de construir la UI.

2. **Interfaz de predicción**
   - Al menos 3 controles de entrada (sliders, dropdowns o text inputs) que correspondan a features del modelo.
   - Un botón o evento que lance la predicción.
   - Muestra el resultado de forma clara (etiqueta, valor numérico, o gráfico).

3. **Panel de métricas**
   - Carga y muestra `artifacts/metrics.json` en el dashboard (tabla o cards con accuracy, RMSE, tiempos).

4. **Visualización adicional** (elige una)
   - Distribución de predicciones sobre el dataset de test.
   - Curva ROC o Precision-Recall si es clasificación.
   - Importancia de features si el modelo lo soporta.

### Entregables

- Notebook ejecutado con el dashboard visible en la última celda.
- Instrucciones en el README para lanzar el dashboard (`gr.launch()` o `st.run()`).
- El dashboard debe funcionar con los artefactos de la Práctica 1.

---

## Práctica 3 — Pipeline de orquestación

**Notebook**: `03_pipeline_template.ipynb`
**Duración estimada**: 3–4 horas

### Contexto

Convertirás el flujo de las Prácticas 1 y 2 en un **pipeline reproducible** usando Prefect (o Python puro estructurado en funciones). El objetivo es que cualquier persona pueda ejecutar el pipeline completo con un solo comando.

### Tareas obligatorias

1. **Definición de tasks**
   Encapsula cada paso en un task bien nombrado:
   - `task_ingest`: lectura y validación de datos.
   - `task_transform`: feature engineering.
   - `task_train`: entrenamiento y evaluación.
   - `task_save_artifacts`: guardado de `model.joblib`, `metrics.json`, `clean.csv`.

2. **Parametrización**
   - Ninguna ruta ni hiperparámetro puede estar hardcodeado dentro de un task.
   - Usa un diccionario de configuración o parámetros del flow.

3. **Logs**
   - Cada task debe loggear al menos: inicio, fin y resultado clave (p. ej., accuracy obtenida).
   - Usar `print` con formato estructurado es suficiente; Prefect logging es bonus.

4. **Ejecución completa**
   - El pipeline debe ejecutarse de principio a fin en la última celda con `flow.run()` o equivalente.
   - Al finalizar, los artefactos deben estar en `artifacts/` (mismos que Práctica 1).

5. **Manejo básico de errores**
   - Si un task falla (archivo no encontrado, NaN inesperado), el pipeline debe mostrar un error claro, no un traceback críptico.

### Entregables

- Notebook ejecutado con la salida del flow visible.
- `artifacts/` completado tras la ejecución del pipeline.
- README actualizado con el comando para ejecutar el pipeline.

---

## Estructura de artefactos esperada

```
artifacts/
├── clean.csv          ← datos procesados por la Práctica 1
├── metrics.json       ← {"accuracy": 0.87, "rmse": null, "tiempo_gpu_ms": 320, "tiempo_cpu_ms": 4100}
└── model.joblib       ← modelo cuML serializado
```

---

## Criterios de evaluación

Ver [`../04-evaluacion/rubrica.md`](../04-evaluacion/rubrica.md) para la rúbrica completa.
Ver [`../04-evaluacion/checklist-entrega.md`](../04-evaluacion/checklist-entrega.md) para la lista de verificación.

---

## Recursos de apoyo

- Teoría: [`../01-teoria/01-rapids-cudf-cuml.md`](../01-teoria/01-rapids-cudf-cuml.md)
- Teoría: [`../01-teoria/03-benchmarks-optimizacion-gpu.md`](../01-teoria/03-benchmarks-optimizacion-gpu.md)
- Guía orquestación: [`../02-ejemplos/00-guia-ejemplos.md`](../02-ejemplos/00-guia-ejemplos.md)
- Plantilla informe: [`../05-recursos/plantilla-informe.md`](../05-recursos/plantilla-informe.md)
- Plantilla autoevaluación: [`../05-recursos/plantilla-autoevaluacion.md`](../05-recursos/plantilla-autoevaluacion.md)
