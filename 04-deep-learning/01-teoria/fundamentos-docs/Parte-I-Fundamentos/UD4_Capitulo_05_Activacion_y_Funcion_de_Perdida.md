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

# Capítulo 5 — Funciones de activación y función de pérdida

## 5.1. Por qué necesitamos funciones de activación

Si una red neuronal solo encadena operaciones lineales, todo el modelo se
comporta como una única transformación lineal.

Consecuencia:
- No puede aprender relaciones complejas
- No puede construir fronteras de decisión no lineales

Las funciones de activación resuelven ese problema porque introducen
**no linealidad** capa a capa.

---

## 5.2. Activaciones más habituales

### 5.2.1. Sigmoid

- Rango: (0, 1)
- Muy usada en salida para clasificación binaria
- Interpretación probabilística

Limitación principal:
- Puede saturarse y producir gradientes pequeños

---

### 5.2.2. ReLU (Rectified Linear Unit)

- Rango: [0, +infinito)
- Activación habitual en capas ocultas
- Entrena más rápido que sigmoid en muchos escenarios

Limitación principal:
- Puede dejar neuronas inactivas (neuronas muertas)

---

### 5.2.3. Softmax

- Convierte un vector de salidas en probabilidades
- La suma de probabilidades es 1
- Se usa en salida para clasificación multiclase

---

## 5.3. Relación entre activación y tipo de problema

La activación de la última capa debe ser coherente con el problema:

- Regresión: salida lineal
- Clasificación binaria: sigmoid
- Clasificación multiclase: softmax

Elegir mal la activación de salida dificulta el entrenamiento y la
interpretación de resultados.

---

## 5.4. Por qué necesitamos una función de pérdida

Una red neuronal produce predicciones, pero para entrenarla necesitamos medir
qué tan buenas o malas son.

> La función de pérdida convierte el error en un número optimizable.

Sin función de pérdida no hay criterio para ajustar parámetros.

![Concepto de Función de Pérdida](images/25_concepto_perdida.png)

---

## 5.5. Qué mide una función de pérdida

La función de pérdida mide la distancia entre:
- Valor real
- Valor predicho

Puede interpretarse como:
- Error
- Coste
- Penalización

Cuanto mayor es la pérdida, peor es el ajuste.
Cuanto menor es la pérdida, mejor es el ajuste.

---

## 5.6. La pérdida como superficie

Podemos imaginar la pérdida como una superficie:

- Cada punto representa un conjunto de parámetros
- La altura representa el error
- El objetivo es encontrar mínimos

En redes neuronales esta superficie suele ser compleja, con múltiples valles y
zonas planas.

![Superficie de Pérdida: de 1 a 2 parámetros](images/26_superficie_perdida.png)

---

## 5.7. Relación entre pérdida y parámetros del modelo

La pérdida depende de:

- Pesos
- Sesgos
- Arquitectura del modelo

Entrenar consiste en modificar esos parámetros para reducir la pérdida.

> Ajustar parámetros para minimizar la pérdida es el núcleo del aprendizaje.

---

## 5.8. Tipos de funciones de pérdida según el problema

### 5.8.1. Regresión

Pérdidas habituales:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

---

### 5.8.2. Clasificación binaria

Pérdida habitual:
- Binary Crossentropy

---

### 5.8.3. Clasificación multiclase

Pérdida habitual:
- Categorical Crossentropy

![Tipos de Funciones de Pérdida: MSE, MAE, BCE, CCE](images/27_tipos_perdida.png)

---

## 5.9. Combinaciones recomendadas: activación + pérdida

| Tipo de problema       | Activación de salida | Función de pérdida        |
| ---------------------- | -------------------- | ------------------------- |
| Regresión              | Lineal               | MSE o MAE                 |
| Clasificación binaria  | Sigmoid              | Binary Crossentropy       |
| Clasificación multiclase | Softmax            | Categorical Crossentropy  |

Esta combinación mejora estabilidad y coherencia durante el entrenamiento.

---

## 5.10. Pérdida vs métricas

No son lo mismo:

- La pérdida guía el entrenamiento
- Las métricas evalúan rendimiento
- La pérdida debe ser diferenciable
- La métrica puede no serlo

Ejemplo:
- Accuracy es útil para interpretar resultados
- Pero no suele usarse como función de pérdida

![Función de Pérdida vs Métricas de Evaluación](images/28_perdida_vs_metricas.png)

---

## 5.11. Minimizar la pérdida: objetivo real del entrenamiento

Entrenar una red neuronal implica:

1. Calcular salida
2. Calcular pérdida
3. Calcular gradientes
4. Actualizar parámetros
5. Repetir

Este ciclo conecta directamente con gradiente descendente y backpropagation.

![Proceso de Entrenamiento: Minimizar la Pérdida](images/29_minimizar_perdida.png)

---

## 5.12. Idea clave del capítulo

> Las activaciones permiten modelar complejidad.
> La pérdida define qué significa aprender bien.

Ambas piezas son necesarias para que el entrenamiento funcione.

---

### 🔜 Siguiente paso lógico

👉 **Capítulo 6 — Derivadas y gradientes (intuición geométrica)**

Conectaremos:
- superficie de pérdida
- pendiente
- dirección de descenso

---

## 5.13. Desde la teoría a la práctica

En los notebooks prácticos verás cómo cambia el entrenamiento al modificar:
- Activación de salida
- Función de pérdida

👉 **Keras Fashion MNIST** en [UD4_01_Red_Neuronal_Keras_Binaria_FashionMNIST.ipynb](../../Parte-2-Pract/UD4_01_Red_Neuronal_Keras_Binaria_FashionMNIST.ipynb)

---

## 5.14. Preguntas de autoevaluación

### Opción múltiple

1. **¿Qué función tienen las activaciones en una red neuronal?**
   - A) Reducir el tamaño del dataset
   - **B) Introducir no linealidad para aprender relaciones complejas**
   - C) Sustituir la función de pérdida
   - D) Evitar el uso de gradientes

2. **¿Qué combinación es más adecuada para clasificación binaria?**
   - A) Softmax + Categorical Crossentropy
   - **B) Sigmoid + Binary Crossentropy**
   - C) Lineal + MSE
   - D) ReLU + MAE

3. **¿Cuál es la diferencia entre pérdida y métrica?**
   - A) Son equivalentes
   - **B) La pérdida entrena; la métrica evalúa**
   - C) La métrica actualiza parámetros
   - D) La pérdida solo se usa al final

### Pregunta corta

4. **Explica por qué una red sin activaciones se comporta como un modelo lineal.** (2-3 líneas)
