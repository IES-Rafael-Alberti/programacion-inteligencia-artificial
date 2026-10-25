# Guion de la séptima clase de PIA — instalar R en VS Code, comparativa y repaso de pandas

> **Documento interno del profesorado. Solo repositorio docente; no publicar en `main` del alumnado, GitHub Pages ni Moodle.**

**Duración de referencia:** 2 horas.

**Continuidad real de la sexta clase (20-10):** EDA con NumPy visto en su totalidad sobre empleados; creado el notebook `16-eda_numpy_edificios.ipynb` para que el alumnado haga su propio EDA. R no llegó a verse con RStudio: la página de descarga devolvía un XML en lugar de iniciar la descarga, así que se pasó a **instalar R directamente desde CRAN** y a **instalar los plugins de VS Code para R**. Pandas conserva solo lo ya presentado (Series, DataFrame e inicio de indexación).

**Situación de instalación en el alumnado:** hay mezcla de caminos. **Algunos ya tienen R instalado y también RStudio;** otros optaron por VS Code y **todavía se están peleando con plugins, kernels y dependencias de R no satisfechas**. La decisión para esta clase es **«si el lunes lo tienen todo listo, tiramos por local; si no, tiramos por Colab».**

## 1. Decisión de alcance (sesión más corta: 2 h)

