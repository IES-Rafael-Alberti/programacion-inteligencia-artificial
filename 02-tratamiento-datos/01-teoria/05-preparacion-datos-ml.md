# Preparación de Datos para Machine Learning: Pasos Clave
La **Preparación de Datos (*Data Preparation*)** es la fase natural que sigue al EDA. De hecho, las dos fases se superponen: el EDA **diagnostica** los problemas, y la Preparación de Datos **resuelve** esos problemas.
La Preparación de Datos se conecta directamente con las últimas fases del EDA (Manejo de *Outliers*, Ingeniería de Características y Transformación de Variables) y prepara el *dataset* final para la fase de Modelado (Entrenamiento de Algoritmos de Machine Learning).

Resumen de la fase de "Preparación de Datos" como continuación lógica del flujo de trabajo:

---

## 🛠️ Preparación de Datos para el Modelado de Machine Learning

La Preparación de Datos, también conocida como *Feature Engineering* o preprocesamiento, toma los hallazgos del EDA (diagnósticos de *outliers*, *NaNs*, y desbalanceo) y los transforma en un *dataset* limpio y estructurado que cumple con los requisitos matemáticos de los algoritmos de Machine Learning.

---

### Fase 1: Finalización de la Limpieza y Manejo de Faltantes
Esta fase es la acción correctiva directa sobre los diagnósticos de calidad del EDA.

#### 1. Manejo Final de Valores Faltantes (NaNs)
La decisión sobre cómo tratar los valores faltantes, tomada durante el EDA, se implementa aquí:

* **Imputación:** Rellenar los valores faltantes.
    * **Variables Numéricas:** Imputar con la **mediana** (más robusta a *outliers*), media, o un valor constante (ej., -1 si tiene un significado de "desconocido").
    * **Variables Categóricas:** Imputar con la **moda** (el valor más frecuente) o con una nueva categoría "Desconocido".
* **Eliminación:** Eliminar filas o columnas enteras si el porcentaje de *NaNs* es muy alto (ej., > 70%) y la imputación no es viable.

#### 2. Manejo de *Outliers* y Asimetría
Los tratamientos identificados para normalizar distribuciones se aplican ahora.

* **Transformación:** Aplicar transformaciones como el **logaritmo** ($\ln(x)$ o $\ln(1+x)$) o la **raíz cuadrada** a variables numéricas fuertemente sesgadas (*skewed*) para acercarlas a una distribución normal.
* ***Capping* (Limitación):** Reemplazar los *outliers* extremos con un valor umbral (ej., el percentil 99 o 1) en lugar de eliminarlos, si se considera que contienen información.

---

### Fase 2: Codificación y Transformación de Variables
Muchos de los algoritmos de ML solo entienden números, por lo que las variables categóricas deben ser transformadas.

Algunos comoo los árboles de decisión pueden manejar variables categóricas de forma nativa, pero la mayoría (Regresión Lineal, SVM, Redes Neuronales) requieren codificación numérica.

#### 3. Codificación de Variables Categóricas
Las categorías deben convertirse en una representación numérica.

* **One-Hot Encoding (OHE):** Crear una nueva columna binaria (0 o 1) por cada categoría única. Es ideal para variables **Nominales** (sin orden natural, ej., Color, Ciudad).
* **Ordinal Encoding:** Asignar rangos numéricos (1, 2, 3...) según el orden natural de la categoría. Es ideal para variables **Ordinales** (con orden natural, ej., Bajo, Medio, Alto).
* **Target Encoding:** Reemplazar la categoría con la **media del *target*** para esa categoría. Útil para *datasets* grandes, pero debe aplicarse cuidadosamente para evitar *data leakage*.
* **Frecuencia o Conteo:** Reemplazar la categoría con su frecuencia o conteo en el *dataset*. Útil para variables con muchas categorías.
* **Agrupación de Categorías Raras:** Combinar categorías poco frecuentes en una categoría "Otro" para reducir la dimensionalidad.
* **Embeddings:** Utilizar representaciones densas aprendidas (común en NLP y Deep Learning) para variables categóricas con muchas categorías.  

#### 4. Discretización (*Binning*)
Transformar una variable numérica continua en grupos categóricos u ordinales.

