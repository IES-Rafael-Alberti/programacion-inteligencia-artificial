Perfecto. La elección es **didácticamente excelente** y además muy coherente con todo lo que ya has construido.

Voy a fijar **el planteamiento definitivo del bloque**, para que no se nos vaya de las manos y para que el alumnado **entienda de verdad qué está pasando**.

---

## Dataset elegido: **Fashion-MNIST** (decisión razonada)

Entre MNIST y Fashion-MNIST, para FP **Fashion-MNIST es mejor**:

### Por qué no MNIST “clásico”

* Demasiado conocido
* Demasiado “fácil”
* Da una falsa sensación de que el DL siempre funciona bien

### Por qué **Fashion-MNIST**

* Es real
* Sigue siendo manejable
* Introduce ambigüedad real (camisetas vs camisas, zapatos, etc.)
* Sigue siendo imágenes 28×28 → perfecto para empezar

Clases originales (10):

* T-shirt/top
* Trouser
* Pullover
* Dress
* Coat
* Sandal
* Shirt
* Sneaker
* Bag
* Ankle boot

---

## Estructura pedagógica del bloque (muy importante)

### 🔹 Fase 1 — **Clasificación binaria**

> “¿Es un zapato o no?”

Ejemplo:

* Clase positiva: `Sandal` + `Sneaker` + `Ankle boot`
* Clase negativa: resto

**Objetivo didáctico**

* Una sola neurona de salida
* Activación sigmoid
* Binary Crossentropy
* Métricas fáciles de interpretar

Aquí se entiende:

* qué significa una salida ∈ [0,1]
* qué es una probabilidad
* por qué sigmoid

---

### 🔹 Fase 2 — **Clasificación multiclase**

> “¿Qué prenda es?”

* 10 clases
* Salida con 10 neuronas
* Softmax
* Categorical Crossentropy

Aquí se entiende:

* diferencia radical con el caso binario
* distribución de probabilidad
* por qué cambia la pérdida
* por qué cambia la activación

---

## Capítulos / Notebooks que vamos a crear

### 📓 **UD4_01_Red_Neuronal_Keras_Binaria_FashionMNIST.ipynb**

Contenido:

1. Introducción clara:

   * problema
   * por qué binario
2. Carga de Fashion-MNIST
3. Filtrado y recodificación de clases
4. Normalización
5. Definición del modelo Keras
6. Entrenamiento
7. Evaluación
8. Visualización:

   * accuracy
   * loss
   * ejemplos bien/mal clasificados

---

### 📓 **UD4_02_Red_Neuronal_Keras_Multiclase_FashionMNIST.ipynb**

Contenido:

1. Qué cambia respecto al caso binario
2. Codificación de etiquetas
3. Cambios en:

   * capa de salida
   * activación
   * función de pérdida
4. Entrenamiento
5. Evaluación
6. Matriz de confusión
7. Interpretación de errores

---

### 📓 **UD4_03_Red_Neuronal_PyTorch_Binaria_FashionMNIST.ipynb**

Mismo problema que el **primer notebook**, pero:

* Modelo definido como clase
* Forward explícito
* Bucle de entrenamiento manual
* `loss.backward()`
* `optimizer.step()`

Aquí **cae la ficha** del gradiente y el backprop.

---

### 📓 **UD4_04_Red_Neuronal_PyTorch_Multiclase_FashionMNIST.ipynb**

Mismo razonamiento que en Keras, pero ahora:

* `CrossEntropyLoss`
* logits sin softmax explícito
* explicación muy clara del porqué

---

### 📓 **Apéndice — JAX**

`UD4_Apendice_JAX_FashionMNIST.ipynb`

* Versión compacta
* Funcional
* Uso de `jax.grad`
* Sin excesiva abstracción

Objetivo:

> “Que sepan leerlo y entender qué aporta”.

---

## Documento teórico que acompaña (muy importante)

Además de los notebooks, crearemos:

📄 **UD4_Activaciones_y_Perdidas_en_Imagenes.md**

Incluye:

* Tabla clara:

