---
title: "001-Keras-NLP"
author: "José Manuel Sánchez Álvarez"
date: "2025-02-26"
output: pdf_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```
# Procesamiento de Lenguaje Natural (NLP) con Keras y TensorFlow

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **Keras y TensorFlow**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **12 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**
2. **Preparación de los Datos de Texto**
3. **Construcción de un Modelo de NLP con RNN**
4. **Mejorando con LSTM y GRU**
5. **Uso de Word Embeddings en Keras**
6. **Implementación de un Transformer desde Cero**
7. **Entrenamiento del Modelo en un Dataset Realista**
8. **Predicción y Evaluación del Modelo**
9. **Optimización y Fine-Tuning con Modelos Preentrenados**
10. **Mini Despliegue de un Modelo de NLP con Flask y TensorFlow**
11. **Transferencia de Conocimiento entre Modelos**
12. **Retrieval-Augmented Generation (RAG)**

---

## ✅ **Paso 1: Fundamentos del NLP y Deep Learning**

El **Procesamiento de Lenguaje Natural (NLP)** es un campo de la inteligencia artificial que permite a las máquinas comprender, interpretar y generar texto en lenguaje humano. Se usa en aplicaciones como:

- **Traducción automática** (Google Translate, DeepL)
- **Análisis de sentimiento** (clasificación de opiniones)
- **Chatbots y asistentes virtuales** (ChatGPT, Siri, Alexa)
- **Resumen de textos**
- **Corrección gramatical**

El NLP tradicionalmente se basaba en reglas escritas a mano y modelos estadísticos, pero hoy en día se apoya en el **Deep Learning**, permitiendo un mejor rendimiento gracias a modelos como **LSTM, GRU, Transformers (BERT, GPT, etc.)**.

---

## ✅ **Paso 2: Preparación de los Datos de Texto**

Antes de entrenar modelos NLP, es fundamental preparar los datos correctamente. Usaremos **Keras y TensorFlow** para procesar textos.

```python
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Datos de ejemplo
texts = ["El NLP es fascinante", "Me encanta aprender IA", "TensorFlow facilita el Deep Learning"]

# Tokenización y secuenciación
tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, padding='post')
print(padded_sequences)
```

---

## ✅ **Paso 3: Construcción de un Modelo de NLP con RNN**

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

model = Sequential([
    Embedding(input_dim=10000, output_dim=16, input_length=10),
    SimpleRNN(32, return_sequences=False),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
```

---

## ✅ **Paso 4: Mejorando con LSTM y GRU**

```python
from tensorflow.keras.layers import LSTM, GRU

# Modelo con LSTM
model_lstm = Sequential([
    Embedding(10000, 16, input_length=10),
    LSTM(64, return_sequences=False),
    Dense(1, activation='sigmoid')
])

# Modelo con GRU
model_gru = Sequential([
    Embedding(10000, 16, input_length=10),
    GRU(64, return_sequences=False),
    Dense(1, activation='sigmoid')
])
```

---

## ✅ **Paso 5: Uso de Word Embeddings en Keras**

```python
import numpy as np

def load_glove_embeddings(filepath):
    embeddings_index = {}
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
    return embeddings_index

embeddings_index = load_glove_embeddings("glove.6B.100d.txt")
```

---

## ✅ **Paso 6: Implementación de un Transformer desde Cero**

```python
from tensorflow.keras.layers import MultiHeadAttention, LayerNormalization, Dropout

class TransformerBlock(tf.keras.layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super(TransformerBlock, self).__init__()
        self.att = MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = Sequential([
            Dense(ff_dim, activation="relu"),
            Dense(embed_dim)
        ])
        self.norm1 = LayerNormalization(epsilon=1e-6)
        self.norm2 = LayerNormalization(epsilon=1e-6)
        self.dropout1 = Dropout(rate)
        self.dropout2 = Dropout(rate)

    def call(self, inputs, training):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.norm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.norm2(out1 + ffn_output)
```

---

El tutorial sigue con los siguientes pasos:

✅ **Paso 7: Entrenamiento del Modelo en un Dataset Realista**
✅ **Paso 8: Predicción y Evaluación del Modelo**
✅ **Paso 9: Optimización y Fine-Tuning con Modelos Preentrenados**
✅ **Paso 10: Mini Despliegue con Flask y TensorFlow**
✅ **Paso 11: Transferencia de Conocimiento entre Modelos**
✅ **Paso 12: Retrieval-Augmented Generation (RAG)**

