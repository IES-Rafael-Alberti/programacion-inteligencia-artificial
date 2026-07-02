# Evaluación — UD4 Deep Learning

Esta carpeta centraliza los instrumentos de evaluación de la unidad. Las rúbricas detalladas de cada laboratorio se mantienen en sus carpetas de origen; aquí se recogen la rúbrica consolidada, el checklist de entrega y el cuestionario GIFT de teoría.

## Camino rápido

1. Completa el laboratorio o laboratorios indicados por el profesorado.
2. Entrega el trabajo siguiendo la plantilla de entrega de cada lab y el `checklist-entrega.md`.
3. Revisa la calificación esperada con `rubrica.md` (consolidada) o con la rúbrica específica del lab.
4. Realiza el cuestionario GIFT si el profesorado lo activa en Moodle.

## Distribución de laboratorios

| Laboratorio | Tema | Peso en UD4 |
| --- | --- | ---: |
| Lab 1 — TF Playground | Exploración visual de redes neuronales | 25 % |
| Lab 2 — Backpropagation desde cero | Implementación manual del algoritmo | 30 % |
| Lab 3 — Playground → código real | Transición a framework real | 45 % |

## Qué se evalúa por laboratorio

**Lab 1 — TensorFlow Playground:**
- Diseño experimental (variación sistemática de capas, activaciones, learning rate).
- Interpretación de resultados (convergencia, sobreajuste, frontera de decisión).
- Conexión con teoría (gradiente, activaciones, profundidad).
- Claridad y presentación del informe.

**Lab 2 — Backpropagation:**
- Identificación de las partes del algoritmo (forward, pérdida, backward, actualización).
- Relación código ↔ teoría (regla de la cadena, gradiente, activación).
- Análisis crítico sobre limitaciones y diferencias con frameworks modernos.
- Rigor técnico y claridad del documento.

**Lab 3 — De Playground a código real:**
- Implementación funcional con un framework (Keras, PyTorch u otro trabajado en la unidad).
- Visualización e interpretación de pérdida y frontera de decisión.
- Experimentación y comparación de arquitecturas con criterio técnico.
- Conexión con backpropagation y superficie de pérdida.
- Calidad técnica del código y la documentación.

## Rúbricas disponibles

- `rubrica.md` (este directorio): rúbrica consolidada sobre 10 puntos con criterios unificados.
- `../03-practicas/laboratorios/Laboratorio1/TensorFlowPlayGround-Rubrica.md`: rúbrica detallada Lab 1.
- `../03-practicas/laboratorios/Laboratorio2/EstudioImplementacionBackpropagation-Rubrica.md`: rúbrica detallada Lab 2.
- `../03-practicas/laboratorios/Laboratorio3/DePlayground_a_CodigoReal-Rubrica.md`: rúbrica detallada Lab 3.

## Cuestionario disponible

- `cuestionario-deep-learning.gift`: preguntas de comprensión teórica sobre fundamentos de DL, backpropagation, frameworks y arquitecturas.

## Criterios de superación

- La nota ponderada de los laboratorios alcanza al menos 5 sobre 10.
- El flujo principal de cada lab ejecuta o está suficientemente documentado.
- La entrega permite verificar el trabajo realizado sin adivinar pasos.
