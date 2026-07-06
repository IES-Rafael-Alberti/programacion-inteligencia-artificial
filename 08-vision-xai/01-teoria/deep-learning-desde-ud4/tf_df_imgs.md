## Cargando y Preprocesando Datos con TensorFlow
En un tema anterior, viste que cargar y preprocesar datos es una parte importante de cualquier proyecto de aprendizaje automático. Utilizaste Pandas para cargar y explorar el conjunto de datos de viviendas de California (modificado), que estaba almacenado en un archivo CSV, y aplicaste los transformadores de Scikit-Learn para el preprocesamiento. Estas herramientas son bastante convenientes, y probablemente las usarás a menudo, especialmente cuando explores y experimentes con datos.

Sin embargo, al entrenar modelos de TensorFlow en grandes conjuntos de datos, podrías preferir usar la propia API de carga y preprocesamiento de datos de TensorFlow, llamada tf.data. Es capaz de cargar y preprocesar datos de manera extremadamente eficiente, leyendo de múltiples archivos en paralelo usando multihilo y encolamiento, mezclando y agrupando muestras, y más. Además, puede hacer todo esto al vuelo: carga y preprocesa el siguiente lote de datos en múltiples núcleos de CPU, mientras tus GPUs o TPUs están ocupadas entrenando el lote actual de datos.

