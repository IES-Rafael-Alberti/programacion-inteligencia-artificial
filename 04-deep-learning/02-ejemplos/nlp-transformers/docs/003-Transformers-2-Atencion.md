---
title: "Transformers 2: Mecanismo de Atención"
output:
  html_document:
    toc: true
    toc_depth: 2
    toc_float: true
    number_sections: true
    fig_caption: true
    code_folding: hide
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true
    fig_caption: true
    latex_engine: xelatex
---


# Transformers

## 🌟 ¿Qué es un modelo Transformer?

Un **Transformer** es un tipo de red neuronal diseñada para **entender secuencias de datos**, como frases, párrafos o incluso código. Es el modelo que está detrás de tecnologías como **ChatGPT**, **Google Translate** o **BERT**.

### 🔍 ¿Para qué sirve?

Principalmente, se usa para tareas de **procesamiento del lenguaje natural (NLP)** como:

* Traducir idiomas
* Resumir textos
* Contestar preguntas
* Completar frases o escribir texto

### 🧠 ¿Cómo funciona a grandes rasgos?

En vez de leer palabra por palabra en orden (como lo hace una RNN), el Transformer **lee toda la frase al mismo tiempo** y decide **a qué palabras debe prestar más atención**. A eso se le llama **atención**.

Por ejemplo:

> En la frase “El gato se subió al árbol porque *era alto*”, ¿a qué se refiere "alto"?
> El Transformer usa **atención** para ver que se refiere a **árbol**, no al gato.

### 🧩 ¿Cuáles son sus piezas principales?

1. **Embeddings**: convierte palabras en números que se pueden procesar.
2. **Atención** (*Attention*): decide qué palabras son importantes para cada palabra.
3. **Capas** que procesan y combinan la información varias veces.
4. **Decodificador (Decoder)** (opcional): genera nuevas palabras o frases (por ejemplo, en una traducción).

### 🎯 Ventajas frente a modelos anteriores (como RNN o LSTM):

* **Mucho más rápido**: porque procesa todo a la vez (en paralelo).
* **Mejor en contextos largos**: puede tener en cuenta relaciones entre palabras lejanas.
* **Muy flexible**: se adapta a muchas tareas distintas con pocos cambios.

---


## Attention is all you need

Vamos a explicar el "módulo de atención" en términos sencillos. Imagina que estás leyendo un libro y quieres entender una frase en particular. El módulo de atención funciona de manera similar: te ayuda a enfocarte en las partes más importantes de la información.

### ¿Qué es el módulo de atención?
Es una parte clave de los modelos Transformer. Su función principal es ayudar al modelo a "prestar atención" a diferentes partes de una secuencia (como una frase o un párrafo) al mismo tiempo. Esto permite al modelo entender mejor las relaciones entre las palabras y entender el contexto general.

**El foco en una conversación:** Imagina que estás en una habitación con varias personas hablando. Aunque oyes a todos, prestas más atención a la persona con la que estás hablando. El modelo de atención hace algo similar: "escucha" todo, pero se enfoca más en lo que le interesa para entender mejor el mensaje.


### ¿Cómo funciona?
1.  **Entrada**: El módulo de atención recibe una secuencia de datos, como las palabras de una oración.
2.  **Proyección en Q, K y V**: Cada token se transforma en tres vectores llamados **Query (Q)**, **Key (K)** y **Value (V)**.
3.  **Ponderación**: Para cada parte de la secuencia (cada palabra), el módulo calcula un "peso" o "importancia". Este peso indica cuánto debe "prestar atención" el modelo a esa parte.
4.  **Enfoque**: El módulo usa estos pesos para enfocarse en las partes más relevantes de la secuencia.
5.  **Salida**: Finalmente, el módulo produce una representación de la secuencia que resalta las partes más importantes, lo que ayuda al modelo a entender mejor el contexto.

### ¿Qué son Q, K y V?

Estos tres vectores son la base matemática del mecanismo de atención:

* **Q (Query o consulta)**: indica qué está buscando un token.
* **K (Key o clave)**: indica qué puede ofrecer cada token para ser comparado.
* **V (Value o valor)**: contiene la información que se combinará para producir la salida.

Una forma intuitiva de verlo es esta:

* El token actual lanza una **consulta** con `Q`.
* Compara esa consulta con las **claves** `K` del resto de tokens.
* Cuando encuentra tokens relevantes, recoge su contenido a través de `V`.

Por eso suele decirse que **Q decide dónde mirar**, **K ayuda a decidir qué encaja** y **V aporta la información útil**.