- **R (plan doble, local o Colab):** si al menos una parte razonable del grupo tiene R listo localmente (RStudio o VS Code con kernel), trabajar la introducción con el notebook local `06_introduccion_R_fundamentos.ipynb` y la guía de instalación. Si hay muchos puestos sin resolver (plugins, kernels o dependencias de R pendientes), **no invertir la clase en instalaciones**: abrir R en **Google Colab** ([https://colab.research.google.com/notebook#create=true&language=r](https://colab.research.google.com/notebook#create=true&language=r)) desde el navegador y subir el notebook `06_introduccion_R_fundamentos.ipynb` con kernel R. Comprobar con una celda `R.version.string` y un `mean(..., na.rm = TRUE)`. Los paquetes instalados en Colab y los archivos generados pueden perderse al reiniciar el entorno; no es el camino para instalar nada.
- **R (breve):** 15 minutos de R base (vectores, indexación desde 1, `data.frame`, resumen) sobre el recorrido elegido (local o Colab), de forma que sirva de referencia real para la comparativa. Sin parcelas nuevas.
- **Comparativa de lenguajes y formatos (entregable):** ~35 minutos en clase con el enunciado y la plantilla. R recién visto (local o Colab) se compara con Python; Java/JavaScript se valoran por su papel en la aplicación, sin programarlos.
- **Pandas (repaso + continuación):** retomar Series, DataFrame y arranque de indexación para continuar después con `loc`/`iloc`, filtros y columnas calculadas en la siguiente sesión. No abrir agrupaciones en profundidad ni visualización.
- **Lo que queda para después:** ausencias y agrupaciones de pandas, carga/limpieza de datos, visualización comparada Python/R y continuación de UD2.

## 2. Material que conviene abrir antes de clase

Rutas relativas a la raíz del módulo:

| Uso | Ruta |
|---|---|
| Guía de instalación de R + VS Code + kernel (nueva) | `01-fundamentos-python/05-recursos/guia-instalacion-r-vscode.md` |
| Teoría breve de R | `01-fundamentos-python/01-teoria/09-guia-r-complementario.md` |
| Notebook R guiado | `01-fundamentos-python/02-ejemplos/06_introduccion_R_fundamentos.ipynb` (local o Colab) |
| Colab con kernel R (si no hay instalación lista) | `https://colab.research.google.com/notebook#create=true&language=r` |
| Enunciado entregable de la comparativa | `01-fundamentos-python/04-evaluacion/comparativa-lenguajes-formatos-ia.md` |
| Teoría de pandas | `02-tratamiento-datos/01-teoria/01-pandas-introduccion.md` |
| Notebook principal de pandas | `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb` |
| EDA de empleados (referencia del EDA ya visto) | `01-fundamentos-python/03-practicas/09_eda_numpy.md` / `09_eda_numpy.ipynb` |
| EDA para el alumnado (notebook nuevo) | `01-fundamentos-python/03-practicas/16-eda_numpy_edificios.ipynb` |

Comprobar antes de entrar: que el cuaderno `06_introduccion_R_fundamentos.ipynb` abre con kernel **R** y que un notebook nuevo puede seleccionar ese kernel; que el entorno habitual importa `numpy` y `pandas`; y que la comparativa está disponible/habilitada en Moodle.

### Plan de instalación: local si está listo, Colab si no

- **Estado del alumnado (heterogéneo):** algunos **ya tienen R instalado y también RStudio**; otros fueron por **VS Code** y **todavía se están peleando con plugins, kernels y dependencias de R no satisfechas**.
- **Decisión según el lunes:** si el grupo tiene el entorno **local** resuelto, **tiramos por local** (RStudio para unos, VS Code + IRkernel para otros). Si una parte relevante del grupo sigue **sin dependencias de R satisfechas**, no se dedica la clase a arreglar instalaciones: **tiramos por Google Colab** con kernel R desde el navegador.
- Para el recorrido local, la guía nueva `05-recursos/guia-instalacion-r-vscode.md` explica: instalar R desde CRAN, extensiones de VS Code **Jupyter** (`ms-toolsai.jupyter`) y **R** (`REditorSupport.r`), y registrar **IRkernel** con `install.packages("IRkernel")` + `IRkernel::installspec()` desde una terminal con `jupyter` en `PATH`.
- Si alguien que fue por VS Code no pudo instalar o el kernel no aparece, resolver con la tabla de problemas frecuentes de la guía (XML de RStudio, `R` sin `PATH`, kernel no visible, `jupyter` ausente en `installspec`). Si sigue sin salir en pocos minutos, saltar a Colab.
- **No dedicar toda la clase** a resolver la instalación de cada puesto: fijar límite de tiempo y continuar; lo esencial es que haya un kernel R operativo (local o Colab) para la demostración y la comparativa, y que el equipo del profesor esté preparado para ambos caminos.
- **Pendiente Moodle, antes de clase:** subir/habilitar la tarea de la comparativa y decidir la distribución del notebook 16. Comprobar la subida de los tres GIFT NumPy si no se hizo la sesión anterior.

### Precauciones concretas

- La guía nueva evita RStudio (página que devuelve XML) y recomienda R directo desde CRAN + plugins de VS Code + IRkernel. Quien ya tenga RStudio local funciona igual de bien para el recorrido breve; no hace falta migrarlo a VS Code. No afirmar que una instalación local probada en el equipo docente equivalga a que esté lista en los puestos del alumnado.
- Colab es el plan de respaldo para quien no tenga dependencias de R satisfechas: funciona en el navegador sin instalar nada. Los paquetes instalados y los archivos generados pueden perderse si el entorno se reinicia; guardar los notebooks en Drive o descargarlos.
- En pandas, omitir la celda interna `pd.get_option("mode.data_manager")` del notebook: dependía de la versión y está obsoleta. Usar el recorrido de este guion.
- En R, ceñirse a vectores, `c`, `NA`, `data.frame` y resumen; no exigir bucles, funciones completas ni paquetes (sin tidyverse, dplyr ni RMarkdown todavía).
- La comparativa distingue lenguajes (Python, R, Java, JavaScript) de formatos (JSON, YAML, Markdown, XML/HTML) y marcado: no presentarlos como alternativas intercambiables para entrenar un modelo.

## 3. Ritmo de 120 minutos

| Minutos | Bloque | Comprobación |
|---|---|---|
| 0–15 | Arranque y objetivos: decidir **local vs. Colab** según lo que tenga el grupo; quien tenga RStudio o VS Code+IRkernel listo trabaja en local, quien no, abre **Colab con kernel R**. | Cada alumno tiene R ejecutable (local o Colab) y el profesor, para ambos caminos. |
| 15–20 | Repartir la comparativa y explicar el entregable. | El grupo conoce producto, plazo y formato. |
| 20–35 | R base breve: vector, filtro, resumen y `data.frame`; contraste puntero con Python. | Dispone de un ejemplo real de R para la comparación. |
| 35–70 | Comparativa de lenguajes y formatos: tabla, decisión y marcado. | Trabaja y entrega la actividad prevista en clase. |
| 70–75 | Cierre de la entrega y anotación del punto alcanzado. | Revisa que las ocho filas estén completas. |
| 75–100 | Repaso de lo primero de pandas: Series, DataFrame como conjunto de columnas/Series y arranque de indexación. | Distingue columna como Series, etiquetas frente a posiciones. |
| 100–120 | Mini-práctica breve y ticket de salida: selección sencilla y transformación. | Explica una selección y una transformación con pandas. |

**Límite de tiempo:** cerrar la puesta en marcha de R en el minuto 15 (si un puesto falla, pasar a Colab o seguir con demostración del profesor), el bloque R breve en el 35 y la comparativa en el 70. El repaso de pandas debe empezar como mucho en el 75.

## 4. Bloque de arranque: poner en marcha R (local o Colab) y abrir el primer notebook R (0–20 min)

> **Elegir vía según el lunes.** Si buena parte del grupo tiene R listo (RStudio o VS Code+IRkernel), seguir **A (local)**; quien no tenga dependencias de R satisfechas, seguir directamente **B (Colab)** sin quedarse enredado en plugins/kernels.

### A. Instalación local (0–15 min)

Usar `05-recursos/guia-instalacion-r-vscode.md` en pantalla. Resumen operativo:

1. Descargar **R** desde `cran.r-project.org/bin/windows/base/` (Windows), el repositorio de Debian/Ubuntu (`sudo apt update && sudo apt install r-base`) o `cran.r-project.org/bin/macosx/` (macOS). En Windows conviene añadir R al `PATH` durante la instalación. Comprobar con `R --version`.
2. En VS Code, instalar las extensiones **Jupyter** (`ms-toolsai.jupyter`) y **R** (`REditorSupport.r`) desde la vista de extensiones o con `code --install-extension ...`. Reiniciar VS Code.
3. Asegurar un entorno con `jupyter` en `PATH` (por ejemplo `conda activate pia-ud1`).
4. Desde una terminal con ese entorno, arrancar R y ejecutar `install.packages("IRkernel")` y `IRkernel::installspec()`. Verificar con `jupyter kernelspec list` (debe aparecer `ir`).
5. En VS Code: `Ctrl+Shift+P` → «Jupyter: Create New Jupyter Notebook» → selector de kernel → **Jupyter Kernel… → R**. Si no aparece, refrescar o reiniciar.

### B. Vía Colab (para quien no tenga R listo, 0–15 min)

Si una parte relevante del grupo sigue sin dependencias de R satisfechas, usar **Google Colab con kernel R**, sin instalar nada más:

1. Abrir un notebook nuevo de R: `https://colab.research.google.com/notebook#create=true&language=r`.
2. Conectar el entorno y comprobar la versión con una celda: `R.version.string`.
3. Subir y abrir nuestro notebook `06_introduccion_R_fundamentos.ipynb` (Archivo → Subir notebook) y confirmar que las celdas ejecutan R, no Python.
4. Los paquetes instalados (`install.packages(...)`) y los archivos generados pueden perderse si el entorno se reinicia: guardar el notebook en Drive o descargarlo.

Esta vía no sustituye a RStudio para quien ya lo tenga, ni resuelve la instalación local: es el camino de respaldo del lunes. El pequeño código R de la introducción funciona igual en local y en Colab.

### C. Primer notebook R (15–20 min)

Abrir `06_introduccion_R_fundamentos.ipynb` con kernel R o crear celdas nuevas. Mostrar este mínimo y preguntar qué cambia respecto a Python:

```r
notas <- c(6, 8, NA, 9)
print(notas[1])
print(notas[!is.na(notas) & notas >= 7])
print(mean(notas, na.rm = TRUE))

alumnos <- data.frame(
  nombre = c("Ana", "Luis", "Marta", "Pablo"),
  nota = notas
)
print(alumnos)
print(summary(alumnos))
```

Equivalente breve con NumPy ya conocido:

```python
import numpy as np
notas = np.array([6., 8., np.nan, 9.])
print(notas[0])
print(notas[~np.isnan(notas) & (notas >= 7)])
print(np.nanmean(notas))
```

Cinco ideas: asignación `<-`, vector con `c`, índice inicial 1, `NA` y funciones de resumen; un `data.frame` organiza columnas. Es una primera lectura, no un dominio de R. No afirmar que R sea siempre mejor para estadística ni que Python sea siempre más rápido: depende de herramientas, tarea y contexto.

## 5. Comparativa de lenguajes y formatos (entregable, 35–70 min)

Abrir el enunciado público **sin observación docente**: `04-evaluacion/comparativa-lenguajes-formatos-ia.md`. Conserva su ruta canónica. Reparto sugerido: 5 min para interpretar el caso, 18 para la tabla, 8 para conclusión y marcado, 4 para revisar y entregar.

Explicar antes de empezar que se comparan tecnologías con funciones distintas: lenguajes (Python, R, Java, JavaScript/NodeJS) frente a formatos (JSON), configuración (YAML), documentación (Markdown) y marcado (XML/HTML). Java/JavaScript se valoran por su papel en la aplicación, sin programarlos hoy. No pedir tidyverse ni gráficos.

**Observación docente, solo aquí:** el R recién visto (vectores y `data.frame`) da una referencia concreta para la fila R: análisis estadístico, visualización e informes reproducibles. Al retomar visualización en UD2, se compararán gráficos Python/R sobre los mismos datos.

## 6. Repaso de lo primero de pandas (75–100 min)

Continuar sobre los **mismos empleados** del EDA, ahora en un DataFrame, para recuperar lo ya presentado sin repetir la introducción entera. El notebook `01_pandas_fundamentos.ipynb` (dataset de clientes) puede usarse después como repertorio.

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 1000
columnas = ["id", "edad", "salario", "experiencia", "horas", "nivel", "satisfaccion"]
edad = rng.integers(18, 65, size=n)
salario = rng.normal(2500, 800, size=n)
experiencia = np.clip(edad - rng.integers(18, 30, size=n), 0, None)
horas = rng.normal(40, 5, size=n)
nivel = rng.integers(0, 5, size=n)
satisfaccion = rng.normal(7, 2, size=n)
salario[rng.choice(n, 10, replace=False)] *= 4
satisfaccion[rng.choice(n, 15, replace=False)] = np.nan
data = np.column_stack([np.arange(1, n + 1), edad, salario, experiencia, horas, nivel, satisfaccion])
df = pd.DataFrame(data, columns=columnas)
df = df.astype({"id": "int64", "edad": "int64", "experiencia": "int64", "nivel": "int64"})
df = df.set_index("id")

print(df.head())
df.info()
print(type(df["salario"]), type(df[["salario"]]))
print(df["salario"].name, df["salario"].index[:3])
print(df[["salario", "satisfaccion"]].describe())
```

Recuperar en 5 minutos: cada columna es una Series; el índice aporta etiquetas. El paso de `data[:, 2]` a `df["salario"]` conecta con el EDA. Un DataFrame con índice por etiquetas hace que posición `0` y etiqueta `1` ya no coincidan.

**Arranque de indexación (pendiente de continuar la próxima sesión):**

```python
print(df.loc[1, ["edad", "salario"]])   # etiqueta 1
print(df.iloc[0, :2])                    # primera fila, dos primeras columnas
print(df.loc[1:3, ["edad", "salario"]])
```

Distinguir etiquetas frente a posiciones; `.loc` por etiquetas, `.iloc` por números y con convención de Python. No abrir aún ordenación avanzada, `groupby` ni visualización.

## 7. Mini-práctica breve y cierre (100–120 min)

Sobre el DataFrame de empleados ya en memoria:

1. Seleccionar los empleados con salario mayor de 3000 y mostrar `edad`, `salario` y `horas`.
2. Crear una columna `salario_anual` igual a `salario * 12`.
3. Mostrar la primera fila con `iloc` y el empleado con etiqueta 1 con `loc`; explicar la diferencia en una frase.

Dedica 10 minutos a las tres consultas y 5 a la puesta en común. Para la corrección, comprobar formas, columnas e índices y pedir interpretación, no solo leer código.

**Ticket de salida:** escribir una selección por etiqueta, una por posición y un filtro con pandas; explicar en una frase por qué pandas facilita el EDA tabular frente a columnas numeradas de NumPy.

**Si sobra tiempo:** repetir un resumen del EDA con pandas (`describe` sobre el subset) y comparar legibilidad. No abrir agrupaciones, joins ni JAX.

**Si falta tiempo:** cerrar la comparativa en el límite fijado y reducir el repaso de pandas a Series + arranque de indexación; la mini-práctica queda para la siguiente sesión.

## 8. Cierre y ajuste al ritmo

Al terminar, registrar: qué alumnado tiene R operativo y kernel R, entrega de la comparativa, y el punto exacto alcanzado en pandas (Series, DataFrame, inicio de `loc`/`iloc`). El guion previsto no acredita que se hayan impartido todos los bloques.

**Siguiente paso recomendado:** continuar UD2 desde el punto real de pandas: `loc`/`iloc`, filtros compuestos, columnas calculadas y, más adelante, ausencias, agrupaciones y carga de datos. Retomar la comparativa de gráficos Python/R en el bloque de visualización de UD2.

## Referencias para el profesor

- [Guía de instalación de R + notebooks en VS Code](`01-fundamentos-python/05-recursos/guia-instalacion-r-vscode.md`).
- [Selección e indexación en pandas](https://pandas.pydata.org/docs/user_guide/indexing.html).
- [Asignación y Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html).
- [IRkernel — instalación](https://irkernel.github.io/installation/).
