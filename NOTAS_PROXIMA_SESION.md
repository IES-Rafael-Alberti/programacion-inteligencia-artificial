# Handoff PIA — cierre EDA NumPy y pandas (2026-10-19)

La hoja de ruta completa está en `ESTADO_ACTUAL_Y_PENDIENTES.md`. El flujo de publicación está en `ESTRATEGIA_REPOSITORIOS.md`.

## Avance real

- El profesor confirma que el 19 de octubre se ha hecho prácticamente toda la parte de NumPy.
- Pandas ya se presentó: Series, DataFrame como conjunto de columnas/Series e inicio de indexación.
- La siguiente clase comienza con un EDA de cierre en NumPy y continúa en pandas. No se vuelve a impartir el bloque avanzado completo de NumPy.

## Guion para el martes 20 de octubre

`01-fundamentos-python/99-profesor/06-GUION_SEXTA_CLASE_PIA_EDA_NUMPY_PANDAS.md`.

- Duración de referencia: 3 horas, incluida pausa de 10 minutos.
- 5 minutos de continuidad y 35 de EDA NumPy con empleados.
- Transición al DataFrame con los mismos datos; retomar etiquetas y posiciones.
- Núcleo: `loc`/`iloc`, filtros compuestos, ordenación y columnas calculadas.
- Ausentes y una agrupación sencilla si se consolida la selección.
- Mini-práctica por parejas y ticket de salida.
- Álgebra lineal: consulta que se activa en UD3. JAX: ampliación, fuera del recorrido de mañana.

## Materiales

- EDA existente: `01-fundamentos-python/03-practicas/09_eda_numpy.md` y `09_eda_numpy.ipynb`.
- El guion incluye un recorrido ejecutable de EDA que aclara problemas de la práctica antigua: array sin nombres, promoción de tipos, valores fuera de escala y tratamiento de atípicos. No ejecutar la celda final de Jupytext del cuaderno antiguo.
- Pandas: `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb` (selección, transformaciones y agrupaciones), más teoría `01-pandas-introduccion.md` y `02-pandas-ejemplos-guia.md` en `02-tratamiento-datos/01-teoria/`.
- La inspección interna `mode.data_manager` del notebook de pandas no es necesaria y depende de la versión; se omite en el recorrido previsto.
- Refuerzo: `01-fundamentos-python/03-practicas/15-ejercicios_numpy_completo.ipynb`, sin exigir completar todo el banco antes de entrar en pandas.

## Preparación y comprobaciones

- Los siete bloques Python del nuevo guion se ejecutaron en orden; sus seis rutas de recursos existen.
- NumPy y pandas bastan; usar el entorno habitual ya preparado. No instalar dependencias durante la clase.
- Confirmar que el alumnado dispone del EDA y del notebook de pandas por Moodle o copia local del repositorio.
- `Moodle/` es un paquete local ignorado, no prueba de publicación externa. Comprobar la visibilidad real y actualizar los notebooks revisados si se distribuyen por allí.
- Los PDF preparados corresponden a documentación de UD1, no todos exclusivamente a NumPy. Los renombrados y la documentación vigente se consultan en la hoja de ruta.

## Repositorios y pendientes

- `teacher` es la fuente de verdad. Teoría, ejemplos, prácticas e índices públicos se trasladan selectivamente a `origin/main`, reflejando renombrados y eliminaciones. No mezclar el historial docente en el público.
- Los guiones de `99-profesor/`, GIFT con respuestas, soluciones y grafo quedan solo en el remoto docente. `.codex/`, `.opencode/` y la caché Graphify son locales.
- La revisión tras Unison del 19 de octubre validó los ejemplos NumPy 10–13 y los tests de los 18 ejercicios. Se publicó el material del alumnado en `origin/main` (`9e346eef`).
- Pendiente importar/probar el GIFT completo corregido en Moodle. También revisar los cuestionarios base y adicionales que se activen, Feedback, Séneca y calificador Moodle.
- Mantener pendiente la decisión de purgar los tres materiales docentes retirados del historial público; no reescribir historial sin decisión expresa y coordinación.
- Al acabar la próxima clase, anotar qué bloques de pandas se impartieron realmente y continuar desde ese punto.
