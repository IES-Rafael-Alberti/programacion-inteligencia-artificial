# Más allá de las CNN: evolución de los modelos de visión artificial

## 1. Introducción

Durante más de una década, las **redes neuronales convolucionales (CNN)** han sido la arquitectura dominante en visión por computador.

Modelos como:

* AlexNet
* VGG
* ResNet
* EfficientNet

han permitido avances enormes en tareas como:

* clasificación de imágenes
* detección de objetos
* segmentación
* reconocimiento facial

Sin embargo, en los últimos años han aparecido **nuevas arquitecturas** que intentan superar o complementar a las CNN.

---

# 2. ¿Están obsoletas las CNN?

No.

Las CNN **siguen siendo extremadamente útiles y competitivas**.

Lo que ha ocurrido es que han aparecido **alternativas que funcionan mejor en ciertos escenarios**.

Especialmente cuando:

* hay **datasets gigantes**
* se utilizan **clusters de GPUs**
* se entrenan **modelos fundacionales**

En esos casos han surgido modelos basados en **Transformers**.

---

# 3. Vision Transformers

En 2021 Google publicó el artículo:

> **An Image Is Worth 16×16 Words: Transformers for Image Recognition**

La idea principal es tratar una imagen **como una secuencia de parches**, de forma similar a cómo los Transformers procesan palabras en lenguaje natural.

### Pasos principales

1. Dividir la imagen en **patches**.
2. Convertir cada parche en un **vector (embedding)**.
3. Añadir **positional embeddings**.
4. Procesar la secuencia mediante **auto-atención**.
5. Clasificar la imagen con un **MLP**.

Esto permite que el modelo capture **relaciones globales entre regiones de la imagen**.

---

# 4. Sesgos inductivos: CNN vs Transformers

Las CNN tienen **sesgos inductivos fuertes**, es decir, su arquitectura ya incorpora ciertas suposiciones sobre las imágenes.

Por ejemplo:

### Localidad

Los filtros operan sobre regiones pequeñas.

### Compartición de pesos

El mismo filtro se aplica en toda la imagen.

### Invariancia traslacional

Un objeto sigue siendo el mismo aunque cambie ligeramente de posición.

Los Transformers **no tienen estas suposiciones**, lo que los hace más flexibles pero también más dependientes de grandes cantidades de datos.

---

# 5. Nuevas arquitecturas eficientes

En los últimos años han aparecido nuevas familias de modelos que buscan mejorar la eficiencia de los Transformers.

Entre ellas destacan los **State-Space Models (SSM)** y los **Liquid Foundation Models (LFM)**.

Estos modelos sustituyen el mecanismo de atención por **dinámicas de estado** que permiten:

* menor consumo de memoria
* coste computacional lineal
* mejor escalabilidad en secuencias largas

Un ejemplo destacado es **Mamba**.

---

# 6. Comparación de arquitecturas

| Modelo      | Ventaja principal                               | Limitación               |
| ----------- | ----------------------------------------------- | ------------------------ |
| CNN         | Muy eficientes y funcionan bien con pocos datos | Contexto global limitado |
| ViT         | Modelan relaciones globales                     | Necesitan muchos datos   |
| SSM / Mamba | Muy eficientes y escalables                     | Aún en investigación     |

---

# 7. Convergencia de ideas

Hoy en día no se observa una sustitución total de unas arquitecturas por otras.

En su lugar, el campo está evolucionando hacia **modelos híbridos** que combinan ideas de varias familias.

Por ejemplo:

* Transformers con ventanas locales
* CNN con atención
* modelos SSM con convoluciones

El futuro de la visión artificial probablemente estará formado por **arquitecturas híbridas que combinan eficiencia y capacidad expresiva**.


## Anexo I
Buena pregunta, porque **conceptualmente se parecen pero no son lo mismo**. De hecho, comparar **patches de ViT** con **máscaras de convolución** es una forma muy buena de explicarlo a alumnos.

Voy a ponerlo claro.

---

# 1️⃣ Parecido conceptual

Ambos trabajan con **regiones locales de la imagen**.

| CNN                              | ViT                            |
| -------------------------------- | ------------------------------ |
| Usa **filtros pequeños**         | Usa **patches de imagen**      |
| El filtro se mueve por la imagen | La imagen se divide en bloques |
| Aprende características locales  | Procesa bloques como tokens    |

Por eso **visual y pedagógicamente sí puedes decir**:

> Los patches de un ViT recuerdan a las ventanas locales que usan las convoluciones.

Pero el mecanismo interno es distinto.

---

# 2️⃣ Diferencia fundamental

### CNN

Un filtro **se desliza** por la imagen.

Ejemplo:

```
imagen 28x28
filtro 3x3
stride 1
```

El filtro se aplica en **muchas posiciones**:

```
posición (1,1)
posición (1,2)
posición (1,3)
...
```

✔ misma máscara
✔ muchos lugares

Esto produce el **feature map**.

---

### ViT

El ViT **no desliza nada**.

La imagen se **trocea una sola vez**.

Ejemplo:

```
imagen 28x28
patch 7x7
```

Resultado:

```
4 x 4 patches = 16 tokens
```

Cada patch se convierte en un vector.

```
patch → flatten → embedding
```

Luego el Transformer trabaja con la **secuencia de patches**.

---

# 3️⃣ Tamaño de patch

Sí: **es fijo y se define antes de entrenar**.

Ejemplo típico:

| Modelo          | Patch |
| --------------- | ----- |
| ViT original    | 16×16 |
| DeiT            | 16×16 |
| ViT small       | 8×8   |
| Ejemplo docente | 7×7   |

Para Fashion-MNIST usamos:

```
patch = 7x7
```

porque:

```
28 / 7 = 4
```

y obtenemos:

```
4 x 4 = 16 patches
```

que es muy cómodo de visualizar.

---

# 4️⃣ Analogía que funciona muy bien en clase

Puedes decir algo así:

### CNN

La red usa **una lupa pequeña** que recorre toda la imagen.

```
lupa = filtro convolucional
```

---

### ViT

La red **corta la imagen en piezas de puzzle**.

```
cada pieza = patch
```

Luego intenta entender la imagen **viendo cómo se relacionan las piezas**.

---

# 5️⃣ Diferencia importante para entender los modelos

Las CNN tienen **sesgos inductivos fuertes**:

* locality
* weight sharing
* translational invariance

El ViT **no tiene eso**.

Por eso:

| Modelo | Necesita datos |
| ------ | -------------- |
| CNN    | pocos          |
| ViT    | muchos         |

---

# 6️⃣ Visualización muy útil para alumnos

Podrías dibujarlo así:

```
CNN
imagen → filtro 3x3 que se mueve → feature maps

ViT
imagen → dividir en patches → embeddings → transformer
```

Si quieres, en el siguiente paso puedo generarte **una figura muy buena para explicar esto en clase**:

```
convolution sliding window
vs
vit patches grid
```

