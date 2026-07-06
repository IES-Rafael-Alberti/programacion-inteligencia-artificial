# Entornos de Deep Learning — plantillas docentes

Plantillas de instalación para frameworks usados en UD4.

## Estado

- **Uso:** apoyo docente/profesorado, no requisito único para el alumnado.
- **Validación:** scripts revisados sintácticamente, pero no ejecutados en esta pasada.
- **Criterio:** cada práctica debe indicar su entorno mínimo; este directorio sólo conserva recetas base.

## Ficheros

| Fichero | Uso previsto | Observaciones |
|---|---|---|
| `environment.yml` | Entorno amplio con PyTorch, TensorFlow, Keras, JAX, ONNX y herramientas comunes. | Pesado; útil para profesorado o laboratorio controlado. |
| `install_pytorch.sh` | Entorno PyTorch con CUDA. | Requiere GPU NVIDIA compatible si se mantiene `pytorch-cuda`. |
| `install_tensorflow.sh` | Entorno TensorFlow. | Para GPU, revisar compatibilidad de `tensorflow[and-cuda]`. |
| `install_keras3.sh` | Keras 3 multi-backend. | Permite seleccionar backend con `KERAS_BACKEND`. |
| `install_jax.sh` | JAX/Flax/Equinox. | CPU por defecto; GPU requiere adaptar instalación. |
| `install_onnx.sh` | ONNX/ONNX Runtime y herramientas de conversión. | Más cercano a exportación/despliegue que a fundamentos. |
| `install_mlx.sh` | MLX para Apple Silicon. | Sólo para Mac ARM. |

## Decisión

Se mantienen en UD4 como **plantillas de entorno**, no como instrucciones obligatorias. Antes de usarlas en clase hay que probarlas en el hardware real del aula y fijar versiones si se necesita reproducibilidad estricta.
