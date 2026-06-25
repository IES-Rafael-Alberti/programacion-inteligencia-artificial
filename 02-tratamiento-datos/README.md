# 02 — Tratamiento de Datos

## Propósito

Unidad centrada en el tratamiento, limpieza, transformación, análisis exploratorio y visualización de datos tabulares con Python.

El eje es **Pandas + Matplotlib + Seaborn**. A partir de esa base se introducen complementos razonables: Plotly para interactividad, Polars y DuckDB como alternativas modernas, y cuDF/RAPIDS como caso avanzado condicionado por GPU NVIDIA/CUDA.

## Jerarquía de contenidos

| Nivel | Herramientas | Rol |
|-------|--------------|-----|
| Core obligatorio | Pandas, Matplotlib, Seaborn | Base de tratamiento, EDA y visualización |
| Complementos | Plotly, Altair, hvPlot, Panel | Interactividad y visualización declarativa |
| Alternativas a Pandas | Polars, DuckDB | Rendimiento, lazy execution y SQL local |
| Avanzado | cuDF/RAPIDS | DataFrames con GPU NVIDIA/CUDA |
| Anexos/archivo | FireDucks, R, NLTK antiguo | Referencia histórica o curiosidad técnica |

## Estructura

```
01-teoria/         → Guías numeradas: Pandas, EDA, Matplotlib, Seaborn,
│                    Plotly, DuckDB, Altair, cuDF, Polars y planificación
02-ejemplos/       → Notebooks de Pandas, EDA, cuDF, Matplotlib, Plotly,
│                    Altair, Seaborn, Polars y semanas guiadas
03-practicas/      → Ejercicios alumno: EDA visual, Pandas seleccionados,
│                    R Titanic alumno y zips de apoyo
04-evaluacion/     → Pendiente de incorporar
05-recursos/       → Datasets, gráficos demo, chuletas y comparativas EDA
90-archivo/        → NLP_old, alternativas-R, ud3-content, fireducks
99-profesor/       → Soluciones de prácticas y ejemplos
```

## 01-teoria/

- **00:** Guía de la unidad
- **01–03:** Pandas (intro, ejemplos guiados, chuleta)
- **04–05:** EDA y preparación de datos para ML
- **06–08:** Matplotlib
- **09:** Seaborn
- **10:** Altair/hvPlot/Panel (nivel 2)
- **11:** cuDF/RAPIDS (caso NVIDIA)
- **12–13:** Polars y comparación con Pandas/Arrow
- **14:** EDA visual
- **14b:** Plotly Express
- **14c:** DuckDB
- **15:** Errores frecuentes en Altair
- **16–19:** Guías de planificación docente

## 02-ejemplos/

| Bloque | Archivos | Temas |
|--------|----------|-------|
| Pandas / EDA base | `01–03` | Fundamentos, EDA visual, EDA con Pandas |
| Pandas avanzado | `04–06` | Demo, extendido, gráficos |
| Matplotlib | `07–10` | Fundamentos, partes 1 y 2, avanzado |
| Seaborn / EDA aplicada | `11–14` | Spotify, EDA semana 3, House Prices, Titanic |
| Visualización interactiva/declarativa | `15–19` | Altair, Plotly, mini EDA, HoloViz/Panel |
| Alternativas / GPU / SQL local | `20–27` | cuDF, DuckDB, Polars, Pandas vs Polars |
| Transformaciones | `28` | Transformaciones avanzadas |

## 03-practicas/

- `EDA_Visual_Practicas.ipynb` — práctica integrada de visualización.
- `ejercicios_seleccionados/` — 10 ejercicios de Pandas con datasets.
- `r_exercises_titanic_with_tests/` — ejercicios R para alumnado; versiones profesor en `99-profesor/practicas/`.
- Zips de apoyo para ejercicios Pandas/Polars/R.

## 05-recursos/

- Datasets: titanic, flights, penguins, spotify, online_retail.
- Gráficos demo y HTML exportados.
- Comparativas EDA (`.md`): Pandas, DuckDB, cuDF.
- `Seaborn_MegaChuleta.ipynb` — referencia interactiva.

## 90-archivo/

Material conservado fuera del flujo principal:

- `NLP_old/` — material antiguo de NLTK.
- `alternativas-R/` — notebooks y chuletas de R.
- `ud3-content/` — documento de UD3 archivado aquí.
- `fireducks/` — FireDucks como curiosidad técnica, no alternativa central.

## spaCy / NLP

El material spaCy salió de UD2 porque pertenece al bloque NLP. Está ahora en:

- `../04-deep-learning/02-ejemplos/nlp-spacy/`
- `../04-deep-learning/99-profesor/nlp-spacy/`

## 99-profesor/

Soluciones separadas del material de alumno:

- `ejemplos/` — notebooks DOCENTE.
- `practicas/` — soluciones de prácticas, con solución y tests fusionados cuando existían ambas versiones.

## Evaluaciones

- Pendiente: integrar rúbricas y/o cuestionarios en `04-evaluacion/`.
