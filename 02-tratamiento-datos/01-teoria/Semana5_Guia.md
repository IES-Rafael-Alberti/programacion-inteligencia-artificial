# 📖 Guía Semana 5 - Programación de Inteligencia Artificial

## Objetivos de Aprendizaje
- Introducir **Polars** como alternativa moderna y rápida a pandas.
- Comprender operaciones básicas de manipulación de datos: creación de DataFrames, selección, joins y groupby.
- Iniciar el trabajo con **Procesamiento de Lenguaje Natural (NLP)** usando **NLTK**.
- Practicar tokenización, stopwords, stemming y conteo de frecuencias.
- Relacionar el análisis de texto con pequeñas visualizaciones.

---

## Contenido de los Notebooks

### 📘 15_polars_intro.ipynb
- Introducción a **Polars**.
- Comparación rápida con pandas.
- Creación de DataFrames y operaciones básicas.

### 📘 16_polars_operaciones.ipynb
- Selección de columnas y filas.
- Filtrado y joins entre tablas.
- Agrupaciones (`groupby`) y operaciones con pipelines **lazy**.

### 📘 17_nlp_nltk_basico.ipynb
- Tokenización básica en español.
- Eliminación de stopwords.
- Stemming (reducción de palabras a su raíz).

### 📘 18_nlp_frecuencias_visualizacion.ipynb
- Construcción de un corpus pequeño.
- Limpieza y conteo de palabras.
- Visualización de frecuencias con gráficos sencillos.

---

## Metodología de la Semana
- Trabajo práctico en notebooks con ejemplos guiados.
- Comparar siempre con lo aprendido en pandas para ver las ventajas/diferencias.
- Aplicar NLTK a textos cortos en español para practicar.
- Discusión en clase sobre cómo la representación de texto influye en los modelos de IA.

---

## Criterios de Evaluación Relacionados
- **RA1**: Caracterización de lenguajes y herramientas de programación (comparación pandas vs Polars).
- **RA2**: Desarrollo de aplicaciones de IA con entornos de modelado (uso de NLTK para NLP).
- Se evaluará la **capacidad de manipular datos** con Polars y **analizar texto** con NLTK.

---

## Actividad Recomendada
- Tomar un conjunto de frases en español (mínimo 10) e implementar:
  1. Tokenización con NLTK.
  2. Limpieza eliminando stopwords.
  3. Conteo de frecuencias de palabras más comunes.
  4. Una pequeña visualización de barras con `matplotlib`.

---

## Lecturas y Recursos Sugeridos
- Documentación oficial de [Polars](https://pola-rs.github.io/polars/py-polars/html/).
- NLTK Book (capítulos introductorios): [NLTK Book](https://www.nltk.org/book/).
- Apuntes de clase sobre pandas y comparación con Polars.
