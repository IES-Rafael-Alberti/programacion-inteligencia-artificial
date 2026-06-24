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
