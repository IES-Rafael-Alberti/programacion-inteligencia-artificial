# Rúbrica — UD10 Series Temporales

Rúbrica sobre 10 puntos para el proyecto final capstone (sesión 10: Torneo de Modelos). Cubre las tres fases del proyecto: caso guiado Retail, reto autónomo Energía y comparativa final de modelos.

## Escala de desempeño

| Nivel | Referencia |
| --- | --- |
| Insuficiente | No cumple el criterio o no hay evidencia verificable. |
| Básico | Cumple parcialmente, con errores técnicos o sin justificación suficiente. |
| Adecuado | Cumple de forma correcta y revisable. |
| Excelente | Cumple con solidez, razonamiento técnico claro y análisis bien argumentado. |

## Criterios

| Criterio | Peso |
| --- | ---: |
| 1. Fusión y preprocesado de fuentes heterogéneas | 1,5 |
| 2. Partición temporal y prevención de data leakage | 1,5 |
| 3. Baseline y métricas de evaluación | 1,5 |
| 4. Modelo avanzado | 2,0 |
| 5. Tabla comparativa del Torneo | 1,5 |
| 6. Análisis e interpretación de resultados | 1,0 |
| 7. Documentación y reproducibilidad | 1,0 |
| **Total** | **10,0** |

---

## 1. Fusión y preprocesado de fuentes heterogéneas — 1,5 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No se fusionan las fuentes o el merge produce un DataFrame con NaNs masivos sin explicación. |
| Básico | Se intenta la fusión pero sin resample correcto o sin tratar los NaNs con criterio de negocio. |
| Adecuado | Las fuentes se agregan a la misma frecuencia temporal, se fusionan correctamente y los NaNs se tratan con regla de negocio justificada (p. ej. ventas de domingo = 0). |
| Excelente | Se aborda también el reto autónomo de Energía con decisión razonada sobre la granularidad de agregación y comparación con alternativas. |

**Indicadores técnicos:** uso correcto de `resample()`, `merge()` con índice temporal, distinción entre NaN estructural (domingo cerrado) y NaN por fallo de sensor.

---

## 2. Partición temporal y prevención de data leakage — 1,5 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | Se usa `train_test_split` aleatorio o no se separa train/test en ningún momento. |
| Básico | Se divide temporalmente, pero el conjunto de validación o test se solapa con train, o se aplican transformaciones ajustadas sobre todo el dataset. |
| Adecuado | Train, validación y test están separados respetando la flecha del tiempo. Los escaladores y pipelines se ajustan solo sobre train y se transforman val/test. |
| Excelente | Se razona explícitamente por qué `train_test_split` aleatorio arruina los modelos de forecasting y se demuestra que los features con lag no introducen fugas. |

---

## 3. Baseline y métricas de evaluación — 1,5 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No se calcula ningún baseline o se calculan métricas equivocadas. |
| Básico | Hay al menos un baseline, pero la métrica está mal implementada o se calcula sobre train en lugar de test. |
| Adecuado | Al menos un baseline (Naive o Seasonal Naive) evaluado con MAE, RMSE o MAPE calculados correctamente sobre el conjunto de test. |
| Excelente | Se implementan dos o más baselines, se elige y justifica la métrica más apropiada para el problema (p. ej. MAPE cuando los valores son grandes y comparables, MAE cuando no). |

**Métricas esperadas:** MAE (Mean Absolute Error), RMSE (Root Mean Squared Error), MAPE (Mean Absolute Percentage Error).

---

## 4. Modelo avanzado — 2,0 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No se implementa ningún modelo más allá del baseline, o el modelo no ejecuta. |
| Básico | Se entrena un modelo (RF, LSTM, TCN u otro), pero sin una pipeline correcta o con data leakage en el preprocesado. |
| Adecuado | Al menos un modelo avanzado entrenado correctamente sobre train, evaluado sobre test, con métricas calculadas y comparables con el baseline. |
| Excelente | Se elige el modelo con justificación (p. ej. por qué TCN sobre LSTM, o por qué RF en lugar de un Transformer en este problema), se ajustan hiperparámetros y se documenta el proceso. |

**Modelos candidatos:** Random Forest o XGBoost (forecasting como regresión), LSTM, TCN, Transformer simplificado.

---

## 5. Tabla comparativa del Torneo — 1,5 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay comparativa o se comparan modelos sobre conjuntos de test diferentes. |
| Básico | Hay tabla de resultados, pero los modelos no se comparan sobre el mismo horizonte temporal y conjunto de test. |
| Adecuado | Tabla con al menos dos modelos (baseline + modelo avanzado) evaluados sobre el mismo test, con las mismas métricas. |
| Excelente | La tabla incluye tres o más modelos, métricas múltiples, y una fila de resumen con el ganador y la diferencia respecto al baseline. |

---

## 6. Análisis e interpretación de resultados — 1,0 punto

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay análisis o el comentario es una descripción superficial de números sin explicación. |
| Básico | Se identifica el modelo ganador pero sin conectar con características de la serie o limitaciones del modelo. |
| Adecuado | Se explica por qué el ganador supera al baseline, qué patrones captura mejor y dónde falla. |
| Excelente | El análisis conecta el comportamiento del modelo con las componentes de la serie (tendencia, estacionalidad, eventos), propone mejoras concretas y valora cuándo cambiaría de modelo. |

---

## 7. Documentación y reproducibilidad — 1,0 punto

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | El notebook no ejecuta desde cero o faltan pasos críticos sin documentar. |
| Básico | Ejecuta pero con rutas absolutas, dependencias no declaradas o pasos poco claros. |
| Adecuado | El notebook ejecuta con instrucciones suficientes, rutas relativas y dependencias declaradas. |
| Excelente | Totalmente reproducible: celdas ordenadas, comentarios que guían la revisión, datos de ejemplo incluidos o instrucciones claras para obtenerlos. |
