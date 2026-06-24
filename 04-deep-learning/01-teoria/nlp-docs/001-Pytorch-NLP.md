---
title: "Procesamiento de Lenguaje Natural (NLP) con PyTorch"
author: "José Manuel Sánchez Álvarez"
date: "2025-02-26"
output: 
    pdf_document:
        toc: true
        toc_depth: 2
        number_sections: true
        fig_caption: true
        latex_engine: xelatex
---

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  

---

## ✅ **Paso 1: Fundamentos del NLP y Deep Learning**

### 📖 **¿Qué es el NLP y por qué es importante?**

El **Procesamiento de Lenguaje Natural (NLP)** es un campo de la inteligencia artificial que permite a las máquinas comprender, interpretar y generar texto en lenguaje humano. Se usa en aplicaciones como:

- **Traducción automática** (Google Translate, DeepL)
- **Análisis de sentimiento** (clasificación de opiniones)
- **Chatbots y asistentes virtuales** (ChatGPT, Siri, Alexa)
- **Resumen de textos**
- **Corrección gramatical**

El NLP tradicionalmente se basaba en reglas escritas a mano y modelos estadísticos, pero hoy en día se apoya en el **Deep Learning**, permitiendo un mejor rendimiento gracias a modelos como LSTM, GRU, Transformers (BERT, GPT, etc.).

---

### 🧠 **Tipos de redes neuronales en NLP**

Existen diferentes tipos de redes neuronales usadas en NLP, cada una con ventajas y desventajas:

| Tipo de Red | Características | Casos de Uso |
|------------|----------------|--------------|
| **RNN (Red Neuronal Recurrente)** | Permite modelar secuencias de texto, pero sufre del problema del **gradiente desaparecido**. | Modelos simples de secuencias de texto. |
| **LSTM (Long Short-Term Memory)** | Variante de RNN que maneja dependencias largas mejor. | Análisis de sentimiento, generación de texto. |
| **GRU (Gated Recurrent Unit)** | Similar a LSTM pero más eficiente. | Modelado de texto en tiempo real. |
| **Transformer** | Usa mecanismos de **self-attention**, permite paralelización y es la base de modelos modernos como BERT y GPT. | Traducción, generación de texto, chatbots. |

---

### 🔢 **Representación de Texto en Deep Learning**

Antes de alimentar texto en una red neuronal, es necesario convertirlo en una representación numérica. Existen varias opciones:

1. **One-hot encoding**: Representa palabras como vectores binarios, pero no captura relaciones semánticas.
2. **Word Embeddings**: Representación densa en un espacio vectorial que captura relaciones semánticas (Ej: *Word2Vec, GloVe, FastText*).
3. **Embeddings entrenables en PyTorch**: Se inicializan al azar y se ajustan durante el entrenamiento.

Ejemplo en PyTorch:

```python
import torch
import torch.nn as nn

# Definimos un vocabulario de 5 palabras
vocab_size = 5
embedding_dim = 10

# Creamos la capa de embedding
embedding = nn.Embedding(vocab_size, embedding_dim)

# Entrada de ejemplo (palabras representadas como índices)
input_ids = torch.tensor([0, 1, 3, 4])

# Obtenemos los embeddings de las palabras
embedded_output = embedding(input_ids)
print(embedded_output)
```

---

### 🔍 **Comparación de enfoques en NLP**

| Técnica | Ventajas | Desventajas |
|---------|----------|--------------|
| **One-hot encoding** | Simple, rápida. | No captura relaciones entre palabras. |
| **Word2Vec/GloVe** | Captura relaciones semánticas. | No se adapta a nuevos datos sin reentrenar. |
| **Embeddings entrenables** | Se ajustan dinámicamente. | Requiere más datos y tiempo de entrenamiento. |

---

## ✅ **Paso 2: Preparación de los Datos de Texto**

Para entrenar modelos NLP en PyTorch, es crucial preparar y limpiar los datos de texto correctamente. Vamos a trabajar con textos clásicos como *Don Quijote*, *Moby Dick* y otros disponibles en formato `.txt`.

### 📥 **Descarga y Carga de Datos**

Podemos obtener textos clásicos desde **Project Gutenberg** o repositorios similares.

```python
import requests

def descargar_texto(url, archivo):
    respuesta = requests.get(url)
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(respuesta.text)

# Descarga de Don Quijote y Moby Dick
descargar_texto("https://www.gutenberg.org/files/2000/2000-0.txt", "don_quijote.txt")
descargar_texto("https://www.gutenberg.org/files/2701/2701-0.txt", "moby_dick.txt")
```

