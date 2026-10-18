# 08 - De NumPy a JAX: ampliación del cálculo numérico

JAX amplía el trabajo con arrays incorporando transformaciones como compilación,
derivación automática y vectorización de funciones. Se estudia **después de NumPy**:
no es un atajo para evitar comprender arrays, ejes, indexación o broadcasting.

## Antes de empezar

1. Leer [Introducción a NumPy](05-numpy-introduccion.md) y completar
   [Fundamentos de NumPy](../02-ejemplos/05_numpy_fundamentos.ipynb).
2. Comparar bucles y operaciones vectorizadas en
   [Rendimiento con NumPy](../02-ejemplos/06_numpy_rendimiento.ipynb).
3. Trabajar [broadcasting](07-broadcasting-numpy.md) y su
   [notebook de vectorización](../02-ejemplos/07_numpy_broadcasting_vectorizacion.ipynb).

## Qué aporta JAX

| Herramienta | Problema que resuelve | Límite que hay que entender |
|---|---|---|
| `jax.numpy` | Expresar cálculos con una API similar a NumPy | La compatibilidad no es total; sus arrays no se modifican en el sitio como los de NumPy. |
| `jax.jit` | Compilar una función para reutilizar su cálculo | La primera ejecución incluye compilación; no toda tarea resulta más rápida. |
| `jax.grad` | Obtener derivadas automáticamente | Se parte aquí de funciones con salida escalar. |
| `jax.vmap` | Aplicar una función a lotes sin escribir un bucle explícito | Hay que identificar correctamente el eje del lote. |

Estas herramientas permiten reutilizar funciones numéricas al entrenar modelos y
optimizar parámetros. No implican que JAX sustituya siempre a NumPy ni que haga
falta una GPU para comprender sus conceptos.

## Actividad guiada

Abrir [Introducción a JAX y comparativa con NumPy](../02-ejemplos/08_introduccion_jax_comparativa.ipynb).
El recorrido es: arrays → `jit` → `grad` → `vmap` → comparación de tiempos.
Usar el entorno indicado en la actividad. Si no dispone de JAX, las celdas NumPy
siguen sirviendo como referencia; completar la ampliación en un entorno con JAX.

Al comparar tiempos, separar compilación y ejecución, usar formas y tipos de
arrays equivalentes y esperar a que termine el cálculo JAX con
`block_until_ready()`. De otro modo puede medirse el envío de la operación en
lugar de su ejecución. La transferencia entre CPU y acelerador también tiene coste.

## Qué debes poder explicar

- Qué diferencia hay entre vectorizar operaciones NumPy y transformar funciones con JAX.
- Qué calcula `grad` y por qué es útil para optimización.
- Por qué la primera ejecución compilada no mide el coste de las siguientes.
- Cuándo basta NumPy y qué necesidad justificaría incorporar JAX.

Esta ampliación no abre por sí sola una nueva entrega evaluable. Las tareas,
rúbricas y fechas se comunicarán por separado. Pandas y la manipulación tabular
pertenecen a UD2, no a este bloque.

## Referencias

- [Introducción oficial a JAX](https://docs.jax.dev/en/latest/quickstart.html).
- [Medición de rendimiento en JAX](https://docs.jax.dev/en/latest/benchmarking.html).
