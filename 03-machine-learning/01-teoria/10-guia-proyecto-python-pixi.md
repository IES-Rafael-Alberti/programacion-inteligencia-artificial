# Guía de proyecto de IA con Python y Pixi

Usa Pixi como flujo operativo del módulo: el manifiesto declara las dependencias, el lockfile fija las versiones y `pixi run` ejecuta cada tarea sin activar un entorno a mano.

## Ruta rápida en este repositorio

Desde la raíz del repositorio, prepara el entorno adecuado y ejecuta el trabajo dentro de él:

```bash
pixi install --environment ud3
pixi run --environment ud3 jupyter lab
pixi run --environment ud3 python ruta/a/tu_script.py
```

Para P2 con PyCaret usa exclusivamente el entorno aislado, porque requiere versiones incompatibles con la base de UD3:

```bash
pixi install --environment ud3-pycaret
pixi run --environment ud3-pycaret jupyter lab
```

Consulta `docs/manual-pixi-pia.md` para la instalación de Pixi, los entornos disponibles y la selección del intérprete en VS Code.

## Estructura recomendada

```text
mi_proyecto_ia/
├── data/          # Datos brutos y procesados
├── notebooks/     # EDA y experimentos
├── src/           # Preprocesamiento, entrenamiento e inferencia
├── outputs/       # Modelos y resultados generados
├── tests/         # Comprobaciones automatizadas
├── .env           # Secretos locales; nunca se versiona
├── pixi.toml      # Dependencias y tareas del proyecto
└── pixi.lock      # Versiones exactas resueltas
```

Mantén separados los datos, el código reproducible y los resultados generados. Un notebook explora; el código de `src/` debe permitir repetir el proceso.

## Dependencias y tareas

En el repositorio PIA no añadas dependencias a mano: utiliza el entorno indicado por la actividad. Para un proyecto Pixi independiente, crea su manifiesto y declara solo lo que necesite:

```bash
pixi init mi_proyecto_ia
cd mi_proyecto_ia
pixi add python=3.12 pandas seaborn matplotlib scikit-learn jupyterlab python-dotenv
pixi run jupyter lab
```

Cada cambio de dependencias actualiza `pixi.toml` y `pixi.lock`; versiona ambos archivos. No combines Pixi y Poetry en el mismo proyecto.

## Modelado

- Para el modelado manual, reserva el conjunto de test antes de ajustar decisiones y usa `Pipeline` junto con validación cruzada sobre entrenamiento.
- Para P2, usa `ud3-pycaret`; no instales PyCaret en `ud3` porque su rango de NumPy es distinto.
- Guarda el modelo entrenado y documenta sus entradas, la métrica y las limitaciones de uso.

## Despliegue opcional

Si la actividad incluye una API o una interfaz, crea un proyecto Pixi específico para el despliegue y declara únicamente sus dependencias:

```bash
pixi init mi_despliegue
cd mi_despliegue
pixi add python=3.12 fastapi uvicorn streamlit pandas joblib
pixi run uvicorn main:app --reload
# o
pixi run streamlit run app.py
```

FastAPI y Streamlit resuelven necesidades distintas; consulta `09-despliegue-streamlit-fastapi.md` antes de escoger uno.

## Seguridad y entrega

Guarda las claves en `.env`, cárgalas con variables de entorno y entrega un `.env.example` sin secretos. Incluye el comando Pixi empleado y evidencia de que el proyecto se ejecuta desde un clon limpio.

## Poetry, solo si publicas un paquete

Poetry también puede gestionar metadatos y publicar paquetes Python. No es la ruta de ejecución del módulo: úsalo solo si un proyecto externo exige su flujo de empaquetado y nunca junto con Pixi en el mismo directorio.
