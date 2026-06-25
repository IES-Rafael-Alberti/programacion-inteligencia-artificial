# 14c — DuckDB: analítica SQL local sobre ficheros

DuckDB es una base de datos analítica embebida. En esta unidad se usa como complemento a Pandas: permite consultar CSV, Parquet u otros datos locales con SQL sin montar un servidor de base de datos.

## Qué problema resuelve

Pandas es excelente para manipulación programática de datos, pero a veces una consulta SQL expresa mejor una operación:

- seleccionar columnas;
- filtrar registros;
- agrupar y agregar;
- unir tablas;
- consultar directamente ficheros grandes.

DuckDB permite hacer eso de forma local y ligera.

## Patrón básico

```python
import duckdb

resultado = duckdb.sql("""
    SELECT categoria, AVG(valor) AS media
    FROM 'datos.csv'
    GROUP BY categoria
    ORDER BY media DESC
""").df()
```

El resultado puede volver a Pandas con `.df()`, así que DuckDB no sustituye el flujo de trabajo: lo complementa.

## Cuándo usar DuckDB

- Cuando una transformación se expresa mejor en SQL.
- Cuando interesa consultar CSV/Parquet sin cargarlos manualmente.
- Para comparar mentalidad SQL frente a mentalidad DataFrame.
- Para análisis local reproducible sin infraestructura externa.

## Cuándo NO usarlo

- Si el objetivo es aprender primero Pandas.
- Si basta una operación sencilla de DataFrame.
- Si se necesita una base de datos transaccional con usuarios, permisos y servidor.

## Comparación rápida

| Herramienta | Mejor para |
|-------------|------------|
| Pandas | Manipulación general de DataFrames en Python |
| Polars | DataFrames rápidos, lazy execution, Arrow |
| DuckDB | SQL analítico local sobre ficheros/tablas |
| cuDF | DataFrames acelerados con GPU NVIDIA/CUDA |

## Relación con la unidad

- Core previo: Pandas, limpieza, joins, groupby, EDA.
- Notebook asociado: `../02-ejemplos/23_duckdb_eda.ipynb`.
- Recurso asociado: `../05-recursos/EDA_DuckDB.md`.

## Idea clave

DuckDB no es “otro Pandas”. Es una forma de traer SQL analítico al trabajo local con datos. La comparación útil es: cuándo conviene pensar en DataFrames y cuándo conviene pensar en consultas.
