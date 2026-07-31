# Evaluación — UD9 GPU Avanzado

Esta carpeta reúne los instrumentos de evaluación de la unidad de programación GPU avanzada con RAPIDS, JAX y JIT.

## Camino rápido

1. Completa el [preflight del runtime](../03-practicas/README.md#preflight-obligatorio-del-runtime).
2. Completa las prácticas indicadas por el profesorado en [`03-practicas/`](../03-practicas/README.md).
3. Entrega la evidencia evaluable de cuDF, cuML y benchmarking ejecutada en una GPU NVIDIA.
4. Realiza el cuestionario GIFT si el profesorado lo activa en Moodle.

Si no tienes una GPU NVIDIA local, utiliza Google Colab con runtime GPU o el runtime cloud equivalente indicado por el profesorado. La ejecución CPU sirve para preparar y depurar, pero **no se considera evidencia equivalente** de aceleración GPU.

## Instrumentos disponibles

| Fichero | Qué evalúa |
| --- | --- |
| `cuestionario_rapids_jax.gift` | Comprensión teórica de RAPIDS (cuDF, cuML), JAX (JIT, grad, vmap) y optimización GPU. |

## Prácticas evaluables

Las prácticas de `03-practicas/` incluyen plantillas base de proyecto, dashboard y pipeline orientados a GPU avanzado. El profesorado indica cuáles son evaluables en cada grupo.

Los notebooks de teoría de `01-teoria/` y los demos de `02-ejemplos/` son material de referencia y apoyo, no prácticas evaluables directas.

## Evidencias esperadas

- Notebook o script ejecutado con salidas visibles o capturas de resultados.
- Preflight visible con modelo de GPU NVIDIA, versiones de librerías y backend/dispositivo utilizado.
- Comparativa de rendimiento GPU/CPU cuando el enunciado lo requiera.
- Breve análisis del comportamiento observado (speedup, limitaciones, casos de uso).

## Criterios de superación

- La entrega ejecuta sin errores críticos en el entorno indicado.
- La evidencia GPU procede de un runtime NVIDIA verificable; una ejecución solo en CPU no acredita este criterio.
- Las evidencias permiten verificar los resultados obtenidos.
- El análisis conecta los resultados con los conceptos de la unidad.
