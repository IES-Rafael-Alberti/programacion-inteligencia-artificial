# Mini-tarea — Representar un dataset de películas como grafo

**Ampliación opcional de UD3 · ~50 minutos · Actividad formativa (no evalúa P1/P2/P3)**

Contexto: tras la demostración del profesorado, el grafo de películas ya está cargado en Neo4j con el fixture de 4 películas. El grafo tiene estos nodos y relaciones:

```text
(Movie)-[:HAS_GENRE]->(Genre)
(Movie)-[:DIRECTED_BY]->(Director)
(Movie)-[:FEATURES]->(Actor)
```

Consulta todo lo que necesites en la documentación del apéndice: [apéndice de dataset como grafo](../../01-teoria/apendice-dataset-grafos.md).

## Entrega (al final de la sesión)

1. Tu fichero `mis_consultas.cypher` con las consultas de las tareas 1 a 4.
2. El CSV de características exportado de la tarea 4 (o una captura legible del resultado).
3. La respuesta escrita a la tarea 5 (3–5 líneas).

## Tarea 1 — Actores de una película (≈8 min)

Elige una película del grafo (por ejemplo `Arrival` o `Dune`) y escribe una consulta que liste sus actores ordenados alfabéticamente.

```cypher
MATCH (m:Movie {title: '...'})-[:FEATURES]->(a:Actor)
RETURN m.title AS title, a.name AS actor
ORDER BY a.name;
```

Comprueba: `Arrival` → 2 actores; `Dune` → 2 actores; `The Godfather` → 1 actor.

## Tarea 2 — Películas por género (≈10 min)

Escribe una consulta que devuelva el número de películas por género, de mayor a menor.

Comprueba tu resultado contra estas tres respuestas (no es necesario que coincida el orden de los empates):

| genre | movies |
|---|---|
| Science Fiction | 2 |
| Drama | 2 |
| Crime | 1 |

## Tarea 3 — Coaparición entre dos actores (≈10 min)

Elige dos actores de tu película y escribe una consulta que devuelva la(s) película(s) donde coinciden.

Comprueba: `Amy Adams` y `Jeremy Renner` coinciden solo en `Arrival`.

## Tarea 4 — Exportar una tabla de características (≈12 min)

Ejecuta la consulta de características del apéndice (sección 4) y expórtala como CSV:

```cypher
MATCH (m:Movie)
OPTIONAL MATCH (m)-[:HAS_GENRE]->(g:Genre)
WITH m, count(DISTINCT g) AS genre_count
OPTIONAL MATCH (m)-[:FEATURES]->(a:Actor)
WITH m, genre_count, count(DISTINCT a) AS actor_count
OPTIONAL MATCH (m)-[:DIRECTED_BY]->(d:Director)
RETURN m.id AS movie_id, m.title AS title, m.year AS year,
       genre_count, actor_count, count(DISTINCT d) AS director_count
ORDER BY movie_id;
```

En Neo4j Browser: vista **Table** y botón de descarga (esquina superior derecha del marco de resultados) → **CSV**.

Comprueba que obtienes 4 filas. `The Godfather` debe tener `genre_count = 2` (Crime y Drama) y `actor_count = 1`.

## Tarea 5 — Reflexión (≈5 min)

Responde en 3–5 líneas: de las consultas que has escrito, ¿cuál es más natural de expresar en un grafo que en una tabla de pandas o en SQL? Justifica por qué.

## Nota final

El CSV/Parquet del capstone sigue siendo la fuente canónica para ML. Este grafo es una representación derivada para explorar relaciones; las consultas que has hecho podrían convertirse en variables tabulares (como en la tarea 4) para continuar el pipeline.
