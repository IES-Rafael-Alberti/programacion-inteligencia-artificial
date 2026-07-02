## **Sobreajuste vs. Subajuste en Machine Learning**

El aprendizaje automático se basa en la construcción de modelos que generalicen bien a datos no vistos. Sin embargo, dos problemas comunes pueden afectar la capacidad de generalización de un modelo: **sobreajuste (overfitting)** y **subajuste (underfitting)**. Comprender estas problemáticas es fundamental para diseñar modelos efectivos.

![](Sobreajuste-Subajuste_En-ML.jpeg)

------------------------------------------------------------------------

### **¿Qué es el Sobreajuste (Overfitting)?**

El sobreajuste ocurre cuando un modelo se ajusta demasiado a los datos de entrenamiento, capturando tanto los patrones reales como el ruido presente en ellos. Como resultado, el modelo tiene un alto desempeño en los datos de entrenamiento, pero un bajo rendimiento en datos nuevos.

#### **Causas del sobreajuste:**

-   Modelo demasiado complejo en relación con la cantidad de datos.
-   Exceso de parámetros en comparación con la información disponible.
-   Entrenamiento por demasiadas iteraciones.
-   Falta de regularización.

#### **Ejemplo de sobreajuste:**

-   Un modelo de regresión polinómica de alto grado que se adapta perfectamente a los puntos de entrenamiento pero falla en la predicción de nuevos datos.
-   Un árbol de decisión profundo que memoriza los datos de entrenamiento en lugar de encontrar patrones generalizables.

#### **Cómo evitar el sobreajuste:**

-   **Regularización:** Aplicar técnicas como Ridge (L2) y Lasso (L1) para penalizar la complejidad del modelo.
-   **Validación cruzada:** Dividir los datos en conjuntos de entrenamiento y validación para evaluar el desempeño en datos no vistos.
-   **Aumento de datos:** Incluir más ejemplos para mejorar la capacidad de generalización del modelo.
-   **Reducción de complejidad:** Simplificar la estructura del modelo eliminando características irrelevantes.
-   **Uso de ensambles:** Métodos como Bagging y Boosting ayudan a reducir la varianza del modelo.

------------------------------------------------------------------------

### **¿Qué es el Subajuste (Underfitting)?**

El subajuste ocurre cuando un modelo es demasiado simple y no logra capturar la estructura subyacente de los datos. Como resultado, el modelo tiene un bajo desempeño tanto en los datos de entrenamiento como en los datos de prueba.

#### **Causas del subajuste:**

-   Modelo con una estructura demasiado simple.
-   Falta de entrenamiento o insuficiente número de iteraciones.
-   Uso de características insuficientes o poco representativas.

#### **Ejemplo de subajuste:**

-   Una regresión lineal tratando de ajustar datos que siguen una relación no lineal.
-   Un árbol de decisión con muy poca profundidad que no captura patrones importantes.

#### **Cómo evitar el subajuste:**

-   **Aumentar la complejidad del modelo:** Usar modelos más expresivos, como redes neuronales en lugar de modelos lineales.
-   **Añadir más características:** Incluir atributos adicionales que representen mejor la estructura de los datos.
-   **Entrenar por más tiempo:** Permitir más iteraciones para que el modelo aprenda mejor los patrones de los datos.
-   **Reducir la regularización:** Ajustar los hiperparámetros de regularización para permitir un mayor ajuste a los datos.

------------------------------------------------------------------------

### **Equilibrio entre Sobreajuste y Subajuste**

El objetivo en Machine Learning es encontrar un modelo con un buen equilibrio entre sobreajuste y subajuste. Un modelo óptimo debe capturar los patrones de los datos sin ajustarse demasiado al ruido del conjunto de entrenamiento.

Este equilibrio se representa en la descomposición del error: $$ Error Total = Sesgo^2 + Varianza + Ruido $$

-   **Alto sesgo, baja varianza → Subajuste** (modelo demasiado simple).

-   **Bajo sesgo, alta varianza → Sobreajuste** (modelo demasiado complejo).

-   **Punto óptimo:** Se minimizan tanto el sesgo como la varianza.

#### **Técnicas para encontrar el equilibrio:**

-   Selección de hiperparámetros con validación cruzada.
-   Uso de modelos con regularización adecuada.
-   Implementación de técnicas de ensamble como Random Forest o XGBoost.
-   Recolección de más datos para mejorar la capacidad de generalización.

------------------------------------------------------------------------

### **Conclusión**

Tanto el sobreajuste como el subajuste son problemas críticos en Machine Learning. Un modelo bien ajustado debe encontrar un equilibrio adecuado, evitando ser demasiado simple o demasiado complejo. Aplicar técnicas como validación cruzada, regularización y selección de características adecuadas es esencial para mejorar el desempeño y la capacidad de generalización del modelo.

