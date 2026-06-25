# Teoría UD1 — Fundamentos de Python

Esta carpeta contiene la teoría de apoyo y las guías de la unidad. Para no duplicar material, los conceptos básicos de Python se trabajan principalmente como **teoría guiada en notebooks** dentro de `../02-ejemplos/`.

## Ruta recomendada

| Orden | Tema | Material principal | Apoyo |
|-------|------|--------------------|-------|
| 00 | Presentación de la unidad | `00-guia-unidad.md` | — |
| 01 | Entorno, notebooks y ejecución | `../02-ejemplos/01_introduccion_entorno_python.ipynb` | `01-guia-semana-1-python-basico.md` |
| 02 | Variables, tipos, texto e imports | `02-python-esencial-variables-texto-imports.md`, `../02-ejemplos/02_variables_tipos_operadores.ipynb` | `01-guia-semana-1-python-basico.md` |
| 03 | Control de flujo, funciones y patrones base | `03-python-esencial-control-funciones-patrones.md`, `../02-ejemplos/03_control_flujo_y_funciones.ipynb` | `01-guia-semana-1-python-basico.md` |
| 04 | Estructuras de datos básicas | `../02-ejemplos/04_estructuras_datos_basicas.ipynb` | `04-estructuras-datos-basicas-practica.md` |
| 04b | Estructuras adicionales | `04b-estructuras-datos-adicionales.md` | `../02-ejemplos/04_bis-Estructuras_datos_adicionales.ipynb` |
| 05 | Rendimiento y paso a computación numérica | `../02-ejemplos/05_numpy_rendimiento.ipynb` | `05-guia-semana-2-numpy-jax.md` |
| 06 | NumPy básico | `06-numpy-introduccion.md` | `../02-ejemplos/06_numpy_fundamentos.ipynb` |
| 07 | Broadcasting y vectorización | `07-broadcasting-numpy.md`, `07b-broadcasting-numpy-infografia.md` | `../02-ejemplos/07_numpy_broadcasting_vectorizacion.ipynb` |
| 08 | Introducción comparativa a JAX | `../02-ejemplos/08_introduccion_jax_comparativa.ipynb` | `05-guia-semana-2-numpy-jax.md` |
| 09 | R como complemento | `09-guia-r-complementario.md` | `../02-ejemplos/06_introduccion_R_fundamentos.ipynb` |

## Cobertura

- Los notebooks `01` a `04` de ejemplos son suficientemente explicativos para actuar como teoría práctica.
- Los documentos `02` y `03` no duplican los notebooks: fijan la referencia mínima de Python necesaria para IA antes de pasar a NumPy/Pandas.
- `04b` y `05` son más parciales: conviene usarlos como material de apoyo, no como explicación única.
- NumPy y broadcasting sí tienen documentación teórica específica.
- JAX queda como introducción ligera mediante notebook, sin documento teórico largo para no alargar la unidad.

## Pendiente

- Incorporar evaluación en `../04-evaluacion/` si se decide crear GIFT/rúbrica para la unidad.
