---
editor_options: 
  markdown: 
    wrap: 72
output: 
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true 
    fig_caption: true
    latex_engine: xelatex
---

# Capítulo 1 — Del Machine Learning clásico a las Redes Neuronales

## 1.1. Punto de partida: qué sabemos hasta ahora

En las unidades anteriores hemos trabajado con **Machine Learning clásico**, utilizando librerías como:

- pandas, seaborn, matplotlib (análisis y visualización)
- scikit-learn, cuML (modelos y métricas)
- Técnicas de validación y selección de modelos
- Despliegue básico de modelos (Streamlit, FastAPI)

Estos modelos se basan, en general, en la siguiente idea:

> Dado un conjunto de datos bien estructurados y unas características adecuadas, es posible aprender una función que relacione entradas con salidas.

Ejemplos típicos:
- Regresión lineal
- Árboles de decisión
- Random Forest
- KNN
- SVM

En muchos casos, estos modelos **funcionan muy bien** y siguen siendo la mejor opción.

---

## 1.2. Limitaciones del Machine Learning clásico

A medida que los problemas se vuelven más complejos, aparecen limitaciones claras:

![ML Clásico vs Redes Neuronales](images/01_ML_clasico_vs_RNA.png)

- Dependencia fuerte del **feature engineering manual**
- Dificultad para modelar relaciones muy no lineales
- Problemas con datos de alta dimensionalidad
- Escalabilidad limitada en algunos algoritmos
- Dificultad para trabajar con datos no estructurados

Ejemplos de situaciones problemáticas:
- Muchas variables con interacciones complejas
- Datos secuenciales (tiempo, texto)
- Datos como imágenes, audio o vídeo
- Casos donde no sabemos *a priori* qué características son relevantes

Aquí es donde empiezan a aparecer las **redes neuronales artificiales**.

---

## 1.3. Qué son las Redes Neuronales Artificiales

Una **red neuronal artificial** es un modelo matemático que:

- Está formado por **capas de unidades simples** (neuronas artificiales)
- Aplica transformaciones lineales y no lineales
- Aprende ajustando sus parámetros a partir de datos

![Arquitectura de una Red Neuronal Simple](images/03_arquitectura_RNA_simple.png)

Conceptualmente, una red neuronal es:

> Un sistema capaz de aprender una representación interna de los datos, sin necesidad de definir explícitamente todas las características a mano.

Es importante destacar algo clave:

> Las redes neuronales **no son nuevas**.  
> Existen desde hace décadas y preceden al término *Deep Learning*.

---

## 1.4. Redes neuronales ≠ Deep Learning

Aquí conviene aclarar una confusión muy habitual.

![Redes Neuronales vs Deep Learning](images/02_RNA_vs_DeepLearning.png)

### Redes neuronales artificiales
- Incluyen:
  - Perceptrón
  - Perceptrón multicapa (MLP)
  - Redes feedforward clásicas
- Pueden tener pocas capas
- Funcionan con datasets relativamente pequeños
- Se entrenan con gradiente descendente y backpropagation

### Deep Learning
- Es un **subconjunto** de las redes neuronales
- Se caracteriza por:
  - Muchas capas (profundidad)
  - Uso intensivo de tensores
  - Grandes volúmenes de datos
  - Hardware especializado (GPU)
- Incluye arquitecturas específicas:
  - CNN
  - RNN
  - LSTM / GRU
  - Transformers

En esta unidad empezamos por **las bases comunes**, que son las mismas para todas ellas.

---

## 1.5. Qué cambia respecto al ML clásico

Cuando pasamos de ML clásico a redes neuronales, cambian varias cosas importantes:

![Características Manuales vs Aprendidas](images/05_caracteristicas_manual_vs_aprendidas.png)

### 1.5.1. Representación de los datos
- Los datos dejan de verse solo como tablas
- Se trabajan como **vectores, matrices y tensores**
- El modelo aprende transformaciones internas de esos datos

### 1.5.2. Aprendizaje de características
- En ML clásico, las características se diseñan manualmente
- En redes neuronales, el modelo aprende representaciones intermedias

### 1.5.3. Entrenamiento
- El entrenamiento se basa en:
  - Función de pérdida
  - Derivadas
  - Gradiente descendente
- Es un proceso iterativo y continuo

![Proceso de Entrenamiento](images/04_proceso_entrenamiento.png)

### 1.5.4. Interpretabilidad
- Los modelos suelen ser menos explicables
- A cambio, pueden modelar relaciones más complejas

---

## 1.6. Qué papel juegan las matemáticas

Las matemáticas en redes neuronales **no son un fin en sí mismas**.

Se utilizan porque:
- Permiten representar datos complejos de forma uniforme
- Hacen posible optimizar modelos automáticamente
- Permiten entrenar modelos con millones de parámetros

En esta unidad:
- No se busca memorizar fórmulas
- Se busca **entender el significado** de:
  - vectores
  - matrices
  - tensores
  - gradientes
  - derivadas
  - backpropagation

La intuición es más importante que el formalismo.

---

## 1.7. Qué veremos en esta unidad (UD4)

En esta unidad vamos a:

- Entender qué es una red neuronal y cómo funciona
- Comprender la base matemática necesaria para entrenarlas
- Construir redes neuronales sencillas
- Compararlas con modelos de ML clásico
- Entender cuándo aportan valor y cuándo no

Y **no** vamos a:
- Entrar en demostraciones matemáticas formales
- Profundizar todavía en arquitecturas avanzadas
- Sustituir el ML clásico por redes neuronales sin criterio

---

## 1.8. Relación con las siguientes unidades

Este capítulo sienta las bases para:

- Deep Learning con Keras y PyTorch
- Redes convolucionales (visión)
- Redes recurrentes y modelos secuenciales
- Transformers y modelos de lenguaje
- Uso de GPU y aceleradores

---

## 1.9. Idea clave para el alumno

> Las redes neuronales no sustituyen al Machine Learning clásico.  
> Lo amplían.

Saber **cuándo usar cada enfoque** es una de las competencias más importantes en Inteligencia Artificial.

---

## 1.10. Desde la teoría a la práctica

Una vez tengas clara la motivación detrás de las redes neuronales, estará bien que veas cómo se usan en la práctica.

👉 **Primera implementación práctica**: [Red Neuronal Binaria con Keras (Fashion MNIST)](../../Parte-2-Pract/UD4_01_Red_Neuronal_Keras_Binaria_FashionMNIST.ipynb)

---

## 1.11. Preguntas de autoevaluación

### Opción múltiple

1. **¿Cuál es la principal limitación del Machine Learning clásico que motiva el uso de redes neuronales?**
   - A) Es demasiado rápido  
   - **B) Requiere ingeniería manual de características**  
   - C) No usa derivadas  
   - D) Solo funciona con datos numéricos

2. **¿Qué característica NO es típica del Deep Learning?**
   - A) Múltiples capas ocultas  
   - B) Grandes volúmenes de datos  
   - **C) Ingeniería manual exhaustiva de características**  
   - D) Uso de GPUs

3. **¿Cuál es la diferencia fundamental entre el aprendizaje automático clásico y una red neuronal en términos de extracción de características?**
   - A) El ML clásico usa más datos  
   - **B) La RNA las aprende automáticamente; el ML clásico las requiere definidas manualmente**  
   - C) La RNA es más lenta  
   - D) El ML clásico es más moderno

### Pregunta corta

4. **¿Por qué es importante que una red neuronal tenga capas ocultas?** (2-3 líneas)