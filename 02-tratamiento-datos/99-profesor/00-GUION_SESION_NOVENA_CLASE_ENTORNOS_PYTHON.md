# Guion de la novena clase — Taller práctico de entornos Python

> **Documento interno del profesorado. Solo repositorio docente; no publicar en `main` del alumnado, GitHub Pages ni Moodle.**

**UD2 · 120 minutos, incluidos 10 de descanso.** Una herramienta cada vez: **instalar/comprobar → configurar → ejecutar → probar → modificar y volver a probar**. El alumnado trabaja desde el comienzo; las ventajas e inconvenientes se comparan al final a partir de la experiencia.

Este enfoque sustituye al guion anterior, que dedicaba bloques a teoría y permitía dejar conda en una lectura o `--dry-run`. Ahora las instalaciones y las comprobaciones son parte del aprendizaje. **Una demo del profesor no cuenta como una práctica realizada por el alumnado.**

## 1. Material que se entrega y objetivo visible

Proyectar y facilitar como documento central:

`02-tratamiento-datos/03-practicas/00-entornos-hazlo-tu.md`

La práctica contiene instrucciones por sistema operativo, ejemplo común, salidas esperadas, cambios por herramienta y formato de registro. Es la fuente de comandos: este guion organiza la clase sin duplicarla.

Objetivo para decir en una frase:

> «Al terminar, habrás ejecutado el mismo análisis de pandas con distintas herramientas, sabrás comprobar qué Python lo ejecuta y tendrás los archivos necesarios para repetirlo».

Manuales de consulta, no de lectura lineal al empezar:

| Necesidad | Fuente en `02-tratamiento-datos/01-teoria/` |
|---|---|
| Comparar herramientas después de probarlas | `00a-entornos-python.md` |
| Instalar/consultar Pixi | `00b-manual-pixi-pia.md` |
| Instalar/consultar conda | `00c-manual-conda-pia.md` |
| Pasar después al trabajo completo de datos de UD2 | `10a-guia-proyecto-python-pixi.md` |

## 2. Preparación antes de clase

- Abrir la práctica actualizada y comprobar acceso a los instaladores oficiales de Python, uv, Miniforge y Pixi desde la red del aula. Tener identificados sistemas operativos, arquitecturas y equipos sin permisos.
- Preparar los instaladores grandes de Miniforge apropiados para el aula si la red suele ser lenta. **Se instalan durante su bloque**, no todos al principio. Quien ya tenga la herramienta verifica versión/configuración y avanza al ejemplo.
- Probar en el equipo docente los comandos de los cuatro bloques en carpetas temporales fuera del repositorio. La comprobación documental no equivale a una instalación ensayada en Windows, macOS y Linux.
- Crear la tarea Moodle de registro **hecho/no hecho**, con posibilidad de completar lo pendiente después. Sustituir el enunciado/PDF anterior: la antigua actividad de preguntas y simulación de conda ya no es el taller vigente.
- No es necesario resolver todos los entornos del `pixi.toml` raíz ni decidir primero la dependencia Matplotlib de `base/default`: el taller crea proyectos pequeños independientes, inicialmente con pandas.

## 3. Ritmo orientativo de 120 minutos

| Minutos | Trabajo del alumnado | Punto de control |
|---|---|---|
| 0–5 | Crear carpetas, copiar `analisis.py`, abrir el registro | Cada estudiante tiene archivos y terminal en el primer bloque. |
| 5–23 | **venv + pip**: comprobar Python, crear/activar, instalar pandas, ejecutar y modificar datos | Python en `.venv`; total 60 y después 70; ambas pruebas OK. |
| 23–43 | **uv**: instalar si falta, reabrir terminal, crear proyecto, ejecutar, añadir rich y sincronizar | Python en `.venv`, `pyproject.toml`, `uv.lock` y prueba OK. |
| 43–53 | Descanso | Guardar el registro antes de salir. |
| 53–80 | **conda**: instalar Miniforge si falta, inicializar, crear desde YAML, ejecutar, actualizar y exportar | `pia-taller-conda`, prueba OK, rich instalado y YAML exportado. |
| 80–108 | **Pixi**: instalar si falta, crear proyecto, añadir paquetes, ejecutar, crear tarea y probar | `pixi.toml`, `pixi.lock`, tarea `analizar` y prueba OK. |
| 108–115 | Comparar ventajas, inconvenientes y usos observados | Tabla individual y cuatro decisiones justificadas. |
| 115–120 | Entregar el registro y anotar la continuación | Estado real por bloque, sin dar por hecho lo no ejecutado. |

**Es una previsión, no una promesa de cuatro instalaciones completas en cualquier equipo.** Si los instaladores o la red consumen el tiempo, se termina el bloque en curso y se retoma el siguiente en la próxima sesión. Se reservan igualmente los últimos cinco minutos para entregar el estado real. La comparación global se completa al haber probado las cuatro herramientas; si faltan bloques, hoy solo se comparan los realizados.

## 4. Método dentro de cada bloque

1. **Consigna de 60–90 segundos como máximo:** qué hay que conseguir y qué salida lo demuestra. No dar una charla sobre todas las opciones antes de ejecutar.
2. **Manos al teclado:** cada estudiante sigue la sección de la práctica en su sistema. El profesor acompaña y resuelve incidencias, no ejecuta todo mientras los demás miran.
3. **Punto de control visible:** pedir la ruta de Python y `PRUEBA OK`, además del manifiesto cuando corresponda. Usar una señal sencilla: «instalando / probando / terminado / bloqueo».
4. **Modificación individual:** cambiar los datos, añadir una dependencia o crear una tarea, según el bloque. Volver a ejecutar y guardar evidencia.
5. **Cierre de un minuto:** una ventaja o dificultad que acaban de observar. Las anécdotas largas y la matriz completa se dejan para el final.

