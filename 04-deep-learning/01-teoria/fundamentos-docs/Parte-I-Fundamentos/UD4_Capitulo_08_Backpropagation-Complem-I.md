---
output:
  word_document:
    toc: true
    toc_depth: '2'
  html_document: default
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true
    fig_caption: true
    latex_engine: xelatex
---
# 🧭 DÓNDE ESTAMOS AHORA

* ✔ Ya saben qué es una **función de pérdida**
* ✔ Ya han visto **gradiente descendente**
* 👉 Ahora toca **cómo se calcula el gradiente realmente**
  → **Backpropagation**

> Nota: este complemento usa imágenes externas como apoyo visual. Si alguna no
> carga al exportar PDF, usa las figuras locales del capítulo principal.

---

# 🧠 1️⃣ BACKPROPAGATION — IDEA VISUAL GLOBAL

### Mensaje clave (antes de cualquier fórmula)

> **Backpropagation no es un algoritmo distinto.**
> Es simplemente **aplicar la regla de la cadena** muchas veces.

---

## Imagen 1 — Red neuronal como grafo

![Image](https://miro.medium.com/v2/resize%3Afit%3A1138/0%2ADxiGsw0MskmqsL2a)

![Image](https://images.openai.com/static-rsc-3/DKCqDjvcScbdEStZUaT-VeTVxHfmHH3w6TLsdKY6d3tvlEBN6K8Z-7hOSZSEyYYPZm6NiuUzT6WI5X0baZmvYWT7MxhWetNjSblYlcWmGYk?purpose=fullsize\&v=1)

![Image](https://serokell.io/files/a0/a05ov1m.Backpropagation_in_NN_pic1.jpg)

### Qué decir aquí

* La red es un **grafo de operaciones**
* Cada nodo:

  * recibe valores
  * produce un valor
* Primero vamos **hacia delante (forward)**
* Luego volvemos **hacia atrás (backward)**

Nada más. Sin fórmulas todavía.

---

# 🔗 2️⃣ GRAFO COMPUTACIONAL Y REGLA DE LA CADENA

Ahora sí: **visual + matemáticas suaves**.

---

## Imagen 2 — Regla de la cadena visual

![Image](https://colah.github.io/posts/2015-08-Backprop/img/tree-backprop.png)

![Image](https://i.sstatic.net/zP6uK.png)

![Image](https://substackcdn.com/image/fetch/%24s_%21tVnr%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6d6d5c9-dcac-4409-8312-d506a8556477_1176x840.png)

### Idea clave (frase que funciona)

> “Si A afecta a B, y B afecta a C,
> entonces A afecta a C.”

Matemáticamente:
$$
\frac{\partial L}{\partial w}
=
\frac{\partial L}{\partial y}
\cdot
\frac{\partial y}{\partial w}
$$

Pero **no la memorices**.
👉 **La ves en el grafo**.

---

## Imagen 3 — Forward vs Backward

![Image](https://images.openai.com/static-rsc-3/DKCqDjvcScbdEStZUaT-VeTVxHfmHH3w6TLsdKY6d3tvlEBN6K8Z-7hOSZSEyYYPZm6NiuUzT6WI5X0baZmvYWT7MxhWetNjSblYlcWmGYk?purpose=fullsize\&v=1)

![Image](https://www.researchgate.net/publication/327068529/figure/fig2/AS%3A660454913359874%401534476130993/Forward-and-backward-passes-during-inference-and-backpropagation.png)

### Qué remarcar

* **Forward**:

  * se calculan salidas
  * se calcula la pérdida
* **Backward**:

  * se calculan derivadas
  * se propagan errores
  * se actualizan pesos

Aquí conectas directamente con:

```python
loss.backward()
```

---

# 🧮 3️⃣ BACKPROP EN UNA CAPA (SIN ASUSTAR)

Antes de redes profundas, **una capa**.

---

## Imagen 4 — Neurona individual

![Image](https://www.researchgate.net/publication/338569900/figure/fig3/AS%3A847101370044416%401578976113970/The-back-propagation-process-through-a-single-neuron-The-local-derivatives-can-be.png)

![Image](https://images.openai.com/static-rsc-3/83n8GYLckl4nm5p_-ghvOrutTpZUH7Mhiav-0jmoVcvZpLP1PpirFUtu0QXcMq-9uhnIapLZ3MXpA06w8hdz1j5diEW91-MILYji6O88G0M?purpose=fullsize\&v=1)

### Explicación paso a paso

1. Entrada (x)
2. Peso (w)
3. Suma ponderada: $z = w \cdot x + b$
4. Activación: $y = f(z)$
5. Pérdida: $L(y, y_{real})$

Backprop:

* ¿Cómo cambia $L$ si cambio $w$?
* Cadena:
  $$
  \frac{\partial L}{\partial w}
  =
  \frac{\partial L}{\partial y}
  \cdot
  \frac{\partial y}{\partial z}
  \cdot
  \frac{\partial z}{\partial w}
  $$

Esto **ya lo han visto** sin saberlo.

---

# 🧑‍💻 4️⃣ CONEXIÓN DIRECTA CON CÓDIGO

Aquí es donde **PyTorch y JAX brillan**.

---

## PyTorch (lo que YA han visto)

```python
loss = criterion(outputs, targets)
loss.backward()      # ← aquí ocurre TODO
optimizer.step()
```

Explicación honesta:

* PyTorch construye el **grafo automáticamente**
* Calcula derivadas **con backprop**
* Tú solo indicas:

  * qué es el forward
  * cuál es la pérdida

---

## JAX (para los valientes)

```python
grads = jax.grad(loss_fn)(params, x, y)
```

Mensaje clave:

> JAX no “hace backprop”:
> **deriva funciones matemáticas puras**

---

# 🧠 FRASES CLAVE QUE CLAVAN EL CONCEPTO

Guárdalas, funcionan muy bien en clase:

* “Backpropagation no aprende: **calcula gradientes**”
* “El aprendizaje ocurre al **actualizar los pesos**”
* “El gradiente es información, no una decisión”
* “El optimizador decide cómo usar el gradiente”

---

# 🧭 DÓNDE NOS QUEDAMOS AHORA (muy importante)

✔ Superficie de pérdida
✔ Gradiente descendente
✔ Learning rate
✔ Divergencia
✔ **Backpropagation visual**

👉 **Siguiente paso natural** (cuando tú quieras):

1. Backprop **en una red de 2 capas**, paso a paso
2. Activaciones y su derivada (ReLU, sigmoid, softmax)
3. Por qué aparecen problemas como:

   * vanishing gradients
   * exploding gradients

Dime:

* ¿seguimos con **activaciones y pérdidas**?
* ¿o hacemos un **notebook visual de backprop paso a paso**?
