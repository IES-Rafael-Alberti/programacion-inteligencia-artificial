
---
title: "EDA Visual – Cuaderno de Prácticas Integradas / Visual EDA – Integrated Practice Workbook"
subtitle: "Guía Docente / Teaching Guide"
author: "Módulo: Programación de Inteligencia Artificial (PIA)"
date: "Curso 2025-2026"
geometry: margin=2.5cm
fontsize: 11pt
---

# EDA Visual – Cuaderno de Prácticas Integradas / Visual EDA – Integrated Practice Workbook
## Guía Docente / Teaching Guide

### 1. Propósito y contextualización

Este cuaderno recoge una serie de prácticas integradas diseñadas para trabajar los fundamentos del **análisis exploratorio de datos (EDA)** y la **visualización en entornos de Inteligencia Artificial**, utilizando librerías del ecosistema Python.

**Objetivos:**
- Consolidar el uso de librerías esenciales (NumPy, pandas, Seaborn, Matplotlib, Plotly Express).
- Aplicar el pensamiento analítico en contextos visuales.
- Preparar al alumnado para realizar análisis exploratorios en proyectos reales (RA2).

**Notebook asociado:** `EDA_Visual_Practicas.ipynb`

---

### 2. Relación con Resultados de Aprendizaje y Criterios de Evaluación

| Resultado de Aprendizaje | Criterios de Evaluación Vinculados | Bloques relacionados |
|----------------------------|------------------------------------|----------------------|
| **RA1.** Caracteriza lenguajes y entornos de programación de IA. | a), b), d) | 2. NumPy – 3. pandas |
| **RA2.** Desarrolla aplicaciones utilizando entornos de modelado de IA. | c), e), f) | 4. Seaborn – 5. Matplotlib – 6. Plotly – 7. Proyecto EDA libre |

---

### 3. Guía paso a paso

#### **Bloque 1. Descarga automática de datasets**
**Objetivo:** Garantizar la disponibilidad de datasets reales y diversos.  
**Pasos:**
1. Ejecutar la celda de descarga. Los ficheros se guardan en `datasets/`.
2. Verificar que el listado de datasets incluye Spotify, Titanic, Penguins, Flights, Happiness y Netflix.
3. Comentar al alumnado la importancia de validar la estructura de los datos tras la carga.

**Notas docentes:** Si alguna URL falla, ofrecer la alternativa de carga manual desde el repositorio del centro o GitHub Classroom.

---

#### **Bloque 2. NumPy — Operaciones y análisis numérico**
**Objetivo:** Reforzar el trabajo con arrays, máscaras y estadísticos básicos.

**Pasos:**
1. Crear un array 4×4 y extraer su diagonal principal.  
2. Generar 1000 valores aleatorios con distribución normal `N(0,1)` y calcular media y desviación.  
3. Calcular cuadrados de una lista sin usar bucles.  
4. **Ejercicio ampliado:** simular 10.000 lanzamientos de dado y estimar la probabilidad `P(X > 4)`.

**Notas docentes:** Insistir en la diferencia entre operaciones vectorizadas y bucles explícitos.  
**Errores comunes:** uso incorrecto de `np.random.randint` (rangos inclusivos/exclusivos).

---

#### **Bloque 3. pandas — Titanic (EDA estructurado)**
**Objetivo:** Familiarizarse con estructuras tabulares, tipos de datos y operaciones básicas de agrupación.

**Pasos:**
1. Cargar el dataset `titanic.csv` y revisar información general con `info()` y `isna().sum()`.  
2. Calcular tasas de supervivencia agrupando por `Pclass` y `Sex`.  
3. Crear una nueva columna `IsChild = Age < 12` y analizar la supervivencia por clase y grupo de edad.  

**Notas docentes:**  
- Introducir el uso de `groupby()` y `agg()` para estadísticas múltiples.  
- Explicar `assign()` como método funcional para añadir columnas.  
- Si hay muchos valores nulos en `Age`, usar `fillna()` con la media o mediana.

---

#### **Bloque 4. Seaborn — Spotify 2023 (EDA visual)**
**Objetivo:** Realizar un análisis exploratorio visual de datos reales musicales.