* **`pd.cut` o `pd.qcut`:** Agrupar la variable continua (ej., Edad) en intervalos (ej., "Joven", "Adulto", "Mayor") para capturar mejor las relaciones no lineales.

---

### Fase 3: Escalamiento y Normalización

La mayoría de los algoritmos basados en distancia (KNN, SVM, K-Means) o gradiente (Regresión Lineal, Redes Neuronales) son sensibles a la escala de las variables.

#### 5. Escalamiento de Variables Numéricas
Asegurar que todas las características contribuyan equitativamente al modelo.

* **Normalización (MinMaxScaler):** Escala los valores al rango $[0, 1]$. Útil cuando la distribución no es normal y se conoce el rango deseado.
    $$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$
* **Estandarización (StandardScaler):** Transforma los datos para que tengan una **media de 0** y una **desviación estándar de 1** (la distribución Z). Es la opción más común y robusta.
    $$X_{std} = \frac{X - \mu}{\sigma}$$

---

### Fase 4: Manejo del Desbalanceo y Partición de Datos

Esta fase aborda el problema de desbalanceo diagnosticado y prepara los datos para el *pipeline* de modelado.

#### 6. Aplicación de Técnicas de Muestreo (Si es necesario)
Si el *target* es categórico y está desbalanceado (como se identificó en el EDA), se aplica la técnica de muestreo. **Importante:** Estas técnicas se deben aplicar **solo al conjunto de entrenamiento** para evitar la contaminación de datos (*data leakage*).

* **Sobremuestreo (SMOTE):** Generar nuevas instancias sintéticas de la clase minoritaria.

#### 7. Ingeniería de Características (Consolidación del *Feature Engineering*)
Se aplican las transformaciones complejas identificadas en la última fase del EDA (ej., la creación de la variable `TotalSqFeet` a partir de la suma de otras áreas).

#### 8. Partición del *Dataset*
Finalmente, el *dataset* completamente limpio, escalado y codificado se divide:

* **Conjunto de Entrenamiento (*Training Set*):** El conjunto más grande (típicamente 70-80%) utilizado para que el modelo aprenda los patrones.
* **Conjunto de Validación (*Validation Set*):** (Opcional, a menudo se usa **Validación Cruzada** en su lugar). Se usa para ajustar los hiperparámetros del modelo.
* **Conjunto de Prueba (*Test Set*):** Un conjunto **totalmente invisible** para el modelo (10-20%) utilizado para evaluar el rendimiento final del modelo de manera imparcial.

$$\text{Total Data} = \text{Train} + \text{Validation} + \text{Test}$$

**Con esto, el *dataset* está listo para la Fase de Modelado (Entrenamiento de Algoritmos).**

---
## 📊 Resumen del Flujo de Trabajo de Preparación de Datos
1. **Limpieza Final y Manejo de Faltantes**
    - Imputar o eliminar valores faltantes.
    - Tratar *outliers* y normalizar distribuciones.
2. **Codificación y Transformación de Variables**
    - Codificar variables categóricas.
    - Discretizar variables numéricas si es necesario.
3. **Escalamiento y Normalización**
    - Escalar variables numéricas para algoritmos sensibles a la escala.
4. **Manejo del Desbalanceo y Partición de Datos**
    - Aplicar técnicas de muestreo si el *target* está desbalanceado.
    - Dividir el *dataset* en conjuntos de entrenamiento, validación y prueba.
Con estos pasos, el *dataset* estará optimizado para el modelado de Machine Learning, maximizando las posibilidades de construir modelos precisos y robustos.

# Apéndice I: Transformaciones Específicas según el Modelo de Machine Learning
¿Las transformaciones de datos dependen del modelo de Machine Learning que se va a utilizar?

¡Absolutamente! La elección del modelo de Machine Learning es uno de los principales factores que determinan qué transformaciones son **obligatorias** o **altamente recomendadas** en la fase de preparación de datos.

Mientras que algunas transformaciones son universales (ej., manejar *NaNs*), otras son específicas para satisfacer los supuestos matemáticos de ciertos grupos de modelos.

Aquí tienes un desglose de las transformaciones clave basadas en el tipo de modelo:

---

## ⚙️ Transformaciones Específicas del Modelo
### 1. Modelos Basados en Distancia y Gradiente (Sensibles a la Escala)

Estos modelos calculan distancias entre puntos o convergen ajustando pesos mediante un gradiente, por lo que las características con magnitudes grandes pueden dominar indebidamente el cálculo.

