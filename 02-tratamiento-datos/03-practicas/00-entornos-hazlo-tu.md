# Ejercicio «hazlo tú» — Entornos de Python

**Entrega:** Moodle, al final de la sesión. **Valoración binaria:** hecho / no hecho. Entregar acredita asistencia; completo acredita seguimiento. No es una prueba y no se corrige el acierto.

Trabaja en pareja. Anota el comando, lo que esperabas y lo que salió. Si algo falla, copia el error completo: es parte de la evidencia.

## 1. venv + pip (5 min)

En una carpeta temporal:

```bash
mkdir -p /tmp/pia-entornos && cd /tmp/pia-entornos
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
which python
pip -V
pip install rich
python -c "from importlib.metadata import version; print(version('rich'))"
deactivate
python -c "import rich"
```

Responde:

- ¿La última línea funciona o falla? ¿Por qué?
- ¿Qué cambia en `which python` al activar y desactivar?
- ¿Dónde se han instalado los paquetes: en el sistema o en `.venv/`?

## 2. conda: leer y razonar (5 min)

Abre `01-fundamentos-python/05-recursos/pia-ud1.yml` y responde sin crear nada:

- ¿Qué nombre de entorno declara?
- ¿Qué versión de Python fija?
- ¿Qué canal usa?

Si tienes conda instalado, ejecuta solo la simulación:

```bash
conda env list
conda env create --dry-run -f 01-fundamentos-python/05-recursos/pia-ud1.yml
```

Si no lo tienes, no lo instales en clase: explica qué haría el comando.

**Caso:** mañana necesitas `matplotlib` solo para una práctica. ¿Creas `pia-ud1-v2` o actualizas `pia-ud1`? Justifica en una frase.

## 3. Pixi en el repositorio (8 min)

Desde la raíz del módulo:

```bash
pixi run --environment default python --version
pixi run --environment default python -c "import numpy, pandas; print(numpy.__version__, pandas.__version__)"
pixi list --environment default
```

Responde:

- ¿Qué dependencias incluye `default` y qué herramienta las gestiona?
- ¿Por qué Matplotlib no está todavía disponible en `default`?
- ¿Qué dos ficheros hay que versionar para reproducir el entorno? ¿Cuál **no** se versiona?

## 4. Comprueba el entorno con un notebook real (opcional, 8 min)

Usa el entorno que acabas de preparar para abrir y ejecutar parcialmente el notebook:
`02-tratamiento-datos/02-ejemplos/03_pandas_eda_visualizacion.ipynb`.

Con conda:

```bash
conda activate pia-ud2
jupyter lab
```

Con Pixi, usa el entorno de UD2 que incluya Matplotlib (`ud2` cuando se declare esa
feature), no el `default` actual:

```bash
pixi run --environment ud2 jupyter lab
```

Ejecuta las celdas iniciales y al menos una gráfica. Comprueba que el notebook puede
importar NumPy, pandas y Matplotlib desde el entorno elegido. No hace falta completar
todo el EDA ni entregar el notebook: es una prueba de integración.

## 5. Elige herramienta (5 min)

Para cada caso, escribe la herramienta y una razón:

1. Proyecto de UD2 con notebooks, NumPy, pandas y Matplotlib.
2. Cuatro prácticas de experimentación que comparten el 90 % de dependencias.
3. Script de 20 líneas que solo usa `requests`.
4. Librería que quieres publicar en PyPI.

## 6. Experimentar o desplegar (5 min)

Clasifica cada elemento como **experimentación (E)**, **despliegue (D)** o **ambos**, justificando el uso: un manifiesto o un lockfile puede servir en los dos momentos.


| Elemento | E / D |
|---|---|
| `pixi.toml` + `pixi.lock` | |
| `environment.yml` de conda | |
| Wheel generado con `poetry build` | |
| Imagen Docker | |
| `requirements.txt` con hashes | |
| Jupyter Lab | |

Responde:

- ¿Por qué no se lleva Jupyter a la imagen de producción?
- Si construyes una imagen con uv, ¿qué comando deja el entorno instalado sin dependencias de desarrollo?
- ¿Qué herramienta usarías para instalar una utilidad de línea de comandos sin contaminar el proyecto?
- ¿Por qué `pip freeze` de tu entorno de clase no es un buen lock de producción?

## Ticket de salida

Completa en dos o tres líneas:

- La diferencia que más clara te ha quedado entre **pip/venv** y **conda/Pixi**.
- Por qué **no** instalamos las dependencias del módulo con `pip install` en el sistema.
- Una situación de tu día a día en la que usarías **conda** en vez de **Pixi**.
- Una frase que resuma la diferencia entre **experimentar** y **desplegar**.
