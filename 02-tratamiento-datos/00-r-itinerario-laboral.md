# Decisión — Itinerario R con suficiencia profesional básica

## Veredicto

El material R actual de UD2 **no es suficiente todavía** para que el alumnado pueda defenderse con R en un entorno de trabajo donde se use de forma habitual.

Sí sirve como **primer contacto** para alumnado que viene de Python/Pandas, pero necesita ampliarse si el objetivo es competencia operativa mínima.

## Evidencia revisada

Material activo revisado:

- `03-practicas/r_exercises_titanic_with_tests/00D-Chuleta-R.md`
- `03-practicas/r_exercises_titanic_with_tests/00_Intro_R_alumnos.Rmd`
- `03-practicas/r_exercises_titanic_with_tests/01_Filter_Index_R_alumnos.Rmd`
- `03-practicas/r_exercises_titanic_with_tests/02_GroupApply_R_alumnos.Rmd`
- `03-practicas/r_exercises_titanic_with_tests/03_Merge_R_alumnos.Rmd`
- `03-practicas/r_exercises_titanic_with_tests/04_TimeSeries_R_alumnos.Rmd`
- `03-practicas/r_exercises_titanic_with_tests/05_Visualization_R_alumnos.Rmd`

Resultado de la revisión:

| Competencia | Estado actual | Veredicto |
|---|---|---|
| Leer datos con R | Aparece `read_csv()` | Suficiente como inicio |
| Inspeccionar estructura | Aparece `head()`/`str()` en chuleta | Básico |
| Seleccionar columnas | Aparece `select()` | Básico |
| Filtrar filas | Aparece `filter()` | Básico |
| Crear variables | Aparece en chuleta con `mutate()`, pero no como práctica sólida | Insuficiente |
| Agrupar y resumir | Documentado en chuleta, pero no practicado con profundidad | Insuficiente |
| Joins | Nombrado en README, pero sin práctica real detectada | Insuficiente |
| Fechas / series temporales | Fichero existente, pero sin práctica real suficiente detectada | Insuficiente |
| Visualización con `ggplot2` | Nombrado en README, pero sin práctica real detectada | Insuficiente |
| EDA completo | No hay práctica R completa activa comparable a Pandas | Insuficiente |
| Comunicación de resultados | No hay entrega específica en R | Insuficiente |

## Decisión docente

R debe seguir siendo **opcional**, pero si se mantiene por empleabilidad debe tener un itinerario mínimo más serio.

No se trata de convertir UD2 en una unidad de R. Se trata de que una persona que ya entiende Pandas pueda reconocer y resolver tareas básicas en R si llega a un equipo donde se use R/tidyverse.

## Competencia mínima deseable

Al terminar el itinerario opcional, el alumnado debería poder:

1. abrir un proyecto/notebook R y ejecutar código básico;
2. cargar CSV/XLSX con `readr` o equivalente;
3. inspeccionar estructura, tipos y valores perdidos;
4. seleccionar, filtrar y ordenar datos con `dplyr`;
5. crear variables con `mutate()`;
6. agrupar y resumir con `group_by()` + `summarise()`;
7. unir tablas con `left_join()`;
8. hacer gráficos básicos con `ggplot2`;
9. construir un mini-EDA reproducible;
10. explicar las equivalencias principales Pandas ↔ dplyr.

## Ampliación mínima propuesta

Crear o rehacer el itinerario R activo con estas piezas:

| Pieza | Propósito | Prioridad |
|---|---|---|
| `00_instalacion_y_entorno_R.md` | R, RStudio/Quarto/Jupyter, paquetes mínimos | Media |
| `01_titanic_basico_R.Rmd` | lectura, estructura, selección, filtros | Alta |
| `02_titanic_transformacion_R.Rmd` | `mutate`, missing values, factores/categorías | Alta |
| `03_titanic_agrupaciones_R.Rmd` | `group_by`, `summarise`, tablas comparativas | Alta |
| `04_titanic_visualizacion_R.Rmd` | `ggplot2`: barras, histogramas, boxplots, facetas | Alta |
| `05_titanic_eda_R.Rmd` | mini-EDA completo con conclusiones | Alta |
| `06_comparativa_pandas_dplyr.md` | tabla de equivalencias operativas | Alta |

## Evaluación si se activa

No conviene evaluarlo con un examen de sintaxis. Debe evaluarse con una entrega breve:

- notebook/Rmd ejecutable;
- 4–6 operaciones de transformación justificadas;
- 3 visualizaciones útiles;
- conclusiones escritas;
- comparación explícita con Pandas.

## Estado

Implementación mínima aplicada en `03-practicas/r_exercises_titanic_with_tests/`: carga, filtrado, transformación, agrupación, joins, fechas, visualización, mini-EDA y comparativa Pandas ↔ dplyr. Queda pendiente probar ejecución real en un entorno R si se va a usar en clase.
