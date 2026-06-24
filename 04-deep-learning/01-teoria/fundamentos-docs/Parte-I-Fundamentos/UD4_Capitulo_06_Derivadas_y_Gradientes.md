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

# Capítulo 6 — Derivadas y gradientes: la intuición detrás del aprendizaje

## 6.1. Por qué aparecen las derivadas en redes neuronales

En el capítulo anterior hemos visto que entrenar una red neuronal consiste en:

> Ajustar los parámetros del modelo para **minimizar la función de pérdida**.

La pregunta inmediata es:

> ¿Cómo sabemos en qué dirección hay que cambiar los parámetros para reducir la pérdida?

Aquí es donde entran las **derivadas** y los **gradientes**.

---

## 6.2. Derivada: la idea de pendiente

Una **derivada** responde a una pregunta muy concreta:

> Si cambio un poco una variable, ¿cómo cambia el resultado?

Geométricamente:
- La derivada es la **pendiente** de una curva en un punto
- Indica si la función:
  - Sube
  - Baja
  - Se mantiene constante

Ejemplo intuitivo:
- Una carretera cuesta arriba → derivada positiva
- Una carretera cuesta abajo → derivada negativa
- Una zona llana → derivada cercana a cero

En redes neuronales:
- La variable suele ser un **peso**
- El resultado es la **pérdida**

![Derivada: La Idea de Pendiente](images/30_derivada_pendiente.png)

---

## 6.3. Derivada aplicada a la función de pérdida

Recordemos:
- La pérdida depende de los parámetros del modelo
- Cada peso influye en el error final

La derivada nos dice:
- Cuánto cambia la pérdida
- Cuando modificamos **un peso concreto**

Interpretación práctica:
- Si la derivada es grande → ese peso influye mucho
- Si es pequeña → influye poco

![Derivada aplicada a la Función de Pérdida](images/31_derivada_perdida.png)

---

## 6.4. De una dimensión a muchas: el gradiente

En redes neuronales no tenemos:
- Un solo peso
- Una sola derivada

Tenemos:
- Miles o millones de parámetros

El **gradiente** es la generalización de la derivada a muchas dimensiones.

Formalmente:
- Es un vector
- Cada componente es la derivada respecto a un parámetro

Intuición clave:
> El gradiente indica la dirección en la que la pérdida crece más rápido.

![Gradiente en Muchas Dimensiones](images/32_gradiente_multidimensional.png)

---

## 6.5. Interpretación geométrica del gradiente

Volviendo a la idea de la superficie de pérdida:

- La superficie es un paisaje
- El gradiente es una flecha
- Esa flecha apunta hacia la subida más pronunciada

Si queremos **bajar**, hacemos lo contrario:

> Avanzamos en la dirección opuesta al gradiente.

Esta idea es el núcleo del entrenamiento.

![Interpretación Geométrica del Gradiente](images/33_interpretacion_geometrica_gradiente.png)

---

## 6.6. Por qué el gradiente es tan importante

Gracias al gradiente:
- No probamos parámetros al azar
- No necesitamos evaluar todas las combinaciones posibles
- El aprendizaje es eficiente y dirigido

Sin gradientes:
- El entrenamiento sería impracticable
- Especialmente en modelos grandes

Por eso:
> El cálculo del gradiente es la pieza central del aprendizaje en redes neuronales.

---

## 6.7. Gradiente y velocidad de aprendizaje

El gradiente indica la **dirección**, pero no la **distancia** que damos en cada paso.

Eso se controla con un parámetro clave:
- **Learning rate**

Intuición:
- Learning rate grande → pasos largos (riesgo de pasarse)
- Learning rate pequeño → pasos cortos (aprendizaje lento)

El equilibrio es fundamental.

![Gradiente + Learning Rate = Actualización](images/34_gradiente_learning_rate.png)

---

## 6.8. Qué NO es necesario saber ahora

En este punto **no es necesario**:
- Calcular derivadas a mano
- Conocer fórmulas complejas
- Dominar cálculo diferencial formal

Las librerías modernas:
- Calculan derivadas automáticamente
- Gestionan gradientes de forma eficiente

Lo importante es entender:
- Qué representan
- Para qué se usan
- Cómo influyen en el entrenamiento

---

## 6.9. Idea clave del capítulo

> Las derivadas y los gradientes permiten convertir
> el aprendizaje en un problema de **búsqueda dirigida**.

Gracias a ellos, las redes neuronales pueden:
- Ajustar millones de parámetros
- Aprender a partir de datos
- Mejorar iterativamente su rendimiento

---

## 6.10. Preparación para el siguiente capítulo

Ahora ya sabemos:
- Qué es la pérdida
- Qué es una derivada
- Qué es un gradiente

En el siguiente capítulo veremos:
> Cómo usar esta información para entrenar realmente una red neuronal.

Eso nos lleva al **gradiente descendente**.

🔜 Siguiente capítulo

👉 Capítulo 7 — Gradiente descendente

Ahí cerramos el círculo:
pérdida → gradiente → actualización de pesos → aprendizaje.

---

## 6.11. Preguntas de autoevaluación

### Opción múltiple

1. **¿Qué nos dice la derivada de una función en un punto?**
   - A) Si la función es positiva o negativa  
   - **B) La pendiente o tasa de cambio de la función en ese punto**  
   - C) El máximo valor de la función  
   - D) Cuántos datos hay

2. **¿Qué es un gradiente en el contexto de las redes neuronales?**
   - A) Un color bonito  
   - **B) Un vector de derivadas parciales que indica el cambio de pérdida respecto a cada parámetro**  
   - C) Una operación matemática rara  
   - D) Una función de activación

3. **¿En qué dirección debemos cambiar los parámetros para reducir la pérdida?**
   - A) En la dirección del gradiente  
   - **B) En la dirección opuesta al gradiente**  
   - C) De manera aleatoria  
   - D) No importa la dirección

### Pregunta corta

4. **¿Por qué el gradiente siempre apunta en la dirección donde la función AUMENTA más rápido?** (2-3 líneas)
