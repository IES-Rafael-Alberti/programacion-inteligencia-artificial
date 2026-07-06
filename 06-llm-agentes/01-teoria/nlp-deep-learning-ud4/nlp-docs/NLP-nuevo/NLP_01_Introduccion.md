# 🧠 Introducción al Procesamiento de Lenguaje Natural (NLP)

## 🎯 ¿Qué vamos a hacer en esta unidad?

En esta unidad vamos a trabajar con un tipo de datos diferente a los que hemos visto hasta ahora:

👉 **texto**

Nuestro objetivo será:

- entender cómo se representa el texto para poder trabajar con él
- construir un primer modelo de clasificación
- detectar las limitaciones de estos enfoques

## 🧩 El problema: los modelos no entienden texto

Imagina que queremos trabajar con esta frase:

`"Me encanta este curso"`

Un modelo de Machine Learning no puede trabajar con texto directamente.

Necesita números.

## 🔁 Primera transformación: texto → tokens

Antes de convertir a números, descomponemos el texto.

Esto se llama **tokenización**.

`"Me encanta este curso" → ["me", "encanta", "este", "curso"]`

Aquí aparecen algunos conceptos importantes:

- **Documento** → un texto
- **Corpus** → conjunto de textos
- **Token** → unidad mínima (palabra normalmente)

## 🧹 Limpieza del texto (preprocesado)

En muchos casos, antes de trabajar con texto:

- pasamos todo a minúsculas
- eliminamos signos de puntuación
- quitamos palabras poco relevantes

Ejemplo:

`"¡Me encanta la IA!" → ["encanta", "ia"]`

⚠️ Importante: esto no siempre se hace en NLP moderno, pero nos sirve para entender lo básico.

## 🔢 Segunda transformación: tokens → números

Aquí está el punto clave de toda la unidad:

👉 ¿Cómo representamos texto como números?

## 📦 Representación 1: Bag of Words

La primera idea útil es muy simple: construir un vocabulario con las palabras que aparecen en nuestro corpus y contar cuántas veces aparece cada una en cada documento.

### Ejemplo

Corpus:

- Doc1: `"me gusta la ia"`
- Doc2: `"la ia es interesante"`

Vocabulario:

`["me", "gusta", "la", "ia", "es", "interesante"]`

Representación:

- Doc1 → `[1,1,1,1,0,0]`
- Doc2 → `[0,0,1,1,1,1]`

De esta forma, cada texto queda transformado en un vector numérico.

## ⚠️ Problemas de Bag of Words

Aunque funciona, tiene limitaciones importantes:

- no tiene en cuenta el orden de las palabras
- todas las palabras pesan igual
- no entiende significado ni contexto

Por ejemplo, para este sistema no es tan evidente diferenciar entre frases que comparten casi las mismas palabras, aunque signifiquen cosas distintas.

## 📦 Representación 2: TF-IDF

TF-IDF mejora Bag of Words.

La idea ya no es solo contar palabras, sino dar más peso a las que son importantes en un documento y menos a las que aparecen en casi todos.

TF-IDF (Term Frequency - Inverse Document Frequency) es una medida que evalúa la importancia de una palabra en un documento dentro de una colección.

### Intuición

Palabras como:

- “el”, “la”, “de”

aparecen en muchos documentos y suelen aportar poca información.

En cambio, palabras como:

- “transformer”, “modelo”, “entrenamiento”

pueden ser mucho más informativas.

Por tanto, TF-IDF intenta reflejar esa diferencia en los valores numéricos.

Cálculo:
TF(t,d) = (nº de veces que t aparece en d) / (nº total de términos en d)
IDF(t) = log(Total documentos / Documentos que contienen t)
TF-IDF(t,d) = TF(t,d) × IDF(t)
Ejemplo:
- Documentos: "el gato come", "el perro duerme"
- TF("el", doc1) = 1/3 ≈ 0.33
- IDF("el") = log(2/2) = 0
- TF-IDF("el") = 0 (palabra común en todos los docs)
Interpretación:
- TF-IDF alto → palabra importante (frecuente en este doc, rara en otros)
- TF-IDF bajo → palabra común o irrelevante

## 🔄 Pipeline completo de NLP clásico

Con todo lo anterior ya podemos describir el flujo completo de un primer sistema de NLP clásico:

1. Partimos del texto.
2. Lo limpiamos o preprocesamos.
3. Lo convertimos en vectores con Bag of Words o TF-IDF.
4. Entrenamos un modelo de clasificación.
5. Hacemos predicciones.

## 🤖 Modelos que vamos a usar

Una vez el texto está representado como números, ya podemos aplicar modelos tradicionales de Machine Learning, por ejemplo:

- Naive Bayes
- Logistic Regression
- SVM

En esta fase inicial nos interesa más entender el pipeline que complicarnos con muchos modelos distintos.

## 📊 Evaluación

Para saber si el sistema funciona, necesitaremos algunas métricas básicas:

- **accuracy**
- **matriz de confusión**
- **precision / recall**

No basta con entrenar: hay que medir y analizar.

## 🚧 Limitaciones importantes

Estos métodos permiten construir sistemas útiles, pero tienen una limitación de fondo:

👉 **no entienden realmente el lenguaje**

Por ejemplo, frases como:

- `"me gusta"`
- `"no me gusta"`

pueden parecer demasiado parecidas si solo miramos qué palabras aparecen.

Ahí es donde empiezan a quedarse cortos los métodos clásicos.

## 🔗 ¿Qué viene después?

Este problema nos lleva a la siguiente evolución natural dentro de NLP:

`TF-IDF → Embeddings → Deep Learning → Transformers`

Es decir:

- primero representamos texto con técnicas clásicas
- después aprendemos representaciones más ricas
- finalmente usamos modelos que capturan contexto mucho mejor

## 💡 Idea clave de la unidad

> En NLP, muchas veces lo decisivo no es solo el modelo,
> sino **cómo representamos el texto**.

Si la representación es pobre, el modelo tendrá límites muy claros.
Si la representación mejora, el sistema también mejora.
