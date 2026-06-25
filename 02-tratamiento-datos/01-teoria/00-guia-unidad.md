# 00 — Guía de la unidad: Tratamiento de datos

## Propósito

Esta unidad enseña a trabajar con datos tabulares en Python: cargar, inspeccionar, limpiar, transformar, agregar, unir y visualizar datos para preparar análisis exploratorios y fases posteriores de Machine Learning.

La prioridad no es coleccionar librerías. La prioridad es que el alumnado entienda el flujo de trabajo con datos y sepa elegir herramientas con criterio.

## Jerarquía didáctica

### Core obligatorio

1. **Pandas**
   - carga y exportación de datos;
   - selección, filtrado y ordenación;
   - limpieza de valores nulos;
   - transformaciones y columnas derivadas;
   - `groupby`, agregaciones y joins;
   - EDA básico.

2. **Matplotlib**
   - base conceptual de la visualización;
   - líneas, barras, histogramas, dispersión, mapas de calor;
   - títulos, ejes, leyendas, estilos y exportación.

3. **Seaborn**
   - EDA estadístico rápido sobre Pandas;
   - distribuciones, relaciones y comparaciones por categorías.

### Complementos de visualización

- **Plotly Express**: interactividad rápida en notebooks y HTML.
- **Altair / hvPlot / Panel**: visualización declarativa y dashboards ligeros. Material de nivel 2, no eje principal.

### Alternativas a Pandas

- **Polars**: DataFrames rápidos, lazy execution y Arrow.
- **DuckDB**: SQL analítico local sobre CSV/Parquet.
- **cuDF/RAPIDS**: caso avanzado de DataFrames con GPU NVIDIA/CUDA.

### Anexos o material archivado

- **FireDucks**: curiosidad técnica pandas-compatible acelerada por CPU; no eje curricular.
- **spaCy/NLP**: trasladado a la unidad de Deep Learning/NLP porque rompe el foco de datos tabulares.

## Secuencia sugerida

| Fase | Foco | Material base |
|------|------|---------------|
| 1 | Pandas básico | `01-pandas-introduccion.md`, `01_pandas_fundamentos.ipynb` |
| 2 | EDA y preparación | `04-eda-pasos.md`, `05-preparacion-datos-ml.md`, `02_pandas_eda_visualizacion.ipynb` |
| 3 | Matplotlib | `06-matplotlib-fundamentos.md`, `07-matplotlib-parte1.md`, `08-matplotlib-parte2.md` |
| 4 | Seaborn | `09-seaborn.md`, `11_seaborn_spotify.ipynb` |
| 5 | Interactividad | `14b-plotly-express-interactividad.md`, `17_plotly_express_interactivo.ipynb` |
| 6 | Alternativas | `12-polars-intro.md`, `13-polars-vs-pandas.md`, `14c-duckdb-analitica-local.md` |
| 7 | GPU | `11-cudf-introduccion.md`, `20_cudf_rapids_intro.ipynb` |

## Criterio de evaluación formativa

Al finalizar la unidad, el alumnado debería poder:

- explicar qué problema resuelve Pandas en el flujo de datos;
- limpiar un dataset realista y justificar las decisiones tomadas;
- usar `groupby`, agregaciones y joins sin copiar recetas a ciegas;
- generar visualizaciones legibles con Matplotlib y Seaborn;
- elegir cuándo una visualización interactiva aporta valor;
- explicar cuándo Polars, DuckDB o cuDF son alternativas razonables y cuándo no;
- distinguir entre herramienta central, complemento y anexo.

## Fuera de alcance

- NLP con spaCy o Transformers: se trabaja en Deep Learning/NLP.
- GPU como eje transversal: se introduce como caso avanzado con cuDF/RAPIDS.
- Dashboards completos: se dejan como extensión, no como requisito base.