🚀 **Con este tutorial, aprenderás a dominar NLP con Keras y TensorFlow, desde lo básico hasta técnicas avanzadas como RAG.**

# Procesamiento de Lenguaje Natural (NLP) con Keras y TensorFlow

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **Keras y TensorFlow**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **12 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**
2. **Preparación de los Datos de Texto**
3. **Construcción de un Modelo de NLP con RNN**
4. **Mejorando con LSTM y GRU**
5. **Uso de Word Embeddings en Keras**
6. **Implementación de un Transformer desde Cero**
7. **Entrenamiento del Modelo en un Dataset Realista**
8. **Predicción y Evaluación del Modelo**
9. **Optimización y Fine-Tuning con Modelos Preentrenados**
10. **Mini Despliegue de un Modelo de NLP con Flask y TensorFlow**
11. **Transferencia de Conocimiento entre Modelos**
12. **Retrieval-Augmented Generation (RAG)**

---

## ✅ **Paso 7: Entrenamiento del Modelo en un Dataset Realista**

Para entrenar nuestro modelo en datos reales, utilizaremos el dataset de **IMDb Reviews**, disponible en TensorFlow Datasets.

### 📥 **Carga del Dataset**

```python
import tensorflow as tf
import tensorflow_datasets as tfds

# Cargar el dataset IMDb
dataset, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)
train_data, test_data = dataset["train"], dataset["test"]
```

### 🔍 **Preprocesamiento de Datos**

Convertimos los textos en secuencias de números con un Tokenizer de Keras y normalizamos su longitud.

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Tokenización
tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")

# Ajustar tokenizer con datos de entrenamiento
def tokenize_dataset(dataset):
    texts, labels = [], []
    for text, label in dataset:
        texts.append(text.numpy().decode("utf-8"))
        labels.append(label.numpy())
    return texts, labels

train_texts, train_labels = tokenize_dataset(train_data)
test_texts, test_labels = tokenize_dataset(test_data)

# Convertir textos a secuencias numéricas
tokenizer.fit_on_texts(train_texts)
train_sequences = tokenizer.texts_to_sequences(train_texts)
test_sequences = tokenizer.texts_to_sequences(test_texts)

# Padding de secuencias
train_padded = pad_sequences(train_sequences, padding='post', maxlen=200)
test_padded = pad_sequences(test_sequences, padding='post', maxlen=200)
```

### 🏋️ **Entrenamiento del Modelo LSTM**

Entrenamos un modelo basado en LSTM para clasificación de reseñas de películas.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Definir el modelo
model = Sequential([
    Embedding(10000, 16, input_length=200),
    LSTM(64, return_sequences=False),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamiento
epochs = 5
history = model.fit(
    train_padded, train_labels,
    validation_data=(test_padded, test_labels),
    epochs=epochs,
    batch_size=32
)
```

---

### 📌 **Conclusión y Próximos Pasos**

- Hemos preparado un **dataset realista** para entrenar el modelo.
- Implementamos un **modelo LSTM** para clasificación de texto.
- En el **próximo paso**, evaluaremos el modelo y realizaremos predicciones en texto nuevo. 🚀

# Procesamiento de Lenguaje Natural (NLP) con Keras y TensorFlow

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **Keras y TensorFlow**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **12 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**
2. **Preparación de los Datos de Texto**
3. **Construcción de un Modelo de NLP con RNN**
4. **Mejorando con LSTM y GRU**
5. **Uso de Word Embeddings en Keras**
6. **Implementación de un Transformer desde Cero**
7. **Entrenamiento del Modelo en un Dataset Realista**
8. **Predicción y Evaluación del Modelo**
9. **Optimización y Fine-Tuning con Modelos Preentrenados**
10. **Mini Despliegue de un Modelo de NLP con Flask y TensorFlow**
11. **Transferencia de Conocimiento entre Modelos**
12. **Retrieval-Augmented Generation (RAG)**

---

## ✅ **Paso 8: Predicción y Evaluación del Modelo**

Después de entrenar el modelo, es fundamental evaluar su rendimiento y realizar predicciones en datos de prueba.

### 📊 **Evaluación del Modelo**

Para evaluar el modelo, utilizaremos métricas como **accuracy** y la **curva de pérdida y precisión**.

