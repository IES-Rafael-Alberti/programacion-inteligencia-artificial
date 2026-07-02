# Evaluación — UD10 Series Temporales

Esta carpeta reúne los instrumentos para evaluar la unidad de series temporales y forecasting. El cuestionario GIFT cubre comprensión teórica de los 10 temas del taller; la entrega principal evalúa el proyecto final capstone (sesión 10) mediante rúbrica y checklist.

## Camino rápido

1. Completa el proyecto final siguiendo la guía de `01-teoria/10_proyecto_final.md`.
2. Entrega el notebook y las evidencias siguiendo `checklist-entrega.md`.
3. Revisa la calificación esperada con `rubrica.md`.
4. Realiza el cuestionario GIFT si el profesorado lo activa en Moodle.

## Qué se evalúa

| Bloque | Evidencia esperada |
| --- | --- |
| Fusión y preprocesado de fuentes | Código correcto de resample, merge y tratamiento de NaNs con criterio de negocio. |
| Partición temporal sin data leakage | División de datos en train/val/test respetando la flecha del tiempo. |
| Baseline y métricas | Al menos un baseline (Naive o Seasonal Naive) calculado con MAE, RMSE y/o MAPE. |
| Modelo avanzado | Implementación y entrenamiento de un modelo de DL (LSTM, TCN o Transformer) o de ML (RF, XGBoost). |
| Comparativa de modelos (Torneo) | Tabla comparativa de al menos dos modelos con métricas sobre el mismo conjunto de test. |
| Análisis e interpretación | Comentario razonado sobre qué modelo gana, por qué y cuáles son sus limitaciones. |
| Documentación y reproducibilidad | Notebook ordenado y ejecutable con instrucciones claras. |

## Evidencias de entrega

- Notebook del proyecto final completado con salidas visibles.
- Tabla comparativa de modelos con métricas calculadas sobre el mismo conjunto de test.
- Al menos una visualización: predicción vs. valores reales sobre el horizonte de test.
- Breve análisis del ganador del Torneo y sus limitaciones.
- Instrucciones de ejecución y dependencias si son necesarias.

No se deben entregar claves API, tokens, credenciales ni datos sensibles.

## Relación con notebooks y teoría

La entrega se basa en el notebook `02-ejemplos/10_proyecto_final.ipynb` y la guía `01-teoria/10_proyecto_final.md`, que describen tres fases:

1. **Parte guiada (Retail):** fusión de ventas diarias y tráfico peatonal horario.
2. **Reto autónomo (Energía):** fusión con downsampling — el alumno decide cómo agregar.
3. **El Torneo:** competición de modelos con tabla comparativa final.

Los modelos trabajados a lo largo del taller y candidatos al Torneo son:
- Baselines: Naive, Seasonal Naive, Exponential Smoothing.
- ML: Random Forest, XGBoost (forecasting como regresión).
- DL: LSTM, TCN, Transformer simplificado.

## Cuestionario disponible

- `cuestionario_series_temporales.gift`: preguntas conceptuales sobre los 10 temas del taller (componentes, estacionariedad, métricas, data leakage, modelos DL, etc.).

Sirve para comprobar comprensión teórica y preparar la corrección. No sustituye automáticamente a la rúbrica práctica salvo decisión expresa del profesorado.

## Criterios de superación

- La entrega alcanza al menos 5 sobre 10 en la rúbrica.
- El notebook ejecuta el flujo principal con salidas verificables.
- La tabla comparativa incluye al menos dos modelos distintos con métricas calculadas sobre el mismo test.
- La solución está documentada para que otra persona pueda revisarla.
