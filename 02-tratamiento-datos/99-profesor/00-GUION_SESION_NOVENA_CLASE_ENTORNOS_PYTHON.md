# Guion de la sesión de entornos de Python — 2 horas

> **Documento interno del profesorado. Solo repositorio docente; no publicar en `main` del alumnado, GitHub Pages ni Moodle.**

**Duración:** 120 min (2 h), con descanso de 10 min.

**Ubicación:** **UD2 (`02-tratamiento-datos`)**, después de UD1. El alumnado ya ha instalado y usado NumPy y pandas, así que puede ver el problema real: convivir con **versiones distintas de las mismas herramientas** o con **herramientas distintas para tareas parecidas** sin que se pisen. No se imparte en UD1 porque allí el objetivo es aprender las herramientas, no gestionarlas.

## 1. Objetivos

Al terminar, el alumnado debe saber:

1. Explicar **por qué** no instalamos las dependencias del módulo en el Python del sistema.
2. Distinguir qué gestiona cada herramienta: pip, venv, uv, conda/mamba, Pixi y Poetry.
3. Usar **Pixi** como herramienta principal de los proyectos del módulo.
4. Usar **conda/mamba** como alternativa para entornos reutilizables de experimentación, sin multiplicar entornos.
5. Elegir herramienta con un criterio, no por costumbre.
6. Separar **experimentación** y **despliegue**: qué herramienta y qué artefacto lleva cada momento.

**No** es objetivo de esta sesión: instalar CUDA, migrar el repositorio ni enseñar Poetry o Docker en profundidad.

## 2. Material: no duplicar lo que ya está escrito

La sesión se apoya en la teoría de UD2: `00a-entornos-python.md` cubre el mapa y el criterio de elección; `00b-manual-pixi-pia.md` y `00c-manual-conda-pia.md` desarrollan el manejo. Los manuales se retoman después conforme se necesiten, sin convertir esta sesión en un recorrido exhaustivo por ML, GPU o despliegue.

| Uso | Ruta |
|---|---|
| Documento base de la sesión (alumnado) | `02-tratamiento-datos/01-teoria/00a-entornos-python.md` |
| Manual de Pixi (detalle, comandos, problemas) | `02-tratamiento-datos/01-teoria/00b-manual-pixi-pia.md` |
| Manual de conda (instalación, YAML, Jupyter, problemas) | `02-tratamiento-datos/01-teoria/00c-manual-conda-pia.md` |
| Entornos disponibles del curso | `docs/guia-inicio.md` |
| Guía práctica de proyecto UD2 | `02-tratamiento-datos/01-teoria/10a-guia-proyecto-python-pixi.md` |
| Guía posterior de proyecto ML/UD3 | `03-machine-learning/01-teoria/10-guia-proyecto-python-pixi.md` |
| Manifiesto real del repositorio | `pixi.toml` |
| Entorno conda de UD1 | `01-fundamentos-python/05-recursos/pia-ud1.yml` |
| Entorno conda raíz | `environment.yml` |
| Ejercicio «hazlo tú» (alumnado) | `02-tratamiento-datos/03-practicas/00-entornos-hazlo-tu.md` |
| Chuleta del stack | `07-convergencia-herramientas/05-recursos/cheatsheet_stack_convergente.md` |

> Si el grupo ya ha usado `pixi run` en clase, no se repite la instalación: se entra directamente en el bloque 4 y se recorta el bloque 1.

## 3. Ritmo (120 min)

| Min | Bloque | Formato |
|---|---|---|
| 0–8 | Arranque: el problema y los objetivos | Pregunta al grupo |
| 8–22 | Por qué no el sistema + mapa + ejes experimentar/desplegar | Teoría breve + tabla |
| 22–40 | pip, venv y uv | Demo + «hazlo tú» (5 min) |
| 40–58 | conda/mamba: entornos reutilizables | Demo + «hazlo tú» (5 min) |
| 58–68 | Descanso | — |
| 68–96 | Pixi: la herramienta de los proyectos | Demo + «hazlo tú» (8 min) |
| 96–108 | Poetry y despliegue: wheel, lock, Docker | Demo mínima + decisión |
| 108–120 | Matriz de decisión y ticket de salida | Cierre |