### **Ejemplo: Ajuste de un modelo a datos sintéticos**

1.  **Subajuste (Underfitting):** Un modelo lineal intenta ajustar datos no lineales.
2.  **Ajuste Óptimo:** Un modelo de regresión polinómica de grado adecuado que captura bien la tendencia sin exagerar.
3.  **Sobreajuste (Overfitting):** Un modelo de regresión polinómica de alto grado que se ajusta demasiado a los datos de entrenamiento.

Tres gráficos ilustrando **subajuste, ajuste óptimo y sobreajuste** con regresión polinómica:

![](Underfit_JustRight_Overfit.png)

1.  **Subajuste (Underfitting) - Grado 1 (izquierda)**:
    -   El modelo es demasiado simple (regresión lineal) y no captura la estructura de los datos.\
    -   **Ejemplo típico:** Regresión lineal en datos no lineales.
2.  **Ajuste Óptimo - Grado 3 (centro)**:
    -   El modelo se ajusta bien a la tendencia sin sobreajustarse.\
    -   **Ejemplo típico:** Un modelo bien regulado que generaliza bien en datos nuevos.
3.  **Sobreajuste (Overfitting) - Grado 10 (derecha)**:
    -   El modelo es demasiado complejo y captura ruido en los datos de entrenamiento.\
    -   **Ejemplo típico:** Regresión polinómica de alto grado que no generaliza bien en datos nuevos.

### Código para entrenar modelos de regresión polinómica y visualizar el ajuste:
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Generar datos sintéticos
np.random.seed(42)
X = np.linspace(-3, 3, 30).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(scale=0.2, size=X.shape[0])

# Crear diferentes modelos de regresión polinómica con distintos grados
degrees = [1, 3, 10]  # Subajuste, ajuste óptimo, sobreajuste

plt.figure(figsize=(18, 5))

for i, degree in enumerate(degrees):
    plt.subplot(1, 3, i + 1)
    
    # Crear modelo polinómico
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X, y)
    
    # Predicción en un rango más amplio
    X_test = np.linspace(-3, 3, 100).reshape(-1, 1)
    y_pred = model.predict(X_test)
    
    # Graficar resultados
    plt.scatter(X, y, label="Datos reales", color="orange")
    plt.plot(X_test, y_pred, label=f"Modelo polinómico grado {degree}", color="red")
    plt.title(f"Regresión polinómica (grado {degree})")
    plt.legend()