La API tf.data te permite manejar conjuntos de datos que no caben en la memoria, y te permite hacer uso completo de tus recursos de hardware, acelerando así el entrenamiento. De fábrica, la API tf.data puede leer de archivos de texto (como archivos CSV), archivos binarios con registros de tamaño fijo, y archivos binarios que usan el formato TFRecord de TensorFlow, que admite registros de tamaños variables. TFRecord es un formato binario flexible y eficiente que generalmente contiene protocol buffers (un formato binario de código abierto). La API tf.data también tiene soporte para leer desde bases de datos SQL. Además, muchas extensiones de código abierto están disponibles para leer de todo tipo de fuentes de datos, como el servicio BigQuery de Google (ver https://tensorflow.org/io).

Keras también viene con potentes, pero fáciles de usar, capas de preprocesamiento que pueden integrarse en tus modelos: de esta manera, cuando despliegues un modelo en producción, será capaz de ingerir datos crudos directamente, sin que tengas que agregar ningún código de preprocesamiento adicional. Esto elimina el riesgo de discrepancia entre el código de preprocesamiento utilizado durante el entrenamiento y el código de preprocesamiento utilizado en producción, lo que probablemente causaría sesgo de entrenamiento/servicio. Y si despliegas tu modelo en múltiples aplicaciones codificadas en diferentes lenguajes de programación, no tendrás que reimplementar el mismo código de preprocesamiento varias veces, lo que también reduce el riesgo de discrepancia. Como verás, ambas API pueden usarse conjuntamente, por ejemplo, para beneficiarse de la carga de datos eficiente ofrecida por tf.data y la comodidad de las capas de preprocesamiento de Keras.

En este tema, primero cubriremos la API tf.data y el formato TFRecord.
Luego exploraremos las capas de preprocesamiento de Keras y cómo usarlas con la API tf.data. Por último, echaremos un vistazo rápido a algunas bibliotecas relacionadas que podrías encontrar útiles para cargar y preprocesar datos, como TensorFlow Datasets y TensorFlow Hub. ¡Así que comencemos!

### La API tf.data
La API completa de tf.data gira en torno al concepto de un tf.data.Dataset: esto representa una secuencia de elementos de datos. Usualmente usarás conjuntos de datos que leen datos del disco gradualmente, pero por simplicidad, vamos a crear un conjunto de datos a partir de un simple tensor de datos usando tf.data.Dataset.from_tensor_slices():

La API `tf.data` de TensorFlow es una herramienta poderosa y flexible diseñada para facilitar la carga, el procesamiento, la manipulación y la reutilización de conjuntos de datos en aplicaciones de aprendizaje automático. Central a esta API es el concepto de `tf.data.Dataset`, que proporciona una interfaz robusta para crear y manipular pipelines de datos complejos de una manera eficiente y escalable. Este manual proporcionará una visión general de cómo utilizar la API `tf.data` para trabajar con datos en TensorFlow.

## Conceptos Básicos

### `tf.data.Dataset`

El objeto `tf.data.Dataset` representa una secuencia de elementos, cada uno compuesto de uno o más componentes. Estos elementos pueden ser cualquier forma de datos, como un simple tensor, una tupla de tensores o incluso un diccionario de tensores. La API está diseñada para manejar grandes cantidades de datos, leer de múltiples fuentes de datos y realizar transformaciones complejas sobre los datos de manera eficiente.

### Crear un Dataset

Hay varias formas de crear un `Dataset`. Aquí se presentan los métodos más comunes:

#### Desde Tensors

Utiliza `tf.data.Dataset.from_tensors()` o `tf.data.Dataset.from_tensor_slices()` para crear un dataset directamente desde tensores. Mientras que `from_tensors()` devuelve un dataset que contiene un solo elemento, compuesto por el tensor completo, `from_tensor_slices()` crea un dataset cortando el tensor a lo largo de su primera dimensión.

```python
import tensorflow as tf

# Crear Dataset desde un tensor
tensor = tf.range(10)
dataset = tf.data.Dataset.from_tensor_slices(tensor)

for element in dataset:
    print(element.numpy())
```

#### Desde Archivos

Para leer archivos, como archivos CSV o de texto, TensorFlow ofrece funciones específicas como `tf.data.TextLineDataset` o `tf.data.FixedLengthRecordDataset` que facilitan la carga eficiente de datos.

```python
# Crear un Dataset que lea todas las líneas de un archivo de texto
filenames = ["archivo1.txt", "archivo2.txt"]
dataset = tf.data.TextLineDataset(filenames)

for line in dataset:
    print(line.numpy())
```

### Transformaciones en Datasets

`tf.data.Dataset` permite aplicar una variedad de transformaciones para preparar los datos para el entrenamiento de modelos. Algunas transformaciones comunes incluyen:

- `map()`: Aplica una función a cada elemento del dataset.
- `batch()`: Combina consecutivamente elementos del dataset en un solo elemento.
- `shuffle()`: Mezcla los elementos del dataset de manera aleatoria.
- `repeat()`: Repite el dataset el número especificado de veces.
- `filter()`: Filtra los elementos del dataset según una función de predicado.
- `prefetch()`: Prepara los elementos del dataset antes de que sean necesarios.

```python
dataset = dataset.map(lambda x: x * 2)  # Multiplica cada elemento por 2
dataset = dataset.batch(3)  # Agrupa los elementos en lotes de 3
dataset = dataset.shuffle(buffer_size=10)  # Mezcla los elementos con un buffer de tamaño 10
dataset = dataset.repeat(2)  # Repite el dataset dos veces

### Encadenando Transformaciones con `tf.data`

En TensorFlow, la API `tf.data` permite encadenar múltiples operaciones de transformación en un flujo de trabajo de preprocesamiento de datos de forma eficiente. Esta capacidad de encadenar transformaciones es crucial para la preparación de datos en proyectos de aprendizaje automático, permitiendo una manipulación de datos flexible y eficiente antes del entrenamiento de modelos.

#### Ejemplo de Encadenamiento de Transformaciones

A continuación, se muestra un ejemplo de cómo encadenar diversas transformaciones utilizando `tf.data.Dataset`. En este ejemplo, cargaremos un conjunto de datos sencillo, aplicaremos varias transformaciones, y prepararemos los datos para el entrenamiento:

```python
import tensorflow as tf

# Simular la carga de un conjunto de datos
data = tf.range(10)  # Crea un tensor de 0 a 9
dataset = tf.data.Dataset.from_tensor_slices(data)

# Encadenar transformaciones
dataset = (dataset
           .map(lambda x: x * 2)  # Multiplica cada elemento por 2
           .shuffle(buffer_size=10)  # Mezcla los elementos del dataset
           .batch(5)  # Agrupa los elementos en lotes de 5
           .repeat(2)  # Repite el dataset dos veces
           .filter(lambda x: tf.reduce_any(x > 5))  # Filtra lotes donde cualquier elemento sea mayor que 5
           .prefetch(tf.data.AUTOTUNE))  # Prepara los datos mientras el modelo está entrenando

# Visualizar el resultado de las transformaciones
for batch in dataset:
    print(batch.numpy())
```

#### Descripción de las Transformaciones

1. **`map(lambda x: x * 2)`**: Transforma cada elemento del conjunto de datos multiplicándolo por 2. Es útil para realizar operaciones elementales que necesitan ser aplicadas a cada entrada del conjunto de datos.

2. **`shuffle(buffer_size=10)`**: Mezcla los elementos del conjunto de datos utilizando un buffer de tamaño 10. Esta operación es fundamental para garantizar que los modelos de aprendizaje automático no aprendan nada del orden de los datos.

3. **`batch(5)`**: Agrupa los elementos del conjunto de datos en lotes de 5. Esto es necesario para el entrenamiento en mini-batch durante el proceso de aprendizaje de modelos, facilitando un entrenamiento más eficiente y generalmente más efectivo.

4. **`repeat(2)`**: Repite el conjunto de datos completo dos veces. Esto se usa comúnmente para aumentar el número de épocas de entrenamiento sin necesidad de recargar los datos.

5. **`filter(lambda x: tf.reduce_any(x > 5))`**: Filtra los lotes para incluir solo aquellos en los que al menos un elemento sea mayor que 5. Esta operación permite refinar el conjunto de datos eliminando datos que no cumplan ciertos criterios.

6. **`prefetch(tf.data.AUTOTUNE)`**: Prepara los datos mientras el modelo está entrenando. Esto ayuda a optimizar el rendimiento, permitiendo que el entrenamiento se ejecute más rápidamente al reducir el tiempo de espera de datos.

Este flujo de trabajo ilustra cómo las transformaciones encadenadas pueden ser implementadas para preparar eficazmente un conjunto de datos para el entrenamiento de un modelo de aprendizaje automático, maximizando el rendimiento y asegurando la calidad del proceso de aprendizaje.


### Barajando los Datos

Para garantizar que el modelo de aprendizaje automático no se ajuste a un orden específico de datos y para mejorar la generalización, es importante barajar los datos antes de alimentarlos al modelo. En TensorFlow, puedes usar el método `shuffle()` en un `tf.data.Dataset`. Este método tiene un parámetro importante llamado `buffer_size`, que determina el tamaño del buffer desde el cual los datos son muestreados aleatoriamente. Aquí hay un ejemplo de cómo aplicarlo:

```python
dataset = dataset.shuffle(buffer_size=1000)
```

El `buffer_size` debería ser lo suficientemente grande para garantizar una buena mezcla aleatoria, pero al mismo tiempo, debe tener en cuenta la memoria disponible. Un valor común es el tamaño del conjunto de datos o un número que refleje un buen equilibrio entre aleatoriedad y eficiencia de costos computacionales.

### Entrelazando Líneas de Múltiples Archivos

A menudo, los datos vienen distribuidos en múltiples archivos, y TensorFlow ofrece herramientas para leer y combinar estos archivos de manera eficiente. Puedes usar `tf.data.Dataset.list_files()` para crear un conjunto de datos de rutas de archivo y luego usar `interleave()` para entrelazar líneas de múltiples archivos. Esto puede ser útil para asegurar que el modelo reciba una mezcla diversa de datos de diferentes archivos durante el entrenamiento. Aquí está cómo se puede hacer:

```python
filenames = tf.data.Dataset.list_files("/path/to/data/*.csv")
dataset = filenames.interleave(
    lambda filename: tf.data.TextLineDataset(filename).skip(1),
    cycle_length=4,
    num_parallel_calls=tf.data.AUTOTUNE
)
```

En este ejemplo, `skip(1)` se utiliza para omitir la primera línea de cada archivo CSV, que generalmente contiene las cabeceras de las columnas. El parámetro `cycle_length` controla cuántos archivos se leen en paralelo.

### Revisemos este código:

El código que proporcionaste realiza la lectura y preprocesamiento básico de los datos CSV. Primero, define la cantidad de entradas (características) que espera por línea y los valores predeterminados para cada una, lo que es útil para manejar datos faltantes. Luego, decodifica cada línea CSV en un tensor y finalmente escala los datos utilizando la media y desviación estándar del conjunto de entrenamiento. Esto es crucial para muchos algoritmos de aprendizaje automático que asumen que todos los datos de entrada están normalizados.

### Poniendo Todo Junto

Aquí está un ejemplo de cómo combinar todo lo discutido en una función útil:

```python
def load_and_preprocess_data(file_pattern, repeat_count=1, batch_size=32):
    def preprocess_line(line):
        x, y = parse_csv_line(line)
        return (x - X_mean) / X_std, y

    filenames = tf.data.Dataset.list_files(file_pattern)
    dataset = filenames.interleave(
        lambda filename: tf.data.TextLineDataset(filename).map(preprocess_line).skip(1),
        cycle_length=4,
        num_parallel_calls=tf.data.AUTOTUNE
    )
    dataset = dataset.shuffle(buffer_size=1000).repeat(repeat_count).batch(batch_size)
    return dataset

# Uso:
dataset = load_and_preprocess_data("/path/to/data/*.csv")
```

Esta función carga los datos desde múltiples archivos CSV, aplica el preprocesamiento definido, los baraja, y los agrupa en lotes. `repeat_count` puede ser ajustado según si se desea que el conjunto de datos se repita durante el entrenamiento (útil para entrenamiento durante múltiples épocas).

## Eficiencia y Rendimiento

El rendimiento es crucial cuando se trabaja con grandes conjuntos de datos. `tf.data` ofrece varias características para mejorar el rendimiento de la carga y preprocesamiento de datos:

- **Pipelining**: Puedes usar `prefetch()` para preparar datos mientras el modelo está entrenando, mejorando así la eficiencia de la entrada de datos.
- **Paralelización**: Con `map()`, puedes utilizar el parámetro `num_parallel_calls` para transformar los datos en paralelo.

```python
dataset = dataset.map(lambda x: x * 2, num_parallel_calls=tf.data.AUTOTUNE)
dataset = dataset.prefetch(tf.data.AUTOTUNE)
```

### Prefetching

Al llamar a `prefetch(1)` al final de la función `custom csv_reader_dataset()`, estamos creando un conjunto de datos que hará todo lo posible por estar siempre un lote adelante. En otras palabras, mientras el modelo está trabajando en el entrenamiento de un lote de datos, TensorFlow estará cargando de manera asincrónica el siguiente lote de datos, lo que puede mejorar significativamente la eficiencia del entrenamiento al reducir el tiempo de espera del modelo para los datos. Aquí se muestra cómo añadir `prefetching` al final del pipeline de procesamiento de datos:

```python
dataset = dataset.prefetch(1)
```

### Usando el Conjunto de Datos con Keras

Ahora podemos usar la función `custom csv_reader_dataset()` que escribimos anteriormente para crear un conjunto de datos para el conjunto de entrenamiento, y para el conjunto de validación y el conjunto de pruebas. El conjunto de entrenamiento será barajado en cada época. Es importante notar que el conjunto de validación y el conjunto de pruebas también serán barajados, aunque realmente no necesitamos eso. Sin embargo, para el ejemplo, mantendremos la consistencia:

```python
train_dataset = csv_reader_dataset("train.csv", shuffle=True)
validation_dataset = csv_reader_dataset("valid.csv", shuffle=True)
test_dataset = csv_reader_dataset("test.csv", shuffle=True)

model = keras.models.Sequential([...])
model.compile([...])
model.fit(train_dataset, validation_data=validation_dataset, epochs=10)
```

## Ejemplos Prácticos

Para consolidar los conceptos, aquí tienes un ejemplo completo que muestra cómo cargar, transformar y utilizar un dataset para entrenar un modelo simple en TensorFlow:

```python
import tensorflow as tf

# Cargar datos
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preparar el Dataset
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(10000).batch(32).prefetch(tf.data.AUTOTUNE)

# Construir el modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Fl

atten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_dataset, epochs=5)
```

### El Formato TFRecord

El formato TFRecord es el formato preferido de TensorFlow para almacenar grandes cantidades de datos y leerlos de manera eficiente. Es un formato binario muy simple que almacena una secuencia de registros binarios. Cada registro incluye un dato en bruto, permitiendo una carga y deserialización muy rápida. Para crear un archivo TFRecord, puedes usar `tf.io.TFRecordWriter`:

```python
with tf.io.TFRecordWriter("data.tfrecords") as file_writer:
    for feature in dataset:
        example = serialize_example(feature)
        file_writer.write(example)
