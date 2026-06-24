# 🤖 Modelado, Entrenamiento y Evaluación de Machine Learning
Ahora pasamos a la fase crítica de **Modelado y Evaluación**. Ya tenemos nuestros datos limpios y transformados, listos para que los algoritmos de Machine Learning aprendan.

Este documento detalla los pasos y consideraciones esenciales para la fase de modelado, abarcando desde la selección del algoritmo hasta la optimización de sus parámetros.

## Aspectos Transversales a Regresión y Clasificación

### 1. Desafíos de Ajuste
Dos problemas fundamentales pueden ocurrir durante el entrenamiento y deben ser diagnosticados comparando el rendimiento en el conjunto de **Entrenamiento** y el conjunto de **Validación** (o prueba).

| Problema | Diagnóstico | Solución |
| :--- | :--- | :--- |
| **Overfitting (Sobreajuste)** | Alto rendimiento en el entrenamiento, **bajo rendimiento** en la validación (el modelo memoriza el ruido). | **Regularización** (L1, L2), **Reducción de características**, Aumento de datos (*Data Augmentation*), **Validación Cruzada**. |
| **Underfitting (Subajuste)** | **Bajo rendimiento** tanto en el entrenamiento como en la validación (el modelo es demasiado simple). | Usar un **modelo más complejo** (ej., de Regresión Lineal a Random Forest), **Ingeniería de Características** más rica, **Aumentar el tiempo de entrenamiento**. |

### 2. Técnicas de Validación
La **Validación Cruzada (*Cross-Validation*)** es crucial para obtener una estimación robusta del rendimiento del modelo y evitar el sobreajuste al conjunto de validación.

* **K-Fold Cross-Validation:** El conjunto de entrenamiento se divide en $K$ subconjuntos (folds). El modelo se entrena $K$ veces, utilizando $K-1$ folds para el entrenamiento y 1 fold para la validación en cada iteración. La métrica final es el promedio de los $K$ resultados.

### 3. Optimización de Parámetros e Hiperparámetros
Los **parámetros** son aprendidos por el modelo durante el entrenamiento (ej., coeficientes en la regresión). Los **hiperparámetros** son configuraciones externas que se ajustan antes de entrenar (ej., la tasa de aprendizaje, el número de árboles).

* **Grid Search (*Búsqueda en Rejilla*):** Prueba sistemáticamente todas las combinaciones posibles de hiperparámetros dentro de un rango definido por el usuario. Es exhaustivo pero computacionalmente costoso.
* **Randomized Search (*Búsqueda Aleatoria*):** Muestra aleatoriamente combinaciones de hiperparámetros. A menudo encuentra buenos resultados más rápido que Grid Search.
* **Bayesian Optimization:** Utiliza modelos probabilísticos para guiar la búsqueda, probando combinaciones que tienen más potencial de mejorar el rendimiento, siendo más eficiente.

---

## 🅰️ Parte A: Modelos de Regresión

El objetivo es predecir un valor numérico continuo.

### I. Regresión Supervisada
| Modelo(s) | Características Clave | Consideraciones de Preparación de Datos |
| :--- | :--- | :--- |
| **Regresión Lineal Simple/Múltiple** | Asume una relación lineal entre las *features* y el *target*. | Requiere **Escalamiento** y, en modelado inferencial, **transformación para normalidad/linealidad**. |
| **Regresión por Rigde (L2) y Lasso (L1)** | Incorpora **regularización** para prevenir el *overfitting*. Lasso puede llevar coeficientes a cero (selección de características). | Requiere **Escalamiento** para aplicar la penalización de forma justa a todos los coeficientes. |
| **Random Forest / Gradient Boosting** | Modelos basados en árboles, robustos a *outliers* y asimetría. No asumen linealidad. | **No requieren Escalamiento**. Se benefician de la **Codificación Ordinal** para variables categóricas. |
| **Regresión por Máquinas de Vectores de Soporte (SVR)** | Eficaz en espacios de alta dimensión. | Requiere **Escalamiento** y es sensible a la elección de *kernels* (función de transformación). |

