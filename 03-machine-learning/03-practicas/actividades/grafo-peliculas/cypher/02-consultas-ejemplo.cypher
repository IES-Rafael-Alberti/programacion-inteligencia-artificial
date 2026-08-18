// Comprobación de idempotencia: debe devolver 4 antes y después de repetir la carga.
MATCH (m:Movie)
RETURN count(m) AS movies;

// Películas de un género.
MATCH (m:Movie)-[:HAS_GENRE]->(g:Genre {name: 'Science Fiction'})
RETURN m.id, m.title, m.year
ORDER BY m.year;

// Directores y número de películas.
MATCH (d:Director)<-[:DIRECTED_BY]-(m:Movie)
RETURN d.name AS director, count(m) AS movies
ORDER BY movies DESC, director;

// Colaboraciones entre actores.
MATCH (a1:Actor)<-[:FEATURES]-(m:Movie)-[:FEATURES]->(a2:Actor)
WHERE a1.name < a2.name
RETURN a1.name AS actor_1, a2.name AS actor_2, count(DISTINCT m) AS shared_movies
ORDER BY shared_movies DESC, actor_1, actor_2;

// Películas conectadas por género y director.
MATCH (m1:Movie)-[:HAS_GENRE]->(g:Genre)<-[:HAS_GENRE]-(m2:Movie),
      (m1)-[:DIRECTED_BY]->(d:Director)<-[:DIRECTED_BY]-(m2)
WHERE m1.id < m2.id
RETURN m1.title AS movie_1, m2.title AS movie_2,
       g.name AS shared_genre, d.name AS shared_director;