# Black Friday — recurso local opcional

Dataset tabular usado como posible apoyo para ejemplos de regresión con redes neuronales en UD4.

## Estado docente

- **Uso actual:** recurso opcional, no práctica canónica evaluable.
- **Encaje:** UD4, si se usa para comparar una red neuronal tabular frente a un baseline sencillo.
- **No sustituye** a las prácticas principales de la unidad (`boston-housing`, `used-cars-dl-tabular` o laboratorios base).

## Ficheros locales esperados

Los CSV no se versionan en Git por la regla global de datos (`*.csv`):

| Fichero | Uso | Columnas clave |
|---|---|---|
| `blkfri_train.csv` | Entrenamiento | incluye `Purchase` como variable objetivo |
| `blkfri_test.csv` | Predicción/inferencia | no incluye `Purchase` |

## Criterios si se reactiva como actividad

Antes de convertirlo en tarea para alumnado hay que preparar un enunciado reproducible que incluya:

- origen o forma controlada de distribución del dataset;
- baseline no neuronal;
- partición correcta de datos y preprocesado sin fuga;
- métricas de regresión en unidades interpretables (`MAE`, `RMSE`, `R²`);
- tratamiento explícito de variables categóricas y valores ausentes;
- reflexión sobre límites del modelo y sesgos comerciales.

## Decisión

Se mantiene como **recurso local opcional de UD4**, pero no queda enlazado desde la evaluación hasta que exista una práctica concreta que lo use.