### 🔍 **Preprocesamiento de Texto**

- Conversión a minúsculas.
- Eliminación de signos de puntuación.
- Tokenización en palabras o subpalabras.

Ejemplo en PyTorch:

```python
import re

def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-záéíóúüñ ]', '', texto)
    return texto

with open("don_quijote.txt", "r", encoding="utf-8") as f:
    texto = f.read()
texto_limpio = limpiar_texto(texto)
print(texto_limpio[:500])
```

En el siguiente paso, exploraremos cómo tokenizar y vectorizar estos textos para su uso en redes neuronales. 🚀

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**
2. **Preparación de los Datos de Texto**
3. **Construcción de un Modelo de NLP con RNN**
4. **Mejorando con LSTM y GRU**
5. **Uso de Word Embeddings en PyTorch**
6. **Implementación de un Transformer desde Cero**
7. **Entrenamiento del Modelo en un Dataset Realista**
8. **Predicción y Evaluación del Modelo**
9. **Optimización y Fine-Tuning con Modelos Preentrenados**
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**

---

## ✅ **Paso 3: Construcción de un Modelo de NLP con RNN**

En este paso, construiremos un modelo de **Red Neuronal Recurrente (RNN)** para procesar texto en secuencias y hacer predicciones sobre datos de lenguaje natural.

### 📌 **Arquitectura de una RNN para NLP**

Una RNN procesa texto palabra por palabra (o carácter por carácter), manteniendo un estado interno que captura la información de palabras previas.

1. Se representa cada palabra con un **embedding**.
2. Se pasa la secuencia de embeddings a través de una **capa recurrente**.
3. Se obtiene una predicción basada en la última salida de la RNN.

### 🔨 **Implementación de una RNN en PyTorch**

```python
import torch
import torch.nn as nn
import torch.optim as optim

class RNNModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(RNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        embedded = self.embedding(x)
        output, hidden = self.rnn(embedded)
        return self.fc(output[:, -1, :])

# Parámetros del modelo
VOCAB_SIZE = 5000
EMBEDDING_DIM = 100
HIDDEN_DIM = 128
OUTPUT_DIM = 1

# Crear la red neuronal
model = RNNModel(VOCAB_SIZE, EMBEDDING_DIM, HIDDEN_DIM, OUTPUT_DIM)
print(model)
```

### ⚙️ **Entrenamiento del Modelo**

```python
# Definir la función de pérdida y el optimizador
loss_fn = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

def train(model, dataloader, loss_fn, optimizer, epochs=5):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for X_batch, y_batch in dataloader:
            optimizer.zero_grad()
            predictions = model(X_batch).squeeze(1)
            loss = loss_fn(predictions, y_batch)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}: Loss = {total_loss/len(dataloader)}")
```

### 🔍 **Evaluación del Modelo**

```python
def evaluate(model, dataloader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for X_batch, y_batch in dataloader:
            predictions = torch.round(torch.sigmoid(model(X_batch).squeeze(1)))
            correct += (predictions == y_batch).sum().item()
            total += y_batch.size(0)
    print(f"Precisión del modelo: {correct/total:.2f}")
```

---

### 🔍 **Alternativas y Consideraciones**

- **Problema del gradiente desaparecido:** Las RNN estándar pueden olvidar información a largo plazo. Para solucionar esto, en el siguiente paso exploraremos **LSTMs y GRUs**.
- **Uso de embeddings preentrenados:** Mejoraremos el modelo en el paso 5 con embeddings preentrenados como **Word2Vec o GloVe**.
- **Transformers:** Para tareas más complejas, exploraremos arquitecturas como **BERT y GPT** en pasos posteriores.

En el **próximo paso**, mejoraremos la RNN con **LSTM y GRU** para manejar dependencias largas en el texto. 🚀

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  

---

## ✅ **Paso 4: Mejorando con LSTM y GRU**

Las **Redes Neuronales Recurrentes (RNN)** presentan el problema del **gradiente desaparecido**, lo que dificulta la captura de dependencias a largo plazo en el texto. Para solucionar esto, utilizamos:

- **LSTM (Long Short-Term Memory):** Puede recordar información durante períodos más largos.
- **GRU (Gated Recurrent Unit):** Variante más eficiente de LSTM, con menos parámetros y similar rendimiento.

### 📌 **Arquitectura de LSTM y GRU**

Ambas redes funcionan de manera similar:
1. Se representa cada palabra con un **embedding**.
2. Se pasa la secuencia de embeddings a través de una **capa LSTM o GRU**.
3. Se obtiene una predicción basada en la última salida de la red.