## 4. Bloques

### 0. Arranque (8 min)

Pregunta de predicción, sin ejecutar nada:

> «Si instalo `pandas 2.2` para este proyecto y otro proyecto necesita `pandas 1.5`, ¿qué crees que pasa en el Python del sistema?»

Caso real del módulo, no inventado: UD1 y UD2 usan **NumPy 2** y **pandas 2.2**; UD2 trabaja con Python 3.12, Matplotlib y Jupyter. Si todo vive en el mismo Python, los proyectos pueden entrar en conflicto.

Recoger 2–3 respuestas. No corregir todavía: la respuesta se construye en el bloque 1. Enunciar los seis objetivos y avisar de que la sesión es **de criterio**, no de instalar todo.

### 1. Por qué no el sistema y qué hace cada herramienta (14 min)

Teoría breve con la tabla de `02-tratamiento-datos/01-teoria/00a-entornos-python.md`:

- Entorno = intérprete + paquetes aislados; activar cambia el `PATH`.
- Tres riesgos del sistema: conflictos, no reproducibilidad, romper el SO.
- Mapa: pip/venv/uv (Python puro) frente a conda/Pixi (también nativos) y Poetry (empaquetado).
- Idea que debe quedar: **Pixi para los proyectos; conda para experimentación reutilizable; pip/venv/uv para lo pequeño; Poetry solo para publicar.** Mamba se menciona como interfaz compatible, pero no se instala aparte: conda moderno ya usa `conda-libmamba-solver` por defecto.
- **Dos ejes que ordenan todo el mapa:** *experimentar* (probar, comparar, romper: Pixi, conda, venv/uv, Jupyter) y *desplegar* (ejecutar igual y sin Jupyter: lockfile, wheel, Docker). El mismo proyecto puede usar Pixi para experimentar y Docker para desplegar; lo que no se hace es llevar el entorno de experimentación tal cual a producción.

Chequeo de predicción: «¿Qué herramienta usarías para un script de 20 líneas que solo usa `requests`? ¿Y para el proyecto con PyTorch?».

### 2. pip, venv y uv (18 min)

Demo en vivo en una carpeta de trabajo `pia-entornos`, creada y abierta desde el
explorador de archivos o la terminal (la ubicación puede ser distinta en cada sistema):

```bash
# Desde la carpeta pia-entornos ya creada y abierta:
python -m venv .venv
```

Activación según el sistema:

```bash
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Windows CMD
.venv\Scripts\activate.bat
```

Con el entorno activo:

```bash
python -c "import sys; print(sys.executable)"
python -m pip -V
python -m pip install rich
python -c "from importlib.metadata import version; print(version('rich'))"
deactivate
python -c "import rich"
```

**Predicción antes de ejecutar:** ¿la última línea funciona o falla? ¿Por qué?

Mensaje: `venv` aísla, pero hay que activarlo; si se olvida, `pip` escribe en el sistema. `uv` hace lo mismo con lockfile y más rápido; se nombra, no se instala si no está.

**«Hazlo tú» (5 min):** crear un `venv`, instalar `rich`, comprobar la versión dentro y que fuera no existe. Dos parejas dicen el resultado.

La secuencia es válida en Linux, macOS y Windows. Si Windows no reconoce `conda
activate`, ejecutar `conda init powershell`, cerrar y volver a abrir PowerShell (o
reiniciarlo) y probar de nuevo.

**Cierre del bloque:** `pip` no es un gestor de entornos; es un instalador. `venv`/`uv` ponen el aislamiento.

### 3. conda/mamba: reutilizar sin multiplicar (18 min)

Referencia para resolver dudas o continuar en casa: `02-tratamiento-datos/01-teoria/00c-manual-conda-pia.md`. En clase se trabaja este bloque; no se recorre el manual completo.

Abrir `01-fundamentos-python/05-recursos/pia-ud1.yml` y leerlo en voz alta: nombre, canal, Python y paquetes.

