# 00 — Introducción a la Visión por Computador Clásica

Antes de las redes neuronales profundas, la visión por computador ya existía.

Durante décadas se desarrollaron sistemas capaces de:

* Detectar bordes
* Extraer características
* Reconocer objetos simples
* Detectar rostros
* Segmentar imágenes

Pero el enfoque era radicalmente distinto al actual.

---

# 00.1 ¿Qué es la visión por computador?

La visión por computador busca:

> Extraer información útil de imágenes.

Esto puede incluir:

* Clasificación
* Detección de objetos
* Seguimiento
* Segmentación
* Reconocimiento facial

---

# 00.2 Enfoque clásico: pipeline manual

La visión clásica seguía un pipeline muy claro:

```plaintext
Imagen
→ Preprocesamiento
→ Extracción de características
→ Clasificador tradicional
```

La parte clave era:

> La ingeniería de características.

El humano decidía:

* Qué patrones buscar
* Cómo representarlos
* Qué algoritmo usar después

---

# 00.3 Ejemplo 1 — Cargar y visualizar imágenes (PIL)

```python
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("imagen.jpg")
plt.imshow(img)
plt.axis("off")
plt.show()
```

Aquí no hay aprendizaje.

Solo manipulación directa de píxeles.

---

# 00.4 Operaciones básicas clásicas

En visión clásica se usaban:

* Escala de grises
* Umbralización
* Detección de bordes
* Filtros
* Morfología matemática

---

## Ejemplo 2 — Detección de bordes simple (Sobel)

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("imagen.jpg", 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

plt.imshow(sobelx, cmap="gray")
plt.title("Bordes horizontales")
plt.show()
```

Esto detecta cambios bruscos de intensidad.

Pero:

* No entiende qué es un objeto
* Solo detecta cambios de píxeles

---

# 00.5 Extracción de características clásicas

Durante años se usaron:

* Histogramas de color
* HOG (Histogram of Oriented Gradients)
* SIFT
* SURF
* LBP

Estas características eran:

* Diseñadas manualmente
* Basadas en intuición geométrica

---

# 00.6 Ejemplo conceptual — HOG

La idea:

* Detectar orientaciones de bordes
* Agruparlas en histogramas
* Usarlas como vector de características

Luego se entrenaba un SVM o un clasificador.

Pipeline:

```plaintext
Imagen
→ HOG
→ SVM
→ Predicción
```

---

# 00.7 Detección facial clásica (dlib / OpenCV)

Ejemplo simplificado:

```python
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

img = cv2.imread("persona.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
```

Este sistema:

* No usa Deep Learning.
* Usa clasificadores en cascada (Haar features).

---

# 00.8 Limitaciones del enfoque clásico

* Dependencia extrema del experto.
* Características específicas para cada problema.
* Mala generalización.
* Dificultad en problemas complejos.
* Sensibilidad a iluminación, rotación, escala.

Cada nuevo problema requería:

> Diseñar nuevas características.

---

# 00.9 El punto de ruptura

Deep Learning cambia esto completamente:

En lugar de:

```plaintext
Imagen → Features diseñadas → Clasificador
```

Tenemos:

```plaintext
Imagen → Red neuronal → Representaciones aprendidas → Clasificación
```

Las características dejan de ser diseñadas.

Son aprendidas.

---

# 00.10 Puente hacia CNN

La pregunta ahora es:

> ¿Puede una red aprender automáticamente esos filtros de bordes, texturas y formas?

La respuesta es:

> Sí. Eso es exactamente lo que hace una CNN.

Y lo hace:

* sin que el humano defina los filtros
* ajustándolos con backpropagation

---

# 🎯 Objetivo pedagógico de este capítulo

Hay que entender:

* Que la visión clásica funcionaba.
* Que no todo empezó con Deep Learning.
* Que CNN no es magia.
* Que las convoluciones no son invento nuevo (ya existían como filtros).
