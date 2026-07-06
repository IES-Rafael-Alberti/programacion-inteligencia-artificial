# Capítulo 10 — Convolutional Neural Networks (CNN)

*(Cómo aprenden las redes neuronales a “ver”)*

Hasta ahora hemos trabajado con redes densas (*fully connected*).
Funcionan bien… pero tienen un problema grave cuando trabajamos con imágenes.

La pregunta que abre este capítulo es:

> ¿Por qué no usamos simplemente una red densa para clasificar imágenes grandes?

---

# 10.1 El problema de las capas densas en imágenes

Supongamos una imagen de:

* 128 × 128 píxeles
* En escala de grises

Eso son:

[
128 \times 128 = 16,384 \text{ entradas}
]

Si conectamos esa entrada a una capa de 256 neuronas:

[
16,384 \times 256 = 4,194,304 \text{ pesos}
]

Solo en la primera capa.

---

## Problemas

* Demasiados parámetros
* Sobreajuste inmediato
* Ignora estructura espacial
* No reutiliza patrones

---

## Intuición clave

Una red densa:

* No sabe que dos píxeles vecinos están relacionados.
* Trata cada píxel como independiente.

Eso es antinatural para imágenes.

---

# 10.2 Idea central de las CNN

Las CNN se basan en una hipótesis muy fuerte y razonable:

> En imágenes, los patrones importantes son locales.

Ejemplos:

* Bordes
* Texturas
* Curvas
* Esquinas

Y esos patrones:

* pueden aparecer en cualquier parte de la imagen.

---

# 10.3 La Convolución (nivel intuitivo)

Imagina una pequeña ventana (filtro) que:

* recorre la imagen
* multiplica valores
* suma el resultado
* produce una activación

Eso genera un nuevo mapa:

→ **Feature Map**

---

## Metáfora sencilla

Si una red densa es:

> "Analizar todos los ingredientes a la vez"

Una CNN es:

> "Buscar patrones pequeños que se repiten en distintas partes"

---

# 10.4 Convolución (nivel matemático suave)

Sea una imagen ( I ) y un filtro ( K ):

[
S(i,j) = \sum_m \sum_n I(i+m, j+n) \cdot K(m,n)
]

Esto es:

* Producto elemento a elemento
* Suma local
* Repetido por toda la imagen

---

# 10.5 Parámetros compartidos

Clave absoluta:

En CNN:

* El mismo filtro se aplica en toda la imagen.
* Los pesos se comparten.

Esto reduce:

* Parámetros
* Sobreajuste
* Coste computacional

---

# 10.6 Arquitectura típica de una CNN

Estructura básica:

```plaintext
Imagen
→ Convolución
→ Activación
→ Pooling
→ Convolución
→ Activación
→ Pooling
→ Flatten
→ Capas densas
→ Salida
```

---

# 10.7 Pooling

El pooling:

* Reduce dimensiones
* Hace el modelo más robusto
* Reduce sensibilidad a pequeñas traslaciones

Tipos comunes:

* Max Pooling
* Average Pooling

---

# 10.8 Interpretación geométrica

Una CNN:

* No transforma directamente el espacio completo.
* Extrae representaciones progresivamente más abstractas.

Ejemplo conceptual:

* Capa 1 → detecta bordes
* Capa 2 → detecta formas simples
* Capa 3 → detecta partes de objetos
* Capas finales → detectan objetos

Esto es:

> Jerarquía de representación.

---

# 10.9 Comparación: Densa vs CNN

| Característica            | Red Densa            | CNN        |
| ------------------------- | -------------------- | ---------- |
| Conexiones                | Totalmente conectada | Local      |
| Parámetros                | Muchos               | Menos      |
| Estructura espacial       | Ignorada             | Preservada |
| Escalabilidad en imágenes | Mala                 | Buena      |

---

# 10.10 Conexión con backpropagation

Nada cambia en el mecanismo fundamental:

* Se calcula pérdida
* Se propagan gradientes
* Se actualizan pesos

La única diferencia es:

> La estructura de la red.

Backpropagation funciona igual.

---

# 10.11 Implementación mínima en Keras

Ejemplo básico:

```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])
```

---

# 10.12 Implementación equivalente en PyTorch

```python
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3)
        self.pool = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.fc1 = nn.Linear(64*5*5, 64)
        self.fc2 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```

---

# 10.13 Qué hemos ganado

Con CNN:

* Menos parámetros
* Mejor generalización
* Capacidad para trabajar con imágenes reales
* Estructura inductiva adecuada

---

# 10.14 Lo que veremos a continuación

Las CNN profundas introducen nuevos problemas:

* Sobreajuste
* Gradientes inestables
* Necesidad de regularización

Eso nos lleva directamente a:

> Capítulo 11 — Profundidad, Overfitting y Bias–Variance

---

# 📌 Resultado de este capítulo

Entender deberíais:

* Entender por qué no usamos capas densas en imágenes.
* Comprender qué es una convolución.
* Saber qué hace pooling.
* Implementar una CNN básica.
* Relacionar arquitectura con representación.