En parejas se alternan los papeles de operador y ayudante, pero ambos ejecutan y registran. Si solo se puede usar un equipo, repetir la operación por turnos y anotar la limitación; tener un compañero que ejecuta no acredita automáticamente la práctica propia.

## 5. Guía de acompañamiento por herramienta

### A. venv + pip

- Empezar directamente por comprobar Python y crear `.venv`. `venv` viene con Python; en Linux puede faltar el paquete del sistema.
- No exigir otra versión de Python solo para este bloque si el Python instalado es compatible con pandas. Las otras rutas fijan Python 3.12 explícitamente.
- Comprobar `python -m pip --version` antes de instalar. El objetivo es que sepan identificar **dónde** instalan.
- El análisis inicial suma 60; el cambio de 30 a 40 exige actualizar también la aserción a 70. Si falla la prueba, leer el mensaje y contrastar código y expectativa.
- Al salir, comparar rutas de Python. No anunciar que `import pandas` necesariamente fallará fuera: podría estar instalado en otro entorno.

### B. uv

- Instalar uv realmente donde falte; reabrir la terminal forma parte de la configuración del `PATH`.
- Usar `uv init --bare --python 3.12`, añadir pandas y ejecutar el mismo script. No mezclar la activación del `venv` anterior con este proyecto.
- Al añadir rich, pedir que localicen el cambio en `pyproject.toml`. Ejecutar `uv sync --locked` y volver a probar el análisis.
- Pregunta de predicción ligada a la acción: «¿Hace falta activar manualmente `.venv` para usar `uv run`?»; ejecutar y comprobar la ruta.

### C. conda

- Si falta, **instalar Miniforge**, abrir la terminal apropiada e inicializar la shell cuando sea necesario. El bloque no se sustituye por un `--dry-run`.
- Crear `environment.yml` pequeño; no instalar el entorno raíz completo del curso ni el antiguo `pia-ud1.yml` para esta prueba.
- Comprobar `conda env list`, activar `pia-taller-conda` y ejecutar `analisis.py`.
- Añadir rich al YAML, actualizar **el mismo entorno**, ejecutar de nuevo y exportar a otro archivo. Aquí se observa la diferencia entre especificación y resolución.
- Mencionar libmamba solo al comprobar el solver: no abrir otra ronda de instalación de mamba/micromamba.

### D. Pixi

- Instalar Pixi donde falte, comprobar `PATH` en una terminal nueva y trabajar en `04-pixi`, fuera del repositorio del curso.
- Crear el proyecto con pandas; ejecutar y comprobar que Python vive en `.pixi/envs/default`.
- Cada estudiante crea la tarea `analizar`, la ejecuta, añade rich y vuelve a probar desde el lock.
- No recorrer el manifiesto completo del módulo, features de ML ni GPU. El cierre puede señalar que el curso amplía este mismo mecanismo con varios entornos, que se aprenderán cuando se usen.

## 6. Incidencias sin convertir al grupo en público

- **Comando no encontrado:** reabrir la terminal, leer el mensaje del instalador y comprobar `PATH`. En conda, probar Miniforge Prompt antes de modificar más cosas.
- **Error de ruta:** abrir la carpeta exacta del bloque y comprobar que `analisis.py` está allí.
- **Instalación lenta:** registrar el comando y el estado; revisar el manifiesto o preparar el registro durante la descarga. Evitar explicaciones largas para llenar la espera.
- **Bloqueo individual:** el profesor ayuda a ese equipo mientras los demás completan la modificación o la ampliación. Si se usa otro equipo, el alumno bloqueado pasa a operar y comprobar.
- **Bloqueo general de permisos/red:** registrar el punto de parada y resolver la infraestructura o continuar el taller otro día. No declarar realizado un bloque mostrado solo en proyección.
- **Alumnado que termina pronto:** ampliación de la práctica: añadir Matplotlib en uno de sus proyectos y generar una figura. No adelantar las siguientes herramientas mientras el grupo sigue en la anterior.

## 7. Comparación final y entrega

Proyectar la tabla vacía de la práctica. Cada estudiante escribe antes de escuchar respuestas: **ventaja, inconveniente y cuándo usaría cada herramienta**. Contrastar después con el mapa de entornos durante unos minutos.

Orientación para la puesta en común:

| Opción | Evidencia para apoyar la decisión |
|---|---|
| venv + pip | Poco extra si Python ya está instalado; hay que elegir bien intérprete/activación y conservar dependencias. |
| uv | Manifiesto y lock para proyectos Python; no es un gestor general de paquetes nativos como conda/Pixi. |
| conda | Entorno nombrado, Python y paquetes nativos; el YAML con rangos vuelve a resolver y no equivale a un lock exacto. |
| Pixi | Proyecto, lock y tareas con paquetes conda/PyPI; requiere instalar el gestor y entender sus archivos. |

Poetry, pipx y Docker se sitúan en **dos frases de cierre** y quedan en los manuales para retomarlos cuando se utilicen. No reservar un bloque de doce minutos de exposición sobre despliegue en este taller.

Recoger el registro con los bloques completos, en curso y pendientes. Mantener valoración **hecho/no hecho** de seguimiento, sin convertir las incidencias de instalación en una prueba de aciertos. Al finalizar, anotar en la hoja de ruta qué herramientas se han llegado a probar realmente y dónde se retomará la siguiente clase.
