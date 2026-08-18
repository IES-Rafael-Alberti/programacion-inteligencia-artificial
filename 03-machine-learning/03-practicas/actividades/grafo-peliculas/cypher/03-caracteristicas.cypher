// Tabla de características por película para continuar con ML.
// En Neo4j Browser: vista Table y descargar CSV (icono de la esquina superior derecha del marco de resultados).
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