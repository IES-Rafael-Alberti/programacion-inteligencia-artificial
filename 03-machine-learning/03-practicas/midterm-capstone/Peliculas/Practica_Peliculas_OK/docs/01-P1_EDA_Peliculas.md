# Práctica 1 — Exploración y comprensión del dataset de películas

## Contexto
En esta práctica trabajarás con un dataset de películas que ya ha sido construido
a partir de fuentes externas. El único snapshot autorizado es
`data/movies.csv`: P1 usa la misma ruta portátil que P2 y P3, por lo que puede
abrirse desde la raíz o desde la carpeta del notebook.

Antes de empezar, el profesorado debe generar y validar el snapshot según el
[contrato de datos](../DATASET_CONTRACT.md). No sustituyas el fichero por la
salida bruta de Lab1 ni lo regeneres durante la práctica.

Antes de aplicar modelos de Inteligencia Artificial, es imprescindible comprender
los datos, detectar problemas y formular preguntas relevantes.

## Objetivos
- Comprender la estructura del dataset
- Detectar problemas de calidad de datos
- Realizar un análisis exploratorio con sentido
- Extraer conclusiones útiles para el modelado posterior

## Tareas a realizar

### 1. Inspección inicial
- Número de filas y columnas
- Tipos de datos
- Valores nulos
- Duplicados

### 2. Limpieza básica
- Tratamiento de valores nulos
- Eliminación de columnas irrelevantes
- Conversión de tipos si es necesario

### 3. Análisis exploratorio (EDA)
Realiza visualizaciones que respondan a preguntas como:
- Distribución de películas por año
- Distribución por género
- Relación entre duración y valoración
- Detección de valores atípicos

### 4. Conclusiones
Incluye una sección final con:
- Principales hallazgos
- Problemas detectados en los datos
- Variables que consideras útiles para modelos
- Variables que descartarías

## Entregable
Notebook: `P1_EDA_base.ipynb`