# UD9 — GPU Avanzado

## Propósito

Programación GPU de alto rendimiento con RAPIDS (cuDF, cuML) y JAX. Orquestación de flujos con Prefect. Proyecto integrador con pipeline completo, dashboard y benchmark CPU/GPU.

**Resultados de Aprendizaje**: RA2 (b, d, e) · RA3 (a, b)

---

## Requisito de ejecución

Las evidencias evaluables de cuDF, cuML y benchmarking GPU deben ejecutarse en una **GPU NVIDIA**. Si no dispones de una local, usa como ruta canónica un cuaderno de **Google Colab con runtime GPU** o el runtime cloud equivalente que indique el profesorado.

La ejecución en CPU sirve para preparar, depurar y completar las partes no aceleradas, pero **no sustituye** la evidencia GPU ni permite acreditar un benchmark CPU/GPU.

Antes de empezar, completa el [preflight de la práctica](03-practicas/README.md#preflight-obligatorio-del-runtime). Después consulta el [enunciado del proyecto](03-practicas/00-guia-proyecto-gpu.md) y los [instrumentos de evaluación](04-evaluacion/README.md).

---

## Estructura

```
01-teoria/          Guías conceptuales (RAPIDS, JAX, benchmarking)
02-ejemplos/        Notebooks demostrativos con base + soluciones + autotests
03-practicas/       Proyecto integrador: EDA GPU → dashboard → pipeline
04-evaluacion/      Rúbrica, checklist y cuestionario GIFT
05-recursos/        Plantillas de presentación, informe y autoevaluación
90-archivo/         Material histórico (neurosimbólica, cuDF antiguo)
99-profesor/        Soluciones de las prácticas (no publicar al alumnado)
```

---

## Teoría (01-teoria)

| Archivo | Contenido |
|---------|-----------|
| `00-guia-rapids-jax.md` | Índice general y actividades de la unidad |
| `01-rapids-cudf-cuml.md` | RAPIDS: cuDF DataFrames en GPU, cuML algoritmos ML |
| `02-jax-programacion-gpu.md` | JAX: jit, grad, vmap — programación funcional GPU |
| `03-benchmarks-optimizacion-gpu.md` | Medir y optimizar rendimiento GPU vs CPU |

---

## Ejemplos (02-ejemplos)

Todos los notebooks tienen tres versiones: base (alumno), `_SOLUCIONES` y `_SOLUCIONES_TESTS`.

| Notebook | Tema |
|----------|------|
| `01_rapids_intro` | cuDF y cuML: DataFrames y modelos en GPU |
| `02_jax_intro` | JAX: arrays, grad y jit |
| `03_gpu_benchmarks` | Benchmarks comparativos NumPy / JAX / cuDF |
| `04_virtual_agent_intro` | Introducción a agentes con LangChain |
| `05_prefect_intro` | Orquestación de flujos con Prefect |
| `06_agent_api` | APIs de agentes IA |

---

## Prácticas (03-practicas)

Proyecto integrador en tres partes. Ver [`03-practicas/README.md`](03-practicas/README.md) para los enunciados completos.

| Notebook | Práctica |
|----------|----------|
| `01_project_template.ipynb` | EDA + modelado acelerado en GPU + benchmark |
| `02_dashboard_template.ipynb` | Dashboard interactivo con Gradio |
| `03_pipeline_template.ipynb` | Pipeline reproducible con Prefect |

---

## Evaluación (04-evaluacion)

| Instrumento | Descripción |
|-------------|-------------|
| `rubrica.md` | 5 criterios, 10 puntos (aceleración GPU, pipeline, dashboard, artefactos, documentación) |
| `checklist-entrega.md` | Lista de verificación antes de la entrega |
| `cuestionario_rapids_jax.gift` | Cuestionario Moodle: conceptos RAPIDS, JAX y GPU |

---

## Recursos (05-recursos)

| Archivo | Uso |
|---------|-----|
| `00-guia-presentacion-final.md` | Guía para la presentación y evaluación final |
| `plantilla-informe.md` | Estructura del informe técnico del proyecto |
| `plantilla-presentacion.md` | Esquema para las diapositivas de presentación |
| `plantilla-autoevaluacion.md` | Autoevaluación individual obligatoria |

---

## Mejora opcional

- [ ] Valorar si mover `90-archivo/NN-neurosimbólica/` a `11-anexos/` (material histórico sin uso activo).
