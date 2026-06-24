# 🧩 UD2 – Programación Avanzada y Lenguajes Alternativos (Python II / R)

## 1. Problema de partida
En la UD1 aprendimos a escribir programas básicos en Python.  
Sin embargo, cuando los datos crecen o necesitamos automatizar análisis más complejos (por ejemplo, comparar miles de calificaciones o procesar registros de sensores), el enfoque básico deja de ser eficiente.  

Además, en el entorno profesional es habitual combinar Python con otros lenguajes como **R**, especialmente en análisis estadístico, bioinformática o investigación.  

👉 Surge la necesidad de **aprender a manejar estructuras avanzadas de Python y conocer un segundo lenguaje orientado al análisis de datos: R.**

---

## 2. Justificación de la unidad
Esta unidad amplía las bases adquiridas en la UD1 para dar el siguiente paso:  
- Dominar **estructuras de datos avanzadas** (listas anidadas, tuplas, diccionarios y conjuntos).  
- Comprender **la modularidad y reutilización del código**.  
- Introducir el trabajo con **ficheros y entornos de datos externos**.  
- Explorar **R** como lenguaje complementario en el análisis de datos.  

El alumno verá cómo ambos lenguajes, **Python y R**, se utilizan en entornos reales de ciencia de datos y aprendizaje automático, con objetivos y fortalezas distintos.

---

## 3. Objetivos específicos
- Utilizar estructuras avanzadas de datos en Python.  
- Manejar archivos de texto y formatos estructurados (CSV, JSON, XML).  
- Escribir y reutilizar funciones, módulos y scripts.  
- Trabajar con excepciones y depuración.  
- Introducir los fundamentos del lenguaje **R** y su entorno (RStudio).  
- Comparar las capacidades de Python y R en el tratamiento de datos.  

---

## 4. Contenidos

### 🔹 Semana 3 – Estructuras avanzadas y modularidad
- Listas anidadas, tuplas y diccionarios.  
- Métodos y comprensión de listas/diccionarios.  
- Definición de funciones con parámetros variables (`*args`, `**kwargs`).  
- Modularización: creación e importación de módulos propios.  
- Manejo de excepciones (`try`, `except`, `finally`).

### 🔹 Semana 4 – Archivos y datos estructurados
- Lectura y escritura de ficheros de texto y CSV.  
- Introducción al formato **JSON**: lectura, escritura y conversión.  
- Introducción al formato **XML**: estructura, nodos y parsing con `ElementTree`.  
- Scripts automatizados y tratamiento de errores.

### 🔹 Semana 5 – Introducción al lenguaje R
- Instalación y entorno de trabajo (R y RStudio).  
- Sintaxis básica de R: variables, vectores, listas, data frames.  
- Operadores y estructuras de control.  
- Funciones básicas de estadística descriptiva en R.

### 🔹 Semana 6 – Comparativa Python vs R
- Casos prácticos de análisis de datos en ambos lenguajes.  
- Similitudes y diferencias: tipado, librerías, ecosistemas.  
- Integración de resultados: uso de archivos CSV y JSON como puente.  
- Reflexión: ¿cuándo conviene usar Python? ¿cuándo R?

---

## 5. Herramientas
- **Python 3.12+**  
  - Jupyter Notebook o VSCode.  
  - Librerías: `numpy`, `pandas`, `json`, `xml.etree.ElementTree`.  
- **R 4.3+**  
  - RStudio (interfaz recomendada).  
  - Paquetes básicos: `tidyverse`, `readr`, `ggplot2`.  

*(Ambos lenguajes pueden usarse en local o en Colab/RStudio Cloud).*

---

## 6. Actividades propuestas

### 🔸 Semana 3
**Actividad 1:**  
Escribir un script en Python que lea una lista de alumnos y sus calificaciones, calcule la media por alumno y la nota máxima y mínima de la clase.

**Actividad 2 (individual):**  
Crear una función que reciba una lista de diccionarios (alumnos y notas) y devuelva estadísticas (media, máximo, mínimo, número de aprobados).

---

### 🔸 Semana 4
**Actividad 3:**  
Leer un archivo CSV con datos de productos (nombre, categoría, precio, stock) y generar un nuevo archivo JSON con los artículos que estén por debajo del stock mínimo.

**Actividad 4 (en parejas):**  
Crear un módulo Python (`inventario.py`) con funciones para añadir, eliminar y listar productos. Usar excepciones para validar entradas erróneas.

---

### 🔸 Semana 5
**Actividad 5:**  
Realizar en R un análisis básico de un dataset (por ejemplo, `iris` o `mtcars`):  
- Calcular media, desviación y resumen estadístico.  
- Representar gráficamente una variable (histograma o boxplot).

---

### 🔸 Semana 6
**Actividad 6 (comparativa final):**  
Analizar el mismo dataset en **Python (pandas)** y en **R (tidyverse)** y responder:  
- ¿Qué lenguaje ha resultado más sencillo?  
- ¿Cuál ofrece más visualización?  
- ¿Qué ventajas/desventajas tiene cada entorno?

---

## 7. Evaluación (RA/CE vinculados)

| **RA** | **Criterios de evaluación (CE)** | **Instrumentos** |
|:------:|:--------------------------------|:----------------|
| **RA1.b–e** | Desarrolla programas utilizando estructuras de datos, funciones y módulos. | - Notebooks individuales<br>- Actividades prácticas en Python |
| **RA1.f** | Emplea lenguajes de marcado y estructuras de datos externas (JSON, XML). | - Ejercicio de lectura/escritura de archivos |
| **RA1.e (comparativo)** | Analiza ventajas e inconvenientes de distintos lenguajes para IA. | - Informe comparativo Python–R |

📊 **Instrumentos de evaluación**
- Ejercicios entregables en Moodle.  
- Observación directa del trabajo en clase y participación.  
- Cuestionario Moodle con preguntas teórico-prácticas.  
- Informe comparativo final (Python vs R).

---

## 8. Recursos
- Libro: *Python for Data Analysis* (Wes McKinney, O’Reilly, 2022).  
- Libro: *R for Data Science* (Hadley Wickham, 2ª ed., O’Reilly, 2023).  
- Documentación oficial:  
  - [https://docs.python.org](https://docs.python.org)  
  - [https://cran.r-project.org](https://cran.r-project.org)  
- Tutoriales recomendados:  
  - W3Schools Python & R Basics.  
  - Kaggle: Python vs R for Data Science.

---

## 9. Conclusión
Esta unidad consolida la base de programación iniciada en la UD1 y amplía la visión del alumno hacia entornos de análisis de datos reales.  
El dominio de estructuras, modularización y manipulación de datos es esencial antes de abordar la automatización y los modelos de Machine Learning que vendrán en las siguientes unidades.