## Procesamiento del Lenguaje Natural con RNNs y Atención

Cuando Alan Turing imaginó su famosa prueba de Turing en 1950, propuso una manera de evaluar la capacidad de una máquina para igualar la inteligencia humana. Podría haber probado muchas cosas, como la habilidad de reconocer gatos en imágenes, jugar ajedrez, componer música o escapar de un laberinto, pero, curiosamente, eligió una tarea lingüística. Más específicamente, ideó un chatbot capaz de engañar a su interlocutor haciéndole pensar que era humano. Esta prueba sí tiene sus debilidades: un conjunto de reglas predefinidas puede engañar a humanos desprevenidos o ingenuos (por ejemplo, la máquina podría dar respuestas vagas predefinidas en respuesta a algunas palabras clave, podría pretender que está bromeando o borracho para obtener un pase en sus respuestas más extrañas, o podría escapar de preguntas difíciles respondiéndolas con sus propias preguntas), y muchos aspectos de la inteligencia humana son completamente ignorados (por ejemplo, la capacidad de interpretar la comunicación no verbal como las expresiones faciales, o aprender una tarea manual). Pero la prueba sí resalta el hecho de que dominar el lenguaje es, posiblemente, la mayor habilidad cognitiva del Homo sapiens.

¿Podemos construir una máquina que domine el lenguaje escrito y hablado? Este es el objetivo final de la investigación en PNL, pero es un poco amplio, así que en la práctica los investigadores se centran en tareas más específicas, como la clasificación de textos, traducción, resumen, respuesta a preguntas y muchas más.
Un enfoque común para las tareas de lenguaje natural es utilizar redes neuronales recurrentes. Por lo tanto, continuaremos explorando las RNNs (introducidas en el Capítulo 15), comenzando con una RNN de caracteres, o char-RNN, entrenada para predecir el siguiente carácter en una oración. Esto nos permitirá generar algún texto original. Primero utilizaremos una RNN sin estado (que aprende en porciones aleatorias de texto en cada iteración, sin ninguna información sobre el resto del texto), luego construiremos una RNN con estado (que conserva el estado oculto entre las iteraciones de entrenamiento y continúa leyendo donde se detuvo, permitiéndole aprender patrones más largos). A continuación, construiremos una RNN para realizar análisis de sentimientos (por ejemplo, leer reseñas de películas y extraer el sentimiento del crítico sobre la película), esta vez tratando las oraciones como secuencias de palabras, en lugar de caracteres.
Luego mostraremos cómo las RNNs pueden ser utilizadas para construir una arquitectura de codificador-decodificador capaz de realizar la traducción automática neuronal (NMT), traduciendo del inglés al español.
En la segunda parte de este capítulo, exploraremos los mecanismos de atención. Como su nombre sugiere, estos son componentes de redes neuronales que aprenden a seleccionar la parte de las entradas en la que el resto del modelo debería enfocarse en cada paso de tiempo. Primero, mejoraremos el rendimiento de una arquitectura de codificador-decodificador basada en RNN utilizando atención. A continuación, dejaremos de lado las RNNs y utilizaremos una arquitectura solo de atención, llamada transformador, para construir un modelo de traducción. Luego discutiremos algunos de los avances más importantes en PNL en los últimos años, incluyendo modelos de lenguaje increíblemente poderosos como GPT y BERT, ambos basados en transformadores. Por último, te mostraré cómo comenzar con la excelente biblioteca Transformers de Hugging Face.
Comencemos con un modelo simple y divertido que puede escribir como Shakespeare (más o menos).


## Generando texto al estilo de Shakespeare usando una RNN de caracteres
En una famosa publicación de blog de 2015 titulada "La irrazonable eficacia de las Redes Neuronales Recurrentes", Andrej Karpathy mostró cómo entrenar una RNN para predecir el siguiente carácter en una oración. Esta char-RNN puede entonces utilizarse para generar texto novedoso, un carácter a la vez. Aquí hay una pequeña muestra del texto generado por un modelo de char-RNN después de haber sido entrenado con todas las obras de Shakespeare:
PANDARUS:
Ay, creo que se acerca el día
cuando poco se ganaría al ser nunca alimentado,
y quién es sino una cadena y súbditos de su muerte,
no debería dormir.
No es exactamente una obra maestra, pero sigue siendo impresionante que el modelo haya podido aprender palabras, gramática, puntuación adecuada y más, simplemente aprendiendo a predecir el siguiente carácter en una oración. Este es nuestro primer ejemplo de un modelo de lenguaje; modelos de lenguaje similares (pero mucho más poderosos), discutidos más adelante en este capítulo, están en el núcleo de la PNL moderna. En el resto de esta sección, construiremos una char-RNN paso a paso, comenzando con la creación del conjunto de datos.

