# 03 · Laboratorios

Laboratorios evaluables de la UD4. Cada laboratorio incluye enunciado, rúbrica y plantilla de entrega.

## Antes de empezar

- Sigue los laboratorios en orden.
- TensorFlow Playground se abre en el navegador y no necesita entorno local.
- Para la implementación PyTorch del Laboratorio 3, ejecuta desde la raíz `pixi run --environment ud4 jupyter lab`.
- Usa Keras u otra receta especializada sólo si la actividad o el profesorado lo indican; las plantillas de `05-recursos/modelado-entornos/` son referencias contextuales, no alternativas por defecto.
- Todas las entregas se rigen por las [normas comunes de entrega y uso de IA](../../../docs/normas-entregas-y-uso-de-ia.md).

---

## Laboratorios

### [Laboratorio 1 — TF Playground](Laboratorio1/)

Exploración visual de redes neuronales con [TensorFlow Playground](https://playground.tensorflow.org/).

| Archivo | Descripción |
|---|---|
| `TensorFlowPlayGround.pdf` | Enunciado completo |
| `TensorFlowPlayGround_Entrega.md` | Plantilla de entrega |
| `TensorFlowPlayGround-Rubrica.md` | Rúbrica de evaluación |
| `tf-playground-datasets.ipynb` | Notebook con datasets de apoyo |
| `TensorFlowPlayGround.org/.tex` | Fuentes del enunciado |
| `TensorFlowPlayGround-V1.org` | Versión anterior (referencia) |

**Relacionado con:** [fundamentos de redes neuronales](../../01-teoria/01-fundamentos-redes-neuronales/Parte-I-Fundamentos/UD4-DeepLearning-Indice-Parte1-Teoria.md).

---

### [Laboratorio 2 — Backpropagation desde cero](Laboratorio2/)

Implementación manual del algoritmo de backpropagation en Python puro, sin frameworks.

| Archivo | Descripción |
|---|---|
| `EstudioImplementacionBackpropagation.pdf` | Enunciado completo |
| `EstudioImplementacionBackpropagation-Entrega.md` | Plantilla de entrega |
| `EstudioImplementacionBackpropagation-Rubrica.md` | Rúbrica de evaluación |
| `backpropagationRNAscratch.py` | Script de referencia (RNA desde cero) |
| `backPropScratch.py` | Variante simplificada |

**Relacionado con:** [`UD4_Capitulo_08_Backpropagation.md`](../../01-teoria/01-fundamentos-redes-neuronales/Parte-I-Fundamentos/UD4_Capitulo_08_Backpropagation.md) y scripts en [`fundamentos-scripts/`](../../02-ejemplos/fundamentos-scripts/).

---

### [Laboratorio 3 — De Playground a código real](Laboratorio3/)

Transición de la experimentación visual en TF Playground a implementación real con un framework.

| Archivo | Descripción |
|---|---|
| `DePlayground_a_CodigoReal.pdf` | Enunciado completo |
| `DePlayground_a_CodigoReal-Entrega.md` | Plantilla de entrega |
| `DePlayground_a_CodigoReal-Rubrica.md` | Rúbrica de evaluación |

**Relacionado con:** [`frameworks/`](../../02-ejemplos/frameworks/) — implementación con Keras/PyTorch.

---

## Progresión

Los laboratorios siguen el orden del módulo:

```
Lab 1 (exploración visual)  →  Lab 2 (matemática manual)  →  Lab 3 (código real)
```