# Mostrar los gráficos
plt.show()
```


## **Sesgo vs. Varianza en Machine Learning y conceptos relacionados**

### **Equilibrio entre Sesgo y Varianza**

En el aprendizaje automático, el **equilibrio entre sesgo (bias) y varianza (variance)** es un concepto fundamental que impacta directamente el rendimiento y la capacidad de generalización de un modelo. Comprender este equilibrio es clave para desarrollar modelos que no solo se ajusten bien a los datos de entrenamiento, sino que también tengan un buen desempeño en datos no vistos.

![](SesgoVarianzaEn-ML.jpeg)

La imagen proporcionada ilustra este equilibrio. Se divide en dos partes principales: diagramas superiores y un gráfico inferior.

#### **1. Diagramas superiores:**

-   **Izquierda (Subajuste - Underfitting):** Representa un modelo con **alto sesgo y baja varianza**, que no capta la estructura real de los datos y generaliza mal. Se observa una separación demasiado simple (una línea recta) que no se adapta bien a los datos.
-   **Centro (Optimal Model Complexity - Complejidad óptima del modelo):** Representa un modelo equilibrado, con un compromiso adecuado entre sesgo y varianza. Aquí la frontera de decisión se ajusta bien a la estructura de los datos sin sobreajustarse.
-   **Derecha (Sobreajuste - Overfitting):** Representa un modelo con **baja sesgo y alta varianza**, que se ajusta demasiado a los datos de entrenamiento, capturando incluso el ruido. Se observa una frontera de decisión demasiado compleja.

#### **2. Gráfico inferior:**

-   Muestra la relación entre el **error de predicción** y la **complejidad del modelo**.
-   A medida que la complejidad del modelo aumenta:
    -   El **sesgo** (curva roja discontinua) **disminuye**.
    -   La **varianza** (curva azul discontinua) **aumenta**.
-   El **error de entrenamiento** (curva roja sólida) es bajo para modelos complejos, pero el **error de prueba** (curva azul sólida) aumenta en modelos con sobreajuste.
-   El **punto óptimo** está donde se minimiza el **error de prueba**, logrando un buen equilibrio entre sesgo y varianza.

## **Sesgo (Bias)**

El **sesgo** se refiere a la capacidad de un modelo para capturar la relación subyacente entre las variables de entrada y salida. Un modelo con **alto sesgo** tiende a hacer suposiciones demasiado simplificadas, lo que resulta en un desempeño deficiente tanto en los datos de entrenamiento como en los datos de prueba. Este problema se conoce como **subajuste (underfitting)**. Un modelo con alto sesgo es como un jugador de dardos que siempre tira con los ojos cerrados y los tiros acaban en la pared, sin importar cuánto practique porque no apunta bien.
 
### **Síntomas de alto sesgo:**

-   Bajo rendimiento tanto en entrenamiento como en test.
-   No importa cuántos datos se usen, el modelo sigue fallando igual.

### **Ejemplo de alto sesgo:**

-   Un modelo de regresión lineal tratando de ajustar un conjunto de datos con una relación no lineal.
-   Un árbol de decisión con muy poca profundidad que no capta patrones complejos en los datos.

### **Cómo arreglar el alto sesgo:**

-   Usar un modelo más complejo.
-   Añadir más *features* relevantes.
-   Reducir la regularización si está limitando demasiado.

## **Varianza (Variance)**

La **varianza** se refiere a la sensibilidad de un modelo a pequeñas variaciones en los datos de entrenamiento. Un modelo con **alta varianza** se ajusta demasiado a los datos de entrenamiento, capturando tanto los patrones reales como el ruido presente en ellos. Esto da lugar a un mal desempeño en datos nuevos, lo que se conoce como **sobreajuste (overfitting)**. Un modelo con alta varianza es como un jugador de dardos que se obsesiona con cada detalle (velocidad del viento, presión atmosférica, horóscopo), logrando algunos tiros muy buenos pero un rendimiento general errático.

#### **Síntomas de alta varianza:**

-   Precisión brutal en entrenamiento, pero en test se estrella.
-   Pequeños cambios en los datos lo descontrolan.

\####**Ejemplo de alta varianza:**

-   Un modelo de regresión polinómica de grado muy alto que se adapta perfectamente a los datos de entrenamiento pero falla en la predicción de nuevos datos.
-   Un árbol de decisión demasiado profundo que memoriza los datos de entrenamiento en lugar de generalizar patrones.
-   Una red neuronal gigante con pocos datos.

\####**Cómo arreglar la alta varianza:**

-   Regularización (L1/L2, dropout en redes neuronales,batch normalization).
-   Usar menos *features* irrelevantes.
-   Obtener más datos o usar *data augmentation*.
-   Simplificar el modelo.

## **Equilibrio entre Sesgo y Varianza y su relación con Overfitting y Underfitting**

El desafío en el aprendizaje automático es encontrar un modelo con un **equilibrio adecuado entre sesgo y varianza**. Un modelo ideal debería capturar las relaciones fundamentales en los datos sin ajustarse demasiado a sus particularidades.

Este equilibrio se ilustra en la **descomposición del error en machine learning:**

`Error Total = Sesgo^2 + Varianza + Ruido`

-   **Alto sesgo, baja varianza:** El modelo es simple y no captura bien los datos. Esto resulta en **subajuste (underfitting)**, donde el modelo no aprende lo suficiente y falla en todo.
-   **Bajo sesgo, alta varianza:** El modelo es demasiado complejo y se ajusta excesivamente a los datos de entrenamiento. Esto resulta en **sobreajuste (overfitting)**, donde el modelo aprende demasiado bien los datos de entrenamiento y no generaliza.
-   **Equilibrio óptimo:** Se minimiza tanto el sesgo como la varianza, obteniendo un modelo con buena capacidad de generalización.

## **Resumiendo:**

-   **Sesgo y Varianza** explican por qué un modelo puede fallar.
-   **Overfitting y Underfitting** son los síntomas de que algo no está bien balanceado.

### **Técnicas para lograr el equilibrio**

-   **Regularización:** Métodos como Lasso (L1) y Ridge (L2) ayudan a reducir la complejidad del modelo.
-   **Validación cruzada:** Permite evaluar el desempeño del modelo en diferentes subconjuntos de datos.
-   **Reducción de características:** Eliminar características irrelevantes puede ayudar a reducir la varianza.
-   **Aumento de datos:** Ampliar el conjunto de datos puede mejorar la generalización.
-   **Ensamblado de modelos:** Métodos como Bagging (e.g., Random Forest) y Boosting (e.g., XGBoost) ayudan a mitigar sesgo y varianza.

## **Conclusión**

El sesgo y la varianza son dos caras de la misma moneda en el aprendizaje automático. Encontrar un equilibrio adecuado es clave para construir modelos que generalicen bien en datos nuevos. A través de técnicas como regularización, validación cruzada y ensambles, es posible mejorar la capacidad predictiva del modelo y evitar tanto el subajuste como el sobreajuste.

La imagen proporcionada complementa esta información visualizando claramente los conceptos de subajuste, sobreajuste y el equilibrio entre sesgo y varianza. Incorporar la imagen al texto podría mejorar la comprensión de estos conceptos.
