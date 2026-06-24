---
title: "Capítulo 7 — Gradiente descendente: aprender ajustando errores"
output:
  pdf_document: 
    latex_engine: xelatex
---
# Capítulo 7 — Gradiente descendente: aprender ajustando errores

## 7.1. Del gradiente a un algoritmo de aprendizaje

En los capítulos anteriores hemos visto que:

- La función de pérdida mide el error del modelo
- El gradiente indica cómo cambia ese error
- El gradiente apunta hacia donde la pérdida **crece más rápido**

La idea fundamental ahora es sencilla:

> Si el gradiente indica la subida,
> para aprender debemos movernos en la dirección contraria.

Ese procedimiento recibe el nombre de **gradiente descendente**.

---

## 7.2. Qué es el gradiente descendente

El **gradiente descendente** es un algoritmo de optimización que:

- Ajusta los parámetros del modelo
- Paso a paso
- Para minimizar la función de pérdida

En cada iteración:
1. Se calcula la pérdida
2. Se calcula el gradiente
3. Se actualizan los parámetros
4. Se repite el proceso

Este ciclo es el corazón del entrenamiento de una red neuronal.

![Algoritmo de Gradiente Descendente](images/35_algoritmo_gradiente_descendente.png)

---

## 7.3. Regla de actualización de los parámetros

De forma intuitiva, la actualización de un peso sigue esta idea:

> Nuevo peso = peso actual − (learning rate × gradiente)

Interpretación:
- El gradiente indica la dirección
- El learning rate controla el tamaño del paso
- El signo negativo asegura que bajamos la pérdida

No es necesario memorizar la fórmula, sino entender:
- Qué representa cada término
- Qué efecto tiene sobre el aprendizaje

---

## 7.3bis. Ejemplo numérico concreto

Para entender bien cómo funciona el gradiente descendente, veamos un ejemplo paso a paso.

### Escenario
- Una neurona simple con **un solo peso** w
- Una función de pérdida simple: MSE
- Datos de entrenamiento muy reducido (3 ejemplos)

| x | y real |
|---|--------|
| 1 | 3 |
| 2 | 5 |
| 3 | 7 |

**Modelo:** salida = w × x

**Pérdida:** L = (1/N) × Σ(y_real - y_predicho)²

### Inicialización
- w = 1.5 (valor inicial aleatorio)
- learning_rate = 0.1

### Iteración 1: Calcular la pérdida inicial

Para cada ejemplo:
- x=1: ŷ = 1.5 × 1 = 1.5 → error = 3 - 1.5 = 1.5
- x=2: ŷ = 1.5 × 2 = 3.0 → error = 5 - 3.0 = 2.0
- x=3: ŷ = 1.5 × 3 = 4.5 → error = 7 - 4.5 = 2.5

Pérdida: L = (1.5² + 2.0² + 2.5²) / 3 = 8.5 / 3 = **2.833**

### Calcular el gradiente

El gradiente de la pérdida respecto a w es:

dL/dw = (2/N) × Σ[(y_predicho - y_real) × x]

dL/dw = (2/3) × [(1.5 - 3) × 1 + (3.0 - 5) × 2 + (4.5 - 7) × 3]

dL/dw = (2/3) × [(-1.5) × 1 + (-2.0) × 2 + (-2.5) × 3]

dL/dw = (2/3) × [-1.5 - 4.0 - 7.5]

dL/dw = (2/3) × [-13.0] = **-8.667**

### Actualizar el peso

w_nuevo = w_actual - learning_rate × dL/dw

w_nuevo = 1.5 - 0.1 × (-8.667)

w_nuevo = 1.5 + 0.867 = **2.367**

---

### Iteración 2: Calcular la nueva pérdida

Con w = 2.367:

- x=1: ŷ = 2.367 × 1 = 2.367 → error = 3 - 2.367 = 0.633
- x=2: ŷ = 2.367 × 2 = 4.734 → error = 5 - 4.734 = 0.266
- x=3: ŷ = 2.367 × 3 = 7.101 → error = 7 - 7.101 = -0.101

Pérdida: L = (0.633² + 0.266² + 0.101²) / 3 = 0.472 / 3 = **0.157**

Gradiente:

dL/dw = (2/3) × [(2.367 - 3) × 1 + (4.734 - 5) × 2 + (7.101 - 7) × 3]

dL/dw = (2/3) × [(-0.633) + (-0.532) + (0.303)] = (2/3) × [-0.862] = **-0.575**

Nuevo peso:

w_nuevo = 2.367 - 0.1 × (-0.575) = 2.367 + 0.058 = **2.425**

---

### Observaciones

| Iteración | Peso w | Pérdida L | Gradiente |
|-----------|--------|-----------|-----------|
| 0 | 1.500 | 2.833 | -8.667 |
| 1 | 2.367 | 0.157 | -0.575 |
| 2 | 2.425 | 0.029 | -0.086 |

**Qué vemos:**
- La pérdida **disminuye** en cada iteración (buen signo)
- El gradiente cada vez es **más pequeño** (acercándonos al mínimo)
- El peso se acerca al valor óptimo (que sería ~2.0 en este caso simple)
- El proceso es iterativo y convergente

**Idea clave:**

> El gradiente negativo nos dice: "el peso debe aumentar"
> El gradiente positivo nos dice: "el peso debe disminuir"
> La magnitud nos dice: "qué tan fuerte ajustar"

