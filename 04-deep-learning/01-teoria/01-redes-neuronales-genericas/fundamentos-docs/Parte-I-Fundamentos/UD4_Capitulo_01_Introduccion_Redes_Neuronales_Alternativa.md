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

# Capítulo 1 — ¿Qué cambia respecto al Machine Learning clásico?

Hasta ahora hemos trabajado con:

* datasets
* EDA
* modelos de Machine Learning clásico
* métricas
* validación

Ahora entramos en **redes neuronales**.
La pregunta clave es:

> **¿Por qué necesitamos algo distinto al ML clásico?**

---

## 1.1 El límite del Machine Learning clásico

### En ML clásico (scikit-learn)

Normalmente seguimos este flujo:

1. Dataset
2. Limpieza
3. **Ingeniería de características**
4. Modelo (regresión, árbol, SVM…)
5. Evaluación

El paso crítico es el **3**.

---

### Metáfora (receta clásica)

Es como seguir una receta donde:

* el cocinero decide **qué ingredientes usar**
* decide **cómo combinarlos**
* y el horno solo ejecuta

Si eliges mal los ingredientes:

* el resultado nunca será bueno
* aunque el horno sea perfecto

---

## 1.2 El cuello de botella: la ingeniería de características

En ML clásico:

* el modelo **no aprende representaciones**
* solo aprende sobre **las variables que le damos**

Ejemplos:

* imágenes → histogramas, bordes, HOG
* texto → TF-IDF, n-grams
* audio → MFCCs

Todo esto lo decide **el humano**.

---

### Consecuencia directa

* Mucho conocimiento experto
* Soluciones muy específicas
* Difícil generalización
* Difícil reutilización del modelo

---

## 1.3 Qué aportan las redes neuronales

Las redes neuronales cambian una cosa clave:

> **Aprenden automáticamente las representaciones**.

---

### En términos de receta

* Ya no decidimos los ingredientes intermedios
* Definimos:

  * una estructura
  * una función de pérdida
* El sistema **ajusta los ingredientes solo**

La receta se **auto-optimiza**.

---

## 1.4 Capas como transformaciones del espacio de datos

Cada capa de una red neuronal:

* toma un espacio de entrada
* lo transforma en otro espacio
* normalmente de mayor capacidad expresiva

Ejemplo:

* entrada: píxeles
* capas intermedias: formas simples
* capas profundas: conceptos abstractos

---

### Interpretación geométrica

Una red neuronal:

* deforma el espacio de entrada
* hasta que las clases son separables

Esto enlaza directamente con:

* fronteras de decisión no lineales
* profundidad de la red
* activaciones

---

## 1.5 Comparación directa: ML clásico vs Redes neuronales

| Aspecto                 | ML clásico       | Redes neuronales |
| ----------------------- | ---------------- | ---------------- |
| Features                | Diseñadas a mano | Aprendidas       |
| Complejidad             | Limitada         | Escalable        |
| No linealidad           | Limitada         | Alta             |
| Interpretabilidad       | Mayor            | Menor            |
| Dependencia del experto | Alta             | Menor            |
| Datos necesarios        | Menos            | Más              |

---

## 1.6 ¿Por qué ahora funcionan y antes no?

Las redes neuronales **no son nuevas**.
Lo nuevo es:

* datasets grandes
* GPUs
* mejores inicializaciones
* mejores optimizadores
* mejores funciones de activación

Sin estos elementos:

* backpropagation existía
* pero no era viable a gran escala

---

## 1.7 Relación con el gradiente y backpropagation

Las redes neuronales:

* tienen **millones de parámetros**
* todos influyen en la pérdida
* todos deben ajustarse

Backpropagation permite:

* calcular todos los gradientes
* de forma eficiente
* en una sola pasada hacia atrás

Sin backprop:

* entrenar una red profunda sería imposible

---

## 1.8 Conexión con lo que ya sabes (muy importante)

Nada de esto sustituye lo anterior:

* seguimos haciendo EDA
* seguimos limpiando datos
* seguimos evaluando métricas
* seguimos validando modelos

Lo que cambia es **dónde ocurre la inteligencia**:

* antes: en el diseño humano
* ahora: en el proceso de entrenamiento

---

## 1.9 ¿Cuándo NO usar redes neuronales?

Esto es clave para informáticos:

* datasets pequeños
* necesidad de interpretabilidad
* tiempos de entrenamiento muy limitados
* modelos simples suficientes

En estos casos:
👉 ML clásico sigue siendo la mejor opción.

---

## 1.10 Conclusión del capítulo

> Las redes neuronales no sustituyen al ML clásico.
> **Lo generalizan.**

Aprender redes neuronales:

* no invalida lo anterior
* lo complementa
* amplía el tipo de problemas que podemos resolver

---