##Creando el conjunto de datos de entrenamiento
Primero, usando la función útil de Keras tf.keras.utils.get_file(), descarguemos todas las obras de Shakespeare. Los datos se cargan desde el proyecto char-rnn de Andrej Karpathy:
```python
import tensorflow as tf
shakespeare_url = "https://homl.info/shakespeare" # URL abreviada
filepath = tf.keras.utils.get_file("shakespeare.txt", shakespeare_url)
with open(filepath) as f:
    shakespeare_text = f.read()
```
Imprimamos las primeras líneas:
```python
>>> print(shakespeare_text[:80])
First Citizen:
Before we proceed any further, hear me speak.
All:
Speak, speak.
```
¡Parece Shakespeare sin duda!

A continuación, usaremos una capa tf.keras.layers.TextVectorization (introducida en el Capítulo 13) para codificar este texto. Establecemos split="character" para obtener una codificación a nivel de carácter en lugar de la codificación a nivel de palabra predeterminada, y usamos standardize="lower" para convertir el texto a minúsculas (lo que simplificará la tarea):
```python
text_vec_layer = tf.keras.layers.TextVectorization(split="character", standardize="lower")
text_vec_layer.adapt([shakespeare_text])
encoded = text_vec_layer([shakespeare_text])[0]
```
Cada carácter ahora está mapeado a un entero, comenzando en 2. La capa TextVectorization reservó el valor 0 para tokens de relleno y reservó 1 para caracteres desconocidos. No necesitaremos ninguno de estos tokens por ahora, así que restemos 2 de los IDs de caracteres y calculemos el número de caracteres distintos y el número total de caracteres:
```python
encoded -= 2 # descartar tokens 0 (relleno) y 1 (desconocido), que no usaremos
n_tokens = text_vec_layer.vocabulary_size() - 2 # número de caracteres distintos = 39
dataset_size = len(encoded) # número total de caracteres = 1,115,394
```
A continuación, al igual que hicimos en el Capítulo 15, podemos convertir esta secuencia muy larga en un conjunto de datos de ventanas que luego podemos usar para entrenar una RNN de secuencia a secuencia. Los objetivos serán similares a las entradas, pero desplazados un paso de tiempo hacia el "futuro". Por ejemplo, una muestra en el conjunto de datos puede ser una secuencia de IDs de caracteres que representan el texto "to be or not to b" (sin la "e" final), y el objetivo correspondiente: una secuencia de IDs de caracteres que representan el texto "o be or not to be" (con la "e" final, pero sin la "t" inicial).
Escribamos una pequeña función de utilidad para convertir una larga secuencia de IDs de caracteres en un conjunto de datos de pares de ventanas de entrada/objetivo:
```python
def to_dataset(sequence, length, shuffle=False, seed=None, batch_size=32):
    ds = tf.data.Dataset.from_tensor_slices(sequence)
    ds = ds.window(length + 1, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda window_ds: window_ds.batch(length + 1))
    if shuffle:
        ds = ds.shuffle(buffer_size=100_000, seed=seed)
    ds = ds.batch(batch_size)
    return ds.map(lambda window: (window[:, :-1], window[:, 1:])).prefetch(1)
```
Esta función comienza de manera similar a la función de utilidad personalizada to_windows() que creamos en el Capítulo 15:
- Toma una secuencia como entrada (es decir, el texto codificado) y crea un conjunto de datos que contiene todas las ventanas de la longitud deseada.
- Aumenta la longitud en uno, ya que necesitamos el siguiente carácter para el objetivo.
- Luego, baraja las ventanas (opcionalmente), las agrupa en lotes, las divide en pares de entrada/salida y activa la precarga.

La Figura 16-1 resume los pasos de preparación del conjunto de datos: muestra ventanas de longitud 11 y un tamaño de lote de 3. El índice de inicio de cada ventana se indica al lado.
![link text](ShuffledWindows.png)