```python
import matplotlib.pyplot as plt

# Evaluación del modelo
test_loss, test_acc = model.evaluate(test_padded, test_labels)
print(f"Precisión en datos de prueba: {test_acc:.4f}")

# Graficar la curva de pérdida y precisión
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Pérdida de Entrenamiento')
plt.plot(history.history['val_loss'], label='Pérdida de Validación')
plt.legend()
plt.title('Curva de Pérdida')

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Precisión de Entrenamiento')
plt.plot(history.history['val_accuracy'], label='Precisión de Validación')
plt.legend()
plt.title('Curva de Precisión')
plt.show()
```

### 🔍 **Realizar Predicciones**

Podemos utilizar el modelo entrenado para predecir el sentimiento de nuevas reseñas de películas.

```python
import numpy as np

def predict_sentiment(model, tokenizer, text):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=200, padding='post')
    prediction = model.predict(padded_sequence)[0][0]
    return "Positivo" if prediction > 0.5 else "Negativo"

# Ejemplo de predicción
review = "Esta película fue increíble, realmente la disfruté."
print(f"Reseña: '{review}' → Sentimiento Predicho: {predict_sentiment(model, tokenizer, review)}")
```

### 📌 **Conclusión y Próximos Pasos**

- Evaluamos el rendimiento del modelo con **métricas de precisión y pérdida**.
- Implementamos una **función para predecir el sentimiento de nuevos textos**.
- En el **próximo paso**, optimizaremos y aplicaremos **fine-tuning con modelos preentrenados**. 🚀


# Procesamiento de Lenguaje Natural (NLP) con Keras y TensorFlow

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **Keras y TensorFlow**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **12 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**
2. **Preparación de los Datos de Texto**
3. **Construcción de un Modelo de NLP con RNN**
4. **Mejorando con LSTM y GRU**
5. **Uso de Word Embeddings en Keras**
6. **Implementación de un Transformer desde Cero**
7. **Entrenamiento del Modelo en un Dataset Realista**
8. **Predicción y Evaluación del Modelo**
9. **Optimización y Fine-Tuning con Modelos Preentrenados**
10. **Mini Despliegue de un Modelo de NLP con Flask y TensorFlow**
11. **Transferencia de Conocimiento entre Modelos**
12. **Retrieval-Augmented Generation (RAG)**

---

## ✅ **Paso 9: Optimización y Fine-Tuning con Modelos Preentrenados**

Para mejorar el rendimiento del modelo, podemos utilizar modelos preentrenados como **BERT**, adaptándolos a nuestra tarea específica mediante **fine-tuning**.

### 📌 **Carga de un Modelo Preentrenado con Hugging Face**

Usaremos la librería `transformers` para cargar un modelo **BERT** preentrenado y realizar fine-tuning.

```python
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf

# Cargar el tokenizador y el modelo preentrenado
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = TFBertForSequenceClassification.from_pretrained(model_name, num_labels=2)
```

### 🔄 **Preparación de los Datos para BERT**

Convertimos los textos en entradas compatibles con BERT.

```python
def encode_texts(texts, labels, tokenizer, max_length=512):
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=max_length, return_tensors="tf")
    labels = tf.convert_to_tensor(labels)
    return encodings, labels

train_encodings, train_labels = encode_texts(train_texts, train_labels, tokenizer)
test_encodings, test_labels = encode_texts(test_texts, test_labels, tokenizer)
```

### 🏋️ **Fine-Tuning del Modelo**

Entrenamos BERT en nuestro dataset específico.

```python
from tensorflow.keras.optimizers.schedules import PolynomialDecay
from tensorflow.keras.optimizers import Adam

# Configurar el optimizador y la función de pérdida
num_train_steps = len(train_encodings["input_ids"]) // 32 * 3  # 3 épocas, batch size 32
lr_scheduler = PolynomialDecay(initial_learning_rate=5e-5, end_learning_rate=0, decay_steps=num_train_steps)
optimizer = Adam(learning_rate=lr_scheduler)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# Compilar modelo
model.compile(optimizer=optimizer, loss=loss_fn, metrics=["accuracy"])

# Entrenar modelo
history = model.fit(
    train_encodings["input_ids"], train_labels,
    validation_data=(test_encodings["input_ids"], test_labels),
    epochs=3,
    batch_size=8
)
```

### 🔍 **Evaluación del Modelo Fine-Tuned**

```python
# Evaluar el modelo después del fine-tuning
test_loss, test_acc = model.evaluate(test_encodings["input_ids"], test_labels)
print(f"Precisión después del fine-tuning: {test_acc:.4f}")
```

### 📌 **Conclusión y Próximos Pasos**

