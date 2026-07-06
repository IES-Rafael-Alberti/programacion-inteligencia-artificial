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

# Glosario UD4 — Fundamentos de Redes Neuronales

---

## A

**Activación (función de)**
Función no lineal aplicada a la salida de una neurona para introducir no linealidad. Ejemplos: ReLU, Sigmoid, Tanh.
*Ver: Capítulo 2.4*

**Algoritmo de optimización**
Procedimiento iterativo para ajustar los parámetros de un modelo y minimizar una función objetivo. Ejemplo: Gradiente descendente.
*Ver: Capítulo 7*

---

## B

**Backpropagation**
Algoritmo que calcula eficientemente los gradientes de la pérdida respecto a todos los pesos de una red neuronal, aplicando la regla de la cadena.
*Ver: Capítulo 8*

**Batch (lote)**
Pequeño conjunto de ejemplos procesados juntos durante una iteración del entrenamiento. El batch size es el número de ejemplos en cada lote.
*Ver: Capítulo 7.7*

**Batch Gradient Descent (BGD)**
Variante del gradiente descendente que usa todo el dataset para calcular cada actualización.
*Ver: Capítulo 7.6.1*

**Bias (sesgo)**
Parámetro adicional en una neurona que permite desplazar la función, evitando que esté atada al origen.
*Ver: Capítulo 2.3*

---

## C

**Capa**
Conjunto de neuronas organizadas horizontalmente en una red neuronal. Tipos: entrada, ocultas, salida.
*Ver: Capítulo 2.5*

**Capa oculta**
Capa intermedia en una red neuronal que no está directamente conectada a los datos ni a la salida final. Aprende representaciones internas.
*Ver: Capítulo 2.5*

**Capa de entrada**
Primera capa de una red neuronal que recibe los datos originales sin realizar transformaciones complejas.
*Ver: Capítulo 2.5*

**Capa de salida**
Última capa de una red neuronal que produce la predicción final. Su forma depende del tipo de problema.
*Ver: Capítulo 2.5*

**Clasificación**
Tarea de aprendizaje supervisado donde el objetivo es predecir una etiqueta discreta (clase) a partir de datos.
*Ver: Capítulo 5.5.2 y 5.5.3*

**Convergencia**
Situación en la que un algoritmo de optimización llega a un punto donde los cambios en los parámetros son muy pequeños, indicando que se ha alcanzado un mínimo.
*Ver: Capítulo 7*

---

## D

**Deep Learning**
Subconjunto de las redes neuronales caracterizado por múltiples capas (profundidad), grandes volúmenes de datos y uso de hardware especializado.
*Ver: Capítulo 1.4*

**Derivada**
Medida de cómo cambia una función en un punto específico. En redes neuronales, indica cómo cambia la pérdida al variar un parámetro.
*Ver: Capítulo 6.2*

---

## E

**Entrenamiento**
Proceso iterativo de ajustar los parámetros de una red neuronal para minimizar la función de pérdida usando datos etiquetados.
*Ver: Capítulo 1.5.3, Capítulo 7*

**Epoch (época)**
Una pasada completa a través de todo el conjunto de datos de entrenamiento.
*Ver: Capítulo 7.7*

**Error**
Diferencia entre el valor predicho y el valor real. Cuantificado por la función de pérdida.
*Ver: Capítulo 5*

---

## F

**Feature engineering (ingeniería de características)**
Proceso manual de crear y seleccionar características relevantes para un modelo en ML clásico.
*Ver: Capítulo 1.2*

**Feedforward**
Tipo de red neuronal donde la información fluye solo hacia delante, sin ciclos ni retroalimentación.
*Ver: Capítulo 2.6*

**Función de activación**
Ver: Activación (función de)

**Función de pérdida (Loss function)**
Función que cuantifica el error entre las predicciones del modelo y los valores reales. Guía el entrenamiento.
*Ver: Capítulo 5*

---

## G

**Gradiente**
Vector que contiene las derivadas parciales de la pérdida respecto a todos los parámetros. Indica la dirección de mayor crecimiento de la pérdida.
*Ver: Capítulo 6.4*

**Gradiente descendente**
Algoritmo de optimización que ajusta iterativamente los parámetros en la dirección opuesta al gradiente para minimizar la función de pérdida.
*Ver: Capítulo 7*

**Gradiente descendente estocástico (SGD)**
Variante del gradiente descendente que usa un solo ejemplo (o pocos) para cada actualización.
*Ver: Capítulo 7.6.2*

---

## H

**Hiperparámetro**
Parámetro que controla el comportamiento del algoritmo pero no se aprende durante el entrenamiento. Ejemplo: learning rate.
*Ver: Capítulo 7.5*

---

## I

**Interpretabilidad**
Grado en que es posible entender y explicar cómo un modelo llega a sus predicciones.
*Ver: Capítulo 1.5.4*

---

## L

**Learning rate (tasa de aprendizaje)**
Hiperparámetro que controla el tamaño del paso en cada actualización de parámetros durante el entrenamiento.
*Ver: Capítulo 7.5*

