# Teoría UD1 — Fundamentos de Python

Esta carpeta contiene la teoría de apoyo y las guías de la unidad. Para no duplicar material, los conceptos básicos de Python se trabajan principalmente como **teoría guiada en notebooks** dentro de `../02-ejemplos/`.

## Ruta recomendada

| Orden | Tema | Material principal | Apoyo |
|-------|------|--------------------|-------|
| 00 | Presentación de la unidad | `00-guia-unidad.md` | — |
| 01 | Entorno, notebooks y ejecución | `../02-ejemplos/01_introduccion_entorno_python.ipynb` | `01-guia-python-basico.md` |
| 02 | Variables, tipos, texto e imports | `02-python-esencial-variables-texto-imports.md`, `../02-ejemplos/02_variables_tipos_operadores.ipynb` | `01-guia-python-basico.md` |
| 03 | Control de flujo, funciones y patrones base | `03-python-esencial-control-funciones-patrones.md`, `../02-ejemplos/03_control_flujo_y_funciones.ipynb` | `01-guia-python-basico.md` |
| 04 | Estructuras de datos básicas | `../02-ejemplos/04_estructuras_datos_basicas.ipynb` | `04-estructuras-datos-basicas-practica.md` |
| 04b | Estructuras adicionales | `04b-estructuras-datos-adicionales.md` | `../02-ejemplos/04b-estructuras-datos-adicionales.ipynb` |
| 04c | Orientación a objetos | `04c-orientacion-objetos-python.md`, `../02-ejemplos/05_orientacion_objetos_python.ipynb` | — |
| 05 | Introducción y fundamentos de NumPy | `05-numpy-introduccion.md` | `../02-ejemplos/05_numpy_fundamentos.ipynb` |
| 06 | Rendimiento y vectorización con NumPy | `../02-ejemplos/06_numpy_rendimiento.ipynb` | `05-numpy-introduccion.md` |
| 07 | Broadcasting y vectorización | `07-broadcasting-numpy.md`, `07b-broadcasting-numpy-infografia.md` | `../02-ejemplos/07_numpy_broadcasting_vectorizacion.ipynb` |
| 08 | Introducción comparativa a JAX | `../02-ejemplos/08_introduccion_jax_comparativa.ipynb` | `08-guia-numpy-jax.md` |
| 09 | R como complemento | `09-guia-r-complementario.md` | `../02-ejemplos/06_introduccion_R_fundamentos.ipynb` |
| 10 | Comparativa de lenguajes y formatos para IA | `../04-evaluacion/comparativa-lenguajes-formatos-ia.md` | Python, R, Java, JavaScript/NodeJS, JSON, YAML, Markdown, XML/HTML |

## Cobertura

- Los notebooks `01` a `04` de ejemplos son suficientemente explicativos para actuar como teoría práctica.
- Los documentos `02` y `03` no duplican los notebooks: fijan la referencia mínima de Python necesaria para IA. `04c` añade una guía específica de POO como preparación para PyTorch, antes de pasar a NumPy/Pandas.
- `04b` es material de apoyo; NumPy se introduce antes de medir rendimiento y trabajar broadcasting.
- NumPy y broadcasting sí tienen documentación teórica específica.
- JAX es una ampliación posterior a NumPy: la guía `08` explica qué aporta y prepara el notebook comparativo, sin sustituir los fundamentos.

## Pendiente

- Decidir si JAX queda como introducción ligera o se desarrolla como bloque propio más adelante.