```

Donde `serialize_example` es una función que convierte tus datos a un formato que TensorFlow puede entender, normalmente usando `tf.train.Example`.

### Archivos TFRecord Comprimidos

A veces puede ser útil comprimir tus archivos TFRecord, especialmente si necesitan ser cargados a través de una conexión de red. Puedes especificar un tipo de compresión al crear un `TFRecordWriter`, que puede ser `GZIP` o `ZLIB`. Aquí se muestra cómo crear y leer archivos TFRecord comprimidos:

```python
options = tf.io.TFRecordOptions(compression_type="GZIP")
with tf.io.TFRecordWriter("data_compressed.tfrecord", options=options) as file_writer:
    for feature in dataset:
        example = serialize_example(feature)
        file_writer.write(example)

def read_tfrecord(filename):
    raw_dataset = tf.data.TFRecordDataset(filename, compression_type="GZIP")
    parsed_dataset = raw_dataset.map(parse_example)  # Assuming a parse_example function is defined
    return parsed_dataset
```

En este ejemplo, `serialize_example` sería una función que prepara y serializa cada ejemplo a un formato binario, mientras que `parse_example` sería la función que deserializa los datos almacenados en el formato TFRecord para su uso en TensorFlow.

### Una Breve Introducción a los Protocol Buffers
**Protocol Buffers** (protobufs) son un sistema de serialización de datos estructurados desarrollado por Google, y son ampliamente utilizados dentro de TensorFlow, especialmente en el formato de almacenamiento TFRecord. Los protobufs ofrecen un método compacto, eficiente y extensible para serializar datos estructurados, superando en muchos aspectos a otros formatos como JSON o XML en términos de velocidad y tamaño de almacenamiento.

Aunque cada registro puede usar cualquier formato binario que desees, los archivos TFRecord generalmente contienen protocol buffers serializados (también llamados protobufs). Protocol buffers son un método eficiente y flexible para serializar datos estructurados, ofreciendo ventajas en términos de eficiencia y compatibilidad hacia adelante en comparación con formatos más simples como JSON o XML.


#### Ventajas de Protocol Buffers
1. **Eficiencia**: Los protobufs son extremadamente eficientes tanto en tamaño como en velocidad de serialización y deserialización.
2. **Compatibilidad hacia adelante y hacia atrás**: Permiten que los esquemas de datos evolucionen sin romper los despliegues existentes, incluso si el código antiguo y nuevo necesita leer y escribir los mismos datos.
3. **Automatización en la compilación de código**: Puedes generar automáticamente código de datos a partir de archivos de definición `.proto`, lo que simplifica la codificación y reduce errores de runtime.

#### Instalar Protocol Buffer

Para comenzar a usar Protocol Buffers, primero necesitas instalar el compilador `protoc`, que se utiliza para compilar archivos de definición `.proto` a clases de datos en varios lenguajes de programación.

**Instalación en sistemas basados en Unix (Linux, macOS):**
```bash
sudo apt-get install protobuf-compiler
# o en macOS
brew install protobuf
```

**Instalación en Windows:**
- Descarga un release precompilado desde la página de [releases de GitHub de Protocol Buffers](https://github.com/protocolbuffers/protobuf/releases).
- Extrae el archivo y añade la ruta del binario `protoc` al PATH de tu sistema.

#### Compilar archivos `.proto`

Una vez que tengas el compilador instalado, puedes definir tus propios tipos de mensajes en un archivo `.proto`. Aquí hay un ejemplo simple de cómo se podría ver un archivo `.proto`:

```proto
syntax = "proto3";

message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
```

Para compilar este archivo a código Python, ejecuta:

```bash
protoc --python_out=./path/to/output/folder ./path/to/proto/file/person.proto
```

Esto generará un archivo `person_pb2.py` que puedes importar en tus proyectos Python.

#### Usar con TensorFlow

Dentro de TensorFlow, especialmente cuando se trabaja con TFRecord, los Protocol Buffers se utilizan para definir la estructura de los datos que se están almacenando. Un ejemplo común es el formato de ejemplo de TensorFlow (`tf.train.Example`), que se utiliza para almacenar datos de forma que TensorFlow pueda entender y procesar eficientemente.

Aquí está un ejemplo de cómo crear un `tf.train.Example` a partir de datos:

```python
import tensorflow as tf