### 🔨 **Implementación de una LSTM en PyTorch**

```python
import torch
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(LSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        embedded = self.embedding(x)
        output, (hidden, cell) = self.lstm(embedded)
        return self.fc(output[:, -1, :])

# Parámetros del modelo
VOCAB_SIZE = 5000
EMBEDDING_DIM = 100
HIDDEN_DIM = 128
OUTPUT_DIM = 1

# Crear la red neuronal
model_lstm = LSTMModel(VOCAB_SIZE, EMBEDDING_DIM, HIDDEN_DIM, OUTPUT_DIM)
print(model_lstm)
```

### 🔨 **Implementación de una GRU en PyTorch**

```python
class GRUModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(GRUModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.gru = nn.GRU(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        embedded = self.embedding(x)
        output, hidden = self.gru(embedded)
        return self.fc(output[:, -1, :])

# Crear la red neuronal
model_gru = GRUModel(VOCAB_SIZE, EMBEDDING_DIM, HIDDEN_DIM, OUTPUT_DIM)
print(model_gru)
```

### ⚙️ **Entrenamiento de LSTM y GRU**

El entrenamiento sigue la misma estructura que la RNN estándar:

```python
import torch.optim as optim

loss_fn = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model_lstm.parameters(), lr=0.001)

def train(model, dataloader, loss_fn, optimizer, epochs=5):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for X_batch, y_batch in dataloader:
            optimizer.zero_grad()
            predictions = model(X_batch).squeeze(1)
            loss = loss_fn(predictions, y_batch)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}: Loss = {total_loss/len(dataloader)}")
```

### 🔍 **Comparación de Modelos RNN vs LSTM vs GRU**

| Modelo | Parámetros | Ventajas | Desventajas |
|--------|-----------|----------|--------------|
| **RNN** | Menos | Rápida, fácil de entender | Problema del gradiente desaparecido |
| **LSTM** | Más | Maneja secuencias largas | Computacionalmente costosa |
| **GRU** | Intermedia | Más eficiente que LSTM con similar rendimiento | Menos flexible que LSTM |

---

### 🔍 **Conclusiones y Siguientes Pasos**

- **Para secuencias cortas**, una **RNN estándar** puede ser suficiente.
- **Para texto más complejo**, se recomienda **LSTM o GRU**.
- **Para tareas avanzadas como traducción automática o generación de texto**, utilizaremos **Transformers**, que veremos en el Paso 6.

En el **próximo paso**, aprenderemos a **utilizar embeddings preentrenados** como **Word2Vec y GloVe** para mejorar el rendimiento del modelo. 🚀

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  

---

## ✅ **Paso 5: Uso de Word Embeddings en PyTorch**

Para mejorar el rendimiento de los modelos NLP, utilizamos **word embeddings**, que representan palabras en un espacio vectorial denso, capturando relaciones semánticas.

### 📌 **Tipos de Word Embeddings**

| Técnica | Características |
|---------|----------------|
| **One-hot encoding** | Representa palabras con vectores binarios, pero no captura relaciones semánticas. |
| **Word2Vec** | Modela el contexto de palabras en una ventana, generando embeddings significativos. |
| **GloVe** | Basado en matrices de coocurrencia, capturando relaciones globales. |
| **FastText** | Considera subpalabras, mejorando el manejo de palabras raras. |
| **Embeddings entrenables** | Se ajustan durante el entrenamiento, optimizados para la tarea específica. |

---

### 🔨 **Uso de Embeddings en PyTorch**

#### **1. Creación de Embeddings desde Cero**

```python
import torch
import torch.nn as nn

# Definir el tamaño del vocabulario y la dimensión del embedding
vocab_size = 5000
embedding_dim = 100

# Crear capa de embedding
embedding = nn.Embedding(vocab_size, embedding_dim)

# Entrada de ejemplo (índices de palabras en vocabulario)
input_ids = torch.tensor([1, 4, 3, 2])

# Obtener embeddings
embedded_output = embedding(input_ids)
print(embedded_output)
```

#### **2. Uso de Embeddings Preentrenados (GloVe, Word2Vec)**

```python
import gensim
import torch
import torch.nn as nn
import numpy as np

# Cargar modelo Word2Vec preentrenado
glove_path = "glove.6B.100d.txt"
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(glove_path, binary=False)

# Convertir a matriz de PyTorch
embedding_matrix = np.zeros((len(word2vec_model.key_to_index), 100))
for word, idx in word2vec_model.key_to_index.items():
    embedding_matrix[idx] = word2vec_model[word]

embedding_tensor = torch.tensor(embedding_matrix, dtype=torch.float32)

# Crear capa de embedding en PyTorch con los pesos preentrenados
embedding_layer = nn.Embedding.from_pretrained(embedding_tensor, freeze=False)
```

