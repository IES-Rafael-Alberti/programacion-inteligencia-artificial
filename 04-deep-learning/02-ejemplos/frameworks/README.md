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

## Ejecución local

La ruta local principal es el entorno Pixi `ud4`, válido para los ejemplos base de PyTorch:

```bash
pixi install --environment ud4
pixi run --environment ud4 jupyter lab
```

Abre los notebooks desde `notebooks/redes-neuronales/pytorch/` o `notebooks/optimizadores/pytorch/`. Los materiales Keras y JAX son comparativas complementarias y pueden necesitar dependencias que no forman parte de `ud4`; usa una receta especializada sólo cuando se indique expresamente. Las recetas de `requirements.txt` y `05-recursos/modelado-entornos/` quedan como referencia docente, no como flujo principal del alumnado.
