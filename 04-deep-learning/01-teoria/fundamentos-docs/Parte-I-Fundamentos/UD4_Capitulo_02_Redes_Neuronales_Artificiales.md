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

# Capítulo 2 — Qué es una Red Neuronal Artificial

## 2.1. De los modelos clásicos a las redes neuronales

En Machine Learning clásico, muchos modelos pueden verse como funciones relativamente simples:

- Una regresión lineal combina variables con pesos
- Un árbol de decisión divide el espacio en regiones
- Un SVM busca un hiperplano separador

Las **redes neuronales artificiales** generalizan esta idea:

> En lugar de definir explícitamente la forma de la función,
> dejamos que el modelo **aprenda la función** a partir de datos.

---

## 2.2. La neurona artificial

La **neurona artificial** es la unidad básica de una red neuronal.

Conceptualmente:
- Recibe varias entradas
- Cada entrada tiene un peso asociado
- Se calcula una combinación ponderada
- Se aplica una función de activación

![Estructura de una Neurona Artificial](images/06_neurona_artificial_estructura.png)

De forma simplificada:

```

entrada → pesos → suma → activación → salida

```

Matemáticamente (a alto nivel):

- Entradas: vector **x**
- Pesos: vector **w**
- Sesgo (bias): **b**

La neurona calcula:

```

salida = activación(w · x + b)

```

No es necesario memorizar la fórmula:
lo importante es entender **qué representa cada parte**.

---

## 2.3. Pesos y sesgo (bias)

### Pesos
- Indican la **importancia relativa** de cada entrada
- Se ajustan durante el entrenamiento
- Determinan cómo se combinan las variables

### Sesgo (bias)
- Permite desplazar la función
- Evita que la neurona esté “atada” al origen
- Es equivalente a una variable constante adicional

Intuición geométrica:
- Los pesos orientan el hiperplano
- El sesgo lo desplaza
![Pesos y Sesgo: Intuición Geométrica](images/12_pesos_sesgo_geometria.png)
---

## 2.4. Funciones de activación

Si una red solo aplicara combinaciones lineales, **no sería más potente que una regresión lineal**.

Las funciones de activación introducen **no linealidad**, que es clave para:

- Modelar relaciones complejas
- Separar datos no linealmente separables
- Aumentar la capacidad expresiva del modelo

![Funciones de Activación Comunes](images/07_funciones_activacion.png)

Funciones comunes:

- Sigmoid
- Tanh
- ReLU
- Variantes de ReLU

No es necesario memorizar fórmulas, sino entender que:

> La activación decide **qué información pasa** a la siguiente capa.

---

## 2.5. Capas en una red neuronal

Una red neuronal está organizada en **capas**:

![Capas de una Red Neuronal](images/08_capas_red_neuronal.png)

### Capa de entrada
- Recibe los datos originales
- No realiza cálculos complejos
- Su tamaño depende del número de variables

### Capas ocultas
- Transforman los datos internamente
- Aprenden representaciones intermedias
- Puede haber una o varias

### Capa de salida
- Produce la predicción final
- Su forma depende del problema:
  - Regresión
  - Clasificación binaria
  - Clasificación multiclase

---

## 2.6. Redes feedforward (perceptrón multicapa)

Las redes que vamos a estudiar primero son **redes feedforward**:

- La información fluye solo hacia delante
- No hay ciclos
- Cada capa recibe la salida de la anterior

![Redes Feedforward vs Con ciclos](images/09_feedforward_vs_ciclos.png)

Este tipo de red se conoce como:
- Perceptrón multicapa (MLP)

Son la base de:
- Redes profundas
- CNN
- RNN
- Transformers

---

## 2.7. Interpretación geométrica de una capa

Cada capa neuronal realiza una operación que puede interpretarse como:

- Una transformación del espacio de datos
- Rotaciones, escalados y combinaciones
- Seguidas de una deformación no lineal
![Transformación Geométrica de una Capa](images/10_transformacion_geometrica.png)
Intuición importante:

> Una red neuronal no “memoriza datos”,
> **deforma el espacio** para separar mejor los ejemplos.

Esto conecta directamente con:
- Visualizaciones de tensores
- Producto matricial
- Activaciones

---

## 2.8. Por qué varias capas son más potentes

Una sola capa:
- Puede aprender fronteras simples

Varias capas:
- Aprenden representaciones jerárquicas
- Combinan patrones simples en otros más complejos

![Jerarquía de Capas: Patrones a Abstracciones](images/11_jerarquia_capas.png)

Ejemplo conceptual:
- Primera capa: patrones básicos
- Segunda capa: combinaciones
- Tercera capa: estructuras más abstractas

Este principio es común a:
- Visión
- Lenguaje
- Series temporales

---

## 2.9. Qué NO es todavía Deep Learning

Hasta aquí:
- Hemos hablado de redes neuronales clásicas
- Arquitecturas relativamente simples
- Pocas capas

Todavía **no** hemos entrado en:
- Redes convolucionales
- Redes recurrentes
- Atención
- Transformers

Sin embargo, **las bases matemáticas y conceptuales son las mismas**.

---

## 2.10. Idea clave del capítulo

> Una red neuronal artificial es una función compuesta
> que aprende a transformar datos mediante capas sucesivas.

Entender:
- neurona
- pesos
- activación
- capas

es imprescindible antes de pasar a:
- entrenamiento
- gradiente descendente
- backpropagation


---

## 2.9. Desde la teoría a la práctica

Ahora que entiendes la estructura de una red neuronal (neuronas, pesos, capas), es el momento de ver cómo se definen estas redes en código.

👉 **Implementación: Redes multicapa** en [Keras Fashion MNIST Multiclase](../../Parte-2-Pract/UD4_03_Red_Neuronal_Keras_Multiclase_FashionMNIST.ipynb) — verás cómo se crean capas ocultas y cómo impactan en el rendimiento.

---

## 2.10. Preguntas de autoevaluación

### Opción múltiple

1. **¿Qué papel juega el sesgo (bias) en una neurona artificial?**
   - A) Prevenir el sobreajuste  
   - **B) Permitir el desplazamiento de la función de activación**  
   - C) Acelerar el cálculo  
   - D) Reducir el número de parámetros

2. **¿Por qué es necesaria una función de activación no lineal?**
   - A) Para que el código sea más rápido  
   - **B) Para que la red pueda aprender relaciones no lineales en los datos**  
   - C) Para ahorrar memoria  
   - D) No es realmente necesaria

3. **¿Cuál es la función de una capa oculta en una red neuronal?**
   - A) Mostrar al usuario las predicciones  
   - **B) Aprender representaciones internas complejas del problema**  
   - C) Validar los datos de entrada  
   - D) Almacenar información en el disco duro

### Pregunta corta

4. **Explica con tus palabras: ¿por qué una red neuronal con una sola capa (sin capas ocultas) no puede resolver un problema XOR?** (3-4 líneas)

---

### 🔜 Siguiente paso


👉 **Capítulo 3 — Representación matemática de los datos (escalares, vectores, matrices y tensores)**: texto + gráficos + código.
