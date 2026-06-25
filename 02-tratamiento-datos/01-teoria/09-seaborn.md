---
title: "Seaborn – Mega Chuleta (EDA rápido y gráficos estadísticos)"
author: "Curso de Especialización en Inteligencia Artificial y Big Data"
subtitle: "Programación de Inteligencia Artificial — Visualización con Seaborn"
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

# Seaborn – Mega Chuleta (EDA rápido y gráficos estadísticos)

> 💬 **Qué es:** Seaborn es una librería de alto nivel construida sobre **Matplotlib** y **Pandas** que facilita la creación de gráficos estadísticos con **menos código y mejor estética**.
>
> 🎯 **Para qué sirve:** EDA rápido, comparaciones entre variables, análisis por categorías, correlaciones y regresiones.
>
> 🔁 **Diferencias con Matplotlib:** Matplotlib es bajo nivel (control fino). Seaborn añade **abstracciones estadísticas** (agregaciones, estimadores, faceteado) y estilos por defecto.

---

## Configuración y carga de datos

💡 **Idea clave:** Establece tema/estilo y paleta al inicio. Usa `load_dataset` para datasets de ejemplo.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")           # Estilo base
sns.set_palette("deep")                    # Paleta por defecto
tips = sns.load_dataset("tips")
penguins = sns.load_dataset("penguins")    # para el bonus EDA final
```

✅ **Consejo:** Cambia la paleta cuando quieras con `sns.set_palette("pastel")` o por gráfico con `palette="muted"`.

🧩 **Ejercicio:** Cambia a `sns.set_theme(style="darkgrid")` y compara.

---

## Gráficos univariantes (distribuciones)

💡 **Selecciona la forma de visualizar una variable** según el contexto (frecuencias, densidad o cuartiles).

### Histograma / KDE (distribución continua)

```python
sns.set_palette("pastel")
fig, ax = plt.subplots(1,2, figsize=(10,4))
sns.histplot(data=tips, x="total_bill", bins=25, kde=True, ax=ax[0])
sns.kdeplot(data=tips, x="total_bill", fill=True, ax=ax[1])
ax[0].set_title("Histograma + KDE (pastel)")
ax[1].set_title("Densidad KDE (pastel)")
plt.show()
```

### Boxplot / Violinplot (distribución por categoría)

```python
sns.set_palette("muted")
fig, ax = plt.subplots(1,2, figsize=(10,4))
sns.boxplot(data=tips, x="day", y="total_bill", ax=ax[0])
sns.violinplot(data=tips, x="day", y="total_bill", inner="quartile", ax=ax[1])
ax[0].set_title("Boxplot (muted)")
ax[1].set_title("Violinplot (muted)")
plt.show()
```

✅ **Consejo:** Para muchos puntos, prueba `swarmplot` (muestra distribución discreta sin solaparse).

🧩 **Ejercicio:** Repite el violinplot coloreando por `hue="sex"` y usando `split=True`.

---

## Gráficos bivariantes y multivariantes

### Dispersión con hue/size/style

```python
sns.set_palette("deep")
sns.scatterplot(data=tips, x="total_bill", y="tip",
                hue="time", style="sex", size="size")
