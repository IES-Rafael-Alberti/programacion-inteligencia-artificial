# Preparación del entorno R

Este itinerario usa R como ampliación opcional de UD2. El objetivo no es sustituir Python/Pandas, sino reconocer y resolver tareas habituales con paquetes habituales del ecosistema R para datos.

## Herramientas recomendadas

| Herramienta | Uso |
|---|---|
| R | Lenguaje de trabajo |
| RStudio o Positron | Entorno cómodo para R/R Markdown |
| R Markdown o Quarto | Informes reproducibles |
| tidyverse | Lectura, transformación y visualización |

## Paquetes mínimos

```r
install.packages(c("dplyr", "ggplot2", "tibble", "lubridate", "rmarkdown", "knitr"), repos = "https://cloud.r-project.org")
```

En cada práctica:

```r
library(dplyr)
library(ggplot2)
library(tibble)
library(lubridate)
```

## Dataset

Se usa Titanic desde:

`../../05-recursos/datasets/titanic.csv`

Si el fichero no está disponible en el entorno de ejecución, el profesorado debe facilitar una copia junto al `.Rmd`.

## Resultado esperado

Al terminar, el alumnado debe poder abrir un `.Rmd`, ejecutar los bloques, interpretar errores básicos y explicar qué operación de Pandas equivale a cada operación de `dplyr`.

> Nota: la lectura de CSV se hace con `read.csv()` de R base para evitar depender de `readr` si hay problemas de compilación.
