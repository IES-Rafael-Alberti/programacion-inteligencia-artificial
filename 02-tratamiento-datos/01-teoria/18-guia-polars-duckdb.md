# 18 — Guía docente 5: alternativas modernas a Pandas

## Objetivos de aprendizaje

- Presentar Polars como herramienta que puede usarse de forma independiente,
  sin requerir Pandas.
- Introducir **Polars** como DataFrame moderno orientado a rendimiento, Arrow y ejecución lazy.
- Introducir **DuckDB** como motor SQL local para consultar CSV/Parquet sin servidor.
- Distinguir cuándo una alternativa aporta valor y cuándo solo añade complejidad.

## Material asociado

| Bloque | Archivo |
|--------|---------|
| Polars intro | `12-polars-intro.md`, `../02-ejemplos/24_polars_intro.ipynb` |
| Polars operaciones | `../02-ejemplos/25_polars_operaciones.ipynb` |
| Polars avanzado | `../02-ejemplos/26_polars_avanzado_con_graficos.ipynb` |
| Polars vs Pandas | `13-polars-vs-pandas.md`, `../02-ejemplos/27_pandas_vs_polars.ipynb` |
| DuckDB | `14c-duckdb-analitica-local.md`, `../02-ejemplos/23_duckdb_eda.ipynb` |

## Secuencia sugerida

1. Trabajar con Polars de forma nativa en los ejemplos 24 (introducción), 25
   (operaciones) y 26 (Polars avanzado y gráficos).
2. Continuar con el ejemplo 27 para comparar Pandas y Polars y practicar la
   conversión o interoperabilidad únicamente cuando sea necesaria.
3. Profundizar en Polars avanzado con el ejemplo 28 de transformaciones.
4. Usar DuckDB para expresar una transformación equivalente con SQL y comparar
   legibilidad, rendimiento percibido y coste cognitivo.

## Mensaje didáctico

Polars no necesita Pandas para los ejemplos nativos. La comparación y la
interoperabilidad se introducen después, en el ejemplo 27, para que el alumnado
aprenda a elegir herramientas según el problema:

- Pandas: manipulación general en Python.
- Polars: rendimiento, lazy execution y Arrow.
- DuckDB: SQL analítico local sobre ficheros.

## Fuera de este bloque

NLP con NLTK/spaCy se trabaja en la unidad de Deep Learning/NLP, no en UD2.
