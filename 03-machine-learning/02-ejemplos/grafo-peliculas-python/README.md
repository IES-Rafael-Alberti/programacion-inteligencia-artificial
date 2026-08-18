# Neo4j desde Python: del grafo a una tabla para ML

Este ejemplo es la **ruta programática** del [apéndice de dataset como grafo](../../01-teoria/apendice-dataset-grafos.md). El módulo se llama Programación de IA: la interfaz web de Neo4j (Browser) sirve para la demostración visual, pero el fin último es consultar el grafo **desde un programa** y usar las características resultantes con modelos de ML.

## Requisitos

1. Contenedor Neo4j arrancado con el fixture cargado (ver apéndice, secciones 1 y 2).
2. Entorno Pixi `ud3-graph`, que añade el driver oficial `neo4j` (paquete conda-forge `neo4j-python-driver`) sin tocarlo en el entorno común:

```bash
pixi install --environment ud3-graph
```

## Ejecución

Desde la raíz del repositorio, con el servidor Neo4j en marcha:

```bash
NEO4J_URI=bolt://localhost:7687 \
NEO4J_USER=neo4j \
NEO4J_PASSWORD=course-only-password \
pixi run --environment ud3-graph python 03-machine-learning/02-ejemplos/grafo-peliculas-python/grafo_a_ml.py
```

Las credenciales van por variables de entorno, nunca en el código. `NEO4J_URI` y `NEO4J_USER` tienen valores por defecto (`bolt://localhost:7687` y `neo4j`).

## Qué demuestra

1. Conexión al servidor con `GraphDatabase.driver` y `verify_connectivity()`.
2. Consulta de la tabla de características (géneros, actores, directores por película) con Cypher.
3. Conversión de los resultados a `pandas.DataFrame`.
4. Uso de esas características con un modelo de scikit-learn (`KMeans`) para agrupar las películas.

En un proyecto real, las columnas derivadas del grafo se unirían con la variable objetivo del capstone y alimentarían un clasificador como el de P3, siempre documentando su procedencia desde el grafo.

## Salida esperada (fixture de 4 películas)

Las características deben coincidir con las del apéndice:

```
movie_id  title               year  genre_count  actor_count  director_count
m1        Arrival             2016  1            2            1
m2        Dune                2021  1            2            1
m3        The Godfather       1972  2            1            1
m4        Lost in Translation 2003  1            2            1
```

La asignación de clústeres es un ejemplo didáctico (con `random_state=42` es reproducible), no un resultado docente.

## Límites

- No instala el servidor Neo4j: el driver solo habla con el que ya esté corriendo.
- No añade la dependencia al entorno común de UD3: `ud3-graph` queda aislado para quien haga la ampliación.
- No sustituye el uso directo de Cypher en Browser como introducción visual al grafo.