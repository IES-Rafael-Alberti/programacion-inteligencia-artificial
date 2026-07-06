---
title: "Transformers 7: Comparativa con LSTM y GRU"
output:
  html_document:
    toc: true
    toc_depth: 2
    toc_float: true
    number_sections: true
    fig_caption: true
    code_folding: hide
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true
    fig_caption: true
    latex_engine: xelatex
---


# 🔁 LSTM / GRU: ¿Qué limita el tamaño de la secuencia?
La diferencia en cómo procesan las secuencias las **LSTM/GRU** frente a los **modelos Transformer** tiene implicaciones directas sobre el **tamaño máximo de la secuencia** que pueden manejar de forma eficiente. Vamos a verlo en detalle:

### 1. **Procesamiento secuencial**

* Tanto LSTM como GRU procesan la secuencia **paso a paso**, es decir, **cada paso depende del anterior**.
* Esto implica que **no se puede paralelizar** el procesamiento a lo largo de la secuencia.
* Cuanto más larga la secuencia, más operaciones secuenciales se necesitan → **más lentitud**.

### 2. **Vanishing/Exploding Gradients**

* Aunque LSTM y GRU están diseñados para mitigar este problema (mejor que RNN), aún sufren:

  * **Pérdida de información** al retropropagar el gradiente en secuencias muy largas.
  * La “memoria” se diluye.

### 3. **Uso limitado de contexto lejano**

* Aunque en teoría pueden recordar información lejana, en la práctica se **concentran en el contexto reciente** (por el olvido controlado).
* Esto limita su capacidad de aprender dependencias largas.

---

## 🧠 Transformers: ¿Por qué pueden manejar secuencias más largas?

### 1. **Procesamiento paralelo**

* Los modelos Transformer procesan **toda la secuencia a la vez**, no paso a paso.
* Cada token **atiende a todos los demás** en una sola operación de atención.
* Esto permite una **aceleración enorme** en comparación con RNN/LSTM.

### 2. **Atención total**

* Cada palabra puede “mirar” directamente a cualquier otra, sin depender de una cadena de pasos intermedios.
* Esto permite **capturar dependencias largas con facilidad**.

### 3. **Limitaciones distintas (pero más controlables)**

* El límite práctico en los modelos Transformer no es por arquitectura secuencial, sino por:

  * **Memoria y coste computacional**: la atención tiene complejidad cuadrática `O(n²)` respecto a la longitud de la secuencia.
  * Por eso surgen variantes como **Longformer**, **Performer**, **FlashAttention**, etc.

---

## 📌 Resumen comparativo

| Modelo      | Procesamiento | Límite clave          | Dependencias largas | Paralelizable |
| ----------- | ------------- | --------------------- | ------------------- | ------------- |
| LSTM / GRU  | Secuencial    | Tiempo + gradientes   | Difícil             | ❌ No          |
| Transformer | Paralelo      | Memoria / complejidad | ✅ Fácil             | ✅ Sí          |


![LSTM/GRU son secuenciales, Transformers son paralelos](./Transformers_vs_LSTM-GRU.png)
---

## 🔍 Conclusión
* **LSTM/GRU** son buenos para secuencias cortas y tareas donde el contexto reciente es clave.
* Los **modelos Transformer** son ideales para tareas que requieren atención a largo plazo y procesamiento rápido.
* La elección entre ambos depende del tipo de tarea y la longitud de las secuencias que se manejan.
* En general, para tareas de NLP modernas, los **modelos Transformer** son la opción preferida.
* Sin embargo, LSTM y GRU siguen siendo útiles en contextos específicos, como en tareas de tiempo real o donde la memoria es limitada.
