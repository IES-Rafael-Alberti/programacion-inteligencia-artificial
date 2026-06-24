# Herramientas de datos para IA

## Introducción

El procesamiento de datos es una parte central de cualquier proyecto de IA. Antes de entrenar o desplegar modelos, hay que limpiar, transformar, agregar y preparar los datos.

---

## Polars

### ¿Qué es?

Librería de procesamiento de datos muy rápida, con API expresiva y buen rendimiento en una sola máquina.

### Fortalezas

- Muy buen rendimiento.
- Bajo consumo de memoria.
- Soporta modo eager y lazy.

### Cuándo usarlo

- Datos medianos que caben en una máquina.
- Procesamiento tabular rápido.
- Sustitución moderna de muchos flujos con pandas.

```python
import polars as pl

df = pl.read_csv("datos.csv")
resultado = df.filter(pl.col("valor") > 0)
```

---

## Dask

### ¿Qué es?

Herramienta de computación paralela para escalar flujos parecidos a pandas o NumPy.

### Fortalezas

- Escala de una máquina a varias.
- Útil cuando los datos no caben en memoria.
- Buena integración con ecosistemas Python.

### Cuándo usarlo

- Datos más grandes que la memoria disponible.
- Procesos distribuidos con sintaxis cercana a pandas.

```python
import dask.dataframe as dd

df = dd.read_csv("datos_grandes.csv")
resultado = df.groupby("categoria").valor.mean().compute()
```

---

## Spark

### ¿Qué es?

Motor de procesamiento distribuido ampliamente usado en entornos empresariales y Big Data.

### Cuándo usarlo

- Datos muy grandes.
- Integración con ecosistemas ya basados en Spark.
- Necesidad de SQL distribuido y pipelines más industriales.

---

## DuckDB

### ¿Qué es?

Motor analítico embebido especialmente útil para consultar archivos locales o Parquet con SQL.

### Cuándo usarlo

- Análisis rápido.
- Consulta de ficheros sin desplegar una base de datos compleja.
- Trabajo local con datasets medianos.

```python
import duckdb

duckdb.sql("SELECT * FROM 'datos.parquet' LIMIT 10")
```

---

## Otras alternativas libres

### pandas

- La librería tabular más extendida en Python.
- Sigue siendo la referencia de entrada en muchos proyectos docentes.

### Ray Data

- Parte del ecosistema Ray.
- Interesante cuando se quieren pipelines de datos e inferencia distribuidos dentro del mismo entorno.

---

## Comparativa

| Herramienta | Mejor encaje | Ventaja principal | Limitación |
|-------------|--------------|-------------------|------------|
| Polars | Datos medianos en una máquina | Velocidad | No sustituye a un clúster |
| Dask | Datos grandes en Python | Escalado progresivo | Más complejidad operativa |
| Spark | Big Data y entorno empresarial | Escala y ecosistema | Más pesado para proyectos pequeños |
| DuckDB | Consulta analítica local | Simplicidad y velocidad | No es un framework distribuido |
| pandas | Introducción y compatibilidad | Muy conocido | Menor rendimiento en algunos casos |
| Ray Data | Pipelines distribuidos con Ray | Integración con ecosistema Ray | Más avanzado para docencia básica |

---

## Aplicación al proyecto

Antes de elegir una herramienta de datos conviene responder:

1. ¿Cuánto volumen de datos se va a manejar?
2. ¿Los datos caben en memoria?
3. ¿Hace falta procesamiento distribuido?
4. ¿El grupo ya trabaja con Python tabular o con Spark?

En muchos proyectos docentes, Polars o DuckDB son suficientes. Dask o Spark solo compensan cuando la escala o la arquitectura del proyecto lo justifican.

---

## Recomendaciones generales

| Caso | Herramienta recomendada |
|------|-------------------------|
| Primer contacto con datos tabulares | pandas |
| Datos pequeños o medianos | Polars o DuckDB |
| Datos grandes en Python | Dask |
| Datos muy grandes o entorno empresarial | Spark |

---

## Ejemplo de pipeline de datos para ML

```python
import polars as pl

df = pl.read_csv("datos.csv")
df = df.filter(pl.col("valor").is_not_null())

features = df.group_by("id").agg(
    pl.col("valor").mean().alias("media"),
    pl.len().alias("n_registros")
)

features.write_parquet("features.parquet")
```

---

## Fuentes recomendadas

- Documentación oficial de Polars.
- Documentación oficial de Dask.
- Documentación oficial de Apache Spark.
- Documentación oficial de DuckDB.
- Documentación oficial de pandas y Ray Data.
