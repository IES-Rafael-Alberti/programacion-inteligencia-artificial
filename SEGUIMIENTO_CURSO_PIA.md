# Seguimiento del curso PIA 2026-2027

Este documento acompaña al libro `SEGUIMIENTO_CURSO_PIA.xlsx` y define su uso operativo durante el curso.

## Hojas incluidas

- **Imparticion**: seguimiento de partes impartidas por unidad, bloque, fecha, grupo, sesiones reales y próxima acción.
- **Actividades**: catálogo de actividades, prácticas, cuestionarios y rúbricas detectadas en `03-practicas/` y `04-evaluacion/`.
- **Registro_Notas**: registro por alumno y actividad para controlar entregas, corrección, nota, peso y nota ponderada.
- **Resumen_Alumno**: medias por alumno calculadas desde `Registro_Notas`.
- **Listas**: estados normalizados para evitar anotaciones inconsistentes.

## Uso recomendado

1. Al empezar una unidad, filtrar **Imparticion** por unidad y marcar cada parte como `En curso`, `Impartido`, `Reforzar` u `Omitido`.
2. En **Actividades**, marcar qué prácticas se proponen realmente, fechas, entregas esperadas, entregas recibidas y pendientes de corrección.
3. En **Registro_Notas**, introducir una fila por alumno y actividad evaluada. La columna `Nota ponderada` se calcula si hay `Nota 0-10` y `Peso %`.
4. En **Resumen_Alumno**, escribir el alumnado en la columna `Alumno` para obtener media simple, media ponderada, número de actividades registradas y correcciones pendientes.
5. Para trazabilidad fina por RA/CE, cruzar este libro con `TRAZABILIDAD_CALIFICACIONES_RA_CE.xlsx`.

## Criterio de mantenimiento

- Si se añade una práctica nueva al repositorio, debe añadirse también a la hoja **Actividades**.
- Si se cambia la estructura de una unidad, debe revisarse la hoja **Imparticion**.
- Este libro es una herramienta de aula: no sustituye a la programación ni a la trazabilidad legal, pero facilita el seguimiento diario.