### ¿Qué es la scaled dot-product attention?

La forma más habitual de calcular la atención en los Transformer es la llamada **scaled dot-product attention**. Su fórmula es:

$$
Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Donde:

* `QK^T` calcula las puntuaciones de similitud entre consultas y claves.
* `d_k` es la dimensión de los vectores `K`.
* La división por `\sqrt{d_k}` evita que los valores crezcan demasiado cuando la dimensión es grande.

Si no se hiciera esta división, los productos escalares podrían ser muy altos, el **softmax** se volvería demasiado extremo y el entrenamiento sería menos estable.

Por tanto, esta escala sirve para:

* mantener los valores en un rango más razonable,
* obtener distribuciones de atención menos saturadas,
* facilitar un entrenamiento más estable.

### Ejemplo sencillo
Imagina la frase: "El perro marrón corre por el parque".

*   El módulo de atención podría "prestar más atención" a las palabras "perro" y "parque" porque son clave para entender de qué se trata la frase.
*   También podría "prestar menos atención" a palabras como "el" o "por".

### Beneficios
*   **Mejor comprensión**: Permite a los modelos entender el contexto y las relaciones entre las palabras de manera más efectiva.
*   **Mayor eficiencia**: Permite procesar la información de manera más rápida y eficiente.
*   **Escalabilidad**: Funciona bien con secuencias largas, como textos completos.

En resumen, el módulo de atención es como un "foco" que el modelo usa para enfocarse en las partes más importantes de la información, lo que le permite entender mejor el contexto y las relaciones entre las palabras.


Vamos a desglosar un ejemplo paso a paso de cómo se calculan los pesos en el módulo de atención. Para simplificar, usaremos una versión simplificada y un ejemplo muy pequeño.

### Ejemplo: "El gato duerme."

Imaginemos que tenemos un modelo de atención que procesa esta frase.

**1. Representación Inicial (Embeddings)**

*   Primero, cada palabra se convierte en un vector numérico (embedding). Para simplificar, digamos que cada palabra se representa con un vector de dos números:
    *   "El" = \[1, 0]
    *   "gato" = \[0, 1]
    *   "duerme" = \[1, 1]
*   Estos vectores representan las palabras en un espacio numérico.

**2. Cálculo de las "Queries", "Keys" y "Values"**

*   El módulo de atención transforma cada embedding en tres vectores diferentes: "Query" (Q), "Key" (K) y "Value" (V). Esto se hace mediante matrices de pesos (Wq, Wk, Wv) que el modelo aprende durante el entrenamiento.
*   Para simplificar, digamos que usamos las siguientes matrices de pesos (en realidad, serían mucho más complejas):

    *   Wq = \[1, 0; 0, 1]
    *   Wk = \[0, 1; 1, 0]
    *   Wv = \[1, 1; 0, 1]

*   Calculamos Q, K y V para cada palabra:

    *   "El":
        *   Q = \[1, 0] * Wq = \[1, 0]
        *   K = \[1, 0] * Wk = \[0, 1]
        *   V = \[1, 0] * Wv = \[1, 1]
    *   "gato":
        *   Q = \[0, 1] * Wq = \[0, 1]
        *   K = \[0, 1] * Wk = \[1, 0]
        *   V = \[0, 1] * Wv = \[0, 1]
    *   "duerme":
        *   Q = \[1, 1] * Wq = \[1, 1]
        *   K = \[1, 1] * Wk = \[1, 1]
        *   V = \[1, 1] * Wv = \[2, 2]

*   En formato tabla

| Palabra | Q       | K       | V       |
| ------- | ------- | ------- | ------- |
| El      | \[1, 0] | \[0, 1] | \[1, 1] |
| gato    | \[0, 1] | \[1, 0] | \[0, 1] |
| duerme  | \[1, 1] | \[1, 1] | \[2, 2] |

Funcionamiento del módulo de atención:
![En imágenes](./MecanismoDeAtencion.png)

Cálculos en detalle:
![Cálculos del módulo de atención](./CalculoMecanismoDeAtencion.png)

