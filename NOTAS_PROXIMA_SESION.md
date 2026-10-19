# Handoff PIA — R, comparativa, EDA NumPy y pandas (2026-10-19)

La hoja de ruta completa está en `ESTADO_ACTUAL_Y_PENDIENTES.md`. El flujo de publicación está en `ESTRATEGIA_REPOSITORIOS.md`.

## Avance real

- El profesor confirma que el 19 de octubre se ha hecho prácticamente toda la parte de NumPy.
- Pandas ya se presentó: Series, DataFrame como conjunto de columnas/Series e inicio de indexación.
- Falta la introducción breve a R: se añade al comienzo, seguida de la comparativa de lenguajes y formatos que el profesor quiere hacer en clase. Después se cierra NumPy con EDA y se continúa pandas.

## Guion para el martes 20 de octubre

`01-fundamentos-python/99-profesor/06-GUION_SEXTA_CLASE_PIA_EDA_NUMPY_PANDAS.md`.

- Duración de referencia: 3 horas, incluida pausa de 10 minutos.
- 0–5: objetivos y entrega. 5–20: R base. 20–55: comparativa entregable.
- 55–85: EDA NumPy de empleados. 85–100: pasar los mismos datos a pandas.
- 100–110: pausa. 110–140: `loc`/`iloc` y filtros. 140–160: transformaciones.
- 160–175: mini-práctica. 175–180: cierre. Ausentes/agrupaciones, solo ampliación.
- Mini-práctica por parejas y ticket de salida.
- Álgebra lineal: consulta que se activa en UD3. JAX: ampliación, fuera del recorrido de mañana.

## Materiales

- Actividad entregable: `01-fundamentos-python/04-evaluacion/comparativa-lenguajes-formatos-ia.md`, sin observación docente y con plantilla/instrucciones. PDF para subir en `Moodle/01-UD1/03-practicas/comparativa-lenguajes-formatos-ia.pdf`.
- R: guía `01-fundamentos-python/01-teoria/09-guia-r-complementario.md` y notebook `01-fundamentos-python/02-ejemplos/06_introduccion_R_fundamentos.ipynb`. El guion selecciona solo vectores, filtros, `data.frame` y resumen; no requiere paquetes adicionales.

- EDA existente: `01-fundamentos-python/03-practicas/09_eda_numpy.md` y `09_eda_numpy.ipynb`.
- El guion incluye un recorrido ejecutable de EDA que aclara problemas de la práctica antigua: array sin nombres, promoción de tipos, valores fuera de escala y tratamiento de atípicos. No ejecutar la celda final de Jupytext del cuaderno antiguo.
- Pandas: `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb` (selección, transformaciones y agrupaciones), más teoría `01-pandas-introduccion.md` y `02-pandas-ejemplos-guia.md` en `02-tratamiento-datos/01-teoria/`.
- La inspección interna `mode.data_manager` del notebook de pandas no es necesaria y depende de la versión; se omite en el recorrido previsto.
- Refuerzo: `01-fundamentos-python/03-practicas/15-ejercicios_numpy_completo.ipynb`, sin exigir completar todo el banco antes de entrar en pandas.

## Preparación y comprobaciones

- Ejecutados los ocho bloques Python y el ejemplo R con `Rscript`; diez rutas de recursos comprobadas (nueve archivos y el directorio de evaluación).
- NumPy y pandas en el entorno habitual; R preparado previamente en el equipo docente. Si falta kernel R en equipos del alumnado, hacer demostración y lectura sin instalación en clase.
- Confirmar que el alumnado dispone del EDA y del notebook de pandas por Moodle o copia local del repositorio.
- `Moodle/` es un paquete local ignorado, no prueba de publicación externa. Comprobar la visibilidad real y actualizar los notebooks revisados si se distribuyen por allí.
- Los PDF preparados corresponden a documentación de UD1, no todos exclusivamente a NumPy. Los renombrados y la documentación vigente se consultan en la hoja de ruta.

## Pendiente mañana 20-10: Moodle, antes de clase

1. Importar `cuestionario-numpy.gift` (25 preguntas), `cuestionario-eda-numpy.gift` (20) y `cuestionario-numpy-completo.gift` (18), desde `01-fundamentos-python/04-evaluacion/`. Total: 63 preguntas. No adjuntar las fuentes GIFT como recursos del alumnado.
2. Comprobar categorías, recuentos, respuestas y feedback; evitar duplicados al reimportar. Crear/actualizar los recursos de cuestionario y revisar acceso/visibilidad con rol de estudiante. Álgebra 13–15 del completo: categoría de consulta UD3, fuera del repaso obligatorio; EDA tras verlo.
3. Subir la comparativa en PDF y habilitar su tarea de entrega para hacerla en clase. Mostrar el plazo y formatos admitidos antes de comenzar.
4. La importación y la subida no se han hecho desde esta sesión; son pendientes reales.

## Repositorios y pendientes

- Decisión docente 2026-10-19: cuando se vean gráficas en Python, realizar ejemplos equivalentes en R y comparar código y resultados sobre los mismos datos. Retomarlo al preparar visualización en UD2; mañana solo se introduce R de forma breve.

- `teacher` es la fuente de verdad. Teoría, ejemplos, prácticas e índices públicos se trasladan selectivamente a `origin/main`, reflejando renombrados y eliminaciones. No mezclar el historial docente en el público.
- Los guiones de `99-profesor/`, GIFT con respuestas, soluciones y grafo quedan solo en el remoto docente. `.codex/`, `.opencode/` y la caché Graphify son locales.
- La revisión tras Unison del 19 de octubre validó los ejemplos NumPy 10–13 y los tests de los 18 ejercicios. Se publicó el material del alumnado en `origin/main` (`9e346eef`).
- Ampliación local de cuestionarios validada estáticamente (25+20+18). Pendiente importar/probar los tres bancos actualizados mañana, además de revisar Feedback, Séneca y calificador Moodle cuando corresponda.
- Mantener pendiente la decisión de purgar los tres materiales docentes retirados del historial público; no reescribir historial sin decisión expresa y coordinación.
- Al acabar la próxima clase, anotar qué bloques de pandas se impartieron realmente y continuar desde ese punto.
