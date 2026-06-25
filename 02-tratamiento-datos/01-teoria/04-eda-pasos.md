# EDA Exhaustivo: Pasos Detallados para un Análisis Completo
Un Análisis Exploratorio de Datos (EDA) exhaustivo es un proceso iterativo y multifacético. Aunque la secuencia puede variar y no todos los pasos son necesarios para cada *dataset*, tener esta lista completa garantiza que no se omitirá ningún aspecto crítico.

Aquí está una lista exhaustiva de todos los pasos para un EDA completo, organizada en fases lógicas:

## 🧭 Fases de un Análisis Exploratorio de Datos (EDA) Exhaustivo
### Fase 1: Carga, Estructura e Inspección Inicial
El primer paso es entender la forma, el tamaño y la calidad bruta del *dataset*.

1.  **Carga del *Dataset***:
    * Cargar los datos desde la fuente (CSV, SQL, JSON, etc.). Utilizar funciones como `pd.read_csv()` o `pd.read_sql()`.
2.  **Inspección Rápida de la Estructura**:
    * Verificar las dimensiones: `df.shape` (filas y columnas).
    * Mostrar las primeras/últimas filas: `df.head()`, `df.tail()`.
    * Obtener un resumen de la información: `df.info()` (conteo de no-nulos, tipos de datos, uso de memoria).
3.  **Inspección del Tipo de Datos**:
    * Verificar los tipos de datos de cada columna: `df.dtypes`.
    * Identificar variables **numéricas**, **categóricas** (o nominales/ordinales), y de **fecha/hora**.
    * Corregir tipos de datos incorrectos (ej., un número que se leyó como *string*).
4.  **Identificación de la Columna Clave**:
    * Verificar si existe un **identificador único** (`ID` o índice).
    * Evaluar si la columna clave es realmente única (e.g., `df['ID'].nunique() == len(df)`).

---

### Fase 2: Calidad de Datos (Limpieza y Preprocesamiento)
Esta fase se centra en identificar y cuantificar problemas de calidad que podrían sesgar el análisis.

5.  **Manejo de Valores Faltantes (Missing Values)**:
    * **Cuantificación**: Calcular el porcentaje de valores **NaN** por columna.
    * **Análisis del Patrón**: Determinar si los datos faltan de forma aleatoria (MCAR), por causas relacionadas con otras variables (MAR) o no aleatoria (MNAR).
    * **Decisión de Imputación/Eliminación**: Planificar cómo se manejarán los valores faltantes (imputación por media/mediana/moda, eliminación de filas/columnas, o técnicas avanzadas).
6.  **Manejo de Duplicados**:
    * **Identificación**: Detectar filas completamente duplicadas: `df.duplicated().sum()`.
    * **Eliminación**: Eliminar filas duplicadas, eligiendo conservar la primera, la última o ninguna.
7.  **Detección y Manejo de *Outliers* (Valores Atípicos)**:
    * **Identificación Gráfica**: Utilizar **diagramas de caja** (`boxplot`) o histogramas.
    * **Identificación Estadística**: Utilizar el Rango Intercuartílico (IQR), Z-score o métodos más robustos (como DBSCAN o Isolation Forest).
    * **Manejo**: Planificar el *clamping* (limitación), la transformación (logarítmica) o la eliminación, justificando la elección.
8.  **Corrección de Errores de Entrada de Datos (*Data Entry Errors*)**:
    * Para variables categóricas, buscar variaciones de un mismo valor (ej., "NY", "New York", "N.Y.").
    * Unificar el formato de *strings* (ej., convertir a minúsculas, eliminar espacios en blanco).

---

### Fase 3: Análisis Univariado (Columna por Columna)
Se exploran las características de cada variable individualmente.

9.  **Análisis de Variables Numéricas**:
    * **Estadísticas Descriptivas**: Calcular `df.describe()` (media, mediana, desviación estándar, cuartiles).
    * **Distribución de Frecuencias**: Visualizar con **Histogramas** para ver la forma de la distribución (normal, sesgada).
    * **Medición de Asimetría (*Skewness*) y Curtosis (*Kurtosis*)**: Cuantificar el sesgo y la "pesadez" de las colas de la distribución.
10. **Análisis de Variables Categóricas**:
    * **Conteo de Frecuencia**: `Series.value_counts()` para ver la distribución de categorías.
    * **Visualización**: Usar **diagramas de barras** para comparar la frecuencia de cada categoría.
    * **Cardinalidad**: Identificar variables con alta cardinalidad (demasiados valores únicos), que podrían requerir ser agrupadas o eliminadas.
