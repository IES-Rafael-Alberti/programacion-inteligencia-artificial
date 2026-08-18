// Restricciones del modelo. Ejecutar CADA sentencia completa por separado.
// No pegar una línea FOR ... aislada: falla.
CREATE CONSTRAINT movie_id IF NOT EXISTS
FOR (m:Movie) REQUIRE m.id IS UNIQUE;

CREATE CONSTRAINT genre_name IF NOT EXISTS
FOR (g:Genre) REQUIRE g.name IS UNIQUE;

CREATE CONSTRAINT director_name IF NOT EXISTS
FOR (d:Director) REQUIRE d.name IS UNIQUE;

CREATE CONSTRAINT actor_name IF NOT EXISTS
FOR (a:Actor) REQUIRE a.name IS UNIQUE;