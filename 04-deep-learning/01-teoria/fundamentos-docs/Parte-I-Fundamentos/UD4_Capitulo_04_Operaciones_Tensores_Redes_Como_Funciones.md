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

# Capítulo 4 — Operaciones con tensores y redes neuronales como funciones

## 4.1. De los datos a las operaciones

En el capítulo anterior hemos visto que:
- Los datos se representan como tensores
- Las redes neuronales reciben tensores como entrada
- Todo el cálculo se basa en operaciones matemáticas

En este capítulo respondemos a la pregunta clave:

> ¿Qué operaciones realiza realmente una red neuronal sobre los datos?

La respuesta es más simple de lo que parece:
- Operaciones lineales
- Operaciones elemento a elemento
- Composición de funciones

---

## 4.2. Una red neuronal es una función

Una red neuronal puede verse como una **función matemática compleja**, construida a partir de funciones más simples.

![Red Neuronal como Función](images/19_red_como_funcion.png)

Formalmente:
- Entrada → salida
- Datos → predicción

Conceptualmente:
> Una red neuronal es una función que transforma un tensor de entrada en un tensor de salida.

Cada capa añade una nueva transformación.

---

## 4.3. Transformaciones lineales

La primera operación que realiza una capa es una **transformación lineal**.

![Transformación Lineal](images/20_transformacion_lineal.png)

Forma general:
- Producto matricial
- Suma de un sesgo (bias)

Conceptualmente:
- Se combinan las variables de entrada
- Se cambia la orientación del espacio de datos
- Se mezclan las características

En código (idea):
```python
Y = X @ W + b
````

Interpretación geométrica:

* Rotación
* Escalado
* Proyección

Por sí sola, esta operación **no es suficiente** para modelar relaciones complejas.

---

## 4.4. Operaciones elemento a elemento

Tras la transformación lineal, se aplican **operaciones elemento a elemento**.

![Operaciones Elemento a Elemento](images/21_operaciones_elemento_elemento.png)

Estas operaciones:

* Se aplican posición a posición
* No mezclan información entre elementos
* Son muy eficientes computacionalmente

Ejemplos:

* Suma
* Multiplicación
* Funciones no lineales

Son esenciales para introducir no linealidad.

---

## 4.5. Funciones de activación

Las **funciones de activación** se aplican elemento a elemento al resultado de la transformación lineal.

Su objetivo es:

* Introducir no linealidad
* Permitir que la red aprenda relaciones complejas
* Decidir qué información se transmite a la siguiente capa

Ejemplos comunes:

* ReLU
* Sigmoid
* Tanh

Idea clave:

> Sin funciones de activación, una red neuronal profunda sería equivalente a una sola capa lineal.

---

## 4.6. Composición de funciones

Cada capa de una red neuronal realiza una operación simple.

La red completa es la **composición** de todas ellas:

![Composición de Funciones](images/22_composicion_funciones.png)

```
f(x) = fₙ(fₙ₋₁(...f₂(f₁(x))))
```

No es necesario entender la fórmula, sino la idea:

> Las redes neuronales aprenden encadenando transformaciones simples.

Cada capa refina la representación aprendida por la anterior.

---

## 4.7. Redes neuronales como deformación del espacio

Desde un punto de vista geométrico, una red neuronal:

* Recibe una nube de puntos (datos)
* Aplica una transformación lineal
* Aplica una deformación no lineal
* Repite el proceso varias veces

![Deformación del Espacio](images/23_deformacion_espacio.png)

El efecto acumulado es:

* Separar regiones
* Alinear clases
* Simplificar el problema para la capa final

Esta interpretación explica por qué:

* Más capas permiten mayor expresividad
* El orden de las capas importa

---

## 4.8. Profundidad y capacidad del modelo

Añadir capas aumenta:

* Capacidad de representación
* Complejidad del modelo

Pero también:

* Riesgo de sobreajuste
* Coste computacional
* Dificultad de entrenamiento

Por eso:

> Más profundo no siempre es mejor.

El diseño de la arquitectura es un equilibrio.

---

## 4.9. El papel del sesgo (bias) en las transformaciones

El sesgo:

* Desplaza la transformación
* Permite mayor flexibilidad
* Evita restricciones innecesarias

![Papel del Sesgo](images/24_papel_sesgo.png)

Geométricamente:

* El bias desplaza hiperplanos

---

## 4.6. Preguntas de autoevaluación

### Opción múltiple

1. **¿Qué significa que una red neuronal sea una composición de funciones?**
   - A) Que se escribe de forma bonita  
   - **B) Que la salida de una capa se convierte en entrada de la siguiente**  
   - C) Que no tiene parámetros  
   - D) Que solo funciona con música

2. **¿Cuál es el propósito de una transformación lineal en una red neuronal?**
   - A) Hacer el entrenamiento instantáneo  
   - **B) Cambiar la dimensionalidad y rotar el espacio de datos**  
   - C) Prevenir errores  
   - D) No tiene propósito real

3. **¿Qué sucede geométricamente cuando aplicamos una función de activación no lineal?**
   - A) Los datos desaparecen  
   - **B) El espacio se deforma de manera compleja, permitiendo separación no lineal**  
   - C) Todo se convierte en puntos iguales  
   - D) Los datos se vuelven unidimensionales

### Pregunta corta

4. **¿Por qué la composición de funciones lineales seguida de funciones no lineales permite a las redes neuronales aprender relaciones complejas?** (3 líneas)
* Permite separar datos que de otro modo no serían separables

Aunque es un término simple, es esencial para el funcionamiento de la red.

---

## 4.10. Qué hace realmente una capa neuronal (resumen)

Cada capa realiza:

1. Una combinación lineal de las entradas
2. La suma de un sesgo
3. Una activación no lineal

Este patrón se repite en:

* Redes densas
* CNN
* RNN
* Transformers

Cambian las operaciones concretas, pero **la idea base es la misma**.

---

## 4.11. Idea clave del capítulo

> Una red neuronal no es más que una función compleja
> construida a partir de transformaciones simples aplicadas a tensores.

Entender estas operaciones es imprescindible para comprender:

* La función de pérdida
* El entrenamiento
* El gradiente descendente
* La backpropagation

```

---

### 🔜 Siguiente capítulo

👉 **Capítulo 5 — La función de pérdida**

Porque ya sabemos:
- qué hace la red
- cómo transforma los datos

y toca responder:

> ¿Cómo sabemos si lo está haciendo bien o mal?