---

## 7.4. Interpretación geométrica

Imaginemos de nuevo la superficie de pérdida:

- Estamos en un punto del paisaje
- Calculamos la pendiente
- Damos un pequeño paso cuesta abajo
- Volvemos a calcular la pendiente
- Repetimos

Con cada paso:
- El error disminuye
- El modelo mejora

Este proceso se repite miles o millones de veces.

![Visualización del Descenso](images/36_visualizacion_descenso.png)

---

## 7.5. Learning rate: un parámetro crítico

El **learning rate** controla cuánto avanzamos en cada paso.

### Learning rate demasiado grande
- Saltos bruscos
- El modelo puede no converger
- Puede “pasarse” del mínimo

### Learning rate demasiado pequeño
- Aprendizaje muy lento
- Mucho tiempo de entrenamiento
- Riesgo de quedarse atrapado

Elegir un buen learning rate es clave para entrenar bien.

![Efecto del Learning Rate](images/38_learning_rate_efecto.png)

---

## 7.6. Tipos de gradiente descendente

En función de cuántos datos usamos para calcular el gradiente, distinguimos:

### 7.6.1. Batch Gradient Descent

- Usa todo el dataset en cada paso
- Gradiente preciso
- Costoso computacionalmente

Adecuado para:
- Datasets pequeños
- Funciones simples

---

### 7.6.2. Stochastic Gradient Descent (SGD)

- Usa un solo ejemplo por paso
- Muy rápido
- Más ruido en la actualización

Ventaja:
- Puede escapar de mínimos locales

Inconveniente:
- Trayectoria inestable

---

### 7.6.3. Mini-batch Gradient Descent

- Usa pequeños lotes de datos
- Compromiso entre estabilidad y eficiencia
- Es el método más utilizado en la práctica

Aquí aparece un concepto clave:
- **batch size**

![Tipos de Gradiente Descendente](images/37_tipos_gradiente_descendente.png)

---

## 7.7. Data batches y entrenamiento moderno

En redes neuronales modernas:
- Los datos se procesan en batches
- Cada batch produce una actualización

Ventajas:
- Aprovecha paralelismo (CPU / GPU)
- Reduce ruido extremo
- Mejora la estabilidad del entrenamiento

El uso de batches es esencial en deep learning.

---

## 7.8. Mínimos locales y paisaje de pérdida

La función de pérdida de una red neuronal:
- No suele ser convexa
- Tiene múltiples valles y colinas

Consecuencias:
- Puede haber mínimos locales
- No siempre se alcanza el mínimo global

El gradiente descendente:
- No garantiza el mejor mínimo
- Pero suele encontrar soluciones suficientemente buenas

En la práctica:
> Un mínimo “bueno” suele ser suficiente.

![Mínimos Locales vs Globales](images/39_minimos_locales_globales.png)

---

## 7.9. Optimización en librerías modernas

Hoy en día:
- No implementamos gradiente descendente a mano
- Usamos optimizadores avanzados

Ejemplos:
- SGD con momentum
- RMSprop
- Adam

Todos ellos:
- Se basan en gradiente descendente
- Introducen mejoras de estabilidad y velocidad

La base conceptual sigue siendo la misma.

---

## 7.10. Idea clave del capítulo

> El gradiente descendente transforma el aprendizaje
> en un proceso iterativo de mejora guiada.

Gracias a él, las redes neuronales:
- Ajustan millones de parámetros
- Aprenden a partir de datos
- Convergen hacia soluciones útiles

---

## 7.11. Preparación para el siguiente capítulo

Hasta ahora hemos visto:
- Pérdida
- Derivadas
- Gradiente
- Gradiente descendente

Falta una pieza esencial:

> ¿Cómo se calcula el gradiente en redes con muchas capas?

Eso nos lleva al siguiente capítulo:

👉 **Capítulo 8 — Backpropagation**

---

## 7.12. Desde la teoría a la práctica

El gradiente descendente está en el corazón de todos los frameworks modernos. Verás cómo TensorFlow/PyTorch/Keras lo implementan automáticamente.

👉 **Optimizadores en práctica** en [PyTorch Fashion MNIST Binaria](../../Parte-2-Pract/UD4_04_Red_Neuronal_PyTorch_Binaria_FashionMNIST.ipynb) — experimenta con diferentes learning rates y observa cómo afecta la convergencia.

---

## 7.13. Preguntas de autoevaluación

### Opción múltiple

1. **¿Cuál es el parámetro más importante para controlar la velocidad de aprendizaje en el gradiente descendente?**
   - A) El número de capas  
   - **B) El learning rate (tasa de aprendizaje)**  
   - C) El tipo de datos  
   - D) El color de los gráficos

2. **¿Cuál es la principal diferencia entre Batch GD, Mini-batch GD y SGD?**
   - A) El color de los gráficos  
   - **B) El número de ejemplos usados en cada actualización de parámetros**  
   - C) La velocidad absoluta  
   - D) El idioma del código

3. **¿Qué problema puede ocurrir si el learning rate es demasiado grande?**
   - A) El modelo será más preciso  
   - **B) El error puede divergir (crecer) en lugar de converger**  
   - C) Todo funciona mejor  
   - D) No hay problema

### Pregunta corta

4. **¿Cómo diferenciarías entre un mínimo local y uno global al entrenar una red neuronal? ¿Es crítico alcanzar el mínimo global?** (3-4 líneas)