**Loss**
Ver: Función de pérdida

---

## M

**Machine Learning clásico**
Enfoque tradicional de ML usando modelos como regresión lineal, árboles de decisión, SVM, etc.
*Ver: Capítulo 1.1*

**Matriz**
Array bidimensional de números. En redes neuronales, representan pesos entre capas.
*Ver: Capítulo 3.4*

**Mini-batch Gradient Descent**
Variante del gradiente descendente que usa pequeños lotes de datos para cada actualización. Equilibra estabilidad y eficiencia.
*Ver: Capítulo 7.6.3*

**Mínimo global**
Punto donde la función de pérdida alcanza su valor más bajo en todo el espacio de parámetros.
*Ver: Capítulo 7.8*

**Mínimo local**
Punto donde la función de pérdida alcanza un valor bajo en una región, pero no el más bajo globalmente.
*Ver: Capítulo 7.8*

---

## N

**Neurona artificial**
Unidad básica de una red neuronal que recibe entradas, las pondera, suma y aplica una función de activación.
*Ver: Capítulo 2.2*

**No linealidad**
Comportamiento de una función que no es una línea recta. Las funciones de activación introducen no linealidad.
*Ver: Capítulo 2.4*

---

## O

**Optimizador**
Algoritmo que implementa una estrategia para actualizar los parámetros. Ejemplos: SGD, Adam, RMSprop.
*Ver: Capítulo 7.9*

---

## P

**Parámetro**
Valor aprendido durante el entrenamiento. En redes neuronales: pesos y sesgos.
*Ver: Capítulo 2.2*

**Pendiente**
Inclinación de una curva en un punto específico. Relacionada con la derivada.
*Ver: Capítulo 6.2*

**Perceptrón multicapa (MLP)**
Red neuronal feedforward con una o más capas ocultas.
*Ver: Capítulo 2.6*

**Peso (weight)**
Parámetro que indica la importancia de una entrada en una neurona. Se ajusta durante el entrenamiento.
*Ver: Capítulo 2.3*

---

## R

**Red neuronal artificial (RNA)**
Modelo matemático compuesto por capas de neuronas interconectadas, capaz de aprender relaciones complejas en los datos.
*Ver: Capítulo 1.3*

**Regla de la cadena**
Principio matemático que permite calcular derivadas de funciones compuestas. Base de backpropagation.
*Ver: Capítulo 8.4*

**Regresión**
Tarea de aprendizaje supervisado donde el objetivo es predecir un valor continuo.
*Ver: Capítulo 5.5.1*

**Representación interna**
Transformación de los datos que la red aprende internamente, diferente de los datos originales.
*Ver: Capítulo 1.3*

---

## S

**Sesgo**
Ver: Bias

**Sigmoid**
Función de activación que mapea valores a un rango entre 0 y 1. Común en clasificación binaria.
*Ver: Capítulo 2.4*

**Stochastic Gradient Descent (SGD)**
Ver: Gradiente descendente estocástico

**Superficie de pérdida**
Representación geométrica de cómo varía la función de pérdida con respecto a los parámetros del modelo.
*Ver: Capítulo 5.3*

---

## T

**Tanh**
Función de activación que mapea valores a un rango entre -1 y 1.
*Ver: Capítulo 2.4*

**Tensor**
Arreglo multidimensional de números. Generalización de escalares, vectores y matrices.
*Ver: Capítulo 3.5*

**Transformación geométrica**
Cambio en la posición, orientación o escala de datos en el espacio. Las capas neuronales realizan transformaciones.
*Ver: Capítulo 2.7*

---

## V

**Validación**
Evaluación del rendimiento de un modelo en datos que no se usaron durante el entrenamiento.
*Ver: Capítulo 1.1*

**Vector**
Arreglo unidimensional de números. Representa una dirección y magnitud en el espacio.
*Ver: Capítulo 3.3*

---

## Z

**Zona de saturación**
Región donde una función de activación es casi plana, resultando en gradientes muy pequeños que ralentizan el aprendizaje.
*Ver: Capítulo 8.7*

---

## Índice inverso por capítulo

**Capítulo 1:** Activación, Capa de entrada, Clasificación, Deep Learning, Feature engineering, Red neuronal artificial, Representación interna, Validación

**Capítulo 2:** Activación, Bias, Capa, Feedforward, Neurona artificial, No linealidad, Parámetro, Peso

**Capítulo 3:** Matriz, Tensor, Vector

**Capítulo 4:** Transformación geométrica

**Capítulo 5:** Clasificación, Error, Función de pérdida, Regresión, Superficie de pérdida

**Capítulo 6:** Derivada, Gradiente, Pendiente, Regla de la cadena

**Capítulo 7:** Algoritmo de optimización, Batch, BGD, Convergencia, Entrenamiento, Epoch, Gradiente descendente, Hiperparámetro, Learning rate, Mínimo global, Mínimo local, Mini-batch GD, Optimizador, SGD

**Capítulo 8:** Backpropagation, Regla de la cadena, Zona de saturación

