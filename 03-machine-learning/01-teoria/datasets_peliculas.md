# Fuentes de datos abiertas para construir un dataset de películas

Existen varias fuentes de datos abiertas y actualizadas que cumplen con los criterios solicitados (acceso **gratuito**, formato **API/CSV**, activas en 2025) para crear datasets de películas. A continuación se presentan **5 fuentes viables**, con sus enlaces y características clave:

## 1. The Movie Database (TMDB)

- **Enlace:** https://www.themoviedb.org/documentation/api
- **Datos ofrecidos:** Títulos, sinopsis, fechas de estreno, reparto, equipo, imágenes promocionales (pósters, fondos), géneros, idiomas, compañías productoras.
- **Acceso:** Gratuito. Requiere registro para obtener una clave API personal. Respuestas en formato JSON vía REST API.
- **Integración:** Moderada. Fácilmente consumible desde `requests` o `httpx` en Python. Librerías cliente disponibles.
- **Ventajas educativas:** Base de datos completa y multilingüe. Ideal para ejercicios de EDA con metadatos, relaciones entre películas y artistas, y análisis temático o temporal. Incluye imágenes y estructura limpia.

## 2. OMDb API (Open Movie Database)

- **Enlace:** https://www.omdbapi.com/
- **Datos ofrecidos:** Trama, año, duración, géneros, director, reparto, puntuaciones (IMDb, Rotten Tomatoes, Metacritic), imágenes.
- **Acceso:** Gratuito con registro (requiere email). Respuestas en JSON.
- **Integración:** Muy sencilla. Consultas rápidas a través de una URL. Ideal para usar con `requests` y procesar con pandas.
- **Ventajas educativas:** Perfecta para iniciación al uso de APIs REST. Respuestas simples y útiles para EDA de ratings o metadatos.

## 3. MovieLens (GroupLens datasets)

- **Enlace:** https://grouplens.org/datasets/movielens/
- **Datos ofrecidos:** Valoraciones de usuarios reales. Versiones disponibles desde 100K hasta 32 millones de ratings sobre ~87K películas. Incluye `movies.csv`, `ratings.csv`, `tags.csv`.
- **Acceso:** Descarga directa en ZIP/CSV. Sin necesidad de autenticación.
- **Integración:** Muy fácil. Compatible con pandas. Ideal para trabajar con ratings, sistemas de recomendación, y análisis de usuarios.
- **Ventajas educativas:** Datasets reales, bien estructurados y ampliamente utilizados en entornos académicos. Ejercicios completos de análisis, merging, y modelado colaborativo.

## 4. Kaggle Datasets (Ejemplo: The Movies Dataset)

- **Enlace:** https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
- **Datos ofrecidos:** Metadatos de ~45K películas, datos de reparto, equipo, palabras clave, compañías, presupuesto, recaudación, ratings de usuarios.
- **Acceso:** Gratuito con cuenta de Kaggle. Descarga directa o vía API.
- **Integración:** Sencilla. Requiere unificación de archivos (películas + ratings + cast/crew). Compatible con pandas.
- **Ventajas educativas:** Excelente para proyectos de ciclo completo. Documentado, acompañado de notebooks y permite tareas desde limpieza hasta sistemas de recomendación.

## 5. Wikidata

- **Enlace:** https://www.wikidata.org/wiki/Wikidata:Main_Page / https://query.wikidata.org/
- **Datos ofrecidos:** Títulos en múltiples idiomas, año de estreno, reparto, directores, premios, género, país, ingresos, enlaces a otras bases de datos (IMDb, TMDB, etc.).
- **Acceso:** Abierto y gratuito. Consultas vía SPARQL (servicio web). También se ofrecen dumps completos.
- **Integración:** Requiere familiaridad con SPARQL o uso de librerías como `SPARQLWrapper` en Python. Respuestas JSON o CSV.
- **Ventajas educativas:** Ideal para introducir datos enlazados y estructurados. Permite enriquecer datasets con información externa. Licencia libre, sin restricciones de uso.

---

Estas fuentes permiten construir datasets personalizados o enriquecer otros ya existentes. Cada una tiene ventajas específicas para el aula, desde aprendizaje técnico de APIs hasta análisis reales de datos cinematográficos complejos.

