# Rúbrica de evaluación

La práctica se calificará sobre 10 puntos. La nota no dependerá solo de que el código funcione, sino también de cómo se ha planteado el trabajo, de la comparación realizada y de la calidad de las conclusiones.

## 1. Carga de datos y preparación del pipeline (2 puntos)

Se valorará:

- La carga correcta del dataset.
- La separación adecuada entre entrenamiento, validación y test.
- El uso razonable de redimensionado, lotes y optimización del pipeline.
- Alguna comprobación visual o básica de que los datos se han cargado bien.

Orientación:

- 2,0 puntos: apartado completo, correcto y bien resuelto.
- 1,0 punto: apartado parcialmente resuelto o con carencias menores.
- 0 puntos: apartado no resuelto o con errores importantes.

## 2. Modelo base entrenado desde cero (2 puntos)

Se valorará:

- La existencia de un modelo de referencia propio.
- La coherencia de la arquitectura planteada.
- El entrenamiento y la evaluación correctos.
- Su utilidad real como baseline para comparar.

Orientación:

- 2,0 puntos: baseline completo, funcional y bien planteado.
- 1,0 punto: baseline incompleto o con problemas menores.
- 0 puntos: no hay baseline válido o no permite comparar.

## 3. Transfer learning y fine-tuning (3 puntos)

Se valorará:

- El uso correcto de un modelo preentrenado, como `MobileNetV2` o `MobileNetV3Small`.
- El entrenamiento inicial con la base congelada.
- La aplicación posterior de fine-tuning parcial.
- La configuración razonable del entrenamiento y del preprocesado asociado.

Orientación:

- 3,0 puntos: implementación completa y técnicamente correcta.
- 2,0 puntos: implementación funcional, aunque mejorable.
- 1,0 punto: intento parcial con errores relevantes.
- 0 puntos: no hay una implementación válida de transfer learning.

## 4. Comparación y análisis de resultados (2 puntos)

Se valorará:

- La comparación entre el modelo desde cero, el modelo con base congelada y el modelo con fine-tuning.
- La presentación de métricas relevantes.
- La interpretación de los resultados.
- La discusión sobre rendimiento, velocidad y generalización.

Orientación:

- 2,0 puntos: análisis claro, comparativo y bien justificado.
- 1,0 punto: análisis superficial o incompleto.
- 0 puntos: apenas hay comparación o no se interpreta.

## 5. Presentación y calidad de la entrega (1 punto)

Se valorará:

- El orden y la claridad del notebook o del informe.
- La respuesta a las cuestiones planteadas.
- La coherencia de la conclusión final.
- Que la entrega sea limpia y fácil de revisar.

Orientación:

- 1,0 punto: entrega clara, completa y bien presentada.
- 0,5 puntos: entrega suficiente, pero mejorable.
- 0 puntos: entrega desordenada, incompleta o difícil de evaluar.

## Calificación final

- La suma de los apartados anteriores dará la nota sobre 10.
- Para alcanzar una nota alta no basta con entrenar modelos: hace falta comparar, interpretar y justificar.
- Un trabajo técnicamente funcional pero sin análisis suficiente no podrá alcanzar la máxima puntuación.

## Observaciones

- El profesorado podrá ajustar ligeramente algún apartado si la tarea concreta pone más peso en una parte determinada.
- Si faltan elementos pedidos en la entrega, la calificación podrá reducirse.
- Si el notebook no se puede ejecutar o revisar con normalidad, esto afectará negativamente a la evaluación.
