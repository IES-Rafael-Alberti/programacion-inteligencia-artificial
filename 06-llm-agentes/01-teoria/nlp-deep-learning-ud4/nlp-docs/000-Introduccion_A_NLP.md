# 🧠 FASE 1 — Introducción al NLP

## De texto a números (Bag of Words y TF-IDF)

---

# 🎯 Objetivo de la unidad

En esta unidad aprenderás:

* qué es el **Procesamiento de Lenguaje Natural (NLP)**
* cómo convertir texto en datos numéricos
* cómo aplicar un modelo de clasificación sobre texto
* por qué los métodos clásicos tienen limitaciones

---

# 1️⃣ ¿Qué es NLP?

El **Procesamiento de Lenguaje Natural (NLP)** es la rama de la IA que trabaja con texto.

Ejemplos:

* análisis de sentimiento (positivo/negativo)
* clasificación de noticias
* detección de spam
* chatbots

---

# 2️⃣ Problema fundamental

Los modelos de Machine Learning trabajan con números, no con texto.

Por tanto, necesitamos transformar:

```text
"Me encanta este curso"
```

en algo como:

```text
[0, 1, 0, 3, 0, ...]
```

---

# 3️⃣ Conceptos básicos

## 📌 Documento

Un texto individual.

## 📌 Corpus

Conjunto de documentos.

## 📌 Token

Unidad mínima (normalmente palabra).

Ejemplo:

```text
"Me gusta la IA"
→ ["me", "gusta", "la", "ia"]
```

## 📌 Vocabulario

Conjunto de palabras únicas.

---

# 4️⃣ Preprocesado básico

Antes de convertir texto en números, se suele limpiar.

Operaciones típicas:

* pasar a minúsculas
* eliminar signos de puntuación
* eliminar palabras vacías (stopwords)

Ejemplo:

```text
"¡Me encanta la IA!"
→ ["encanta", "ia"]
```

⚠️ Nota: En NLP moderno, este preprocesado es menos agresivo.

---

# 5️⃣ Representación 1: Bag of Words

Idea:

> contar cuántas veces aparece cada palabra

---

## Ejemplo

Corpus:

```text
Doc1: "me gusta la ia"
Doc2: "la ia es interesante"
```

Vocabulario:

```text
["me", "gusta", "la", "ia", "es", "interesante"]
```

Representación:

```text
Doc1 → [1,1,1,1,0,0]
Doc2 → [0,0,1,1,1,1]
```

---

## Problema

* no tiene en cuenta el orden
* todas las palabras pesan igual

---

# 6️⃣ Representación 2: TF-IDF

TF-IDF mejora Bag of Words.

Idea:

> palabras importantes en un documento, pero no en todos

---

## Ejemplo intuitivo

Palabra: “el”

* aparece en todos los documentos → poco útil

Palabra: “transformer”

* aparece poco pero es relevante → más peso

---

# 7️⃣ Pipeline completo NLP clásico

```text
Texto
↓
Preprocesado
↓
Vectorización (BoW / TF-IDF)
↓
Modelo (clasificador)
↓
Predicción
```

---

# 8️⃣ Dataset 1 — Español

Ejemplo:

* noticias clasificadas por categoría
* reseñas en español
* titulares

Objetivo:

```text
clasificar texto en categorías
```

---

# 9️⃣ Dataset 2 — Inglés

Ejemplo:

* SMS spam
* 20 Newsgroups
* IMDb

Objetivo:

```text
clasificar spam / no spam o categorías
```

---

# 🔟 Modelo de clasificación

Modelos típicos en NLP clásico:

* Naive Bayes
* Logistic Regression
* SVM

---

## Ejemplo conceptual

```text
Texto → TF-IDF → Modelo → Predicción
```

---

# 1️⃣1️⃣ Métricas

Para evaluar:

* accuracy
* matriz de confusión
* precision / recall

---

# 1️⃣2️⃣ Limitaciones del enfoque clásico

Los métodos vistos tienen problemas:

❌ no entienden contexto
❌ no entienden orden de palabras
❌ no capturan significado

Ejemplo:

```text
"no me gusta"
"me gusta"
```

pueden parecer similares.

---

# 1️⃣3️⃣ Conexión con lo que viene

Esto nos lleva a la siguiente fase:

```text
Bag of Words / TF-IDF
↓
Embeddings
↓
Transformers
```

---

# 💡 Idea clave de la unidad

> En NLP, lo más importante no es el modelo,
> sino **cómo representamos el texto**.

---

# 🧪 Actividades propuestas

1. Limpiar y tokenizar textos
2. Aplicar Bag of Words
3. Aplicar TF-IDF
4. Entrenar un clasificador
5. Comparar resultados entre datasets
6. Analizar errores

---

# 📌 Conclusión

* El texto debe convertirse en números
* TF-IDF mejora Bag of Words
* los modelos clásicos funcionan… pero tienen límites
* necesitamos mejores representaciones → embeddings