11. **Análisis de Variables de Fecha/Hora**:
    * **Rango Temporal**: Identificar la fecha mínima y máxima para establecer el periodo de los datos.
    * **Extracción de Componentes**: Crear nuevas variables (año, mes, día de la semana) a partir de la columna de fecha.

---

### Fase 4: Análisis Bivariado y Multivariado (Relaciones)
Se explora la relación entre pares de variables y entre grupos de variables.

12. **Análisis de Correlación**:
    * **Cálculo**: Generar la **matriz de correlación** entre todas las variables numéricas (`df.corr()`).
    * **Visualización**: Usar un **mapa de calor** (`heatmap`) para visualizar la fuerza y dirección de las correlaciones. 
    * **Identificación de Multicolinealidad**: Detectar variables altamente correlacionadas que podrían inflar los modelos predictivos.
13. **Relación Numérica vs. Numérica**:
    * **Diagramas de Dispersión (*Scatter Plots*)**: Visualizar la relación entre pares de variables.
14. **Relación Categórica vs. Numérica**:
    * **Diagramas de Caja (*Box Plots*) o de Violín**: Comparar la distribución de una variable numérica a través de diferentes categorías. (Ej., Edad vs. Supervivencia).
    * **Gráficos de Barras Agrupadas**: Mostrar la media o suma de la variable numérica por categoría.
15. **Relación Categórica vs. Categórica**:
    * **Tablas de Contingencia**: Generar tablas de frecuencia cruzada (`pd.crosstab()`).
    * **Gráficos de Barras Apiladas/Agrupadas**: Visualizar la distribución conjunta.

---

### Fase 5: Preguntas Dirigidas y *Feature Engineering*
Se aplican transformaciones y se explora el *dataset* en el contexto del problema específico.

16. **Análisis Dirigido a la Variable Objetivo (*Target Variable*)**:
    * Si el objetivo es predecir `Y`, analizar exhaustivamente la relación de cada variable (`X`) con `Y` (ej., para la clasificación, ver la distribución de cada `X` entre las clases de `Y`).
17. **Ingeniería de Características (*Feature Engineering*)**:
    * **Creación de Nuevas Características**: Generar variables que capturen mejor la información (ej., a partir de Nombre, crear "Título" (Sr., Sra.); o calcular ratios entre columnas).
    * **Discretización/Cuantificación**: Convertir variables continuas a categóricas usando `pd.cut()` o `pd.qcut()`.
    * **Normalización/Escalado**: Planificar transformaciones para modelos que requieren datos escalados.
18. **Análisis de *Skewness* y Transformación**:
    * Aplicar transformaciones logarítmicas o de raíz cuadrada a variables numéricas sesgadas para que se aproximen a una distribución normal (útil para muchos modelos predictivos).

---
### Fase 6: Resumen e Informe Final
Documentación y comunicación de los hallazgos.

19. **Resumen de Hallazgos Clave**:
    * Documentar las principales ideas: variables con mayor poder predictivo, distribuciones anómalas, *outliers* críticos y decisiones de limpieza tomadas.
20. **Informe de EDA (Automatizado o Manual)**:
    * Generar un informe final (HTML, Notebook, o PDF) que contenga todas las visualizaciones y conclusiones para comunicar el conocimiento adquirido a las partes interesadas. (Aquí es donde brillan herramientas como **Pandas Profiling** o **Sweetviz**).

Al seguir estos pasos, se garantiza una comprensión profunda del *dataset*, identificando tanto sus fortalezas como sus debilidades antes de pasar a la fase de modelado.
---

# Apéndice I: Relación entre Variable Predictora y Target
 Entender la relación entre una variable (predictora) y la variable objetivo (*target*) es el corazón del EDA. El tipo de análisis y las herramientas estadísticas/gráficas cambian drásticamente según la naturaleza de ambas variables.

A continuación, se detalla un análisis exhaustivo para cada una de las cuatro combinaciones posibles, utilizando las metodologías más comunes:

---

## 1. Variable Categórica vs. Target Categórico (Clasificación)

En este escenario, ambas variables representan grupos o categorías. El objetivo es ver si la distribución de una categoría influye en la otra.

