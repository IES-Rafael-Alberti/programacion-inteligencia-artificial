# Cómo trabajar con los materiales del curso

Usa el portal para orientarte y el repositorio para ejecutar notebooks, scripts y prácticas. El portal no publica todos los archivos ejecutables ni los datos del curso.

## Ruta rápida

1. Localiza la unidad y la actividad en el portal.
2. Obtén una copia local del repositorio.
3. Desde la raíz del repositorio, usa el entorno indicado por la actividad.
4. Abre el notebook o ejecuta la práctica desde esa copia local.

## Obtener el repositorio

Puedes clonarlo con Git:

```bash
git clone https://github.com/IES-Rafael-Alberti/programacion-inteligencia-artificial.git
cd programacion-inteligencia-artificial
```

Si no utilizas Git, [descarga el repositorio en formato ZIP](https://github.com/IES-Rafael-Alberti/programacion-inteligencia-artificial/archive/refs/heads/main.zip), descomprímelo y abre una terminal en la carpeta resultante.

## Elegir el entorno

No existe un único entorno válido para todas las unidades. Utiliza el nombre que indique la actividad o su README.

| Entorno Pixi | Uso documentado |
|---|---|
| `default` | Base común de Python, NumPy, Pandas, SciPy y JupyterLab. |
| `ud3` | Machine Learning clásico con scikit-learn y XGBoost. |
| `ud3-pycaret` | Práctica de PyCaret de UD3. |
| `ud3-datasets` | Construcción de datasets de UD3. |
| `ud3-flaml` | Alternativa experimental FLAML de UD3. |
| `ud4` | Deep Learning en CPU. |

Si una actividad no indica un entorno Pixi, sigue el procedimiento de su README o enunciado: puede utilizar un fichero de requisitos, un entorno propio o una herramienta externa. No asumas que `default` contiene las dependencias de todo el curso.

Consulta el [manual práctico de Pixi](manual-pixi-pia.md) para instalar la herramienta y entender los entornos disponibles.

## Ejecutar notebooks y prácticas

Desde la raíz del repositorio, sustituye `<entorno>` por el nombre indicado en la actividad:

```bash
pixi install --environment <entorno>
pixi run --environment <entorno> jupyter lab
```

Después, abre el notebook desde JupyterLab. Para scripts o proyectos, ejecuta el comando específico del enunciado con el mismo entorno.

Si la actividad documenta una alternativa a Pixi, ejecútala desde la carpeta que indique su guía y conserva aisladas sus dependencias.

## Si algo falla

Antes de cambiar dependencias, registra:

- la unidad y la actividad;
- el comando completo;
- el entorno elegido;
- el mensaje de error completo;
- el sistema operativo.

Con esos datos se puede reproducir el problema sin convertir una incidencia local en cambios innecesarios para todo el curso.
