# Guía: instalar R, configurar VS Code y usar notebooks con R

Esta guía permite instalar **R desde CRAN** (no RStudio), conectar su kernel en **VS Code** mediante **Jupyter** y abrir notebooks con celdas en R. Es el material de arranque para la introducción a R del módulo.

> **Nota de la sexta clase:** la página de descarga de RStudio devuelve un XML en lugar de comenzar la descarga en algunos navegadores/configuraciones. **No es necesario RStudio para este módulo:** se instala R directamente desde CRAN y se trabaja desde VS Code con la extensión de R y el kernel de IRkernel.

## 0. Resumen de pasos

1. Descargar e instalar **R** desde CRAN.
2. Comprobar que `R` funciona desde la terminal.
3. Instalar en VS Code las extensiones de **Jupyter** y de **R**.
4. Asegurarse de que hay un entorno con **Jupyter** disponible.
5. Instalar **IRkernel** dentro de R y registrar el kernel (espec).
6. Crear/abrir un notebook en VS Code y seleccionar el kernel **R**.

## 1. Instalar R desde CRAN

Descargar la versión base de R correspondiente al sistema operativo:

| Sistema | Descarga |
|---|---|
| Windows | `https://cran.r-project.org/bin/windows/base/` — instalar el ejecutable `R-4.x.x-win.exe` con los valores por defecto. |
| Linux (Debian/Ubuntu) | Consultar `https://cran.r-project.org/bin/linux/` y seguir las instrucciones del repositorio (`sudo apt update && sudo apt install r-base`). |
| macOS | `https://cran.r-project.org/bin/macosx/` — instalar el paquete `.pkg`. |

Al instalar R, en Windows suele recomendarse añadir R al `PATH` (marcar la casilla durante la instalación). Esto permite usar `R` desde la terminal y que la extensión de VS Code lo localice.

### Comprobar la instalación

Abrir una terminal y ejecutar:

```bash
R --version
```

Debe mostrar la versión de R instalada. En Windows, si `R` no se reconoce, abrir el `RGui` instalado o buscar la ruta de `R.exe` (por ejemplo `C:\Program Files\R\R-4.x.x\bin\R.exe`) para añadirla al `PATH`.

## 2. Instalar las extensiones de VS Code

Desde la vista de extensiones de VS Code (`Ctrl+Shift+X`) o por línea de comandos, instalar dos extensiones:

| Extensión | Identificador | Uso |
|---|---|---|
| **Jupyter** (Microsoft) | `ms-toolsai.jupyter` | Permite crear y ejecutar notebooks. |
| **R** (REditorSupport) | `REditorSupport.r` | Lenguaje R: resaltado, `IntelliSense`, sesión R y reconocimiento del kernel. |

Por terminal:

```bash
code --install-extension ms-toolsai.jupyter
code --install-extension REditorSupport.r
```

Reiniciar VS Code antes de continuar para que ambas extensiones se activen.

## 3. Asegurar un entorno con Jupyter

Para que un notebook pueda ejecutar celdas R hace falta un comando `jupyter` (o `jupyter kernelspec`) accesible desde la terminal. En este módulo suele estar disponible en el entorno de trabajo habitual (por ejemplo el entorno conda `pia-ud1` o un entorno Pixi).

Activar el entorno que tenga Jupyter antes de los pasos 4 y 5:

```bash
# Ejemplo con conda (ajustar al nombre real del entorno)
conda activate pia-ud1
```

Si no hay ningún entorno con Jupyter, puede instalarse en el gestor usado en el módulo:

```bash
# Ejemplo con conda
conda install jupyter
```

## 4. Instalar IRkernel y registrar el kernel

Con el entorno que tiene Jupyter activado y **sin abrir RStudio**, arrancar R desde la misma terminal y ejecutar:

```r
install.packages("IRkernel")
IRkernel::installspec()
```

- `install.packages("IRkernel")` instala el paquete que convierte R en un kernel de Jupyter.
- `IRkernel::installspec()` registra el kernel con el nombre `ir` y el nombre visible **R**, para el usuario actual.

Si se usan varias versiones de R registradas, se puede dar un nombre distinto, por ejemplo:

```r
IRkernel::installspec(name = "ir", displayname = "R")
```

Siempre instalar IRkernel en el intérprete de R desde el que se quiere ejecutar y registrarlo con el comando `jupyter` activo en `PATH`.

### Verificación rápida del registro

Volver a la terminal normal y comprobar que el kernel existe:

```bash
jupyter kernelspec list
```

Debe aparecer una entrada `ir` (R).

## 5. Crear o abrir un notebook con kernel R

1. Reiniciar VS Code.
2. Abrir la paleta de comandos (`Ctrl+Shift+P`) y elegir **«Jupyter: Create New Jupyter Notebook»**.
3. En el selector de kernel (arriba a la derecha), elegir **«Select Kernel» → «Jupyter Kernel…» → R**.
4. Si R no aparece, pulsar el icono de **refrescar** en el selector o volver a reiniciar VS Code.
5. La etiqueta de cada celda debe indicar la **language R**. A partir de ahí, las celdas ejecutan R.

También se puede abrir un notebook `.ipynb` existente (por ejemplo `06_introduccion_R_fundamentos.ipynb`) y, si su kernel es **R** o se selecciona R, ejecutar sus celdas.

## 6. Comprobación rápida

En una celda de un notebook con kernel R ejecutar:

```r
notas <- c(6, 8, NA, 9)
print(notas[1])
print(mean(notas, na.rm = TRUE))

alumnos <- data.frame(
  nombre = c("Ana", "Luis", "Marta"),
  nota = c(7, 4, 9)
)
print(alumnos)
print(summary(alumnos))
```

Si se muestra el vector, la media y el `data.frame`, el kernel R funciona correctamente.

## 7. Problemas frecuentes

| Situación | Solución |
|---|---|
| La página de descarga de RStudio devuelve XML y no descarga. | **No usar RStudio**: instalar R desde CRAN (sección 1) y trabajar desde VS Code. |
| `R` no se reconoce en la terminal. | Añadir R al `PATH` (Windows) o reinstalar marcando «añadir al PATH». |
| `IRkernel::installspec()` falla por `jupyter-client has to be installed`. | El comando `jupyter` no está en `PATH`: activar primero el entorno que tenga Jupyter (sección 3) y repetir el registro. |
| El kernel **R** no aparece en VS Code. | Reiniciar VS Code, refrescar el selector de kernel y confirmar que `jupyter kernelspec list` muestra `ir`. |
| Las celdas muestran language Python. | Seleccionar el kernel **R** en el selector de kernel del notebook. |
| Se está trabajando con varias versiones de R. | Registrar un kernel con `name`/`displayname` propios y seleccionar esa variante en el notebook. |

## 8. Material de apoyo

- Introducción a R (teoría): `01-fundamentos-python/01-teoria/09-guia-r-complementario.md`.
- Notebook de R: `01-fundamentos-python/02-ejemplos/06_introduccion_R_fundamentos.ipynb`.
- Comparativa de lenguajes y formatos para IA: `01-fundamentos-python/04-evaluacion/comparativa-lenguajes-formatos-ia.md`.