Ejemplo en Python:
```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Palabras y embeddings simplificados
words = ["El", "gato", "duerme"]
embeddings = {
    "El": np.array([1, 0]),
    "gato": np.array([0, 1]),
    "duerme": np.array([1, 1])
}

# Pesos Wq, Wk, Wv (simplificados)
Wq = np.array([[1, 0], [0, 1]])
Wk = np.array([[0, 1], [1, 0]])
Wv = np.array([[1, 1], [0, 1]])

# Q, K, V
Q, K, V = {}, {}, {}
for w, e in embeddings.items():
    Q[w] = e @ Wq
    K[w] = e @ Wk
    V[w] = e @ Wv

# Scores
score_matrix = np.zeros((3, 3))
for i, qw in enumerate(words):
    for j, kw in enumerate(words):
        score_matrix[i, j] = np.dot(Q[qw], K[kw])

# Softmax
def softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()

attention_weights = np.apply_along_axis(softmax, 1, score_matrix)
df = pd.DataFrame(attention_weights, index=words, columns=words)

# Visualización
plt.figure(figsize=(6, 5))
sns.heatmap(df, annot=True, cmap="YlGnBu", cbar=True)
plt.title("Matriz de Atención")
plt.xlabel("Key")
plt.ylabel("Query")
plt.show()

df
```

**3. Cálculo de los "Scores" (Puntuaciones)**

*   Calculamos una puntuación (score) para cada par de palabras. Esto se hace multiplicando la "Query" de una palabra con la "Key" de otra.
*   En este ejemplo, usamos el producto escalar (dot product):

    *   "El" con "El": \[1, 0] . \[0, 1] = 0
    *   "El" con "gato": \[1, 0] . \[1, 0] = 1
    *   "El" con "duerme": \[1, 0] . \[1, 1] = 1
    *   "gato" con "El": \[0, 1] . \[0, 1] = 0
    *   "gato" con "gato": \[0, 1] . \[1, 0] = 0
    *   "gato" con "duerme": \[0, 1] . \[1, 1] = 1
    *   "duerme" con "El": \[1, 1] . \[0, 1] = 1
    *   "duerme" con "gato": \[1, 1] . \[1, 0] = 1
    *   "duerme" con "duerme": \[1, 1] . \[1, 1] = 2

**4. Cálculo de los Pesos (Softmax)**

*   Aplicamos la función "Softmax" a los scores para obtener los pesos. Softmax convierte los scores en probabilidades que suman 1.
*   En este ejemplo, la función Softmax podría dar los siguientes pesos (los valores reales dependerían de la implementación):

    *   "El":
        *   "El": 0.2
        *   "gato": 0.4
        *   "duerme": 0.4
    *   "gato":
        *   "El": 0.3
        *   "gato": 0.2
        *   "duerme": 0.5
    *   "duerme":
        *   "El": 0.3
        *   "gato": 0.3
        *   "duerme": 0.4

**5. Ponderación de los "Values"**

*   Multiplicamos cada vector "Value" por su peso correspondiente y sumamos los resultados. Esto nos da una representación ponderada de la secuencia.
*   Por ejemplo, para "El":
    *   (0.2 \* \[1, 1]) + (0.4 \* \[0, 1]) + (0.4 \* \[2, 2]) = \[1, 1.4]
*   Repetimos este proceso para cada palabra.

**6. Resultado**

*   El resultado final son los nuevos vectores para cada palabra, que tienen en cuenta la información de las otras palabras de la secuencia. Por ejemplo, el nuevo vector para "El" (\[1, 1.4]) ahora contiene información sobre "gato" y "duerme".

### Resumen del Ejemplo

1.  **Embeddings**: Cada palabra se representa como un vector.
2.  **Q, K, V**: Se calculan "Query", "Key" y "Value" para cada palabra.
3.  **Scores**: Se calculan puntuaciones entre las "Queries" y las "Keys".
4.  **Pesos (Softmax)**: Se convierten las puntuaciones en pesos (probabilidades).
5.  **Ponderación**: Se ponderan los "Values" con los pesos y se suman.
6.  **Resultado**: Se obtienen nuevos vectores que representan cada palabra, considerando el contexto.

Este es un ejemplo simplificado, pero ilustra el proceso básico. En modelos reales, se utilizan matrices más grandes, funciones de activación más complejas y se considera la "atención multi-cabeza" para capturar diferentes tipos de relaciones.

¿Cómo es capaz el mecanismo de atención de decidir qué palabras están más relacionadas con Sancho Panza, por ejemplo, para mantener la coherencia? Básicamente cómo el mecanismo de atención crea esas relaciones.

 La clave para que el mecanismo de atención relacione palabras como "Sancho Panza" con otras palabras relevantes reside en cómo el modelo aprende y utiliza las representaciones vectoriales de las palabras y las relaciones entre ellas. Vamos a desglosarlo:

### 1. **Representaciones Vectoriales (Embeddings)**