#### **3. Entrenamiento con Embeddings**

Podemos usar estos embeddings en nuestros modelos **LSTM o GRU** para mejorar la calidad del aprendizaje.

```python
class LSTMWithEmbeddings(nn.Module):
    def __init__(self, embedding_matrix, hidden_dim, output_dim):
        super().__init__()
        self.embedding = nn.Embedding.from_pretrained(embedding_matrix, freeze=False)
        self.lstm = nn.LSTM(embedding_matrix.shape[1], hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        embedded = self.embedding(x)
        output, (hidden, cell) = self.lstm(embedded)
        return self.fc(output[:, -1, :])

# Crear modelo con embeddings preentrenados
model = LSTMWithEmbeddings(embedding_tensor, hidden_dim=128, output_dim=1)
print(model)
```

---

### 🔍 **Ventajas y Desafíos de los Embeddings**

| Método | Ventajas | Desafíos |
|--------|----------|--------------|
| **GloVe/Word2Vec** | Mejora la semántica del modelo | No adapta el significado a nuevos contextos |
| **FastText** | Maneja palabras raras mejor | Más costoso en tiempo de cómputo |
| **Embeddings entrenables** | Se adaptan al dominio específico | Requieren muchos datos para buen rendimiento |

---

### 📌 **Conclusiones y Siguientes Pasos**

- Los **word embeddings** mejoran significativamente la calidad de los modelos NLP.
- Podemos usar embeddings preentrenados como **GloVe, Word2Vec** o entrenar los nuestros.
- **En el próximo paso**, implementaremos **Transformers desde cero** para aprovechar los avances modernos en NLP. 🚀

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  

---

## ✅ **Paso 6: Implementación de un Transformer desde Cero**

Los **Transformers** han revolucionado el NLP al permitir la paralelización y capturar relaciones contextuales a largo plazo mediante el mecanismo de **self-attention**.

### 📌 **Arquitectura del Transformer**

Un modelo Transformer estándar consta de:

- **Embeddings Posicionales:** Se suman a los embeddings de palabras para capturar el orden.
- **Mecanismo de Self-Attention:** Permite que cada palabra preste atención a otras en la oración.
- **Capas de Feed-Forward:** Aplican transformaciones no lineales después de la atención.
- **Normalización y Dropout:** Mejoran la estabilidad y reducen el sobreajuste.

---

### 🔨 **Implementación del Mecanismo de Self-Attention**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SelfAttention(nn.Module):
    def __init__(self, embed_dim, heads):
        super(SelfAttention, self).__init__()
        self.embed_dim = embed_dim
        self.heads = heads
        self.head_dim = embed_dim // heads
        
        assert self.head_dim * heads == embed_dim, "Embed dim must be divisible by heads"
        
        self.values = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.keys = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.queries = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.fc_out = nn.Linear(heads * self.head_dim, embed_dim)
    
    def forward(self, values, keys, query):
        N = query.shape[0]
        
        values = values.reshape(N, -1, self.heads, self.head_dim)
        keys = keys.reshape(N, -1, self.heads, self.head_dim)
        queries = query.reshape(N, -1, self.heads, self.head_dim)
        
        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
        attention = torch.softmax(energy / (self.embed_dim ** 0.5), dim=3)
        out = torch.einsum("nhql,nlhd->nqhd", [attention, values])
        out = out.reshape(N, -1, self.heads * self.head_dim)
        
        return self.fc_out(out)
```

---

### 🔨 **Construcción del Bloque del Transformer**

```python
class TransformerBlock(nn.Module):
    def __init__(self, embed_dim, heads, dropout, forward_expansion):
        super(TransformerBlock, self).__init__()
        self.attention = SelfAttention(embed_dim, heads)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.feed_forward = nn.Sequential(
            nn.Linear(embed_dim, forward_expansion * embed_dim),
            nn.ReLU(),
            nn.Linear(forward_expansion * embed_dim, embed_dim)
        )
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        attention = self.attention(x, x, x)
        x = self.norm1(attention + x)
        forward = self.feed_forward(x)
        x = self.norm2(forward + x)
        return self.dropout(x)
