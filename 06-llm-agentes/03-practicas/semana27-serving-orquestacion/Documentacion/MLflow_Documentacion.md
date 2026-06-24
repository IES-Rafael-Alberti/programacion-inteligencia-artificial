# MLflow: documentación práctica

MLflow es una plataforma para gestionar el ciclo de vida de modelos de IA. No se limita a registrar métricas: permite hacer seguimiento de experimentos, guardar artefactos, versionar modelos y servirlos mediante una API.

## Por qué es más que un log

Un log guarda mensajes o valores. TensorBoard visualiza métricas, especialmente en entrenamiento de redes neuronales. MLflow añade una capa más amplia: organiza experimentos, relaciona parámetros con métricas, guarda modelos, registra versiones y permite desplegar.

| Capacidad | Log básico | TensorBoard | MLflow |
|---|---|---|---|
| Métricas | Sí | Sí | Sí |
| Parámetros | Manual | Limitado | Sí |
| Artefactos | Manual | Algunos | Sí |
| Comparación de runs | No | Parcial | Sí |
| Registro de modelos | No | No | Sí |
| Versionado de modelos | No | No | Sí |
| Despliegue del modelo | No | No | Sí |

## Componentes principales

### Experimentos

Agrupan ejecuciones relacionadas. Por ejemplo: `iris_clasificadores`, `mnist_cnn` o `rag_configuraciones`.

### Runs

Una run es una ejecución concreta con sus parámetros, métricas y artefactos.

```python
import mlflow

mlflow.set_experiment("iris_clasificadores")

with mlflow.start_run(run_name="logistic_regression"):
    mlflow.log_param("modelo", "LogisticRegression")
    mlflow.log_param("C", 1.0)
    mlflow.log_metric("accuracy", 0.96)
```

### Parámetros

Describen la configuración: tipo de modelo, hiperparámetros, proveedor de LLM, `top_k`, tamaño de fragmento, etc.

### Métricas

Miden resultados: accuracy, F1, pérdida, relevancia de contexto, fidelidad de respuesta o tiempo de inferencia.

### Artefactos

Son archivos asociados a una run: modelos, informes, gráficos, matrices de confusión, ejemplos de respuestas o JSON de evaluación.

```python
mlflow.log_artifact("confusion_matrix.png")
mlflow.log_artifact("ejemplos_respuestas.json")
```

### Model Registry

Permite versionar modelos y asignar estados como `Staging`, `Production` o `Archived`.

```python
mlflow.register_model("runs:/<run_id>/model", "IrisClassifier")
```

### Model Serving

MLflow puede servir un modelo registrado como API REST.

```bash
mlflow models serve -m "models:/IrisClassifier/Production" -p 5000
```

## MLflow con modelos clásicos

Ejemplo de uso en clase:

1. Entrenar varios clasificadores.
2. Registrar parámetros y métricas.
3. Comparar runs en la interfaz de MLflow.
4. Guardar el mejor modelo.
5. Usarlo después desde Gradio o FastAPI.

## MLflow con RAG y LLM

También puede registrar configuraciones generativas:

1. Recuperador usado: Chroma, FAISS, TF-IDF o búsqueda simple.
2. Modelo de embeddings.
3. `top_k`.
4. Prompt utilizado.
5. Modelo LLM.
6. Métricas como relevancia, fidelidad o presencia de citas.

```python
with mlflow.start_run(run_name="rag_chroma_top3"):
    mlflow.log_param("retriever", "chroma")
    mlflow.log_param("top_k", 3)
    mlflow.log_metric("faithfulness", 0.82)
    mlflow.log_metric("context_relevance", 0.76)
```

## Buenas prácticas

1. Registrar siempre parámetros y métricas juntos.
2. Guardar artefactos que permitan entender el resultado.
3. Usar nombres claros de experimentos y runs.
4. Registrar también configuraciones que funcionaron mal si aportan aprendizaje.
5. Conectar MLflow con Gradio o FastAPI para usar el mejor modelo.

## Errores frecuentes

1. Usarlo como si fuera solo un fichero de log.
2. Guardar métricas sin los parámetros que las explican.
3. Comparar experimentos con particiones de datos distintas sin indicarlo.
4. No guardar el modelo o los artefactos necesarios para reproducir.
5. Empezar a registrar demasiado tarde.

## Relación con los notebooks

El notebook `Fase2/100_mlflow_llamaindex_rag.ipynb` muestra tracking de modelos sencillos y registro de una configuración RAG. Usa MLflow real si está disponible y fallback JSON si no lo está.

## Cuándo usar MLflow

Usa MLflow cuando compares modelos, prompts, configuraciones RAG o versiones de un pipeline y necesites justificar la elección con datos.

No es necesario para una prueba aislada que no se va a comparar ni reproducir.

## Instalación

```bash
pip install mlflow
mlflow ui
```

Documentación oficial: https://mlflow.org/docs/latest/index.html