| Análisis Clave | Herramientas y Gráficos | Objetivo Principal |
| :--- | :--- | :--- |
| **Tablas de Contingencia** | `pd.crosstab()`, Tablas de Frecuencia Cruzada, Porcentajes por Fila/Columna. | Contar la co-ocurrencia de categorías. Permite ver cuántos casos de Categoría A (Target) caen dentro de la Categoría X (Variable). |
| **Análisis de Proporciones** | **Gráficos de Barras Apiladas** (Stacked Bar Charts).  | Visualizar la distribución relativa. Por ejemplo: ¿Qué porcentaje de la Categoría X sobrevivió (Target)? |
| **Prueba Chi-Cuadrado** | Prueba estadística $H_0$: Las variables son independientes. | **Evaluar la significancia estadística** de la relación. Si el p-valor es bajo, la relación es estadísticamente significativa. |
| **Métricas de Asociación** | V de Cramer, Coeficiente de Contingencia. | Cuantificar la **fuerza de la asociación** entre las dos variables categóricas. |

---

## 2. Variable Numérica vs. Target Categórico (Clasificación)

Este es un caso fundamental en los problemas de clasificación, donde se busca si los valores de una variable continua difieren significativamente entre los grupos del *target*.

| Análisis Clave | Herramientas y Gráficos | Objetivo Principal |
| :--- | :--- | :--- |
| **Análisis de Distribución por Clase** | **Histogramas Superpuestos** o **Gráficos de Densidad (KDE)**.  | Visualizar si la distribución de la variable numérica es diferente para cada clase del *target*. Una buena separación indica una característica predictiva fuerte. |
| **Análisis de Medidas Centrales** | **Diagramas de Caja (*Box Plots*)** y **Diagramas de Violín** por categoría. | Comparar la **media, mediana y dispersión** de la variable numérica en cada clase. Muestra si hay diferencias claras en los valores típicos (ej., ¿La media de Edad de los sobrevivientes es diferente a la de los no-sobrevivientes?). |
| **Pruebas de Diferencia de Medias** | **ANOVA** (para más de dos clases en el *target*) o **Prueba T de Student** (para un *target* binario). | Determinar si la diferencia entre las medias de los grupos es **estadísticamente significativa**. |
| **Curvas ROC (Receiver Operating Characteristic)** | Curvas ROC si la variable se usa como clasificador simple. | Evaluar la capacidad predictiva de la variable por sí sola. |

---

## 3. Variable Categórica vs. Target Numérico (Regresión)

Aquí se busca si las categorías de la variable predictora tienen un impacto distinto en el valor promedio de la variable *target* continua.

| Análisis Clave | Herramientas y Gráficos | Objetivo Principal |
| :--- | :--- | :--- |
| **Medias y Desviaciones por Grupo** | Tablas que muestran la **Media, Mediana y Desviación Estándar** del *Target* para cada categoría de la Variable. | Cuantificar la diferencia en el valor central (ej., ¿Cuál es el precio promedio de las casas con techo de teja vs. las de techo de metal?). |
| **Análisis de Variación** | **Diagramas de Caja (*Box Plots*)** y **Diagramas de Violín** (uno por cada categoría).  | Visualizar la **dispersión y los *outliers*** de los valores del *target* dentro de cada categoría. Una gran diferencia en la media o mediana entre cajas indica una relación fuerte. |
| **Prueba de ANOVA** | Análisis de Varianza. $H_0$: Las medias del *target* en los diferentes grupos categóricos son iguales. | **Evaluar la significancia estadística** de que la variable categórica impacte la media del *target*. |
| **Agrupación (*Feature Engineering*)** | Si hay alta cardinalidad, agrupar las categorías con medias similares. | Crear una **nueva característica** más informativa y con menos categorías. |

---

## 4. Variable Numérica vs. Target Numérico (Regresión)

Ambas son variables continuas. El foco está en la dirección, la fuerza y la forma (lineal o no lineal) de la asociación.

| Análisis Clave | Herramientas y Gráficos | Objetivo Principal |
| :--- | :--- | :--- |
| **Correlación de Pearson** | Coeficiente $r$, matriz de correlación. | **Cuantificar la fuerza y dirección de la relación lineal**. Un valor cercano a 1 o -1 indica una relación lineal fuerte. |
| **Diagrama de Dispersión** | ***Scatter Plot***. 

[Image of a scatter plot showing the relationship between two numerical variables]
 | **Visualizar la forma de la relación**. Permite identificar rápidamente si la relación es: **Lineal** (fácil de modelar), **No Lineal** (requiere transformación) o si no existe relación. |
