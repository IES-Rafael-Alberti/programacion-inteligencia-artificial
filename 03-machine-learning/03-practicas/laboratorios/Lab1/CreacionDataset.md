# Actividad práctica: construir un dataset de películas

Esta actividad consume las API de TMDB y OMDb, combina sus respuestas y guarda un dataset para analizarlo después. El entorno reproducible del laboratorio es el entorno Pixi `ud3-datasets` del repositorio PIA.

## Ruta rápida

Desde la raíz del repositorio:

```bash
pixi install
pixi run --environment ud3-datasets python --version
```

Configura tus claves en un archivo `.env` dentro de `mi_dataset_peliculas/` (no lo subas al repositorio):

```env
TMDB_API_KEY=REPLACE_ME
OMDB_API_KEY=REPLACE_ME
```

Para ejecutar el código del laboratorio, usa la tarea definida en `pixi.toml`:

```bash
pixi run --environment ud3-datasets lab1-dataset
```

La tarea establece el directorio de trabajo del proyecto y el `PYTHONPATH` necesario para que funcionen los imports relativos. No ejecutes `build_dataset.py` directamente: al hacerlo se pierde el contexto del paquete y pueden fallar imports como `from .tmdb import ...`.

## Requisitos previos

- Pixi instalado siguiendo el [manual de Pixi para PIA](../../../../docs/manual-pixi-pia.md).
- Una clave de TMDB: <https://developer.themoviedb.org/signup>.
- Una clave gratuita de OMDb: <https://www.omdbapi.com/apikey.aspx>.

Pixi es el único gestor de entorno y dependencias de este laboratorio. No es necesario instalar ni configurar otro gestor de paquetes.

## Estructura del proyecto

```text
mi_dataset_peliculas/
├── data/
├── src/mi_dataset_peliculas/
│   ├── config.py
│   ├── tmdb.py
│   ├── omdb.py
│   ├── merge.py
│   └── build_dataset.py
└── README.md
```

## Cómo funciona

`config.py` lee las claves mediante `python-dotenv` y los módulos `tmdb.py` y `omdb.py` usan `requests`. `merge.py` conserva las columnas seleccionadas de ambas API. `build_dataset.py` crea `data/dataset_peliculas.csv`.

El flujo mínimo de consulta TMDB es:

```python
import requests
from .config import get_api_keys


def get_popular_movies(page=1):
    tmdb_api_key, _ = get_api_keys()
    response = requests.get(
        "https://api.themoviedb.org/3/movie/popular",
        params={"api_key": tmdb_api_key, "language": "es-ES", "page": page},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["results"]
```

Para OMDb se usa el mismo patrón, pasando `apikey` y el título consultado. No guardes claves en el código ni en notebooks versionados.

## Tarea

### Trazabilidad CRISP-DM mínima

Antes de entregar, deja una tabla o apartado breve con estas evidencias. No hace falta reproducir la teoría: basta justificar decisiones reales del laboratorio.

| Fase | Evidencia en Lab1 |
|---|---|
| Comprensión del problema y datos | propósito del dataset, TMDB/OMDb, campos y condiciones de uso. |
| Preparación | columnas elegidas, duplicados, nulos o conflictos al fusionar respuestas. |
| Evaluación y entrega | comprobaciones de casos normales/errores, CSV generado, limitaciones y cómo repetir la ejecución con Pixi. |


1. Completa o revisa `tmdb.py` y `omdb.py`.
2. Obtén varias páginas y evita duplicados.
3. Añade columnas justificadas, por ejemplo género, actores o director.
4. Analiza el CSV resultante con pandas y documenta decisiones y limitaciones.
5. Comprueba casos normales, respuestas sin resultados y errores de red; registra el resultado y la limitación de las comprobaciones.
6. Entrega también las evidencias de proceso y verificación exigidas por las [normas comunes de entregas y uso de IA](../../../../docs/normas-entregas-y-uso-de-ia.md).

## Problemas habituales

| Problema | Solución |
|---|---|
| `pixi: command not found` | Abre un terminal nuevo y comprueba el `PATH`. |
| `ModuleNotFoundError: mi_dataset_peliculas` | Ejecuta la tarea `lab1-dataset` desde la raíz del repositorio. |
| Clave `None` o respuesta 401 | Revisa `.env`, los nombres de las variables y los permisos de las claves. |
| El CSV aparece en otra carpeta | Ejecuta la tarea Pixi; su directorio de trabajo es el proyecto del laboratorio. |

## Siguiente paso

Ejecuta el laboratorio con tus claves reales y documenta las comprobaciones realizadas junto con el dataset entregado.
