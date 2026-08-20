# Radar de avances en IA para adaptar el curso

Este documento es **interno de planificación docente**. No forma parte del temario publicado ni debe enlazarse desde materiales del alumnado.

Su objetivo es revisar, cada dos o tres semanas, si han aparecido cambios relevantes en IA que convenga mencionar, incorporar o dejar preparados antes de empezar una unidad.

## Uso rápido

1. Revisar novedades relevantes cada 2-3 semanas.
2. Anotar sólo avances con impacto docente posible.
3. Decidir una acción concreta: ignorar, mencionar, adaptar o sustituir.
4. Antes de empezar cada unidad, comprobar si hay entradas que afecten a esa unidad.

## Criterios de decisión

| Acción | Cuándo usarla | Resultado esperado |
|---|---|---|
| Ignorar | Novedad llamativa pero sin utilidad clara para RA/CE, prácticas o proyectos. | No se toca el material. |
| Mencionar | Avance útil como contexto, pero no necesario para trabajar. | Comentario breve en clase o recurso opcional. |
| Adaptar práctica | Mejora una práctica existente sin cambiar el objetivo de aprendizaje. | Ajuste menor de notebook, herramienta, dataset o API. |
| Sustituir herramienta | La herramienta anterior queda obsoleta, inaccesible o claramente peor. | Cambio documentado antes de usar la unidad. |
| Crear ampliación | Encaja bien como reto, refuerzo o demostración, pero no debe cargar el núcleo. | Recurso opcional o actividad de extensión. |

## Radar vivo

| Fecha | Avance observado | Fuente / referencia | Unidades afectadas | Impacto docente | Acción | Revisión |
|---|---|---|---|---|---|---|
| 2026-07-03 | Crear este radar interno de avances en IA. | Decisión docente interna. | Todas | Evitar que el temario se quede rígido y facilitar ajustes periódicos. | Crear mecanismo de revisión. | Revisar antes del inicio de curso. |
| 2026-07-04 | Señal reciente en modelos de espacio de estados: Mamba/SSM siguen apareciendo como alternativa eficiente para secuencias largas, pero no sustituyen todavía de forma general a Transformers en docencia básica. | `Mamba-3: Improved Sequence Modeling using State Space Principles` (arXiv, 2026-03-16); `Harmonic: Hierarchical State Space Models for Efficient Long-Context Language Modeling` (arXiv, 2026-05-30); `Scaling State-Space Models from Lines to Paragraphs: An Ablation of Mamba-based OCR` (arXiv, 2026-06-22). | UD4, UD6, UD8, UD10 | Buen tema para explicar límites de Transformers, coste de atención y alternativas lineales/recurrentes. En OCR largo hay ventaja de velocidad, pero peor resultado en escritura manuscrita frente a Transformer: sirve para enseñar tradeoffs, no hype. | Mencionar / crear ampliación opcional. | Revisar antes de UD4 y UD6. |
| 2026-07-04 | Modelos híbridos Mamba-Transformer y arquitecturas eficientes siguen ganando tracción para inferencia larga y razonamiento, especialmente en modelos abiertos o de despliegue eficiente. | `NVIDIA Nemotron Nano 2: An Accurate and Efficient Hybrid Mamba-Transformer Reasoning Model` (arXiv, 2025-08-20); `DUET: Disaggregated Hybrid Mamba-Transformer LLMs...` (arXiv, 2026-03-16). | UD6, UD9, UD12 | Interesa para hablar de serving, coste de inferencia, throughput, memoria y por qué la arquitectura importa además del tamaño del modelo. | Mencionar / adaptar práctica si hay modelo accesible localmente. | Revisar antes de UD6 y UD9. |
| 2026-07-04 | Liquid Foundation Models siguen siendo una línea interesante, sobre todo para modelos compactos, edge/on-device y dominios científicos; no parece todavía un sustituto directo del bloque base de LLMs del curso. | `LFM2 Technical Report` (arXiv, 2025-11-28); `MMAI Gym for Science: Training Liquid Foundation Models for Drug Discovery` (arXiv, 2026-03-03). | UD4, UD6, UD12 | Útil como caso de estudio: arquitecturas híbridas/eficientes, modelos pequeños especializados y despliegue en local. Conviene no convertirlo en contenido obligatorio salvo que haya herramienta estable y fácil de usar. | Mencionar / crear ampliación opcional. | Revisar antes del inicio de curso. |

## Revisión antes de empezar una unidad

Antes de iniciar cada unidad, comprobar:

- [ ] ¿Ha cambiado alguna herramienta central de la unidad?
- [ ] ¿Hay modelos, APIs o librerías nuevas que simplifiquen una práctica?
- [ ] ¿Alguna dependencia se ha vuelto de pago, inestable o difícil de usar?
- [ ] ¿Conviene cambiar un ejemplo por otro más actual sin tocar RA/CE?
- [ ] ¿La evaluación sigue midiendo el proceso, la verificación y la comprensión?
- [ ] ¿Hace falta avisar al alumnado de límites en el uso de IA para esta unidad?

## Registro de ajustes realizados

| Fecha | Unidad | Cambio realizado | Motivo | Verificación |
|---|---|---|---|---|
| 2026-07-03 | Todas | Se crea el radar interno de avances. | Mantener el curso como currículo vivo sin modificar continuamente el temario publicado. | Documento creado en `00-planificación/`. |
| 2026-07-04 | UD4, UD6, UD9, UD12 | Añadidas entradas sobre Mamba/SSM, modelos híbridos Mamba-Transformer y Liquid Foundation Models. | Vigilar alternativas no puramente Transformer y su posible impacto en long-context, inferencia eficiente, edge y proyectos. | Búsqueda web con fuentes arXiv y referencias técnicas recientes. |

## Regla práctica

No actualizar por ansiedad ni por moda. Actualizar cuando el cambio ayude a enseñar mejor, evaluar mejor o evitar que el alumnado trabaje con herramientas claramente desfasadas.