```bash
conda env list
conda env create --dry-run -f 01-fundamentos-python/05-recursos/pia-ud1.yml
conda activate pia-ud1
conda list
conda env update -f 01-fundamentos-python/05-recursos/pia-ud1.yml --prune
```

Si conda no está instalado o el solver tarda, se hace solo `--dry-run` y se explica la salida; **no se invierte la clase en instalar conda**. Desde conda 23.10 el solver `libmamba` viene configurado por defecto; `mamba` sigue siendo una interfaz compatible, pero no es una instalación necesaria para la sesión.

**Predicción:** «Si añado una dependencia al `.yml` y ejecuto `conda env update --prune`, ¿se crea otro entorno o se actualiza el mismo?».

Mensaje clave: **un `environment.yml` por familia de proyectos**, actualizar en vez de crear, y `--from-history` para exportar limpio. Crear un entorno por prueba es el error que queremos evitar.

**«Hazlo tú» (5 min):** responder por parejas: (a) ¿qué versión de Python fija `pia-ud1.yml`?; (b) si mañana necesito `matplotlib` solo para una práctica, ¿creo `pia-ud1-v2` o actualizo `pia-ud1`?; (c) ¿qué riesgo tiene duplicar el entorno?

### 4. Pixi: la herramienta de los proyectos (28 min)

Abrir el `pixi.toml` real de la raíz y señalar `[feature.base]`, `[feature.ud3]` y `[environments]`. No recorrer todo el fichero. La guía de UD2 advierte que Matplotlib está ahora en `ud3`, no en `base/default`.

```bash
pixi --version
pixi info
pixi install
pixi run --environment default python --version
pixi run --environment default python -c "import numpy, pandas; print(numpy.__version__, pandas.__version__)"
pixi task list
```

**Predicciones encadenadas:**

1. ¿Qué contiene `default` y qué dependencia de visualización falta declarar? (Matplotlib no está en `base/default`.)
2. Si ejecuto `python` sin `pixi run`, ¿usa el entorno del proyecto? (No necesariamente: depende del `PATH`.)
3. ¿Qué fichero hay que versionar para que otra persona reproduzca el entorno? (`pixi.toml` **y** `pixi.lock`.)

Mensaje clave: Pixi compone **features** y **entornos** sin duplicar definiciones; los entornos viven en `.pixi/`, que no se versiona. El detalle está en `02-tratamiento-datos/01-teoria/00b-manual-pixi-pia.md`; no se repite aquí.

**«Hazlo tú» (8 min):** en el repositorio, cada pareja ejecuta y anota:

```bash
pixi run --environment default python --version
pixi run --environment default python -c "import numpy, pandas; print(numpy.__version__, pandas.__version__)"
```

Y responde: ¿por qué no se debe afirmar que `default` sirve ya para visualizar? (Porque Matplotlib está declarado en `ud3`; hay que modificar la feature de UD2 o usar conda.)

**Comprobación de integración (opcional, 8 min):** si ya se ha creado el entorno conda `pia-ud2`, o si existe el entorno Pixi de UD2 con Matplotlib, abrir `02-tratamiento-datos/02-ejemplos/03_pandas_eda_visualizacion.ipynb`, ejecutar las celdas iniciales y mostrar una gráfica. No se completa el EDA ni se entrega el notebook: solo se comprueba que el entorno ejecuta material real de la unidad.

### 5. Poetry y despliegue: experimentar no es desplegar (12 min)

Proyectar la tabla «Experimentar / Desplegar» de `02-tratamiento-datos/01-teoria/00a-entornos-python.md`. La idea que debe quedar: **el entorno de experimentación no se lleva tal cual a producción**; se separan dependencias de desarrollo y de runtime, y se despliega un artefacto construido desde el lockfile.

**Poetry (3 min, sin instalar nada):**

- `pyproject.toml` + `poetry.lock`; grupos `dev` frente a runtime (`poetry install --without dev`).
- `poetry build` genera un wheel; se instala con `pip install dist/*.whl`.
- `poetry export` **ya no viene en el núcleo desde Poetry 2.0**: es un plugin (`poetry-plugin-export`).
- No resuelve binarios nativos/GPU: no es la ruta de ejecución del módulo.

