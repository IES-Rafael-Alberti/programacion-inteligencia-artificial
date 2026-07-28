# Práctica 3 — Modelo final, afinado y conclusiones

## Resultado esperado

Reimplementa con scikit-learn el enfoque elegido en P2 mediante un flujo **reproducible y sin fuga de datos**. El resultado no es solo una métrica: debe mostrar cómo se reservaron los datos, cómo se ajustó el pipeline y qué errores mantiene el modelo.

## Flujo obligatorio

1. Define el objetivo (`rating_high` en el ejemplo), las variables predictoras y las columnas excluidas con su motivo.
2. Separa `X_train`, `X_test`, `y_train` e `y_test` con `train_test_split(..., test_size=0.20, random_state=42, stratify=y)` **antes** de imputar, codificar o escalar.
3. Crea un `ColumnTransformer` dentro de un `Pipeline`: imputación y escalado para variables numéricas; imputación y `OneHotEncoder(handle_unknown="ignore")` para categóricas. Las columnas se identifican desde `X_train`.
4. Ajusta `GridSearchCV(cv=5, scoring="f1")` solo con `X_train` e `y_train`. La cuadrícula debe ser razonable y la métrica, justificada.
5. Antes de mirar el test, documenta el mejor resultado medio de CV y los hiperparámetros seleccionados.
6. Evalúa el `best_estimator_` sobre `X_test` **una única vez**; informa de accuracy, precision, recall y F1, matriz de confusión y una muestra de errores.
7. Formula conclusiones, límites del dataset y una mejora futura. Si el test abre una nueva hipótesis, ese test queda agotado: la nueva iteración necesita otra evaluación reservada.

## Por qué el pipeline evita fugas

Un imputador, un codificador o un escalador aprende estadísticas de los datos. Si se ajusta antes de separar, o fuera de la validación cruzada, incorpora información que no estaría disponible al predecir. Al colocarlos en el `Pipeline`, scikit-learn los ajusta únicamente con la parte de entrenamiento de cada fold y, al final, con el entrenamiento completo antes de predecir el test.

## Tareas a realizar

### 1. Reimplementación explícita

- Usa scikit-learn, no PyCaret.
- Construye un `Pipeline` de preprocesado y modelo.
- Justifica las columnas excluidas, especialmente IDs o información no disponible en el momento de la predicción.

### 2. Ajuste de hiperparámetros

- Usa `GridSearchCV` con cinco folds sobre entrenamiento.
- Compara el resultado medio y su variabilidad, no una métrica del test.
- Mantén el espacio de búsqueda acotado y explicable.

### 3. Evaluación final y errores

- No llames a `predict(X_test)` hasta cerrar la selección.
- Calcula las métricas finales una vez y representa la matriz de confusión.
- Revisa errores concretos: ¿qué variables o casos pueden explicar las predicciones fallidas?

### 4. Conclusiones

- Calidad del modelo respecto al objetivo y la métrica.
- Limitaciones de datos, etiqueta o generalización.
- Mejoras futuras, sin reutilizar el test para validarlas.

## Entregable y evidencias

Entrega `notebooks/alumno/P3_Modelo_base.ipynb` completado e incluye:

- separación 80/20 reproducible con estratificación;
- `ColumnTransformer` y `Pipeline` completos;
- tabla de resultados de CV y decisión de ajuste;
- métricas finales, matriz de confusión y análisis de errores del test;
- conclusiones, limitaciones y trazabilidad de decisiones;
- las evidencias de proceso y de verificación exigidas en las [normas comunes de entrega y uso de IA](../../../../../../docs/normas-entregas-y-uso-de-ia.md).

## Anexo GPU (opcional)

Una variante GPU puede ser útil para acelerar el entrenamiento, pero no modifica el contrato metodológico: separación primero, transformadores y CV sobre entrenamiento, y una única evaluación final sobre test.
