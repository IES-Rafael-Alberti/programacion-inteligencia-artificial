# Decisiones sobre material archivado

Este documento convierte el pendiente genérico de “revisar legacy” en decisiones por ruta concreta. No implica mover ni borrar nada todavía: primero se decide, después se actúa.

## Criterio de decisión

| Decisión | Significado |
|---|---|
| Conservar como histórico | Se mantiene fuera del flujo docente activo. |
| Revisar para reutilizar | Puede aportar valor, pero requiere revisión antes de moverlo a una unidad activa. |
| Mantener como refuerzo opcional | No es contenido obligatorio; se usa solo si el diagnóstico del grupo lo justifica. |
| Descartar tras copia segura | Candidato a eliminación futura, siempre después de confirmar que no aporta contenido único. |

## Tabla de decisión

| Ruta | Tipo | Tamaño aprox. | Decisión | Motivo | Acción futura |
|---|---:|---:|---|---|---|
| `01-fundamentos-python/90-archivo/NumPy-20251016.zip` | ZIP histórico | 7,9 MB | Conservar como histórico | El material activo de UD1 ya cubre NumPy sobradamente. El EPUB dentro del ZIP puede servir como referencia futura en una revisión global de libros de apoyo. | Conservar en archivo. Revisar el EPUB solo si se hace una pasada unificada de libros/material de referencia externo. |
| `06-llm-agentes/90-archivo/MCP-24-25/` | Material MCP histórico | 20 KB | Conservar como histórico | MCP ya está integrado en UD6 mediante prácticas, documentación y evaluación; no hace falta otro bloque obligatorio. | Mantener en archivo. Revisar solo si el refuerzo MCP necesita ampliación. |
| `06-llm-agentes/05-recursos/mcp-refuerzo/` | Refuerzo opcional | Pendiente | Mantener como refuerzo opcional | Complementa MCP sin sobrecargar UD6. | Usar solo si el test inicial detecta carencias. |
| `11-anexos/90-archivo/actividades-rl/` | Actividades RL archivadas (Catch the Fruit) | 56 KB | Mantener como refuerzo opcional | Actividad RL completa y autocontenida: entorno personalizado, Q-Table + DQN, separación alumno/profesor, guía con rúbrica. Ya referenciada desde `11-anexos/README.md`. | Usar como actividad complementaria de RL si se necesita. No requiere integración en unidades obligatorias. |
| `11-anexos/90-archivo/snake_rl_materiales_actualizado.zip` | ZIP RL (notebooks + PDFs) | ~50 KB | **Versión canónica (contenido)** | Contiene los notebooks reales (Q-Table y DQN) y PDFs. Versión actualizada con sección de evaluación añadida. | Conservar como base para crear un único paquete unificado con `snake_rl_completo_con_env.zip`. |
| `11-anexos/90-archivo/snake_rl_completo_con_env.zip` | ZIP RL (entorno + scaffolds) | ~7 KB | **Versión canónica (entorno)** | Contiene `snake_env.py`, requirements, environment.yml y README. Necesario para ejecutar los notebooks. | Conservar como base para unificar con `snake_rl_materiales_actualizado.zip`. |
| `11-anexos/90-archivo/snake_rl_materiales.zip` | ZIP RL | ~55 KB | Conservar como histórico | Versión anterior de los notebooks, sin sección de evaluación. Superseded por `materiales_actualizado`. | Mantener en archivo. |
| `11-anexos/90-archivo/snake_rl_materiales_completo.zip` | ZIP RL (solo README) | ~1,5 KB | Conservar como histórico | Solo contiene un README.txt descriptivo; incompleto como paquete. | Mantener en archivo. |
| `11-anexos/90-archivo/snake_rl_completo_final.zip` | ZIP RL (scaffolds sin env) | ~3 KB | Conservar como histórico | Versión previa sin `snake_env.py`. Superseded por `completo_con_env`. | Mantener en archivo. |
| `11-anexos/90-archivo/snake-rl-github.zip` | ZIP RL (plantilla vacía) | ~1 KB | Conservar como histórico | Estructura GitHub con notebooks vacíos (stubs de 65 B). Posible plantilla para alumnos. | Mantener en archivo por si se recupera como esqueleto de ejercicios. |
| `11-anexos/90-archivo/snake-rl-github-actualizado.zip` | ZIP RL (plantilla vacía) | ~4 KB | Conservar como histórico | Misma estructura que github.zip con README mejorado. Notebooks igualmente vacíos. | Mantener en archivo por si se recupera como esqueleto de ejercicios. |
| `90-archivo-historico/convergencia-anterior/` | Archivo histórico amplio | 75 MB | Conservar como histórico | Volumen alto y ubicación histórica; no debe entrar en publicación ni revisión fina sin objetivo concreto. | Revisar solo si se busca recuperar material concreto de convergencia. |
| `02-tratamiento-datos/90-archivo/NLP_old/` | NLP antiguo | 36 KB | Conservar como histórico | NLP encaja mejor en UD6/LLM o como archivo; incluye soluciones/tests y no debe publicarse tal cual. | Revisar solo si se necesita una actividad clásica de NLP previa a LLM. |
| `02-tratamiento-datos/90-archivo/alternativas-R/` | Alternativas en R | 1,1 MB | Conservar como histórico | El eje actual parece Python/pandas; R puede distraer si se activa sin una decisión curricular explícita. | Mantener archivado salvo que se cree un recurso comparativo Python/R. |
| `03-machine-learning/90-archivo/office/` | PDFs/DOCX antiguos | 972 KB | Conservar como histórico | Todo el contenido ya fue extraído a Markdown activo (teoría caps 00-04, guía datasets, EDA Titanic/Ames, data prep). Los Org mode son placeholders. | Mantener en archivo como originales fuente. No requiere extracción adicional. |
| `03-machine-learning/90-archivo/teoria-html/` | HTML teórico antiguo | 13 MB | **Descartar** | Exportaciones HTML del mismo contenido ya en Markdown en `01-teoria/`. Si los `.md` se modifican, los HTML quedan desactualizados y confunden. | Eliminar los HTML. El contenido canónico está en `01-teoria/`. |
| `04-deep-learning/90-archivo/fundamentos-old/` | Fundamentos DL antiguos | 3,9 MB | Mixto — ver detalle | El `.md` es borrador previo del activo (mismo contenido, peor formateado). El `.org` es fuente única de intro a RNA sin homólogo directo. `Codigo/` tiene scripts únicos y duplicados. | **Descartar:** `001-GradDesc-Backprop-Optim.md/.pdf`, `IntroModeladoRNA.pdf/.tex`, `Codigo/backpropagationRNAscratch.py`, `Codigo/backPropScratch.py` (duplicados). **Conservar como histórico:** `IntroModeladoRNA.org`. **Conservar como complemento:** resto de `Codigo/` (scripts únicos). |
| `09-gpu-avanzado/90-archivo/sem25-old/` | Semana antigua GPU/datos | 44 KB | Mixto — ver detalle | Polars ya cubierto en UD2 (nada que mover). cuDF absorbido en Semana26 activa. Comparativa útil como complemento histórico. Semana25_Guia reemplazada por Semana26. | **Descartar:** `87_polars_intro*`, `Semana25_Guia.md`. **Conservar como histórico:** `88_cudf_intro.ipynb`, `89_pandas_comparison.ipynb`. **Unificar soluciones:** eliminar `*_SOLUCIONES.ipynb`, conservar solo `*_SOLUCIONES_TESTS.ipynb`. |
| `09-gpu-avanzado/90-archivo/sem25-neurosimbólica/` | Material neurosimbólico | 652 KB | Conservar como histórico | Tema lateral para GPU avanzado; no parece núcleo de la unidad. | Revisar solo si se decide crear una ampliación de IA neurosimbólica. |