# Supongamos que tenemos la siguiente data:
name = "John Doe"
id = 1234
email = "johndoe@example.com"

# Crear un objeto tf.train.Example
example = tf.train.Example(features=tf.train.Features(feature={
    "name": tf.train.Feature(bytes_list=tf.train.BytesList(value=[name.encode('utf-8')])),
    "id": tf.train.Feature(int64_list=tf.train.Int64List(value=[id])),
    "email": tf.train.Feature(bytes_list=tf.train.BytesList(value=[email.encode('utf-8')]))
}))

# Serializar a string
serialized_example = example.SerializeToString()

# Guardar en un archivo TFRecord o enviar a un API que acepte protobufs
with tf.io.TFRecordWriter("output.tfrecords") as writer:
    writer.write(serialized_example)
```

Este código muestra cómo encapsular datos en un formato `tf.train.Example`, que es esencial para trabajar eficientemente con grandes volúmenes de datos en TensorFlow, particularmente cuando los datos se escalan a operaciones de producción o se procesan en sistemas de aprendizaje distribuido.


### Otro ejemplo Protobufs de TensorFlow

El protobuf principal típicamente utilizado en un archivo TFRecord es el protobuf `Example`, que representa una instancia en un conjunto de datos. Contiene una lista de características nombradas, donde cada característica puede ser una lista de cadenas de bytes, una lista de flotantes, o una lista de enteros. Aquí está la definición del protobuf (del código fuente de TensorFlow):

```protobuf
message Example {
  Features features = 1;
}

message Features {
  map<string, Feature> feature = 1;
}

message Feature {
  oneof kind {
    BytesList bytes_list = 1;
    FloatList float_list = 2;
    Int64List int64_list = 3;
  }
}
```

Este diseño permite almacenar y recuperar estructuras de datos complejas de una manera estandarizada y eficiente.

### Cargando y Analizando Ejemplos

Para cargar los `Example` protobufs serializados, usaremos un `tf.data.TFRecordDataset` una vez más, y analizaremos cada `Example` usando `tf.io.parse_single_example()`. Requiere al menos dos argumentos: un tensor escalar de cadena que contiene los datos serializados, y una descripción de cada característica. La descripción es un diccionario que mapea cada nombre de característica a un descriptor `tf.io.FixedLenFeature` indicando la forma, tipo y valor predeterminado de la característica, o un descriptor `tf.io.VarLenFeature` indicando solo el tipo si la longitud de la lista de la característica puede variar (como para la característica "emails"). El siguiente código define un diccionario de descripción, luego crea un `TFRecordDataset` y aplica una función de preprocesamiento personalizada para analizar cada protobuf `Example` serializado que este conjunto de datos contiene:

```python
feature_description = {
    'id': tf.io.FixedLenFeature([], tf.int64),
    'name': tf.io.FixedLenFeature([], tf.string),
    'emails': tf.io.VarLenFeature(tf.string)
}

def parse_example(example_proto):
    return tf.io.parse_single_example(example_proto, feature_description)

dataset = tf.data.TFRecordDataset("your_dataset.tfrecord")
parsed_dataset = dataset.map(parse_example)
```

### Manejando Listas de Listas Usando el Protobuf `SequenceExample`

Aquí está la definición del protobuf `SequenceExample`:

```protobuf
message SequenceExample {
  FeatureList context = 1;
  FeatureLists feature_lists = 2;
}

message FeatureList {
  repeated Feature feature = 1;
}

message FeatureLists {
  map<string, FeatureList> feature_list = 1;
}
```

`SequenceExample` es útil cuando se manejan secuencias de datos o cualquier estructura que involucre listas de listas, como puede ser común en aplicaciones de procesamiento del lenguaje natural o series temporales. Cada `FeatureList` puede contener varias `Feature`, lo que permite modelar una matriz de tiempo o secuencias de elementos con múltiples características en cada paso de tiempo.

## Capas de Preprocesamiento de Keras
Preparar tus datos para una red neuronal típicamente requiere normalizar las características numéricas, codificar las características categóricas y el texto, recortar y redimensionar imágenes, y más. Hay varias opciones para esto:

- El preprocesamiento puede hacerse con antelación al preparar tus archivos de datos de entrenamiento, usando cualquier herramienta que te guste, como NumPy, Pandas, o Scikit-Learn. Necesitarás aplicar exactamente los mismos pasos de preprocesamiento en producción, para asegurar que tu modelo de producción reciba entradas preprocesadas similares a las que se entrenó.

- Alternativamente, puedes preprocesar tus datos al vuelo mientras los cargas con tf.data, aplicando una función de preprocesamiento a cada elemento de un conjunto de datos usando el método map() de ese conjunto de datos, como hicimos anteriormente en este capítulo. Nuevamente, necesitarás aplicar los

 mismos pasos de preprocesamiento en producción.

- Un último enfoque es incluir capas de preprocesamiento directamente dentro de tu modelo para que pueda preprocesar todos los datos de entrada al vuelo durante el entrenamiento, luego usar las mismas capas de preprocesamiento en producción. El resto de este capítulo verá este último enfoque.

Keras ofrece muchas capas de preprocesamiento que puedes incluir en tus modelos: se pueden aplicar a características numéricas, características categóricas, imágenes y texto. Revisaremos las características numéricas y categóricas en las siguientes secciones, así como el preprocesamiento básico de texto, y cubriremos el preprocesamiento de imágenes

### La Capa de Normalización

Keras proporciona una capa de `Normalization` que podemos usar para estandarizar las características de entrada, es decir, ajustar los datos para que tengan una media de 0 y una desviación estándar de 1. Esta capa calculará la media y la desviación estándar de los datos durante el ajuste y las utilizará para escalar los datos durante el entrenamiento y las predicciones. Aquí te muestro cómo usarla:

```python
from tensorflow.keras.layers import Normalization
from tensorflow.keras.models import Sequential

normalizer = Normalization(axis=-1)  # Normaliza las características a lo largo del último eje

# Suponiendo X_train como tus datos de entrenamiento
normalizer.adapt(X_train)  # Calcula la media y la desviación estándar

model = Sequential([
    normalizer,
    # ... otras capas de tu modelo ...
])
```

### La Capa de Discretización

El objetivo de la capa de `Discretization` es transformar una característica numérica en una característica categórica mapeando rangos de valores (llamados bins) a categorías. Aquí se muestra cómo usarla:

```python
from tensorflow.keras.layers import Discretization

age_bins = [0, 18, 50, float('inf')]  # Define los bins
discretizer = Discretization(bins=age_bins)