**Despliegue (9 min):**

- **pip + `requirements.txt`**: universal; versiones fijadas y `--require-hashes`. **No** congeles con `pip freeze` de un entorno con Jupyter.
- **pip-tools**: `pip-compile requirements.in` genera el lock; `pip-sync` lo instala.
- **uv**: `uv export --format requirements.txt`; en imagen, `UV_NO_DEV=1 uv sync --locked`.
- **conda-lock / micromamba**: lock de conda para CI o imagen, sin resolver en cada arranque.
- **Docker**: empaqueta SO + Python + dependencias; la imagen se construye *desde* el lockfile y sin dev. Enseñar el Dockerfile mínimo del documento, **no ejecutarlo**.
- **pipx**: para herramientas CLI aisladas, no para las librerías del proyecto.

**Predicciones:**

1. «¿La imagen de producción debe llevar Jupyter y pytest?» (No: solo runtime.)
2. «¿`pip freeze` de mi entorno con notebooks es un buen lock de producción?» (No: arrastra desarrollo y ruido.)
3. «¿Poetry serviría para el proyecto con PyTorch y CUDA?» (No como gestor de ejecución; sí, en todo caso, para publicar un wheel.)

### 6. Matriz de decisión y ticket (12 min)

Proyectar la matriz de `02-tratamiento-datos/01-teoria/00a-entornos-python.md` y resolver cinco casos en voz alta:

1. Proyecto final con notebooks, scikit-learn y GPU → **Pixi** para experimentar; **imagen Docker** con la variante CUDA para desplegar.
2. Cuatro prácticas de experimentación que comparten el 90 % de dependencias → **un entorno conda actualizado**, no cuatro.
3. Servicio o API en producción → **Docker** construido desde un lock (uv/pip).
4. Librería que se publica en PyPI → **wheel con Poetry** (o hatch/uv).
5. Herramienta de línea de comandos → **pipx**.

Ticket de salida (en el ejercicio): una frase por herramienta, un caso propio y la diferencia entre experimentar y desplegar. Se entrega en Moodle; valoración **binaria (hecho/no hecho)**, igual que los cuadernos «hazlo tú».

## 5. Entregable y evaluación

- Ejercicio: `02-tratamiento-datos/03-practicas/00-entornos-hazlo-tu.md`.
- Entrega en Moodle al final de la sesión.
- **Hecho / no hecho.** Entregar acredita asistencia; completo acredita seguimiento. No es prueba ni se corrige acierto.
- Si alguien no termina, puede acabarlo en casa y subirlo igualmente.

## 6. Precauciones

- **No convertir la sesión en instalaciones.** Si falta conda o Pixi en algún equipo, se trabaja en parejas o con demostración proyectada. La ruta conda alternativa de UD2 crea `pia-ud2` con Python 3.12, NumPy, pandas, Matplotlib, JupyterLab e ipykernel; se comprueban versiones, se exporta con `--from-history` y se desactiva al terminar.
- **No ejecutar `pixi install` de todos los entornos** en clase: la primera resolución puede tardar. Para esta sesión se usa `default`; la guía ML/UD3 queda como referencia posterior.
- **No abrir** el `pixi.toml` entero línea a línea: confunde. Tres features y el bloque `[environments]`.
- Verificar antes de clase: `pixi --version`, `pixi run --environment default python -c "import numpy, pandas"` y la situación de `pixi.lock`. No ejecutar comandos Pixi que requieran resolver en este entorno docente.
- Si el grupo no tiene conda, el bloque 3 se reduce a leer el `.yml` y comparar con Pixi; el objetivo es el criterio, no la instalación.
- **No instalar Docker en clase.** El bloque de despliegue es conceptual: se enseña el Dockerfile y se explica el artefacto; la práctica real de contenedores pertenece a UD5.
- **No mezclar los dos ejes en el mismo ejemplo:** Pixi/conda para experimentar; lock + wheel/imagen para desplegar. Si se mezclan, el alumnado acaba creyendo que «producción = activar el entorno de clase».
- No afirmar que una herramienta es «mejor» en abstracto: depende del caso. Insistir en la matriz.