### II. Evaluación de Regresión (Métricas)

La evaluación se centra en la magnitud del error. Las métricas deben calcularse en la **escala original** del *target*.

| Métrica | Descripción | Cuándo Usar |
| :--- | :--- | :--- |
| **Error Cuadrático Medio (MSE)** | Promedio de los errores al cuadrado. Castiga fuertemente los errores grandes (*outliers*). | Común, pero puede ser difícil de interpretar debido a las unidades al cuadrado. |
| **Raíz del Error Cuadrático Medio (RMSE)** | Raíz cuadrada del MSE. Mismo significado que el MSE, pero en las **unidades originales** del *target*. | **Métrica estándar**. Fácil de interpretar. |
| **Error Absoluto Medio (MAE)** | Promedio del valor absoluto de los errores. Menos sensible a los *outliers* que el RMSE. | Útil cuando los errores grandes no deben ser castigados de forma excesiva. |
| **Coeficiente de Determinación ($R^2$)** | Proporción de la varianza en el *target* que es predecible a partir de las *features*. Rango $[0, 1]$ (idealmente). | Métrica de bondad de ajuste. Indica la **capacidad explicativa** del modelo. |

---

## 🅱️ Parte B: Modelos de Clasificación

El objetivo es predecir la clase o categoría de una instancia.

### I. Clasificación Supervisada

| Modelo(s) | Características Clave | Consideraciones de Preparación de Datos |
| :--- | :--- | :--- |
| **Regresión Logística** | Modelo lineal que estima la probabilidad de que una instancia pertenezca a una clase. | Requiere **Escalamiento**. Muy sensible al **desbalanceo de clases**. |
| **K-Vecinos más Cercanos (KNN)** | Clasifica por mayoría de votos de los $K$ vecinos más cercanos. | **Requiere Escalamiento**; sensible a la dimensionalidad y al ruido. |
| **Naive Bayes** | Basado en el teorema de Bayes y asume independencia condicional entre las *features*. | **No requiere Escalamiento**. La versión Gaussiana se beneficia de la **Normalidad**. |
| **Random Forest / XGBoost** | Robusto al ruido y *outliers*. Excelente para problemas no lineales. | **No requiere Escalamiento**. Se beneficia de la **Ponderación de Clases** para manejar desbalanceo. |

### II. Evaluación de Clasificación (Métricas)

La evaluación debe considerar el equilibrio entre los diferentes tipos de errores (Falsos Positivos vs. Falsos Negativos).

* **Matriz de Confusión:** La base de todas las métricas, resume los resultados en 4 categorías: Verdaderos Positivos (TP), Verdaderos Negativos (TN), Falsos Positivos (FP), Falsos Negativos (FN).

| Métrica | Descripción (Fórmula) | Cuándo Usar |
| :--- | :--- | :--- |
| **Accuracy (Precisión)** | Proporción de predicciones correctas sobre el total. $(\frac{TP+TN}{\text{Total}})$ | **Solo si las clases están balanceadas.** Engañosa en *datasets* desbalanceados. |
| **Precision (Valor Predictivo Positivo)** | De todos los positivos predichos, cuántos son correctos. $(\frac{TP}{TP+FP})$ | Cuando el **Costo del Falso Positivo es alto** (ej., diagnóstico de cáncer, enviar *spam*). |
| **Recall (Sensibilidad)** | De todos los positivos reales, cuántos fueron predichos. $(\frac{TP}{TP+FN})$ | Cuando el **Costo del Falso Negativo es alto** (ej., no detectar un fraude, un misil). |
| **F1-Score** | Media armónica de Precision y Recall. $(\frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}})$ | **Métrica estándar** para *datasets* desbalanceados; busca un equilibrio entre FP y FN. |

