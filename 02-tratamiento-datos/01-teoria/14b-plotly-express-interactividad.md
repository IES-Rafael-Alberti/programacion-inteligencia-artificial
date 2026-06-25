# 14b — Plotly Express: interactividad rápida para EDA

Plotly Express es un complemento práctico después de dominar Pandas, Matplotlib y Seaborn. No sustituye a Matplotlib como base conceptual: se usa cuando interesa explorar datos con gráficos interactivos de forma rápida.

## Cuándo usar Plotly

- Explorar datos con zoom, hover y filtros visuales.
- Crear gráficos interactivos para notebooks o HTML.
- Presentar resultados cuando la interacción aporta valor.
- Prototipar dashboards sencillos antes de usar herramientas más completas.

## Cuándo NO usarlo

- Para aprender los fundamentos de la visualización: primero Matplotlib.
- Para EDA estadístico rápido: normalmente Seaborn es más directo.
- Para gráficos estáticos simples que no necesitan interacción.
- Si el tamaño del dataset hace que el navegador vaya lento.

## Patrón básico

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("datos.csv")

fig = px.scatter(
    df,
    x="x",
    y="y",
    color="categoria",
    hover_data=["nombre"],
    title="Relación entre x e y"
)

fig.show()
```

## Gráficos habituales

| Necesidad | Función |
|-----------|---------|
| Dispersión | `px.scatter()` |
| Barras | `px.bar()` |
| Líneas temporales | `px.line()` |
| Histogramas | `px.histogram()` |
| Boxplots | `px.box()` |
| Mapas de calor | `px.imshow()` |

## Relación con la unidad

- Core previo: Pandas + Matplotlib + Seaborn.
- Notebook asociado: `../02-ejemplos/17_plotly_express_interactivo.ipynb`.
- Práctica integrada: `../02-ejemplos/18_mini_eda_matplotlib_plotly.ipynb`.

## Idea clave

Plotly aporta interactividad, no fundamentos. Si el alumno no sabe explicar qué representa un gráfico en Matplotlib/Seaborn, Plotly solo añade brillo encima de una base débil.
