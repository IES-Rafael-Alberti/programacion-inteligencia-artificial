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

# Capítulo 8 — Backpropagation: cómo aprenden realmente las redes neuronales

## 8.1. El problema a resolver

En los capítulos anteriores hemos visto que:

- La función de pérdida mide el error
- El gradiente indica cómo cambia la pérdida
- El gradiente descendente usa ese gradiente para ajustar los pesos

Pero queda una pregunta clave:

> ¿Cómo se calcula el gradiente cuando la red tiene muchas capas?

Aquí es donde aparece **backpropagation**.

---

## 8.2. Qué es backpropagation (idea general)

**Backpropagation** es el algoritmo que permite:

- Calcular el gradiente de la pérdida
- Respecto a **cada peso de la red**
- De forma eficiente

Idea clave:

> Backpropagation aplica la **regla de la cadena**
> para propagar el error desde la salida hacia atrás.

No es un algoritmo de entrenamiento en sí:
- Es un método para **calcular gradientes**
- El entrenamiento lo realiza el gradiente descendente

![Backpropagation: visión general](images/40_backprop_overview.png)

---

## 8.3. La red como una cadena de operaciones

Una red neuronal puede verse como:

- Una secuencia de operaciones matemáticas
- Cada capa transforma la salida de la anterior

Ejemplo simplificado:


Entrada → Capa 1 → Capa 2 → Capa 3 → Salida

Cada paso:
- Aplica una operación
- Produce un resultado intermedio

La pérdida depende del resultado final,
pero **cada capa ha contribuido al error**.

---

## 8.4. Regla de la cadena (intuición)

La **regla de la cadena** responde a esta pregunta:

> Si A afecta a B y B afecta a C,
> ¿cómo afecta A a C?

En redes neuronales:
- Un peso afecta a una activación
- Esa activación afecta a la siguiente capa
- Finalmente afecta a la pérdida

Backpropagation usa esta regla para:
- Repartir la “culpa” del error
- Entre todos los pesos

![Regla de la cadena](images/41_chain_rule.png)

---

## 8.5. Propagación hacia delante vs hacia atrás

### Forward pass (propagación hacia delante)
- Los datos entran en la red
- Se calculan las activaciones
- Se obtiene una predicción
- Se calcula la pérdida

### Backward pass (propagación hacia atrás)
- Se parte de la pérdida
- Se calcula el gradiente de la última capa
- Se propaga hacia capas anteriores
- Se obtienen gradientes para todos los pesos

Ambos pasos son inseparables.

![Forward pass vs Backward pass](images/42_forward_backward.png)

---

## 8.6. Intuición geométrica del proceso

Imagina la red como una cadena de engranajes:

- El error aparece al final
- Se transmite hacia atrás
- Cada engranaje recibe una parte del error
- Cada peso ajusta su contribución

Idea clave:

> Cuanto más influyó un peso en el error,
> mayor será su corrección.

![Flujo del error hacia atrás](images/43_error_flow_gears.png)

---

## 8.7. Backpropagation y funciones de activación

Las funciones de activación juegan un papel crítico porque:

- Introducen no linealidad
- Afectan al gradiente
- Pueden amplificar o atenuar el error

Por eso:
- Algunas activaciones facilitan el aprendizaje
- Otras pueden provocar problemas (gradientes muy pequeños)

Este tema se profundizará en capítulos posteriores.

![Activaciones y gradientes](images/44_activaciones_gradientes.png)

---

## 8.8. Por qué backpropagation es eficiente

Sin backpropagation:
- Calcular gradientes sería inviable
- El coste computacional sería enorme

Backpropagation:
- Reutiliza cálculos intermedios
- Evita cálculos redundantes
- Escala a redes muy grandes

Es una de las razones por las que el deep learning es posible hoy.

---

## 8.9. Backpropagation en librerías modernas

En la práctica:
- No implementamos backpropagation manualmente
- Las librerías lo hacen por nosotros

Ejemplos:
- TensorFlow: `GradientTape`
- PyTorch: `autograd`

Estas herramientas:
- Construyen automáticamente el grafo de operaciones
- Calculan derivadas
- Gestionan el backward pass

Nuestro papel como desarrolladores es:
- Diseñar la arquitectura
- Elegir la pérdida
- Elegir el optimizador

---

## 8.10. Errores comunes al entender backpropagation

Es importante aclarar que backpropagation:

- ❌ No es “magia”
- ❌ No es exclusivo del deep learning
- ❌ No significa que la red “entienda” los datos

Es simplemente:
> Aplicación sistemática de derivadas
> a una cadena de operaciones.

---

## 8.11. Qué cambia respecto al ML clásico

En modelos clásicos:
- Pocos parámetros
- Gradientes simples
- Optimización directa

En redes neuronales:
- Millones de parámetros
- Dependencias profundas
- Necesidad de backpropagation

Esto explica:
- El mayor coste computacional
- El uso intensivo de GPU
- La importancia de frameworks especializados

---

## 8.12. Idea clave del capítulo

> Backpropagation es el mecanismo que permite
> que las redes neuronales aprendan ajustando todos sus pesos
> de forma coherente y eficiente.

Sin backpropagation:
- No habría deep learning moderno
- No habría entrenamiento a gran escala

---

## 8.13. Cierre del bloque teórico

Con este capítulo ya hemos cubierto:

- Tensores y operaciones
- Función de pérdida
- Gradientes
- Gradiente descendente
- Backpropagation

A partir de ahora:
> Pasamos de la teoría a la práctica.

Entramos en:
- Keras
- PyTorch
- Implementación real de redes neuronales

---

## 8.14. Desde la teoría a la práctica

Backpropagation es automático en todos los frameworks modernos. Pero es vital que entiendas qué sucede "detrás de cámaras" para debugging y optimización.

👉 **Observe GradientTape en acción** en [PyTorch Multiclase](../../Parte-2-Pract/UD4_05_Red_Neuronal_PyTorch_Multiclase_FashionMNIST.ipynb) y [JAX Fashion MNIST](../../Parte-2-Pract/UD4_Apendice_JAX_FashionMNIST.ipynb) — nota cómo los frameworks calculan automáticamente los gradientes.

---

## 8.15. Preguntas de autoevaluación

### Opción múltiple

1. **¿Cuál es el propósito fundamental de backpropagation?**
   - A) Complicar el código  
   - **B) Calcular eficientemente los gradientes de la pérdida respecto a todos los pesos**  
   - C) Validar los datos  
   - D) Generar gráficos

2. **¿En qué orden se calculan los gradientes en backpropagation?**
   - A) De entrada a salida (forward)  
   - **B) De salida a entrada (backward), usando la regla de la cadena**  
   - C) En orden aleatorio  
   - D) No importa el orden

3. **¿Por qué es eficiente backpropagation en comparación con calcular derivadas numéricamente?**
   - A) Porque usa GPUs  
   - **B) Porque reutiliza cálculos intermedios de la pasada forward**  
   - C) Porque no usa derivadas  
   - D) No hay diferencia real

### Pregunta corta

4. **¿Qué es el problema de vanishing gradient? ¿En qué tipo de redes es más problemático?** (3-4 líneas)
