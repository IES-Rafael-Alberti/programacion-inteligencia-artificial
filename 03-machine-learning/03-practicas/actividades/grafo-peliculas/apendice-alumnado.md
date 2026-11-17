# Apéndice para el alumnado — Consultar un dataset de películas como grafo

Esta ampliación opcional de UD3 te permite representar y consultar relaciones entre películas, géneros, directores y actores con Neo4j y Cypher. No necesitas esta actividad para completar P1, P2, P3 ni el itinerario ordinario de machine learning.

El CSV o Parquet del proyecto sigue siendo la fuente canónica. El grafo es una representación derivada para explorar relaciones; si quieres usar sus resultados en un modelo, primero tendrás que convertirlos en una tabla de características.

## Recorrido rápido

1. Abre Neo4j Browser en la instancia que indique el profesor e inicia sesión con las credenciales proporcionadas para la actividad.
2. Comprueba que el grafo está cargado con la consulta de la sección **1**.
3. Ejecuta las consultas de ejemplo de la sección **3** y observa el patrón `MATCH`.
4. Completa la [mini-tarea](mini-tarea-alumnado.md) y exporta la tabla de características de la sección **4**.

No reutilices estas credenciales fuera del ejercicio ni incluyas contraseñas personales en consultas o entregas.

## 1. Comprueba el grafo

En Neo4j Browser, ejecuta:

```cypher
MATCH (m:Movie)
RETURN count(m) AS movies;
```

El fixture de la actividad contiene **4 películas**. Si obtienes otro resultado o un error, no intentes instalar o reconfigurar el servidor por tu cuenta: guarda el mensaje y consulta al profesor.

## 2. Datos y modelo

El fixture `fixture/movies_graph.csv` contiene 8 filas y 4 películas. Una película puede aparecer en varias filas si tiene más de un género o actor. El modelo del grafo es:

```text
(Movie)-[:HAS_GENRE]->(Genre)
(Movie)-[:DIRECTED_BY]->(Director)
(Movie)-[:FEATURES]->(Actor)
```

Cada nodo `Movie` tiene un identificador estable (`id`), título y año. Los nodos `Genre`, `Director` y `Actor` se relacionan con la película mediante aristas etiquetadas. Por ejemplo, para encontrar los actores de una película, recorremos la relación `FEATURES`:

```cypher
MATCH (m:Movie {title: 'Arrival'})-[:FEATURES]->(a:Actor)
RETURN m.title AS title, a.name AS actor
ORDER BY a.name;
```

El resultado debe incluir a Amy Adams y Jeremy Renner. En Cypher, los paréntesis representan nodos, las relaciones se escriben entre corchetes y las propiedades se indican entre llaves.

### Si te piden cargar el fixture

Normalmente recibirás acceso a un grafo ya preparado. Si la actividad requiere que lo cargues tú, necesitas Docker y la carpeta de materiales con `fixture/movies_graph.csv` y los ficheros de `cypher/`. Sigue estas instrucciones desde una carpeta de trabajo propia, no desde la carpeta original del repositorio:

1. Copia `fixture/movies_graph.csv` a una carpeta local llamada `import` dentro de tu carpeta de trabajo.
2. Arranca Neo4j desde esa carpeta:

```bash
docker run --name neo4j-movies \
  --publish 7474:7474 --publish 7687:7687 \
  --env NEO4J_AUTH=neo4j/course-only-password \
  --volume "$PWD/import:/var/lib/neo4j/import" \
  neo4j:5.26-community
```

3. Abre <http://localhost:7474>, inicia sesión con `neo4j` y `course-only-password`, y selecciona la base de datos `neo4j`.
4. Ejecuta cada sentencia completa de `cypher/00-restricciones.cypher` y, después, `cypher/01-carga.cypher`.
5. Repite la consulta de comprobación de esta sección. Debe devolver `4`, también después de volver a ejecutar la carga.

La ruta de montaje del comando puede variar según el sistema operativo y la configuración de Docker. Si Docker no reconoce la carpeta `import`, consulta al profesor en vez de modificar permisos de carpetas compartidas. Al terminar, puedes parar y eliminar el contenedor con `docker rm --force neo4j-movies`.

## 3. Consultas de ejemplo

En una consulta Cypher, `MATCH` describe el patrón que queremos encontrar; `RETURN` elige las columnas de salida y `ORDER BY` ordena el resultado.

### Películas de un género

```cypher
MATCH (m:Movie)-[:HAS_GENRE]->(g:Genre {name: 'Science Fiction'})
RETURN m.id AS movie_id, m.title AS title, m.year AS year
ORDER BY m.year;
```

El resultado contiene `Arrival` y `Dune`.

### Directores y número de películas

```cypher
MATCH (d:Director)<-[:DIRECTED_BY]-(m:Movie)
RETURN d.name AS director, count(m) AS movies
ORDER BY movies DESC, director;
```

La flecha puede recorrerse en ambos sentidos: aquí partimos del director y seguimos la relación entrante `DIRECTED_BY` hasta las películas.

### Películas compartidas por dos actores

```cypher
MATCH (a1:Actor)<-[:FEATURES]-(m:Movie)-[:FEATURES]->(a2:Actor)
WHERE a1.name < a2.name
RETURN a1.name AS actor_1, a2.name AS actor_2,
       count(DISTINCT m) AS shared_movies
ORDER BY shared_movies DESC, actor_1, actor_2;
```

`DISTINCT` evita contar dos veces una película si el patrón produce duplicados.

### Películas conectadas por género y director

```cypher
MATCH (m1:Movie)-[:HAS_GENRE]->(g:Genre)<-[:HAS_GENRE]-(m2:Movie),
      (m1)-[:DIRECTED_BY]->(d:Director)<-[:DIRECTED_BY]-(m2)
WHERE m1.id < m2.id
RETURN m1.title AS movie_1, m2.title AS movie_2,
       g.name AS shared_genre, d.name AS shared_director;
```

La consulta encuentra `Arrival` y `Dune`, que comparten género y director.

## 4. Exporta una tabla de características

El grafo no sustituye a las filas y columnas que utiliza un modelo de ML. Esta consulta resume las relaciones de cada película en variables tabulares:

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

En Neo4j Browser, cambia el resultado a vista **Table** y utiliza el botón de descarga del marco de resultados para guardarlo como CSV. Debes obtener 4 filas. `The Godfather` tendrá `genre_count = 2` y `actor_count = 1`.

Estas columnas describen el fixture. En un proyecto real tendrías que justificar cómo se han obtenido, unirlas de forma correcta al resto de datos y evitar usar información que revele la respuesta que intenta predecir el modelo.

## 5. Límites de esta representación

- El grafo de esta práctica es un fixture pequeño y derivado, no el dataset canónico del capstone.
- Cypher facilita consultar conexiones; no hace automáticamente mejor el análisis ni el modelo.
- La tabla exportada puede usarse en un pipeline, pero hay que documentar su procedencia y decidir si las variables responden al problema.
- Esta actividad no cubre administración de bases de datos, despliegue productivo ni redes neuronales de grafos.

## Continúa con la actividad

Usa la [mini-tarea para el alumnado](mini-tarea-alumnado.md) para practicar consultas, exportar el CSV y explicar cuándo una pregunta resulta natural de expresar como grafo.
