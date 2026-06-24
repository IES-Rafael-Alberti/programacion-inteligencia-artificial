from .tmdb import get_popular_movies
from .omdb import get_omdb_data
from .merge import merge_tmdb_omdb
import pandas as pd

tmdb_movies = get_popular_movies(page=1)
merged_data = merge_tmdb_omdb(tmdb_movies, get_omdb_data)

df = pd.DataFrame(merged_data)
df.to_csv("data/dataset_peliculas.csv", index=False)
print("✅ Dataset guardado correctamente.")
