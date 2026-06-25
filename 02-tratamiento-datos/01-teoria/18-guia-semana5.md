# 18 — Guía Semana 5: alternativas modernas a Pandas

## Objetivos de aprendizaje

- Consolidar Pandas como referencia antes de comparar alternativas.
- Introducir **Polars** como DataFrame moderno orientado a rendimiento, Arrow y ejecución lazy.
- Introducir **DuckDB** como motor SQL local para consultar CSV/Parquet sin servidor.
- Distinguir cuándo una alternativa aporta valor y cuándo solo añade complejidad.

## Material asociado

| Bloque | Archivo |
|--------|---------|
| Polars intro | `12-polars-intro.md`, `../02-ejemplos/24_polars_intro.ipynb` |
| Polars operaciones | `../02-ejemplos/25_polars_operaciones.ipynb` |
| Polars vs Pandas | `13-polars-vs-pandas.md`, `../02-ejemplos/27_pandas_vs_polars.ipynb` |
| DuckDB | `14c-duckdb-analitica-local.md`, `../02-ejemplos/23_duckdb_eda.ipynb` |

## Secuencia sugerida

1. Resolver una tarea con Pandas.
2. Repetirla con Polars para ver diferencias de API y mentalidad.
3. Usar DuckDB para expresar una transformación equivalente con SQL.
4. Comparar legibilidad, rendimiento percibido y coste cognitivo.

## Mensaje didáctico

Pandas sigue siendo la base. Polars y DuckDB no se introducen para “sustituirlo todo”, sino para que el alumnado aprenda a elegir herramientas según el problema:

- Pandas: manipulación general en Python.
- Polars: rendimiento, lazy execution y Arrow.
- DuckDB: SQL analítico local sobre ficheros.

## Fuera de esta semana

NLP con NLTK/spaCy se trabaja en la unidad de Deep Learning/NLP, no en UD2.
