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
| `01-fundamentos-python/90-archivo/NumPy-20251016.zip` | ZIP histórico | 7,9 MB | Revisar para reutilizar | Puede contener material de NumPy útil para UD1, pero está archivado y comprimido. | Inspeccionar contenido antes de decidir si se extrae algo hacia `01-fundamentos-python/05-recursos/` o se conserva solo como histórico. |
| `06-llm-agentes/90-archivo/MCP-24-25/` | Material MCP histórico | 20 KB | Conservar como histórico | MCP ya está integrado en UD6 mediante prácticas, documentación y evaluación; no hace falta otro bloque obligatorio. | Mantener en archivo. Revisar solo si el refuerzo MCP necesita ampliación. |
| `06-llm-agentes/05-recursos/mcp-refuerzo/` | Refuerzo opcional | Pendiente | Mantener como refuerzo opcional | Complementa MCP sin sobrecargar UD6. | Usar solo si el test inicial detecta carencias. |
| `11-anexos/90-archivo/actividades-rl/` | Actividades RL archivadas | 56 KB | Revisar para reutilizar | Incluye notebooks de alumno/profesor y ZIPs; puede encajar como anexo o ampliación, pero no debe publicarse sin separar soluciones. | Separar material de alumnado/profesor y decidir si pasa a recurso activo en anexos. |
| `11-anexos/90-archivo/snake_rl_materiales.zip` | ZIP RL | Parte de 200 KB | Revisar para reutilizar | Posible material práctico de aprendizaje por refuerzo. | Comparar con el resto de ZIPs Snake RL y conservar una única versión canónica. |
| `11-anexos/90-archivo/snake_rl_materiales_completo.zip` | ZIP RL | Parte de 200 KB | Revisar para reutilizar | Parece variante completa; puede duplicar otros ZIPs. | Comparar contenido y decidir si sustituye a versiones parciales. |
| `11-anexos/90-archivo/snake-rl-github.zip` | ZIP RL | Parte de 200 KB | Revisar para reutilizar | Posible copia de repositorio externo o snapshot. | Comprobar licencia/origen y si aporta algo frente a versiones propias. |
| `11-anexos/90-archivo/snake_rl_completo_final.zip` | ZIP RL | Parte de 200 KB | Revisar para reutilizar | Nombre sugiere versión final, pero hay varias variantes. | Comparar con `snake_rl_completo_con_env.zip` y `snake_rl_materiales_actualizado.zip`. |
| `11-anexos/90-archivo/snake_rl_completo_con_env.zip` | ZIP RL | Parte de 200 KB | Revisar para reutilizar | Puede incluir entorno; útil si se conserva como práctica reproducible. | Verificar dependencias y decidir si se publica o se documenta como histórico. |
| `11-anexos/90-archivo/snake_rl_materiales_actualizado.zip` | ZIP RL | Parte de 200 KB | Revisar para reutilizar | Nombre sugiere versión más reciente. | Candidato a versión canónica si no contiene soluciones o material sensible. |
| `11-anexos/90-archivo/snake-rl-github-actualizado.zip` | ZIP RL | Parte de 200 KB | Revisar para reutilizar | Posible snapshot actualizado externo. | Comprobar licencia/origen y duplicidad. |
| `90-archivo-historico/convergencia-anterior/` | Archivo histórico amplio | 75 MB | Conservar como histórico | Volumen alto y ubicación histórica; no debe entrar en publicación ni revisión fina sin objetivo concreto. | Revisar solo si se busca recuperar material concreto de convergencia. |
| `02-tratamiento-datos/90-archivo/NLP_old/` | NLP antiguo | 36 KB | Conservar como histórico | NLP encaja mejor en UD6/LLM o como archivo; incluye soluciones/tests y no debe publicarse tal cual. | Revisar solo si se necesita una actividad clásica de NLP previa a LLM. |
| `02-tratamiento-datos/90-archivo/alternativas-R/` | Alternativas en R | 1,1 MB | Conservar como histórico | El eje actual parece Python/pandas; R puede distraer si se activa sin una decisión curricular explícita. | Mantener archivado salvo que se cree un recurso comparativo Python/R. |
| `03-machine-learning/90-archivo/office/` | PDFs/DOCX antiguos | 972 KB | Revisar para reutilizar | Puede contener guías útiles de EDA/datasets/ML, pero está en formatos menos mantenibles. | Extraer solo ideas vigentes hacia Markdown si aportan valor único. |
| `03-machine-learning/90-archivo/teoria-html/` | HTML teórico antiguo | 13 MB | Revisar para reutilizar | Puede contener teoría de ML/Scikit/CuML, pero en HTML generado y con posible duplicidad. | Comparar con teoría activa de UD3 antes de mover nada. |
| `04-deep-learning/90-archivo/fundamentos-old/` | Fundamentos DL antiguos | 3,9 MB | Revisar para reutilizar | Puede aportar base de gradiente/backprop, pero puede duplicar contenido activo. | Revisar si UD4 necesita una explicación base más clara; si no, conservar histórico. |
| `09-gpu-avanzado/90-archivo/sem25-old/` | Semana antigua GPU/datos | 44 KB | Revisar para reutilizar | Incluye Polars/cuDF y soluciones/tests; puede ser útil para GPU avanzado, pero requiere separación docente/alumnado. | Separar versiones alumno/profesor antes de cualquier publicación. |
| `09-gpu-avanzado/90-archivo/sem25-neurosimbólica/` | Material neurosimbólico | 652 KB | Conservar como histórico | Tema lateral para GPU avanzado; no parece núcleo de la unidad. | Revisar solo si se decide crear una ampliación de IA neurosimbólica. |

## Próxima acción recomendada

Revisar primero el lote de menor riesgo y mayor impacto:

1. `11-anexos/90-archivo/*.zip`: elegir una versión canónica de Snake RL o dejar todo como histórico.
2. `01-fundamentos-python/90-archivo/NumPy-20251016.zip`: decidir si contiene recursos útiles para UD1.
3. `03-machine-learning/90-archivo/office/`: extraer solo ideas vigentes, nunca publicar DOCX/PDF antiguos sin revisión.