#### Trade-off Precision-Recall y Curvas

Existe un **Trade-off** entre Precision y Recall: generalmente, mejorar uno implica sacrificar el otro ajustando el umbral de clasificación.

* **Curva ROC (Receiver Operating Characteristic):** Grafica la Tasa de Verdaderos Positivos (Recall) vs. la Tasa de Falsos Positivos para varios umbrales.
    * **Métrica AUC (Area Under the Curve):** El área bajo la curva ROC. El **AUC-ROC** es la métrica de rendimiento más robusta al desbalanceo. Un valor de 1.0 es perfecto; 0.5 es aleatorio.
* **Curva Precision-Recall:** Grafica Precision vs. Recall para varios umbrales. Es preferible a la curva ROC cuando el *dataset* está **fuertemente desbalanceado**.

---

## 🌐 Parte C: Modelos No Supervisados

En el aprendizaje no supervisado, no hay variable *target*. El objetivo es encontrar estructuras o patrones ocultos en los datos.

### I. Clustering (Agrupamiento)

El objetivo es agrupar observaciones similares sin etiquetas previas.

| Modelo(s) | Propósito | Ingeniería de Características |
| :--- | :--- | :--- |
| **K-Means** | Divide los datos en $K$ grupos (clústers) donde los puntos en un clúster están cerca del centroide. | **Requiere Escalamiento**. Es sensible a la elección de $K$ y a los *outliers*. |
| **DBSCAN** | Agrupa puntos densamente agrupados, marcando los puntos aislados como ruido (*outliers*). | **Requiere Escalamiento**. No requiere definir $K$ de antemano. |
| **Clustering Jerárquico** | Crea una jerarquía de clústeres representados por un dendrograma. | Requiere **Escalamiento**. Útil para visualizar la estructura de agrupamiento. |

### II. Reducción de Dimensionalidad

El objetivo es reducir el número de *features* manteniendo la mayor parte posible de la varianza (información).

* **Análisis de Componentes Principales (PCA)**:
    * **Propósito:** Proyecta los datos en un nuevo subespacio de menor dimensión. Las nuevas dimensiones (Componentes Principales) capturan la máxima varianza.
    * **Preparación:** **Requiere Escalamiento** (Estandarización) para que las variables con mayor varianza original no dominen la proyección.
    * **Uso en ML Complejo:** Las nuevas *features* (Componentes Principales) son a menudo **ortogonales** (no correlacionadas), lo que puede mejorar el rendimiento de modelos lineales o reducir el tiempo de entrenamiento en modelos complejos.

### III. Ingeniería de Características con Modelos No Supervisados

* **Uso de Clústeres como *Features***: Se puede aplicar un algoritmo de *clustering* (ej., K-Means) a los datos y luego asignar el *ID del clúster* a cada fila como una **nueva variable categórica** en un modelo supervisado posterior. Esto a menudo ayuda al modelo supervisado a capturar interacciones no lineales.

---

## 🔎 ¿Algo Olvidado?

Sí, un aspecto crucial en el proceso de modelado es la **Interpretación y Explicabilidad del Modelo (XAI - Explainable AI)**, que debe realizarse después de la evaluación.

### 4. Interpretación del Modelo (XAI)

Después de seleccionar el modelo con la mejor métrica, es vital entender **por qué** toma ciertas decisiones.

* **Modelos Lineales:** La interpretación es directa: los **coeficientes** indican la dirección e intensidad de la relación de cada *feature* con el *target*.
* **Modelos Basados en Árboles (Caja Negra):**
    * **Importancia de las Características (*Feature Importance*):** Cuantifica cuánto contribuyó cada *feature* a la reducción del error o impureza del nodo en el conjunto de árboles.
    * **SHAP (SHapley Additive exPlanations):** Técnica avanzada que asigna un valor a cada *feature* para una predicción específica, explicando por qué una predicción individual fue alta o baja. Es la forma más precisa de explicar modelos complejos.