- Hemos cargado y fine-tuneado **BERT** para nuestra tarea específica.
- Evaluamos el modelo optimizado y medimos su rendimiento.
- En el **próximo paso**, veremos cómo desplegar nuestro modelo con Flask y TensorFlow. 🚀




# Procesamiento de Lenguaje Natural (NLP) con Keras y TensorFlow

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **Keras y TensorFlow**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **12 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**
2. **Preparación de los Datos de Texto**
3. **Construcción de un Modelo de NLP con RNN**
4. **Mejorando con LSTM y GRU**
5. **Uso de Word Embeddings en Keras**
6. **Implementación de un Transformer desde Cero**
7. **Entrenamiento del Modelo en un Dataset Realista**
8. **Predicción y Evaluación del Modelo**
9. **Optimización y Fine-Tuning con Modelos Preentrenados**
10. **Mini Despliegue de un Modelo de NLP con Flask y TensorFlow**
11. **Transferencia de Conocimiento entre Modelos**
12. **Retrieval-Augmented Generation (RAG)**

---

## ✅ **Paso 10: Mini Despliegue de un Modelo de NLP con Flask y TensorFlow**

En este paso, veremos cómo desplegar nuestro modelo fine-tuneado en un servicio web utilizando **Flask** y **TensorFlow**.

### 📌 **Instalación de Flask y Preparación del Entorno**

Antes de comenzar, asegurémonos de tener Flask instalado:

```bash
pip install flask tensorflow transformers
```

---

### 🔍 **Creación del Servidor Flask**

Primero, definimos un archivo `app.py` donde cargaremos nuestro modelo y tokenizador.

```python
from flask import Flask, request, jsonify
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

app = Flask(__name__)

# Cargar modelo preentrenado
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = TFBertForSequenceClassification.from_pretrained(model_name, num_labels=2)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    
    # Tokenizar texto
    inputs = tokenizer(text, return_tensors="tf", truncation=True, padding=True, max_length=512)
    
    # Obtener predicción
    predictions = model(inputs["input_ids"])['logits']
    sentiment = tf.argmax(predictions, axis=1).numpy()[0]
    
    return jsonify({"text": text, "sentiment": "Positivo" if sentiment == 1 else "Negativo"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

---

### 🏃 **Ejecución del Servidor Flask**

Ejecutamos el servidor con el siguiente comando:

```bash
python app.py
```

Esto iniciará la API en `http://127.0.0.1:5000/predict`, lista para recibir solicitudes.

---

### 🔄 **Consumo de la API desde Python**

Podemos probar la API enviando una solicitud desde Python:

```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {"text": "This movie was fantastic!"}
response = requests.post(url, json=data)
print(response.json())
```

---

### 🔥 **Despliegue en Producción**

Para desplegarlo en producción, podemos utilizar:
- **Docker** para encapsular el servicio y ejecutarlo en la nube.
- **AWS Lambda o Google Cloud Functions** para una solución sin servidores.
- **Heroku o Render** para un despliegue rápido con Flask.

Ejemplo de **Dockerfile** para empaquetar la API:

```dockerfile
FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

### 📌 **Conclusión**

¡Felicidades! Hemos completado un flujo completo de **NLP con Keras y TensorFlow**, desde la creación del modelo hasta su despliegue en un servicio web.

- Aprendimos sobre **RNN, LSTM, Transformers y Fine-Tuning**.
- Implementamos un modelo basado en **BERT** para clasificación de texto.
- Entrenamos, evaluamos y finalmente **desplegamos el modelo** en una API con Flask.

🚀 Ahora puedes seguir explorando NLP con más modelos avanzados o mejorar el despliegue con infraestructura en la nube. ¡Éxito en tu viaje con NLP y TensorFlow!


























# Procesamiento de Lenguaje Natural (NLP) con Keras

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **Keras y TensorFlow**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **12 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**
2. **Preparación de los Datos de Texto**
3. **Construcción de un Modelo de NLP con RNN**
4. **Mejorando con LSTM y GRU**
5. **Uso de Word Embeddings en Keras**
6. **Implementación de un Transformer desde Cero**
7. **Entrenamiento del Modelo en un Dataset Realista**
8. **Predicción y Evaluación del Modelo**
9. **Optimización y Fine-Tuning con Modelos Preentrenados**
10. **Mini Despliegue de un Modelo de NLP con Flask y TensorFlow**
11. **Transferencia de Conocimiento entre Modelos**
12. **Retrieval-Augmented Generation (RAG)**

---

## ✅ **Paso 11: Transferencia de Conocimiento entre Modelos**

La **transferencia de conocimiento** permite reutilizar modelos preentrenados para nuevas tareas con menos datos y entrenamiento. Es una estrategia clave en **aprendizaje profundo** que optimiza el rendimiento de los modelos sin necesidad de entrenar desde cero.

### 📌 **Métodos de Transferencia de Conocimiento**

1. **Fine-Tuning Completo**: Se ajustan todas las capas del modelo preentrenado en la nueva tarea. Esto permite máxima adaptación, pero requiere más datos y tiempo de entrenamiento.
2. **Congelación de Capas**: Se mantienen congeladas las primeras capas del modelo preentrenado (que capturan características generales) y solo se ajustan las capas superiores para la nueva tarea. Esta técnica es útil cuando se tienen pocos datos.
3. **Extracción de Características**: Se usa el modelo preentrenado para extraer representaciones de los datos, sin modificar sus pesos, y se agrega una nueva capa para la tarea específica. Es la opción más eficiente en datos limitados.

Ejemplo en Keras de congelación de capas en un modelo basado en **BERT**:

```python
import tensorflow as tf
from transformers import TFBertForSequenceClassification

