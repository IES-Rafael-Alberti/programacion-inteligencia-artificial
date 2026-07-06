# Seguimiento del curso PIA 2026-2027

Este documento acompaña al libro `SEGUIMIENTO_CURSO_PIA.xlsx` y define su uso operativo durante el curso.

## Idea clave

La actividad o práctica es el contenedor de evidencias. La calificación oficial debe poder registrarse por criterio de evaluación (CE) asociado al RA correspondiente.

Por eso, la hoja principal para evaluación es **Registro_CE**, no `Registro_Notas`.

## Hojas incluidas

- **Imparticion**: seguimiento de partes impartidas por unidad, bloque, fecha, grupo, sesiones reales y próxima acción.
- **Actividades**: catálogo de actividades, prácticas, cuestionarios y rúbricas detectadas en `03-practicas/` y `04-evaluacion/`. Incluye una columna `CE previstos` para anotar los criterios que cubre cada actividad.
- **Registro_CE**: registro por alumno, actividad y CE evaluado. Permite anotar nota del CE, peso dentro de la actividad, evidencia y estado de corrección.
- **Resumen_CE**: medias por alumno y CE calculadas desde `Registro_CE`.
- **Registro_Notas**: hoja auxiliar para una nota global de actividad si se necesita internamente. No debe sustituir a la calificación por CE.
- **RA_CE**: texto de referencia de resultados de aprendizaje y criterios de evaluación.
- **Listas**: estados normalizados para evitar anotaciones inconsistentes.

## Uso recomendado

1. En **Actividades**, anotar en `CE previstos` los CE que cubre cada práctica antes de proponerla.
2. En **Registro_CE**, introducir una fila por alumno, actividad y CE evaluado.
3. Usar `Nota CE 0-10` para la calificación real del criterio, no sólo de la tarea completa.
4. Usar `Peso CE %` si una actividad reparte varios CE con pesos diferentes.
5. En **Resumen_CE**, copiar el nombre del alumno en las filas de los CE que se quieran consultar.
6. Usar `Registro_Notas` sólo como apoyo interno cuando interese conservar una nota global de práctica.

## Relación con la trazabilidad RA/CE

`TRAZABILIDAD_CALIFICACIONES_RA_CE.xlsx` sirve para mapa y propagación rápida actividad → RA/CE. Para seguimiento diario y calificación defendible por CE, usar preferentemente `SEGUIMIENTO_CURSO_PIA.xlsx`, hoja **Registro_CE**.
