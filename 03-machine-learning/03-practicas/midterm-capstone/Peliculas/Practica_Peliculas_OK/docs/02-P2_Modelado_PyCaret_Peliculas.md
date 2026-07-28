# Práctica 2 — Modelado exploratorio con PyCaret

## Contexto
En esta práctica utilizarás PyCaret como herramienta de AutoML para explorar
qué modelos funcionan mejor con el dataset.

PyCaret se usará como apoyo para la toma de decisiones, no como solución final.

## Flujo obligatorio: entrenamiento, CV y holdout

PyCaret no sustituye al criterio de quien modela. En esta práctica se sigue este flujo reproducible:

1. `setup(..., train_size=0.8, session_id=42, fold=5)` reserva un **holdout del 20 %** y deja el 80 % para entrenamiento.
2. `compare_models(sort="F1", fold=5)` compara candidatos mediante validación cruzada de cinco folds **solo sobre el entrenamiento**. En este caso `F1` equilibra precisión y exhaustividad; si el contexto penaliza de forma distinta los falsos positivos o negativos, se debe justificar otra métrica.
3. Si se ajusta un candidato, `tune_model(..., optimize="F1", fold=5)` mantiene esa misma separación y métrica. Se conserva `selected_model = best_model` si no hay ajuste; si lo hay, pasa a ser el modelo ajustado.
4. Una vez elegida la solución, `predict_model(selected_model)` sin `data=` evalúa el holdout reservado **una única vez**.

No escales, codifiques ni imputes el `DataFrame` antes de `setup`: PyCaret aprende esas transformaciones a partir del entrenamiento y las aplica mediante su pipeline. Tampoco uses el resultado del holdout para volver a comparar o ajustar modelos.

## Objetivos
- Definir correctamente un problema de clasificación.
- Comparar modelos de forma reproducible con CV de cinco folds.
- Elegir y, si procede, ajustar un candidato sin consultar el holdout.
- Interpretar la evaluación final, sus limitaciones y las decisiones tomadas.

## Problema a resolver

Clasificación: predecir si una película tendrá una valoración alta (`rating_high`). Si se plantea otro objetivo o una regresión, hay que adaptar el módulo de PyCaret y justificarlo.

## Tareas a realizar

### 1. Preparación y configuración
- Selecciona variables, define el objetivo y justifica columnas excluidas.
- Ejecuta `setup` con `train_size=0.8`, `session_id=42` y `fold=5`.
- Conserva la tabla de configuración como evidencia.

### 2. Comparación y ajuste sobre entrenamiento
- Ejecuta `compare_models(sort="F1", fold=5)` y guarda la tabla de resultados. `F1` es un punto de partida razonable para una clase potencialmente desbalanceada; justifica otra métrica si el caso lo exige.
- Justifica la métrica priorizada y el modelo elegido.
- Si ajustas hiperparámetros, usa `tune_model(modelo, optimize="F1", fold=5)` con la misma métrica; no ajustes basándote en el holdout.
- Define siempre `selected_model`: será el candidato de `compare_models` si no ajustas o el resultado de `tune_model` si ajustas.

### 3. Evaluación final
- Cuando la elección esté cerrada, ejecuta una sola vez `predict_model(modelo_elegido)`.
- Guarda la tabla de métricas y algunas predicciones del holdout.
- No uses `finalize_model` antes de esta comprobación: incorporaría el holdout al entrenamiento. Después de documentarla, puede usarse solo para preparar despliegue con todos los datos; no es una nueva evaluación ni sustituye la métrica de holdout.

## Evidencias del entregable

El notebook `P2_PyCaret_base.ipynb` debe permitir comprobar:

- configuración reproducible (80/20, semilla 42 y 5 folds);
- tabla de comparación de CV y criterio de selección;
- ajustes realizados, si los hubo;
- una única tabla de evaluación final sobre el holdout;
- limitaciones y decisiones documentadas.

## Anexo I LazyClassifier vs Pycaret

**LazyPredict** y **PyCaret** son ambas bibliotecas de Python diseñadas para agilizar los flujos de trabajo de aprendizaje automático, pero difieren significativamente en alcance, funcionalidad y casos de uso.

### **LazyPredict**
- **Enfoque Principal**: Evaluación y comparación rápida de modelos.
- **Características Clave**:
  - Entrena y evalúa **docenas de modelos con solo dos líneas de código**.
  - **Sin ajuste de hiperparámetros** — proporciona estimaciones de rendimiento base.
  - Ligero y rápido — ideal para prototipado rápido o exploración inicial de modelos.
  - Los resultados son fácilmente replicables usando scikit-learn.
- **Mejor Para**: Científicos de datos que desean una **forma rápida y de bajo código para comparar múltiples modelos** sin personalización profunda.

### **PyCaret**
- **Enfoque Principal**: Automatización de extremo a extremo del ciclo de vida del aprendizaje automático.
- **Características Clave**:
  - Automatiza el **preprocesamiento de datos, ingeniería de características, selección de modelos, ajuste de hiperparámetros y despliegue**.
  - Ofrece **abstracciones de alto nivel** con amplias herramientas de visualización (ej. curvas ROC, matrices de confusión).
  - Soporta **interpretación de modelos, guardado de pipelines e integración con MLOps**.
  - Incluye capacidades avanzadas como **PLN, clustering, detección de anomalías y minería de reglas de asociación**.
- **Mejor Para**: Usuarios que buscan un **flujo de trabajo completo y listo para producción** con código mínimo, especialmente para proyectos complejos.

### **Resumen Comparativo**
| Característica | **LazyPredict** | **PyCaret** |
|--------|------------------|-------------|
| Entrenamiento de Modelos | Sí (base) | Sí (con ajuste) |
| Ajuste de Hiperparámetros | ❌ No | ✅ Sí |
| Preprocesamiento de Datos | ❌ Mínimo | ✅ Automatización completa |
| Despliegue de Modelos | ❌ No incluido | ✅ Soportado |
| Velocidad | ⚡ Muy rápido | ⏱️ Más lento (más características) |
| Caso de Uso | Comparación rápida de modelos | Automatización completa de pipeline ML |

### **Conclusión**
- Usa **LazyPredict** cuando necesites **benchmarking rápido y simple de modelos**.
- Usa **PyCaret** cuando quieras **construir y desplegar pipelines completos de aprendizaje automático** con mínimo esfuerzo.

> **Nota**: Ambas herramientas no son reemplazos del juicio experto. Se utilizan mejor como **aceleradores** en las etapas tempranas de un proyecto.