model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Congelar todas las capas excepto la última
for layer in model.layers[:-1]:
    layer.trainable = False

# Agregar una nueva capa de clasificación
model.layers[-1].trainable = True
```

Además, al entrenar en un dominio específico, se pueden aplicar técnicas como **diferentes tasas de aprendizaje por capa** o **ajuste progresivo**, donde primero se entrenan las capas superiores y luego se descongelan gradualmente las inferiores.

---

## ✅ **Paso 12: Retrieval-Augmented Generation (RAG)**

**Retrieval-Augmented Generation (RAG)** es un enfoque híbrido que combina modelos generativos (como GPT) con recuperación de información externa. Esto permite que el modelo recupere información relevante de documentos o bases de datos antes de generar una respuesta, mejorando la precisión y reduciendo la generación de contenido inexacto.

### 📌 **Cómo Funciona RAG**

1. **Retrieval (Recuperación):** Se busca información relevante en bases de datos o documentos.
2. **Augmentation (Aumento):** La información recuperada se combina con la entrada del usuario.
3. **Generation (Generación):** Un modelo generativo usa la información recuperada para generar una respuesta coherente y precisa.

Ejemplo en Keras y TensorFlow usando `transformers`:

```python
from transformers import RagTokenizer, RagRetriever, TFRagModel
import tensorflow as tf

# Cargar modelo RAG
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq")
model = TFRagModel.from_pretrained("facebook/rag-token-nq")

# Entrada del usuario
input_text = "¿Quién escribió Don Quijote?"
inputs = tokenizer(input_text, return_tensors="tf")

# Generar respuesta
output = model.generate(**inputs)
print(tokenizer.batch_decode(output, skip_special_tokens=True))
```

### 📌 **Casos de Uso de RAG**

- **Sistemas de preguntas y respuestas (Q&A):** Mejora la precisión al obtener respuestas desde bases de conocimiento actualizadas.
- **Asistentes virtuales y chatbots:** Integra información de documentos y bases de datos externas para dar respuestas más precisas.
- **Generación de informes y resúmenes:** Extrae información de múltiples fuentes para generar contenido estructurado.
- **Análisis de información legal y médica:** Permite a los modelos recuperar normativa o papers científicos relevantes.

### 📌 **Ventajas de RAG sobre Modelos Generativos Simples**

| Característica | Modelos Generativos Tradicionales | RAG |
|---------------|--------------------------------|----|
| **Contexto basado en datos externos** | No | Sí |
| **Capacidad de actualización** | Baja (entrenamiento previo) | Alta (consulta en tiempo real) |
| **Reducción de alucinaciones** | No | Sí |
| **Capacidad de integración con bases de datos** | No | Sí |

---

### 📌 **Conclusión Final**

- Hemos agregado técnicas avanzadas de **transferencia de conocimiento** para optimizar el uso de modelos preentrenados en nuevas tareas.
- Hemos explorado **Retrieval-Augmented Generation (RAG)** para mejorar la generación de texto con recuperación de información en tiempo real.
- Estos enfoques permiten crear modelos NLP más eficientes, precisos y con mejor capacidad de generalización.

🚀 ¡Ahora estás listo para construir modelos NLP robustos con Keras y TensorFlow!