*   **Cada palabra se convierte en un vector:** Antes de que el modelo procese las palabras, cada una se convierte en un vector numérico (un "embedding"). Estos vectores capturan información semántica sobre las palabras. Palabras que tienen significados similares (como "Sancho Panza" y "escudero") tendrán vectores más cercanos entre sí en el espacio vectorial.
*   **Aprendizaje de los embeddings:** Durante el entrenamiento, el modelo ajusta estos vectores. Aprende a representar las palabras de manera que las relaciones semánticas se reflejen en la cercanía de los vectores.

### 2. **El Proceso de Atención**

*   **Queries, Keys, y Values:** Como vimos antes, el modelo transforma cada embedding en tres vectores: Query (Q), Key (K) y Value (V).
*   **Cálculo de la atención (Scores):** El modelo calcula una puntuación (score) para cada par de palabras. Esta puntuación indica cuán "relacionadas" están dos palabras. Se calcula, por ejemplo, multiplicando la "Query" de una palabra con la "Key" de otra.
*   **Sancho Panza y las palabras relacionadas:**
    *   Si "Sancho Panza" aparece en la frase, su vector "Query" se compara con los vectores "Key" de todas las demás palabras de la frase.
    *   Las palabras que están semánticamente relacionadas con "Sancho Panza" (como "escudero", "caballo", "aventuras", etc.) tendrán vectores "Key" que, al multiplicarse con la "Query" de "Sancho Panza", producirán puntuaciones (scores) más altas.
*   **Softmax y Pesos:** Se aplica Softmax a los scores para obtener pesos (probabilidades). Las palabras con scores más altos tendrán pesos más altos, lo que significa que el modelo "prestará más atención" a esas palabras.

### 3. **Cómo el Modelo "Sabe" qué Palabras están Relacionadas**

*   **Entrenamiento con datos:** El modelo aprende estas relaciones durante el entrenamiento, al exponerse a un gran corpus de texto (en este caso, Don Quijote). El modelo aprende a identificar patrones y relaciones entre las palabras, como la conexión entre "Sancho Panza" y "escudero".
*   **Contexto:** El modelo aprende a considerar el contexto. Por ejemplo, si "Sancho Panza" aparece cerca de palabras como "hambre" o "cansancio", el modelo entenderá que esas palabras también están relacionadas con Sancho.
*   **Matrices de pesos:** Las matrices de pesos (Wq, Wk, Wv) que se utilizan para calcular Q, K y V se ajustan durante el entrenamiento. Estas matrices "codifican" las relaciones entre las palabras. El modelo aprende a usar estas matrices para "transformar" las palabras de manera que se resalten las relaciones importantes.
*   **Parecido**: El producto escalar entre Q y K mide **cuánto se parecen** (cuánta relación hay). Si Q y K son muy similares, el producto será grande. Por eso se dice que el modelo "presta atención" a las palabras más parecidas o relevantes en ese contexto.
* **Atención multicabeza:** Y esto que hemos visto es solo una "cabeza de atención". Los modelos Transformer usan varias cabezas a la vez (atención multicabeza) para fijarse en diferentes aspectos del significado o las relaciones entre palabras.

### 4. **Generación de Texto**

*   **Uso de la atención para la coherencia:** Cuando el modelo genera texto, utiliza la atención para decidir qué palabras son más relevantes para la continuación de la historia. Si el modelo ha mencionado a "Sancho Panza", el mecanismo de atención "activará" las conexiones con las palabras relacionadas con Sancho, lo que influirá en la elección de las siguientes palabras.
*   **Ejemplo:** Si el modelo está generando una frase después de mencionar a "Sancho Panza", el módulo de atención podría "prestar más atención" a palabras como "escudero", "caballo", "viaje", etc. Esto aumentará la probabilidad de que el modelo genere frases que hablen sobre las acciones o los pensamientos de Sancho, manteniendo la coherencia.

### Resumen

El mecanismo de atención crea estas relaciones a través de:

1.  **Representaciones vectoriales (embeddings)** que capturan la semántica de las palabras.
2.  **Cálculo de scores** que miden la relación entre las palabras.
3.  **Aprendizaje a través del entrenamiento** con un gran corpus de texto.
4.  **Uso de la atención** para influir en la generación de texto, priorizando las palabras relacionadas con el contexto.

En resumen, el modelo "aprende" las relaciones entre las palabras durante el entrenamiento, y luego utiliza el mecanismo de atención para "recordar" esas relaciones y generar texto coherente.

Para una ampliación técnica sobre las cabezas de atención y la atención multicabeza, consulta el documento complementario:

➡️ *Transformers 2: Anexo sobre Cabezas de Atención y Multi-Head Attention*