```

---

### 🔨 **Implementación del Modelo Transformer Completo**

```python
class Transformer(nn.Module):
    def __init__(self, embed_size, num_layers, heads, dropout, forward_expansion, vocab_size, max_length):
        super(Transformer, self).__init__()
        self.word_embedding = nn.Embedding(vocab_size, embed_size)
        self.position_embedding = nn.Embedding(max_length, embed_size)
        self.layers = nn.ModuleList(
            [TransformerBlock(embed_size, heads, dropout, forward_expansion) for _ in range(num_layers)]
        )
        self.fc_out = nn.Linear(embed_size, vocab_size)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        N, seq_length = x.shape
        positions = torch.arange(0, seq_length).expand(N, seq_length).to(x.device)
        out = self.dropout(self.word_embedding(x) + self.position_embedding(positions))
        for layer in self.layers:
            out = layer(out)
        return self.fc_out(out)
```

---

### 🔍 **Ventajas de los Transformers sobre RNNs y LSTMs**

| Característica | Transformers | LSTMs/GRUs |
|---------------|-------------|------------|
| **Paralelización** | Alta (procesa toda la secuencia a la vez) | Baja (procesa secuencialmente) |
| **Manejo de Secuencias Largas** | Bueno | Limitado (problema del gradiente desaparecido) |
| **Atención Contextual** | Usa self-attention | Depende de memoria a largo plazo |

---

### 📌 **Conclusiones y Siguientes Pasos**

- Hemos implementado un **Transformer desde cero**, incluyendo **Self-Attention y Multi-Head Attention**.
- Los Transformers son más eficientes que RNNs y LSTMs en tareas de NLP avanzadas.
- **En el próximo paso**, entrenaremos nuestro modelo Transformer en un dataset realista. 🚀

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  

---

## ✅ **Paso 7: Entrenamiento del Modelo en un Dataset Realista**

Ahora que hemos implementado un Transformer desde cero, es momento de entrenarlo en un dataset realista para ver cómo aprende patrones en el lenguaje natural.

### 📌 **Selección del Dataset**

Para este entrenamiento, utilizaremos el conjunto de datos de **IMDb Reviews**, que contiene reseñas de películas etiquetadas como positivas o negativas.

```python
from torchtext.datasets import IMDB
from torchtext.data.utils import get_tokenizer

# Descarga y carga del dataset
train_iter = IMDB(split='train')
test_iter = IMDB(split='test')
```

### 🔍 **Tokenización y Preparación de Datos**

Antes de entrenar el modelo, es necesario tokenizar y vectorizar los textos.

```python
from torchtext.vocab import build_vocab_from_iterator
from torch.utils.data import DataLoader, Dataset
import torch

tokenizer = get_tokenizer("basic_english")

def yield_tokens(data_iter):
    for _, text in data_iter:
        yield tokenizer(text)

# Construir vocabulario
vocab = build_vocab_from_iterator(yield_tokens(train_iter), specials=["<unk>"])
vocab.set_default_index(vocab["<unk>"])
```

### 🔄 **Conversión de Texto a Tensores**

```python
def text_pipeline(text):
    return vocab(tokenizer(text))

def label_pipeline(label):
    return 1 if label == 'pos' else 0
```

### 📥 **Creación del DataLoader**

```python
class IMDBDataset(Dataset):
    def __init__(self, data_iter):
        self.data = [(text_pipeline(text), label_pipeline(label)) for label, text in data_iter]
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return torch.tensor(self.data[idx][0]), torch.tensor(self.data[idx][1])

train_dataset = IMDBDataset(IMDB(split='train'))
test_dataset = IMDBDataset(IMDB(split='test'))

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, collate_fn=lambda x: tuple(zip(*x)))
```

### 🏋️ **Entrenamiento del Transformer**

```python
def train_model(model, dataloader, loss_fn, optimizer, epochs=3):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for texts, labels in dataloader:
            texts, labels = torch.stack(texts).to(device), torch.tensor(labels).to(device)
            optimizer.zero_grad()
            output = model(texts)
            loss = loss_fn(output, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}: Loss = {total_loss/len(dataloader)}")
```

### 📌 **Conclusión y Próximos Pasos**

- Hemos preparado un dataset realista y entrenado nuestro Transformer en datos reales.
- En el **próximo paso**, veremos cómo evaluar el rendimiento del modelo y realizar predicciones. 🚀

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  

---

## ✅ **Paso 8: Predicción y Evaluación del Modelo**

Después de entrenar nuestro modelo Transformer, es fundamental evaluar su rendimiento y realizar predicciones en datos de prueba.

### 📌 **Evaluación del Modelo**

Para evaluar el modelo, utilizaremos métricas comunes en NLP como **accuracy (precisión)** y **F1-score**.

```python
from sklearn.metrics import accuracy_score, f1_score
import torch.nn.functional as F

