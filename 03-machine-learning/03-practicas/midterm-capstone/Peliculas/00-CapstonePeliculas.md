# 🧠 Proyecto de IA — Dataset de películas

En este proyecto trabajarás con un **dataset de películas** para recorrer **todas las fases de un proyecto real de Inteligencia Artificial**, desde el análisis de los datos hasta la evaluación de un modelo.

El objetivo no es solo que el código funcione, sino que **entiendas lo que haces y sepas justificarlo**.

---

## 🧭 Marco de trabajo: CRISP-DM

Usaremos CRISP-DM como guía breve y **iterativa**: no se trata de completar seis casillas, sino de poder justificar las decisiones con evidencia.

| Fase | Evidencia en este capstone |
|---|---|
| Comprensión del problema y datos | objetivo de clasificación/regresión, fuente, variables y límites del dataset. |
| Preparación | EDA, tratamiento de nulos, selección de variables y partición train/test antes de ajustar transformadores. |
| Modelado y evaluación | comparación y ajuste con validación dentro de entrenamiento; evaluación final única sobre test, errores y decisión razonada. |
| Entrega | notebooks reproducibles, conclusiones, limitaciones y defensa oral. |

La [guía CRISP-DM de UD3](../../../01-teoria/05a-marco-crisp-dm.md) explica el marco. Para evitar fuga de datos, imputadores, escaladores, codificadores o selectores se ajustan solo con entrenamiento. Los modelos y sus hiperparámetros se comparan o ajustan con validación cruzada o un conjunto de validación dentro de entrenamiento; el test se usa una sola vez, al final, para evaluar el modelo elegido.

## 📌 Qué vas a hacer

El proyecto se divide en **3 prácticas encadenadas**:

### 🔹 Práctica 1 — Análisis de datos (EDA)

* Explorar el dataset
* Detectar problemas (valores nulos, outliers, variables inútiles)
* Realizar visualizaciones con sentido
* Sacar conclusiones sobre los datos

### 🔹 Práctica 2 — Modelado exploratorio (PyCaret)

* Definir un problema de IA (clasificación o regresión)
* Probar varios modelos con PyCaret
* Comparar métricas mediante validación cruzada o un conjunto de validación dentro de entrenamiento
* Elegir **un modelo** y justificar por qué, sin usar el test para decidir

### 🔹 Práctica 3 — Modelo final

* Implementar el modelo elegido **sin PyCaret**
* Ajustar hiperparámetros mediante validación cruzada o un conjunto de validación dentro de entrenamiento
* Evaluar una única vez el rendimiento final sobre test
* Analizar errores y limitaciones
* Confirmar que cualquier transformación aprendida se ajustó solo con entrenamiento

---

## ⚡ Ampliación GPU (opcional)

Si tienes GPU o acceso a GPU en la nube, puedes:

* usar **cuDF / cuML**
* comparar CPU vs GPU (tiempo, métricas, dificultad)

👉 **Es opcional y no penaliza no hacerlo**.

---

## 📦 Qué tienes que entregar

* Los **3 notebooks completos**:

  * Práctica 1
  * Práctica 2
  * Práctica 3
* Un **documento final de conclusiones** (plantilla proporcionada), con el objetivo, decisiones de datos, métricas, limitaciones y siguiente paso

Formato:

* Notebooks `.ipynb`
* Documento final `.md` o `.pdf`

---

## 🗣️ Defensa oral

Habrá una **defensa oral individual (5–10 minutos)** en la que tendrás que explicar:

* qué problema has resuelto
* qué decisiones has tomado
* qué conclusiones sacas de tu trabajo

> No tendrás que explicar el código línea a línea,
> sino demostrar que **entiendes lo que has hecho**.

---

## 📊 Cómo se evalúa

Se valorará principalmente:

* el análisis de los datos
* la justificación de las decisiones
* la correcta evaluación del modelo
* la capacidad de sacar conclusiones

No basta con que “funcione”.

---

## 💡 Consejo final

Este proyecto se parece mucho a cómo se trabaja **en proyectos reales de IA**.
Si entiendes bien este proceso, estás haciendo **IA de verdad**, no solo ejercicios.
