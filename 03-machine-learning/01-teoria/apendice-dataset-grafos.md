# Apéndice opcional — representar un dataset de películas como grafo

Este apéndice muestra una **alternativa de almacenamiento y consulta** para un dataset que ya ha sido integrado, limpiado y validado. No cambia el itinerario de UD3: el CSV/Parquet sigue siendo la fuente canónica y el grafo es una representación derivada para explorar relaciones.

> **Opcional.** No hace falta Neo4j para completar P1, P2, P3 ni el modelo de ML. La actividad sirve para conocer una herramienta útil cuando las relaciones entre entidades son tan importantes como las columnas.

## Secuencia didáctica propuesta

La ampliación se plantea como una actividad breve de aula, no como otro proyecto de la unidad:

1. **Demostración del profesor (20–30 min):** explicar tabla frente a grafo, crear el fixture de películas, cargarlo en Neo4j y resolver dos consultas sencillas.
2. **Mini-tarea del alumnado (45–60 min):** completar consultas sobre el mismo grafo, añadir una relación o propiedad pequeña y exportar una tabla agregada.
3. **Puesta en común (10–15 min):** comparar qué preguntas resultan naturales en Cypher y cuáles siguen siendo más adecuadas para pandas/SQL y el pipeline de ML.

La mini-tarea debe poder terminarse en una sesión y no requiere modificar P1, P2 ni P3.

> **Material listo para el aula** (en `03-practicas/actividades/grafo-peliculas/`): ficha de la [mini-tarea del alumnado](../../03-machine-learning/03-practicas/actividades/grafo-peliculas/mini-tarea-alumnado.md), copia local del fixture (`fixture/movies_graph.csv`) y los bloques Cypher listos para pegar en `cypher/`. El guion de la demostración y las soluciones de la mini-tarea son material docente local, no versionado.

## Guion operativo para el aula

### Antes de la clase — profesor

- Comprobar que Docker arranca y que los puertos `7474` y `7687` están libres.
- Descargar la imagen indicada y ejecutar una vez el comando de creación del contenedor.
- Cargar el fixture y ejecutar las restricciones y la importación completa.
- Repetir la importación y comprobar que el recuento de películas sigue siendo `4`.
- Probar las consultas de ejemplo y la exportación CSV de características.
- Llevar una copia del fixture y de los bloques Cypher por si se trabaja sin acceso a Internet.

Comprobación rápida del contenedor:

```bash
docker ps --filter name=neo4j-movies
curl -fsS http://localhost:7474 >/dev/null && echo "Neo4j Browser disponible"
```

### Durante la demostración

1. Mostrar primero el CSV y explicar que sigue siendo la fuente canónica.
2. Dibujar cuatro tipos de nodo y tres tipos de relación.
3. Ejecutar la restricción, la carga y una consulta de vecinos.
4. Repetir la carga para hacer visible la idempotencia de `MERGE`.
5. Exportar una tabla y relacionarla con el paso posterior de ML.

### Si Docker no está disponible

No se improvisará una instalación compleja durante la clase. Se puede:

- hacer la demostración proyectando una ejecución preparada;
- usar una instancia temporal autorizada por el profesor;
- dejar la mini-tarea como lectura guiada y consultas razonadas.

La falta de Neo4j no afecta al resto de UD3 ni se convierte en incidencia del entorno Pixi.

### Evidencias de la mini-tarea

Cada alumno o pareja entrega:

- el fichero `.cypher` con sus consultas;
- la exportación CSV o una captura legible del resultado;
- una explicación breve de una consulta que resulte más natural en un grafo que en una tabla.

La actividad es formativa y no modifica la evaluación ordinaria de P1/P2/P3.

## Objetivos

Al terminar, podrás:

- distinguir una tabla, un grafo de propiedades y una matriz de características para ML;
- modelar nodos, relaciones, propiedades e identificadores estables;
- cargar datos de películas de forma repetible con Cypher;
- consultar vecinos, agregaciones y caminos sencillos;
- exportar características tabulares para continuar el proceso de ML.

## Cuándo tiene sentido un grafo

Una tabla es normalmente la mejor opción para entrenar un modelo con filas y columnas. Un grafo resulta atractivo cuando las preguntas recorren relaciones:

- ¿qué actores han trabajado con un director concreto?
- ¿qué películas comparten género y miembros del reparto?
- ¿qué entidades conectan dos películas?

El grafo no hace automáticamente mejor al modelo. Aporta una forma cómoda de consultar la estructura conectada; después podemos convertir esas consultas en variables tabulares.

## Frontera con el dataset del curso

El `movies.csv` del capstone conserva el snapshot docente validado y está pensado para el pipeline tabular. No contiene todas las entidades necesarias para construir este ejemplo (por ejemplo, identificadores de película, actores o directores).

Por eso aquí usamos un **fixture enriquecido y derivado**. En un proyecto real, ese fixture se generaría durante la integración de fuentes, manteniendo trazabilidad hacia el dataset canónico:

```text
fuentes → integración y validación → CSV/Parquet canónico → representación derivada en Neo4j
                                                        ↘ características tabulares para ML
```

