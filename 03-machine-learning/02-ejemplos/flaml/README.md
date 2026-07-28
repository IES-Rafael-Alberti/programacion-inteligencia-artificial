# FLAML: AutoML ligero con test reservado

Este ejemplo es una **alternativa experimental** para UD3. No sustituye PyCaret ni
es un requisito del curso: se probará durante el curso antes de decidir si se usa
en una actividad.

## Ejecución

Desde la raíz del repositorio:

```bash
pixi install --environment ud3-flaml
pixi run --environment ud3-flaml python 03-machine-learning/02-ejemplos/flaml/flaml_holdout_sintetico.py
```

El script genera 400 observaciones sintéticas y solo verifica que el flujo funciona.
Sus métricas no son resultados docentes ni sirven para seleccionar una herramienta.

## Patrón que demuestra

1. Separar un holdout estratificado antes del AutoML.
2. Ejecutar la búsqueda con `X_train` e `y_train`, una métrica (`f1`) y un presupuesto
   de tiempo explícitos.
3. Predecir `X_test` una única vez al final.

Al adaptarlo a un dataset real, hay que documentar variables, métrica, límite de
tiempo y decisión de modelo. No se puede usar el holdout para repetir búsquedas o
ajustes.

## Límites deliberados

- La lista de estimadores es corta para que la comprobación sea rápida y
  reproducible; no pretende hallar el mejor modelo posible.
- No hay preprocesado manual en este ejemplo numérico sintético. Para datos reales,
  el tratamiento de columnas y valores ausentes debe quedar dentro del flujo de
  entrenamiento, sin aprender nada del test.
- PyCaret sigue siendo la herramienta de P2; FLAML queda como alternativa futura a
evaluar por su menor peso y su presupuesto de cómputo explícito.