| **Detección de *Outliers*** | *Scatter Plot* con puntos etiquetados, Análisis de Residuos. | Identificar puntos que se alejan de la tendencia general y que podrían sesgar la correlación y el modelo de regresión. |
| **Transformación (Logarítmica, Raíz, etc.)** | Aplicar transformaciones para **linealizar la relación** si es curva o para **reducir la asimetría** de las variables. | Mejorar el ajuste del modelo de regresión lineal. |
| **Prueba de Correlación** | Prueba T o F para evaluar la **significancia estadística** del coeficiente de correlación. | Determinar si la correlación observada es probablemente real y no producto del azar. |

---
¡Esa es una de las preguntas más críticas en la ciencia de datos! Cuando el *target* categórico no está balanceado (hay muchas más instancias de una clase que de otras, por ejemplo, 95% "No" y 5% "Sí"), el análisis de las relaciones puede ser engañoso y los modelos predictivos fallarán.

A continuación, se detalla qué análisis se pueden hacer y las técnicas de preprocesamiento para manejar *datasets* **desbalanceados (*imbalanced datasets*)**:

---
# Apendice II: Análisis y Técnicas para Variables Predictoras con Target Categórico Desbalanceado
## ⚖️ Análisis con Clases Desbalanceadas

Cuando el *target* categórico está desbalanceado, los análisis deben centrarse en la **proporción de la clase minoritaria** dentro de cada grupo.

### 1. Ajuste en el Análisis Categórico vs. Target Categórico
* **Enfoque en Proporciones Condicionales:** No mires el conteo total, mira el porcentaje.
    * **Herramienta:** **Tablas de Contingencia con Porcentajes de Fila/Columna**.
    * **Análisis Clave:** Evaluar la **tasa de éxito** (proporción de la clase minoritaria) para cada categoría de la variable predictora. Si la tasa de éxito de la Categoría A es 10% y la media general es 5%, esa Categoría A es importante.
    * **Gráfico Ajustado:** Usar **Gráficos de Barras Apiladas Normalizadas** (al 100%). Esto fuerza a que todas las barras tengan la misma altura, permitiendo comparar visualmente las proporciones (porcentajes) de la clase minoritaria entre las diferentes categorías.

### 2. Ajuste en el Análisis Numérico vs. Target Categórico
* **Enfoque en la Separación de Distribuciones:**
    * **Herramienta:** **Gráficos de Densidad (KDE) o Violin Plots**.
    * **Análisis Clave:** Observar si la distribución de la variable numérica para la **clase minoritaria** está claramente separada o tiene una moda diferente a la de la clase mayoritaria. Incluso si la clase minoritaria tiene menos puntos, si esos pocos puntos se agrupan en un rango numérico específico, esa variable será predictiva.
    * **Métrica:** La **superficie de solapamiento** entre las curvas de densidad de las dos clases indica la calidad predictiva de la variable.

---

## 🛠️ Técnicas de Preprocesamiento y Modelado
Para corregir el desbalanceo antes de entrenar un modelo o para realizar un EDA más representativo, se aplican técnicas que modifican el *dataset* o ajustan el proceso de entrenamiento.

### 1. Técnicas de Muestreo (Sampling)
Estas técnicas buscan nivelar el número de instancias por clase modificando el *dataset*.

| Técnica | Descripción | Riesgo |
| :--- | :--- | :--- |
| **Sobremuestreo (*Oversampling*)** | Aumentar artificialmente el número de instancias de la **clase minoritaria** duplicando o sintetizando nuevos datos. | Puede llevar a un **sobreajuste (*overfitting*)**, ya que el modelo solo aprende a clasificar correctamente las copias o datos muy cercanos a los originales. |
| **SMOTE (Synthetic Minority Over-sampling Technique)** | Un método avanzado que crea **ejemplos sintéticos** de la clase minoritaria interpolando entre los ejemplos existentes, sin simplemente duplicarlos. | Más efectivo que la duplicación simple, pero aún puede introducir ruido si las fronteras de clase son complejas. |
| **Submuestreo (*Undersampling*)** | Reducir el número de instancias de la **clase mayoritaria** eliminando datos aleatoriamente. | Riesgo de **perder información valiosa** contenida en los ejemplos eliminados de la clase mayoritaria. |
| **Tomek Links / NearMiss** | Métodos avanzados de submuestreo que eliminan instancias de la clase mayoritaria cercanas a la frontera de decisión para limpiar el espacio de clases. | Conserva la información más relevante de la clase mayoritaria. |

### 2. Enfoques a Nivel de Algoritmo y Evaluación
Estas técnicas no modifican el *dataset*, sino cómo el modelo lo aprende o cómo evaluamos su rendimiento.

