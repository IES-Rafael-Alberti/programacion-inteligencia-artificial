# Parte 2 — Prácticas (UD4)

Colección de notebooks, documentación y material práctico sobre **redes neuronales** y **optimizadores** en Keras, PyTorch y JAX.

## Estructura

```
Parte-2-Pract/
├── README.md
├── requirements.txt
├── data/
│   └── FashionMNIST/          # Dataset FashionMNIST (descargado automáticamente)
├── docs/
│   ├── introduccion/          # Guías de introducción por framework
│   │   ├── UD4_Intro_Keras.md + .html
│   │   ├── UD4_Intro_PyTorch.md + .html
│   │   ├── UD4_Intro_PyTorch_DataLoader.md   # Guía específica: Dataset y DataLoader
│   │   └── UD4_Intro_JAX.md + .html
│   ├── optimizadores/         # Teoría de optimizadores
│   │   └── OPTIMIZADORES_Teorico.md + .html
│   └── planificacion/         # Índice, planificación y comparativa de frameworks
│       ├── UD4-DeepLearnig-Indice-Parte2-Pratica.md
│       ├── UD4-DeepLearnig-Practica-QueHaremos.md
│       └── UD4-DeepLearning-ComparativaFrameWorks.md
└── notebooks/
    ├── redes-neuronales/      # Primera red neuronal (misma red en tres frameworks)
    │   ├── keras/             # UD4_01, UD4_02, UD4_03
    │   ├── pytorch/           # UD4_04, UD4_05
    │   └── jax/               # UD4_05_Jax, UD4_Apendice_JAX (apéndice)
    └── optimizadores/         # Práctico de optimizadores
        ├── jax/               # JAX puro + JAX+Equinox+Optax (+ versión ejecutada)
        ├── keras/
        └── pytorch/
```

## Referencias cruzadas

Cada subdirectorio de `notebooks/` contiene un `README.md` con enlaces a la documentación relacionada en `docs/`.

| Notebooks | Documentación relacionada |
|-----------|--------------------------|
| `redes-neuronales/keras/` | `docs/introduccion/UD4_Intro_Keras.md` |
| `redes-neuronales/pytorch/` | `docs/introduccion/UD4_Intro_PyTorch.md` |
| `redes-neuronales/jax/` | `docs/introduccion/UD4_Intro_JAX.md` |
| `optimizadores/*/` | `docs/optimizadores/OPTIMIZADORES_Teorico.md` + intro del framework |

Quick start (recomendado con `mamba` / `conda`):

```bash
# Crear entorno
mamba create -n ud4-optimizers -y python=3.10
conda activate ud4-optimizers

# Instalar dependencias principales (CPU)
mamba install -y -c conda-forge tensorflow numpy matplotlib scikit-learn
mamba install -n ud4-optimizers -y pytorch torchvision cpuonly -c pytorch
```

Ejecutar notebooks localmente:

- Abre Jupyter (`jupyter lab` o `jupyter notebook`) dentro del entorno.
- Carga y ejecuta cualquiera de los notebooks en `notebooks/practicos/`.

Instalación rápida (comando que los alumnos pueden copiar):

```bash
# Conda/mamba (recomendado):
mamba create -n ud4-optimizers -y python=3.10 && conda activate ud4-optimizers && mamba install -y -c conda-forge numpy matplotlib scikit-learn && mamba install -n ud4-optimizers -y pytorch torchvision cpuonly -c pytorch

# Pip (alternativa; JAX/CPU como ejemplo):
pip install -r requirements.txt
```

Usar Google Colab (badge + snippet):

- Puedes generar un badge "Open In Colab" que apunte a la ruta del notebook en GitHub. Ejemplo (reemplaza `<USERNAME>/<REPO>`):

```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<USERNAME>/<REPO>/blob/main/notebooks/practicos/jax/UD4_Practico_Optimizadores_JAX_Equinox.ipynb)
```

- Celda de instalación rápida para Colab (añádela como primera celda del notebook):

```python
# Celda Colab — instala dependencias (ajusta si necesitas jaxlib GPU wheel)
!pip install -q equinox optax jax jaxlib
# Opcional: montar Google Drive
from google.colab import drive
drive.mount('/content/drive')
```

Notas:

- Si vas a usar GPU en Colab, puede ser necesario instalar un `jaxlib` con soporte CUDA específico; sigue https://github.com/google/jax#installation para instrucciones.
- Para instalar localmente con `pip`, usa `pip install -r requirements.txt` y asegúrate de elegir la rueda de `jaxlib` correcta si usas JAX.

Siguientes pasos disponibles:

- Insertar badges directamente dentro de los notebooks en `notebooks/practicos/`.
- Generar un script que añada automáticamente los badges a todos los notebooks.

Si quieres que inserte los badges automáticamente en los notebooks, dímelo y lo hago.
