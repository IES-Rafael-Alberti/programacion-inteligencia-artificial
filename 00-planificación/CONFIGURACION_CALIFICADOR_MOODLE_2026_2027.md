# Configuracion del calificador Moodle - PIA 2026/2027

Esta es la estructura operativa del calificador de PIA. No es un CSV importable:
Moodle importa calificaciones desde CSV, pero las categorias, ponderaciones e
instrumentos se crean en un curso plantilla y se reutilizan mediante copia de
seguridad sin usuarios o importacion de curso.

## Criterio de calculo

- Usar agregacion **Media ponderada de calificaciones** en cada categoria.
- Calificar las evidencias sobre 100 puntos para leer sus pesos directamente.
- Las ponderaciones son internas a cada categoria y suman 100 %.
- Mantener oculto el total general del curso o identificarlo como **informativo**:
  la nota oficial se calcula en Seneca por RA/CE segun
  `PONDERACION_RA_SENECA_2026_2027.md`.
- Usar el valor de `ID` como identificador del item para enlazarlo con la matriz.
- Una tarea o cuestionario crea su item automaticamente. No crear un item manual
  duplicado.
- Las propuestas, checkpoints, ejercicios guiados y ampliaciones opcionales se
  publican sin nota, o con su item oculto y excluido del total.
- UD11 es un anexo opcional y queda fuera de la evaluacion ordinaria.

## Arbol de categorias