# Usando el discretizer en un modelo
model = Sequential([
    discretizer,
    # ... otras capas de tu modelo ...
])
```

### La Capa de CategoryEncoding

Para realizar codificación one-hot, Keras ofrece la capa `CategoryEncoding`. Aquí se muestra cómo aplicarlo a una característica categórica como la edad discretizada:

```python
from tensorflow.keras.layers import CategoryEncoding

# Suponiendo que 'num_tokens' es el número de categorías distintas
encoder = CategoryEncoding(num_tokens=4, output_mode='one_hot')

# Incorporándolo en un modelo
model = Sequential([
    discretizer,
    encoder,
    # ... otras capas de tu modelo ...
])
```

### La Capa StringLookup

La capa `StringLookup` se puede usar para convertir strings en índices enteros, que son más amigables para los modelos de machine learning. También se puede usar para codificar one-hot automáticamente las características categóricas de strings:

```python
from tensorflow.keras.layers import StringLookup

city_lookup = StringLookup(output_mode='one_hot')

# Suponiendo que cities es un tensor o arreglo de nombres de ciudades
city_lookup.adapt(cities)  # Ajusta el lookup a los datos únicos

model = Sequential([
    city_lookup,
    # ... otras capas de tu modelo ...
])
```

### La Capa Hashing

La capa `Hashing` es útil cuando tienes un número grande o desconocido de categorías y deseas reducir la dimensión del espacio de características. Aquí se muestra cómo usarla:

```python
from tensorflow.keras.layers import Hashing

hash_layer = Hashing(num_bins=100)  # Usando 100 bins

# Incorporándolo en un modelo
model = Sequential([
    hash_layer,
    # ... otras capas de tu modelo ...
])
```

Cada una de estas capas tiene un propósito específico en el procesamiento de datos y puede ser integrada directamente en modelos de Keras, simplificando el flujo de trabajo y asegurando que el preprocesamiento aplicado durante el entrenamiento sea exactamente el mismo que se utiliza durante la inferencia en producción.

#### Ejemplo de uso de las capas de tratamiento de datos.
Imaginemos un pequeño proyecto de ejemplo donde predecimos si un cliente suscribirá un depósito a plazo en un banco, basado en sus datos demográficos y transaccionales. Utilizaremos TensorFlow y Keras para construir un modelo de red neuronal que integre las capas de preprocesamiento directamente en el modelo.

### Datos

Los datos ficticios contienen las siguientes características:
- `age`: Edad del cliente (numérico).
- `salary`: Salario anual (numérico).
- `city`: Ciudad de residencia (categórico).
- `products`: Número de productos bancarios utilizados por el cliente (categórico, valores posibles: 1, 2, 3+).
- `subscribed`: Si el cliente se suscribió a un depósito a plazo (1: sí, 0: no) (objetivo).

### Preparación de los Datos

Para simplificar, generaremos datos sintéticos usando NumPy y pandas:

```python
import numpy as np
import pandas as pd

# Generar datos sintéticos
np.random.seed(42)
data_size = 1000
data = pd.DataFrame({
    'age': np.random.randint(18, 70, size=data_size),
    'salary': np.random.randint(30000, 100000, size=data_size),
    'city': np.random.choice(['New York', 'San Francisco', 'Austin'], size=data_size),
    'products': np.random.choice(['1', '2', '3+'], size=data_size),
    'subscribed': np.random.choice([0, 1], size=data_size)
})
```

### Modelo con Capas de Preprocesamiento

A continuación, integraremos las capas de preprocesamiento en un modelo Keras. Usaremos `Normalization` para las características numéricas, `StringLookup` y `CategoryEncoding` para las categóricas:

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Normalization, StringLookup, CategoryEncoding, Dense

# Separar datos
train_dataset = data.sample(frac=0.8, random_state=42)
test_dataset = data.drop(train_dataset.index)

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('subscribed')
test_labels = test_features.pop('subscribed')

# Capas de preprocesamiento
normalizer = Normalization(axis=-1)
normalizer.adapt(train_features[['age', 'salary']])

city_lookup = StringLookup()
city_lookup.adapt(train_features['city'])

city_encoder = CategoryEncoding(output_mode='one_hot', num_tokens=city_lookup.vocabulary_size())

product_lookup = StringLookup()
product_lookup.adapt(train_features['products'])

product_encoder = CategoryEncoding(output_mode='one_hot', num_tokens=product_lookup.vocabulary_size())

# Modelo
model = Sequential([
    normalizer,
    city_lookup,
    city_encoder,
    product_lookup,
    product_encoder,
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento
model.fit(x=train_features, y=train_labels, epochs=10, validation_split=0.2)

# Evaluación
model.evaluate(test_features, test_labels)
```

Este ejemplo crea un flujo de trabajo de machine learning donde las transformaciones de datos están integradas en el modelo, lo que garantiza que las mismas transformaciones aplicadas durante el entrenamiento se apliquen durante la inferencia. Además, facilita el despliegue y mantenimiento del modelo en producción.




### Codificando Características Categóricas Usando Incrustaciones (embeddings)
Una incrustación es una representación densa de algunos datos de mayor dimensión, como una categoría, o una palabra en un vocabulario. Si hay 50,000 categorías posibles, entonces la codificación one-hot produciría un vector disperso de 50,000 dimensiones (es decir, que contiene principalmente ceros). En contraste, una incrustación sería un vector denso comparativamente pequeño; por ejemplo, con solo 100 dimensiones.

En el aprendizaje profundo, las incrustaciones generalmente se inicializan aleatoriamente, y luego se entrenan por descenso de gradiente, junto con los otros parámetros del modelo. Por ejemplo, la categoría "NEAR BAY" en el conjunto de datos de viviendas de California podría representarse inicialmente por un vector aleatorio como [0.131, 0.890], mientras que la categoría "NEAR OCEAN" podría estar representada por otro vector aleatorio como [0.631, 0.791]. En este ejemplo, usamos incrustaciones 2D, pero el número de dimensiones es un hiperparámetro que puedes ajustar.

Dado que estas incrustaciones son entrenables, mejorarán gradualmente durante el entrenamiento; y como representan categorías bastante similares en este caso, el descenso de gradiente ciertamente terminará acercándolas, mientras tenderá a alejarlas de la incrustación de la categoría "INLAND" (ver Figura 13-6). De hecho, cuanto mejor sea la representación, más fácil será para la red neuronal hacer predicciones precisas, por lo que el entrenamiento tiende a hacer que las incrustaciones sean representaciones útiles de las categorías. Esto se llama aprendizaje de representación (verás otros tipos de aprendizaje de representación en el Capítulo 17).

