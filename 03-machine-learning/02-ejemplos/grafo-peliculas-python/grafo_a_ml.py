"""Del grafo de películas a una tabla para ML (apéndice de grafos de UD3).

Demuestra la ruta programática del apéndice: consultar Neo4j desde Python con el
driver oficial, convertir el resultado a pandas y alimentar un modelo de
scikit-learn con características derivadas del grafo.

El servidor Neo4j no se instala con este script: debe estar corriendo aparte
(contenedor Docker). Las credenciales se leen de variables de entorno.
"""

import os
import sys

import pandas as pd
from neo4j import GraphDatabase
from sklearn.cluster import KMeans

URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
USER = os.environ.get("NEO4J_USER", "neo4j")
PASSWORD = os.environ.get("NEO4J_PASSWORD")

FEATURES_QUERY = """
MATCH (m:Movie)
OPTIONAL MATCH (m)-[:HAS_GENRE]->(g:Genre)
WITH m, count(DISTINCT g) AS genre_count
OPTIONAL MATCH (m)-[:FEATURES]->(a:Actor)
WITH m, genre_count, count(DISTINCT a) AS actor_count
OPTIONAL MATCH (m)-[:DIRECTED_BY]->(d:Director)
RETURN m.id AS movie_id,
       m.title AS title,
       m.year AS year,
       genre_count,
       actor_count,
       count(DISTINCT d) AS director_count
ORDER BY movie_id;
"""


def main():
    if not PASSWORD:
        print(
            "Falta NEO4J_PASSWORD. Define NEO4J_URI, NEO4J_USER y NEO4J_PASSWORD "
            "(las credenciales nunca se escriben en el código).",
            file=sys.stderr,
        )
        return 2

    print(f"Conectando a {URI} como {USER} ...")
    try:
        with GraphDatabase.driver(URI, auth=(USER, PASSWORD)) as driver:
            driver.verify_connectivity()
            records, _, _ = driver.execute_query(FEATURES_QUERY, database_="neo4j")
    except Exception as exc:
        print(f"No se pudo conectar a Neo4j: {exc}", file=sys.stderr)
        print(
            "Comprueba que el contenedor está arrancado: "
            "`docker ps --filter name=neo4j-movies`",
            file=sys.stderr,
        )
        return 1

    df = pd.DataFrame([record.data() for record in records])
    print("\nCaracterísticas derivadas del grafo:")
    print(df.to_string(index=False))

    features = df[["year", "genre_count", "actor_count", "director_count"]]
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(features)

    print("\nAgrupación (KMeans, 2 clústeres) sobre las características del grafo:")
    print(df[["movie_id", "title", "cluster"]].to_string(index=False))

    print(
        "\nSiguiente paso: estas columnas (genre_count, actor_count, director_count) "
        "pueden unirse con la variable objetivo del capstone y alimentar un "
        "clasificador como el de P3, documentando su procedencia desde el grafo."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
