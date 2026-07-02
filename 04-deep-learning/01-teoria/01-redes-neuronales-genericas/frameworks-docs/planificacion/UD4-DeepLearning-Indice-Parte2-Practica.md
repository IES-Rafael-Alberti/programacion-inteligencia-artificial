## 📦 Bloque UD4 — Primera red neuronal: Keras, PyTorch y JAX

### Objetivo del bloque

Que el alumnado:

* Vea **la misma red neuronal** implementada en:

  * Keras
  * PyTorch
  * (Apéndice) JAX
* Entienda **qué cambia y qué no cambia**
* Comprenda que:

  * la teoría es la misma
  * el framework solo cambia la forma de expresarla

---

## 🧠 Modelo común (para los tres)

Usaremos **el mismo problema** en los tres casos:

* Dataset sencillo (clasificación binaria o multiclase)

  * por ejemplo: `sklearn.datasets.make_classification`
* Arquitectura:

  * Entrada
  * 1–2 capas ocultas densas
  * Activación ReLU
  * Capa de salida con activación adecuada
* Pérdida estándar
* Optimizador Adam

Nada de complicaciones: **el foco es entender**, no optimizar.

---

## 🧩 Capítulo 9 — Primera red neuronal en Keras

### Por qué empezamos por Keras

Keras es ideal porque:

* Es **declarativo**
* El código se parece mucho a la teoría
* Permite centrarse en:

  * arquitectura
  * activaciones
  * pérdida
  * optimizador

Aquí el alumno **ve la red como un todo**.

### Entregable

* 📓 `UD4_01_Primera_Red_Keras.ipynb`

Contenido:

1. Breve introducción teórica (markdown)
2. Carga / generación del dataset
3. Definición del modelo (`Sequential`)
4. Compilación:

   * pérdida
   * optimizador
   * métricas
5. Entrenamiento
6. Evaluación
7. Visualización de:

   * pérdida
   * accuracy

> Aquí **NO** entramos aún en backprop explícito: Keras lo oculta a propósito.

---

## 🔁 Capítulo 10 — La misma red en PyTorch

### Por qué PyTorch después

PyTorch:

* Es más explícito
* Obliga a entender:

  * forward
  * backward
  * entrenamiento
* Es el puente entre:

  * “magia de Keras”
  * “entender lo que pasa”

Aquí el alumno **entiende de verdad** gradiente y backprop.

### Entregable

* 📓 `UD4_02_Primera_Red_PyTorch.ipynb`

Contenido:

1. Misma introducción y dataset
2. Definición de la red como clase
3. Forward explícito
4. Definición de:

   * pérdida
   * optimizador
5. Bucle de entrenamiento manual
6. Evaluación

Aquí se ve claramente:

* forward pass
* backward pass
* `loss.backward()`
* `optimizer.step()`

---

## 🧪 Apéndice A — La misma red en JAX

### Por qué JAX como apéndice

Tu razonamiento es correcto, y conviene **dejarlo claro al alumnado**:

**JAX se usa cuando:**

* Investigación avanzada
* Modelos muy grandes
* Múltiples GPUs / TPUs
* Alto rendimiento y compilación (`jit`, `vmap`, `pmap`)

Pero:

* No es ideal para empezar
* Tiene curva de aprendizaje mayor

Aquí el objetivo es:

> “Que sepan que existe, qué aporta y cómo se ve”.

### Entregable

* 📓 `UD4_Apendice_JAX_Primera_Red.ipynb`

Contenido:

1. Misma red conceptual
2. Tensores inmutables
3. Función de pérdida
4. Gradientes con `jax.grad`
5. Entrenamiento funcional

Sin entrar en:

* paralelismo complejo
* TPUs
* código demasiado abstracto

---

## ⚖️ Capítulo 11 — Comparativa práctica: Keras vs PyTorch vs JAX

Documento corto (Markdown):

* 📄 `UD4_Comparativa_Frameworks.md`

Incluye una tabla clara como esta:

| Aspecto            | Keras | PyTorch | JAX   |
| ------------------ | ----- | ------- | ----- |
| Facilidad inicial  | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐    | ⭐⭐    |
| Control bajo nivel | ⭐⭐    | ⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐ |
| Investigación      | ⭐⭐⭐   | ⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐ |
| Producción         | ⭐⭐⭐⭐  | ⭐⭐⭐⭐    | ⭐⭐⭐   |
| Curva aprendizaje  | Baja  | Media   | Alta  |

Y texto explicativo usando **exactamente el argumento que has dado** (que es muy bueno).

---

## 🔥 Capítulo 12 — Funciones de activación y pérdida en la práctica

Aquí ya **no es teoría**, sino experimentación.

### Activaciones

* Sigmoid
* Tanh
* ReLU
* Leaky ReLU
* Softmax

Qué veremos:

* cómo cambian las curvas
* cuándo se saturan
* impacto en el entrenamiento

### Pérdidas

* MSE
* Binary Crossentropy
* Categorical Crossentropy

Se probarán:

* combinaciones correctas
* combinaciones incorrectas
* efectos prácticos

### Entregable

* 📓 `UD4_03_Activaciones_y_Perdidas.ipynb`

---

## 📌 Estado actual del módulo (honesto)

Con esto:

* 🔧 Recuperas el **núcleo técnico** que faltaba
* 🧠 El alumnado entiende **qué está pasando**
* 📈 Se prepara de verdad para:

  * CNN
  * RNN
  * Transformers
  * Gradio
  * proyectos finales

Nada de “castaña”: esto **sí es Programación de IA**.

---

### Siguiente paso inmediato (te propongo)

👉 Empiezo ya con **`UD4_01_Primera_Red_Keras.ipynb`**, con explicaciones markdown cuidadas y código limpio.

Dime:

* ¿clasificación binaria o multiclase?
* ¿dataset sintético o uno real pequeño?
