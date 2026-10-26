# Entornos de Python: qué herramienta elegir

> Documento de apoyo para la sesión de entornos de **UD2**. Se imparte después de UD1: el alumnado ya ha usado NumPy y pandas y puede ver el problema real. No sustituye al [manual práctico de Pixi](manual-pixi-pia.md): lo sitúa junto a las demás herramientas y explica **por qué** no instalamos las dependencias del módulo en el Python del sistema.

## 1. El problema

Un proyecto de IA necesita una versión concreta de Python, de NumPy, de pandas, de scikit-learn, de PyTorch y, a veces, bibliotecas nativas (CUDA, BLAS, compiladores). Instalar todo en el Python del sistema produce tres problemas clásicos:

- **Conflictos:** dos proyectos piden versiones incompatibles de la misma librería y arreglar uno rompe el otro.
- **Falta de reproducibilidad:** «en mi portátil funciona» y en el aula no.
- **Riesgo para el sistema:** actualizar o desinstalar paquetes puede romper herramientas del sistema operativo.

No es un caso teórico: en este módulo, UD1 y UD2 usan **NumPy 2** y **pandas 2.2**, mientras que **PyCaret 3.3** (UD3) exige `NumPy < 1.27` y `pandas < 2.2`. Si todo comparte el mismo Python, una de las dos partes deja de funcionar.

Un **entorno** es una carpeta aislada con su propio intérprete y sus propios paquetes. Al activarlo, `python` y `pip` apuntan ahí.

## 2. Por qué no usar la instalación del sistema

| Motivo | Qué evita |
|---|---|
| Aislamiento | Que un proyecto rompa otro proyecto o el sistema. |
| Reproducibilidad | Que cada equipo tenga versiones distintas. |
| Varias versiones de Python | Tener 3.11 para PyCaret y 3.12 para el resto. |
| Paquetes nativos y GPU | Resolver binarios compatibles sin compilar a mano. |
| Permisos | No necesitar `sudo` ni `pip install --user`. |
| Limpieza | Borrar el entorno deja el sistema intacto. |
| Colaboración y CI | El mismo entorno en aula, casa y servidor. |

**Cuándo sí es razonable:** herramientas del propio SO, scripts de un solo uso sin dependencias críticas o utilidades ya instaladas. **Para los proyectos del módulo, no.**

> Si el comando lleva `sudo pip install`, casi seguro está mal planteado.

## 3. Qué gestiona cada herramienta

| Herramienta | Gestiona | Punto fuerte | Límite | Uso en el módulo |
|---|---|---|---|---|
| **pip** | Paquetes de PyPI | Universal y sencillo | No aísla por sí solo; no gestiona Python | Instalar dentro de un entorno |
| **venv** | Entorno virtual ligero (stdlib) | Sin instalar nada extra | Solo paquetes Python; no resuelve binarios | Proyectos pequeños o pruebas |
| **uv** | Entorno, Python y paquetes | Muy rápido; lockfile | Ecosistema Python | Alternativa moderna a pip/venv |
| **conda / mamba** | Python, paquetes y binarios | Paquetes nativos; entornos reutilizables | Más pesado; resolución lenta sin mamba | Experimentación y compatibilidad |
| **Pixi** | Proyecto completo (conda + PyPI) | Reproducible, por proyecto, features y entornos | Curva de aprendizaje inicial | **Herramienta principal** |
| **Poetry** | Dependencias y empaquetado | Publicar paquetes; `pyproject.toml` | No resuelve binarios nativos | Solo si se publica un paquete |

**Idea clave:** pip, venv, uv y Poetry trabajan sobre todo con paquetes **Python**; conda y Pixi también resuelven **paquetes nativos** y versiones de Python. Por eso el módulo usa Pixi: hay CUDA, BLAS, compiladores y paquetes que no son Python puro.

La comparación rápida de Pixi con `uv` y Conda ya está en [manual-pixi-pia.md](manual-pixi-pia.md); aquí solo se amplía el mapa completo.

## 4. pip y venv: el mínimo

`venv` viene con Python y crea un entorno aislado; `pip` instala dentro de él.

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows (PowerShell o CMD)

which python                     # Linux / macOS
where python                     # Windows

pip install numpy pandas
pip list
deactivate
```

Sin activar ningún entorno, `pip install` escribe en el Python del sistema (o del usuario). Ese es el error que queremos evitar.

`uv` hace lo mismo con lockfile y mucha más velocidad (`uv venv`, `uv add`, `uv run`, `uv sync`). Es válido para proyectos pequeños, pero **no sustituye a Pixi** cuando hacen falta paquetes nativos o varios entornos compuestos.

## 5. Conda y mamba: entornos reutilizables

Conda gestiona entornos con paquetes Python y nativos. La especificación vive en un `environment.yml`:

```yaml
name: pia-ud1
channels:
  - conda-forge
dependencies:
  - python=3.12
  - numpy>=2,<3
  - pandas>=2.2,<3
  - jupyterlab
