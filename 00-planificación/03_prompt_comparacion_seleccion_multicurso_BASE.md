# Prompt 3 — Comparación y selección multi-curso antes de reorganizar

## Objetivo

Comparar varias versiones históricas del material docente de un mismo módulo para construir una **propuesta de unidad ideal** antes de reorganizar.

Este prompt está pensado especialmente para casos en los que el curso actual no parece ser la mejor base y existen materiales de cursos anteriores más redondos, completos o coherentes.

No reorganices archivos todavía. Primero debes analizar, comparar y proponer qué conservar, combinar, descartar o rehacer.

## Contexto del módulo

Módulo: **[NOMBRE_DEL_MÓDULO]**

Código corto: **[CÓDIGO]**

Versiones a comparar:

1. Curso actual: `[RUTA_CURSO_ACTUAL]`
2. Curso anterior: `[RUTA_CURSO_ANTERIOR]`
3. Curso anterior adicional, si existe: `[RUTA_CURSO_ANTERIOR_2]`

Inventarios disponibles:

1. Inventario curso actual: `[INVENTARIO_CURSO_ACTUAL.md]`
2. Inventario curso anterior: `[INVENTARIO_CURSO_ANTERIOR.md]`
3. Inventario curso anterior adicional: `[INVENTARIO_CURSO_ANTERIOR_2.md]`

Si no existe inventario separado para cada curso, primero debe generarse con los prompts `00`, `01` y `02` para cada versión que se vaya a comparar.

## Rol del modelo

Actúa como arquitecto docente, revisor curricular y editor de materiales didácticos.

Tu tarea no es elegir lo más moderno ni lo más extenso automáticamente. Debes elegir lo que mejor funcione para enseñar y evaluar el módulo.

Valora especialmente:

- Coherencia didáctica.
- Secuencia de aprendizaje.
- Correspondencia con resultados de aprendizaje y criterios de evaluación.
- Claridad para el alumnado.
- Viabilidad real en aula.
- Actualidad tecnológica.
- Calidad de prácticas, ejemplos, rúbricas y guías.
- Reutilización razonable de material previo sin arrastrar deuda o duplicados.

## Entradas que debes usar

Usa como entrada principal:

1. Los inventarios consolidados de cada versión del módulo.
2. El prompt base de inventario usado para definir exclusiones y criterios.
3. Cualquier documento de planificación curricular disponible.
4. La estructura de unidades prevista para el próximo curso, si ya existe.

No inventes archivos ni materiales que no aparezcan en los inventarios o en el árbol real.

## Método de comparación

Compara el material por unidad o bloque equivalente.

Para cada unidad:

1. Identifica qué versiones existen en cada curso.
2. Resume el enfoque de cada versión.
3. Señala fortalezas y debilidades.
4. Detecta solapamientos, duplicados y contradicciones.
5. Propón una versión base recomendada.
6. Indica qué piezas deben rescatarse de otros años.
7. Marca qué material debe archivarse, descartarse o quedar como ampliación.
8. Señala huecos que haya que crear desde cero o actualizar.

## Criterios de decisión

Prioriza una pieza de material cuando:

- Está mejor secuenciada.
- Tiene instrucciones más claras.
- Tiene mejor conexión con evaluación.
- Usa herramientas viables para el aula.
- Evita dependencia excesiva de servicios frágiles, caros o difíciles de reproducir.
- Puede actualizarse con cambios menores.
- Encaja mejor con la unidad ideal propuesta.

No priorices una pieza solo porque:

- Es más reciente.
- Tiene más páginas.
- Usa una tecnología más llamativa.
- Está más maquetada pero enseña peor.
- Ya está en el curso actual.

## Formato de salida

Genera un fichero Markdown llamado preferentemente:

`comparativa_multicurso_[codigo_modulo].md`

Debe seguir esta estructura:

```md
# Comparativa multi-curso del módulo: [NOMBRE_DEL_MÓDULO]

## 1. Resumen ejecutivo

- Diagnóstico general del curso actual.
- Qué curso o versión parece más sólido como base.
- Riesgos principales si se reorganiza solo el curso actual.
- Criterio recomendado para construir el nuevo material.

## 2. Mapa de versiones comparadas

| Versión | Ruta | Estado general | Observaciones |
| ------- | ---- | -------------- | ------------- |

## 3. Comparativa por unidad

### Unidad [N] — [Nombre]

| Curso/versión | Material relevante | Fortalezas | Debilidades | Decisión recomendada |
| ------------- | ------------------ | ---------- | ----------- | -------------------- |

**Base recomendada:** [curso/ruta]

**Piezas a rescatar de otros años:**

- [ruta] — [motivo]

**Material a archivar o descartar:**

- [ruta] — [motivo]

**Huecos o mejoras necesarias:**

- [mejora]

## 4. Propuesta de unidades ideales

| Unidad ideal | Base principal | Piezas complementarias | Material a crear/actualizar | Riesgo |
| ------------ | -------------- | ---------------------- | --------------------------- | ------ |

## 5. Recomendaciones para el prompt de reorganización

Indica cómo debe adaptarse el prompt de reorganización:

- Estructura final recomendada.
- Unidades definitivas.
- Material que debe copiarse como ruta principal.
- Material que debe ir a ampliación.
- Material que debe ir a archivo.
- Material docente interno que debe quedar fuera de publicación.

## 6. Pendientes antes de reorganizar

- [pendiente]
```

## Reglas de seguridad

- No modifiques archivos originales.
- No muevas archivos originales.
- No borres archivos originales.
- No copies entregas de alumnado ni artefactos privados de corrección.
- Si hay duda entre conservar o descartar, conserva como `pendiente_revision` o `90-archivo`, pero explícitalo.

## Resultado esperado

El resultado de este prompt debe permitir adaptar el prompt `04_prompt_reorganizacion_materia_BASE_DESDE_PIA.md` al módulo concreto.

La reorganización solo debe ejecutarse después de tener clara la propuesta de unidades ideales.
