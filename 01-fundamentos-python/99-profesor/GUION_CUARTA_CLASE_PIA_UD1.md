# Guion de la cuarta clase de PIA — NumPy avanzado

> **Documento interno del profesorado. No publicar en GitHub Pages ni en Moodle.**

**Duración:** 120 minutos. **Continuidad:** tras la tercera clase, dedicada a estructuras adicionales y una posible introducción a POO. Esta sesión consolida NumPy con `06-numpy-avanzado.md` y `09_numpy_avanzado.ipynb`.

## Objetivos y preparación

Interpretar `shape`, `axis` y `dtype`; seleccionar con máscaras; agregar por ejes; distinguir vistas de copias; generar datos reproducibles y justificar una operación vectorizada. Comprobar ambos materiales, tener NumPy instalado y abrir `import numpy as np; print(np.__version__)`. No usar archivos externos ni internet.

## Ritmo de 120 minutos

| Tiempo | Actividad | Evidencia |
|---:|---|---|
| 0–10 | Recuperación: predecir la forma de una suma por eje. | Explica qué eje desaparece. |
| 10–25 | Notebook: `dtype`, `itemsize`, `shape` y `reshape`. | Diagnóstico correcto. |
| 25–45 | Indexado, máscaras, `where` y `select`. | Filtro sin `and`/`or` de Python. |
| 45–62 | Agregaciones y `keepdims`; conexión con broadcasting. | Media por columna alineada. |
| 62–70 | Pausa y puesta en común de errores. | Dudas clasificadas. |
| 70–88 | Vistas, copias y `shares_memory`. | Predice la mutación. |
| 88–102 | `Generator`, semilla y vectorización; micro-medición. | Resultado reproducible. |
| 102–114 | Mini-reto en parejas. | Código y explicación. |
| 114–120 | Ticket de salida. | Respuesta individual. |

**Si van lentos:** omitir micro-medición y puente a librerías; trabajar una matriz pequeña y guiar el reto. **Si van rápidos:** pedir comparación de `keepdims`, una copia defensiva y cuándo migrar a pandas/JAX/PyTorch, sin instalar nada.

## Preguntas de comprobación

- En `a.shape == (2, 3)`, ¿qué forma tiene `a.sum(axis=0)` y qué representa?
- ¿Por qué `(a > 2) & (a < 8)` lleva paréntesis?
- ¿Qué riesgo tiene modificar `a[1:3]`?
- ¿Qué garantiza una semilla y qué no?
- ¿Qué problema resuelve pandas que no resuelve un `ndarray`?

## Mini-reto final y criterio de salida

Con un `Generator` sembrado, crea una matriz `float32` de 4 estudiantes y 3 pruebas. Calcula la media por estudiante, clasifica cada media como `"no apto"`, `"apto"` o `"notable"` mediante `select`, y muestra el índice de la mayor media. Incluye una máscara y no uses bucles para los cálculos. Cada pareja explica el eje y si ha creado copias.

Se alcanza el objetivo si cada persona ejecuta el notebook sin dependencias externas, obtiene resultados reproducibles y explica forma, eje, máscara y vista/copia. Si falla una idea, registrar refuerzo para la siguiente práctica; Moodle se valida/publica después.
