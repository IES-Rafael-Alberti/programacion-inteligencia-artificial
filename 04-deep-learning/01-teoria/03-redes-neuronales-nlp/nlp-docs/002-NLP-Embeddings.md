---
output: 
  pdf_document:
    toc: true
    number_sections: true
    latex_engine: xelatex
---

# **Introducción a los Embeddings en Inteligencia Artificial**

## **1. ¿Qué son los embeddings?**
Los embeddings son representaciones numéricas densas de palabras, frases, imágenes o cualquier tipo de datos, que capturan relaciones semánticas y contextuales. Estas representaciones permiten que los modelos de inteligencia artificial trabajen con datos textuales o no estructurados de manera eficiente.

---

## **2. Técnicas para transformar palabras/frases en embeddings**
### **TF-IDF (Term Frequency-Inverse Document Frequency)**
- Método clásico que mide la relevancia de palabras en un documento respecto a un corpus.
- Fórmulas:
  - Frecuencia de término (TF):  
    $$ \text{TF}(t,d) = \frac{\text{número de veces que } t \text{ aparece en } d}{\text{número total de palabras en } d} $$
  - Frecuencia inversa de documento (IDF):  
    $$ \text{IDF}(t,D) = \log\left(\frac{\text{número total de documentos}}{\text{número de documentos que contienen } t}\right) $$
  - Puntuación TF-IDF:  
    $$ \text{TF-IDF}(t,d,D) = \text{TF}(t,d) \times \text{IDF}(t,D) $$

### **Word2Vec**
- Modelo predictivo que genera vectores densos mediante dos enfoques:
  - *CBOW*: Predice una palabra basada en su contexto.
  - *Skip-gram*: Predice el contexto dado una palabra.
- Ejemplo: "rey - hombre + mujer ≈ reina".

### **GloVe (Global Vectors for Word Representation)**
- Combina estadísticas globales de co-ocurrencia para capturar relaciones semánticas y sintácticas entre palabras.

### **FastText**
- Extensión de Word2Vec que considera subpalabras (n-gramas), útil para lenguajes con morfología compleja o palabras raras.

### **Transformers (BERT, GPT, etc.)**
- Generan embeddings contextuales dinámicos considerando el orden y las relaciones entre palabras.
- Ejemplo: "banco" como institución financiera vs "banco" como asiento.

---

## **3. ¿Cómo se utilizan los embeddings en modelos de inteligencia artificial?**
### Aplicaciones principales:
1. **Procesamiento de Lenguaje Natural (NLP):**
   - Análisis de sentimientos.
   - Traducción automática.
   - Búsqueda semántica.

2. **Sistemas de recomendación:**
   - Comparan embeddings de usuarios y productos para sugerencias personalizadas.

3. **Visión por computadora:**
   - Reconocimiento facial, clasificación médica o búsqueda inversa de imágenes.

4. **Clustering y detección de anomalías:**
   - Agrupamiento semántico y detección de outliers en grandes conjuntos de datos.

---

## **4. ¿Cómo facilitan los embeddings la búsqueda por significado?**
Los embeddings permiten búsquedas por significado gracias a su capacidad para representar texto como vectores numéricos que capturan relaciones semánticas. Esto se logra mediante:

1. **Proximidad semántica:**  
   Palabras/frases similares se ubican cerca en el espacio vectorial (ejemplo: "feliz" y "alegre").

2. **Medidas matemáticas:**  
   La similitud entre vectores se calcula utilizando métricas como el coseno del ángulo entre ellos.

3. **Contexto dinámico:**  
   Modelos como BERT generan representaciones contextuales que entienden el significado según el entorno.

---

## **5. Comparación entre embeddings de palabras y oraciones**
| Aspecto                | Embeddings de palabras         | Embeddings de oraciones             |
|------------------------|---------------------------------|-------------------------------------|
| Contexto               | Estático (por palabra)         | Dinámico (por secuencia completa)  |
| Orden gramatical       | No aplica                      | Poca sensibilidad                  |
| Negaciones             | No capturadas                 | Mínimo impacto                     |
| Uso óptimo             | Diccionarios, traducción básica | Búsqueda semántica, clasificación |

