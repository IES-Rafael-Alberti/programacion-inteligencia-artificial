// Carga idempotente del fixture.
// Requiere que fixture/movies_graph.csv esté montado en el contenedor en /var/lib/neo4j/import/movies_graph.csv.
// MERGE evita duplicar nodos y relaciones al repetir la carga.
LOAD CSV WITH HEADERS FROM 'file:///movies_graph.csv' AS row
MERGE (m:Movie {id: row.movie_id})
  ON CREATE SET m.title = row.title, m.year = toInteger(row.year)
MERGE (g:Genre {name: row.genre})
MERGE (d:Director {name: row.director})
MERGE (a:Actor {name: row.actor})
MERGE (m)-[:HAS_GENRE]->(g)
MERGE (m)-[:DIRECTED_BY]->(d)
MERGE (m)-[:FEATURES]->(a);