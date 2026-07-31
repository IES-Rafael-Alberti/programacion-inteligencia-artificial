# Proyecto: Dataset de películas con TMDB + OMDb

Este proyecto forma parte del Lab1 de UD3. El flujo recomendado usa Pixi desde la raíz del repositorio PIA:

```bash
pixi install
pixi run --environment ud3-datasets lab1-dataset
```

El entorno `ud3-datasets` aporta Python 3.12, pandas, requests y python-dotenv, además de las dependencias comunes y de ML de UD3. Las claves `TMDB_API_KEY` y `OMDB_API_KEY` deben estar en un archivo `.env` local; nunca se deben subir al repositorio.

La guía completa de la actividad está en [`CreacionDataset.md`](../CreacionDataset.md). Pixi centraliza las dependencias y la ejecución reproducible de este proyecto en el archivo `pixi.toml` de la raíz del repositorio.

`lab1-dataset` genera el CSV exploratorio del laboratorio mediante emparejamiento por título, cuya ambigüedad forma parte del análisis docente. `capstone-movies-dataset` es un flujo distinto: aplica un contrato estricto y empareja TMDB con OMDb exclusivamente mediante `imdb_id`.
