# Instrucciones de trabajo del repositorio PIA

## Hoja de ruta obligatoria

`ESTADO_ACTUAL_Y_PENDIENTES.md` es la hoja de ruta local del repositorio.

Después de cualquier cambio significativo, revisión, decisión docente, limpieza, movimiento de material, corrección o cierre parcial de una unidad, hay que actualizarla en el mismo turno de trabajo.

No se debe responder que una tarea está terminada si antes no se ha comprobado si procede actualizar esta hoja de ruta.

## Regla anti-pendientes obsoletos

Cuando una tarea, pendiente o decisión quede resuelta, hay que marcarla como hecha inmediatamente en `ESTADO_ACTUAL_Y_PENDIENTES.md`, antes de empezar otro bloque de trabajo.

La actualización debe incluir, cuando proceda:

- cambiar `[ ]` o `[~]` a `[x]`;
- sustituir textos antiguos tipo "queda pendiente" por el estado real;
- mover la acción fuera de "Próximas acciones sugeridas" si ya se ha completado;
- dejar sólo pendientes reales, no históricos ya cerrados.

Si se detecta una contradicción entre una sección antigua y una sección nueva de la hoja de ruta, corregirla en el mismo turno. No se debe dejar una tarea hecha marcada como pendiente.

## Qué debe anotarse

- Qué se ha hecho.
- Qué decisión se ha tomado.
- Qué rutas se han tocado.
- Qué queda pendiente.
- Cuál es el siguiente paso recomendado.

## Regla para subagentes

Cuando se delegue trabajo a subagentes, el prompt debe incluir esta obligación:

> Actualiza `ESTADO_ACTUAL_Y_PENDIENTES.md` si completas una parte del saneamiento, tomas una decisión o cambias el estado de pendientes.

Si el subagente no puede actualizarla, debe devolver explícitamente el bloque que hay que incorporar.

## Cierre de sesión

Antes de cerrar una sesión de trabajo, revisar:

1. `git status --short`
2. Cambios relevantes no consolidados
3. `ESTADO_ACTUAL_Y_PENDIENTES.md`
4. Siguiente paso recomendado

Además, **al final de cada sesión** hay que:

- consolidar en commits los cambios relevantes;
- dejar `ESTADO_ACTUAL_Y_PENDIENTES.md` al día y sin pendientes obsoletos;
- subir al remoto (`git push origin main`) para no dejar trabajo local suelto.

Solo así los pendientes que se lean otro día son reales: la hoja de ruta se vuelve a consultar siempre con el repo sincronizado.

La memoria persistente ayuda, pero no sustituye a la hoja de ruta del repo.