Keras proporciona una capa de incrustación, que envuelve una matriz de incrustación: esta matriz tiene una fila por categoría y una columna por dimensión de incrustación. Por defecto, se inicializa aleatoriamente. Para convertir un ID de categoría en una incrustación, la capa de incrustación simplemente busca y devuelve la fila que corresponde a esa categoría. ¡Eso es todo! Por ejemplo, inicialicemos una capa de incrustación con cinco filas y incrustaciones 2D, y úsala para codificar algunas categorías:
Para ejemplificar el uso de una capa de incrustación (`Embedding`) en Keras y demostrar cómo se puede inicializar y utilizar para convertir IDs de categorías en incrustaciones densas, a continuación se detalla un pequeño ejemplo. Este ejemplo creará una capa de incrustación que puede manejar cinco categorías distintas, cada una representada como un vector en un espacio de dos dimensiones.

### Preparación del código

Primero, vamos a definir las categorías y luego usar la capa `Embedding` para mapear estos IDs a vectores 2D.

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import Sequential

# Definición de la capa de incrustación
# Supongamos que tenemos 5 categorías distintas, y queremos una incrustación de 2 dimensiones para cada una.
embedding_layer = Embedding(input_dim=5,  # Número de categorías
                            output_dim=2,  # Número de dimensiones de cada incrustación
                            input_length=1)  # Longitud de entrada, 1 porque cada entrada es un solo ID de categoría

# Modelo simple para demostrar la incrustación
model = Sequential([
    embedding_layer
])

# Compilar modelo (no es necesario en este caso ya que no vamos a entrenar, pero lo incluimos para completitud)
model.compile(optimizer='adam', loss='mean_squared_error')

# IDs de categoría como ejemplo
category_ids = np.array([0, 1, 2, 3, 4])

# Usar la capa de incrustación para obtener vectores
category_embeddings = model.predict(category_ids)

# Mostrar los vectores de incrustación para cada ID de categoría
print("Embeddings for each category ID:")
for i, embedding in enumerate(category_embeddings):
    print(f"Category ID {category_ids[i]}: {embedding}")
```

### Explicación del código

1. **Capa de Incrustación (`Embedding`)**: Se inicializa con cinco categorías (`input_dim=5`) y cada categoría se representa en un espacio de dos dimensiones (`output_dim=2`).

2. **Modelo de Keras (`Sequential`)**: Se añade la capa de incrustación al modelo. Aunque este modelo es extremadamente simple y solo contiene una capa de incrustación, sirve para demostrar cómo se puede utilizar esta capa.

3. **Predicción de Incrustaciones**: Pasamos un array de IDs de categorías al modelo para obtener sus respectivas incrustaciones. El modelo retorna los vectores de incrustación para cada ID.

Este código es útil en escenarios donde necesitas representar categorías como vectores densos, comúnmente en sistemas de recomendación, procesamiento de lenguaje natural, y otros tipos de modelos de aprendizaje profundo que necesitan entender y procesar relaciones complejas entre categorías.



Poniendo todo junto, ahora podemos crear un modelo de Keras que pueda procesar una característica de texto categórico junto con características numéricas regulares y aprender una incrustación para cada categoría (así como para cada cubo OOV):

Para completar y añadir código a la sección sobre el uso de incrustaciones para codificar características categóricas, vamos a desarrollar un pequeño ejemplo usando Keras. Crearemos un modelo que combine características numéricas y categóricas, usando incrustaciones para estas últimas, y entrenaremos este modelo para predecir un objetivo ficticio.

### Creación de Datos Sintéticos

Primero, generemos algunos datos sintéticos que incluyan tanto características numéricas como categóricas:

```python
import numpy as np
import pandas as pd
from tensorflow.keras.utils import to_categorical

# Generar datos sintéticos
np.random.seed(42)
data_size = 1000

# Simulación de datos categóricos y numéricos
data = pd.DataFrame({
    'category': np.random.choice(['NEAR BAY', 'NEAR OCEAN', 'INLAND', 'RURAL'], data_size),
    'income': np.random.rand(data_size) * 100,
    'age': np.random.randint(18, 70, data_size),
    'subscribed': np.random.choice([0, 1], data_size)
})
```

### Preparación de Datos

Antes de alimentar los datos al modelo, necesitamos preparar las características categóricas:

```python
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import StringLookup, Embedding

# Convertir categorías a índices
category_lookup = StringLookup(output_mode='int')
category_lookup.adapt(data['category'])

# Dividir datos
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
train_labels = train_data.pop('subscribed')
test_labels = test_data.pop('subscribed')
```

### Modelo de Keras con Incrustaciones

Ahora, construyamos un modelo que incluya una capa de incrustación para las categorías:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Concatenate, Input, Embedding, Flatten
from tensorflow.keras import Model

# Parámetros de la incrustación
num_categories = category_lookup.vocabulary_size()
embedding_dim = 2  # Número de dimensiones de la incrustación

# Capa de incrustación
category_embedding = Embedding(input_dim=num_categories, output_dim=embedding_dim, input_length=1, name='category_embedding')

# Modelo
input_category = Input(shape=(1,), dtype='int32', name='input_category')
input_numeric = Input(shape=(2,), name='input_numeric')

# Incrustación y aplanado
category_vector = category_embedding(input_category)
category_vector = Flatten()(category_vector)

# Concatenar entradas
concatenated = Concatenate()([category_vector, input_numeric])

# Capas densas
output = Dense(128, activation='relu')(concatenated)
output = Dense(1, activation='sigmoid')(output)

# Construir y compilar el modelo
model = Model(inputs=[input_category, input_numeric], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Preparar datos para el modelo
train_features = [category_lookup(train_data['category']), train_data[['income', 'age']]]
test_features = [category_lookup(test_data['category']), test_data[['income', 'age']]]

# Entrenar el modelo
model.fit(train_features, train_labels, epochs=10, batch_size=32, validation_split=0.2)

# Evaluación del modelo
model.evaluate(test_features, test_labels)
```

Este código crea un modelo que combina datos numéricos y una característica categórica utilizando una capa de incrustación. La categoría es convertida a un índice, y luego se busca en una matriz de incrustaciones para obtener una representación densa, que luego es concatenada con las características numéricas para hacer predicciones. Este modelo proporciona una manera eficiente de manejar características categóricas con muchas categorías posibles, aprendiendo representaciones útiles durante el entrenamiento del modelo.


##### ASIDE: INCRUSTACIONES DE PALABRAS

No solo las incrustaciones generalmente serán representaciones útiles para la tarea en cuestión, sino que a menudo estas mismas incrustaciones pueden reutilizarse con éxito para otras tareas. El ejemplo más común de esto son las incrustaciones de palabras (es decir, incrustaciones de palabras individuales): cuando estás trabajando en una tarea de procesamiento de lenguaje natural, a menudo es mejor reutilizar incrustaciones de palabras preentrenadas que entrenar las tuyas propias.

