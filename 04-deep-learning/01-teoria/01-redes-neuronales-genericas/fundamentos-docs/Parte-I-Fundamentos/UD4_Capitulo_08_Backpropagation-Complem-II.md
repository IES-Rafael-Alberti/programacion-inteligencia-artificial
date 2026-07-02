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
# Capítulo 8bis — Backpropagation: cómo aprende realmente una red neuronal

> Nota: este complemento usa ejemplos y fórmulas para reforzar la intuición.
> Si necesitas soporte visual estable para PDF, prioriza las figuras locales
> del capítulo principal.

## 8.1 El problema que queremos resolver

Una red neuronal produce una salida.
La comparamos con el valor real y obtenemos un **error** (función de pérdida).

👉 El problema no es calcular el error.
👉 El problema es **saber qué cambiar para reducirlo**.

---

### 📌 Metáfora de la receta

Imagina que estás haciendo un pastel:

* Sigues una receta
* Usas ciertos ingredientes en ciertas cantidades
* El resultado final **no sabe bien**

La pregunta clave no es *“¿el pastel está malo?”*
La pregunta clave es:

> **¿Qué ingrediente ha contribuido más a que el sabor sea malo?**

Eso es exactamente lo que hace **backpropagation**.

---

## 8.2 Forward pass: cocinar la receta

### En redes neuronales

Durante el **forward pass**:

1. Los datos de entrada pasan por la red
2. Se aplican operaciones matemáticas (capas)
3. Se obtiene una predicción
4. Se calcula la pérdida

Formalmente:
$$
\hat{y} = f(x; w)
\quad\Rightarrow\quad
L = \text{loss}(y, \hat{y})
$$

---

### En la receta

* Mezclas ingredientes
* Horneas
* Pruebas el pastel
* Evalúas el sabor

➡️ El **forward pass** es simplemente *hacer la receta*.

---

## 8.3 Backward pass: averiguar qué ingrediente ajustar

Aquí empieza el aprendizaje real.

---

### En la receta

El pastel no sabe bien.

Te preguntas:

* ¿Ha sido demasiada sal?
* ¿Poco azúcar?
* ¿Tiempo de horno excesivo?

No rehaces todo desde cero:
👉 **analizas hacia atrás** desde el sabor final.

---

### En redes neuronales

Hacemos exactamente lo mismo:

* Partimos de la pérdida final
* Vamos hacia atrás por la red
* Calculamos **cuánto ha contribuido cada peso al error**

Esto es backpropagation.

---

## 8.4 El grafo computacional: receta y red son lo mismo

Una red neuronal puede verse como un **grafo de operaciones**:

```
Entrada → Capa 1 → Capa 2 → Salida → Pérdida
```

Cada nodo:

* recibe valores
* produce un resultado
* depende de los anteriores

---

### Metáfora directa

```
Ingredientes → Masa → Horno → Sabor
```

Cambian los nombres, **no la estructura**.

---

## 8.5 La regla de la cadena (sin fórmulas todavía)

### Idea intuitiva

Si:

* A influye en B
* B influye en C

Entonces:

* A influye en C

---

### En la receta

* La cantidad de harina afecta a la masa
* La masa afecta al resultado final
* Por tanto, la harina afecta al sabor

---

### En redes neuronales

Si:

* Un peso afecta a una neurona
* Esa neurona afecta a la salida
* La salida afecta a la pérdida

Entonces:

* Ese peso afecta a la pérdida

Eso es **la regla de la cadena**.

---

## 8.6 La regla de la cadena (formulación matemática)

Para quien quiera el detalle formal:

$$
\frac{\partial L}{\partial w}
=
\frac{\partial L}{\partial y}
\cdot
\frac{\partial y}{\partial z}
\cdot
\frac{\partial z}{\partial w}
$$

Interpretación:

* ¿Cuánto cambia la pérdida?
* Si cambia la salida
* Que cambia si cambia una neurona
* Que cambia si cambia un peso

👉 No es una fórmula a memorizar.
👉 Es una **traducción matemática de la intuición**.

---

## 8.7 Backpropagation en una neurona

Para una neurona simple:

1. $z = w \cdot x + b$
2. $y = f(z)$
3. $L = \text{loss}(y, y_{real})$

Backpropagation calcula:

* Cómo afecta $w$ a $z$
* Cómo afecta $z$ a $y$
* Cómo afecta $y$ a $L$

Y lo encadena.

---

### Metáfora

* Ingrediente → paso intermedio → sabor
* Ajustas el ingrediente **en función de su impacto real**

---

## 8.8 De la teoría al código

### En PyTorch

```python
loss = criterion(outputs, targets)
loss.backward()
optimizer.step()
```

* `loss.backward()`:

  * construye el grafo
  * aplica backpropagation
  * calcula todos los gradientes

---

### En JAX

```python
grads = jax.grad(loss_fn)(params, x, y)
```

Aquí:

* no hay clases
* no hay estado oculto
* se derivan funciones matemáticas puras

---

## 8.9 Qué NO es backpropagation

Es importante aclararlo:

* ❌ No es el algoritmo de aprendizaje
* ❌ No decide cuánto cambiar los pesos
* ❌ No optimiza por sí mismo

Backpropagation **solo calcula gradientes**.

El aprendizaje ocurre cuando:

* usamos esos gradientes
* con un optimizador
* y actualizamos los pesos

---

## 8.10 Conclusión

> Backpropagation es simplemente
> **averiguar qué ingredientes ajustar
> para que el resultado final mejore**.

La matemática:

* formaliza la intuición
* permite automatizar el proceso
* escala a miles o millones de parámetros

---
