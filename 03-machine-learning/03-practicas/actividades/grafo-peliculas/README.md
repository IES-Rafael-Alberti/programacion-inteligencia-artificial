# Kit de aula — Dataset de películas como grafo (Neo4j/Cypher)

Ampliación **opcional** de UD3: representar el dataset de películas como grafo de propiedades. La teoría, el modelo y las consultas completas están en el [apéndice de dataset como grafo](../../01-teoria/apendice-dataset-grafos.md). Aquí se prepara su uso en el aula.

## Contenido publicado

| Archivo | Uso |
|---|---|
| `mini-tarea-alumnado.md` | Ficha de la mini-tarea del alumnado (~50 min), auto-verificable |
| `fixture/movies_graph.csv` | Copia del fixture (8 filas, 4 películas) para importar en el contenedor |
| `cypher/00-restricciones.cypher` | Restricciones de unicidad (`Movie`, `Genre`, `Director`, `Actor`) |
| `cypher/01-carga.cypher` | Carga idempotente con `MERGE` |
| `cypher/02-consultas-ejemplo.cypher` | Las 4 consultas de la demostración + comprobación de idempotencia |
| `cypher/03-caracteristicas.cypher` | Exportación de la tabla de características para ML |

El guion de la demostración (`demo-profesor.md`) y las soluciones de referencia de la mini-tarea (`cypher/04-mini-tarea-solucion.cypher`) son **material docente local, no versionado** (reglas `*profe*` y `*-sol*` del `.gitignore`): se conservan en la máquina del profesorado y no viajan con el repositorio.

## Preparación antes de la clase (profesorado)

1. Arrancar el contenedor y montar el fixture:
   - carpeta local `fixture/` → `/var/lib/neo4j/import/` del contenedor;
   - el CSV debe quedar como `import/movies_graph.csv` (ver apéndice, sección 1).
2. Ejecutar `cypher/00-restricciones.cypher` y `cypher/01-carga.cypher` una vez.
3. Comprobar que `count(m)` devuelve `4` y que la recarga no duplica películas.
4. Probar `cypher/02-consultas-ejemplo.cypher` y `cypher/03-caracteristicas.cypher` contra los resultados esperados de `demo-profesor.md`.
5. Llevar copia local del fixture y de los bloques Cypher por si se trabaja sin Internet.

## No modifica el curso

- No toca el entorno común: Neo4j va en Docker aparte y el driver Python vive en la feature/entorno `ud3-graph` de `pixi.toml`.
- No altera `movies.csv` del capstone, ni P1/P2/P3.
- La **ruta programática** (objetivo del módulo) está en el ejemplo `03-machine-learning/02-ejemplos/grafo-peliculas-python/`: consulta desde Python, conversión a pandas y uso con un modelo de scikit-learn.