| Modelo(s) | Transformación Requerida | Justificación |
| :--- | :--- | :--- |
| **K-Vecinos más Cercanos (KNN)**, **Máquinas de Vectores de Soporte (SVM)**, **K-Means** | **Escalamiento (Estandarización/Normalización)** | **Requerido:** KNN y K-Means se basan en la distancia euclidiana. Si la variable $X_1$ tiene un rango de 0-1000 y $X_2$ tiene un rango de 0-1, $X_1$ dominará totalmente la distancia. |
| **Regresión Lineal/Logística**, **Redes Neuronales (Deep Learning)** | **Escalamiento (Estandarización)** | **Altamente Recomendado:** El escalamiento acelera la convergencia del algoritmo de optimización (Descenso de Gradiente) y ayuda a evitar que los pesos iniciales se "disparen" en las Redes Neuronales. |
| **Regresión/Clasificación Lineal (Lasso, Ridge)** | **Escalamiento** | **Altamente Recomendado:** Es vital para que la penalización (L1 o L2) se aplique de manera justa a todos los coeficientes. |
| **Variables Categóricas con Alta Cardinalidad** | **One-Hot Encoding** | **Obligatorio:** La mayoría de los modelos lineales no pueden procesar categorías como *strings* directamente. |

---

### 2. Modelos Basados en Árboles (Insensibles a la Escala)

Los modelos basados en árboles (bosques, *boosting*) toman decisiones basadas en umbrales (ej., "¿Es $X > 10.5$?"), por lo que la magnitud absoluta o la distribución de una variable no afecta fundamentalmente su rendimiento.

| Modelo(s) | Transformación Requerida | Justificación |
| :--- | :--- | :--- |
| **Árboles de Decisión**, **Random Forest**, **Gradient Boosting (XGBoost, LightGBM)** | **Ningún escalamiento/normalización.** | **Innecesario:** No usan distancia ni gradiente. La decisión "Edad > 40" es la misma si la Edad está en el rango $[0, 100]$ o $[0, 1]$. |
| **Asimetría (*Skewness*)** | **Ninguna transformación.** | **Innecesario:** Los árboles son robustos a la asimetría y a los *outliers*. De hecho, forzar la normalidad (ej., con logaritmos) a veces puede disminuir su rendimiento al ocultar puntos de corte naturales. |
| **Variables Categóricas** | **Ordinal Encoding** o **Target Encoding.** | **Recomendado:** OHE crea muchas columnas, lo que puede ralentizar los árboles. Usar un *Ordinal Encoding* o *Target Encoding* reduce la dimensionalidad y, a menudo, mejora la velocidad y rendimiento. |

---

### 3. Modelos Basados en Probabilidad y Supuestos Estadísticos

Estos modelos asumen ciertas propiedades sobre la distribución de los datos para que sus cálculos estadísticos sean válidos.

| Modelo(s) | Transformación Requerida | Justificación |
| :--- | :--- | :--- |
| **Análisis de Discriminante Lineal (LDA)** | **Transformación para Normalidad.** | **Altamente Recomendado/Requerido:** Asume que los datos están distribuidos normalmente (Gaussiana) dentro de cada clase y que las matrices de covarianza son iguales. |
| **Regresión Lineal (Modelado Inferencial)** | **Transformación para Linealidad y Homoscedasticidad.** | **Requerido para la Inferencia:** Si se quiere usar el modelo para **explicar** relaciones, se deben cumplir los supuestos de linealidad y residuos normalmente distribuidos. Esto a menudo requiere transformar variables no lineales (ej., con logaritmos). |
| **Naive Bayes (Gaussiano)** | **Transformación para Normalidad.** | **Recomendado:** La versión Gaussiana asume que las variables numéricas siguen una distribución normal. |

---

## 🔑 Resumen de la Regla de Oro

| Grupo de Modelos | Escalamiento | Tratamiento de Asimetría (*Skewness*) |
| :--- | :--- | :--- |
| **Modelos Lineales, Basados en Distancia y NN** | **SI (Estandarización es común)** | SI (Transformar con log/raíz para acercarse a la normalidad). |
| **Modelos Basados en Árboles (RF, GB)** | NO | NO (Son robustos a la asimetría y *outliers*). |