```text
PIA 2026/2027 (total informativo, oculto)
|- UD1 - Fundamentos Python
|  `- UD1 - Cuestionarios Moodle
|- UD2 - Tratamiento de datos
|  `- UD2 - Cuestionarios Moodle
|- UD3 - Machine Learning
|  `- UD3 - Cuestionarios Moodle
|- UD4 - Deep Learning
|  `- UD4 - Cuestionarios Moodle
|- UD5 - Cloud y MLOps
|  `- UD5 - Cuestionarios Moodle
|- UD6 - LLM y agentes
|  `- UD6 - Cuestionarios Moodle
|- UD7 - Convergencia de herramientas
|  `- UD7 - Cuestionarios Moodle
|- UD8 - Vision y XAI
|  `- UD8 - Cuestionarios Moodle
|- UD9 - GPU avanzado
|  `- UD9 - Cuestionarios Moodle
|- UD10 - Series temporales
|  `- UD10 - Cuestionarios Moodle
`- UD12 - Proyecto integrado
```

## Items evaluables

| Categoria | Actividad Moodle / item | Tipo | Peso | ID | RA/CE principal |
|---|---|---|---:|---|---|
| UD1 | Practica Python y NumPy | Tarea | 60 % | `ud1-practica-python` | RA1.a, RA1.d/e |
| UD1 | Comparativa de lenguajes y formatos | Tarea | 20 % | `ud1-comparativa-lenguajes` | RA1.b-f |
| UD1 / Cuestionarios | Cuestionario fundamentos Python | Cuestionario | 100 % de cuestionarios | `ud1-quiz-fundamentos` | RA1.a/d |
| UD1 | Total cuestionarios | Categoria | 20 % | `ud1-cuestionarios` | RA1.a/d |
| UD2 | Caso de tratamiento y visualizacion de datos | Tarea | 70 % | `ud2-practica-datos` | RA1.d/e/f, RA2.b-e |
| UD2 / Cuestionarios | Cuestionario tratamiento de datos | Cuestionario | 100 % de cuestionarios | `ud2-quiz-datos` | RA1.d/e, RA2.b |
| UD2 | Total cuestionarios | Categoria | 30 % | `ud2-cuestionarios` | RA1.d/e, RA2.b |
| UD3 | Laboratorio o capstone de ML seleccionado | Tarea | 75 % | `ud3-capstone-ml` | RA2.a-e |
| UD3 / Cuestionarios | Cuestionario Bank Marketing | Cuestionario | 100 % de cuestionarios | `ud3-quiz-bank-marketing` | RA2.b-e |
| UD3 | Total cuestionarios | Categoria | 25 % | `ud3-cuestionarios` | RA2.b-e |
| UD4 | Laboratorios de Deep Learning | Tarea | 75 % | `ud4-laboratorios-dl` | RA2.b-e |
| UD4 / Cuestionarios | Cuestionario Deep Learning | Cuestionario | 100 % de cuestionarios | `ud4-quiz-deep-learning` | RA2.b/c |
| UD4 | Total cuestionarios | Categoria | 25 % | `ud4-cuestionarios` | RA2.b/c |
| UD5 | Tarea comparativa cloud y MLOps | Tarea | 70 % | `ud5-comparativa-cloud` | RA2.a/b, RA3.a-c |
| UD5 / Cuestionarios | Cuestionarios infraestructura y RAG | Dos cuestionarios | 50 % cada uno | `ud5-quiz-*` | RA2.a/b, RA3.b/c |
| UD5 | Total cuestionarios | Categoria | 30 % | `ud5-cuestionarios` | RA2.a/b, RA3.b/c |
| UD6 | Proyecto integrado LLM, RAG y serving | Tarea | 75 % | `ud6-proyecto-llm` | RA2.a-e, RA3.d |
| UD6 / Cuestionarios | Cuestionarios interfaces y orquestacion | Dos cuestionarios | 50 % cada uno | `ud6-quiz-*` | RA2.a/b, RA3.d |
| UD6 | Total cuestionarios | Categoria | 25 % | `ud6-cuestionarios` | RA2.a/b |
| UD7 | Practicas de stack convergente | Tarea o tareas | 40 % | `ud7-practicas-stack` | RA3.a-e, RA4.c |
| UD7 | Proyecto de stack convergente | Tarea | 40 % | `ud7-proyecto-stack` | RA3.a-e, RA4.a/c/d |
| UD7 / Cuestionarios | Cuestionario de integracion | Cuestionario | 100 % de cuestionarios | `ud7-quiz-integracion` | RA3.a-d, RA4.a/c/d |
| UD7 | Total cuestionarios | Categoria | 20 % | `ud7-cuestionarios` | RA3.a-d, RA4.a/c/d |
| UD8 | Proyecto de vision y XAI | Tarea | 75 % | `ud8-proyecto-vision-xai` | RA2.b-e |
| UD8 / Cuestionarios | Cuestionario vision y XAI | Cuestionario | 100 % de cuestionarios | `ud8-quiz-vision-xai` | RA2.b/c |
| UD8 | Total cuestionarios | Categoria | 25 % | `ud8-cuestionarios` | RA2.b/c |
| UD9 | Proyecto o benchmark GPU | Tarea | 75 % | `ud9-proyecto-gpu` | RA1.d/e, RA2.b-e |
| UD9 / Cuestionarios | Cuestionario GPU | Cuestionario | 100 % de cuestionarios | `ud9-quiz-gpu` | RA1.d/e, RA2.b |
| UD9 | Total cuestionarios | Categoria | 25 % | `ud9-cuestionarios` | RA1.d/e, RA2.b |
| UD10 | Proyecto de series temporales | Tarea | 75 % | `ud10-proyecto-series` | RA2.c-e, RA3.e, RA4.d |
| UD10 / Cuestionarios | Cuestionario series temporales | Cuestionario | 100 % de cuestionarios | `ud10-quiz-series` | RA2.b/c/e |
| UD10 | Total cuestionarios | Categoria | 25 % | `ud10-cuestionarios` | RA2.b/c/e |
| UD12 | Proyecto final integrado | Tarea | 80 % | `ud12-proyecto-final` | RA2.c-e, RA3.a-e, RA4.a-d |
| UD12 | Defensa individual | Tarea sin entrega o item manual | 20 % | `ud12-defensa` | RA2.e, RA3.e, RA4.a-d |

El profesorado puede concretar el bloque elegido de UD8 o el laboratorio de UD3,
pero debe conservar el ID y la cobertura prevista. Las actividades opcionales no
reciben peso adicional ni penalizan a quien no las realice.

## Orden de montaje en Moodle

1. Crear el curso plantilla `PIA 2026/2027 - plantilla`, sin alumnado.
2. Crear las once categorias del arbol con media ponderada.
3. Crear las tareas y cuestionarios de UD1 y UD2; mover los items creados a sus
   categorias y aplicar IDs y pesos.
4. Repetir el proceso con UD3 a UD10 segun se publiquen los instrumentos.
5. Crear UD12 y el item manual de defensa cuando se presente el proyecto final.
6. Comprobar con una cuenta de prueba que cada categoria suma 100 % y conservar
   una copia de seguridad sin usuarios.

La matriz de acreditacion se mantiene fuera de los totales Moodle en
`MATRIZ_SEGUIMIENTO_RA_CE_2026_2027.md`. Moodle organiza instrumentos; Seneca
calcula la calificacion oficial por RA/CE.
