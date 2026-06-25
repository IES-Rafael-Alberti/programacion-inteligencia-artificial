---
title: "Matplotlib – Mega Chuleta (Parte 2: Personalización y Anotaciones)"
author: "Curso de Especialización en Inteligencia Artificial y Big Data"
subtitle: "Programación de Inteligencia Artificial — Visualización avanzada con Matplotlib"
date: "2025-11-04"
geometry: margin=2cm
output: pdf_document
fontsize: 11pt
header-includes:
  - |
    \usepackage{graphicx}
    \usepackage{float}
    \usepackage{fancyhdr}
    \fancyhead[R]{\includegraphics[height=1.5cm]{images/logo-centro.png}}
    \pagestyle{fancy}
---

# Matplotlib – Mega Chuleta (Parte 2)

> 💬 Esta parte continúa la **Mega Chuleta de Matplotlib (Parte 1)** y se centra en la **personalización, anotaciones, estilos y presentación visual** de gráficos.

---

## Personalización visual avanzada

💡 **Idea clave:** Matplotlib permite personalizar prácticamente todos los elementos de un gráfico: colores, estilos de línea, transparencia y fuentes.

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.style.use('seaborn-v0_8-whitegrid')  # Estilo base

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
plt.scatter(tips["total_bill"], tips["tip"], c=tips["size"], cmap="viridis", alpha=0.7, edgecolors="black")
plt.title("Relación entre total y propina")
plt.xlabel("Total de la cuenta ($)")
plt.ylabel("Propina ($)")
plt.colorbar(label="Tamaño de grupo")
plt.show()
```

✅ **Consejo:** Usa `alpha` para transparencia y `cmap` para paletas automáticas.

🧩 **Ejercicio:** Cambia el estilo a `ggplot` o `dark_background` con `plt.style.use('ggplot')` y observa las diferencias.

---

## Anotaciones y texto

💡 **Idea clave:** Usa `plt.text()` para colocar texto libre y `plt.annotate()` para destacar puntos con flechas o etiquetas explicativas.

```python
plt.figure(figsize=(6,4))
plt.scatter(tips["total_bill"], tips["tip"], alpha=0.6)
plt.title("Ejemplo de anotaciones")
plt.xlabel("Total de la cuenta ($)")
plt.ylabel("Propina ($)")

plt.text(45, 2, "Valor alto", fontsize=10, color="red")
plt.annotate("Propina inusualmente alta",
             xy=(40, 8), xytext=(25, 10),
             arrowprops=dict(facecolor="black", shrink=0.05, width=1))

plt.show()
```

✅ **Consejo:** Usa `xycoords='data'` o `'axes fraction'` para posicionar texto en coordenadas relativas.

🧩 **Ejercicio:** Añade una segunda anotación marcando el punto con mayor `total_bill` del dataset.

---

## Leyendas y títulos

💡 **Idea clave:** Las leyendas ayudan a interpretar los datos; deben colocarse donde no obstruyan la visualización.

```python
plt.figure(figsize=(6,4))
for day, df_day in tips.groupby("day"):
    plt.scatter(df_day["total_bill"], df_day["tip"], label=day, alpha=0.6)

plt.title("Propinas por día de la semana", fontsize=14, fontweight="bold")
plt.xlabel("Total ($)")
plt.ylabel("Propina ($)")
plt.legend(title="Día", loc="upper left", fontsize=9, title_fontsize=10)
plt.show()
```

✅ **Consejo:** Usa `bbox_to_anchor` para mover la leyenda fuera del gráfico.

🧩 **Ejercicio:** Coloca la leyenda fuera del gráfico (`loc='center left', bbox_to_anchor=(1, 0.5)`).

---

## Cuadrículas, líneas y fondos

💡 **Idea clave:** Las cuadrículas, líneas y colores de fondo ayudan a resaltar información o tendencias.

```python
flights = sns.load_dataset("flights")
pivot = flights.pivot_table(values="passengers", index="month", columns="year")

plt.figure(figsize=(8,4))
plt.plot(pivot[1949], label="1949", linestyle="--")
plt.plot(pivot[1960], label="1960", linestyle="-", linewidth=2)

plt.title("Comparación de pasajeros por año")
plt.xlabel("Mes")
plt.ylabel("Pasajeros")
plt.grid(True, linestyle="--", alpha=0.5)
plt.axhline(y=350, color="red", linestyle=":", label="Referencia")
plt.legend()
plt.show()
```

✅ **Consejo:** Usa `axhline`, `axvline`, `axhspan`, `axvspan` para marcar rangos o umbrales.

🧩 **Ejercicio:** Añade un fondo gris claro con `plt.gca().set_facecolor('whitesmoke')`.

---

## Guardado y exportación profesional

💡 **Idea clave:** Usa `plt.savefig()` para exportar gráficos en alta calidad con control de DPI y márgenes.

```python
plt.figure(figsize=(6,4))
sns.barplot(data=tips, x="day", y="total_bill", palette="pastel")
plt.title("Gasto medio por día")

plt.tight_layout()
plt.savefig("gasto_medio_dia.png", dpi=300, bbox_inches="tight")
plt.show()
```

✅ **Consejo:** Usa `bbox_inches="tight"` para evitar cortes y `dpi>=300` para publicaciones.

🧩 **Ejercicio:** Exporta el gráfico en formato PDF y SVG y compara la nitidez al hacer zoom.

---

## Bonus: Estilos globales y paletas corporativas

💡 **Idea clave:** Los estilos globales y las paletas personalizadas mejoran la coherencia visual de informes y dashboards.

### Cambiar estilos globales

```python
plt.style.use('seaborn-v0_8-darkgrid')
# plt.style.use('ggplot')
# plt.style.use('dark_background')
```

### Crear tu propio estilo `.mplstyle`

Crea un archivo `mi_estilo.mplstyle` con:

```
axes.titlesize : 14
axes.labelsize : 12
lines.linewidth : 2
font.family : sans-serif
figure.facecolor : white
```
y aplícalo con:
```python
plt.style.use('mi_estilo.mplstyle')
```

### Paletas corporativas o personalizadas

```python
from matplotlib import cm
from matplotlib.colors import ListedColormap

colores_empresa = ["#003366", "#6699CC", "#FFCC00"]
cmap_empresa = ListedColormap(colores_empresa)

plt.figure(figsize=(6,3))
sns.barplot(data=tips, x="day", y="tip", palette=colores_empresa)
plt.title("Ejemplo con paleta corporativa")
plt.show()
```

✅ **Consejo:** Si trabajas en un entorno profesional, adapta las paletas a la **identidad visual de la empresa o institución** (colores corporativos, logotipos, tipografías coherentes).

---

> 📘 **Resumen rápido:**
> - Personaliza con `style`, `alpha`, `linewidth`, `font`, `grid`.
> - Usa `annotate()` para destacar insights.
> - Controla leyendas y títulos con `loc`, `fontsize`, `bbox_to_anchor`.
> - Exporta con `savefig()` en alta calidad.
> - Aplica estilos y paletas corporativas para informes consistentes.