Ahora estamos listos para crear el conjunto de entrenamiento, el conjunto de validación y el conjunto de prueba. Utilizaremos aproximadamente el 90% del texto para el entrenamiento, el 5% para la validación y el 5% para las pruebas:
```python
length = 100
tf.random.set_seed(42)
train_set = to_dataset(encoded[:1_000_000], length=length, shuffle=True, seed=42)
valid_set = to_dataset(encoded[1_000_000:1_060_000], length=length)
test_set = to_dataset(encoded[1_060_000:], length=length)
```
CONSEJO
Establecimos la longitud de la ventana en 100, pero puedes intentar ajustarla: es más fácil y rápido entrenar RNNs en secuencias de entrada más cortas, pero la RNN no podrá aprender ningún patrón más largo que la longitud, así que no lo hagas demasiado pequeño.

¡Eso es todo! Preparar el conjunto de datos fue la parte más difícil. Ahora vamos a crear el modelo.


###Construcción y entrenamiento del modelo Char-RNN
Dado que nuestro conjunto de datos es razonablemente grande y modelar el lenguaje es una tarea bastante difícil, necesitamos algo más que un simple RNN con algunos neuronas recurrentes. Construyamos y entrenemos un modelo con una capa GRU compuesta de 128 unidades (puedes intentar ajustar el número de capas y unidades más tarde, si es necesario):
```python
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=n_tokens, output_dim=16),
    tf.keras.layers.GRU(128, return_sequences=True),
    tf.keras.layers.Dense(n_tokens, activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy", optimizer="nadam",
              metrics=["accuracy"])
model_ckpt = tf.keras.callbacks.ModelCheckpoint(
    "my_shakespeare_model", monitor="val_accuracy", save_best_only=True)
history = model.fit(train_set, validation_data=valid_set, epochs=10,
                    callbacks=[model_ckpt])
```
Repasemos este código:
Utilizamos una capa de Embedding como la primera capa para codificar los IDs de los caracteres (los embeddings se introdujeron en el Capítulo 13). El número de dimensiones de entrada de la capa Embedding es el número de IDs de caracteres distintos, y el número de dimensiones de salida es un hiperparámetro que puedes ajustar; lo estableceremos en 16 por ahora. Mientras que las entradas de la capa de Embedding serán tensores 2D de forma [tamaño del lote, longitud de la ventana], la salida de la capa de Embedding será un tensor 3D de forma [tamaño del lote, longitud de la ventana, tamaño del embedding].
Utilizamos una capa Dense para la capa de salida: debe tener 39 unidades (n_tokens) porque hay 39 caracteres distintos en el texto, y queremos emitir una probabilidad para cada carácter posible (en cada paso de tiempo). Las 39 probabilidades de salida deben sumar 1 en cada paso de tiempo, por lo que aplicamos la función de activación softmax a las salidas de la capa Dense.
Finalmente, compilamos este modelo, utilizando la pérdida "sparse_categorical_crossentropy" y un optimizador Nadam, y entrenamos el modelo durante varios epochs,3 utilizando un callback ModelCheckpoint para guardar el mejor modelo (en términos de precisión de validación) a medida que avanza el entrenamiento.

CONSEJO
Si estás ejecutando este código en Colab con una GPU activada, el entrenamiento debería tomar aproximadamente una a dos horas. Puedes reducir el número de epochs si no quieres esperar tanto tiempo, pero por supuesto, la precisión del modelo probablemente será menor. Si la sesión de Colab se agota, asegúrate de reconectar rápidamente, o de lo contrario el entorno de ejecución de Colab será destruido.

Este modelo no maneja el preprocesamiento de texto, así que envolvámoslo en un modelo final que contenga la capa tf.keras.layers.TextVectorization como la primera capa, más una capa tf.keras.layers.Lambda para restar 2 a los IDs de los caracteres ya que no estamos usando los tokens de relleno y desconocidos por ahora:
```python
shakespeare_model = tf.keras.Sequential([
    text_vec_layer,
    tf.keras.layers.Lambda(lambda X: X - 2), # sin tokens <PAD> o <UNK>
    model
])
```
Y ahora usémoslo para predecir el siguiente carácter en una oración:
```python
>>> y_proba = shakespeare_model.predict(["To be or not to b"])[0, -1]
>>> y_pred = tf.argmax(y_proba) # elegir el ID de carácter más probable
>>> text_vec_layer.get_vocabulary()[y_pred + 2]
'e'
```
Genial, el modelo predijo correctamente el siguiente carácter. Ahora usemos este modelo para pretender que somos Shakespeare.