* **Ajuste de Pesos de Clase (*Class Weights*)**:
    * Muchos algoritmos (como Árboles de Decisión, Bosques Aleatorios y Regresión Logística en *scikit-learn*) permiten asignar un **mayor peso** a los errores cometidos en la **clase minoritaria**. Esto hace que el modelo "penalice" más la mala clasificación de esa clase.
* **Métricas Adecuadas de Evaluación**:
    * **Nunca uses la Precisión (*Accuracy*)** como métrica principal, ya que un modelo puede tener 95% de precisión simplemente prediciendo siempre la clase mayoritaria.
    * Utiliza:
        * **Recall (Sensibilidad):** Importante si no quieres perderte ningún positivo (ej., detección de enfermedades).
        * **Precision (Valor Predictivo Positivo):** Importante si quieres asegurar que tus positivos son correctos (ej., envío de correos de marketing costosos).
        * **F1-Score:** La media armónica de Precision y Recall, útil para un equilibrio.
        * **Área bajo la curva ROC (AUC-ROC):** La mejor métrica para evaluar el poder discriminatorio del modelo, independientemente del umbral de clasificación.
* **Algoritmos Específicos**:
    * Algoritmos basados en árboles como **Bosques Aleatorios (*Random Forests*)** a menudo manejan el desbalanceo de manera más robusta que los modelos lineales.
* **Aprendizaje con Detección de Anomalías**:
    * Si el desbalanceo es extremo (por ejemplo, 1:1000), a veces es más efectivo tratar el problema como una **Detección de Anomalías** (la clase minoritaria es la anomalía) en lugar de un problema de clasificación binaria tradicional.




## 🧭 ¿Cuándo Ocurre el Análisis de Desbalanceo?

### 1. La Fase de EDA (Análisis)
El EDA tiene como objetivo **diagnosticar problemas** y **entender las relaciones**.

* **Identificación del Problema (Paso 1 del EDA):** En la Fase 3 del EDA (Análisis Univariado), debes usar `Series.value_counts()` sobre la variable *target*. Si la proporción entre las clases es extrema (ej., 95% vs. 5%), inmediatamente **diagnosticas el desbalanceo**.
* **Análisis del Impacto (Paso 2 del EDA):** En la Fase 4 (Análisis Bivariado), utilizas gráficos como el **Gráfico de Barras Apiladas Normalizadas** para ver si la variable predictora tiene poder predictivo *a pesar* del desbalanceo. Si una categoría del predictor tiene una tasa de éxito del 20% (mientras que la tasa base es del 5%), esa variable es valiosa, aunque el *dataset* esté desbalanceado.

**Conclusión en el EDA:** El EDA te dice: **"Hay un problema grave de desbalanceo y estas variables *podrían* ayudar a resolverlo."**

---

### 2. La Fase Posterior: Preparación de Datos (Pre-Modelado)

Una vez que el EDA ha identificado y cuantificado el desbalanceo, las **soluciones de muestreo y ponderación** pasan a la fase de preparación de datos, ya que modifican el *dataset* que será consumido por el modelo.

* **Aplicación de Soluciones:** Aquí se toman decisiones críticas que afectan directamente el entrenamiento del modelo:
    * **Muestreo:** Aplicar **SMOTE** (Sobremuestreo) o **Tomek Links** (Submuestreo) para equilibrar las clases. *Esta es una transformación del dataset que ocurre justo antes del entrenamiento.*
    * **Ajuste de Hiperparámetros:** Decidir qué algoritmos usar (ej., *Random Forest*) y cómo configurar los **pesos de clase** para penalizar los errores en la clase minoritaria.
    * **Definición de Métricas:** Establecer que se utilizarán métricas robustas como **F1-Score** o **AUC-ROC** en lugar de *Accuracy*.

**Conclusión en la Preparación de Datos:** En esta fase, **actúas** sobre el diagnóstico del EDA.

### Resumen del Flujo de Trabajo

| Pregunta | Fase del Proyecto | Herramientas Típicas |
| :--- | :--- | :--- |
| **¿Existe desbalanceo y cómo se ve?** | **Análisis Exploratorio de Datos (EDA)** | `value_counts()`, Gráficos de Proporción, KDE. |
| **¿Cómo arreglamos el desbalanceo para entrenar?** | **Preparación/Preprocesamiento de Datos** | SMOTE, `class_weight='balanced'`, Submuestreo. |