La idea de usar vectores para representar palabras se remonta a la década de 1960, y se han utilizado muchas técnicas sofisticadas para generar vectores útiles, incluido el uso de redes neuronales. Pero las cosas realmente despegaron en 2013, cuando Tomáš Mikolov y otros investigadores de Google publicaron un artículo describiendo una técnica eficiente para aprender incrustaciones de palabras usando redes neuronales, superando significativamente los intentos anteriores. Esto les permitió aprender incrustaciones en un corpus de texto muy grande: entrenaron una red neuronal para predecir las palabras cercanas a cualquier palabra dada y obtuvieron incrustaciones de palabras asombrosas. Por ejemplo, los sinónimos tenían incrustaciones muy cercanas, y palabras semánticamente relacionadas como Francia, España e Italia terminaron agrupadas.

No se trata solo de proximidad, sin embargo: las incrustaciones de palabras también se organizaron a lo largo de ejes significativos en el espacio de incrustación. Aquí hay un ejemplo famoso: si calculas "Rey - Hombre + Mujer" (sumando y restando los vectores de incrustación de estas palabras), entonces el resultado estará muy cerca de la incrustación de la palabra "Reina". En otras palabras, ¡las incrustaciones de palabras codifican el concepto de género!

De manera similar, puedes calcular "Madrid - España + Francia", y el resultado está cerca de "París", lo que parece mostrar que la noción de ciudad capital también estaba codificada en las incrustaciones.

Desafortunadamente, las incrustaciones de palabras a veces capturan nuestros peores sesgos. Por ejemplo, aunque aprenden correctamente que "Hombre es a Rey como Mujer es a Reina", también parecen aprender que "Hombre es a Doctor como Mujer es a Enfermera": ¡un sesgo bastante sexista! Para ser justos, este ejemplo particular probablemente esté exagerado, como se señaló en un artículo de 2019 por Malvina Nissim et al. Sin embargo, asegurar la equidad en los algoritmos de aprendizaje profundo es un tema importante y activo de investigación. Al abordar estos desafíos, los investigadores continúan desarrollando técnicas para des-sesgar las incrustaciones o para crear nuevas que reflejen principios más equitativos.

### Preprocesamiento de Texto

Keras proporciona una capa de `TextVectorization` para el preprocesamiento básico de texto. Esta capa puede normalizar, dividir y mapear strings a enteros, lo cual es útil para preparar texto para ser procesado por un modelo de aprendizaje automático, como una red neuronal. Puedes especificar cómo se tokeniza el texto (por ejemplo, por espacios en blanco o usando un tokenizador personalizado), cómo se normaliza (por ejemplo, convirtiendo a minúsculas), y finalmente cómo se convierte texto en secuencias de enteros o vectores de bag-of-words. Si no proporcionas un vocabulario, la capa puede aprenderlo automáticamente de los datos de entrenamiento usando el método `adapt()`.

Aquí te muestro un ejemplo de cómo utilizar la capa `TextVectorization` para preparar datos de texto para un modelo:

```python
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense

# Ejemplo de datos de texto
samples = ["The cat sat on the mat.", "The dog sat on the log.", "Dogs and cats living together."]

# Crear la capa de TextVectorization
# Establecemos max_tokens como 50 (tamaño del vocabulario) y output_sequence_length como 8
vectorize_layer = TextVectorization(
    max_tokens=50,
    output_mode='int',
    output_sequence_length=8)

# Aprender el vocabulario del texto de muestra
vectorize_layer.adapt(samples)

# Crear un modelo simple para demostración
model = Sequential([
    vectorize_layer,
    Embedding(50, 7, input_length=8),  # Suponemos 50 tokens y una dimensión de incrustación de 7
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')  # Supongamos una salida binaria
])

# Compilando el modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Preparando etiquetas ficticias para demostración
labels = [1, 0, 1]  # Etiquetas binarias para el ejemplo

# Entrenar el modelo
model.fit(samples, labels, epochs=10)

# Ahora el modelo está listo para procesar texto usando el preprocesamiento aprendido y el modelo de aprendizaje profundo
```

### Descripción del Código

1. **Definición de `TextVectorization`:** Se crea la capa especificando un máximo de 50 tokens y una longitud de secuencia de salida de 8. Esto significa que cada muestra de texto se convertirá en una secuencia de hasta 8 enteros, cada uno representando un token.

2. **Aprendizaje del Vocabulario:** Utilizamos el método `adapt()` para hacer que la capa aprenda el vocabulario del conjunto de datos dado, que en este caso son tres frases de ejemplo.

3. **Construcción del Modelo:** El modelo se compone de la capa de vectorización seguida por una capa de incrustación (Embedding) y capas densas. La capa de incrustación convierte los enteros en vectores densos de tamaño 7.

4. **Compilación y Entrenamiento:** El modelo se compila con una función de pérdida de entropía cruzada binaria, lo que es común para problemas de clasificación binaria, y se entrena con los datos de ejemplo y etiquetas asociadas.

Este ejemplo ilustra cómo integrar directamente el preprocesamiento de texto dentro de un modelo de Keras, lo que facilita la aplicación de transformaciones de texto consistentes durante el entrenamiento y la inferencia.

### Usando Componentes de Modelos de Lenguaje Preentrenados

La biblioteca TensorFlow Hub es una plataforma para compartir modelos preentrenados, y es especialmente útil para integrar componentes avanzados de procesamiento de lenguaje, visión por computadora, y más, en tus proyectos. Estos componentes se llaman módulos y vienen completos con código de preprocesamiento y pesos entrenados, lo que facilita su integración en tus propios modelos. A menudo, no necesitan entrenamiento adicional, aunque tu modelo puede requerir ajustes o entrenamiento adicional en otras partes.

Veamos cómo puedes usar un módulo preentrenado de lenguaje de TensorFlow Hub, específicamente el `nnlm-en-dim50` versión 2. Este módulo toma texto crudo y produce incrustaciones de oraciones de 50 dimensiones.

#### Paso a Paso: Cargando e Integrando un Módulo de TensorFlow Hub

```python
import tensorflow as tf
import tensorflow_hub as hub

# Cargar el modelo preentrenado de TF Hub
hub_layer = hub.KerasLayer("https://tfhub.dev/google/nnlm-en-dim50/2", input_shape=[], dtype=tf.string, trainable=True)

# Construcción del modelo usando el módulo de TensorFlow Hub
model = tf.keras.Sequential([
    hub_layer,
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilación del modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Datos de ejemplo
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "I am a sentence for which I would like to get its embedding."
]

# Usar el módulo para obtener incrustaciones
embeddings = hub_layer(sentences)

print("Embeddings:", embeddings)

# Supongamos etiquetas de ejemplo para demostración
labels = [1, 0]

# Entrenar el modelo con los datos de ejemplo
model.fit(sentences, labels, epochs=10)
```

#### Descripción del Código:

1. **Cargar el Módulo de TensorFlow Hub:** Importamos `tensorflow_hub` y cargamos `nnlm-en-dim50/2`, que es una red preentrenada capaz de convertir texto en incrustaciones de 50 dimensiones. `hub.KerasLayer` facilita integrar este módulo directamente en un modelo secuencial de Keras.

