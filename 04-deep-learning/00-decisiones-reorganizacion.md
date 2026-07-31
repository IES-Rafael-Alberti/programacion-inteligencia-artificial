# Decisiones de reorganización — UD4 Deep Learning

Este documento propone qué hacer con cada bloque de `04-deep-learning/` antes de mover, archivar o eliminar material.

La regla general es: **UD4 debe quedarse como Deep Learning base**. Lo que sea visión aplicada debe ir a UD8; lo que sea NLP/transformers aplicado debe ir a UD6; lo que sea generado o bibliografía pesada debe salir del flujo activo.

## Leyenda

| Decisión | Significado |
|---|---|
| Mantener | Sigue siendo parte activa de UD4. |
| Mantener reorganizado | Sigue en UD4, pero con ruta/nombre más claro. |
| Mover | Debe pasar a otra unidad activa. |
| Archivar | Se conserva fuera del flujo principal. |
| Eliminar generado | Se puede borrar si existe fuente `.md` o no aporta valor docente directo. |
| Revisar manualmente | No mover todavía; requiere inspección puntual. |

## Tabla de decisiones

| Ruta actual | Qué contiene | Decisión propuesta | Destino propuesto | Motivo | Riesgo / comprobación |
|---|---|---|---|---|---|
| `04-deep-learning/README.md` | Descripción general de UD4. | Mantener reorganizado | `04-deep-learning/README.md` | Debe explicar la nueva frontera de UD4: fundamentos + frameworks base. | Actualizar después de mover/archivar. |
| `04-deep-learning/01-teoria/README.md` | Índice de teoría. | Mantener reorganizado | `04-deep-learning/01-teoria/README.md` | Debe convertirse en mapa de lectura corto. | Evitar que enlace a material movido sin actualizar. |
| `01-teoria/01-redes-neuronales-genericas/fundamentos-docs/` | Fundamentos: redes, tensores, activaciones, pérdidas, gradiente, backpropagation. | Mantener reorganizado | `04-deep-learning/01-teoria/01-fundamentos-redes-neuronales/` | Es el corazón de UD4. | Revisar duplicados y generados antes de mover. |
| `fundamentos-docs/Parte-I-Fundamentos/*.md` | Fuentes Markdown de fundamentos. | Mantener | Nueva carpeta de fundamentos UD4. | Son fuente activa. | Ordenar índice y dejar secuencia docente única. |
| `fundamentos-docs/Parte-I-Fundamentos/*.pdf` | PDFs generados desde Markdown. | Eliminar generado o archivar | `90-archivo/generados/ud4-fundamentos/` si se conservan | No deben vivir junto a la fuente activa. | Confirmar que existe `.md` equivalente antes de borrar. |
| `fundamentos-docs/Parte-I-Fundamentos/*.html` | HTML generado desde Markdown. | Eliminar generado | Ninguno | El sitio se genera desde Markdown; mantener HTML duplica ruido. | Confirmar fuente `.md`. |
| `fundamentos-docs/Parte-I-Fundamentos/*.docx` | Documentos editables/generados. | Revisar manualmente | `90-archivo/generados/ud4-fundamentos/` | Puede haber versiones alternativas no equivalentes al `.md`. | No borrar sin comparar. |
| `01-teoria/02-frameworks-deep-learning/frameworks-docs/` | Keras, PyTorch, JAX, Lightning, DataLoader, optimizadores. | Mantener reorganizado | `04-deep-learning/01-teoria/02-frameworks-deep-learning/` | Pertenece a UD4 como introducción a frameworks. | Evitar duplicar con UD9/JAX avanzado. |
| `frameworks-docs/introduccion/*.md` | Introducciones a frameworks. | Mantener | Nueva carpeta de frameworks UD4. | Material activo y útil. | Crear una ruta de lectura única: no todos los frameworks al mismo nivel de profundidad. |
| `frameworks-docs/introduccion/*.html` | HTML generado. | Eliminar generado | Ninguno | Duplicado de Markdown. | Confirmar fuente `.md`. |
| `frameworks-docs/optimizadores/*.md` | Teoría de optimizadores. | Mantener | Nueva carpeta de frameworks/fundamentos UD4. | Es contenido base de DL. | Puede integrarse con fundamentos o frameworks. |
| `frameworks-docs/optimizadores/*.html` | HTML generado. | Eliminar generado | Ninguno | Duplicado de Markdown. | Confirmar fuente `.md`. |
| `frameworks-docs/planificacion/` | Planificación de la parte práctica/frameworks. | Mantener reorganizado | `04-deep-learning/01-teoria/00-planificacion/` o integrar en README | Útil para el profesor, pero no debe dispersar teoría. | Separar lo docente de lo público si procede. |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/` | Mezcla conceptos, frameworks, métricas, teoría, libros, visión y NLP. | Desguazar | Varios destinos | Es el principal bloque problemático. | Requiere aplicar decisiones por subcarpeta. |
| `modelado-avanzado-docs/conceptos/RedesConvolucionales.md` | CNN / visión. | Mover | `08-vision-xai/01-teoria/` | Encaja mejor en visión. UD4 puede enlazarlo como ampliación. | Revisar enlaces e imágenes. |
| `modelado-avanzado-docs/conceptos/Datasets_para_vision_y_transfer_learning.md` | Datasets de visión y transfer learning. | Mover | `08-vision-xai/01-teoria/` o `08-vision-xai/05-recursos/` | Es visión aplicada. | Confirmar si depende de datasets locales en UD4. |
| `modelado-avanzado-docs/conceptos/Keras_vs_PyTorch_en_vision.md` | Comparativa aplicada a visión. | Mover | `08-vision-xai/01-teoria/` | Su contexto natural es visión. | Puede dejarse enlace desde UD4 frameworks. |
| `modelado-avanzado-docs/conceptos/NLP_Atencion.md` | Atención/NLP. | Mover | `06-llm-agentes/01-teoria/` o archivo de NLP | Encaja mejor con NLP/LLM. | Decidir si es contenido activo o histórico. |
| `modelado-avanzado-docs/conceptos/RedesRecurrentes.md` | RNN/LSTM. | Revisar manualmente | UD4 si es arquitectura base; UD6/10 si está aplicado a NLP/series | Puede servir como arquitectura DL base, pero también como puente a NLP/series. | Leer antes de mover. |
| `modelado-avanzado-docs/conceptos/TensorFlow_BajoNivel.md` | TensorFlow bajo nivel. | Archivar o mantener como ampliación | `04-deep-learning/90-archivo/tensorflow-avanzado/` o `01-teoria/02-frameworks...` | No parece núcleo obligatorio. | Ver si hay prácticas activas que lo usen. |
| `modelado-avanzado-docs/conceptos/TensorFlow_DataAPI.md` | TensorFlow Data API. | Archivar o mantener como ampliación | `04-deep-learning/90-archivo/tensorflow-avanzado/` | Útil, pero puede ser demasiado específico. | Ver dependencia con prácticas. |
| `modelado-avanzado-docs/conceptos/tf_df_imgs.md` | TensorFlow / imágenes. | Mover o archivar | `08-vision-xai/` o archivo | Si es visión aplicada, no debe cargar UD4. | Revisar contenido. |
| `modelado-avanzado-docs/conceptos/Mas_alla_del_entrenamiento.md` | Buenas prácticas tras entrenamiento. | Mantener reorganizado | UD4 o UD7 según enfoque | Si habla de evaluación/producción, puede encajar en UD7. | Revisar si es técnico DL o MLOps. |
| `modelado-avanzado-docs/frameworks/*.md` | JAX, Keras3, MLX, ONNX, PyTorch, Lightning, TensorFlow. | Mantener reorganizado | `04-deep-learning/01-teoria/02-frameworks-deep-learning/` | Es contenido de frameworks DL. | Evitar duplicado con `frameworks-docs/`. |
| `modelado-avanzado-docs/frameworks/*tutorial.pdf` | Tutoriales PDF de frameworks. | Archivar | `04-deep-learning/90-archivo/bibliografia-frameworks/` | Bibliografía/derivado pesado fuera del flujo activo. | Confirmar licencia/origen si se conserva. |
| `modelado-avanzado-docs/metricas/*.md` | Métricas, curvas, regresión, bias/variance. | Mantener reorganizado | `04-deep-learning/01-teoria/03-metricas-evaluacion/` | Es esencial para RA2.e. | Revisar solapamiento con UD3. |
| `modelado-avanzado-docs/metricas/*.pdf` | PDFs generados o referencias. | Eliminar generado o archivar | `90-archivo/generados/ud4-metricas/` | No deben estar en teoría activa. | Confirmar fuente `.md`. |
| `modelado-avanzado-docs/metricas/*.html` | HTML generado. | Eliminar generado | Ninguno | Duplicado de Markdown. | Confirmar fuente `.md`. |
| `modelado-avanzado-docs/teoria/001-DeepLearningV2.md` | Teoría general DL. | Mantener o fusionar | `01-fundamentos-redes-neuronales/` | Puede duplicar fundamentos. | Comparar con capítulos de fundamentos. |
| `modelado-avanzado-docs/teoria/002-Comparativa_Frameworks.md` | Comparativa frameworks. | Mantener | `02-frameworks-deep-learning/` | Muy útil para ordenar herramientas. | Evitar duplicidad con planificación. |
| `modelado-avanzado-docs/teoria/002-Underfit-Overfit_BiasVariance.md` | Generalización, sesgo/varianza. | Mantener | `03-metricas-evaluacion/` | Núcleo de evaluación de modelos. | Puede enlazar con UD3. |
| `modelado-avanzado-docs/teoria/GUIA_PROYECTO_PYTHON_ML.md` | Guía de proyecto ML. | Mover o archivar | `03-machine-learning/` o `12-proyecto-integrado/90-archivo/` | No es específico de DL. | Revisar si se usa activamente. |
| `modelado-avanzado-docs/teoria/*.pdf`, `*.html`, `*.tex` | Generados o fuentes antiguas. | Eliminar generado o archivar | `90-archivo/generados/ud4-modelado/` | Ensucian la teoría activa. | No borrar `.tex` si es fuente única. |
| `modelado-avanzado-docs/libros/` | PDFs/EPUB de libros y referencias. | Archivar | `04-deep-learning/90-archivo/bibliografia/` o fuera del repo público | Bibliografía pesada no debe estar en flujo activo. | Revisar derechos/licencias y tamaño. |
| `01-teoria/02-redes-neuronales-vision/` | Teoría de visión, CNN, modelos alternativos, guía profesor. | Mover parcialmente | `08-vision-xai/01-teoria/` | UD8 ya existe para visión/XAI. | UD4 puede conservar una introducción mínima a CNN. |
| `02-redes-neuronales-vision/vision-teoria/01-CNN.md` | CNN. | Mantener copia mínima o mover | UD4 introducción mínima + UD8 desarrollo completo | CNN es puente entre DL y visión. | Decidir si se duplica como resumen o se enlaza. |
| `02-redes-neuronales-vision/vision-teoria/00-VisionArtificialClasica.md` | Visión clásica. | Mover | `08-vision-xai/01-teoria/` | No es deep learning base. | Revisar enlaces a recursos. |
| `02-redes-neuronales-vision/vision-teoria/002-ud4_cnn_y_evolucion_modelos.md` | CNN y evolución. | Mover o resumir | UD8; resumen en UD4 | Es desarrollo de visión. | Mantener sólo introducción si se necesita para DL. |
| `02-redes-neuronales-vision/vision-teoria/modelos_alternativos/` | LFM, Mamba, RWKV, SSM y comparativas. | Archivar o mover como ampliación | `08-vision-xai/05-recursos/modelos-alternativos/` o `11-anexos/` | Material avanzado/experimental, no núcleo UD4. | No mezclar con flujo obligatorio. |
| `02-redes-neuronales-vision/vision-teoria/*profesor*` | Guías profesor. | Mover a profesor o archivar | `08-vision-xai/99-profesor/` o `04-deep-learning/99-profesor/` | No debe estar en teoría pública. | Revisar nombres con “profesor”. |
| `01-teoria/03-redes-neuronales-nlp/` | NLP, embeddings, Keras/PyTorch NLP, spaCy, BERT. | Mover parcialmente | `06-llm-agentes/01-teoria/` o `06-llm-agentes/05-recursos/` | UD6 ya concentra LLM/agentes/RAG. | UD4 puede conservar sólo nota de RNN/transformers como arquitectura. |
| `03-redes-neuronales-nlp/nlp-docs/000-Introduccion_A_NLP.md` | Introducción NLP. | Mover | `06-llm-agentes/01-teoria/nlp/` | Encaja con UD6. | Ver si duplica contenido actual. |
| `03-redes-neuronales-nlp/nlp-docs/001-Keras-NLP.md` | Keras NLP. | Mover o archivar | `06-llm-agentes/05-recursos/nlp/` | Aplicación NLP, no núcleo UD4. | Revisar actualidad. |
| `03-redes-neuronales-nlp/nlp-docs/001-Pytorch-NLP.md` | PyTorch NLP. | Mover o archivar | `06-llm-agentes/05-recursos/nlp/` | Aplicación NLP, no núcleo UD4. | Revisar actualidad. |
| `03-redes-neuronales-nlp/nlp-docs/002-NLP-Embeddings.md` | Embeddings. | Mover | `06-llm-agentes/01-teoria/` | Muy útil para LLM/RAG. | Revisar integración con RAG. |
| `03-redes-neuronales-nlp/nlp-docs/003-spacy-guia.md` | spaCy. | Mover | `06-llm-agentes/05-recursos/nlp/` o archivo | NLP clásico de apoyo. | Puede ser opcional, no central. |
| `03-redes-neuronales-nlp/nlp-docs/NLP-nuevo/` | Bloque nuevo NLP/BERT/pro. | Mover o archivar | `06-llm-agentes/01-teoria/nlp/` | Mejor contexto en UD6. | Revisar solape con LLM actual. |
| `03-redes-neuronales-nlp/nlp-libros/` | Bibliografía NLP. | Archivar | `06-llm-agentes/90-archivo/bibliografia-nlp/` o fuera del repo público | Bibliografía pesada fuera de flujo activo. | Revisar derechos/licencias. |
| `02-ejemplos/frameworks/` | Ejemplos de frameworks, redes y optimizadores. | Mantener reorganizado | `04-deep-learning/02-ejemplos/frameworks/` | Pertenece a UD4. | Limpiar datos pesados si hay duplicados. |
| `02-ejemplos/fundamentos-notebooks/` | Notebooks de fundamentos. | Mantener | `04-deep-learning/02-ejemplos/fundamentos/` | Apoya el núcleo de UD4. | Renombrar si se reorganiza. |
| `02-ejemplos/fundamentos-scripts/` | Scripts auxiliares de fundamentos. | Mantener | `04-deep-learning/02-ejemplos/fundamentos-scripts/` | Apoyo directo a fundamentos. | Revisar si scripts generan imágenes/artefactos. |
| `02-ejemplos/modelado-avanzado-ejemplos/fashion-mnist-flask/` | Demo/app FashionMNIST Flask. | Revisar manualmente | UD4 o UD8 | Puede ser DL aplicado o visión aplicada. | Decidir según uso docente. |
| `02-ejemplos/nlp-spacy/` | Ejemplos spaCy. | Mover | `06-llm-agentes/02-ejemplos/nlp-spacy/` | NLP debe vivir en UD6. | Actualizar referencias. |
| `02-ejemplos/nlp-transformers/` | Docs, notebooks, scripts, tareas y modelos transformers. | Mover o archivar parcialmente | `06-llm-agentes/02-ejemplos/transformers/` y/o `06-llm-agentes/90-archivo/` | Transformers/NLP encajan en UD6. | Revisar tamaño, modelos y zips. |
| `02-ejemplos/nlp-transformers/zips/` | Zips de apoyo. | Archivar o eliminar | `06-llm-agentes/90-archivo/transformers-zips/` | No deben estar en flujo activo. | Confirmar si contienen fuentes únicas. |
| `02-ejemplos/vision-scripts/` | Scripts visión. | Mover | `08-vision-xai/02-ejemplos/` | Visión debe vivir en UD8. | Revisar dependencias de rutas. |
| `02-ejemplos/vision-yolo/` | YOLO / visión. | Mover | `08-vision-xai/02-ejemplos/` o `08-vision-xai/03-practicas/` | Encaja directamente en UD8. | Separar ejemplos de prácticas. |
| `03-practicas/laboratorios/` | Labs base DL: Playground, backpropagation, código real. | Mantener | `04-deep-learning/03-practicas/laboratorios/` | Núcleo práctico de UD4. | Revisar generados PDF/TeX. |
| `03-practicas/laboratorios/*.pdf`, `*.tex` | Enunciados/generados de labs. | Revisar manualmente | Mantener si son fuente de entrega; archivar si son generados | Puede haber fuentes únicas en TeX. | No borrar sin confirmar Markdown equivalente. |
| `03-practicas/modelado-notebooks/fundamentos/` | Prácticas de fundamentos. | Mantener | UD4. | Núcleo DL. | Ninguno. |
| `03-practicas/modelado-notebooks/series-temporales/` | Notebooks series temporales. | Mover | `10-series-temporales/` | Ya existe UD10. | Revisar si son DL temporal o taller viejo. |
| `03-practicas/modelado-notebooks/vision/` | Notebooks visión. | Mover | `08-vision-xai/03-practicas/` | Visión debe vivir en UD8. | Actualizar evaluación si se mueve. |
| `03-practicas/modelado-proyectos/boston-housing/` | Proyecto tabular/regresión con Keras, PyTorch y variantes tipo scikit-learn. | Mantener | `04-deep-learning/03-practicas/modelado-proyectos/boston-housing/` | Encaja en UD4 como práctica de regresión tabular con redes neuronales. | Saneamiento documental cerrado; corregir baseline, escalado y métricas si se convierte en práctica evaluable. |
| `03-practicas/modelado-proyectos/euromillones/` | Proyecto predictor. | Revisar manualmente | Archivo o UD4 si es laboratorio DL | Riesgo de baja calidad didáctica si es azar/predicción dudosa. | Revisar antes de mantener activo. |
| `03-practicas/modelado-proyectos/house-prices-kaggle/` | Proyecto Kaggle tabular. | Revisar manualmente | UD3 o archivo | Parece más ML clásico que DL. | Ver enfoque real. |
| `03-practicas/modelado-proyectos/used-cars/` | Proyecto tabular con MLflow/mlruns. | Mover o archivar | UD3/UD5/UD7 o archivo | No parece núcleo DL y contiene `mlruns`. | Revisar tamaño y artefactos generados. |
| `03-practicas/nlp-tareas/` | Tareas NLP. | Mover | `06-llm-agentes/03-practicas/nlp/` | NLP debe salir de UD4. | Revisar si son activas o históricas. |
| `03-practicas/vision-tareas/` | Tareas visión. | Mover | `08-vision-xai/03-practicas/` | Visión debe salir de UD4. | Separar enunciados de soluciones/profesor. |
| `04-evaluacion/` | Rúbrica, checklist, GIFT. | Mantener y revisar después | `04-deep-learning/04-evaluacion/` | La evaluación debe adaptarse a la nueva frontera de UD4. | Tras mover visión/NLP, puede sobrar contenido en la rúbrica/GIFT. |
| `05-recursos/modelado-datos/` | Datasets de modelado. | Revisar manualmente | UD4/UD3/archivo según uso | Puede ser soporte de prácticas activas. | No mover sin saber qué notebook lo usa. |
| `05-recursos/modelado-entornos/` | Entornos de frameworks. | Mantener reorganizado | `04-deep-learning/05-recursos/entornos/` | Soporte UD4 frameworks. | Revisar obsolescencia. |
| `05-recursos/nlp-datos/` | Datos NLP. | Mover | `06-llm-agentes/05-recursos/nlp-datos/` | NLP sale de UD4. | Revisar tamaño/derechos. |
| `05-recursos/vision-data/` | Datos visión pesados. | Mover o archivar | `08-vision-xai/05-recursos/vision-data/` o archivo externo | Visión sale de UD4; datasets pueden ser pesados. | Revisar si deben estar en Git. |
| `05-recursos/vision-datos/` | Datos visión. | Mover o archivar | `08-vision-xai/05-recursos/vision-datos/` | Visión sale de UD4. | Revisar duplicado con `vision-data`. |
| `90-archivo/fundamentos-old/` | Material histórico de fundamentos. | Mantener archivado | `04-deep-learning/90-archivo/fundamentos-old/` | Ya está fuera de activo. | No reactivar por inercia. |
| `99-profesor/` | Material docente privado. | Mantener privado | `04-deep-learning/99-profesor/` | Separación correcta. | Si se mueve NLP/visión, mover profesor correspondiente con su unidad. |

## Reglas de limpieza de generados

| Patrón | Decisión por defecto | Condición |
|---|---|---|
| `*.html` dentro de teoría/prácticas | Eliminar generado | Si existe `.md` equivalente o si MkDocs lo genera en `site/`. |
| `*.pdf` junto a `.md` | Archivar o eliminar generado | Conservar sólo si es material final de entrega o no hay fuente editable. |
| `*.docx` | Revisar manualmente | Puede ser fuente original o alternativa. |
| `*.tex` | Revisar manualmente | Puede ser fuente única de PDF. |
| `*_profesor*`, `*profesor*` | Mover a `99-profesor/` o archivo privado | No debe quedar en flujo público. |
| `zips/` | Archivar o eliminar | Confirmar si contienen fuente única. |
| `mlruns/`, modelos entrenados, checkpoints | Archivar o ignorar | No deben contaminar una unidad docente ligera salvo que sean imprescindibles. |

## Propuesta de frontera final

### UD4 — Deep Learning base

Debe quedarse con:

- fundamentos de redes neuronales;
- backpropagation, gradiente, tensores, activaciones y pérdidas;
- métricas básicas y generalización;
- frameworks base: Keras, PyTorch, JAX, Lightning;
- laboratorios introductorios.

### UD6 — NLP, Transformers y LLM

Debe recibir:

- NLP clásico;
- embeddings;
- transformers;
- BERT;
- spaCy;
- tareas y ejemplos NLP.

### UD8 — Visión y XAI

Debe recibir:

- visión clásica;
- CNN aplicada;
- transfer learning;
- YOLO;
- datasets y scripts de visión;
- modelos alternativos de visión si se mantienen activos.

### UD10 — Series temporales

Debe recibir:

- notebooks o prácticas temporales que ahora estén en UD4.

## Próximo paso recomendado

Aplicar primero una limpieza **no destructiva**:

1. Mover/archivar generados claros (`*.html`) cuando exista `.md`.
2. Separar visión hacia UD8.
3. Separar NLP hacia UD6.
4. Revisar `modelado-avanzado-docs/` archivo por archivo.

No conviene tocar datasets pesados, PDFs, DOCX, TeX ni zips hasta confirmar si son fuente única.

## Limpieza aplicada

### 2026-07-04 — HTML generados con Markdown equivalente

Se eliminaron **45 ficheros `.html`** dentro de `04-deep-learning/` que tenían un `.md` equivalente con el mismo nombre base en la misma carpeta.

No se tocaron:

- PDFs;
- DOCX;
- TeX;
- zips;
- datasets;
- modelos;
- checkpoints;
- HTML sin `.md` homónimo.

### 2026-07-04 — Fuente Markdown recuperada para underfit/overfit

Se recuperó la fuente Markdown de:

`/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD4/04-modelado-avanzado/docs/teoria/002-Underfit-Overfit_BiasVariance.md`

y se copió como:

`04-deep-learning/01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/metricas/Underfit-Overfit_BiasVariance.md`

Después se eliminó:

`04-deep-learning/01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/metricas/Underfit-Overfit_BiasVariance.html`

Resultado: **no quedan ficheros `.html` dentro de `04-deep-learning/`**.

### 2026-07-04 — Reorganización por frontera conceptual

Se aplicó la separación principal acordada: UD4 queda como **Deep Learning base** y los bloques aplicados salen a sus unidades naturales.

#### Movido a UD6 — LLM, NLP y agentes

| Origen | Destino |
|---|---|
| `04-deep-learning/01-teoria/03-redes-neuronales-nlp/` | `06-llm-agentes/01-teoria/nlp-deep-learning-ud4/` |
| `04-deep-learning/01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/conceptos/NLP_Atencion.md` | `06-llm-agentes/01-teoria/nlp-deep-learning-ud4/NLP_Atencion_desde_modelado_avanzado.md` |
| `04-deep-learning/02-ejemplos/nlp-spacy/` | `06-llm-agentes/02-ejemplos/nlp-spacy-ud4/` |
| `04-deep-learning/02-ejemplos/nlp-transformers/` | `06-llm-agentes/02-ejemplos/nlp-transformers-ud4/` |
| `04-deep-learning/03-practicas/nlp-tareas/` | `06-llm-agentes/03-practicas/nlp-tareas-ud4/` |
| `04-deep-learning/05-recursos/nlp-datos/` | `06-llm-agentes/05-recursos/nlp-datos-ud4/` |
| `04-deep-learning/99-profesor/nlp-spacy/` | `06-llm-agentes/99-profesor/nlp-spacy-ud4/` |

Los subdirectorios pesados `modelos/` y `zips/` de transformers se sacaron del flujo activo y quedaron en:

- `06-llm-agentes/90-archivo/nlp-transformers-ud4/modelos/`
- `06-llm-agentes/90-archivo/nlp-transformers-ud4/zips/`

#### Movido a UD8 — Visión y XAI

| Origen | Destino |
|---|---|
| `04-deep-learning/01-teoria/02-redes-neuronales-vision/` | `08-vision-xai/01-teoria/redes-neuronales-vision-ud4/` |
| `04-deep-learning/01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/conceptos/RedesConvolucionales.md` | `08-vision-xai/01-teoria/deep-learning-desde-ud4/RedesConvolucionales.md` |
| `04-deep-learning/01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/conceptos/Datasets_para_vision_y_transfer_learning.md` | `08-vision-xai/01-teoria/deep-learning-desde-ud4/Datasets_para_vision_y_transfer_learning.md` |
| `04-deep-learning/01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/conceptos/Keras_vs_PyTorch_en_vision.md` | `08-vision-xai/01-teoria/deep-learning-desde-ud4/Keras_vs_PyTorch_en_vision.md` |
| `04-deep-learning/01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/conceptos/tf_df_imgs.md` | `08-vision-xai/01-teoria/deep-learning-desde-ud4/tf_df_imgs.md` |
| `04-deep-learning/02-ejemplos/vision-scripts/` | `08-vision-xai/02-ejemplos/vision-scripts-ud4/` |
| `04-deep-learning/02-ejemplos/vision-yolo/` | `08-vision-xai/02-ejemplos/vision-yolo-ud4/` |
| `04-deep-learning/03-practicas/modelado-notebooks/vision/` | `08-vision-xai/03-practicas/modelado-notebooks-vision-ud4/` |
| `04-deep-learning/03-practicas/vision-tareas/` | `08-vision-xai/03-practicas/vision-tareas-ud4/` |
| `04-deep-learning/05-recursos/vision-data/` | `08-vision-xai/05-recursos/vision-data-ud4/` |
| `04-deep-learning/05-recursos/vision-datos/` | `08-vision-xai/05-recursos/vision-datos-ud4/` |

#### Movido a UD10 — Series temporales

| Origen | Destino |
|---|---|
| `04-deep-learning/03-practicas/modelado-notebooks/series-temporales/` | `10-series-temporales/03-practicas/modelado-notebooks-series-ud4/` |

#### Queda en UD4 para revisión posterior

- `01-teoria/01-redes-neuronales-genericas/`
- `02-ejemplos/frameworks/`
- `02-ejemplos/fundamentos-notebooks/`
- `02-ejemplos/fundamentos-scripts/`
- `02-ejemplos/modelado-avanzado-ejemplos/`
- `03-practicas/laboratorios/`
- `03-practicas/modelado-notebooks/fundamentos/`
- `03-practicas/modelado-proyectos/`
- `05-recursos/modelado-datos/`
- `05-recursos/modelado-entornos/`

El siguiente foco de revisión ya no es visión/NLP, sino **modelado avanzado y proyectos tabulares** dentro de UD4.

### 2026-07-04 — Reorganización interna de UD4 base

Se movieron los bloques internos claros para que UD4 tenga una estructura legible:

| Origen | Destino |
|---|---|
| `01-teoria/01-redes-neuronales-genericas/fundamentos-docs/` | `01-teoria/01-fundamentos-redes-neuronales/` |
| `01-teoria/02-frameworks-deep-learning/frameworks-docs/` | `01-teoria/02-frameworks-deep-learning/frameworks-docs/` |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/frameworks/` | `01-teoria/02-frameworks-deep-learning/frameworks-avanzados/` |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/conceptos/TensorFlow_BajoNivel.md` | `01-teoria/02-frameworks-deep-learning/tensorflow-avanzado/TensorFlow_BajoNivel.md` |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/conceptos/TensorFlow_DataAPI.md` | `01-teoria/02-frameworks-deep-learning/tensorflow-avanzado/TensorFlow_DataAPI.md` |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/teoria/002-Comparativa_Frameworks.md` | `01-teoria/02-frameworks-deep-learning/002-Comparativa_Frameworks.md` |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/metricas/` | `01-teoria/03-metricas-evaluacion/` |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/teoria/notebook_mitigacion_overfitting.ipynb` | `01-teoria/03-metricas-evaluacion/notebooks/notebook_mitigacion_overfitting.ipynb` |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/teoria/notebook_overfitting_vs_underfitting.ipynb` | `01-teoria/03-metricas-evaluacion/notebooks/notebook_overfitting_vs_underfitting.ipynb` |
| `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/libros/` | `90-archivo/bibliografia-modelado-avanzado/` |

También se eliminó el duplicado `002-Underfit-Overfit_BiasVariance.md` porque era idéntico a `01-teoria/03-metricas-evaluacion/Underfit-Overfit_BiasVariance.md`.

La lista pendiente queda reescrita en:

`04-deep-learning/00-pendientes-revision.md`

## Movimiento `used-cars` — 2026-07-04

Se separó el antiguo bloque `04-deep-learning/03-practicas/modelado-proyectos/used-cars/` porque mezclaba deep learning tabular, AutoML y visión.

| Origen | Destino | Motivo |
|---|---|---|
| `used-cars/notebooks/keras_notebook2.ipynb` | `04-deep-learning/03-practicas/modelado-proyectos/used-cars-dl-tabular/notebooks/` | Regresión tabular con Keras; pertenece a UD4. |
| `used-cars/notebooks/tf_keras_notebook.ipynb` | `04-deep-learning/03-practicas/modelado-proyectos/used-cars-dl-tabular/notebooks/` | Variante Keras con datos grandes; pertenece a UD4 si se conserva como práctica avanzada. |
| `used-cars/notebooks/pytorch_notebook.ipynb` | `04-deep-learning/03-practicas/modelado-proyectos/used-cars-dl-tabular/notebooks/` | Regresión tabular con PyTorch; pendiente de limpieza interna. |
| `used-cars/notebooks/vehiculoPycaret.ipynb` | `03-machine-learning/03-practicas/actividades/automl-used-cars/notebooks/` | AutoML/PyCaret; pertenece a UD3. |
| `used-cars/notebooks/layersReuse.ipynb` | `08-vision-xai/03-practicas/modelado-notebooks-vision-ud4/transfer-learning/` | Transfer learning de visión; pertenece a UD8. |

Los datos locales de `used-cars/data/` y las trazas `used-cars/mlruns/` no están versionados en Git y se mantienen fuera del repositorio docente.
| `used-cars/extras/Samoyedo.jpg` | `08-vision-xai/03-practicas/modelado-notebooks-vision-ud4/transfer-learning/extras/` | Imagen de apoyo para visión/transfer learning; no pertenece al proyecto de coches. |

## Limpieza `boston-housing` — 2026-07-04

| Acción | Motivo |
|---|---|
| Archivado `notebooks/nna-vs-traditional.ipynb` en `04-deep-learning/90-archivo/boston-housing/notebooks-incorrectos/nna-vs-traditional-iris-clasificacion.ipynb` | El contenido usa Iris, regresión logística y árbol de decisión; no corresponde a Boston Housing ni a regresión DL. |
| Añadido `README.md` en `boston-housing/` | Documenta el encaje del proyecto como UD4 DL tabular. |
| Actualizados scripts para cargar `data/housing.csv` con ruta relativa al proyecto | Evita que fallen al ejecutarse desde otro directorio. |
| Versionado explícito de `boston-housing/data/housing.csv` | Dataset pequeño (~49 KB); se conserva para que los scripts sean reproducibles sin descarga externa. |

## Auditoría `boston-housing` — 2026-07-06

Decisión: se mantiene en UD4 como práctica de regresión tabular con redes neuronales, pero queda cerrada sólo como material saneado/documentado. No se considera práctica evaluable canónica hasta corregir la deuda metodológica.

| Comprobación | Resultado | Decisión |
|---|---|---|
| Dataset local | `data/housing.csv` ocupa ~49 KB y contiene 506 filas. | Se versiona por excepción explícita en `.gitignore` para garantizar reproducibilidad. |
| Rutas de scripts | Las cuatro variantes cargan `data/housing.csv` con ruta relativa basada en `Path(__file__)`. | No requiere movimiento ni cambio mecánico de rutas. |
| Notebook residual | `nna-vs-traditional.ipynb` ya estaba archivado por ser Iris/clasificación. | No debe volver al flujo activo de Boston Housing. |
| Metodología | Falta baseline; Keras/PyTorch standalone escalan antes del split; PyTorch reporta métricas sobre datos escalados; SciKeras es la variante más limpia. | Documentar deuda técnica antes de usar en clase; corregir si se convierte en tarea evaluable. |
| Contexto ético | Boston Housing es histórico y contiene variables problemáticas. | README debe advertir que no es dataset moderno ni apto para decisiones reales. |

## Movimiento `house-prices-kaggle` — 2026-07-04

Se retiró de UD4 porque no contiene deep learning real: es una actividad de EDA, pipelines y machine learning tabular.

| Origen | Destino | Motivo |
|---|---|---|
| `house-prices-kaggle/notebooks/house_prices_advanced_regression2.ipynb` | `03-machine-learning/03-practicas/actividades/house-prices-kaggle/notebooks/` | Notebook principal de EDA/pipelines/ML tabular; pertenece a UD3. |
| `house-prices-kaggle/docs/rubrica.md` | `03-machine-learning/03-practicas/actividades/house-prices-kaggle/docs/` | Rúbrica de selección, entrenamiento y evaluación de modelos; encaja en UD3. |
| `house-prices-kaggle/docs/conceptos.org` | `03-machine-learning/03-practicas/actividades/house-prices-kaggle/docs/` | Fuente Org de apoyo estadístico/preprocesado; se conserva, no se elimina. |
| `house-prices-kaggle/notebooks/house_prices_advanced_regresionR.ipynb` | `03-machine-learning/90-archivo/house-prices-kaggle/notebooks/` | Notebook R incompleto y mezclado con datos de cacao; histórico, no activo. |
| `house-prices-kaggle/notebooks/prueba.ipynb` | `03-machine-learning/90-archivo/house-prices-kaggle/notebooks/` | Pruebas básicas de pandas con datos de vino; no pertenece al proyecto activo. |
| `house-prices-kaggle/docs/rubricaSelecEntrenModel.odt` | `03-machine-learning/90-archivo/house-prices-kaggle/docs/` | Versión ODT histórica local, si existía. |

Los datos locales de Kaggle, vino y cacao no se versionan; quedan fuera de Git.
| Datos locales Kaggle `train/test/sample/data_description/zip` | `03-machine-learning/03-practicas/actividades/house-prices-kaggle/data/` | Datos locales no versionados; se colocan junto a la actividad UD3 para que las rutas del notebook tengan sentido. |
| Datos ajenos `wine/cacao` | `03-machine-learning/90-archivo/house-prices-kaggle/data-ajena/` | Datasets no relacionados con House Prices; se conservan sólo como archivo local ignorado. |

## Reubicación material ajeno a `house-prices-kaggle` — 2026-07-04

| Origen previo | Destino | Motivo |
|---|---|---|
| `03-machine-learning/90-archivo/house-prices-kaggle/data-ajena/winemag-data-130k-v2.csv*` | `02-tratamiento-datos/05-recursos/datasets/wine-reviews/` | Dataset propio de análisis de datos/pandas, no de House Prices ni UD3 ML. |
| `03-machine-learning/90-archivo/house-prices-kaggle/data-ajena/flavors_of_cacao.csv` | `02-tratamiento-datos/05-recursos/datasets/cacao-flavors/` | Dataset propio para análisis de datos, no de House Prices. |
| `03-machine-learning/90-archivo/house-prices-kaggle/notebooks/house_prices_advanced_regresionR.ipynb` | `02-tratamiento-datos/90-archivo/alternativas-R/house-prices-r/` | Material R; pertenece a la unidad de tratamiento de datos junto a pandas/EDA, no a ML ni DL. |
| `03-machine-learning/90-archivo/house-prices-kaggle/notebooks/prueba.ipynb` | `02-tratamiento-datos/90-archivo/pandas-wine-reviews/` | Prueba básica de pandas con Wine Reviews; se conserva como semilla histórica, no actividad activa. |

## Pendiente docente transversal — R en UD2 — 2026-07-05

Resuelto el 2026-07-06: R queda como itinerario opcional en `02-tratamiento-datos/03-practicas/r_exercises_titanic_with_tests/`, especialmente para análisis estadístico, visualización y EDA. Se mantiene como complemento sin desplazar el eje principal Python/pandas/scikit-learn.

### 2026-07-05 — Cierre del residuo `modelado-avanzado-docs/`

Se cerró el residuo que quedaba en `01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/`. La carpeta antigua quedó vacía y se eliminó.

| Material | Decisión | Destino |
|---|---|---|
| RNN/LSTM | UD4 conserva sólo una introducción conceptual; el desarrollo largo no queda activo. | `01-teoria/01-fundamentos-redes-neuronales/Parte-II-RedesEspecializadas/RedesRecurrentes_y_LSTM_intro.md` y `90-archivo/modelado-avanzado-docs/redes-recurrentes/` |
| Fuentes `.org` y `.tex` | Conservar como histórico/fuente, fuera del flujo activo. | `90-archivo/modelado-avanzado-docs/fuentes-org-tex/` y `90-archivo/modelado-avanzado-docs/redes-recurrentes/` |
| Apuntes largos de gradiente/backpropagation y Deep Learning V2 | Archivar por solape con fundamentos activos. | `90-archivo/modelado-avanzado-docs/fundamentos/` |
| PDF derivado de gradiente/backpropagation | Archivar como generado, no activo. | `90-archivo/modelado-avanzado-docs/generados/` |
| `GUIA_PROYECTO_PYTHON_ML.md` | Archivar; no corresponde a UD4 base y no se mueve a UD3 en esta pasada. | `90-archivo/modelado-avanzado-docs/guias-proyecto-ml/` |
| `Mas_alla_del_entrenamiento.md` | Archivar porque mezcla transfer learning y RAG; no debe ampliar UD4. | `90-archivo/modelado-avanzado-docs/conceptos/` |
| `notas_housing.txt` | Archivar como nota histórica sin tocar la práctica `boston-housing`. | `90-archivo/modelado-avanzado-docs/boston-housing/` |
| `planTrabajoPytorch.txt` | Separar como nota interna docente. | `90-archivo/modelado-avanzado-docs/notas-internas/` |
| `regularizacion_pack.zip` | Conservar como paquete histórico sin descomprimir. | `90-archivo/modelado-avanzado-docs/tareas/` |
| `002-Underfit-Overfit_BiasVariance.md~` | Eliminar como backup temporal, al existir fuente activa. | Eliminado. |

Con esto, `modelado-avanzado-docs/` deja de ser un pendiente operativo de UD4. Los pendientes restantes de UD4 pasan a proyectos prácticos, recursos y evaluación.

### 2026-07-05 — Reencuadre de `euromillones`

Se revisó `03-practicas/modelado-proyectos/euromillones/` y se decide conservarlo como **actividad crítica**, no como práctica predictiva canónica.

| Elemento | Decisión | Motivo |
|---|---|---|
| Notebooks de Euromillones | Mantener como material histórico/actividad crítica. | Permiten discutir sobreajuste, ausencia de señal y evaluación honesta. |
| Scripts LSTM | Mantener como apoyo técnico no canónico. | Sirven para mostrar arquitectura recurrente y sus límites ante datos sin patrón predictivo real. |
| CSV locales de `data/` | No versionar por defecto. | La regla global `*.csv` los ignora; si se usan, deben distribuirse por Moodle o fuente controlada. |
| README de la carpeta | Crear. | Evita que el alumnado interprete la actividad como promesa de predicción de lotería. |

La carpeta queda dentro de UD4 sólo como refuerzo de conceptos de RNN/LSTM, sobreajuste y validación temporal. No debe evaluarse como “capacidad de acertar resultados”.

### 2026-07-05 — Saneamiento documental de `used-cars-dl-tabular`

Se auditó `04-deep-learning/03-practicas/modelado-proyectos/used-cars-dl-tabular/` sin ejecutar notebooks pesados.

| Elemento | Decisión | Motivo |
|---|---|---|
| `keras_notebook2.ipynb` | Mantener en UD4. | Es regresión tabular de precio de coches usados con Keras. Requiere advertir que las métricas deben ser de regresión, no `accuracy`. |
| `tf_keras_notebook.ipynb` | Mantener como variante avanzada/incompleta. | Trabaja datos grandes con PyArrow/Vaex/Parquet y Keras, pero mezcla dependencias y conserva un bloque DEAP incompleto. |
| `pytorch_notebook.ipynb` | Mantener sólo como pendiente de refactor. | Aunque importa PyTorch, el flujo principal conserva código Keras; no debe presentarse como práctica PyTorch cerrada. |
| `README.md` | Reescrito como guía docente y de límites. | Deja explícitos objetivo, datos no versionados, notebooks incluidos, baseline, leakage, métricas, reproducibilidad y qué no versionar. |

Decisión docente: el bloque pertenece a UD4 como regresión tabular con redes neuronales, pero se considera saneado **documentalmente**, no reejecutado ni refactorizado a nivel de notebook.
