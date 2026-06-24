import requests
from .config import OMDB_API_KEY

def get_omdb_data(title):
    params = {
        "apikey": OMDB_API_KEY,
        "t": title
    }
    resp = requests.get("http://www.omdbapi.com/", params=params)
    return resp.json()
