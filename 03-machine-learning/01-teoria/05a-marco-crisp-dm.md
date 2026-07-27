# CRISP-DM: marco de trabajo para los proyectos de datos de UD3

CRISP-DM es el **marco ligero de trabajo** que usamos en PIA para no empezar por el algoritmo: primero se aclara el problema y se comprende el dato. No es una secuencia rígida; se puede volver a una fase anterior cuando la evidencia lo requiera.

## Ruta rápida

1. Formula el objetivo y el criterio de éxito.
2. Describe, explora y prepara los datos sin perder la trazabilidad.
3. Modela y evalúa con una separación honesta entre entrenamiento y prueba.
4. Comunica el resultado, sus límites y el siguiente paso.

## Las seis fases aplicadas en PIA

| Fase CRISP-DM | Pregunta que debe poder responderse | Evidencia mínima en UD3 |
|---|---|---|
| Comprensión del problema | ¿Qué decisión, predicción o análisis se quiere apoyar? | objetivo, destinatario y criterio de éxito |
| Comprensión de los datos | ¿Qué hay, de dónde procede y qué calidad tiene? | fuente, licencia/condiciones, diccionario breve y EDA |
| Preparación de los datos | ¿Qué transformaciones se han aplicado y por qué? | limpieza, variables, tratamiento de nulos y transformadores ajustados solo con entrenamiento |
| Modelado | ¿Qué alternativas se probaron? | modelos, configuración y criterio de comparación mediante validación dentro de entrenamiento |
| Evaluación | ¿La evidencia responde al objetivo y es fiable? | evaluación final única sobre test, errores, limitaciones y sesgos |
| Entrega o despliegue | ¿Qué se entrega y cómo se podrá usar o repetir? | instrucciones de ejecución, resultados y siguiente decisión |

## Regla de oro contra la fuga de datos

**Primero se separa entrenamiento y prueba. Después se ajusta cualquier transformador solo con entrenamiento.** Esto incluye imputadores, escaladores, codificadores, selectores de variables y técnicas de reducción de dimensionalidad. El conjunto de prueba solo recibe `transform`, nunca `fit` ni `fit_transform`.

En scikit-learn, la forma preferida es un `Pipeline` con `ColumnTransformer`: reduce errores y hace reproducible la misma preparación al entrenar y al predecir. Véase [Preparación de datos para ML](05-preparacion-datos-ml.md).

## CRISP-DM y arquitectura Medallion

Ambos conceptos se complementan, pero responden a preguntas distintas:

| Concepto | Para qué sirve | Dónde se trabaja |
|---|---|---|
| CRISP-DM | Organizar el ciclo completo de un proyecto de datos/ML y justificar decisiones. | PIA, especialmente UD3. |
| Medallion (Bronze, Silver, Gold) | Organizar técnicamente las capas del dato: crudo, depurado e información lista para consumo. | Sistemas de Big Data. |

Medallion apoya sobre todo la comprensión y preparación de datos de CRISP-DM. En PIA no se repite la arquitectura: se usa el marco para razonar, documentar y evaluar el proyecto.

## Checklist para una entrega de UD3

- [ ] Objetivo y fuente de datos explícitos.
- [ ] EDA y decisiones de limpieza justificadas.
- [ ] Separación train/test previa a cualquier ajuste aprendido de los datos.
- [ ] Métricas, limitaciones y errores relevantes explicados.
- [ ] Ejecución y resultados reproducibles para otra persona.

El [Lab1 de dataset](../03-practicas/laboratorios/Lab1/CreacionDataset.md) cubre principalmente la comprensión del problema y de los datos, y la preparación; aporta evidencia parcial de evaluación y entrega mediante el análisis básico, la trazabilidad y la ejecución reproducible. El [capstone de películas](../03-practicas/midterm-capstone/Peliculas/00-CapstonePeliculas.md) recorre el ciclo completo.
