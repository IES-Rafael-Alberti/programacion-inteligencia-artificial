# Contrato del dataset docente `movies.csv`

Este contrato define el único snapshot local que consumen P1, P2 y P3. El CSV
no se versiona; `movies.manifest.json` permite comprobar exactamente qué
snapshot validado se entregó.

## Crear el snapshot

1. Copia `03-machine-learning/03-practicas/laboratorios/Lab1/mi_dataset_peliculas/.env.example`
   como `.env` en esa misma carpeta y completa `TMDB_API_KEY` y `OMDB_API_KEY`.
2. Desde la raíz del repositorio, ejecuta:

   ```bash
   pixi install --environment ud3-datasets
   pixi run --environment ud3-datasets capstone-movies-dataset
   ```

3. Revisa el mensaje de validación y `movies.manifest.json`. Solo entonces
   distribuye `data/movies.csv` junto con ese manifiesto.

Las claves permanecen en `.env`, que está ignorado por Git. No se pasan por
argumentos, no se escriben en el CSV y no aparecen en el manifiesto.

El snapshot y el manifiesto deben escribirse dentro del repositorio. El comando rechaza rutas externas antes de consultar las API o crear archivos.

## Procedencia y emparejamiento

| Aspecto | Decisión |
|---|---|
| Fuente principal | TMDB API v3, `discover/movie` ordenado por popularidad. |
| Enriquecimiento y etiqueta | OMDb API. |
| Clave de emparejamiento | Solo `imdb_id`, obtenido de `external_ids` de TMDB. Nunca título/año. |
| Snapshot | `data/movies.csv`, local y no versionado. |
| Evidencia versionable | `movies.manifest.json`: parámetros, esquema, recuentos, distribución, SHA-256 y fecha. |

## Esquema y objetivo

| Columna | Tipo | Uso |
|---|---|---|
| `release_year` | entero | Predictor. |
| `runtime_minutes` | entero | Predictor. |
| `budget_usd` | entero | Predictor; `0` significa presupuesto no informado. |
| `genres` | texto separado por `|` | Predictor categórico multilabel. |
| `original_language` | texto | Predictor. |
| `production_countries_count` | entero | Predictor. |
| `production_companies_count` | entero | Predictor. |
| `is_collection` | 0/1 | Predictor. |
| `adult` | 0/1 | Control de adquisición; con `include_adult=false` es constante y no aporta señal predictiva. |
| `rating_high` | 0/1 | Objetivo: `1` cuando OMDb informa `imdbRating >= 7.0`. |

`imdb_rating` se consulta solo para construir `rating_high` y no se conserva.
Tampoco se incluyen `vote_average`, `vote_count`, títulos ni identificadores:
son métricas posteriores, fugas potenciales o identificadores de alta
cardinalidad, no predictores del capstone.

## Validación automática

Antes de escribir el snapshot, el pipeline exige: esquema exacto, mínimo 100
filas (ajustable), cero nulos, cero filas duplicadas, rangos plausibles,
variables binarias válidas y ambas clases con una proporción mínima del 20 %.
El manifiesto registra tanto los descartes como la distribución final.

## Limitaciones del muestreo

- TMDB se consulta por popularidad: el snapshot representa películas visibles en ese criterio y no una muestra aleatoria del catálogo. Las conclusiones no deben generalizarse a todo el cine.
- La consulta excluye contenido adulto (`include_adult=false`), por lo que `adult` queda constante en el snapshot actual. Se conserva como evidencia del filtro de adquisición, pero no debe interpretarse como predictor útil.
- La popularidad cambia mientras se recorren páginas; el pipeline deduplica por `tmdb_id` y registra esos descartes en el manifiesto.

Para comprobar el contrato sin claves ni red:

```bash
pixi run --environment ud3-datasets python -m unittest \
  03-machine-learning/03-practicas/laboratorios/Lab1/mi_dataset_peliculas/tests/test_capstone_dataset.py
```

## Repetición controlada

El comando predeterminado consulta 10 páginas de TMDB. Para una reconstrucción
con otro tamaño, deja documentado el cambio en el manifiesto:

```bash
pixi run --environment ud3-datasets capstone-movies-dataset --pages 15
```

No sustituyas el snapshot sin volver a ejecutar P2 y P3: la nueva composición
de datos puede cambiar el balance, las columnas válidas y las conclusiones.