```

```bash
conda env create -f environment.yml
conda activate pia-ud1
conda env update -f environment.yml --prune
conda list
conda deactivate
```

El repositorio ya trae ejemplos reales: [`pia-ud1.yml`](../01-fundamentos-python/05-recursos/pia-ud1.yml) y [`environment.yml`](https://github.com/IES-Rafael-Alberti/programacion-inteligencia-artificial/blob/main/environment.yml). Para UD2, consulta la [guía de proyecto con Python, Pixi y conda](../02-tratamiento-datos/01-teoria/10a-guia-proyecto-python-pixi.md); la guía ML queda reservada a UD3.

**Reutilizar sin multiplicar entornos.** La tentación es crear un entorno por experimento. Mejor:

- Un `environment.yml` por **familia de proyectos**, no por prueba.
- Actualizar el mismo entorno con `conda env update -f ... --prune` en vez de crear otro.
- Exportar una especificación portable con `conda env export --from-history > environment.yml`.
- Duplicar (`conda create --clone`) solo para congelar una versión que comparar.
- Para reproducibilidad estricta, `conda-lock` genera un lockfile por plataforma.

`mamba` es un reemplazo compatible y mucho más rápido del solver: los mismos comandos con `mamba` delante.

**Límite honesto:** conda no compone variantes de un mismo proyecto tan limpiamente como Pixi. Si necesitas «base + ML», «base + GPU» y «base + AutoML», acabas con varios entornos o con un `environment.yml` inflado.

## 6. Pixi: la herramienta principal

Pixi es un gestor **por proyecto**: las dependencias se declaran en `pixi.toml`, se fijan en `pixi.lock` y los entornos se crean dentro de `.pixi/`. No hay un entorno global que se contamine.

En este módulo se usa para los proyectos porque:

- **Reproducible por proyecto:** `pixi.toml` + `pixi.lock` viajan con el repositorio.
- **Composición sin duplicar:** una feature (`base`, `ud3`, `ud4`) se reutiliza en varios entornos.
- **Multiplataforma:** el mismo lockfile resuelve Linux, Windows y macOS.
- **Tareas:** `pixi run` evita depender de que el alumnado active el entorno correcto.
- **Aísla de verdad:** los entornos viven en el proyecto, no en una lista global.

Todo el detalle (instalación, conceptos, comandos, features, entornos, problemas frecuentes y buenas prácticas) está en **[manual-pixi-pia.md](manual-pixi-pia.md)**. El proyecto real del curso es el [`pixi.toml`](https://github.com/IES-Rafael-Alberti/programacion-inteligencia-artificial/blob/main/pixi.toml) de la raíz. La [guía de proyecto de UD2](../02-tratamiento-datos/01-teoria/10a-guia-proyecto-python-pixi.md) cubre tratamiento de datos; la [guía de proyecto ML/UD3](../03-machine-learning/01-teoria/10-guia-proyecto-python-pixi.md) es específica de aprendizaje automático.

**Inconvenientes:** hay que instalarlo una vez y entender `pixi run`; la primera resolución puede tardar y ocupar disco; no es la herramienta habitual en todas las empresas, así que conviene saber también conda y pip.

## 7. Experimentar y desplegar: no es el mismo entorno

Experimentar y desplegar tienen requisitos distintos. El error típico es llevar a producción el entorno de experimentación (con Jupyter, notebooks, tests y paquetes de desarrollo) o, al contrario, intentar experimentar dentro de una imagen de producción.

| | Experimentar | Desplegar |
|---|---|---|
| Objetivo | Probar, comparar, romper y repetir | Ejecutar igual, sin intervención manual |
| Duración | Cambia cada semana | Congelado por versión |
| Herramientas | Pixi, conda/mamba, venv + uv, Jupyter | pip/uv, Poetry, Docker, conda-lock |
| Artefacto | `pixi.toml` + `pixi.lock`, `environment.yml` | Imagen Docker, wheel, `requirements.lock` |
| Dependencias | También desarrollo (Jupyter, pytest, ruff) | Solo runtime |
| Reproducibilidad | Lockfile del proyecto | Lockfile + imagen inmutable |

### Separar dependencias de desarrollo y de producción

- **Pixi:** features separadas (`base`, `ud3`, `gpu`) y entornos que las combinan; no metas Jupyter en el entorno de producción.
- **uv:** grupos de dependencias (`[dependency-groups]`, `--no-dev`, `UV_NO_DEV=1`).
- **Poetry:** grupos (`[tool.poetry.group.dev.dependencies]`) e instalación con `--without dev`.
- **pip:** un `requirements.txt` de runtime y otro `requirements-dev.txt` aparte.

### Herramientas de despliegue

| Herramienta | Para qué | Nota |
|---|---|---|
| **pip + requirements.txt** | Instalar en cualquier sitio | Universal; fija versiones y usa `--require-hashes` |
| **pip-tools** | Generar el lock de pip | `pip-compile requirements.in`; `pip-sync` |
| **uv** | Lock e instalación rápidos | `uv export --format requirements.txt`; `uv sync --locked` |
| **Poetry** | Wheel y publicación | `poetry build`; `poetry export` es plugin desde 2.0 |
| **conda-lock / micromamba** | Lock e instalación de conda en CI o imagen | Evita resolver en producción |
| **Docker** | Empaquetar SO + Python + dependencias | Frontera habitual de despliegue |
| **pipx** | Instalar herramientas CLI aisladas | No para librerías del proyecto |

### Reglas prácticas

1. **Un lockfile, un artefacto.** No instales en producción con `pip install paquete` sin versión.
2. **No congeles con `pip freeze`** de un entorno sucio: arrastra dependencias de desarrollo y del sistema. Usa `pip-compile`, `uv export` o `poetry export`.
3. **No lleves Jupyter a producción.** El servicio solo necesita runtime.
4. **Docker no sustituye al gestor:** la imagen se construye *desde* el lockfile.
5. **GPU:** resuelve el entorno con Pixi/conda, pero despliega una imagen con la variante CUDA validada.
6. **conda en producción:** usa `conda-lock` o `micromamba` con un lock, no `conda env create` resolviendo en cada arranque.

Ejemplo mínimo de imagen con uv:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && UV_NO_DEV=1 uv sync --locked --no-install-project
COPY . .
RUN UV_NO_DEV=1 uv sync --locked
ENV UV_NO_DEV=1
CMD ["uv", "run", "--locked", "python", "-m", "app"]
```