## Próxima acción recomendada

Lotes ya resueltos:

1. ✅ `01-fundamentos-python/90-archivo/NumPy-20251016.zip` → Conservar como histórico
2. ✅ `11-anexos/90-archivo/snake-rl-*` → Canónica: `materiales_actualizado` + `completo_con_env`; resto histórico
3. ✅ `03-machine-learning/90-archivo/office/` → Conservar como histórico (todo ya extraído a Markdown)

Siguientes lotes pendientes (aún "Revisar para reutilizar"):

4. ✅ `11-anexos/90-archivo/actividades-rl/` → Mantener como refuerzo opcional; referenciado desde `11-anexos/README.md`

Siguientes lotes pendientes:

5. ✅ `03-machine-learning/90-archivo/teoria-html/` → Descartar (HTML desactualizados, contenido ya en Markdown)

Siguientes lotes pendientes:

6. ✅ `04-deep-learning/90-archivo/fundamentos-old/` — Mixto (descartar duplicados, conservar `.org` y scripts únicos)

7. ✅ `09-gpu-avanzado/90-archivo/sem25-old/` — Mixto (descartar Polars y guía; histórico cuDF y comparativa; unificar soluciones)

---

✅ **Todos los lotes de material archivado revisados.** Pendiente: ejecutar las acciones de limpieza (descartar, unificar, eliminar) en una pasada final.
