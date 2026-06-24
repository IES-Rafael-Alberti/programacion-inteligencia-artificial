---
editor_options:
  markdown:
    wrap: 72
output:
  word_document:
    toc: true
    toc_depth: '2'
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true
    fig_caption: true
    latex_engine: xelatex
---

# Capítulo 5 — Funciones de activación y funciones de pérdida

*(cómo aprende una red neuronal y hacia dónde la guiamos)*

Hasta ahora sabemos que:

* una red neuronal es una sucesión de transformaciones
* el entrenamiento busca minimizar una función de pérdida
* backpropagation calcula gradientes

Pero falta responder a dos preguntas clave:

> **1. Por qué una red neuronal puede aprender relaciones complejas**
> **2. Cómo le decimos qué significa “hacerlo bien”**

Aquí entran:

* las **funciones de activación**
* las **funciones de pérdida**

---

## 5.1 El problema sin funciones de activación

Imaginemos una red **sin activaciones**:

* solo capas densas
* solo multiplicaciones y sumas

Matemáticamente:

* varias capas lineales seguidas
* equivalen a **una sola capa lineal**

---

### Consecuencia

Sin activaciones:

* la red **no puede aprender relaciones no lineales**
* no importa cuántas capas pongamos

---

### Metáfora (receta)

Es como:

* repetir el mismo paso de cocina una y otra vez
* sin cambiar nunca la técnica

El resultado:

* siempre sabe “parecido”
* no hay riqueza ni complejidad

---

## 5.2 Funciones de activación: introducir no linealidad

Las **funciones de activación** se aplican tras cada capa y permiten:

* introducir no linealidad
* modelar relaciones complejas
* deformar el espacio de datos

---

### Idea clave

> Las activaciones son lo que hace que una red neuronal **no sea solo álgebra lineal**.

---

## 5.3 Activaciones más habituales

### 5.3.1 Sigmoid

* Rango: (0, 1)
* Interpretación probabilística
* Muy usada en:

  * clasificación binaria
  * capa de salida

```python
tf.keras.layers.Dense(1, activation="sigmoid")
```

**Problemas**:

* saturación
* gradientes pequeños (vanishing gradients)

---

### Metáfora

Un interruptor “suave”:

* decide cuánto pasa
* pero puede quedarse atascado

---

### 5.3.2 ReLU (Rectified Linear Unit)

* Rango: [0, ∞)
* Simple y eficiente
* Activación por defecto en capas ocultas

```python
tf.keras.layers.Dense(128, activation="relu")
```

**Ventajas**:

* entrenamiento rápido
* gradientes más estables

**Inconvenientes**:

* neuronas muertas

---

### Metáfora

Un filtro:

* deja pasar lo positivo
* bloquea lo negativo

---

### 5.3.3 Softmax

* Convierte salidas en una distribución de probabilidad
* Usada en clasificación multiclase

```python
tf.keras.layers.Dense(10, activation="softmax")
```

---

### Interpretación

> “De todas las opciones posibles, ¿cuál es más probable?”

---

## 5.4 Activaciones y geometría del espacio

Cada activación:

* cambia la forma del espacio de datos
* permite crear fronteras de decisión complejas

![Image](https://www.researchgate.net/publication/376188282/figure/fig4/AS%3A11431281209230008%401701711509941/Comparison-of-Decision-Boundaries-with-Different-Activation-Functions-for-Binary.ppm)

![Image](https://global.discourse-cdn.com/dlai/original/3X/b/f/bf766249114e7b28e8de6f8d015cd593e6baad09.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A2000/1%2ADS1v5jEBZXwbK7RFyWPkFQ.png)

Este punto conecta directamente con:

* lo que vieron en el EDA
* las visualizaciones de fronteras de decisión

---

## 5.5 Funciones de pérdida: definir qué significa equivocarse

La función de pérdida responde a:

> **¿Qué tan mala es la predicción del modelo?**

Es el **objetivo** del entrenamiento.

---

### Metáfora (receta)

* El sabor final es malo
* La función de pérdida cuantifica *cuán malo*
* Backpropagation decide *qué ingredientes ajustar*

---

## 5.6 Funciones de pérdida más comunes

### 5.6.1 Binary Crossentropy

* Clasificación binaria
* Salida sigmoide

```python
loss="binary_crossentropy"
```

Usada en:

* zapato vs no-zapato
* bolsa vs resto

---

### 5.6.2 Categorical Crossentropy

* Clasificación multiclase
* Salida softmax

```python
loss="categorical_crossentropy"
```

---

### 5.6.3 Mean Squared Error (MSE)

* Regresión

```python
loss="mse"
```

Penaliza errores grandes de forma cuadrática.

---

## 5.7 Elegir activación y pérdida (tabla clave)

| Problema              | Activación salida | Pérdida                  |
| --------------------- | ----------------- | ------------------------ |
| Clasificación binaria | Sigmoid           | Binary Crossentropy      |
| Multiclase            | Softmax           | Categorical Crossentropy |
| Regresión             | Lineal            | MSE                      |

👉 **Esta tabla vale oro para el alumnado.**

---

## 5.8 Relación con backpropagation

Las funciones de activación y pérdida determinan:

* la forma de la superficie de pérdida
* cómo fluyen los gradientes
* si el entrenamiento es estable o no

Una mala elección puede provocar:

* entrenamiento lento
* gradientes que desaparecen
* resultados pobres

---

## 5.9 Conexión con el código (lo que ya han visto)

En Keras:

```python
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
```

Aquí se define **todo el comportamiento del aprendizaje**:

* qué se optimiza
* cómo se mide
* cómo fluye el gradiente

---

## 5.10 Conclusión del capítulo

> Las funciones de activación determinan **qué puede aprender** la red.
> Las funciones de pérdida determinan **qué considera un error**.

Sin una buena combinación:

* el modelo entrena
* pero no aprende bien

---

## Dónde estamos ahora (importante)
✔ Diferencias con ML clásico
✔ Fundamentos matemáticos
✔ Activaciones y pérdidas
✔ Gradiente descendente
✔ Backpropagation