# Función de evaluación
def evaluate_model(model, dataloader):
    model.eval()
    all_preds = []
    all_labels = []
    
    with torch.no_grad():
        for texts, labels in dataloader:
            texts, labels = torch.stack(texts).to(device), torch.tensor(labels).to(device)
            output = model(texts)
            predictions = torch.round(torch.sigmoid(output)).cpu().numpy()
            all_preds.extend(predictions)
            all_labels.extend(labels.cpu().numpy())
    
    acc = accuracy_score(all_labels, all_preds)
    f1 = f1_score(all_labels, all_preds)
    print(f"Accuracy: {acc:.4f}, F1-score: {f1:.4f}")
```

### 🔍 **Realizar Predicciones**

Ahora, podemos utilizar el modelo entrenado para hacer predicciones sobre nuevas reseñas de películas.

```python
def predict_sentiment(model, text):
    model.eval()
    tokens = text_pipeline(text)
    tokens_tensor = torch.tensor(tokens).unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(tokens_tensor)
        prediction = torch.sigmoid(output).item()
    
    return "Positivo" if prediction > 0.5 else "Negativo"

# Ejemplo de predicción
review = "This movie was amazing, I really enjoyed it!"
print(predict_sentiment(model, review))
```

### 📌 **Conclusión y Próximos Pasos**

- Hemos evaluado nuestro modelo Transformer utilizando **accuracy** y **F1-score**.
- También hemos implementado una función para realizar **predicciones en texto nuevo**.
- En el **próximo paso**, veremos cómo optimizar y hacer **fine-tuning con modelos preentrenados**. 🚀

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  

---

## ✅ **Paso 9: Optimización y Fine-Tuning con Modelos Preentrenados**

En este paso, exploraremos cómo mejorar nuestro modelo utilizando **fine-tuning** sobre modelos preentrenados como **BERT** y **GPT-2**.

### 📌 **¿Por qué Fine-Tuning?**

Los modelos preentrenados han sido entrenados en grandes volúmenes de datos y pueden transferir su conocimiento a nuevas tareas con poca cantidad de datos específicos.

### 🔍 **Carga de un Modelo Preentrenado con Hugging Face**

Usaremos `transformers` de Hugging Face para cargar **BERT** y realizar fine-tuning en nuestro dataset.

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Cargar modelo y tokenizador preentrenado
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Enviar modelo a GPU si está disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

### 🔄 **Preparación de los Datos para BERT**

Convertimos los textos en entradas compatibles con BERT.

```python
def encode_texts(texts, labels, tokenizer, max_length=512):
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=max_length, return_tensors="pt")
    labels = torch.tensor(labels)
    return encodings, labels
```

### 🏋️ **Fine-Tuning del Modelo**

Entrenamos BERT en nuestro dataset específico.

```python
from torch.utils.data import DataLoader, TensorDataset
import torch.optim as optim

def train_bert(model, train_texts, train_labels, tokenizer, epochs=3, batch_size=8):
    model.train()
    encodings, labels = encode_texts(train_texts, train_labels, tokenizer)
    dataset = TensorDataset(encodings['input_ids'], encodings['attention_mask'], labels)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    optimizer = optim.AdamW(model.parameters(), lr=5e-5)
    loss_fn = torch.nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        total_loss = 0
        for batch in dataloader:
            input_ids, attention_mask, labels = [b.to(device) for b in batch]
            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}: Loss = {total_loss/len(dataloader)}")