2. **Construcción del Modelo:** El modelo consiste en la capa del módulo de TensorFlow Hub seguida de dos capas densas, donde la última capa tiene una activación de sigmoid, adecuada para una clasificación binaria.

3. **Compilación y Entrenamiento del Modelo:** Compilamos el modelo con optimizador Adam y función de pérdida `binary_crossentropy`. Después entrenamos el modelo con algunas oraciones de ejemplo, lo que demuestra cómo se puede utilizar el módulo para transformar texto en vectores que luego pueden ser usados para entrenar una red neuronal.

Este ejemplo muestra cómo integrar fácilmente componentes preentrenados en tus modelos, permitiendo aprovechar modelos complejos y bien entrenados sin tener que empezar desde cero.

### Capas de Preprocesamiento de Imágenes

Las capas de preprocesamiento de imágenes de Keras simplifican la tarea de preparar imágenes para modelos de aprendizaje profundo. A continuación, se describen tres capas útiles que cubren la mayoría de las necesidades básicas en el preprocesamiento de imágenes:

1. **tf.keras.layers.Resizing**: Esta capa cambia el tamaño de las imágenes de entrada al tamaño deseado. Si el cambio de tamaño resulta en una distorsión de la relación de aspecto original de la imagen y esto es un problema, puedes usar el argumento `crop_to_aspect_ratio=True` para recortar la imagen y mantener su relación de aspecto original, ajustándola al tamaño deseado sin distorsión.

```python
from tensorflow.keras.layers import Resizing

# Cambiar el tamaño de la imagen a 100x200
resize_layer = Resizing(height=100, width=200)

# Cambiar el tamaño con el recorte para mantener la relación de aspecto
resize_layer_aspect_ratio = Resizing(height=100, width=200, crop_to_aspect_ratio=True)
```

2. **tf.keras.layers.Rescaling**: Esta capa reescala los valores de los píxeles de la imagen. Es común en modelos de imágenes que los valores de los píxeles se normalicen de alguna manera, y esta capa facilita ese proceso. Por ejemplo, puedes escalar los valores de píxel de 0-255 a -1 a 1 o a 0 a 1, dependiendo de las necesidades de tu modelo.

```python
from tensorflow.keras.layers import Rescaling

# Reescalar los valores de los píxeles de 0-255 a -1 a 1
rescaling_layer = Rescaling(scale=2/255, offset=-1)

# Reescalar los valores de los píxeles de 0-255 a 0 a 1
rescaling_layer_to_one = Rescaling(scale=1/255)
```

3. **tf.keras.layers.CenterCrop**: Esta capa recorta las imágenes para mantener solo un parche central del tamaño deseado. Es especialmente útil cuando deseas asegurarte de que el modelo se enfoque en la parte más central de una imagen, o cuando quieres eliminar bordes que podrían contener ruido o información irrelevante.

```python
from tensorflow.keras.layers import CenterCrop

# Recortar al centro con dimensiones deseadas
center_crop_layer = CenterCrop(height=100, width=100)
```

### Ejemplo de Uso en un Modelo

Aquí se muestra cómo integrar estas capas en un modelo de Keras, formando una secuencia de preprocesamiento seguida por una red convolucional simple:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense

# Construir un modelo secuencial
model = Sequential([
    # Preprocesamiento
    Resizing(height=180, width=180, crop_to_aspect_ratio=True),
    Rescaling(scale=1./255),
    CenterCrop(height=150, width=150),

    # Capas convolucionales
    Conv2D(32, 3, activation='relu'),
    Conv2D(64, 3, activation='relu'),
    Flatten(),

    # Capa densa para clasificación
    Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

En este ejemplo, las imágenes son primero redimensionadas, reescaladas y recortadas, antes de ser procesadas por las capas convolucionales y finalmente clasificadas. Esto asegura que las imágenes estén en el formato correcto y optimizadas para el entrenamiento del modelo.

## El Proyecto TensorFlow Datasets

El proyecto TensorFlow Datasets (TFDS) es una herramienta increíblemente útil para los desarrolladores y científicos de datos que trabajan en el campo del aprendizaje automático y la inteligencia artificial. Proporciona una forma sencilla y uniforme de cargar una variedad de conjuntos de datos estandarizados, lo que facilita tanto la experimentación como el desarrollo de modelos robustos. Estos conjuntos de datos varían en tamaño y tipo, abarcando desde conjuntos de datos pequeños como MNIST o Fashion MNIST hasta enormes colecciones de datos como ImageNet, que requieren una cantidad considerable de espacio en disco.

### Tipos de Conjuntos de Datos Disponibles

TFDS ofrece conjuntos de datos en varias categorías, incluyendo:

- **Imágenes**: Perfecto para tareas de visión computarizada, como reconocimiento de objetos y clasificación de imágenes.
- **Texto**: Incluye conjuntos de datos para tareas de procesamiento de lenguaje natural, como traducción automática y análisis de sentimientos.
- **Audio y Video**: Para proyectos que involucran procesamiento y análisis de multimedia.
- **Series Temporales**: Utilizados en análisis predictivo y en la monitorización de datos a lo largo del tiempo.

### Exploración de Conjuntos de Datos

Para explorar la lista completa de conjuntos de datos disponibles y obtener una descripción detallada de cada uno, puedes visitar el enlace [TensorFlow Datasets](https://homl.info/tfds). Además, la herramienta "Know Your Data" permite a los usuarios explorar y entender mejor las características y la composición de los conjuntos de datos proporcionados por TFDS, lo que es esencial para aplicar técnicas de aprendizaje automático adecuadas y efectivas.

### Ejemplo de Uso de TFDS

A continuación, se muestra un ejemplo de cómo cargar y preparar un conjunto de datos usando TensorFlow Datasets:

```python
import tensorflow_datasets as tfds

# Cargar el conjunto de datos MNIST
ds, ds_info = tfds.load('mnist', with_info=True, as_supervised=True)

# Obtener el conjunto de entrenamiento y prueba
train_ds, test_ds = ds['train'], ds['test']

# Preparación simple de los datos
def preprocess(image, label):
    image = tf.cast(image, tf.float32) / 255.0  # Normalizar las imágenes a valores de 0-1
    return image, label

# Aplicar la función de preprocesamiento
train_ds = train_ds.map(preprocess).batch(32).shuffle(1024)
test_ds = test_ds.map(preprocess).batch(32)

# Usar los datos para entrenamiento o evaluación
# model.fit(train_ds, epochs=10)
# model.evaluate(test_ds)
```

Este ejemplo carga el conjunto de datos MNIST, lo divide en conjuntos de entrenamiento y prueba, aplica una función de preprocesamiento para normalizar las imágenes, y finalmente lo prepara para entrenamiento o evaluación en un modelo de TensorFlow. TFDS hace que este proceso sea intuitivo y directo, reduciendo el código necesario para cargar y preparar datos estándar, lo que permite a los usuarios concentrarse más en la construcción y optimización de sus modelos.
