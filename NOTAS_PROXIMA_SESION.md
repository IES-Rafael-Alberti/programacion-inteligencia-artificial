# Handoff PIA — NumPy/JAX (2026-10-14)

Documento portátil para reanudar el trabajo en otro ordenador. La hoja de ruta
completa está en `ESTADO_ACTUAL_Y_PENDIENTES.md`; el procedimiento de remotos y
publicación selectiva, en `ESTRATEGIA_REPOSITORIOS.md`.

## Objetivo de la próxima clase

El grupo dice que la sesión de NumPy avanzada se quedó corta. La siguiente clase
debe ofrecer más práctica y ejemplos, reforzar especialmente broadcasting y
pasar después a JAX si el entorno está listo. R no es obligatorio; si queda tiempo
se puede hacer una breve conexión con pandas o R, pero no ambas.

Guion docente: `01-fundamentos-python/99-profesor/GUION_CUARTA_CLASE_PIA_UD1.md`.

## Materiales NumPy/JAX preparados

- `01-fundamentos-python/01-teoria/06-numpy-avanzado.md`: tipos/memoria, ejes,
  indexación, máscaras, vistas y agregaciones.
- `01-fundamentos-python/01-teoria/07-broadcasting-numpy.md`: regla de formas,
  centrado, normalización, productos exteriores y distancias.
- `01-fundamentos-python/01-teoria/07c-casos-practicos-numpy.md`: ejes,
  `keepdims`, máscaras, `where`, linalg, random, normalización y ejercicios.
- `01-fundamentos-python/02-ejemplos/09_numpy_avanzado.ipynb`: notebook
  canónico avanzado.
- `01-fundamentos-python/02-ejemplos/10_numpy_casos_practicos.ipynb`: taller
  ejecutable con muchos ejemplos y ejercicios.
- `01-fundamentos-python/02-ejemplos/07_numpy_broadcasting_vectorizacion.ipynb`.
- JAX: `01-fundamentos-python/01-teoria/08-guia-numpy-jax.md` y
  `01-fundamentos-python/02-ejemplos/08_introduccion_jax_comparativa.ipynb`.
- Pandas para un enganche breve (la revisión concluyó que UD2 ya tiene material
  suficiente): `02-tratamiento-datos/01-teoria/01-pandas-introduccion.md` y
  `02-tratamiento-datos/01-teoria/02-pandas-ejemplos-guia.md`.

El entorno Pixi `default` **no incluye JAX**. Para la demo JAX, comprobar el
entorno `pia-ud1` definido en `01-fundamentos-python/05-recursos/pia-ud1.yml` o
usar un entorno ya preparado en el aula. No instalar dependencias sobre la marcha;
si JAX no está listo, continuar con NumPy y dejar JAX como demo posterior. El
notebook JAX usa un benchmark moderado de 300 000 elementos.

## Paquete temporal Moodle

- `Moodle/01-UD1/01-documentacion/` contiene 15 PDF, incluidos NumPy avanzado y
  casos prácticos, regenerados desde sus fuentes Markdown.
- `Moodle/01-UD1/02-ejemplos/` contiene los notebooks de fundamentos, estructuras,
  NumPy, broadcasting, casos prácticos, JAX y R opcional.
- POO sigue siendo opcional; no publicar ni asignar sus materiales si no se llega
  al bloque.
- `Moodle/` está excluida de Git. Los PDF se regeneran y los notebooks se copian
  desde sus fuentes; después de confirmar la subida se puede borrar el paquete.
- Confirmar en Moodle qué recursos están visibles; el paquete local preparado no
  equivale a una publicación ya realizada.

## Comprobaciones realizadas

- Ejecutados correctamente `09_numpy_avanzado.ipynb`,
  `10_numpy_casos_practicos.ipynb` y `08_introduccion_jax_comparativa.ipynb`.
- Los PDF `14_NumPy_avanzado.pdf` y `15_Casos_practicos_NumPy.pdf` se generaron y
  validaron.
- `mkdocs build --strict` y `python scripts/check_public_unit_links.py` pasan.
- La ficha pública `docs/accesos-rapidos.md` enlaza el GitHub Pages y el
  repositorio del alumnado.

## Repositorios y otras tareas pendientes

- Trabajar en `teacher`; el directorio único usa `teacher/main` como fuente
  docente y `origin/main` para la exportación pública del alumnado.
- Revisar qué materiales UD0/UD1 están realmente visibles en Moodle y confirmar
  el estado del cuestionario base de Python y la encuesta Feedback.
- Pendiente configurar/verificar Séneca y el calificador Moodle, y validar los
  cuestionarios GIFT base y los tres adicionales de POO/NumPy/EDA. Los GIFT con
  respuestas correctas son fuentes docentes y no se publican en `origin/main`.
- Pendiente decidir si se pide purgar del historial público tres materiales
  docentes retirados del árbol actual; eso requiere reescribir historial y
  coordinar clones.
- Antes de cambiar de ordenador, comprobar que Unison finalizó y que no queden
  conflictos; no copiar `.codex/`, `.opencode/` ni artefactos temporales de
  `graphify-out/`.

Para sincronizar en el ordenador receptor:

```bash
git fetch --all --prune
git switch teacher
git pull --ff-only teacher main
```