```

### 🔍 **Evaluación del Modelo Fine-Tuned**

```python
def evaluate_bert(model, test_texts, test_labels, tokenizer):
    model.eval()
    encodings, labels = encode_texts(test_texts, test_labels, tokenizer)
    dataset = TensorDataset(encodings['input_ids'], encodings['attention_mask'], labels)
    dataloader = DataLoader(dataset, batch_size=8, shuffle=False)
    
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in dataloader:
            input_ids, attention_mask, labels = [b.to(device) for b in batch]
            outputs = model(input_ids, attention_mask=attention_mask)
            preds = torch.argmax(outputs.logits, dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    
    print(f"Accuracy: {correct / total:.4f}")
```

### 📌 **Conclusión y Próximos Pasos**

- Hemos cargado y fine-tuneado **BERT** para nuestra tarea específica.
- Evaluamos el modelo optimizado y medimos su rendimiento.
- En el **próximo paso**, veremos cómo desplegar nuestro modelo con Flask y PyTorch. 🚀
# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **10 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  

---

## ✅ **Paso 10: Mini Despliegue de un Modelo de NLP con Flask y PyTorch**

En este último paso, veremos cómo desplegar nuestro modelo fine-tuneado en un servicio web utilizando **Flask** y **PyTorch**.

### 📌 **Instalación de Flask y Preparación del Entorno**

Antes de comenzar, asegurémonos de tener Flask instalado:

```bash
pip install flask torch transformers
```

---

### 🔍 **Creación del Servidor Flask**

Primero, definimos un archivo `app.py` donde cargaremos nuestro modelo y tokenizador.

```python
from flask import Flask, request, jsonify
import torch
from transformers import BertTokenizer, BertForSequenceClassification

app = Flask(__name__)

# Cargar modelo preentrenado
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    
    # Tokenizar texto
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    inputs = {key: val.to(device) for key, val in inputs.items()}
    
    # Obtener predicción
    with torch.no_grad():
        output = model(**inputs)
        prediction = torch.argmax(output.logits, dim=1).item()
    
    return jsonify({"text": text, "sentiment": "Positivo" if prediction == 1 else "Negativo"})

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

¡Felicidades! Hemos completado un flujo completo de **NLP con PyTorch**, desde la creación del modelo hasta su despliegue en un servicio web.

- Aprendimos sobre **RNN, LSTM, Transformers y Fine-Tuning**.
- Implementamos un modelo basado en **BERT** para clasificación de texto.
- Entrenamos, evaluamos y finalmente **desplegamos el modelo** en una API con Flask.

🚀 Ahora puedes seguir explorando NLP con más modelos avanzados o mejorar el despliegue con infraestructura en la nube. ¡Éxito en tu viaje con NLP y PyTorch!

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **12 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**  
2. **Preparación de los Datos de Texto**  
3. **Construcción de un Modelo de NLP con RNN**  
4. **Mejorando con LSTM y GRU**  
5. **Uso de Word Embeddings en PyTorch**  
6. **Implementación de un Transformer desde Cero**  
7. **Entrenamiento del Modelo en un Dataset Realista**  
8. **Predicción y Evaluación del Modelo**  
9. **Optimización y Fine-Tuning con Modelos Preentrenados**  
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**  
11. **Transferencia de Conocimiento entre Modelos**  
12. **Retrieval-Augmented Generation (RAG)**  

---

## ✅ **Paso 11: Transferencia de Conocimiento entre Modelos**

La **transferencia de conocimiento** permite reutilizar modelos preentrenados para nuevas tareas con menos datos y entrenamiento.

### 📌 **Métodos de Transferencia de Conocimiento**

1. **Fine-Tuning Completo**: Se ajustan todas las capas del modelo preentrenado.
2. **Congelación de Capas**: Se mantiene congelada una parte del modelo y solo se ajustan las últimas capas.
3. **Extracción de Características**: Se usa el modelo preentrenado para extraer representaciones de los datos sin modificar sus pesos.

Ejemplo en PyTorch de congelación de capas en un modelo basado en **BERT**:

```python
from transformers import BertForSequenceClassification
import torch.nn as nn

model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Congelar todas las capas excepto la última
for param in model.base_model.parameters():
    param.requires_grad = False

# Agregar una nueva capa de clasificación
model.classifier = nn.Linear(model.config.hidden_size, 2)
```

---

## ✅ **Paso 12: Retrieval-Augmented Generation (RAG)**

**RAG** combina modelos generativos (como GPT) con recuperación de información externa para mejorar la precisión y contextualización de respuestas generadas.

### 📌 **Cómo Funciona RAG**

1. **Retrieval**: Se busca información relevante en bases de datos o documentos.
2. **Augmentation**: Se combina la información recuperada con la entrada del usuario.
3. **Generation**: Un modelo generativo utiliza la información recuperada para generar una respuesta.

Ejemplo en PyTorch usando `transformers`:

```python
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import torch

# Cargar modelo RAG
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq")
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq")

# Entrada del usuario
input_text = "¿Quién escribió Don Quijote?"
inputs = tokenizer(input_text, return_tensors="pt")

# Generar respuesta
with torch.no_grad():
    generated = model.generate(**inputs)
    print(tokenizer.batch_decode(generated, skip_special_tokens=True))
```

### 📌 **Beneficios de RAG**

- Integra fuentes de información externas en modelos generativos.
- Reduce la **alucinación** en modelos de lenguaje.
- Es útil en sistemas de preguntas y respuestas, chatbots y generación de contenido basada en conocimiento actualizado.

---

### 📌 **Conclusión Final**

- Hemos agregado técnicas avanzadas de **transferencia de conocimiento** y **Retrieval-Augmented Generation**.
- Estos enfoques permiten crear modelos NLP más eficientes y con mejor capacidad de generalización.
- Puedes seguir explorando modelos aún más avanzados con **transformers especializados y retrieval en bases de datos semánticas**.

🚀 ¡Ahora estás listo para construir modelos NLP robustos con PyTorch!

# Procesamiento de Lenguaje Natural (NLP) con PyTorch

Este tutorial es una guía completa para entender cómo aplicar técnicas de **Procesamiento de Lenguaje Natural (NLP)** con **PyTorch**. Aprenderemos desde los fundamentos hasta el despliegue de modelos en producción.

---

## 📌 **Estructura del tutorial**

Este tutorial se dividirá en **12 pasos** clave:

1. **Fundamentos del NLP y Deep Learning**
2. **Preparación de los Datos de Texto**
3. **Construcción de un Modelo de NLP con RNN**
4. **Mejorando con LSTM y GRU**
5. **Uso de Word Embeddings en PyTorch**
6. **Implementación de un Transformer desde Cero**
7. **Entrenamiento del Modelo en un Dataset Realista**
8. **Predicción y Evaluación del Modelo**
9. **Optimización y Fine-Tuning con Modelos Preentrenados**
10. **Mini Despliegue de un Modelo de NLP con Flask y PyTorch**
11. **Transferencia de Conocimiento entre Modelos**
12. **Retrieval-Augmented Generation (RAG)**

---

## ✅ **Paso 11: Transferencia de Conocimiento entre Modelos**

La **transferencia de conocimiento** permite reutilizar modelos preentrenados para nuevas tareas con menos datos y entrenamiento. Es una estrategia clave en **aprendizaje profundo** que optimiza el rendimiento de los modelos sin necesidad de entrenar desde cero.

### 📌 **Métodos de Transferencia de Conocimiento**

1. **Fine-Tuning Completo**: Se ajustan todas las capas del modelo preentrenado en la nueva tarea. Esto permite máxima adaptación, pero requiere más datos y tiempo de entrenamiento.
2. **Congelación de Capas**: Se mantienen congeladas las primeras capas del modelo preentrenado (que capturan características generales) y solo se ajustan las capas superiores para la nueva tarea. Esta técnica es útil cuando se tienen pocos datos.
3. **Extracción de Características**: Se usa el modelo preentrenado para extraer representaciones de los datos, sin modificar sus pesos, y se agrega una nueva capa para la tarea específica. Es la opción más eficiente en datos limitados.

Ejemplo en PyTorch de congelación de capas en un modelo basado en **BERT**:

```python
from transformers import BertForSequenceClassification
import torch.nn as nn

model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Congelar todas las capas excepto la última
for param in model.base_model.parameters():
    param.requires_grad = False

# Agregar una nueva capa de clasificación
model.classifier = nn.Linear(model.config.hidden_size, 2)
```

Además, al entrenar en un dominio específico, se pueden aplicar técnicas como **diferentes tasas de aprendizaje por capa** o **ajuste progresivo**, donde primero se entrenan las capas superiores y luego se descongelan gradualmente las inferiores.

---

## ✅ **Paso 12: Retrieval-Augmented Generation (RAG)**

**Retrieval-Augmented Generation (RAG)** es un enfoque híbrido que combina modelos generativos (como GPT) con recuperación de información externa. Esto permite que el modelo recupere información relevante de documentos o bases de datos antes de generar una respuesta, mejorando la precisión y reduciendo la generación de contenido inexacto.

### 📌 **Cómo Funciona RAG**

1. **Retrieval (Recuperación):** Se busca información relevante en bases de datos o documentos.
2. **Augmentation (Aumento):** La información recuperada se combina con la entrada del usuario.
3. **Generation (Generación):** Un modelo generativo usa la información recuperada para generar una respuesta coherente y precisa.

Ejemplo en PyTorch usando `transformers`:

```python
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import torch

# Cargar modelo RAG
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq")
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq")

# Entrada del usuario
input_text = "¿Quién escribió Don Quijote?"
inputs = tokenizer(input_text, return_tensors="pt")

# Generar respuesta
with torch.no_grad():
    generated = model.generate(**inputs)
    print(tokenizer.batch_decode(generated, skip_special_tokens=True))
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

🚀 ¡Ahora estás listo para construir modelos NLP robustos con PyTorch!