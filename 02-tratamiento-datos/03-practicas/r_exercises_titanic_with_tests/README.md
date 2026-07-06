# Itinerario opcional R — Titanic

Este bloque permite trabajar los mismos conceptos de tratamiento de datos desde R, comparándolos con el flujo principal de la unidad en Python/Pandas.

## Decisión docente

- **Estado:** material opcional de ampliación.
- **Rol:** contraste Pandas ↔ dplyr para alumnado que quiera ver R como herramienta de análisis de datos.
- **No sustituye** al eje obligatorio de UD2: Python, Pandas, Matplotlib y Seaborn.
- **Uso recomendado:** refuerzo, ampliación o comparación metodológica, no práctica principal si el grupo aún no domina Pandas.

## Camino rápido

1. Leer `00D-Chuleta-R.md` para ver equivalencias básicas Pandas ↔ dplyr.
2. Trabajar los `.Rmd` de alumnado en orden:
   - `00_Intro_R_alumnos.Rmd`
   - `01_Filter_Index_R_alumnos.Rmd`
   - `02_GroupApply_R_alumnos.Rmd`
   - `03_Merge_R_alumnos.Rmd`
   - `04_TimeSeries_R_alumnos.Rmd`
   - `05_Visualization_R_alumnos.Rmd`
3. Comparar cada operación con su equivalente en Pandas.
4. Evaluar sólo si el profesorado decide activar este itinerario.

## Qué cubre

| Bloque | Concepto UD2 | Equivalencia aproximada |
|---|---|---|
| Introducción | lectura, estructura y tipos | `read_csv`, `head`, `str` |
| Filtrado e índices | selección de filas y columnas | `filter`, `select` |
| Agrupación | agregaciones y resúmenes | `group_by`, `summarise` |
| Merge | combinación de tablas | `left_join`, `inner_join` |
| Series temporales | fechas y orden temporal | parsing y operaciones con fecha |
| Visualización | EDA visual | `ggplot2` |

## Evaluación

Si se usa como actividad evaluable, aplicar la rúbrica general de UD2 adaptando las evidencias:

- carga y comprensión del dataset;
- limpieza y transformación;
- EDA, visualización y análisis;
- reproducibilidad y claridad del informe.

No debe evaluarse por “saber R” de memoria, sino por transferir correctamente los conceptos de tratamiento de datos.

## Material del profesorado

Las versiones de profesor están en:

`../../99-profesor/practicas/`