plt.title("Dispersión con hue / style / size")
plt.show()
```

### Regresión lineal (lmplot)

```python
sns.set_palette("coolwarm")
sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex", height=4, aspect=1.2)
plt.title("Regresión lineal por sexo (coolwarm)")
plt.show()
```

### Matriz de pares (pairplot)

```python
sns.set_palette("deep")
sns.pairplot(data=tips, vars=["total_bill","tip","size"], hue="sex")
plt.suptitle("Pairplot: relaciones entre variables", y=1.02)
plt.show()
```

### Mapas de calor (correlaciones)

```python
import numpy as np
corr = tips[["total_bill","tip","size"]].corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="YlGnBu", vmin=-1, vmax=1, center=0)
plt.title("Matriz de correlación (YlGnBu)")
plt.show()
```

✅ **Consejo:** Usa `hue` para una tercera variable categórica; `style` y `size` para añadir dimensiones extra.

🧩 **Ejercicio:** Crea `pairplot` de `penguins` con `hue="species"` y comenta diferencias entre especies.

---

## Gráficos categóricos y agregaciones

💡 **Idea clave:** Seaborn agrega automáticamente (media por defecto) y añade intervalos de confianza.

### Barras (agregación)

```python
sns.set_palette("deep")
sns.barplot(data=tips, x="day", y="total_bill", hue="sex", estimator="mean", errorbar="sd")
plt.title("Gasto medio por día y sexo (barras)")
plt.show()
```

### Conteos (frecuencias)

```python
sns.set_palette("pastel")
sns.countplot(data=tips, x="day", hue="sex")
plt.title("Número de cuentas por día y sexo (conteo)")
plt.show()
```

### catplot (faceteado rápido)

```python
sns.set_palette("muted")
g = sns.catplot(data=tips, x="day", y="tip", hue="sex", kind="box", col="time")
g.fig.suptitle("catplot con facetas por time", y=1.02)
plt.show()
```

✅ **Consejo:** Cambia el estimador con `estimator=np.median` o quita barras de error con `errorbar=None`.

🧩 **Ejercicio:** Usa `stripplot` encima de `boxplot` (parámetro `dodge=True`) para ver distribución + estadísticos.

---

## Control visual básico y personalización ligera

💡 **Seaborn depende de Matplotlib**. Puedes combinar funciones de ambos:
- Tema global: `sns.set_theme(style="whitegrid")`
- Paleta global: `sns.set_palette("deep")` o por gráfico `palette="pastel"`
- Contexto: `sns.set_context("talk")` (aumenta tamaño de fuentes para presentaciones)

```python
sns.set_theme(style="whitegrid", context="talk")
sns.barplot(data=tips, x="day", y="tip", palette="pastel")
plt.title("Control visual básico (context='talk')")
plt.show()
```

✅ **Consejo:** Para estilos muy personalizados, aplica `plt.style.use(...)` (ver Matplotlib Parte 2).

🧩 **Ejercicio:** Cambia el `context` a `"paper"` y compara tamaños de texto.

---

## Exportación y buenas prácticas

```python
plt.tight_layout()
plt.savefig("seaborn_ejemplo.png", dpi=300, bbox_inches="tight")
```

✅ **Buenas prácticas:**
- Usa títulos informativos que expliquen *qué se ve*.
- Limita el número de categorías visibles o usa facetas.
- Ajusta el `context` para presentaciones (`talk`) o informes (`paper`).

🧩 **Ejercicio:** Exporta también a PDF y compara nitidez al hacer zoom.

---

## Bonus: Mini‑EDA con `penguins` (multivariable)

💡 **Objetivo:** Responder: *¿Cómo varían medidas corporales entre especies? ¿Qué relaciones hay entre longitud de aleta y masa?*

```python
sns.set_theme(style="whitegrid")
sns.set_palette("deep")

# 1) Resumen rápido
print(penguins.describe(include="all"))

# 2) Distribución por especie (violin + strip)
fig, ax = plt.subplots(1,2, figsize=(12,4))
sns.violinplot(data=penguins, x="species", y="bill_length_mm", inner="quartile", ax=ax[0])
sns.stripplot(data=penguins, x="species", y="bill_length_mm", ax=ax[0], color="k", size=2, alpha=0.5)
ax[0].set_title("Longitud de pico por especie")

sns.boxplot(data=penguins, x="species", y="body_mass_g", ax=ax[1])
sns.stripplot(data=penguins, x="species", y="body_mass_g", color="k", size=2, alpha=0.4, ax=ax[1])
ax[1].set_title("Masa corporal por especie")
plt.show()

# 3) Relaciones multivariantes
sns.pairplot(data=penguins, vars=["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"], hue="species")
plt.suptitle("Pairplot de variables clave por especie", y=1.02)
plt.show()

# 4) Regresión y relación clave
sns.lmplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", height=4, aspect=1.3)
plt.title("Relación aleta vs masa por especie")
plt.show()

# 5) Correlaciones (numéricas)
corr = penguins[["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]].corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="YlGnBu", vmin=-1, vmax=1, center=0)
plt.title("Correlaciones en 'penguins'")
plt.show()
```

✅ **Conclusiones (ejemplo):**
- *Gentoo* tiende a mayor masa y aletas más largas; *Adelie* menor masa.
- Fuerte relación positiva entre **longitud de aleta** y **masa corporal**.

🧩 **Ejercicio final:** Añade `style="sex"` en la regresión para ver diferencias por sexo dentro de cada especie.

---

> 📘 **Resumen rápido:**
> - Seaborn simplifica EDA con funciones de alto nivel y buenas estéticas por defecto.
> - Usa `hue`, `col/row` (facetas) y `pairplot` para relaciones multivariantes.
> - Cambia `palette`, `style`, `context` según el medio (pantalla vs. papel).
