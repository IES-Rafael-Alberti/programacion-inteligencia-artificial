# 🎬 Actividad Práctica: Construcción de un Dataset de Películas con TMDB + OMDb

**Objetivo:** Aprender a consumir dos APIs distintas (TMDB y OMDb), fusionar sus datos en un dataset común, procesarlo y guardarlo de forma estructurada. Todo el flujo estará contenido en un proyecto Poetry.

---

## 🔧 Requisitos previos

* Tener instalado Python 3.10 o superior
* Tener instalado Poetry
* Cuenta creada en TMDB para obtener una API Key:
  👉 [https://developer.themoviedb.org/signup](https://developer.themoviedb.org/signup)
* Clave gratuita de OMDb API:
  👉 [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)

---

## 🧱 Estructura del proyecto

```bash
mi_dataset_peliculas/
├── data/                     # Aquí se guardarán los CSV
├── notebooks/                # Experimentos opcionales
├── src/
│   └── mi_dataset_peliculas/
│       ├── tmdb.py           # Código para TMDB
│       ├── omdb.py           # Código para OMDb
│       ├── merge.py          # Fusionar datos
│       └── build_dataset.py  # Script principal
├── pyproject.toml            # Configuración de Poetry
└── README.md
```

---

## 📦 Paso 1 – Crear el proyecto

```bash
poetry new mi_dataset_peliculas --src
cd mi_dataset_peliculas
poetry add requests pandas
```

---

## 🔑 Paso 2 – Configurar claves API

Crea un archivo `.env` (o un módulo `config.py` temporal) para guardar tus claves:

```python
# src/mi_dataset_peliculas/config.py
TMDB_API_KEY = "tu_api_key_tmdb"
OMDB_API_KEY = "tu_api_key_omdb"
```

---

## 🌐 Paso 3 – Consultar TMDB

```python
# src/mi_dataset_peliculas/tmdb.py
import requests
from .config import TMDB_API_KEY

def get_popular_movies(page=1):
    url = f"https://api.themoviedb.org/3/movie/popular"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "es-ES",
        "page": page
    }
    resp = requests.get(url, params=params)
    return resp.json()["results"]
```

---

## 🍿 Paso 4 – Consultar OMDb

```python
# src/mi_dataset_peliculas/omdb.py
import requests
from .config import OMDB_API_KEY

def get_omdb_data(title):
    params = {
        "apikey": OMDB_API_KEY,
        "t": title
    }
    resp = requests.get("http://www.omdbapi.com/", params=params)
    return resp.json()
```

---

## 🔗 Paso 5 – Combinar información

```python
# src/mi_dataset_peliculas/merge.py
def merge_tmdb_omdb(tmdb_list, omdb_getter):
    result = []
    for movie in tmdb_list:
        omdb = omdb_getter(movie['title'])
        if omdb.get('Response') == 'True':
            movie_data = {
                "title": movie["title"],
                "release_date": movie.get("release_date"),
                "vote_average": movie.get("vote_average"),
                "runtime": omdb.get("Runtime"),
                "director": omdb.get("Director"),
                "imdb_rating": omdb.get("imdbRating")
            }
            result.append(movie_data)
    return result
```

---

## 🧰 Paso 6 – Construir y guardar el dataset

```python
# src/mi_dataset_peliculas/build_dataset.py
from .tmdb import get_popular_movies
from .omdb import get_omdb_data
from .merge import merge_tmdb_omdb
import pandas as pd

tmdb_movies = get_popular_movies(page=1)
merged_data = merge_tmdb_omdb(tmdb_movies, get_omdb_data)

df = pd.DataFrame(merged_data)
df.to_csv("data/dataset_peliculas.csv", index=False)
print("✅ Dataset guardado correctamente.")
```

---

## 🚀 Paso 7 – Ejecutar

```bash
poetry run python src/mi_dataset_peliculas/build_dataset.py
```

---

## 🎯 Tarea para el alumnado

1. Completar los módulos `tmdb.py` y `omdb.py`
2. Probar a obtener datos de varias páginas (cambiar parámetro `page`)
3. Añadir columnas extra como `actors`, `genre`, `plot`, `poster_url`
4. Realizar análisis con pandas o seaborn sobre el CSV resultante
5. (Opcional) Servir el dataset con FastAPI desde el mismo proyecto

---

¿Quieres que genere directamente esta plantilla como proyecto descargable con `pyproject.toml`, carpetas y archivos base?
