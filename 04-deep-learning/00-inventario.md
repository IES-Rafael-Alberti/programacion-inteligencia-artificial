# Inventario de UD4 — Deep Learning

Este documento inventaría la unidad **04-deep-learning** para decidir después si se mantiene como una sola UD con subbloques o si se divide en varias unidades.

## Veredicto rápido

UD4 está **funcionalmente completa**, pero **estructuralmente sobrecargada**.

El problema no es la falta de contenido, sino la mezcla de capas distintas:

- fundamentos matemáticos y de redes;
- frameworks;
- modelado avanzado;
- visión;
- NLP;
- muchos artefactos generados a partir de `.md`.

## Volumen por áreas

| Área | Estado | Lectura rápida |
|---|---|---|
| `01-teoria/01-redes-neuronales-genericas/` | Muy cargada | Mezcla fundamentos, frameworks y modelado avanzado. Es el principal foco de división. |
| `01-teoria/02-redes-neuronales-vision/` | Coherente | Área de visión razonablemente compacta. |
| `01-teoria/03-redes-neuronales-nlp/` | Coherente | Área de NLP más limpia que la genérica. |
| `02-ejemplos/` | Muy grande pero utilizable | Mucho material, bastante repartido por subdominios. |
| `03-practicas/` | Grande pero funcional | Tiene labs, proyectos y tareas separables. |
| `04-evaluacion/` | Pequeña | No es el problema estructural. |
| `05-recursos/` | Muy grande | Hay mucho recurso pesado, especialmente en visión. |
| `90-archivo/` | Pequeña | Material histórico, no debería mezclarse con activo. |
| `99-profesor/` | Pequeña | Material docente privado, no debe contaminar el flujo público. |

## Inventario de la teoría

### 1) `01-redes-neuronales-genericas/`

#### 1.1 `fundamentos-docs/`

Contiene:

- índice de la parte teórica;
- capítulos de introducción a redes neuronales;
- representación matemática;
- tensores;
- activación y función de pérdida;
- derivadas y gradientes;
- gradiente descendente;
- backpropagation y complementos;
- glosario;
- preguntas y respuestas.

**Lectura:** bloque base de fundamentos. Debe quedarse junto, pero no mezclado con frameworks ni modelado avanzado.

#### 1.2 `frameworks-docs/`

Contiene:

- introducciones a Keras, PyTorch, JAX y PyTorch Lightning;
- DataLoader;
- optimizadores;
- planificación de la parte de frameworks.

**Lectura:** bloque técnico de herramientas/frameworks. Tiene sentido separado de fundamentos.

#### 1.3 `modelado-avanzado-docs/`

Contiene:

- conceptos de visión, CNN, RNN, atención y NLP;
- comparativas de frameworks;
- tensorflow bajo nivel y Data API;
- métricas;
- libros de referencia;
- teoría de modelado avanzado;
- guías de proyecto.

**Lectura:** bloque más heterogéneo y más grande. Aquí se mezclan teoría, conceptos, frameworks, métricas y bibliografía. Es el segundo foco de limpieza.

### 2) `02-redes-neuronales-vision/`

Contiene:

- teoría de visión clásica;
- CNN;
- ecosistema deep learning;
- guía del profesorado;
- modelos alternativos tipo SSM/LFM/Mamba/RWKV.

**Lectura:** bloque coherente, aunque conviene separar bien visión clásica de alternativas más experimentales.

### 3) `03-redes-neuronales-nlp/`

Contiene:

- introducción a NLP;
- Keras-NLP;
- PyTorch-NLP;
- embeddings;
- guía spaCy;
- material “NLP-nuevo” con varias secciones;
- demos.

**Lectura:** bloque más limpio que el de genéricas. Se puede mantener como subunidad o incluso como unidad independiente si se decide partir UD4.

## Inventario de ejemplos

### `02-ejemplos/frameworks/`

Ejemplos y notebooks de:

- frameworks;
- red neuronal básica;
- optimizadores;
- actividades y datos.

### `02-ejemplos/fundamentos-notebooks/`

Ejemplos base de fundamentos.

### `02-ejemplos/fundamentos-scripts/`

Scripts auxiliares de fundamentos.

### `02-ejemplos/modelado-avanzado-ejemplos/`

Contiene el ejemplo grande `fashion-mnist-flask/`.

### `02-ejemplos/nlp-spacy/`

Ejemplos de spaCy.

### `02-ejemplos/nlp-transformers/`

Bloque grande y muy denso:

- datos;
- docs;
- modelos;
- notebooks;
- scripts;
- tareas;
- material antiguo;
- zips.

### `02-ejemplos/vision-scripts/` y `02-ejemplos/vision-yolo/`

Material de visión y scripts asociados.

**Lectura general:** ejemplos muy potentes, pero necesitan una poda clara si se quiere que la unidad sea legible.

## Inventario de prácticas

### `03-practicas/laboratorios/`

- Laboratorio 1: TensorFlow Playground.
- Laboratorio 2: backpropagation.
- Laboratorio 3: de Playground a código real.

### `03-practicas/modelado-notebooks/`

- fundamentos;
- series temporales;
- visión.

### `03-practicas/modelado-proyectos/`

Proyectos:

- Boston Housing;
- Euromillones;
- House Prices Kaggle;
- Used Cars.

### `03-practicas/nlp-tareas/`

Tareas de NLP.

### `03-practicas/vision-tareas/`

Tareas de visión.

**Lectura general:** la práctica está bien separada por tipo, pero el número de carpetas hace que UD4 parezca todavía más grande.

## Inventario de evaluación

### `04-evaluacion/`

Debe contener la evaluación canónica de la unidad.

**Lectura:** no es el problema principal; el problema es la masa de teoría y ejemplos alrededor.

## Inventario de recursos

### `05-recursos/`

Incluye:

- datasets de modelado;
- entornos;
- datos de NLP;
- datos de visión.

**Lectura:** hay mucho material útil, pero conviene separar mejor qué es recurso activo y qué es dato pesado de soporte.

## Inventario de archivo y profesorado

### `90-archivo/`

Material histórico de fundamentos.

### `99-profesor/`

Material privado de docencia.

**Lectura:** estos bloques deben quedar claramente fuera del flujo de alumnado.

## Decisiones que quedan pendientes a partir de este inventario

1. Decidir si UD4 se divide en **3 unidades**:
   - fundamentos;
   - frameworks/modelado avanzado;
   - visión + NLP;
   o si se mantiene como una sola UD con subbloques muy claros.
2. Decidir qué parte de `modelado-avanzado-docs/` se queda en teoría activa y qué parte pasa a archivo.
3. Decidir qué generados se eliminan y cuáles se conservan solo como derivado de publicación.
4. Limpiar la frontera entre material de teoría, ejemplos, prácticas y archivo.

## Conclusión provisional

UD4 sí puede seguir funcionando, pero **no está preparada para considerarse cerrada** en el sentido estructural.

El siguiente paso no es mover piezas al azar: es decidir la división de la unidad a partir de este inventario.
