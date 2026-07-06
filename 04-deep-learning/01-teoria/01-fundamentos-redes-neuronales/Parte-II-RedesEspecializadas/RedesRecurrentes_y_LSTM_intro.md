# Redes recurrentes y LSTM en UD4

Este documento deja una introducción conceptual mínima a las redes recurrentes dentro de UD4. El objetivo no es desarrollar una práctica aplicada completa, sino situar la idea de memoria y procesamiento de secuencias antes de continuar en otras unidades.

## Qué debe quedar claro en UD4

- Una red recurrente procesa datos secuenciales manteniendo un estado interno.
- Las RNN simples pueden sufrir problemas de gradiente y memoria a corto plazo.
- LSTM y GRU son variantes pensadas para conservar información durante más pasos temporales.
- El encaje natural de las RNN depende del problema: texto, series temporales, señales o secuencias generales.

## Frontera docente

| Tema | Tratamiento en UD4 | Continuidad |
|---|---|---|
| RNN simple | Introducción conceptual. | Prácticas específicas fuera de UD4. |
| LSTM/GRU | Motivación y lectura orientativa. | Series temporales en UD10. |
| Secuencias de texto | Sólo como ejemplo de uso. | NLP, transformers y LLM en UD6. |
| Predicción temporal | Sólo como motivación. | Modelado de series temporales en UD10. |

## Material histórico conservado

El desarrollo largo anterior se conserva fuera del flujo activo en:

- `04-deep-learning/90-archivo/modelado-avanzado-docs/redes-recurrentes/RedesRecurrentes.md`
- `04-deep-learning/90-archivo/modelado-avanzado-docs/redes-recurrentes/LSTM.org`
- `04-deep-learning/90-archivo/modelado-avanzado-docs/redes-recurrentes/LSTM.tex`

Para clase, usar esta introducción como puente. Si se necesita práctica aplicada, continuar en UD6 o UD10 en lugar de ampliar UD4.