**Pasos:**
1. Cargar `spotify_2023.csv` y normalizar nombres de columnas.  
2. Analizar la distribución de `popularity` con `histplot`.  
3. Calcular y representar la popularidad media por género (top 8).  
4. Representar la relación entre `popularity` y `danceability` mediante `scatterplot`.  
5. Añadir un `lmplot` con `hue=genre` para observar tendencias por género.

**Notas docentes:**  
- Destacar el papel de la estética (`palette`, `style`) en la comunicación de datos.  
- Reforzar la interpretación de correlaciones visuales.  
- Promover la comparación entre gráficos estáticos (Seaborn) y los interactivos (Plotly).

---

#### **Bloque 5. Matplotlib — Penguins (personalización y exportación)**
**Objetivo:** Comprender la personalización avanzada y la exportación profesional de gráficos.

**Pasos:**
1. Cargar el dataset `penguins.csv` y eliminar valores nulos.  
2. Crear un diagrama de dispersión `Flipper length vs Body mass`.  
3. Añadir una anotación con `annotate()`.  
4. Guardar el gráfico en alta resolución (300 DPI) con `savefig()`.  
5. Cambiar estilo global a `ggplot` y añadir línea horizontal de referencia (`axhline`).

**Notas docentes:**  
- Resaltar cómo los estilos predefinidos afectan a la percepción visual.  
- Mostrar cómo los ejes, anotaciones y líneas de referencia ayudan a contextualizar los datos.  
- Evitar el uso excesivo de colores o decoraciones innecesarias.

---

#### **Bloque 6. Plotly Express — Flights (visualización interactiva)**
**Objetivo:** Introducir gráficos interactivos y visualización temporal.

**Pasos:**
1. Cargar `flights.csv`.  
2. Crear una gráfica de líneas con `px.line()` mostrando pasajeros por mes y año.  
3. Crear un mapa de calor de estacionalidad mediante `pivot_table` + `px.imshow()` o `px.density_heatmap()`.

**Notas docentes:**  
- Mostrar cómo `hover` y `zoom` mejoran la exploración de datos.  
- Comparar la sencillez de `Plotly Express` con el control detallado de Matplotlib.  
- Subrayar la importancia de la interactividad en la narrativa de datos.

---

#### **Bloque 7. Proyecto EDA libre**
**Objetivo:** Aplicar de manera integrada los conocimientos adquiridos en un análisis exploratorio real.

**Requisitos mínimos:**
- Utilizar al menos cuatro tipos de gráficos (univariante, bivariante, categórico, multivariante).  
- Incluir texto explicativo con conclusiones tras cada bloque.  
- Exportar al menos un gráfico en formato PNG o PDF con alta resolución.  

**Datasets sugeridos:**  
Spotify 2023, Titanic, Penguins, Flights, Happiness, Netflix.

**Criterios de evaluación sugeridos:**
| Aspecto | Indicadores |
|----------|-------------|
| Variedad de gráficos | Utiliza al menos 4 tipos distintos correctamente. |
| Interpretación analítica | Las conclusiones son coherentes con las visualizaciones. |
| Claridad y estética | Los gráficos son legibles, con etiquetas y títulos informativos. |
| Documentación del proceso | Explica los pasos y decisiones del análisis. |

**Notas docentes:** Recomendar que los estudiantes trabajen en parejas para fomentar el debate analítico. Si se usa Colab, recordar guardar las figuras antes de cerrar sesión.

---

#### **Bloque 8. Explorador de datasets (opcional)**
**Objetivo:** Permitir la exploración libre de los datasets descargados.  
**Pasos:**
1. Ejecutar `os.listdir("datasets")` para listar los ficheros.  
2. Cargar el dataset elegido con `pd.read_csv()`.  
3. Visualizar las primeras filas y verificar estructura.

**Notas docentes:** Este bloque sirve como preparación para proyectos de IA y Big Data, donde los alumnos deben aprender a identificar estructuras y variables relevantes.

---

### 4. Consideraciones finales

Este cuaderno puede emplearse como:
- Recurso de consolidación tras la enseñanza de librerías individuales.  
- Actividad de refuerzo previa a un proyecto mayor de análisis de datos.  
- Ejercicio de evaluación práctica para los RA1 y RA2 del módulo PIA.

Se recomienda integrar las correcciones en sesiones de tutoría, mostrando ejemplos de buenas prácticas y destacando la importancia del rigor analítico y la comunicación visual.