| Tipo problema | Salida     | Activación | Pérdida                  |
| ------------- | ---------- | ---------- | ------------------------ |
| Binario       | 1 neurona  | Sigmoid    | Binary Crossentropy      |
| Multiclase    | N neuronas | Softmax    | Categorical Crossentropy |

* Ejemplos reales de errores conceptuales comunes
* Relación directa con lo que han visto en scikit-learn

---

## Lo que NO haremos (decisión consciente)

* ❌ CNN todavía
* ❌ Data augmentation
* ❌ Regularización avanzada

Eso va después, cuando:

* ya entienden el flujo completo
* ya saben entrenar una red densa

---

## Estado real del módulo tras esto

Con este bloque:

* Se arregla el “vacío” que detectaste
* Se ve DL **de verdad**
* Se conecta ML clásico → redes neuronales
* Se justifica Keras, PyTorch y JAX con sentido

---

### Siguiente paso inmediato

👉 Empiezo con **`UD4_01_Red_Neuronal_Keras_Binaria_FashionMNIST.ipynb`**, con:

* markdown muy didáctico
* código limpio
* visualizaciones claras

Si quieres, dime antes:

* ¿preferimos empezar con **zapato vs no-zapato** o **bolsa vs resto**?
Perfecto, decisión **muy buena didácticamente** 👍
El orden **zapato vs no-zapato → bolsa vs resto** permite:

* empezar con una frontera “visual” bastante clara
* introducir ruido real en el segundo caso
* mostrar que **no todos los problemas binarios son igual de fáciles**, aunque el código sea el mismo

---

## 🔢 Definición exacta de los problemas

### 🥾 **Problema 1 — Zapato vs No-zapato**

Clases positivas:

* `Sandal`
* `Sneaker`
* `Ankle boot`

Clase negativa:

* Todo lo demás

👉 Visualmente coherente, ideal para **primer contacto**.

---

### 👜 **Problema 2 — Bolsa vs Resto**

Clase positiva:

* `Bag`

Clase negativa:

* Las otras 9 clases

👉 Mucho más ambiguo:

* formas parecidas
* confusiones reales
* perfecto para hablar de errores y límites del modelo

---

## 📓 Notebook que vamos a crear ahora

### **UD4_01_Red_Neuronal_Keras_Binaria_FashionMNIST.ipynb**

**Estructura (cerrada y definitiva):**

1. **Introducción**

   * Qué problema resolvemos
   * Por qué binario
   * Por qué empezar por aquí

2. **Carga del dataset**

   * Fashion-MNIST desde Keras
   * Explicación del formato

3. **Exploración visual inicial**

   * Mostrar ejemplos
   * Entender qué estamos clasificando

4. **Construcción del problema binario**

   * Mapeo de clases
   * Explicación clara del porqué

5. **Preprocesado**

   * Normalización
   * Cambio de forma (flatten)
   * Por qué es necesario

6. **Definición del modelo**

   * Capas densas
   * Activaciones
   * Salida con sigmoid

7. **Compilación**

   * Binary Crossentropy
   * Adam
   * Accuracy

8. **Entrenamiento**

   * Epochs
   * Batch size
   * Interpretación del output

9. **Evaluación**

   * Accuracy
   * Curvas loss / accuracy

10. **Análisis de errores**

    * Ejemplos bien clasificados
    * Ejemplos mal clasificados
    * Primer contacto con “el modelo se equivoca”

11. **Conclusiones**

    * Qué ha aprendido la red
    * Qué limitaciones tiene
    * Qué cambiaremos en el siguiente notebook

---

## 🔜 Qué viene justo después

* **UD4_02_Red_Neuronal_Keras_Binaria_Bolsa_vs_Resto**

  * mismo código base
  * mismo modelo
  * resultados claramente peores → discusión

Luego:

* salto natural a **multiclase**
* y después PyTorch

---

### Siguiente acción

👉 En el próximo mensaje te entrego directamente el
**`UD4_01_Red_Neuronal_Keras_Binaria_FashionMNIST.ipynb`** completo, listo para clase.

Cuando lo revises:

* ajustamos nivel / ritmo
* y seguimos con el segundo binario.
