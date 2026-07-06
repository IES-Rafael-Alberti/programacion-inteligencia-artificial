# Boston Housing — regresión tabular con redes neuronales

Esta carpeta se mantiene en UD4 como práctica de **regresión tabular con redes neuronales**. Su valor docente no es usar Boston Housing como dataset moderno, sino comparar implementaciones Keras/PyTorch y revisar cómo cambian la validación, el escalado y las métricas cuando se integra el flujo con `scikit-learn`.

## Uso recomendado

1. Revisar primero `docs/BostonHousingDesc.txt` para entender las variables.
2. Ejecutar sólo en un entorno con las dependencias ya preparadas; no instalar paquetes desde esta carpeta.
3. Comparar una red neuronal Keras, una red neuronal PyTorch y una variante integrada con `Pipeline`/validación cruzada.
4. Añadir o discutir un baseline sencillo antes de interpretar los resultados.

## Material activo

| Fichero | Papel docente | Estado |
|---|---|---|
| `scripts/bostonHousesPrice_Keras.py` | Red neuronal de regresión con Keras. | Útil como ejemplo inicial, pero normaliza antes del split; no usar como patrón final sin corregirlo. |
| `scripts/bostonHousesPrice_Pytorch.py` | Red neuronal equivalente con PyTorch. | Útil para comparar el bucle de entrenamiento, pero escala antes del split y calcula errores sobre variables escaladas. |
| `scripts/bostonHousesPrice_SciKeras.py` | Integración de Keras con `Pipeline`, `StandardScaler` y validación cruzada. | Variante más correcta para enseñar flujo reproducible con `scikit-learn`. |
| `scripts/bostonHousesPrice_SciPytorch.py` | Wrapper manual de PyTorch con interfaz tipo estimador de `scikit-learn`. | Útil como ampliación; no es SciKeras ni `skorch`, y debe explicarse como integración manual. |
| `docs/BostonHousing-1.md` y `docs/BostonHousing-2.md` | Explicación de variantes PyTorch. | Material de apoyo. |
| `docs/BostonHousingDesc.txt` | Descripción de variables del dataset. | Material de referencia. |
| `data/housing.csv` | Dataset local usado por los scripts. | Versionado explícitamente por reproducibilidad. |

## Datos y reproducibilidad

Los scripts cargan el dataset mediante una ruta relativa al propio proyecto:

```python
Path(__file__).resolve().parents[1] / "data" / "housing.csv"
```

`data/housing.csv` ocupa unos 49 KB y contiene 506 filas. Aunque el repositorio ignora de forma general `*.csv` y carpetas `data/`, `.gitignore` incluye una excepción específica para este fichero porque es pequeño y necesario para reproducir la práctica sin depender de descargas externas.

## Métricas esperadas

Para una práctica evaluable, no basta con mostrar que la red entrena. Deben aparecer, como mínimo:

- baseline ingenua o clásica: media del target, `DummyRegressor` o regresión lineal;
- partición de datos antes de ajustar cualquier escalador;
- MAE y RMSE en unidades originales del problema;
- R² como métrica secundaria, explicando sus límites;
- comparación breve entre baseline, Keras, PyTorch y variante con `Pipeline`.

## Limitaciones éticas y de origen

Boston Housing es un dataset histórico, pequeño y problemático. No debe presentarse como referencia moderna ni como ejemplo de sistema listo para producción.

En particular, algunas variables reflejan supuestos sociales y raciales inaceptables para un caso real actual. Si se usa en clase, debe hacerse explícito que:

- sirve para discutir historia, reproducibilidad y errores metodológicos;
- no es un dataset adecuado para tomar decisiones reales sobre vivienda;
- la práctica debe incluir una reflexión sobre sesgos, variables sensibles y límites del modelado.

## Deuda técnica antes de usarlo como práctica cerrada

El saneamiento documental queda cerrado, pero los scripts no deben venderse como solución canónica completa hasta resolver estos puntos:

- corregir el escalado antes del split en las variantes Keras/PyTorch standalone;
- añadir baseline y métricas MAE/RMSE/R² en unidades originales;
- aclarar la diferencia entre ejecución simple, `Pipeline`, validación cruzada e integración manual de PyTorch;
- decidir si se retira o neutraliza la variable problemática `B` en una versión para alumnado.

## Limpieza aplicada

El notebook `nna-vs-traditional.ipynb` se archivó porque usaba Iris y modelos de clasificación, no Boston Housing ni regresión con redes neuronales.
