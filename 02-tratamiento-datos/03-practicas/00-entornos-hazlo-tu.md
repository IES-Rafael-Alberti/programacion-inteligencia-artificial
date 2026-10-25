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
pixi run --environment ud3 python -c "import sklearn; print(sklearn.__version__)"
pixi run --environment ud3-pycaret python --version
pixi list --environment ud3
```

Responde:

- ¿Qué diferencia hay entre `default`, `ud3` y `ud3-pycaret`?
- ¿Por qué `ud3-pycaret` no incluye la feature `base`?
- ¿Qué dos ficheros hay que versionar para reproducir el entorno? ¿Cuál **no** se versiona?

## 4. Elige herramienta (5 min)

Para cada caso, escribe la herramienta y una razón:

1. Proyecto final con notebooks, scikit-learn y una variante GPU.
2. Cuatro prácticas de experimentación que comparten el 90 % de dependencias.
3. Script de 20 líneas que solo usa `requests`.
4. Librería que quieres publicar en PyPI.

## 5. Experimentar o desplegar (5 min)

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
