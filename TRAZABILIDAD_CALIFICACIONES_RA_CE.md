# Hoja de cálculo de trazabilidad de calificaciones por RA/CE

Archivo asociado: `TRAZABILIDAD_CALIFICACIONES_RA_CE.xlsx`.

> **Nota operativa:** esta plantilla propaga una nota global de actividad a los RA/CE marcados. Si se quiere registrar la calificación oficial directamente por criterio de evaluación, usar `SEGUIMIENTO_CURSO_PIA.xlsx`, hoja `Registro_CE`.

## Uso

1. En la hoja `Mapa_RA_CE`, revisar qué RA/CE trata cada actividad.
   - `1` significa que la actividad computa para ese RA/CE.
   - Un valor parcial como `0.5` reparte la calificación con peso parcial.
2. En la hoja `Calificaciones`, introducir:
   - alumno;
   - actividad;
   - nota sobre 10;
   - observaciones si procede.
3. Las columnas de RA/CE se rellenan automáticamente según el mapa.
4. En `Resumen_RA_CE`, introducir el alumnado en la columna A para obtener la media por RA/CE.

## Hojas incluidas

| Hoja | Función |
|---|---|
| `Instrucciones` | Resumen de uso dentro del propio libro. |
| `Mapa_RA_CE` | Relación actividad → RA/CE. |
| `Calificaciones` | Entrada de notas y propagación automática a RA/CE. |
| `Resumen_RA_CE` | Media por alumno y RA/CE. |
| `RA_CE` | Texto de referencia de RA y criterios de evaluación. |

## Mantenimiento

Cuando se cree, elimine o cambie una práctica, hay que actualizar `Mapa_RA_CE`.

La plantilla no sustituye la rúbrica de cada actividad: sólo traduce la nota final de la actividad a los RA/CE que esa práctica evidencia.