No se modifica `movies.csv`, no se rehacen P2/P3 y no se convierte Neo4j en una dependencia de Pixi.

## 1. Preparar Neo4j Community con Docker

Necesitas Docker funcionando. Desde una carpeta de trabajo vacía:

```bash
mkdir -p neo4j-movies/import
cd neo4j-movies
```

Guarda el siguiente fixture como `import/movies_graph.csv`:

```csv
movie_id,title,year,genre,director,actor
m1,Arrival,2016,Science Fiction,Denis Villeneuve,Amy Adams
m1,Arrival,2016,Science Fiction,Denis Villeneuve,Jeremy Renner
m2,Dune,2021,Science Fiction,Denis Villeneuve,Timothee Chalamet
m2,Dune,2021,Science Fiction,Denis Villeneuve,Zendaya
m3,The Godfather,1972,Crime,Francis Ford Coppola,Al Pacino
m3,The Godfather,1972,Drama,Francis Ford Coppola,Al Pacino
m4,Lost in Translation,2003,Drama,Sofia Coppola,Scarlett Johansson
m4,Lost in Translation,2003,Drama,Sofia Coppola,Bill Murray
```

Arranca un contenedor local (la contraseña es solo para este ejercicio):

```bash
docker run --name neo4j-movies \
  --publish 7474:7474 --publish 7687:7687 \
  --env NEO4J_AUTH=neo4j/course-only-password \
  --volume "$PWD/import:/var/lib/neo4j/import" \
  neo4j:5.26-community
```

Abre <http://localhost:7474>, inicia sesión con `neo4j` y `course-only-password`, y selecciona la base de datos `neo4j`.

La interfaz reciente puede abrir **Workspace** y mostrar solo una línea de comandos. Para seguir esta guía, selecciona **Go to old browser** (Browser clásico): es la vista que ofrece el editor Cypher completo. **Saved Cypher** solo almacena consultas guardadas; no es el editor.

Para detener y eliminar el contenedor al terminar:

```bash
docker rm --force neo4j-movies
```

> En un aula sin Docker se puede usar una instalación local o una instancia temporal autorizada por el profesor. No introduzcas datos personales ni credenciales reales.

## 2. Modelo e importación idempotente

El modelo es un grafo de propiedades:

```text
(Movie)-[:HAS_GENRE]->(Genre)
(Movie)-[:DIRECTED_BY]->(Director)
(Movie)-[:FEATURES]->(Actor)
```

En Neo4j Browser, ejecuta primero estas restricciones y después la carga. Ejecuta **cada restricción completa por separado**; no pegues una línea `FOR ...` aislada. `MERGE` evita duplicar nodos y relaciones al ejecutar el bloque más de una vez.

```cypher
CREATE CONSTRAINT movie_id IF NOT EXISTS
FOR (m:Movie) REQUIRE m.id IS UNIQUE;

CREATE CONSTRAINT genre_name IF NOT EXISTS
FOR (g:Genre) REQUIRE g.name IS UNIQUE;

CREATE CONSTRAINT director_name IF NOT EXISTS
FOR (d:Director) REQUIRE d.name IS UNIQUE;

CREATE CONSTRAINT actor_name IF NOT EXISTS
FOR (a:Actor) REQUIRE a.name IS UNIQUE;
```

```cypher
LOAD CSV WITH HEADERS FROM 'file:///movies_graph.csv' AS row
MERGE (m:Movie {id: row.movie_id})
  ON CREATE SET m.title = row.title, m.year = toInteger(row.year)
MERGE (g:Genre {name: row.genre})
MERGE (d:Director {name: row.director})
MERGE (a:Actor {name: row.actor})
MERGE (m)-[:HAS_GENRE]->(g)
MERGE (m)-[:DIRECTED_BY]->(d)
MERGE (m)-[:FEATURES]->(a);
```

Comprueba que la segunda ejecución no aumenta el número de películas:

```cypher
MATCH (m:Movie)
RETURN count(m) AS movies;
```

El resultado debe ser `4` tanto antes como después de repetir la carga.

## 3. Consultas Cypher

### Películas de un género

```cypher
MATCH (m:Movie)-[:HAS_GENRE]->(g:Genre {name: 'Science Fiction'})
RETURN m.id, m.title, m.year
ORDER BY m.year;
```

### Directores y número de películas

```cypher
MATCH (d:Director)<-[:DIRECTED_BY]-(m:Movie)
RETURN d.name AS director, count(m) AS movies
ORDER BY movies DESC, director;
```

### Colaboraciones entre actores

```cypher
MATCH (a1:Actor)<-[:FEATURES]-(m:Movie)-[:FEATURES]->(a2:Actor)
WHERE a1.name < a2.name
RETURN a1.name AS actor_1, a2.name AS actor_2, count(DISTINCT m) AS shared_movies
ORDER BY shared_movies DESC, actor_1, actor_2;
```

### Películas conectadas por género y director