No hace falta aprenderse el Dockerfile en esta sesión: la idea es que **la imagen se construye desde el lockfile y sin dependencias de desarrollo**.

## 8. Poetry: empaquetar y publicar

Poetry gestiona dependencias y, sobre todo, **empaqueta y publica** paquetes Python (`pyproject.toml`, `poetry.lock`).

```bash
poetry init
poetry add numpy pandas
poetry add --group dev pytest ruff
poetry install --without dev
poetry build
poetry publish
```

El resultado de `poetry build` es un wheel que se instala con `pip install dist/*.whl`; esa es su vía natural de despliegue. `poetry export` ya **no viene en el núcleo desde Poetry 2.0**: si se necesita `requirements.txt`, hay que añadir el plugin `poetry-plugin-export`.

En este módulo **no es la ruta de ejecución**: no resuelve bien paquetes nativos/GPU y no aporta ventaja frente a Pixi para los proyectos. Se usa solo si un proyecto externo exige publicar un paquete o consumir un wheel.

> No mezcles manifiestos: un proyecto con `pixi.toml` **y** `poetry.lock` acaba con dos verdades distintas. Elige uno.

## 9. Matriz de decisión

| Situación | Herramienta |
|---|---|
| Proyecto del módulo con notebooks, ML y GPU | **Pixi** |
| Script pequeño de un día, solo paquetes Python | `venv` + `pip` o `uv` |
| Reutilizar un entorno de experimentación entre prácticas | **conda/mamba** con un `environment.yml` |
| Varias variantes del mismo proyecto (base, ML, GPU) | **Pixi** (features + entornos) |
| Servicio o API en producción | **Docker** construido desde un lock (uv/pip) |
| Trabajo por lotes con GPU | **Docker** con la variante CUDA validada |
| Librería para instalar con `pip` | **Wheel** (Poetry, hatch o uv) |
| Herramienta de línea de comandos | **pipx** |
| Instalar «en el sistema» porque es más rápido | **No** |

## 10. Errores típicos

- `sudo pip install` o instalar sin activar ningún entorno.
- Mezclar conda y pip sin control dentro del mismo entorno.
- Tener `pixi.toml` y `requirements.txt`/`poetry.lock` a la vez.
- No versionar `pixi.lock` o `poetry.lock`.
- Versionar `.pixi/`, `.venv/` o `__pycache__/`.
- Crear un entorno nuevo para cada prueba en vez de actualizar el existente.
- Ejecutar notebooks con un Python distinto del que tiene las dependencias.
- Congelar producción con `pip freeze` de un entorno de experimentación.
- Meter Jupyter, pytest o ruff en la imagen de producción.

## 11. Checklist antes de instalar algo

1. ¿Estoy dentro de un proyecto con su manifiesto?
2. ¿He activado el entorno o usado `pixi run`?
3. ¿La dependencia es Python pura o necesita binarios?
4. ¿Estoy actualizando el entorno existente en vez de crear otro?
5. ¿He versionado el manifiesto y el lockfile?
6. ¿Es una dependencia de experimentación o de producción?
7. ¿El comando y el error están registrados si algo falla?

## Material relacionado

- [Manual práctico de Pixi para PIA](manual-pixi-pia.md)
- [Guía de inicio del curso](guia-inicio.md): qué entorno usar en cada unidad.
- [Guía de proyecto UD2 con Python, Pixi y conda](../02-tratamiento-datos/01-teoria/10a-guia-proyecto-python-pixi.md)
- [Guía de proyecto ML/UD3 con Python y Pixi](../03-machine-learning/01-teoria/10-guia-proyecto-python-pixi.md)
- [Chuleta del stack convergente](../07-convergencia-herramientas/05-recursos/cheatsheet_stack_convergente.md)