Los embeddings de oraciones amplían las capacidades semánticas pero enfrentan limitaciones al capturar transformaciones gramaticales como negaciones o cambios temporales.

---

## **6. Librerías populares para trabajar con embeddings**

### Python:
1. **Gensim**: Para trabajar con Word2Vec, FastText y modelos similares.
   ```python
   from gensim.models import Word2Vec
   sentences = [["gato", "juega", "con", "ratón"], ["perro", "corre", "rápido"]]
   model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)
   print(model.wv['gato'])  # Vector del término 'gato'
   ```

2. **TensorFlow/Keras**: Para implementar capas de embeddings.
   ```python
   from tensorflow.keras.layers import Embedding
   embedding_layer = Embedding(input_dim=1000, output_dim=64)
   ```

3. **Hugging Face Transformers**: Para usar modelos preentrenados como BERT o GPT.
   ```python
   from transformers import AutoTokenizer, AutoModel
   tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
   model = AutoModel.from_pretrained("bert-base-uncased")
   inputs = tokenizer("El gato juega con el ratón", return_tensors="pt")
   outputs = model(**inputs)
   print(outputs.last_hidden_state)
   ```

4. **Scikit-learn**: Para generar representaciones TF-IDF.
   ```python
   from sklearn.feature_extraction.text import TfidfVectorizer
   corpus = ["El gato juega con el ratón", "El perro corre rápido"]
   vectorizer = TfidfVectorizer()
   X = vectorizer.fit_transform(corpus)
   print(X.toarray())  # Matriz TF-IDF
   ```

---

## **7. Ejemplo práctico: Búsqueda semántica con embeddings**

```python
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Modelo preentrenado para generar embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Frases a comparar
query = "El gato juega con el ratón"
documents = ["El perro corre rápido", "El felino juega con su presa"]

# Generar embeddings
query_embedding = model.encode(query)
doc_embeddings = model.encode(documents)

# Calcular similitudes coseno
similarities = cosine_similarity([query_embedding], doc_embeddings)
print(similarities)  # Similitudes entre la consulta y los documentos
```

---

## **8. Libros recomendados para aprender embeddings desde cero**

### **1. [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python-second-edition) - François Chollet**
- Enfoque práctico con ejemplos claros sobre cómo usar capas de embeddings en Keras.
- Ideal para principiantes que quieren aprender desde cero con aplicaciones reales.

### **2. [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125974/) - Aurélien Géron**
- Explica cómo implementar embeddings en proyectos prácticos usando TensorFlow/Keras.
- Incluye tareas como clasificación textual y búsqueda semántica.

### **3. [Natural Language Processing with PyTorch](https://www.oreilly.com/library/view/natural-language-processing/9781491978238/) - Delip Rao & Brian McMahon**
- Enfocado completamente en NLP, con ejemplos detallados sobre Word2Vec, GloVe, FastText y BERT usando PyTorch.

### **4. [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) - Daniel Jurafsky & James H. Martin**
- Cobertura teórica sólida sobre representaciones distribuidas y su evolución desde TF-IDF hasta Transformers.

---

## **9. Bibliografía**

1. Mikolov et al., *Efficient Estimation of Word Representations in Vector Space* (2013).  
2. Pennington et al., *GloVe: Global Vectors for Word Representation* (2014).  
3. Vaswani et al., *Attention is All You Need* (2017).  
4. François Chollet, *Deep Learning with Python* (Manning Publications).  
5. Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (O'Reilly Media).

---

Este documento combina teoría básica, ejemplos prácticos y bibliografía relevante para enseñar sobre embeddings desde cero hasta aplicaciones avanzadas en Python e IA moderna. ¡Perfecto para tus clases! 😊

---
Respuesta de Perplexity: pplx.ai/share