```cypher
MATCH (m1:Movie)-[:HAS_GENRE]->(g:Genre)<-[:HAS_GENRE]-(m2:Movie),
      (m1)-[:DIRECTED_BY]->(d:Director)<-[:DIRECTED_BY]-(m2)
WHERE m1.id < m2.id
RETURN m1.title AS movie_1, m2.title AS movie_2,
       g.name AS shared_genre, d.name AS shared_director;
```

## Mini-tarea de aula

Después de la demostración, el alumnado debe:

1. escribir una consulta que liste los actores de una película elegida;
2. obtener el número de películas por género;
3. añadir una consulta de coaparición entre dos actores;
4. exportar una tabla con `movie_id`, número de géneros y número de actores;
5. responder en unas líneas: ¿qué consulta es más natural en Cypher que en una tabla?

La entrega puede consistir en un fichero `.cypher`, una captura o exportación CSV y una breve explicación. No se evalúa el rendimiento de un modelo; se evalúa comprender la representación y justificar cuándo usarla.

## 4. Volver a una tabla de características para ML

El modelo de ML no recibe nodos y relaciones directamente en este apéndice. Pedimos a Neo4j una tabla agregada por película:

```cypher
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
```

En Neo4j Browser cambia el resultado a vista **Table** si fuese necesario y usa el icono de descarga de la esquina superior derecha del marco de resultados → **CSV**. Ese archivo puede cargarse con pandas y unirse a otras variables, siempre documentando su procedencia.

## 5. Consultar Neo4j desde Python (ruta programática)

El módulo es **Programación de IA**: el uso en el entorno web de Neo4j (Browser) sirve para entender la representación de forma visual, pero el fin último es consultar el grafo **desde un programa** y usar las características resultantes con modelos de ML. Por eso esta es la ruta recomendada al cerrar la actividad.

La imagen Docker proporciona el **servidor** Neo4j. Para consultarlo desde Python solo hace falta el driver oficial, cuyo paquete en PyPI se llama `neo4j` (el nombre antiguo `neo4j-driver` está obsoleto) y en conda-forge `neo4j-python-driver`.

La dependencia queda aislada en una feature/entorno `ud3-graph`, para no instalarla a todo el alumnado que no haga la ampliación:

```toml
[feature.ud3-graph.dependencies]
neo4j-python-driver = ">=6,<7"

[environments]
ud3-graph = ["base", "ud3", "ud3-graph"]
```

Se instala con:

```bash
pixi install --environment ud3-graph
```

El ejemplo completo del bucle grafo → tabla → modelo está en `03-machine-learning/02-ejemplos/grafo-peliculas-python/grafo_a_ml.py`. Ejemplo mínimo de consulta. Las credenciales deben llegar por variables de entorno, nunca escribirse en el código:

```python
import os

import pandas as pd
from neo4j import GraphDatabase

uri = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
user = os.environ["NEO4J_USER"]
password = os.environ["NEO4J_PASSWORD"]

query = """
MATCH (m:Movie)-[:HAS_GENRE]->(g:Genre)
RETURN m.id AS movie_id, m.title AS title, g.name AS genre
ORDER BY movie_id, genre
"""

with GraphDatabase.driver(uri, auth=(user, password)) as driver:
    driver.verify_connectivity()
    records, _, _ = driver.execute_query(query, database_="neo4j")

df = pd.DataFrame([record.data() for record in records])
print(df.head())
```

Ejecutar con el servidor en marcha:

```bash
NEO4J_PASSWORD=course-only-password \
pixi run --environment ud3-graph python 03-machine-learning/02-ejemplos/grafo-peliculas-python/grafo_a_ml.py
```

Esta ruta no elimina el uso introductorio de Cypher en Browser: es la segunda capa (programática) que convierte el grafo en un dato más para el pipeline de ML.

## Grafo frente a CSV/Parquet

| Necesidad | CSV/Parquet | Grafo de propiedades |
|---|---|---|
| Entrenar con filas y columnas | Sencillo y eficiente | Requiere exportar características |
| Consultar relaciones de varias saltos | Hay que hacer `merge` y joins | Natural con patrones Cypher |
| Portabilidad y revisión | Muy alta | Depende del motor y su versión |
| Instalación | No requiere servidor | Requiere Neo4j local o remoto |
| Fuente canónica del capstone | Sí | No; es una copia derivada |

La elección depende de la pregunta. No se trata de reemplazar tablas por grafos en todos los proyectos.

## Fuera de alcance

En esta primera ampliación no se estudian administración de servidores, clustering, seguridad o despliegue productivo; tampoco GNN, embeddings, GraphRAG ni un rediseño del capstone. Esas tecnologías podrían formar actividades posteriores independientes.

## Checklist de cierre

- [ ] He arrancado Neo4j y cargado el fixture.
- [ ] He ejecutado la carga dos veces sin duplicados.
- [ ] He probado al menos tres consultas.
- [ ] He exportado la tabla de características.
- [ ] Puedo explicar por qué el CSV/Parquet sigue siendo la fuente canónica.

## Referencias

- [Neo4j — ejecutar Neo4j con Docker](https://neo4j.com/docs/operations-manual/current/docker/introduction/)
- [Manual de Cypher](https://neo4j.com/docs/cypher-manual/current/)
