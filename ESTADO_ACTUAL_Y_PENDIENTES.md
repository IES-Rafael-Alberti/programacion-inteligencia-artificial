# Estado actual y pendientes — PIA 2026-2027

**Fecha de snapshot:** 2026-09-30
**Veredicto general:** **OPERATIVAMENTE TERMINADO / SEMICERRADO**

## Resultado real de la sexta clase y preparación de la siguiente (2 h) — 2026-10-21

### Cierre y publicación — 2026-10-21

- [x] Creado el guion de 2 h `01-fundamentos-python/99-profesor/07-GUION_SEPTIMA_CLASE_PIA_R_COMPARATIVA_PANDAS.md`; material consolidado en `359f1924` y subido a `teacher/main`.
- [x] Publicada la guía de instalación R/VS Code y sus enlaces en `origin/main` (`1bfdfd91`). Build estricto de MkDocs superado.
- [ ] **Incidencia de publicación:** también se ejecutó por error `git push origin teacher`, actualizando la rama `teacher` del repositorio público a `359f1924`. Esa rama ya existía en `7fd5e3ba`, pero no constituye un espacio privado ni un staging seguro. Revisar su exposición y acordar su retirada y el tratamiento del historial recuperable; no considerar resuelta la incidencia por la publicación selectiva correcta en `origin/main`.

**Siguiente paso de mantenimiento:** resolver la exposición de `origin/teacher` antes de nuevas publicaciones. El trabajo docente para la próxima clase está preparado; Moodle conserva los pendientes indicados abajo.

### Sesión 6 (20-10) — lo realmente impartido

- [x] **EDA con NumPy visto en su totalidad** usando el recorrido del guion (estructura, ausentes, filtros, IQR y conclusión), sobre el dataset de empleados.
- [x] **Creado un nuevo notebook para que el EDA lo hagan los alumnos:** `01-fundamentos-python/03-practicas/16-eda_numpy_edificios.ipynb`, con dataset sintético de edificios y ejercicios sin soluciones (indexado, máscaras, faltantes, IQR, `np.where`, grupos, escalado, correlaciones, resumen y exportación `.npz`). Está enlazado en el README de prácticas. **Pendiente: decidir su publicación/distribución en Moodle.**
- [~] **R no llegó a verse con las herramientas previstas.** Los alumnos intentaron instalar **RStudio**, pero la página de descarga devolvía un XML en lugar de comenzar la descarga. Como alternativa se pasó a **instalar R directamente desde CRAN** y a **instalar los plugins de VS Code para R**. La introducción a R en sí (sintaxis, `data.frame`, resumen) quedó para esta próxima sesión.
- [x] Pandas: la parte tratada previamente (Series, DataFrame, inicio de indexación) aún no se ha ampliado; sigue pendiente el repaso y la continuación planificada.

### Decisión: instalar R y usar notebooks R en VS Code, sin RStudio

- [x] Documentada la ruta de arranque (instalar R desde CRAN, conectar kernel R en VS Code mediante Jupyter/IRkernel) en `01-fundamentos-python/05-recursos/guia-instalacion-r-vscode.md`. Incluye pasos, comprobación, uso de notebooks con kernel R y problemas frecuentes (página de RStudio con XML, `R` sin `PATH`, kernel no visible, `IRkernel::installspec` sin jupyter).
- [x] Enlazada la guía desde `01-fundamentos-python/01-teoria/09-guia-r-complementario.md`, desde la tabla de teoría (`README.md`, fila 15) y desde el README de la unidad.
- [ ] **Antes de la próxima clase:** el alumnado debe instalar R y registrar el kernel (la guía va al comienzo de la clase para hacerlo). Comprobar que el notebook `06_introduccion_R_fundamentos.ipynb` abre con kernel R en el equipo docente. El notebook se ha ampliado con una progresión guiada de exploración, indexación, `NA` y operaciones vectorizadas; la ejecución con kernel R sigue pendiente de comprobar.

### Próxima clase (2 h) — plan

El tiempo de la sesión previa queda muy repartido: lo que no se llegó a hacer (R, comparativa, repaso inicial de pandas) pasa a esta sesión de **2 horas**, más corta que la de 3 horas planeada.

1. **Arranque (instalar R + VS Code):** seguir `05-recursos/guia-instalacion-r-vscode.md` para instalar R, los plugins de VS Code (R y Jupyter) y registrar IRkernel. Un primer notebook R con kernel seleccionado. Todo el ritmo de esta sesión está en `99-profesor/07-GUION_SEPTIMA_CLASE_PIA_R_COMPARATIVA_PANDAS.md`.
2. **Introducción breve a R** con `01-teoria/09-guia-r-complementario.md` y `02-ejemplos/06_introduccion_R_fundamentos.ipynb`: vectores, `data.frame`, resumen (sin bucles/funciones completas ni paquetes nuevos).
3. **Comparativa de lenguajes y formatos** (entregable): `04-evaluacion/comparativa-lenguajes-formatos-ia.md` (subir/habilitar tarea en Moodle) usando el R recién visto como referencia frente a Python.
4. **Repaso de lo primero de pandas:** Series, DataFrame como conjunto de columnas/Series e inicio de indexación, antes de continuar con `loc`/`iloc`, filtros y transformaciones.

**Siguiente paso:** subir la comparativa y decidir la distribución del notebook 16 en Moodle; el guion corto de 2 h ya está creado (`99-profesor/07-GUION_SEPTIMA_CLASE_PIA_R_COMPARATIVA_PANDAS.md`).

## RETOMAR EN EL ORDENADOR DEL INSTITUTO — antes de clase del 20-10-2026

La preparación está terminada y publicada en GitHub; **la importación/publicación en Moodle aún no está hecha**. Este es el orden de trabajo pendiente:

1. [ ] **Comprobar sincronización en el instituto.** Esperar a que Unison termine y revisar `git status --short`. Trabajar en la rama docente `teacher` y comprobar que contiene la ampliación de cuestionarios y el guion actualizado (material en `f0032c94`, cierre en `808a97ca` o posteriores). Si hay cambios locales, revisarlos antes de actualizar desde GitHub. No mezclar el historial docente en `main` del alumnado.
2. [ ] **Importar en Moodle los tres bancos actualizados**, desde `01-fundamentos-python/04-evaluacion/`:
   - `cuestionario-numpy.gift`: **25 preguntas**.
   - `cuestionario-eda-numpy.gift`: **20 preguntas**.
   - `cuestionario-numpy-completo.gift`: **18 preguntas**; 15 de práctica de código y 3 en **Álgebra consulta UD3**.
   - Comprobar categorías, recuentos, respuestas cortas/variantes y retroalimentación. Evitar duplicados si se reimportan bancos previos. Crear/actualizar los recursos de cuestionario, ajustar acceso y visibilidad, y probar con rol de estudiante. Mantener álgebra fuera del repaso obligatorio y activar EDA después de su ejemplo. No publicar los GIFT como archivos descargables.
3. [ ] **Publicar la comparativa y habilitar su entrega para hacerla en clase.** PDF preparado: `Moodle/01-UD1/03-practicas/comparativa-lenguajes-formatos-ia.pdf`. Fuente entregable, sin observación docente: `01-fundamentos-python/04-evaluacion/comparativa-lenguajes-formatos-ia.md`. Mostrar plazo, formatos admitidos y lugar de entrega. **`Moodle/` está ignorada por Git: comprobar que el PDF haya llegado con Unison; si falta, recuperarlo/regenerarlo desde la fuente, no asumir que vendrá de un pull.**
4. [ ] **Preparar el inicio de R y abrir el guion docente:** `01-fundamentos-python/99-profesor/06-GUION_SEXTA_CLASE_PIA_EDA_NUMPY_PANDAS.md`. Comprobar R en el equipo del profesor; si falta en los equipos del alumnado, usar demostración sin instalar durante la clase. Plan: R breve → comparativa entregable → EDA NumPy → pandas. Confirmar acceso a los notebooks EDA y pandas.
5. [ ] **Después de clase:** marcar aquí lo importado/publicado realmente, registrar entrega de la comparativa y punto alcanzado en pandas, y actualizar `NOTAS_PROXIMA_SESION.md`. No marcar Moodle como completado solo por tener archivos locales o por estar en GitHub.

**Recordatorio posterior:** cuando se impartan gráficas en Python (UD2), hacer ejemplos equivalentes en R y comparar código y resultados sobre los mismos datos. No corresponde a la introducción breve de mañana.

## Preparación para mañana: cuestionarios, R y actividad entregable — 2026-10-19

- [x] Ampliado `01-fundamentos-python/04-evaluacion/cuestionario-numpy.gift`: de 10 a **25 preguntas**. Añadidas interpretación de tipos/memoria, cortes 2D, ejes, `keepdims`/`newaxis`, máscaras compuestas, selección, límites, vistas/copias, índices de ordenación, concatenación/apilado, ufuncs, redondeo e I/O básico.
- [x] Ampliado `cuestionario-eda-numpy.gift`: de 10 a **20 preguntas**. Añadidas media/mediana, escalado/estandarización, histograma, frecuencias, correlación/covarianza, distribuciones, muestreo y correspondencia fila-etiqueta. Actualizada la semilla al `Generator` moderno y aclarado el feedback de `np.where(x)`.
- [x] Mantenidas las **18 preguntas** del banco de código, con variantes habituales de respuesta para reducir rechazos por espacios o sintaxis equivalente. Separadas mediante categorías GIFT las preguntas 13–15 de álgebra para consulta/UD3; las otras 15 pertenecen al núcleo actual. No se garantiza aceptación de toda expresión Python equivalente: Moodle compara texto.
- [x] Total de los tres bancos: **63 preguntas**, incluidas **25 nuevas**. Verificados identificadores únicos, delimitadores, alternativas, feedback y categorías; contrastados numéricamente los resultados/propiedades de las 25 nuevas. Falta validar la importación en Moodle.
- [x] Preparado para alumnado el enunciado canónico `04-evaluacion/comparativa-lenguajes-formatos-ia.md`, conservando su ruta: retirado el apartado «Observación docente» y añadidos caso concreto, instrucciones/plantilla de entrega, fuentes/declaración de IA y ejemplo XML/HTML para RA1.f. La observación docente pasa al guion privado. Actualizado el README de evaluación.
- [x] Generado el PDF entregable `Moodle/01-UD1/03-practicas/comparativa-lenguajes-formatos-ia.pdf` (paquete local ignorado), comprobado texto y ajuste de tablas a la página.
- [x] Ajustado el guion `99-profesor/06-GUION_SEXTA_CLASE_PIA_EDA_NUMPY_PANDAS.md`: R base 5–20 min, comparativa en clase 20–55, EDA NumPy 55–85 y pandas después, con pausa y mini-práctica. Ausentes/agrupaciones pasan a ampliación para que las tres horas sean viables. Ejecutados ocho bloques Python y un ejemplo R; comprobadas las rutas.
- [ ] **Mañana, 20-10, antes de clase: subir/importar los tres cuestionarios NumPy actualizados a Moodle**, comprobar categorías/recuentos/feedback y publicar los recursos que procedan. No subir el GIFT fuente como archivo visible. Excluir álgebra de UD3 del repaso obligatorio y activar EDA tras el ejemplo.
- [ ] **Mañana, 20-10: subir el PDF de la comparativa y habilitar su tarea de entrega** para realizarla en clase después de la introducción a R; comprobar plazo y acceso del alumnado.
- [x] Registrada también la decisión de comparar gráficas Python/R al impartir visualización en UD2. Ese trabajo queda pendiente para ese bloque, no para mañana.

- [x] Consolidado el material completo en `teacher/main` (`f0032c94`). Publicados solo el enunciado del alumnado y el README de evaluación en `origin/main` (`0e13064a`); bancos GIFT y guion permanecen privados. MkDocs `--strict`, comprobación de navegación pública y `git diff --check` superados.

**Siguiente paso:** mañana, importar/probar los bancos y publicar la comparativa/tarea en Moodle antes de clase. La preparación y publicación en GitHub ya están completadas; Moodle sigue pendiente.

## Decisión docente — visualización comparada Python/R (2026-10-19)

- [x] Acordado con el profesor que, cuando se trabajen las gráficas en Python, también se harán ejemplos equivalentes en R y se compararán código y resultados con los mismos datos y preguntas de análisis.
- [ ] Al preparar el bloque de visualización de UD2, incorporar la comparación Python/R: tipos de gráfico, sintaxis, etiquetas, tratamiento de datos y lectura del resultado. Elegir las herramientas concretas de R al preparar ese bloque; no se presupone hoy un paquete nuevo.
- [x] La introducción breve de R de mañana se limita a vectores, operaciones, `data.frame` y un resumen. La comparación gráfica queda para el bloque de visualización, no para la sesión del 20 de octubre.

**Siguiente paso:** recuperar esta decisión al preparar las clases de gráficas de UD2.

## Revisión de cobertura de cuestionarios NumPy — 2026-10-19 (diagnóstico previo a la ampliación)

- [x] Contrastados los tres bancos específicos con los ejemplos NumPy 05–13 y el avance comunicado: `04-evaluacion/cuestionario-numpy.gift` (10 preguntas conceptuales), `cuestionario-eda-numpy.gift` (10 preguntas) y `cuestionario-numpy-completo.gift` (18 respuestas cortas). Total: **38 preguntas específicas**. El cuestionario base de Python añade una pregunta general sobre el propósito de NumPy, pero no cubre los huecos avanzados.
- [x] **Diagnóstico: cobertura parcial, no completa respecto a los materiales trabajados.** El banco «completo» acompaña los 18 ejercicios, pero solo pregunta una operación por ejercicio. Una función mencionada en feedback o como distractor no se considera evaluada directamente. Ejemplo: la pregunta 17 pide solo el percentil 25, no histograma, covarianza, correlación ni valores únicos del ejercicio 17.
- [x] Bien cubiertos: concepto de `ndarray`, creación y conversión de tipos, `shape`/`reshape`, suma/media por eje 0, vectorización básica, reglas de broadcasting, máscaras simples, semilla/Generator y normal, permutación/split y detección elemental de NaN/IQR.
- [x] Huecos esenciales detectados: cortes y selección 2D más allá de una columna; ejes 0/1, `keepdims` y `newaxis`; condiciones compuestas con `&`/`|` y paréntesis; `where`/`select`/`clip`; efecto de modificar vistas frente a copias; `sort`/`argsort`/`argmax`; concatenación/apilado; resultados de `reduce`/`accumulate`/`outer`; redondeo, histogramas/`bincount`/`unique`; correlación/covarianza e interpretación; comparación media/mediana/desviación y escalado. No hace falta una pregunta por función, pero sí cubrir estas capacidades con situaciones representativas.
- [x] Cobertura parcial de bloques secundarios: aleatoriedad pregunta generador, normal y permutación, pero no `choice` con probabilidades, distinción `shuffle`/`permutation` ni interpretación de distribuciones. I/O pregunta solo `save`; faltan recuperación y diferencias básicas `.npy`/`.npz`/CSV. Las ampliaciones de distribuciones y formatos se ajustarán a lo efectivamente impartido, no a toda la biblioteca.
- [x] Separado el alcance temporal: preguntas 13–15 del banco completo (producto matricial, norma y `solve`) corresponden al material de consulta/UD3. El EDA previsto para el 20 de octubre todavía no consta como impartido: sus preguntas se activarán tras trabajarlo, sin contabilizarlo como hueco de una clase ya dada.
- [x] Comprobación estática: 10 + 10 + 18 identificadores y bloques de respuesta. Sin nuevos errores graves de respuesta detectados en esta lectura. Sigue pendiente la importación real en Moodle; las respuestas cortas literales no ejecutan Python ni admiten automáticamente todas las expresiones equivalentes.
- [x] Mejora de redacción localizada para una futura edición: en EDA 06, `np.where(x)` sí es una llamada válida que devuelve índices de elementos no nulos; no selecciona los valores mayores de 4. EDA 05 usa la semilla global antigua, válida pero menos alineada con el `Generator` moderno trabajado. No se han modificado los bancos durante esta revisión.
- [x] Ampliación encargada y realizada en este turno: 25 preguntas nuevas en los dos bancos existentes; álgebra separada por categoría y EDA asociado a su momento de clase. El diagnóstico de 38 preguntas anterior es la situación previa, sustituida por los recuentos 25+20+18 de la preparación actual.

**Siguiente paso recomendado:** importar y validar los tres bancos actualizados en Moodle, tal como figura en los pendientes de mañana. La ampliación de cobertura está completada.

## Próxima clase — EDA NumPy y pandas (preparada el 2026-10-19)

- [x] Registrado el avance real comunicado por el profesor: NumPy está prácticamente terminado. Pandas ya se había iniciado con Series, DataFrame e inicio de indexación.
- [x] Creado `01-fundamentos-python/99-profesor/06-GUION_SEXTA_CLASE_PIA_EDA_NUMPY_PANDAS.md` para el 2026-10-20. Plan actualizado: 3 horas con R breve, comparativa entregable, EDA NumPy de cierre (30 minutos) y transición usando los mismos datos a pandas. Prioridad en pandas: `loc`/`iloc`, filtros y columnas calculadas; ausentes/agrupación solo si hay margen.
- [x] Revisado el EDA existente: el guion aclara nombres y tipos en arrays homogéneos, selección aleatoria sin reemplazo, interpretación de valores fuera de escala y atípicos, y conservación de originales. Incluye un recorrido ejecutable sin la celda de conversión Jupytext del cuaderno antiguo.
- [x] Verificación inicial: siete bloques Python y seis rutas; tras añadir R se ejecutaron ocho bloques Python y un ejemplo R. Los notebooks públicos existentes se mantienen; el enunciado entregable sí se actualiza en la preparación posterior.
- [x] Actualizado `NOTAS_PROXIMA_SESION.md` para sustituir la antigua preparación NumPy/JAX por el estado real y el guion de mañana. Guion y continuidad quedan solo en el repositorio docente.

**Siguiente paso:** comprobar disponibilidad de los recursos antes de clase e impartir el EDA de cierre y pandas. Registrar después el punto real alcanzado en UD2; no volver a planificar un repaso completo de NumPy.

## Revisión tras Unison — 2026-10-19

- [x] Revisados los tres commits incorporados desde el instituto (`2952f991`, `4e89ea72`, `59cf253c`) y las modificaciones locales de los notebooks 10, 12 y 13. Se conservan las explicaciones y las salidas de clase.
- [x] Corregido `03-practicas/15-ejercicios_numpy_completo.ipynb`: saltos de línea Markdown, variable `a` explícita, instrucciones de indexado/correlación, demostración efectiva de vista y copia (99 y −1), `int64` para la suma de cuadrados y test de tiempos sin exigir aceleración mínima. Los ejercicios 13–15 quedan identificados como consulta para UD3.
- [x] Corregidos en `02-ejemplos/13_numpy_ufuncs_estadistica_avanzado.ipynb` dos encabezados que se renderizaban como código y una descripción que prometía una normalización inexistente. En el notebook 12 se usan archivos temporales aislados y se cierra el `.npz` con `with`.
- [x] Reparado `04-evaluacion/cuestionario-numpy-completo.gift`: retroalimentación general dentro de las llaves y caracteres de sintaxis escapados. El README remite al cuestionario de Moodle, sin enlazar la fuente docente.
- [x] Ejecutados con `nbclient` los ejemplos 10–13; los 18 ejercicios y sus tests pasan con soluciones inyectadas solo en memoria. Comprobada la estructura de las 18 preguntas GIFT; sigue pendiente su importación real en Moodle.
- [x] Retirada del seguimiento la caché restante de `graphify-out/cache/`, conservada en disco e ignorada; el grafo permanece en el repositorio docente.

- [x] Revisión consolidada y subida al remoto docente en `10050fbe`. Publicado en `origin/main` el subconjunto del alumnado en `9e346eef`: renumeración, teoría, ejemplos 10–14, gráficas de aleatoriedad, cuaderno integral de ejercicios e índices. GIFT, guiones, soluciones y grafo permanecen en el remoto docente.
- [x] `mkdocs build --strict` y `scripts/check_public_unit_links.py` superados en la rama pública: 12 unidades, 60 secciones y cero enlaces internos rotos. `git diff --check` sin incidencias.

**Siguiente paso:** importar y probar el cuestionario corregido en Moodle; actualizar allí los notebooks si se distribuyen mediante el paquete temporal. La preparación local o la publicación en GitHub no acredita su actualización en Moodle.

## Cuaderno integral de ejercicios y cuestionario NumPy — 2026-10-19

## Cuaderno alternativo de ejercicios NumPy — 2026-10-20

- [x] Creado y renombrado `01-fundamentos-python/03-practicas/16-eda_numpy_edificios.ipynb` para el alumnado: EDA con dataset sintético reproducible de consumo energético de edificios, con columnas y contexto distintos del cuaderno de empleados.
- [x] Incluidos ejercicios sin soluciones sobre indexado, máscaras, faltantes, IQR, `np.where`, agregaciones por grupos, escalado, correlaciones, resumen estadístico y exportación `.npz`, con comprobaciones `assert`.
- [x] Añadido el nuevo notebook al índice de `01-fundamentos-python/03-practicas/README.md`.
- [x] Validado localmente el JSON y la sintaxis de las celdas de código; queda pendiente decidir su publicación/importación en Moodle si se distribuye como material adicional.

- [x] Creado `01-fundamentos-python/03-practicas/15-ejercicios_numpy_completo.ipynb` con **18 ejercicios** que recorren fundamentos y contenidos avanzados de NumPy. Cada uno incluye enunciado Markdown, datos iniciales cuando hacen falta, celda de respuesta vacía y tests con `assert`; los ejercicios de broadcasting, vistas/copias, aleatoriedad, distancias, ufuncs e I/O incluyen pistas.
- [x] Creado `01-fundamentos-python/04-evaluacion/cuestionario-numpy-completo.gift` con **18 preguntas de código**, una por ejercicio y en el mismo orden. Cada opción incluye retroalimentación para que el cuestionario acompañe al trabajo en el notebook.
- [x] Enlazado el notebook desde prácticas y descrito el cuestionario de Moodle desde evaluación, sin enlace público al GIFT docente. Las soluciones del notebook se probaron junto con los tests: los 18 conjuntos pasan; la revisión posterior corrige presentación e instrucciones y vuelve a verificarlos.
- [x] Actualizado el grafo Graphify tras añadir los materiales: 3.793 nodos, 5.099 enlaces, 430 comunidades y 61 hiperconexiones; comprobado que no hay extremos de enlace ausentes. MkDocs `--strict` terminó con código 0.
- [x] El GIFT contiene respuestas y retroalimentación con soluciones de referencia; se conserva en el remoto docente privado y no se publica como archivo fuente en `origin/main`. La entrega del cuestionario al alumnado se hará mediante Moodle.

**Siguiente paso:** importar el GIFT en Moodle para validar el formato de la plataforma y probar la secuencia con una cuenta de estudiante; el alumnado debe tener disponibles ambos recursos.

## Renumerado de los materiales avanzados de NumPy — 2026-10-19

Para que cada documento de teoría `.md` y su notebook guiado compartan el mismo número de archivo, se renumeró el bloque avanzado de NumPy:

- **Casos prácticos**: `07c-casos-practicos-numpy.md` → `10-numpy-casos-practicos.md` (emparejado con el notebook `10_numpy_casos_practicos.ipynb`, ya numerado 10).
- **Aleatoriedad**: el notebook `12_numpy_aleatoriedad_avanzado.ipynb` → `11_numpy_aleatoriedad_avanzado.ipynb` (el `.md` ya era `11-numpy-aleatoriedad-avanzado.md`).
- **Entrada/salida**: el notebook `13_numpy_io_archivos_avanzado.ipynb` → `12_numpy_io_archivos_avanzado.ipynb` (el `.md` ya era `12-numpy-io-archivos-avanzado.md`).
- **Ufuncs/estadística**: el notebook `14_numpy_ufuncs_estadistica_avanzado.ipynb` → `13_numpy_ufuncs_estadistica_avanzado.ipynb` (el `.md` ya era `13-numpy-ufuncs-estadistica-avanzado.md`).
- **Álgebra lineal avanzada**: tanto el `.md` `10-numpy-algebra-lineal-avanzado.md` como el notebook `11_numpy_algebra_lineal_avanzado.ipynb` pasan a **14** (`14-numpy-algebra-lineal-avanzado.md` y `14_numpy_algebra_lineal_avanzado.ipynb`), quedando como material de consulta/UD3 tras la serie.

Resultado final (pares alineados): casos=10, aleatoriedad=11, io=12, ufuncs=13, álgebra=14. Se actualizaron las referencias en `01-teoria/README.md`, `docs/unidades/ud01.md`, `NOTAS_PROXIMA_SESION.md`, guiones 04/05 de clase, README del paquete Moodle y los enlaces internos de los propios `.md`. Los notebooks renombrados son JSON válidos (renombrados con `git mv`).

**Siguiente paso:** regenerar los PDF del paquete Moodle de UD1 con los nuevos nombres de origen si se publica el material en Moodle.

## Mejoras al notebook avanzado de aleatoriedad — 2026-10-19

- [x] Añadidas a `01-fundamentos-python/02-ejemplos/11_numpy_aleatoriedad_avanzado.ipynb` las **gráficas de las distribuciones**: una figura 2×3 (15×8) con histogramas de las continuas (Uniforme, Normal, Exponencial) y barras de frecuencias de las discretas (Binomial, Poisson, enteros uniformes), todo con `default_rng(0)` y 10 000 muestras.
- [x] Añadida la sección **"Dataset 2D: barajar bien vs. mal"** con ejemplo didáctico: muestra el fallo de permutar `X` y `y` por separado (se rompe la correspondencia fila-etiqueta) frente a la forma correcta de permutar los índices una sola vez y aplicarlos a ambas (`idx = rng.permutation(n); X[idx]; y[idx]`), con verificación de que cada fila conserva su etiqueta.
- [x] Notebook validado: JSON correcto (28 celdas) y todas las celdas de código compilan con `ast`.

**Validación completada el 2026-10-19:** notebook ejecutado correctamente con `nbclient`. Queda actualizar el paquete Moodle si procede.

## Revisión de sincronización y libros NumPy — 2026-10-18

- [x] Revisado el estado local de PIA: hay cambios sin consolidar en cuatro notebooks (`01_introduccion_entorno_python.ipynb`, `02_variables_tipos_operadores.ipynb`, `10_numpy_casos_practicos.ipynb` y `01_pandas_fundamentos.ipynb`), además de `.codex/` y `.opencode/origin` locales. Se conservan como trabajo local.
- [x] El intento del 2026-10-18 quedó bloqueado por el volumen EVO no montado; el 2026-10-19 el usuario confirma que los cambios del instituto ya están incorporados mediante Unison. Revisados en esta sesión, sin repetir la sincronización.
- [x] Localizado el archivo histórico `01-fundamentos-python/90-archivo/NumPy-20251016.zip` (7,8 MB), que contiene el EPUB de referencia según `DECISIONES_MATERIAL_ARCHIVADO.md`; el material activo está en `01-fundamentos-python/01-teoria/` y `02-ejemplos/`.

**Siguiente paso:** mantener la sincronización entre equipos; la revisión del EPUB histórico sigue siendo opcional.

## Catálogo de bibliografía NumPy — 2026-10-18

- [x] Buscados los mejores libros sobre NumPy (solo o con DS/ML) y comprobado qué tenemos en el equipo. Todo lo relevante está en `/datos/RafaelAlberti` (mayoritariamente en `RafaelAlberti26_27/Libros/`, con duplicados históricos en 23_24/24_25/25_26); `/datos/Biblioteca` es de ficción y `/datos/libros` está sin descomprimir; `/datos/descargas` no existe.
- [x] Extraídos los TOC de los manuales con sección NumPy: **Python Data Science Handbook** (VanderPlas 2023, Parte II C4-C12), **Python for Data Analysis** (McKinney 2022, C4), **Python NumPy For Beginners** (2022, 6 caps), **Machine Learning for Beginners** (2020, C3), **Essential Math for Data Science** (C4 álgebra lineal), **Python for Data Science** (Vasiliev 2022, C3), **Python 4 DS For Dummies**, **Hands-On Data Analysis with Pandas**.
- [x] Determinado que **PDSH (VanderPlas) es el manual de NumPy más completo**; McK aporta álgebra lineal + I/O de arrays + generación aleatoria; NBeg aporta práctica aplicada (CSV, estadística, red neuronal) y EM4DS el fundamento matemático.
- [x] Creado el índice combinado `01-fundamentos-python/05-recursos/INDICE_NUMPY_LIBROS.md` con 7 bloques (antes de NumPy, fundamentos de arrays, indexado/rebanado, operaciones/ufuncs, ordenación/estructuras, aleatorios e I/O, aplicaciones) y tabla por libro; enlazado desde `01-fundamentos-python/README.md` (sección Recursos).
- [ ] Revisar si `90-archivo/NumPy-20251016.zip` (EPUB histórico de NumPy) merece incorporarse al catálogo de la biblioteca. Sin decisión tomada; pendiente de valoración.

**Siguiente paso sugerido:** revisar el EPUB histórico si aporta valor y contrastar el material en clase. Los notebooks avanzados ya se validaron en ejecución; la revisión del 2026-10-19 vuelve a comprobar los ejemplos 10–13.

## Guion de la quinta clase (3 h) — 2026-10-18

- [x] Creado `01-fundamentos-python/99-profesor/GUION_QUINTA_CLASE_PIA_UD1.md` (3 h): retoma NumPy donde quedó en la cuarta (se saltó la parte final y se pasó antes de tiempo a pandas), cierra ufuncs/estadística (13) como esencial, aleatoriedad (11) esencial en parte, I/O (12) como apunte, y deja **álgebra lineal (10) para UD3** (kNN/clustering/PCA) y **JAX** como ampliación; luego EDA con NumPy (repaso de `09_eda_numpy`, ya completo), ejercicios NumPy agrupados (ya hay 18) y **transición suave a pandas** (Series → DataFrame por Series → arranque de indexación con `loc`/`iloc` simples). No se ha creado teoría nueva de EDA ni ejercicios: ya están hechos.

## Expansión NumPy avanzada — 2026-10-18

- [x] Diagnóstico de cobertura: el material NumPy de UD1 cubre bien fundamentos, ufuncs, broadcasting, máscaras y vistas/copias, pero es superficial en **álgebra lineal**, **números aleatorios**, **entrada/salida de archivos** y **funciones universales/estadística avanzadas**.
- [x] Creados **4 documentos de teoría nuevos** (sin modificar los existentes):
  - `01-fundamentos-python/01-teoria/14-numpy-algebra-lineal-avanzado.md`
  - `01-fundamentos-python/01-teoria/11-numpy-aleatoriedad-avanzado.md`
  - `01-fundamentos-python/01-teoria/12-numpy-io-archivos-avanzado.md`
  - `01-fundamentos-python/01-teoria/13-numpy-ufuncs-estadistica-avanzado.md`
- [x] Creados **4 notebooks guiados equivalentes** en `02-ejemplos/` (numerados 11-14, cada uno con celdas markdown explicativas y código ejecutable). Validados con `nbclient` sin errores.
- [x] Enlazados los nuevos documentos en: `01-teoria/README.md` (tabla de ruta), `01-fundamentos-python/README.md` (teoría), `docs/unidades/ud01.md` (enlaces directos a los 4 avanzados).
- [x] `mkdocs build --strict` superado sin errores.
- [x] Regenerados los PDF de NumPy avanzado con Pandoc + XeLaTeX en `Moodle/01-UD1/01-documentacion/`; comprobados existencia y tamaño no vacío. La tabla del README de documentación queda actualizada para los PDF 16–20.
- [x] Saneado `11-numpy-aleatoriedad-avanzado.md`: convertidas las secuencias literales `\n` en saltos de línea reales y regenerado su PDF con Pandoc + XeLaTeX; Markdown y PDF verificados.
- [x] Saneados los nombres de los cuatro PDF avanzados para que coincidan con el nombre base de sus fuentes Markdown (`10-numpy...pdf` a `13-numpy...pdf`), eliminando los nombres antiguos `17_...`–`20_...` sin duplicados.
- [ ] Revisar los notebooks con el dossier de nuevo contenido previo a mostrar en clase.

«Semicerrado» significa que el repositorio está listo para uso docente y no tiene bloqueos operativos, pero seguirá admitiendo mejoras cuando una revisión en profundidad o el uso real en aula revele cambios convenientes.

El repositorio reorganizado es utilizable como base docente para el curso 2026-2027. Los pendientes restantes no impiden compartirlo ni utilizarlo: dependen de Moodle, del comienzo real del curso o de futuras mejoras opcionales.

## Estado operativo actual

- [x] Ampliado y publicado en `origin/main` el material de NumPy: guía avanzada `06-numpy-avanzado.md`, broadcasting con ejemplos aplicados, casos prácticos `10-numpy-casos-practicos.md`, notebook canónico `09_numpy_avanzado.ipynb` y taller `10_numpy_casos_practicos.ipynb` (commit `8a81bb4c`); corrección de errata en broadcasting publicada en `d65f9959`. El notebook JAX usa un benchmark moderado para el aula.
- [x] Creada, enlazada desde la portada y publicada la ficha `docs/accesos-rapidos.md` con las direcciones de GitHub Pages y del repositorio del alumnado (commit `8a81bb4c`).
- [x] Preparada la cuarta clase de PIA (NumPy ampliado y JAX). Revisada la teoría y los ejemplos de pandas de UD2: hay material suficiente (`01-pandas-introduccion.md`, `02-pandas-ejemplos-guia.md` y opcionalmente `05-preparacion-datos-ml.md`), así que solo se enlaza como bloque opcional de preparación de datos en el guion si sobra tiempo tras NumPy/JAX, sin crear teoría nueva.

- [x] Actualizado `NOTAS_PROXIMA_SESION.md` como handoff portable para reanudar PIA desde otro ordenador, con el avance real de clase, el plan de mañana, rutas Moodle y decisiones pendientes.
- [x] Cerrada la preparación de la tercera clase de PIA: guion de estructuras adicionales con POO opcional, materiales listos en `Moodle/01-UD1/` y validación de notebooks/build completada. Antes de entrar al aula solo falta confirmar que el notebook de estructuras adicionales está visible en Moodle; los recursos de POO se mantienen ocultos si no se alcanza ese bloque.
- [x] Registrado el resultado real de la segunda clase: cuestionario y ejercicios básicos, hasta estructuras de datos fundamentales. Preparado el guion de la tercera clase, que prioriza `Counter`, `defaultdict` y `deque`, con POO opcional.
- [x] Incorporados al paquete temporal Moodle de UD1 los notebooks de estructuras adicionales, POO y ejercicios de POO; el bloque POO se publica solo si se alcanza en clase.
- [x] Reorientadas las páginas públicas de prácticas y evaluación de UD1 al alumnado; retiradas las rutas internas a material docente y las instrucciones para importar GIFT.
- [x] Incorporada la guía activa de orientación a objetos de Python en UD1, enlazada entre estructuras de datos y NumPy, y referenciada desde UD4 como preparación para PyTorch. Actualizados objetivos, contenidos, actividades, propósito y materiales asociados; añadidos un notebook guiado y un cuaderno de ejercicios, sin modificar código de PyTorch ni materiales sensibles. Publicación selectiva en `origin/main`: `9e921dac`.

- [x] Añadida a la guía de Python de UD1 la trampa práctica de listas y otros valores mutables como parámetros por defecto, con el patrón recomendado de `None`; enlazada desde la ampliación del guion de segunda clase. La corrección de redacción se sincronizó en el repo docente `f9edfd54` y en el público `179592f4`; el PDF regenerado permanece en el paquete Moodle local.
- [x] Preparados tres bancos GIFT adicionales de UD1 (POO, NumPy y EDA, diez preguntas cada uno). Permanecen como fuentes docentes con respuesta correcta; queda pendiente validarlos e importarlos a Moodle cuando se decida activarlos.
- [x] Preparado el guion de la segunda clase de PIA según el avance real: revisión de control de flujo, funciones con parámetros y `return`, y aplicación a listas con una ruta alternativa de refuerzo.
- [x] Ampliada la secuencia de NumPy en UD1: `06-numpy-avanzado.md`, guía de casos `10-numpy-casos-practicos.md`, broadcasting extendido y notebook de casos con muchos ejemplos. El guion de cuarta clase prioriza NumPy/JAX; pandas y R quedan como enganches optativos.
- [x] Preparado y publicado el apéndice optativo de IA clásica en UD11: guía de búsqueda y juegos, ejemplos Python autocontenidos de DFS/BFS/A* y minimax/alfa-beta. Commit privado `be2b1a6d`, publicación en `origin/main` `703f3aa8`; no añade evaluación ordinaria.
- [x] Corregida la estructura de las tres tablas Markdown del guion docente y revisadas las tildes y la ortografía del documento.
- [x] Corregido el separador de tres columnas en la tabla de ritmo principal del guion docente de primera clase.
- [x] Sincronizado el remoto privado `teacher/main` (commit `5582bfca`) y publicada en `origin/main` la presentación del curso y la limpieza de textos docentes en el portal (commit `daca527c`). Se retiraron del árbol público dos notebooks de soluciones y un GIFT con respuestas (commit `5d4b3f29`); los ficheros permanecen en el repositorio privado.
- [x] Ampliado y ubicado en `01-fundamentos-python/99-profesor/GUION_PRIMERA_CLASE_PIA_2026_09_29.md` el guion docente de la primera clase: presentacion del modulo, ritmo principal de dos horas, alternativa si la presentacion llega a 30 minutos, diagnostico inicial, notebook guiado y mini-reto.
- [x] Importado en Moodle el GIFT de diagnostico tecnico inicial de PIA; queda como cuestionario no evaluable y separado del calificador.
- [x] Adaptado el diagnostico inicial de PIA desde el formulario historico: Feedback anonimo para circunstancias y experiencia, GIFT tecnico no evaluable de 20 preguntas sobre Python, IA, ML, DL, LLM, RAG, agentes y modelos locales, y separacion del bloque de Big Data para SBD.
- [x] Reorganizado el paquete temporal de Moodle por unidad en `Moodle/00-UD0/` y `Moodle/01-UD1/`, con documentación de UD1 en PDF y los notebooks en carpetas separadas; `Moodle/` permanece excluida de Git y se regenera desde las fuentes tras borrarla o subirla.
- [x] Regenerado localmente el paquete de documentación de UD1 con 15 PDF mediante Pandoc + XeLaTeX en `Moodle/01-UD1/01-documentacion/`; queda pendiente publicar y comprobar estos recursos en Moodle.
- [x] Revisada la orientacion publica del portal: portada y manual Pixi reescritos para el alumnado; eliminadas referencias a planificacion interna, recursos del profesorado, flujo docente y un portal futuro.
- [x] Preparada la primera clase del 2026-09-29: guion de presentacion de 15-20 minutos y checklist de publicacion inicial de Moodle para UD1 en `00-planificación/`.
- [x] Añadida `docs/presentacion-curso.md` y enlazada desde la portada y la navegación pública; resume ruta, evaluación, entregas, uso de IA y proyecto integrado sin sustituir las normas ni rúbricas detalladas.
- [x] Definida la evaluacion operativa 2026-2027: ponderacion de RA para Seneca, arbol e instrumentos del calificador Moodle y matriz individual RA/CE en `00-planificación/`.
- [x] Las notas de continuidad técnica se separan del estado docente en `NOTAS_PROXIMA_SESION.md`; el fichero recoge la exploración pendiente del grafo Graphify y no sustituye esta hoja de ruta.
- [x] Cerrada la sesión del 2026-08-19 dejando en `NOTAS_PROXIMA_SESION.md` el orden de trabajo recomendado para la siguiente sesión.
- [x] Grafo de conocimiento Graphify generado para el corpus completo de PIA: 2.655 nodos, 3.508 aristas, 332 comunidades y salidas `graphify-out/graph.html`, `graphify-out/graph.json` y `graphify-out/GRAPH_REPORT.md`; el diagnóstico histórico registraba 423 aristas con extremos ausentes; la revisión del JSON actual del 2026-09-30 encuentra cero extremos ausentes en aristas e hiperconexiones. El grafo sigue siendo parcial para los materiales recientes de Moodle y no acredita publicación externa.
- [x] Regenerado desde cero el chunk 03 de Graphify: `graphify-out/.graphify_chunk_03.json` contiene JSON válido y fue parseado tras la escritura (22 nodos, 20 aristas y 3 hiperconexiones; `DEEP_MODE=false`).
- [x] Regenerado desde cero el chunk 04 de Graphify: `graphify-out/.graphify_chunk_04.json` contiene JSON válido y fue parseado tras la escritura (35 nodos, 27 aristas y 3 hiperconexiones; `DEEP_MODE=false`; 22/22 archivos representados).
- [x] Regenerado desde cero el chunk 02 de Graphify: `graphify-out/.graphify_chunk_02.json` contiene JSON válido y fue parseado tras la escritura (41 nodos, 37 aristas y 3 hiperconexiones; `DEEP_MODE=false`).
- [x] Regenerado desde cero el chunk 12 de Graphify: `graphify-out/.graphify_chunk_12.json` contiene JSON válido y fue parseado tras la escritura (55 nodos, 47 aristas y 3 hiperconexiones; `DEEP_MODE=false`).
- [x] Regenerado desde cero el chunk 11 de Graphify: `graphify-out/.graphify_chunk_11.json` contiene JSON válido y fue parseado tras la escritura (54 nodos, 34 aristas y 3 hiperconexiones; `DEEP_MODE=false`).
- [x] Reorganización curricular y documental completada.
- [x] Evaluación transversal normalizada en las unidades activas.
- [x] Material archivado revisado con decisiones explícitas.
- [x] Nomenclatura basada en semanas eliminada de rutas, ficheros y textos activos.
- [x] Verificación final de que no quedan referencias `semana`/`Semana` en materiales activos, excluyendo datos reales, archivos históricos, `99-sensible/` y `site/` generado.
- [x] Rotación de claves API completada.
- [x] UD3 y su capstone quedan utilizables para el curso: dataset reproducible, P2/P3 ejecutados con datos reales y resultados suficientes como evidencia docente, sin continuar optimizando estas prácticas.
- [x] Navegación pública P0 corregida: las 12 páginas de unidad ofrecen destinos reales o estados explícitos para sus 60 secciones, una ruta común de puesta en marcha y una comprobación automática posterior al build.
- [x] Rutas canónicas del alumnado aclaradas y normas comunes de entrega y uso de IA enlazadas desde las actividades evaluables activas de UD1–UD10 y UD12; UD11 queda fuera por ser anexo opcional sin evaluación ordinaria.
- [x] Apéndice de dataset como grafo (Neo4j/Cypher) preparado para aula: apéndice versionado, kit de aula con mini-tarea del alumnado, fixture y bloques Cypher; demo y soluciones como material docente local.
- [ ] Validar los cuestionarios base GIFT de UD1 y UD2 en Moodle; el diagnóstico inicial ya consta como importado. El mantenimiento histórico no se considera un bloqueo actual sin una nueva comprobación.
- [x] Creados y validados sintácticamente los tres cuestionarios GIFT específicos de UD1 (`cuestionario-poo-python.gift`, `cuestionario-numpy.gift` y `cuestionario-eda-numpy.gift`), con 10 preguntas cada uno y contenidos limitados a los materiales activos.
- [ ] Pendiente validar e importar en Moodle los tres cuestionarios GIFT específicos de UD1.
- [x] Ampliado NumPy en UD1 con teoría, broadcasting, ejemplos prácticos y guion docente de cuarta clase. Rutas: `06-numpy-avanzado.md`, `07-broadcasting-numpy.md`, `10-numpy-casos-practicos.md`, notebooks `09_numpy_avanzado.ipynb` y `10_numpy_casos_practicos.ipynb`, más `GUION_CUARTA_CLASE_PIA_UD1.md`. Build y ejecución de notebooks validados; queda pendiente confirmar su publicación en Moodle y la sincronización selectiva a GitHub Pages.
- [x] Cerrado el hueco documental de rendimiento y vectorización de NumPy con `01-fundamentos-python/01-teoria/07-numpy-rendimiento.md`, enlazado como material principal al notebook `06_numpy_rendimiento.ipynb`. Queda pendiente únicamente validar y publicar el material en Moodle.

## Revisión de `00-planificación` — 2026-08-20

- [x] Examinados `README.md`, inventarios, comparativa multicurso, plantillas y radar de avances de IA.
- [x] Confirmado que los pendientes de los inventarios y de la sección «Pendientes antes de reorganizar» son registros históricos de la fase previa; no describen tareas abiertas del árbol reorganizado.
- [x] Contrastadas las decisiones que allí figuraban como pendientes: estructura final de 12 unidades, archivo de material antiguo, MCP, Lab3, evaluación, proyecto integrado y eliminación de la nomenclatura por semanas ya están resueltos en el repositorio activo.
- [x] No se detecta ninguna modificación adicional necesaria para cerrar la reorganización.
- [x] `mkdocs build --strict` supera la comprobación actual.

La carpeta `00-planificación` se conserva como archivo de trazabilidad y material de planificación. El radar de avances y las plantillas siguen siendo instrumentos vivos, pero su mantenimiento no constituye deuda de reorganización.

## Completado

- Estructura general reorganizada en 12 unidades:
  1. `01-fundamentos-python/`
  2. `02-tratamiento-datos/`
  3. `03-machine-learning/`
  4. `04-deep-learning/`
  5. `05-cloud-mlops/`
  6. `06-llm-agentes/`
  7. `07-convergencia-herramientas/`
  8. `08-vision-xai/`
  9. `09-gpu-avanzado/`
  10. `10-series-temporales/`
  11. `11-anexos/`
  12. `12-proyecto-integrado/`
- UD7 completada, verificada y archivada vía OpenSpec.
- Documentación del proyecto integrado completada:
  - guía del proyecto final;
  - evaluación;
  - mapa de mini-proyectos;
  - checkpoints;
  - banco de ejemplos;
  - FAQ.
- Proyecto integrado reorientado a mini-proyectos progresivos y proyecto final libre con al menos dos fuentes de datos.
- Plantillas transversales añadidas:
  - declaración de uso de IA;
  - normas de trabajo en equipo, coevaluación y entregas.
- Publicadas en el portal las normas comunes para todas las actividades con entrega: penalización gradual por retraso, fecha de cierre, excepciones, evidencias del proceso con IA, verificación independiente y responsabilidad sobre el resultado.
- Ficheros sensibles movidos a `99-sensible/`, sustitución de claves reales por placeholders en materiales revisados y exclusión activa en `.gitignore`.
- Verificado que no quedan claves reales fuera de `99-sensible/` en la revisión realizada.
- Creada la estructura base de evaluación para UD1 y UD2 en `04-evaluacion/`.

## Rotación de claves API

- [x] **OpenAI** — marcada como rotada por el usuario el 2026-07-02.
  - Origen documentado: `99-sensible/openAI-API-Key.txt`
  - Origen documentado: `99-sensible/OPENAI_API_KEY_desde_notebook.txt`
- [x] **Hopsworks** — marcada como rotada por el usuario el 2026-07-02.
  - Origen documentado: `99-sensible/hopsWorks-API-KEY.txt`
- [x] **PageIndex** — marcada como rotada por el usuario el 2026-07-02.
  - Origen documentado: `99-sensible/PageIndex-ApiKey.txt`

## Pendientes críticos

- [x] **Rotar claves API extraídas.** OpenAI, Hopsworks y PageIndex quedan marcadas como rotadas.

## Pendientes importantes

- [x] **Reabrir UD4 (Deep Learning) para saneamiento estructural.** Cerrado operativamente el 2026-07-06: teoría separada, visión movida a UD8, NLP/Transformers a UD6, series temporales a UD10, proyectos tabulares decididos, recursos revisados, evaluación alineada y `mkdocs build --strict` validado.
- [ ] Validar en Moodle los cuestionarios base GIFT de UD1 y UD2; no confundirlos con el diagnóstico inicial ya importado.
- [x] Revisar ZIPs archivados reales con decisión explícita: conservar, mover, documentar o descartar (completado 2026-06-28).
- [x] MCP queda incorporado a UD6 como contenido activo integrado en prácticas, documentación y evaluación. El refuerzo MCP de `06-llm-agentes/05-recursos/mcp-refuerzo/` se mantiene como material opcional condicionado al test inicial; el material antiguo de `06-llm-agentes/90-archivo/MCP-24-25/` queda como histórico.
- [x] Revisar materiales de archivo (`90-archivo/` y `90-archivo-historico/`) antes de distribuirlos al alumnado (completado 2026-06-28).
- [x] Convertir el pendiente genérico de legacy disperso en decisiones por ruta concreta antes de mover o eliminar material (completado 2026-06-28).
- [x] Confirmar si conviene desarrollar el Lab3 de dataset propio en UD3 para igualarlo a Lab1/Lab2 (Lab3 ya existe y está completo).

## Mejoras opcionales

- [x] Revisar H5P históricos solo si se recupera material externo: no quedan ficheros `.h5p` en el repositorio.
- [x] UD6 (LLM/Agentes): crear rúbricas e instrucciones de entrega (completado 2026-06-29)
- [x] UD8 (Visión/XAI): crear evaluación y rúbricas (completado 2026-07-01)
- [x] UD10 (Series Temporales): crear enunciados, rúbricas e instrucciones de entrega (completado 2026-07-01)
- [x] UD4 (DL): extraer rúbricas a 04-evaluacion/ + crear GIFT (completado 2026-07-01)
- [x] Añadir 04-evaluacion/README.md a unidades que faltan (completado 2026-07-01)
- [x] Unificar checklists de entrega en unidades distribuidas (completado 2026-07-01)
- [x] Eliminar nomenclatura de semanas en materiales activos y sustituirla por bloques, temas o fases (completado 2026-07-02).

## Próximas acciones sugeridas

1. En la próxima sesión, abrir en `teacher` y revisar el contenido de los tres archivos retirados de `origin/main`: `03-machine-learning/03-practicas/midterm-capstone/Peliculas/Practica_Peliculas_OK/notebooks/profesor/P2_PyCaret_sol.ipynb`, `03-machine-learning/03-practicas/midterm-capstone/Peliculas/Practica_Peliculas_OK/notebooks/profesor/P3_Modelo_sol.ipynb` y `06-llm-agentes/02-ejemplos/nlp-transformers-ud4/tareas/Transformers_Test_Moodle.gift`; después decidir si se solicita la purga del historial público. Los archivos siguen recuperables en commits anteriores y purgarlos requiere reescribir historial y coordinar clones.
2. Confirmar qué recursos iniciales están realmente visibles en Moodle y decidir si se suben los 15 PDF de UD1 preparados, incluidos POO y NumPy/JAX; comprobar también qué notebooks de UD1 están publicados y probar el acceso con una cuenta de estudiante. No marcar como publicados los archivos que solo estén preparados.
3. Configurar y verificar en Seneca los pesos RA/CE de `00-planificación/PONDERACION_RA_SENECA_2026_2027.md`.
4. Montar y comprobar con una cuenta de prueba el curso plantilla Moodle según `00-planificación/CONFIGURACION_CALIFICADOR_MOODLE_2026_2027.md`; validar los GIFT base de UD1/UD2 y decidir cuándo importar los cuestionarios adicionales de POO, NumPy y EDA. El diagnóstico inicial ya está registrado como importado.
5. Antes de evaluar al primer grupo, duplicar `00-planificación/plantilla_seguimiento_ra_ce.csv` por alumno y realizar una prueba con dos evidencias ficticias.
6. Realizar las comprobaciones Windows/macOS de Pixi y de los ejemplos que se vayan a usar cuando haya equipos disponibles.
7. El día que se imparta el apéndice de grafos: arrancar el contenedor Neo4j, cargar el fixture y repasar los resultados esperados de `demo-profesor.md`.
8. Profundizar o adaptar prácticas concretas solo si el uso durante el curso revela una necesidad docente real.

## Agenda de la próxima sesión — NumPy/JAX

1. Antes de clase, confirmar que los notebooks `09_numpy_avanzado.ipynb`, `10_numpy_casos_practicos.ipynb` y `08_introduccion_jax_comparativa.ipynb` están accesibles en Moodle.
2. Comprobar si está disponible el entorno `pia-ud1` con JAX. Si no, no instalar dependencias durante la sesión: completar NumPy y dejar JAX para otra ocasión.
3. Priorizar ejes, máscaras, broadcasting aplicado y los ejemplos de distancia/normalización del taller. JAX después; si sobra tiempo, elegir solo un enganche entre pandas y R.
4. Tras la clase, anotar lo realmente trabajado y ajustar el paquete Moodle. Confirmar aparte visibilidad de los 15 PDF y estado del cuestionario base.

## Pendiente de seguridad del repositorio público

Decidir, tras revisar su contenido, si se solicita la purga del historial de los tres archivos docentes retirados de `origin/main`; hacerlo reescribe el historial y requiere coordinación de clones. No purgar sin decisión expresa.
5. Preparar el inicio de SBD con el método de PIA: primero revisar el estado del repo, la presentación y los guiones existentes; después ajustar la clase de dos horas y organizar los materiales Moodle por unidad, conservando el paquete como preparación temporal excluida de Git.


## Continuación — 2026-07-21 (normas comunes de entrega y uso de IA)

### Hecho

- Creado `docs/normas-entregas-y-uso-de-ia.md` como norma transversal, pública y versionada para todas las actividades con entrega.
- Definida una penalización calculable del 5 % de la calificación obtenida por cada periodo de 24 horas iniciado, hasta el cierre ordinario a los siete días.
- Reguladas las excepciones justificadas y las condiciones especiales de cierre.
- Diferenciada la evidencia del proceso cuando se utiliza SDD de la selección representativa de prompts cuando no se utiliza, sin exigir conversaciones completas.
- Exigida verificación independiente mediante pruebas, casos límite, fuentes, métricas, seguridad, privacidad, licencias y declaración de limitaciones, según corresponda.
- Enlazadas las normas desde la portada pública `docs/index.md`.

### Estado

- [x] Enlazadas las normas desde los enunciados o instrucciones canónicas de todas las unidades con evaluación ordinaria activa (UD1–UD10 y UD12). UD11 se excluye deliberadamente: su única actividad evaluable es opcional y permanece archivada.

### Siguiente paso recomendado

Mantener un único recordatorio enlazado en cada ruta evaluable canónica y evitar duplicar la política completa.

## Continuación — 2026-07-22 (auditoría de `environment.yml`)

### Resultado

- Auditado `environment.yml` frente a los imports y dependencias de los materiales activos.
- Se confirma que contiene un núcleo útil, pero **no es todavía un entorno único completo y reproducible para todo el curso**.
- Faltan dependencias de varias unidades (`fastapi`, `uvicorn`, `streamlit`, `flask`, `xgboost`, `scikeras`, `opencv`, `pillow`, `pyarrow`, `pandera`, `mlflow`, `shap`, `python-dotenv`, entre otras).
- `pytorch-cuda=13.0` se considera demasiado específico para el entorno común y `pandas>=3.0` requiere revisar compatibilidad con proyectos concretos.

### Siguiente paso recomendado

Reestructurar el entorno en una base común reproducible y extras por unidad/GPU antes de incorporarlo como receta completa del curso.

## Continuación — 2026-07-22 (piloto Pixi)

### Resultado

- Instalado Pixi `0.73.0` y creado un prototipo aislado fuera del repositorio.
- Comprobada la composición de un entorno base (`default`) y otro con una feature adicional (`ud3`), usando `pixi.toml`, `pixi.lock` y `pixi run --environment`.
- El modelo de features funciona correctamente, pero cada entorno instalado mantiene su propio prefijo: en el piloto `default` ocupó aproximadamente 279 MB y `ud3` 210 MB, con unos 99 MB adicionales de caché compartida.

### Decisión provisional

Pixi mejora la organización y reproducibilidad de variantes, pero **no garantiza por sí solo un ahorro grande de disco** si se instalan muchos entornos simultáneamente. Esta hipótesis quedó contrastada con el piloto de `uv` documentado a continuación.

### Siguiente paso recomendado

Comparación con `uv` realizada; la decisión provisional actualizada queda documentada en el bloque siguiente.

## Continuación — 2026-07-22 (piloto uv)

### Resultado

- Probado `uv 0.5.20` en un proyecto aislado con Python 3.12, NumPy y el grupo `ud3` con scikit-learn.
- `uv sync --no-group ud3` y `uv sync --group ud3` reutilizan el mismo `.venv`; no crean un entorno adicional.
- El entorno pasó de aproximadamente 62 MB con la base a 208 MB con `ud3`, y volvió a 62 MB al retirar el grupo.
- El mismo intérprete se mantuvo durante los cambios de grupos.

### Decisión provisional

El usuario confirma que unos cientos de megabytes no son un problema; por tanto, el criterio principal pasa a ser el aislamiento y la compatibilidad con paquetes Conda/nativos y variantes CPU/GPU. Con ese criterio, Pixi queda como candidato preferente, aunque falta probar una estructura más próxima al curso real.

### Siguiente paso recomendado

Diseñar un prototipo PIA con `pixi.toml` y features `default`, `ud3`, `ud4` y `gpu`, y preparar un manual breve de Pixi si la prueba resulta satisfactoria. Mantener `uv` documentado como alternativa evaluada.

## Continuación — 2026-07-23 (manual inicial de Pixi)

### Hecho

- Creado `docs/manual-pixi-pia.md` como guía docente para personas que no han usado Pixi.
- Documentados instalación, conceptos, comandos, features, entornos, CPU/GPU, VS Code/Jupyter, resolución de problemas y buenas prácticas de versionado.
- Añadido un diseño piloto PIA con `default`, `ud3`, `ud4` y `gpu`, dejando explícito que todavía no es una migración real.
- Enlazado el manual desde `docs/index.md`.

### Siguiente paso recomendado

Probar el diseño del manual con las dependencias reales del curso y verificar un clon limpio antes de decidir si se sustituye `environment.yml`.

## Continuación — 2026-07-25 (prototipo Pixi del repositorio)

### Hecho

- Creado `pixi.toml` como prototipo versionable del entorno PIA.
- Definida una base común `default` con Python 3.12, NumPy, pandas, SciPy, JupyterLab e IPykernel.
- Añadidas las features `ud3` (scikit-learn y XGBoost), `ud4` (PyTorch y TorchVision) y `gpu` como marcador sin paquetes de hardware obligatorios.
- Definidos los entornos combinables `default`, `ud3`, `ud4` y `ud4-gpu`.
- Excluidos `.pixi/` y cachés locales de Pixi en `.gitignore`; `pixi.toml` y `pixi.lock` quedan versionables.
- Resueltos e instalados en Linux los entornos `default`, `ud3`, `ud4` y `ud4-gpu` con Pixi 0.73.0; las comprobaciones de imports básicos, ML clásico y PyTorch/TorchVision funcionan.
- Generado `pixi.lock` y verificado que está actualizado.

### Queda pendiente

- Probar el mismo lockfile en un clon limpio y en las plataformas objetivo.
- Comprobar la disponibilidad y compatibilidad de PyTorch/TorchVision en CPU y de la variante GPU por plataforma.
- Comparar las dependencias del prototipo con todos los imports activos del curso y añadir extras por unidad que falten.
- Decidir, después de esas pruebas, si `pixi.toml` sustituye oficialmente a `environment.yml`.

### Siguiente paso recomendado

Validar el lockfile en un clon limpio y revisar si conviene mantener `ud4-gpu` separado: con la feature GPU todavía vacía, ese entorno reproduce el prefijo de `ud4` sin aportar una variante real.

## Continuación — 2026-07-25 (auditoría de documentación Poetry)

### Resultado

- Confirmada documentación activa de Poetry en UD3, no solo restos históricos:
  - `03-machine-learning/01-teoria/10-guia-proyecto-python-poetry.md`;
  - sección extensa sobre Poetry en `03-machine-learning/01-teoria/06-guia-creacion-datasets-propios.md`;
  - guías de FastAPI y Streamlit;
  - laboratorios de creación de datasets con `pyproject.toml` y `poetry.lock`;
  - rúbrica de datasets que evalúa el uso de Poetry.
- También hay referencias opcionales a Poetry en UD9 y en varios checklists/propuestas de entornos reproducibles.

### Estado posterior

La decisión ya está tomada: Pixi es el gestor operativo del módulo y Poetry queda solo como contexto mínimo de empaquetado. Lab1 validó la migración; la tarea pendiente es sustituir gradualmente las restantes guías operativas que aún presenten Poetry como flujo práctico.

## Continuación — 2026-07-25 (decisión Poetry/Pixi)

### Decisión provisional

- Pixi será el gestor operativo principal de entornos y dependencias del módulo.
- Poetry se reducirá a una referencia mínima sobre empaquetado/proyectos Python; no será el flujo recomendado para las prácticas.
- No se mezclarán dos gestores de dependencias dentro del mismo proyecto: primero se migrará y probará un laboratorio real de UD3 antes de retirar sus instrucciones de Poetry.

### Pendiente real

- Sustituir progresivamente las demás guías y rúbricas operativas que aún presenten Poetry como flujo de trabajo.

### Siguiente paso recomendado

Validar el piloto de Lab1 con claves reales en Linux/WSL2 y, cuando sea posible, en Windows y macOS.

## Continuación — 2026-07-25 (auditoría Lab1 Poetry)

### Resultado

- El laboratorio `03-machine-learning/03-practicas/laboratorios/Lab1/mi_dataset_peliculas/` usa realmente `requests`, `pandas` y `python-dotenv`.
- Su `pyproject.toml` declara erróneamente también `dotenv` y exige Python `>=3.14`, mientras el entorno PIA objetivo es Python 3.12.
- Las dos guías `CreacionDataset.md` y `CreacionDataset (1).md` duplican contenido y contienen instrucciones Poetry divergentes; una usa ejemplos con Polars que no coinciden con el código real.
- El laboratorio no necesita publicar un paquete para ser evaluable; el problema principal es ejecutar el código de forma reproducible desde `src/`.

### Estado

El piloto ya se migró y consolidó en `ded163ba` (`docs(ud3): migrate dataset lab to Pixi`). La retirada de sus metadatos Poetry se ha decidido tras validar el flujo reproducible de Pixi; quedan las pruebas funcionales con las API y en las plataformas objetivo.

## Continuación — 2026-07-25 (migración inicial de Lab1 a Pixi)

### Hecho

- Añadida la feature Pixi `ud3-datasets`, combinada en el entorno `ud3-datasets` con `default` y `ud3`.
- Añadidas `requests` y `python-dotenv` y una tarea `lab1-dataset` que ejecuta el módulo desde el directorio correcto, conservando los imports relativos.
- Unificadas las guías `CreacionDataset.md` y `CreacionDataset (1).md`; la segunda queda como redirección de compatibilidad.
- Eliminadas de estas guías las instrucciones operativas de Poetry y sustituidas por comandos Pixi reproducibles.
- Generado y validado `pixi.lock`; el entorno `ud3-datasets` instala e importa `requests`, `python-dotenv` y `pandas` correctamente en Linux.
- Consolidado y sincronizado en `ded163ba` (`docs(ud3): migrate dataset lab to Pixi`).

### Pendiente real

- Validar la tarea en Windows y macOS, incluida la activación de `PYTHONPATH`; Linux nativo ya ejecutó la tarea completa con las API reales.

### Siguiente paso recomendado

Cuando haya acceso a Windows o macOS, ejecutar `pixi install` y `pixi run --environment ud3-datasets lab1-dataset` con claves propias, comprobando el CSV resultante.

## Continuación — 2026-07-25 (retirada de Poetry en Lab1)

### Hecho

- Retirados `pyproject.toml` y `poetry.lock` de `Lab1/mi_dataset_peliculas/`: el laboratorio no se publica como paquete y Pixi ya aporta dependencias, lockfile y tarea de ejecución reproducible.
- Actualizadas la guía, el README y la rúbrica de datasets para usar Pixi como única ruta operativa y evaluar reproducibilidad, no una herramienta concreta de empaquetado.
- Comprobado `pixi lock --check` y eliminadas las referencias documentales activas a Poetry en Lab1 y su rúbrica.
- Ejecutada la tarea completa con claves reales de TMDB y OMDb en Linux: `pixi run --environment ud3-datasets lab1-dataset` finalizó correctamente y generó el dataset.

### Pendiente real

- Repetir la validación cuando haya equipos Windows y macOS disponibles; Linux nativo ya está comprobado con las API reales.

### Siguiente paso recomendado

Cuando haya acceso a Windows o macOS, ejecutar `pixi install` y `pixi run --environment ud3-datasets lab1-dataset` con claves propias, comprobando la activación de `PYTHONPATH` y el CSV resultante.

## Continuación — 2026-07-28 (P3 capstone: flujo anti-fuga)

### Hecho

- Reforzadas la guía y las plantillas de P3 para separar entrenamiento y test antes de todo transformador aprendido.
- Establecido `train_test_split(..., test_size=0.20, random_state=42, stratify=y)`, `ColumnTransformer` y `Pipeline` con imputación, codificación y escalado.
- Limitado `GridSearchCV(cv=5)` a `X_train` e `y_train`, reservando `X_test` para una única evaluación final con métricas y análisis de errores.
- Actualizadas las plantillas de alumnado y profesorado sin inventar resultados de ejecución.

### Pendiente real

- Ejecutar P3 con el dataset concreto antes de su uso en aula para comprobar que la selección de columnas, la variable objetivo y las versiones de dependencias encajan con los datos finales.

### Siguiente paso recomendado

Validar la plantilla P3 en ejecución con un dataset de películas disponible, sin alterar la regla de reservar el test hasta el final.

## Continuación — 2026-07-25 (matriz de plataformas Pixi)

### Decisión de diseño

- El prototipo Pixi debe contemplar cuatro familias de plataforma:
  - `linux-64`: Linux nativo y WSL2;
  - `win-64`: Windows nativo;
  - `osx-64`: macOS Intel;
  - `osx-arm64`: macOS Apple Silicon.
- WSL2 se tratará como Linux para Pixi, no como una quinta plataforma.
- Las dependencias GPU se mantendrán en features/targets específicos; no se instalarán en la base común.
- macOS y equipos Windows/Linux sin GPU deben conservar una ruta CPU funcional.

### Siguiente paso recomendado

Añadir al piloto de UD3 la matriz de plataformas y probar primero el laboratorio en Linux/WSL2 y Windows; después revisar macOS y la variante GPU por separado.


## Continuación — 2026-07-06 (seguimiento de curso)

### Hecho

- Creado `SEGUIMIENTO_CURSO_PIA.xlsx` como libro operativo de aula con hojas para:
  - seguimiento de impartición por unidad, bloque, estado, fechas, sesiones y observaciones;
  - catálogo de actividades detectadas en `03-practicas/` y `04-evaluacion/`;
  - registro de entregas, corrección, notas, pesos y nota ponderada por alumno;
  - resumen de medias y pendientes de corrección por alumno.
- Creada la guía `SEGUIMIENTO_CURSO_PIA.md` con el criterio de uso y mantenimiento.
- Añadida excepción en `.gitignore` para versionar `SEGUIMIENTO_CURSO_PIA.xlsx`, igual que la hoja de trazabilidad RA/CE.

### Queda pendiente

- Rellenar alumnado, grupos, pesos reales y fechas cuando comience el curso.
- Revisar el catálogo si se añaden, eliminan o renombran prácticas antes de usarlo en aula.

### Siguiente paso recomendado

Validar visualmente el libro en LibreOffice/Excel y ajustar pesos reales de las actividades evaluables antes de iniciar el seguimiento con alumnado.


## Continuación — 2026-07-06 (seguimiento por CE)

### Hecho

- Ajustado `SEGUIMIENTO_CURSO_PIA.xlsx` para que la práctica sea contenedor de evidencias y la calificación operativa se registre por CE:
  - añadida hoja `Registro_CE` para una fila por alumno, actividad y criterio de evaluación;
  - añadida hoja `Resumen_CE` para medias por alumno y CE;
  - añadida hoja `RA_CE` como referencia directa de RA/CE;
  - `Registro_Notas` queda como apoyo interno, no como fuente principal de calificación oficial.
- Actualizada `SEGUIMIENTO_CURSO_PIA.md` con el flujo recomendado: primero CE previstos por actividad, después notas por CE.
- Actualizada `TRAZABILIDAD_CALIFICACIONES_RA_CE.md` para aclarar que la propagación de nota global es una simplificación y que el seguimiento defendible por CE está en `Registro_CE`.

### Queda pendiente

- Revisar visualmente el libro y completar los CE previstos reales por actividad.
- Decidir pesos reales de CE cuando una práctica cubra varios criterios.

### Siguiente paso recomendado

Abrir el libro en LibreOffice/Excel y hacer una prueba con 2 alumnos ficticios y 2 actividades para comprobar que el flujo por CE resulta cómodo antes de meter datos reales.


## Continuación — 2026-07-06 (prueba CE ficticia)

### Hecho

- Añadida la hoja `Prueba_CE` a `SEGUIMIENTO_CURSO_PIA.xlsx` con 2 alumnos ficticios y 2 actividades:
  - una actividad reparte peso entre `RA2.c` y `RA2.e`;
  - otra actividad cubre `RA1.d`;
  - incluye fórmulas de nota ponderada, media por CE, suma ponderada y conteo de evidencias.
- Actualizada `SEGUIMIENTO_CURSO_PIA.md` para explicar que `Prueba_CE` es el ejemplo de comprobación antes de meter datos reales.

### Resultado de la prueba

- El modelo permite registrar una misma práctica como contenedor de varios CE.
- Las notas quedan consultables por alumno y CE, sin depender de una única nota global de tarea.

### Siguiente paso recomendado

Abrir visualmente la hoja `Prueba_CE` en LibreOffice/Excel y confirmar si el flujo resulta cómodo; después completar CE previstos y pesos reales en `Actividades`.


## Continuación — 2026-07-07 (revisión cobertura Real Decreto)

### Hecho

- Verificada la fuente normativa principal: Real Decreto 279/2021, BOE-A-2021-7686, módulo 5073 Programación de Inteligencia Artificial.
- Creada `REVISION_COBERTURA_REAL_DECRETO_PIA.md` con revisión específica de RA/CE, contenidos básicos y comparación secundaria con índices editoriales.
- Actualizada `TRAZABILIDAD_LEGAL_PIA.md` para enlazar la revisión detallada y dejar clara la fuente normativa.

### Resultado

- El curso queda cubierto frente a RA/CE, especialmente RA2.
- Los riesgos reales son documentales: RA1.b/c/f, RA3.d/e y RA4.a/b/d necesitan evidencias más explícitas.
- La comparación con libros queda como apoyo secundario; el criterio principal es el Real Decreto.

### Siguiente paso recomendado

Implementar las evidencias mínimas de blindaje: sección empresarial obligatoria en UD12/proyecto final, evidencia de convergencia-seguridad-decisión en UD7 y comparativa de lenguajes/formatos en UD1/UD2.


## Continuación — 2026-07-07 (RA1 lenguajes y formatos)

### Hecho

- Implementada la evidencia mínima de RA1.b/c/d/e/f detectada en la revisión del Real Decreto:
  - creada `01-fundamentos-python/04-evaluacion/comparativa-lenguajes-formatos-ia.md`;
  - enlazada desde `01-fundamentos-python/README.md`;
  - enlazada desde `01-fundamentos-python/01-teoria/README.md`;
  - documentada en `01-fundamentos-python/04-evaluacion/README.md`.
- Actualizadas `TRAZABILIDAD_LEGAL_PIA.md` y `REVISION_COBERTURA_REAL_DECRETO_PIA.md` para marcar RA1.b/c/f como cubiertos explícitamente.
- Añadida la nueva actividad a `SEGUIMIENTO_CURSO_PIA.xlsx` con CE previstos `RA1.b`, `RA1.c`, `RA1.d`, `RA1.e` y `RA1.f`.

### Queda pendiente

- UD12: añadir evidencia obligatoria de negocio, automatización, usuarios, recursos, riesgos y conveniencia del modelo.
- UD7: añadir evidencia de convergencia tecnológica, seguridad y toma de decisiones.

### Siguiente paso recomendado

Continuar mañana por UD12 o UD7; si se busca mayor impacto legal, empezar por UD12 porque concentra RA4.a/b/d y puede servir también para RA3.e.


## Cierre de sesión — 2026-07-07

### Estado guardado

- Revisión del Real Decreto realizada y subida.
- Evidencia RA1 de lenguajes y formatos implementada, validada y subida.
- Repositorio sincronizado con `origin/main` tras el último push.

### Pendientes para retomar

1. **UD12 / Proyecto integrado**: añadir evidencia obligatoria de negocio, automatización, usuarios/clientes, datos como activo, recursos, riesgos, alternativa descartada y conveniencia del modelo. Prioridad recomendada porque cubre RA4.a/b/d y ayuda a RA3.e.
2. **UD7 / Convergencia de herramientas**: añadir evidencia de convergencia tecnológica, seguridad en negocio y toma de decisiones estratégicas.
3. Revisar visualmente `SEGUIMIENTO_CURSO_PIA.xlsx`, especialmente `Prueba_CE`, en LibreOffice/Excel.
4. Probar ejecución completa de los `.Rmd` del itinerario R con paquetes concretos (`dplyr`, `ggplot2`, `tibble`, `lubridate`, `rmarkdown`, `knitr`).
5. Validar GIFT en Moodle cuando la plataforma esté disponible.

### Siguiente paso recomendado

Empezar por UD12: es el refuerzo con mayor valor legal y pedagógico pendiente.

## Historial previo (2026-06-27 a 2026-06-28; sustituido por el estado y pendientes posteriores)

**Fecha:** 2026-06-27

### Estado de la tarea

- Ya está creada la base de evaluación de UD1 y UD2 con `README.md`, `rubrica.md`, `cuestionario-base.gift` y `checklist-entrega.md`.
- `ESTADO_ACTUAL_Y_PENDIENTES.md` actualizado con el avance y con pendientes depurados.

### Siguientes pasos concretos

1. Rotar claves API expuestas.
2. Validar los GIFT actuales de UD1 y UD2 en Moodle cuando la plataforma vuelva a estar disponible.
3. Crear una tabla de decisión para ZIPs y material archivado real antes de publicar.
4. Revisar H5P históricos solo si se recupera material externo.

## Continuación — 2026-06-28 (tarde)

### Hecho hoy

- Revisados y decididos los 7 lotes de material archivado en `DECISIONES_MATERIAL_ARCHIVADO.md`:
  1. `NumPy-20251016.zip` → Conservar como histórico
  2. `snake-rl-*` → Canónica (`materiales_actualizado` + `completo_con_env`); resto histórico
  3. `office/` → Conservar como histórico (todo ya extraído a Markdown)
  4. `actividades-rl/` → Mantener como refuerzo opcional; referenciado desde `11-anexos/README.md`
  5. `teoria-html/` → Descartar (HTML desactualizados; contenido canónico en Markdown)
  6. `fundamentos-old/` → Mixto (descartados duplicados; conservados `.org` fuente y scripts únicos)
  7. `sem25-old/` → Mixto (descartados Polars y guía; conservados cuDF y comparativa como históricos; unificadas soluciones en SOLUCIONES_TESTS)
- Renombradas las guías antiguas de UD9 y UD8 a nombres basados en bloques.
- Eliminados HTML duplicados en UD3 (teoria-html) y UD5 (teoría).
- Ejecutada la limpieza física de archivos marcados para descartar.
- Verificado que Lab3 de UD3 ya existe y está completo.
- Confirmado que no quedan ficheros `.h5p` en el repositorio.
- Los GIFT de UD1 y UD2 están corregidos y listos para importar a Moodle.
- **Revisión curricular completa de UD3 a UD12:**
  - ✅ UD3 (ML): completa
  - ✅ UD4 (DL): completa (rúbricas embedidas en labs)
  - ✅ UD5 (Cloud/MLOps): completa; eliminados HTML duplicados
  - ✅ UD6 (LLM/Agentes): completa
  - ✅ UD7 (Convergencia): archivada
  - ✅ **UD8 (Visión/XAI): teoría creada desde cero** (índice + 3 docs: segmentación, tracking, XAI) + recursos + guías renombradas
  - ✅ **UD9 (GPU): notebooks reubicados a ejemplos + GIFT creado**
  - ✅ **UD10 (Series Temp.): GIFT creado**
  - ✅ UD11 (Anexos): ok
  - ✅ UD12 (Proy. Integrado): ok

### Queda por hacer

- **Rotar claves API**: OpenAI, Hopsworks y PageIndex completadas.
- **Validar GIFT en Moodle** — aplazado hasta que termine el mantenimiento de Moodle.
- **Revisión transversal**: verificar que todas las tareas/prácticas tengan fichero de entrega con formato, evidencias requeridas y referencia a la rúbrica.

### Siguiente paso recomendado

Revisión transversal de fichas de entrega, rúbricas y evidencias en todas las unidades.

## Continuación — 2026-06-29 (mañana)

### Hecho hoy

- Auditoría transversal completa de todas las unidades (01-12, 99-sensible).
- Identificadas carencias críticas en UD6, UD8 y UD10 (sin rúbricas ni instrucciones de entrega).
- UD4 tiene rúbricas pero en laboratorios, no en `04-evaluacion/`.
- Solo UD1 y UD2 tienen `04-evaluacion/` completo (README + checklist + rúbrica + GIFT).
- Resultados detallados documentados en el plan de trabajo de la sesión.

### Queda por hacer (priorizado)

1. **UD8 (Visión/XAI)**: crear evaluación y rúbricas
2. **UD10 (Series Temporales)**: crear enunciados, rúbricas e instrucciones de entrega
3. UD4: extraer rúbricas a `04-evaluacion/` + GIFT
4. Añadir `04-evaluacion/README.md` a unidades 03-12
5. Unificar checklists en unidades distribuidas
6. Rotar claves API + validar GIFT en Moodle (usuario)

### Siguiente paso

Continuar por UD8: crear evaluación y rúbricas.

## Continuación — 2026-06-29 (UD6)

### Hecho

- Creada la evaluación de UD6 en `06-llm-agentes/04-evaluacion/`:
  - `README.md`
  - `rubrica.md`
  - `checklist-entrega.md`
- La rúbrica queda sobre 10 puntos y cubre funcionamiento, reproducibilidad, prompts/pipeline, RAG/agentes, serving/API/interfaz, trazabilidad, documentación y seguridad.
- Los cuestionarios GIFT existentes se mantienen como evaluación conceptual/complementaria.
- MCP queda tratado como contenido integrado y el refuerzo MCP sigue siendo opcional, no dependencia obligatoria.

### Siguiente paso

Crear evaluación y rúbricas de UD8.

## Registro breve de decisiones

- **Estructura de unidades:** se adopta una organización numerada con nombres descriptivos.
- **UD7:** queda completada, verificada y archivada; no se reabre salvo revisión puntual.
- **F6 de UD7:** se define como LlamaIndex con indexación jerárquica, caso ParkingCorp y CrewAI; no como RAG plano con ChromaDB.
- **Orquestación:** Prefect es la referencia principal; Airflow queda como comparación contextual.
- **Proyecto integrado:** se articula mediante mini-proyectos y proyecto final libre, progresivo, con al menos dos fuentes de datos.
- **Uso de IA y equipos:** se añaden plantillas transversales para declaración de uso de IA, normas de equipo, coevaluación y entregas.
- **Seguridad:** los ficheros sensibles se concentran en `99-sensible/` y están excluidos de Git; queda pendiente rotar las claves API extraídas.
- **MCP en UD6:** MCP queda como contenido activo integrado, no como bloque obligatorio independiente; el refuerzo se mantiene como opcional y el material antiguo como histórico.
- **Evaluación UD1/UD2:** el pendiente ya no es importar histórico, sino validar en Moodle los GIFT actuales.
- **UD8 (Visión/XAI):** teoría desarrollada desde cero (índice + segmentación, tracking, XAI). Evaluación completada 2026-07-01.

## Continuación — 2026-07-01

### Hecho hoy

- Creada la evaluación completa de UD8 en `08-vision-xai/04-evaluacion/`:
  - `README.md`: descripción de qué se evalúa, evidencias esperadas y relación con notebooks 78-86.
  - `rubrica.md`: rúbrica sobre 10 puntos con 5 criterios (funcionamiento, métricas, visualizaciones, análisis, documentación). Adaptable a entregas parciales de uno o dos bloques.
  - `checklist-entrega.md`: checklist con evidencias mínimas por bloque (segmentación, tracking, XAI).
  - `cuestionario-vision-xai.gift`: 18 preguntas GIFT repartidas en 3 bloques (segmentación 1-6, tracking 7-12, XAI 13-18).

### Siguiente paso

Crear evaluación y rúbricas de UD10 (Series Temporales).

## Continuación — 2026-07-01 (UD10)

### Hecho

- Creada la evaluación de UD10 en `10-series-temporales/04-evaluacion/`:
  - `README.md`: descripción de qué se evalúa, fases del proyecto (Retail, Energía, Torneo) y relación con notebooks 01-10.
  - `rubrica.md`: rúbrica sobre 10 puntos con 7 criterios (fusión/preprocesado, partición temporal/data leakage, baseline+métricas, modelo avanzado, tabla comparativa del Torneo, análisis, documentación).
  - `checklist-entrega.md`: checklist con evidencias mínimas por fase y comprobaciones específicas de series temporales (escaladores, fuga temporal, partición).
  - El `cuestionario_series_temporales.gift` ya existía y se mantiene.

### Siguiente paso

UD4 (DL): extraer rúbricas embedidas en labs a `04-evaluacion/` + crear GIFT.

## Continuación — 2026-07-01 (UD4)

### Hecho

- Creada la evaluación de UD4 en `04-deep-learning/04-evaluacion/`:
  - `README.md`: descripción de los 3 labs con pesos (Lab1 25 %, Lab2 30 %, Lab3 45 %) y qué se evalúa en cada uno.
  - `rubrica.md`: rúbrica consolidada sobre 10 pts con criterios detallados para cada lab en el formato estándar del curso (4 niveles).
  - `checklist-entrega.md`: checklist común + sección específica por cada lab.
  - `cuestionario-deep-learning.gift`: 18 preguntas GIFT en 4 bloques (fundamentos, backpropagation, frameworks/práctica, arquitecturas avanzadas).
- Las rúbricas originales en los labs se mantienen intactas como referencia detallada.

### Siguiente paso

Añadir `04-evaluacion/README.md` a las unidades que aún no lo tienen (03-12).

## Continuación — 2026-07-01 (READMEs evaluación)

### Hecho

- Creado `04-evaluacion/README.md` en las 6 unidades que faltaban:
  - **UD3 (ML)**: inventario de rúbricas e instrumentos existentes (cuestionario Bank Marketing, rúbricas Labs + capstone).
  - **UD5 (Cloud/MLOps)**: orientación a los 2 GIFT y las prácticas de tarea comparativa y AWS.
  - **UD7 (Convergencia)**: descripción de los 3 instrumentos ya existentes (criterios, rúbrica proyecto, GIFT).
  - **UD9 (GPU)**: orientación al GIFT existente y a las prácticas Sem29; evidencias esperadas.
  - **UD11 (Anexos)**: aclaración del carácter no obligatorio; referencia a la actividad RL opcional con rúbrica en `90-archivo/actividades-rl/`.
  - **UD12 (Proyecto integrado)**: enlace a los documentos de evaluación ya existentes en `01-teoria/` (evaluacion.md, checkpoints, guía).

### Siguiente paso

Unificar checklists de entrega en unidades distribuidas (UD3, UD4, UD5).

## Continuación — 2026-07-01 (checklists)

### Hecho

- Creado `04-evaluacion/checklist-entrega.md` en UD3 (ML): secciones para Labs 1-3 (dataset), Midterm Capstone (películas) y Tarea Bank Marketing.

## Continuación — 2026-07-05 (UD4 saneamiento)

### Hecho

- Cerrado el residuo de `04-deep-learning/01-teoria/01-redes-neuronales-genericas/modelado-avanzado-docs/`.
- La carpeta antigua queda vacía/eliminada del flujo activo.
- RNN/LSTM se conserva en UD4 sólo como introducción conceptual:
  - `04-deep-learning/01-teoria/01-fundamentos-redes-neuronales/Parte-II-RedesEspecializadas/RedesRecurrentes_y_LSTM_intro.md`
- El desarrollo largo y las fuentes antiguas se conservan como archivo histórico versionable:
  - `04-deep-learning/90-archivo/modelado-avanzado-docs/`
- Se añadió una excepción estrecha en `.gitignore` para que ese archivo histórico no quede ignorado por las reglas globales de `90-archivo/`, `*.pdf` y `*.zip`.
- Eliminado el backup temporal `002-Underfit-Overfit_BiasVariance.md~`.

### Estado posterior de UD4

- [x] Recursos de UD4 revisados el 2026-07-06: `blackfriday/`, `modelado-entornos/` y `captura.mp4`.
- [x] Evaluación UD4 revisada el 2026-07-06: GIFT alineado con Deep Learning base, sin preguntas canónicas de visión/NLP/Transformers.
- [x] Cambios consolidados en commits temáticos.
- Creado `04-evaluacion/checklist-entrega.md` en UD5 (Cloud/MLOps): secciones para tarea comparativa cloud (individual + grupal) y tarea AWS.
- Actualizado `04-evaluacion/checklist-entrega.md` en UD4 (DL): añadida sección de tareas de visión (CNN mini-tareas + Chihuahua/Transfer Learning).

### Estado final de las mejoras opcionales

Todas las mejoras opcionales del plan original están completadas. El repositorio queda listo para el curso 2026-2027 salvo las dos acciones de usuario pendientes:

1. **Rotación de claves API completada** — OpenAI, Hopsworks y PageIndex.
2. **Validar GIFT en Moodle** — aplazado hasta que termine el mantenimiento de Moodle.

## Continuación — 2026-07-02 (corte para retomar)

### Hecho hoy

- **UD4**: iniciada reorganización estructural de teoría para evitar unidad monolítica:
  - `01-teoria/01-redes-neuronales-genericas/`
  - `01-teoria/02-redes-neuronales-vision/`
  - `01-teoria/03-redes-neuronales-nlp/`
  - Ya movidos los bloques previos (`fundamentos-docs`, `frameworks-docs`, `modelado-avanzado-docs`, `vision-teoria`, `nlp-docs`, `nlp-libros`) a la nueva estructura.
- **UD9**: normalización de numeración en ejemplos y prácticas:
  - `02-ejemplos/`: renumerado continuo (01..06) con sus variantes `_SOLUCIONES` y `_SOLUCIONES_TESTS`.
  - `03-practicas/`: renumerado `102/103/104` a `01/02/03` y sincronizadas soluciones en `99-profesor/soluciones-practicas/`.
  - Renombrada guía de ejemplos a `02-ejemplos/00-guia-ejemplos.md`.

### Pendiente inmediato (mañana) — histórico

Este bloque queda **resuelto**. Ver estado actualizado en:

- `Continuación — 2026-07-02 (actualización de ejecución)`

### Pendientes de usuario (se mantienen)

- [x] Rotación de claves API completada.
- [~] Validar GIFT en Moodle y ajustar pesos/retroalimentación cuando Moodle vuelva a estar disponible.

## Continuación — 2026-07-02 (actualización de ejecución)

### Estado del pendiente inmediato anterior

- [x] **UD9**: ajustadas referencias textuales residuales a numeración antigua en `README.md` y en `docs/09-gpu-avanzado/README.md` (ejemplos `90..101` -> `01..06`).
- [x] **UD9**: verificación final de coherencia de enlaces y numeración tras renombrados en ejemplos/prácticas.
- [x] **UD4**: actualizados `04-deep-learning/README.md` y `04-deep-learning/01-teoria/README.md` para reflejar la nueva estructura por bloques.
- [x] **UD4**: comprobado que no quedan artefactos `.html`/`.pdf` en `04-deep-learning/01-teoria/` para limpieza inmediata.
- [x] **Normalización transversal**: aplicada en unidades activas (`UD1`, `UD2`, `UD6`, `UD8`, `UD9`) y sus copias en `docs/`, eliminando referencias de semana en títulos/READMEs donde no era material histórico estricto.

### Hecho hoy (detalle)

- **UD4**
  - Reescritos los índices principales para la estructura:
    - `01-redes-neuronales-genericas/`
    - `02-redes-neuronales-vision/`
    - `03-redes-neuronales-nlp/`
  - Actualizada la sección de evaluación (ya consolidada en `04-evaluacion/`).
- **UD9**
  - Sincronizada la tabla de ejemplos con los notebooks renumerados (`01_...` a `06_...`) en raíz y `docs/`.
- **Barrido transversal**
  - Normalizados encabezados y descriptores en guías activas de UD1, UD2, UD8 y UD9.
  - Normalizados textos visibles en el bloque legado de UD6 (`serving-orquestacion`) sin renombrar ficheros históricos.
  - Actualizadas también las copias espejo de `docs/` en cada caso.

### Queda por hacer (operativo)

1. **Pendientes de usuario (sin cambios)**
   - Validación final de cuestionarios GIFT en Moodle, aplazada por mantenimiento de la plataforma.

## Continuación — 2026-07-02 (normalización sin semanas)

### Estado

- [x] **TERMINADO**.

### Hecho

- Eliminada la nomenclatura `semana` de rutas/ficheros activos, guías visibles y referencias internas de las unidades activas.
- Renombradas guías de UD1, UD2, UD4/NLP, UD6 y paquetes ZIP activos de UD8 a nombres por bloque, tema o fase.
- Renombrado `06-llm-agentes/03-practicas/serving-orquestacion/` y sus guías internas a nombres sin calendario.
- Normalizada la guía extensa de UD2 a lenguaje de bloques en lugar de semanas.
- Verificado que no quedan ocurrencias de `semana`/`Semana` en nombres ni textos activos, excluyendo datos reales, archivos históricos y `site/` generado.

### Detalle de cambios realizados

- **UD1**
  - `01-guia-semana-1-python-basico.md` → `01-guia-python-basico.md`
  - `05-guia-semana-2-numpy-jax.md` → `05-guia-numpy-jax.md`
  - Actualizadas referencias en `01-fundamentos-python/01-teoria/README.md`.
- **UD2**
  - `16-guia-semana3.md` → `16-guia-pandas-visualizacion.md`
  - `17-guia-semana4.md` → `17-guia-visualizacion-avanzada.md`
  - `18-guia-semana5.md` → `18-guia-polars-duckdb.md`
  - `19-guia-semanas-5-6-7.md` → `19-guia-pandas-polars-visualizacion.md`
  - `12_semana3_eda.ipynb` → `12_eda_guiado.ipynb`
  - `semana4_fig.png` → `visualizacion_fig.png`
  - Actualizadas referencias y textos visibles en teoría, ejemplos y materiales de profesor.
- **UD3**
  - Renombradas actividades heredadas de UD2 para quitar `Semana7` del nombre.
- **UD4**
  - `003-spacy-guia-semana.md` → `003-spacy-guia.md`
  - Actualizada la referencia desde el README de ejemplos spaCy.
- **UD6**
  - `03-practicas/semana27-serving-orquestacion/` → `03-practicas/serving-orquestacion/`
  - `Semana27_Guia.md` → `00-guia-serving-orquestacion.md`
  - `Semana27_Fase1_Guia.md` → `guia-fase1.md`
  - `Semana27_Fase2_Guia.md` → `guia-fase2.md`
  - Actualizadas referencias internas, README y nombres de experimentos/notas visibles.
- **UD8**
  - Renombrados paquetes ZIP activos de ejemplos y prácticas a nombres por rango de temas (`tema78-80`, `tema81-83`, `tema84-86`).
- **Estado del proyecto**
  - Actualizado este fichero para dejar la normalización marcada como terminada.

### Queda por hacer

- Validación final de cuestionarios GIFT en Moodle, aplazada por mantenimiento de la plataforma.

## Continuación — 2026-07-02 (cierre operativo)

### Estado

- [x] **CURSO CERRADO OPERATIVAMENTE EN EL REPOSITORIO**.

### Hecho

- Rotación de claves API completada: OpenAI, Hopsworks y PageIndex.
- La validación GIFT queda aplazada porque Moodle está en mantenimiento tras el cierre del curso.
- Este aplazamiento no bloquea el cierre operativo del repositorio; queda como tarea externa para cuando Moodle vuelva a estar disponible.

### Único recordatorio futuro

- Importar los GIFT en Moodle cuando la plataforma vuelva a estar disponible y ajustar pesos/retroalimentación si hiciera falta.

## Continuación — 2026-07-02 (política de uso de IA)

### Estado

- [x] **AÑADIDO AL REPOSITORIO**.

### Hecho

- Creada la política transversal `plantillas/uso-ia/politica_uso_ia_pia.md`.
- Vinculada la política con `plantillas/uso-ia/plantilla_declaracion_uso_ia.md`.
- Añadido el uso de IA con trazabilidad, verificación y defensa al proyecto integrado:
  - `12-proyecto-integrado/01-teoria/proyecto.md`
  - `12-proyecto-integrado/01-teoria/evaluacion.md`
  - `12-proyecto-integrado/04-evaluacion/README.md`
- Añadida sección común de uso de IA en los checklists de entrega de las unidades con evaluación activa.
- Añadidos enlaces desde `README.md` y `00-planificación/README.md`.

### Criterio adoptado

En PIA el uso de IA está permitido como herramienta profesional de apoyo, especialmente en proyectos complejos, pero debe dejar trazabilidad suficiente: herramientas usadas, prompts o instrucciones relevantes, decisiones propias, cambios realizados, verificación y defensa oral.

La IA no se trata como atajo ni como trampa automática; se evalúa el producto, el proceso y la capacidad del alumnado para explicar y verificar lo entregado.

## Continuación — 2026-07-05 (reapertura UD4)

### Hecho

- Reabierta UD4 porque concentraba demasiado material de deep learning, visión, NLP, series temporales y proyectos tabulares.
- Creada y mantenida la tabla viva de reorganización en `04-deep-learning/00-pendientes-revision.md`.
- Creado el registro de movimientos en `04-deep-learning/00-decisiones-reorganizacion.md`.
- Separado material de visión hacia UD8, NLP/Transformers hacia UD6 y series temporales hacia UD10.
- Eliminados HTML generados duplicados tras recuperar el Markdown origen de Underfit/Overfit.
- Reorganizada la teoría interna de UD4 en fundamentos, frameworks y métricas/evaluación.
- Revisado y separado `used-cars`:
  - Keras/PyTorch a UD4 como DL tabular.
  - PyCaret/AutoML a UD3.
  - `layersReuse` y recurso de imagen a UD8.
- Revisado y limpiado `boston-housing`:
  - Se mantiene en UD4 como regresión tabular con redes neuronales.
  - Archivado notebook incorrecto Iris/clasificación.
  - Añadido README y corregidas rutas de scripts.
  - Versionado explícito `data/housing.csv` por ser pequeño y necesario para reproducibilidad.
- Revisado y movido `house-prices-kaggle`:
  - Núcleo EDA/pipelines/ML tabular a UD3.
  - Material R y datasets Wine/Cacao reubicados en UD2.
  - Material histórico no activo llevado a archivo.
- Creada trazabilidad legal y hoja de cálculo para calificaciones RA/CE.

### Decisiones docentes

- `euromillones` se conserva como actividad crítica: demuestra límites de ML ante procesos sin patrón y relaciones espurias.
- Los `.org` no se eliminan automáticamente: pueden ser fuentes originales.
- LSTM/RNN debe tener introducción en UD4, continuidad en NLP y cierre/aplicación en series temporales.
- PyCaret/AutoML pertenece a UD3, no a deep learning puro.
- R queda resuelto como itinerario opcional ampliado en UD2 para análisis estadístico, visualización y EDA; queda pendiente sólo probar ejecución completa con paquetes concretos (`dplyr`, `ggplot2`, `tibble`, `lubridate`, `rmarkdown`, `knitr`) antes de aula.

### Pendientes

1. [x] Recursos UD4 revisados: `blackfriday/`, `modelado-entornos/` y `captura.mp4`.
2. [x] Evaluación UD4 revisada: `rubrica.md`, `cuestionario-deep-learning.gift` y `checklist-entrega.md`.
   - `checklist-entrega.md`.
3. Valorar ampliación de R en UD2, especialmente análisis estadístico y visualizaciones de EDA.
4. Hacer revisión final de `git status`, rutas vacías, ignorados y build antes de cerrar commit.

## Continuación — 2026-07-05 (UD4 `euromillones`)

### Hecho

- `euromillones/` queda conservado en UD4 como actividad crítica sobre límites de ML, no como promesa predictiva.
- Añadido `04-deep-learning/03-practicas/modelado-proyectos/euromillones/README.md`.
- Confirmado que los CSV locales de Euromillones están ignorados por Git; si se usan, deben distribuirse por Moodle/fuente controlada.
- La actividad queda fuera del itinerario canónico salvo que el profesorado quiera trabajar explícitamente pensamiento crítico sobre ML.

### Siguiente paso recomendado

Revisar `used-cars-dl-tabular/` y después `boston-housing/` para cerrar los proyectos prácticos de UD4 antes de tocar evaluación.

## Continuación — 2026-07-05 (regla operativa)

### Hecho

- Creado `AGENTS.md` en la raíz del repositorio.
- Añadida regla obligatoria: después de cualquier cambio significativo, decisión, limpieza, movimiento de material o cierre parcial, hay que actualizar `ESTADO_ACTUAL_Y_PENDIENTES.md` en el mismo turno.
- Añadida regla para subagentes: deben actualizar la hoja de ruta o devolver el bloque exacto que haya que incorporar.

### Motivo

Evitar que el estado real del saneamiento y los pendientes quede desfasado respecto al trabajo realizado.

## Continuación — 2026-07-05 (`used-cars-dl-tabular`)

### Hecho

- Auditada la carpeta `04-deep-learning/03-practicas/modelado-proyectos/used-cars-dl-tabular/` sin ejecutar notebooks pesados.
- Revisados los tres notebooks incluidos:
  - `keras_notebook2.ipynb`: se mantiene como ejemplo principal Keras de regresión tabular.
  - `tf_keras_notebook.ipynb`: se mantiene como variante avanzada/incompleta por PyArrow/Vaex/Parquet y bloque DEAP.
  - `pytorch_notebook.ipynb`: queda identificado como pendiente de refactor porque importa PyTorch pero conserva flujo Keras.
- Reescrito el `README.md` del proyecto con objetivo docente, datos no versionados, notebooks, prerequisitos, criterios de evaluación honesta y advertencias de no versionar datasets/`mlruns`/modelos.
- Actualizados `04-deep-learning/00-decisiones-reorganizacion.md` y `04-deep-learning/00-pendientes-revision.md` con la decisión y la deuda técnica concreta.

### Decisión

`used-cars-dl-tabular` se mantiene en UD4 como práctica de regresión tabular con redes neuronales, pero queda cerrado sólo a nivel documental. No se considera cerrado como práctica ejecutable completa hasta refactorizar o retirar la falsa variante PyTorch y preparar una muestra de datos reproducible.

### Queda pendiente

- Refactorizar `pytorch_notebook.ipynb` si se quiere una práctica PyTorch real, o renombrarlo/archivarlo.
- Decidir si `tf_keras_notebook.ipynb` se usa como variante avanzada de profesor o se simplifica.
- Preparar dataset reducido o instrucciones controladas de descarga si se convierte en tarea evaluable.
- Siguiente foco recomendado en UD4: revisar recursos (`blackfriday/`, `modelado-entornos/`, `captura.mp4`) antes de tocar evaluación.

## Continuación — 2026-07-06 (`boston-housing`)

### Hecho

- Auditada la carpeta `04-deep-learning/03-practicas/modelado-proyectos/boston-housing/` sin instalar dependencias ni ejecutar entrenamiento pesado.
- Confirmado que `data/housing.csv` es pequeño (~49 KB, 506 filas) y está permitido por excepción explícita en `.gitignore` pese a las reglas globales `*.csv` y `data/`.
- Confirmado que los cuatro scripts (`Keras`, `Pytorch`, `SciKeras`, `SciPytorch`) cargan el dataset con ruta relativa robusta basada en `Path(__file__)`.
- Reescrito el `README.md` del proyecto con objetivo docente, scripts incluidos, dataset versionado, métricas esperadas, limitaciones éticas de Boston Housing y deuda técnica.
- Actualizados `04-deep-learning/00-decisiones-reorganizacion.md` y `04-deep-learning/00-pendientes-revision.md` con el cierre documental y los pendientes metodológicos.

### Decisión

`boston-housing` se mantiene en UD4 como práctica de regresión tabular con redes neuronales. El saneamiento documental queda cerrado, pero no se considera práctica evaluable canónica hasta corregir baseline, escalado antes del split, métricas en unidades originales y tratamiento ético del dataset.

### Queda pendiente

- Si se usa con alumnado, preparar una versión limpia de los scripts: baseline, split antes de escalado, MAE/RMSE/R² en unidades originales y reflexión ética.
- Continuar el saneamiento de UD4 por recursos pendientes: `blackfriday/`, `modelado-entornos/` y `captura.mp4`.
- Después, revisar evaluación UD4 (`rubrica.md`, `cuestionario-deep-learning.gift`, `checklist-entrega.md`).

## Cierre de sesión — 2026-07-06

### Hecho en esta sesión

- Añadido `AGENTS.md` en la raíz con la regla operativa de actualizar esta hoja de ruta tras cada cambio significativo.
- Cerrado documentalmente `used-cars-dl-tabular/`:
  - se mantiene en UD4 como regresión tabular con redes neuronales;
  - `keras_notebook2.ipynb` queda como ejemplo principal;
  - `tf_keras_notebook.ipynb` queda como variante avanzada/incompleta;
  - `pytorch_notebook.ipynb` queda como deuda técnica explícita.
- Cerrado documentalmente `boston-housing/`:
  - se mantiene en UD4 como regresión tabular con redes neuronales;
  - `housing.csv` queda como dataset pequeño versionable;
  - se documentan las limitaciones éticas y metodológicas del dataset;
  - queda deuda técnica si se convierte en práctica evaluable.

### Estado Git al cierre

- `236` borrados.
- `12` modificados.
- `30` nuevos sin trackear.
- No se ha hecho commit.
- `ESTADO_ACTUAL_Y_PENDIENTES.md` está ignorado por Git y no aparece en `git status`.

### Queda por hacer mañana

1. Revisar recursos UD4:
   - `04-deep-learning/05-recursos/modelado-datos/blackfriday/`
   - `04-deep-learning/05-recursos/modelado-entornos/`
   - `04-deep-learning/05-recursos/captura.mp4`
2. Revisar evaluación UD4:
   - `04-deep-learning/04-evaluacion/rubrica.md`
   - `04-deep-learning/04-evaluacion/cuestionario-deep-learning.gift`
   - `04-deep-learning/04-evaluacion/checklist-entrega.md`
3. Valorar ampliación opcional de R en UD2.
4. Hacer revisión final de rutas vacías, ignorados, `git status` y build antes de preparar commit.

### Siguiente paso recomendado

Empezar por los recursos UD4, primero `blackfriday/`, porque define si todavía queda material práctico de regresión con redes neuronales que deba enlazarse desde la evaluación.

## Continuación — 2026-07-06 (commits temáticos)

### Hecho

- Consolidados los cambios pendientes en 3 commits temáticos:
  - `d9b615a4` — `chore(repo): add workflow and traceability artifacts`
  - `b10d8149` — `refactor(ud4): split applied deep learning materials`
  - `12929f21` — `refactor(ud4): reorganize tabular project materials`
- Corregido whitespace final en `04-deep-learning/90-archivo/fundamentos-old/Codigo/activationFunctions.py` antes de commitear el archivo histórico.
- Verificado `git status --short`: sin cambios pendientes versionados tras los commits.

### Siguiente paso recomendado

Continuar con la revisión de recursos UD4, empezando por `04-deep-learning/05-recursos/modelado-datos/blackfriday/`, y después revisar `modelado-entornos/` y `captura.mp4` antes de ajustar la evaluación UD4.

## Continuación — 2026-07-06 (recursos UD4)

### Hecho

- Revisado `04-deep-learning/05-recursos/modelado-datos/blackfriday/`:
  - contiene `blkfri_train.csv` (~25 MB) y `blkfri_test.csv` (~9,6 MB), ambos ignorados por Git por la regla global `*.csv`;
  - no hay práctica activa que lo enlace actualmente;
  - se añade `README.md` y queda como recurso local opcional de regresión tabular, no como práctica evaluable canónica.
- Revisado `04-deep-learning/05-recursos/modelado-entornos/`:
  - se mantiene como colección de plantillas docentes de entorno;
  - se añade `README.md`;
  - se corrige activación de conda en scripts, `set -euo pipefail`, comillas en `keras>=3.0` y canal `nvidia` en `environment.yml`.
- Revisado `04-deep-learning/05-recursos/captura.mp4`:
  - no tiene referencias activas;
  - se mueve a `04-deep-learning/90-archivo/recursos/captura.mp4` como archivo local ignorado, no versionado.

### Decisión

Los recursos UD4 quedan saneados a nivel documental. No se enlaza `blackfriday` ni `captura.mp4` desde la evaluación. Los entornos quedan como apoyo, no como contrato de instalación obligatorio.

### Siguiente paso recomendado

Revisar evaluación UD4: `04-evaluacion/rubrica.md`, `cuestionario-deep-learning.gift` y `checklist-entrega.md`, para asegurar que ya no evalúan visión/NLP/transformers y que encajan con Deep Learning base.

## Continuación — 2026-07-06 (evaluación UD4)

### Hecho

- Revisada `04-deep-learning/04-evaluacion/rubrica.md`: ya está centrada en los tres laboratorios base de UD4 y no requiere cambios.
- Revisado `04-deep-learning/04-evaluacion/checklist-entrega.md`: mantiene una nota explícita de frontera para derivar visión/NLP a UD8/UD6; no evalúa esos bloques como UD4.
- Ajustado `04-deep-learning/04-evaluacion/cuestionario-deep-learning.gift`:
  - se retiran preguntas canónicas sobre CNN/Transformer;
  - el bloque final queda centrado en generalización, RNN/LSTM como arquitectura puente, early stopping y frontera de decisión.
- Actualizado `04-deep-learning/04-evaluacion/README.md` para describir el GIFT como fundamentos, backpropagation, frameworks, regularización y arquitecturas puente.
- Actualizado `04-deep-learning/00-pendientes-revision.md` con la revisión de evaluación.

### Decisión

La evaluación canónica de UD4 queda alineada con Deep Learning base. Visión aplicada y NLP/Transformers quedan sólo como frontera documentada y se evalúan desde UD8 y UD6 respectivamente.

### Siguiente paso recomendado

Hacer revisión final de rutas vacías, ignorados, `git status` y `mkdocs build --strict` antes de cerrar el saneamiento de UD4 con commit final si procede.

## Continuación — 2026-07-06 (cierre técnico UD4)

### Verificación realizada

- `mkdocs build --strict` ejecutado correctamente; documentación generada sin errores bloqueantes.
- Revisadas rutas vacías en UD4/UD6/UD8/UD10 y eliminados directorios residuales vacíos.
- Verificado `git status --short`: limpio tras los commits realizados.
- Verificados ignorados relevantes:
  - `04-deep-learning/05-recursos/modelado-datos/blackfriday/*.csv` sigue ignorado por `*.csv`.
  - `04-deep-learning/90-archivo/recursos/captura.mp4` sigue ignorado por `*.mp4`.

### Estado

El saneamiento estructural de UD4 queda cerrado a nivel operativo: teoría separada, recursos revisados, evaluación alineada y build estricto validado.

### Pendiente no bloqueante

- [x] Valorar y reforzar ampliación opcional de R en UD2: resuelto el 2026-07-06 con itinerario R/Titanic ampliado, entrega y rúbrica. Queda sólo probar ejecución completa con paquetes concretos (`dplyr`, `ggplot2`, `tibble`, `lubridate`, `rmarkdown`, `knitr`).
- Decidir en otro momento si alguna práctica UD4 (`used-cars-dl-tabular`, `boston-housing`, `blackfriday`) se convierte en tarea evaluable plenamente reproducible.

## Continuación — 2026-07-06 (UD2 R opcional)

### Hecho

- Revisado el material R existente en UD2.
- Confirmado que ya había un bloque activo en `02-tratamiento-datos/03-practicas/r_exercises_titanic_with_tests/` con ejercicios `.Rmd` para alumnado y material de profesor en `99-profesor/practicas/`.
- Añadido `README.md` al itinerario R/Titanic para dejar clara la decisión docente.
- Actualizados los README de UD2, teoría y evaluación para presentar R como itinerario opcional Pandas ↔ dplyr.
- Actualizados los registros de UD4 que mantenían R como pendiente transversal.

### Decisión

R se conserva como **itinerario opcional de ampliación** para análisis estadístico, visualización y EDA, centrado en Titanic y comparación Pandas ↔ dplyr. No sustituye el eje obligatorio de UD2: Python, Pandas, Matplotlib y Seaborn.

### Estado

El pendiente de valorar ampliación de R en UD2 queda resuelto documentalmente.

### Siguiente paso recomendado

Validar con `mkdocs build --strict` y hacer commit temático de la decisión UD2/R.


## Continuación — 2026-07-06 (diagnóstico de suficiencia R)

### Hecho

- Revisado el contenido real de los `.Rmd` activos del itinerario R/Titanic.
- Detectado que el material actual sirve como primer contacto, pero no como suficiencia profesional básica.
- Creado `02-tratamiento-datos/00-r-itinerario-laboral.md` con diagnóstico, brechas y ampliación mínima propuesta.
- Actualizado el README del itinerario R para no presentarlo como suficiente si el objetivo es empleabilidad con R.

### Decisión

R se mantiene como itinerario opcional, pero debe reforzarse si queremos que el alumnado pueda defenderse en un entorno laboral donde se use R/tidyverse.

### Siguiente paso recomendado

Implementar la ampliación mínima del itinerario R: transformación con `mutate`, agrupaciones, joins, `ggplot2`, mini-EDA completo y comparativa Pandas ↔ dplyr.

## Continuación — 2026-07-06 (ampliación mínima R UD2)

### Hecho

- Reforzado el itinerario R activo en `02-tratamiento-datos/03-practicas/r_exercises_titanic_with_tests/`.
- Rehechos los `.Rmd` de alumno para cubrir:
  - carga e inspección de datos;
  - selección, filtrado y ordenación;
  - `mutate`, `group_by` y `summarise`;
  - `left_join` con tabla auxiliar;
  - fechas con `lubridate`;
  - visualización con `ggplot2`;
  - mini-EDA con conclusiones.
- Añadidos:
  - `00_instalacion_y_entorno_R.md`;
  - `06_comparativa_pandas_dplyr.md`.
- Actualizado `02-tratamiento-datos/00-r-itinerario-laboral.md` para reflejar que la ampliación mínima ya está aplicada.

### Verificación

- `mkdocs build --strict` ejecutado correctamente.
- Sintaxis de chunks R validada con `Rscript parse(...)`.
- La ejecución completa de los `.Rmd` queda validada el 2026-07-07 tras eliminar la dependencia de `tidyverse` y `readr`.

### Estado

R queda ahora como itinerario opcional con suficiencia operativa básica razonable para defenderse en un contexto donde se use R para datos; los `.Rmd` activos renderizan correctamente con paquetes concretos.


## Continuación — 2026-07-06 (R UD2: evaluación y soluciones)

### Hecho

- Añadida `02-tratamiento-datos/03-practicas/r_exercises_titanic_with_tests/07_entrega_itinerario_R.md` con evidencias mínimas de entrega.
- Añadida `02-tratamiento-datos/04-evaluacion/rubrica-itinerario-r.md` para evaluar el itinerario R si se activa como actividad.
- Actualizado `02-tratamiento-datos/04-evaluacion/README.md` para enlazar la rúbrica R.
- Actualizadas localmente las soluciones de profesor en `02-tratamiento-datos/99-profesor/practicas/*_R_profesor.Rmd`.

### Nota Git

`99-profesor/` está ignorado por Git mediante la regla `*profe*`, así que las soluciones docentes quedan como material local privado y no se versionan.

### Verificación

Renderizados correctamente los `.Rmd` activos del itinerario R con `dplyr`, `ggplot2`, `tibble`, `lubridate`, `rmarkdown` y `knitr`.

## Continuación — 2026-07-06 (regla anti-pendientes obsoletos)

### Hecho

- Reforzada la regla operativa en `AGENTS.md` para evitar que tareas ya realizadas sigan apareciendo como pendientes.
- Añadida sección explícita "Regla anti-pendientes obsoletos".

### Decisión

Cada vez que se complete una tarea, pendiente o decisión, debe actualizarse inmediatamente `ESTADO_ACTUAL_Y_PENDIENTES.md` antes de iniciar otro bloque de trabajo.

La actualización debe corregir contradicciones entre secciones antiguas y nuevas, cambiar estados `[ ]`/`[~]` a `[x]` cuando proceda y retirar de "Próximas acciones sugeridas" lo que ya esté hecho.

### Siguiente paso recomendado

Aplicar esta regla como cierre obligatorio de cada bloque de trabajo.


## Continuación — 2026-07-07 (UD12 evidencia de negocio y automatización)

### Hecho

- Añadida en `12-proyecto-integrado/01-teoria/proyecto.md` la sección obligatoria de negocio, automatización y conveniencia.
- Reforzados `checkpoints_proyecto_final.md`, `evaluacion.md` y `README.md` para exigir proceso afectado, usuarios, valor esperado, riesgos, alternativa descartada y criterio de conveniencia.

### Resultado posterior

- UD7 quedó completada el 2026-07-07 con la evidencia complementaria de convergencia tecnológica, seguridad y toma de decisiones.

### Siguiente paso recomendado

Volver al bloque general de seguimiento del curso: `Prueba_CE`, `.Rmd` de R y validación GIFT.


## Continuación — 2026-07-07 (UD7 evidencia de negocio, seguridad y decisión)

### Hecho

- Añadido en `07-convergencia-herramientas/01-teoria/10_stack_convergente.md` el recordatorio explícito de proceso afectado, usuarios, riesgos y conveniencia.
- Reforzados `criterios_evaluacion.md` y `rubrica_proyecto.md` para exigir el bloque de impacto/seguridad/conveniencia en el informe del proyecto de UD7.
- Actualizado `07-convergencia-herramientas/README.md` para resumir el nuevo criterio de cierre.

### Resultado

- El proyecto de UD7 ya deja explícito que no basta con integrar herramientas: también debe justificar el efecto sobre negocio/proceso, la seguridad y la conveniencia de la solución.

### Siguiente paso recomendado

Volver al bloque general de seguimiento del curso: `Prueba_CE`, `.Rmd` de R y validación GIFT.


## Continuación — 2026-07-07 (R UD2 sin metapaquete tidyverse)

### Hecho

- Sustituida la carga de `library(tidyverse)` en los `.Rmd` del itinerario R por paquetes concretos: `dplyr`, `ggplot2`, `tibble`, `lubridate`, `rmarkdown`, `knitr` según corresponda.
- Actualizada la guía `00_instalacion_y_entorno_R.md` para instalar sólo los paquetes necesarios.
- Actualizada esta hoja de ruta para no bloquear la prueba por el metapaquete `tidyverse`.

### Motivo

`tidyverse` como metapaquete puede fallar al compilar por una dependencia no usada directamente por el itinerario. Además, la lectura de CSV pasa a `read.csv()` de R base para evitar depender de `readr`.

### Siguiente paso recomendado

Instalar/verificar `dplyr`, `ggplot2`, `tibble`, `lubridate`, `rmarkdown`, `knitr`, y renderizar los `.Rmd` en orden.


## Continuación — 2026-07-07 (R UD2 render validado)

### Hecho

- Eliminada también la dependencia de `readr`: los `.Rmd` leen CSV con `read.csv()` de R base.
- Verificado que están disponibles `dplyr`, `ggplot2`, `tibble`, `lubridate`, `rmarkdown` y `knitr`.
- Renderizados correctamente los seis `.Rmd` activos del itinerario R en salida temporal.

### Resultado

El itinerario R deja de depender de `tidyverse` y `readr`, reduciendo problemas de compilación. El pendiente de ejecución completa de `.Rmd` queda cerrado.

### Siguiente paso recomendado

Quedan como pendientes reales: revisión visual del seguimiento Excel, validación GIFT en Moodle y decisiones futuras sobre prácticas UD4 si se quieren convertir en evaluables reproducibles.

## Cierre de sesión — 2026-07-07 (commits y push)

### Hecho

- Consolidados y subidos a `origin/main` los cambios de cierre:
  - `2ab19c0b docs(ud12): require business impact evidence`;
  - `3a75583c docs(ud7): require impact and safety rationale`;
  - `e9120907 fix(ud2): remove tidyverse dependency from R itinerary`.
- Verificado que `main` queda sincronizada con `origin/main`.
- UD12 queda reforzada con evidencia de negocio, automatización y conveniencia.
- UD7 queda reforzada con evidencia de impacto, seguridad y toma de decisiones.
- UD2/R queda validada sin depender de `tidyverse` ni `readr`; los seis `.Rmd` activos renderizan correctamente.

### Queda pendiente

1. Revisar visualmente `SEGUIMIENTO_CURSO_PIA.xlsx`, especialmente `Prueba_CE`, en LibreOffice/Excel.
2. Validar los cuestionarios GIFT en Moodle cuando la plataforma esté disponible.
3. Decidir más adelante si `used-cars-dl-tabular`, `boston-housing` o `blackfriday` pasan a tareas evaluables plenamente reproducibles.
4. Si se quiere resolver el entorno R del sistema por limpieza, revisar la incompatibilidad de `systemfonts` que bloquea `ragg`/`tidyverse`; no es bloqueante para el repo.

### Siguiente paso recomendado

Retomar por la revisión visual del libro de seguimiento (`SEGUIMIENTO_CURSO_PIA.xlsx`) o por la validación GIFT si Moodle ya está disponible.

## Cierre de sesión — 2026-07-11 (revisión de estado)

### Hecho

- Verificado que `main` está limpia y sincronizada con `origin/main`.
- Confirmado que UD12 ya fue blindada y subida en el commit `2ab19c0b`: incluye evidencia de negocio, automatización y conveniencia del modelo.
- Corregida la presentación de esta hoja de ruta: el snapshot vigente es 2026-07-07 y las continuaciones de junio quedan identificadas como historial sustituido.

### Queda pendiente

1. Revisar visualmente `SEGUIMIENTO_CURSO_PIA.xlsx`, especialmente `Prueba_CE`, en LibreOffice/Excel.
2. Validar los cuestionarios GIFT en Moodle cuando la plataforma esté disponible.
3. Decidir, sólo si interesa convertirlas en evaluables reproducibles, el destino de `used-cars-dl-tabular`, `boston-housing` y `blackfriday` de UD4.
4. Opcional: limpiar la incompatibilidad de `systemfonts` que bloquea `ragg`/`tidyverse` en el entorno R; no afecta al itinerario activo ni al repositorio.

### Siguiente paso recomendado

Abrir `SEGUIMIENTO_CURSO_PIA.xlsx` y revisar `Prueba_CE`; es el único pendiente operativo que no depende de un servicio externo.

## Continuación — 2026-07-14 (validación visual del seguimiento)

### Hecho

- Confirmado por el usuario que `SEGUIMIENTO_CURSO_PIA.xlsx` se abre correctamente.
- Cerrada la revisión visual inicial del libro, incluida la hoja `Prueba_CE`.

### Queda pendiente

1. Validar los cuestionarios GIFT en Moodle cuando la plataforma esté disponible.
2. Completar alumnado, grupos, CE previstos, pesos reales y fechas cuando vaya a comenzar el uso en aula.
3. Decidir, sólo si interesa convertirlas en evaluables reproducibles, el destino de `used-cars-dl-tabular`, `boston-housing` y `blackfriday` de UD4.

### Siguiente paso recomendado

Validar los cuestionarios GIFT de UD1 y UD2 en Moodle cuando la plataforma esté disponible; hasta entonces no queda ningún pendiente operativo inmediato que bloquee el uso del repositorio.

## Cierre operativo — 2026-07-14

- El repositorio queda declarado **semicerrado**: apto para uso docente, sin trabajo inmediato obligatorio.
- Los cambios futuros se tratarán como mejoras surgidas de revisiones en profundidad o de la experiencia de aula, no como deuda que impida utilizar el material actual.
- Se mantienen únicamente los pendientes condicionados por Moodle, la preparación de datos reales del curso y decisiones opcionales sobre prácticas de UD4.

## Decisión Python — 2026-07-16

- **Python 3.12** será la versión objetivo para todos los entornos conda/mamba del curso.
- Las versiones actuales (julio 2026) de numpy (2.5.1), pandas (3.0.3), scipy (1.18.0), scikit-learn (1.9.0), torch (2.13.0), keras (3.15.0), matplotlib (3.11.0), transformers (5.14.0), tensorflow (2.21.0) y polars (1.42.1) son todas compatibles con 3.12.
- El sistema base (Python 3.10.9) no se actualiza; el trabajo se hace por entorno conda/mamba.
- **Acción futura (≈ oct 2026)**: re-verificar compatibilidad de versiones antes del inicio del curso, ya que las librerías pueden haber actualizado sus requisitos mínimos de Python.

## Continuación — 2026-07-27 (CRISP-DM y prevención de fuga de datos en UD3)

### Hecho

- Incorporado `03-machine-learning/01-teoria/05a-marco-crisp-dm.md` como marco breve, iterativo y transversal para proyectos de datos de UD3; enlazado desde el índice y la ruta recomendada de teoría.
- Delimitada la relación con Medallion: CRISP-DM organiza el proyecto de ML en PIA y Medallion conserva su papel de arquitectura de capas del dato en Sistemas de Big Data, sin duplicar contenido.
- Aplicada una trazabilidad CRISP-DM mínima al Lab1 de creación de datasets, al capstone de películas y a sus instrumentos de evaluación.
- Corregida `03-machine-learning/01-teoria/05-preparacion-datos-ml.md`: separación train/test antes de ajustar imputación, codificación y escalado; ejemplo reproducible con `ColumnTransformer` y `Pipeline`.
- Añadida la comprobación anti-fuga de datos al checklist y a la rúbrica del capstone.
- Auditados y reforzados los notebooks P1–P3: P1 queda como EDA; P2 y P3 ya separan antes de transformar, seleccionan con CV sobre entrenamiento y reservan test para la evaluación final única.
- Ejecutado el flujo equivalente de P3 con un dataset sintético temporal de 400 películas: `Pipeline`, `GridSearchCV` y evaluación final funcionaron; las métricas obtenidas son solo evidencia técnica, no resultados docentes.

### Pendiente real

- Ejecutar P2 y P3 con un `movies.csv` representativo antes de distribuirlos al alumnado, para comprobar dependencias, nombres de columnas y resultados sobre datos reales.

### Siguiente paso recomendado

Cuando esté disponible el dataset del capstone, ejecutar primero P3 y conservar como evidencia las métricas y el análisis de errores generados; después verificar P2 con el entorno PyCaret correspondiente.

## Continuación — 2026-07-28 (Capstone P2: flujo anti-fuga)

### Hecho

- Reforzados los notebooks de alumno y profesor de P2 (PyCaret) y su guía con un flujo reproducible: `train_size=0.8`, `session_id=42`, CV de 5 folds y métrica explícita (`F1`, justificable según el caso) para comparar/ajustar solo sobre entrenamiento.
- Se normalizaron los identificadores de celda de ambos notebooks P2 para `nbformat` 4.5. El notebook docente está ignorado por patrón, aunque no está versionado en este clon; deberá añadirse de forma explícita al consolidar esta corrección.
- La evaluación final se documenta mediante una única llamada a `predict_model(selected_model)` sobre el holdout reservado; se prohíbe ajustar o finalizar el modelo antes de esa comprobación. `finalize_model` queda solo para despliegue posterior y no es una nueva evaluación.
- Añadida evidencia mínima revisable: tabla de configuración, resultados de CV, ajustes y métricas/predicciones de holdout, sin inventar resultados.

### Siguiente paso recomendado

Reforzar P3 (modelo manual) con el patrón explícito `train_test_split` → `Pipeline`/CV sobre entrenamiento → evaluación final única en test.

## Continuación — 2026-07-28 (entorno Pixi aislado para P2/PyCaret)

### Hecho

- Creado `ud3-pycaret` como entorno Pixi autónomo para P2: Python 3.11, NumPy 1.26, pandas 2.1, SciPy 1.11, Jupyter e IPykernel junto con PyCaret 3.3.
- Reorganizada la base común como feature `base`; los entornos normales (`default`, `ud3`, `ud3-datasets`, `ud4`) la componen explícitamente, mientras que `ud3-pycaret` no la mezcla.
- Esta separación es necesaria porque PyCaret 3.3 admite NumPy `>=1.21,<1.27`, incompatible con NumPy 2 de la base docente; se ha fijado la serie 1.26 ya validada.
- Resuelto e instalado el entorno; `pixi lock --check` e importaciones de Python, NumPy, pandas, SciPy, scikit-learn y PyCaret han pasado.
- Ejecutado P2 sobre el dataset sintético temporal de 400 películas: holdout 80/20, CV de 5 folds y evaluación final se completaron correctamente. Las métricas son evidencia técnica, no resultados docentes.
- Validado `ud3-pycaret` desde un clon limpio, sin depender de archivos del repositorio original.
- Actualizadas la guía P2 y el manual de Pixi con el comando y la razón del aislamiento.
- Eliminada la referencia ejecutable a cuML: P2 es CPU-only. La guía y ambos notebooks cargan únicamente el CSV docente no versionado desde `03-machine-learning/03-practicas/midterm-capstone/Peliculas/Practica_Peliculas_OK/data/movies.csv` y distinguen ese dato del smoke test sintético temporal y del CSV bruto de Lab1.

### Pendiente real

- Ejecutar P2 y P3 con un `movies.csv` representativo antes de distribuirlos al alumnado, para comprobar columnas, resultados y análisis de errores sobre datos reales.
- Validar el nuevo lockfile y `ud3-pycaret` en Windows y macOS antes del inicio del curso.

### Siguiente paso recomendado

Construir y validar el dataset real del capstone; después repetir P2 y P3 con ese CSV antes de distribuirlos.

## Continuación — 2026-07-28 (FLAML experimental en UD3)

### Hecho

- Añadido `ud3-flaml` como entorno Pixi experimental que compone la base y UD3, sin GPU ni dependencias de PyCaret.
- Incorporado `03-machine-learning/02-ejemplos/flaml/` con un ejemplo autocontenido: holdout estratificado, búsqueda AutoML limitada por tiempo y evaluación final única con datos sintéticos.
- Actualizados el manual Pixi y la guía P2 para presentar FLAML como alternativa ligera en observación, no como requisito ni sustitución de PyCaret.
- Verificado el entorno y el ejemplo con datos sintéticos; sus métricas se consideran exclusivamente evidencia técnica.

### Pendiente real

- Valorar durante el curso FLAML con un dataset real y decidir si aporta suficiente valor docente para ampliar o sustituir alguna práctica de AutoML.

## Continuación — 2026-07-29 (portabilidad de rutas del capstone)

### Hecho

- Corregida la carga de `movies.csv` en los notebooks P2 y P3, tanto de alumnado como de profesorado: ya no depende de iniciar Jupyter en la raíz del repositorio.
- Los notebooks buscan de forma limitada la raíz de PIA desde el directorio de trabajo de Jupyter y cargan la ubicación única `03-machine-learning/03-practicas/midterm-capstone/Peliculas/Practica_Peliculas_OK/data/movies.csv`.
- Actualizadas las guías P2 y P3 para indicar que Jupyter puede iniciarse desde la raíz o desde la carpeta del notebook, manteniendo la misma ruta de datos y procedencia.
- Validada la carga desde los directorios reales de los cuatro notebooks con un `movies.csv` sintético temporal; P3 completó separación, `Pipeline` y `GridSearchCV` antes de la evaluación gráfica, y P2 cargó el CSV en su entorno aislado PyCaret. El fixture temporal fue eliminado.

### Pendiente real

- Construir y validar el `movies.csv` docente a partir de las fuentes de películas antes de distribuir el capstone: adquisición desde las APIs, emparejamiento entre fuentes, normalización de columnas y definición documentada de la variable objetivo.
- Validar los entornos Pixi en Windows/macOS antes del inicio del curso; la instalación desde clon limpio ya está comprobada.

### Siguiente paso recomendado

Diseñar primero el contrato del dataset docente `movies.csv` (fuentes, identificadores para emparejar, columnas, reglas de limpieza y variable objetivo); después implementar su adquisición reproducible a partir de Lab1.

## Continuación — 2026-07-29 (P3 ejecutable de extremo a extremo)

### Hecho

- Añadido `matplotlib >=3.8,<4` a la feature `ud3` de Pixi y actualizado `pixi.lock` para todas las plataformas declaradas.
- Verificado `pixi lock --check`, la importación de Matplotlib y la autonomía de `ud3-pycaret` (`PyCaret 3.3.2` con `NumPy 1.26.4`).
- Ejecutada la solución docente P3 desde su directorio real con un `movies.csv` sintético temporal: separación estratificada, `Pipeline`, `GridSearchCV`, métricas finales y `ConfusionMatrixDisplay` renderizada. El fixture fue eliminado.
- Ajustados los notebooks P3 para llamar explícitamente a `plt.show()` después de la matriz de confusión, de modo que el gráfico se renderice de forma visible en Jupyter.

### Pendiente real

- Sigue pendiente el dataset docente real y la validación del lockfile en Windows y macOS; el clon limpio ya está comprobado.

### Siguiente paso recomendado

Definir e implementar la adquisición y normalización reproducible del `movies.csv` docente antes de su distribución.

## Continuación — 2026-07-30 (migración de guías UD3 a Pixi)

### Hecho

- Migradas las guías operativas activas de UD3 que presentaban Poetry como flujo de trabajo: guía de proyecto, guía de datasets, ejemplos FastAPI y Streamlit, y actividad/plantilla de Lab3.
- Renombrada la guía de proyecto a `03-machine-learning/01-teoria/10-guia-proyecto-python-pixi.md` y actualizado su índice.
- Pixi queda como ruta operativa: `ud3`, `ud3-datasets` y `ud3-pycaret` se usan cuando la actividad ya tiene entorno PIA; FastAPI/Streamlit se presentan como proyectos Pixi independientes con su propio `pixi.toml` y `pixi.lock`.
- Poetry se mantiene solo como nota mínima para publicación de paquetes, sin comandos operativos.

### Pendiente real

- Ejecutar los ejemplos de FastAPI y Streamlit desde un proyecto Pixi independiente antes de distribuirlos, incluida la comprobación en Windows y macOS.

### Siguiente paso recomendado

Crear un proyecto temporal Pixi para cada ejemplo de despliegue y comprobar el arranque de Uvicorn y Streamlit; no modificar el entorno común de UD3 sin una necesidad curricular concreta.

## Continuación — 2026-07-31 (validación FastAPI/Pixi)

### Hecho

- Validada estáticamente la guía y el ejemplo FastAPI como proyecto Pixi independiente: no dependen del `pixi.toml` ni del `pixi.lock` comunes.
- Corregida la guía para incluir `scikit-learn`, necesario en tiempo de carga para el modelo serializado por el ejemplo.
- Se creó un proyecto temporal fuera del repositorio; Pixi pudo inicializar su manifiesto, pero no resolver las dependencias dentro del sandbox porque la caché habitual es de solo lectura y la descarga de `conda-forge` queda bloqueada por DNS/red. No se modificó el entorno común.

### Pendiente real

- Repetir la comprobación funcional de FastAPI en un entorno con acceso a `conda-forge`: resolver e instalar el proyecto temporal, crear o copiar `outputs/modelo_regresion.pkl`, arrancar `pixi run uvicorn main:app` y consultar `GET /` y `POST /predict`.
- Validar posteriormente el mismo flujo en Windows y macOS.

### Siguiente paso recomendado

Validar el dataset docente `movies.csv` del capstone. La comprobación funcional de Streamlit sigue pendiente en un entorno con acceso a `conda-forge`.

## Continuación — 2026-07-31 (validación Streamlit/Pixi)

- Validada estáticamente la guía y el ejemplo Streamlit como proyecto Pixi independiente: no dependen del `pixi.toml` ni del `pixi.lock` comunes.
- Corregida la guía para declarar las dependencias directas del ejemplo (`numpy` y `scikit-learn`) y acotar el artefacto a un modelo de scikit-learn serializado con `joblib`.
- La sintaxis de `app.py` se comprobó con `python -m py_compile`.
- Se creó un proyecto temporal fuera del repositorio y Pixi pudo inicializar su manifiesto, pero no resolver las dependencias dentro del sandbox: la descarga de `conda-forge` queda bloqueada por DNS/red (`Operation not permitted`). No se modificó el entorno común.
- Validación funcional completada por el usuario fuera del sandbox: el proyecto Pixi instaló las dependencias, Streamlit arrancó correctamente y la predicción respondió usando un modelo de demostración compatible.
- El aviso `Help agents write better Streamlit apps` de Streamlit 1.60.0 es una recomendación informativa de la CLI para instalar sus skills; no indica un fallo de la aplicación ni es necesario para el curso.

### Pendientes opcionales

- Probar el mismo flujo con un modelo docente real y en Windows/macOS cuando comience el curso y haya equipos disponibles; no bloquea la distribución porque el ejemplo funcional ya fue validado en Linux por el usuario.

### Siguiente paso recomendado

Retomar la construcción y validación del dataset docente `movies.csv` del capstone.

## Continuación — 2026-07-31 (pipeline reproducible del dataset del capstone)

### Hecho

- Definido el contrato `03-machine-learning/03-practicas/midterm-capstone/Peliculas/Practica_Peliculas_OK/DATASET_CONTRACT.md` para el snapshot local `data/movies.csv`: TMDB es la fuente principal y OMDb solo se consulta mediante el `imdb_id` obtenido desde TMDB.
- Implementado `mi_dataset_peliculas.build_capstone_dataset` y la tarea Pixi `capstone-movies-dataset`: adquiere, normaliza, valida y guarda el CSV local, junto con `movies.manifest.json` versionable (parámetros, esquema, recuentos, objetivo y SHA-256).
- El snapshot excluye IDs, títulos y métricas de valoración posteriores (`imdb_rating`, `vote_average`, `vote_count`). `rating_high` se deriva de OMDb (`imdbRating >= 7.0`) sin conservar el rating fuente.
- Añadidas validaciones automáticas de esquema, nulos, duplicados, rangos, valores binarios y balance mínimo de clases; los tests unitarios del contrato pasan sin claves ni red.
- Unificada P1, tanto alumnado como profesorado, con la ruta portátil que ya utilizan P2/P3. P3 incorpora además una exclusión defensiva de IDs y métricas prohibidas si aparecieran.

### Pendiente real

- [x] Generar el primer snapshot real con claves locales de TMDB y OMDb y revisar `movies.manifest.json`: completado el 2026-07-31 con 154 filas válidas y SHA-256 verificado.
- Ejecutar P2/P3 sobre ese CSV antes de distribuir el capstone.
- Validar después la reconstrucción controlada en Windows y macOS.

### Siguiente paso recomendado

Desde la raíz, con el `.env` local de Lab1 configurado: `pixi install --environment ud3-datasets` y `pixi run --environment ud3-datasets capstone-movies-dataset`; no distribuir el CSV hasta que P2 y P3 terminen contra ese snapshot.

## Continuación — 2026-07-31 (duplicados en la adquisición real del capstone)

### Hecho

- Reproducido y corregido el fallo `El snapshot contiene filas duplicadas` observado con las APIs reales. La causa era la paginación no estable de `discover/movie` ordenada por popularidad: una película puede cambiar de página durante la adquisición y repetirse con el mismo ID de TMDB.
- La adquisición deduplica ahora candidatos repetidos por ID de TMDB antes de consultar detalles y OMDb, y registra el recuento `duplicate_tmdb_candidates` en el manifiesto.
- No se ha relajado la validación final de filas duplicadas. Si dos IDs de TMDB distintos aparecen asociados al mismo `imdb_id`, el pipeline se detiene y muestra el conflicto en vez de ocultarlo.
- Añadidas pruebas de regresión para la repetición entre páginas y para el conflicto de identidad; pasan los 6 tests y la compilación de fuentes y tests.

### Pendiente real

- [x] Repetir la generación real del snapshot y revisar el manifiesto: completado el 2026-07-31; 154 filas, clases 62/92, un candidato TMDB duplicado descartado y SHA-256 coincidente.
- Ejecutar P3 y P2 contra el CSV resultante.
- Validar después la reconstrucción controlada en Windows y macOS.

### Siguiente paso recomendado

Ejecutar P3 contra el snapshot real y, si finaliza correctamente, validar después P2 en `ud3-pycaret`.

## Continuación — 2026-07-31 (primer snapshot real del capstone)

### Hecho

- Generado y validado `data/movies.csv` con 154 películas y el esquema docente acordado.
- Verificado `movies.manifest.json`: TMDB + OMDb por `imdb_id`, umbral `imdbRating >= 7.0`, 200 candidatos, un duplicado TMDB descartado, 3 películas sin `imdb_id`, una sin registro OMDb y 41 descartadas por contrato.
- Distribución de `rating_high`: 62 casos negativos (40,26 %) y 92 positivos (59,74 %).
- Comprobado que el SHA-256 del CSV coincide con el manifiesto: `0101bdc0c2e4df5b74366ab6bbd7ed9c35ba2a87586f59a56333df02e3758c84`.

### Pendiente real

- Ejecutar P3 y después P2 contra este snapshot real y revisar métricas, errores y adecuación pedagógica.
- Validar posteriormente la reconstrucción en Windows y macOS.

### Siguiente paso recomendado

Ejecutar P3 con el CSV real, conservando el test final para una única evaluación; después validar P2 en el entorno aislado `ud3-pycaret`.

## Continuación — 2026-07-31 (P3 ejecutado con el snapshot real)

### Hecho

- Ejecutada la solución docente `P3_Modelo_sol.ipynb` con las 154 filas del snapshot real mediante `nbconvert`, usando backend gráfico no interactivo y sin modificar el notebook fuente.
- Conservado el contrato anti-fuga: partición estratificada 80/20, preprocesamiento dentro de `Pipeline`, selección mediante `GridSearchCV` sobre entrenamiento y una única evaluación final sobre 31 casos de test.
- Mejor F1 media de validación cruzada: `0,7643`; Random Forest seleccionado con `n_estimators=200`, `max_depth=None` y `min_samples_leaf=2`.
- Métricas finales en test: accuracy `0,7419`, precision `0,7619`, recall `0,8421` y F1 `0,8000`.
- Revisados los ocho errores de clasificación mostrados por el notebook; no se han modificado los datos ni el modelo a partir del test final.

### Pendiente real

- Ejecutar P2 con el mismo snapshot en el entorno aislado `ud3-pycaret` y comparar sus evidencias de CV y test final.
- Validar posteriormente la reconstrucción y los entornos en Windows/macOS.

### Siguiente paso recomendado

Ejecutar P2 con `ud3-pycaret`, sin reutilizar el test para seleccionar o reajustar modelos.

## Continuación — 2026-07-31 (P2 ejecutado con el snapshot real)

### Hecho

- Ejecutada la solución docente `P2_PyCaret_sol.ipynb` con el snapshot real en el entorno aislado `ud3-pycaret`, mediante una copia temporal que no modifica el notebook fuente.
- PyCaret reservó 31 casos como holdout y utilizó 123 para entrenamiento con `StratifiedKFold` de 5 particiones.
- `compare_models(sort='F1')` seleccionó Ridge Classifier con F1 media `0,7521`; el ajuste sobre entrenamiento alcanzó F1 media `0,7563` (desviación `0,0598`).
- Evaluación final única sobre holdout: accuracy `0,5806`, AUC `0,5965`, recall `0,5263`, precision `0,7143` y F1 `0,6061`.
- El resultado queda como evidencia pedagógica: el rendimiento de CV no se trasladó al holdout y no se ha reajustado el modelo usando el test. P3 obtuvo F1 `0,8000` en el mismo holdout.

### Pendiente real

- [x] Revisar pedagógicamente la diferencia CV/holdout de P2: el usuario confirma que P2/P3 son utilizables para el curso y no se ampliará el snapshot ni se continuará optimizando estas prácticas en este bloque.
- Validar posteriormente la reconstrucción y los entornos en Windows/macOS.

### Siguiente paso recomendado

Consolidar el bloque actual de UD3/Pixi y volver a la revisión transversal del curso completo, priorizando carencias que afecten realmente a documentos, ejemplos o tareas del alumnado.

## Continuación — 2026-07-31 (bloqueos de revisión UD3/Pixi)

### Hecho

- Restaurado el contrato docente independiente de Lab1: `get_popular_movies`, `get_omdb_data`, `merge_tmdb_omdb` y `build_dataset.py` vuelven a generar el CSV exploratorio por título; el generador del capstone permanece separado en `build_capstone_dataset.py` y empareja solo por `imdb_id`.
- Corregido `experiment_MoviesDataSet.ipynb`: localiza `.env` correctamente, comprueba que ambas variables existen, no imprime sus valores y no conserva salidas con claves.
- Aplicado TDD estricto al contrato capstone: la validación rechaza cada columna cuyo dtype no coincida con `SCHEMA`; se añadieron pruebas negativas y pruebas de regresión del flujo Lab1.
- La escritura del snapshot y el manifiesto prepara y sincroniza archivos temporales antes de reemplazar los destinos; el hash del manifiesto se calcula sobre los bytes exactos del CSV preparado.
- Documentados el sesgo de muestreo por popularidad, la paginación inestable y el carácter constante de `adult` al usar `include_adult=false`; normalizadas a español neutro las instrucciones del contrato.

### Pendiente real

- No quedan bloqueos altos de esta revisión de UD3/Pixi. Las validaciones funcionales externas y multiplataforma siguen siendo no bloqueantes y se realizarán cuando corresponda durante el curso.

### Siguiente paso recomendado

Consolidar este bloque y continuar la revisión transversal del curso, sin profundizar más en P2/P3 salvo que el uso real en aula revele una necesidad concreta.

## Continuación — 2026-07-31 (coherencia transaccional del snapshot)

### Hecho

- Cerrado el último bloqueo de la re-revisión UD3/Pixi: `write_outputs()` conserva el par anterior de snapshot y manifiesto si falla la publicación del segundo archivo; una prueba simula exactamente ese fallo y verifica la restauración byte a byte.
- Añadida una prueba del camino correcto que comprueba la coincidencia entre el SHA-256 publicado y el CSV, y otra que demuestra que una ruta de snapshot externa al repositorio se rechaza antes de escribir.
- La CLI valida las rutas de snapshot y manifiesto antes de adquirir datos. Ambos destinos deben quedar dentro del repositorio y ser distintos.
- El notebook de exploración ya no depende de dónde se abra dentro del repositorio: localiza la raíz mediante `pixi.toml`, deriva la ruta exacta del proyecto y carga su `.env` sin imprimir valores secretos.

### Pendiente real

- No quedan bloqueos de la re-revisión UD3/Pixi. Las comprobaciones externas y multiplataforma permanecen como validaciones no bloqueantes para el curso.

### Siguiente paso recomendado

Consolidar el bloque UD3/Pixi y continuar la revisión transversal del material docente.

## Continuación — 2026-07-31 (navegación pública P0)

### Hecho

- Corregidas las 12 páginas `docs/unidades/ud01.md` a `ud12.md`: las cinco secciones de cada unidad apuntan a una página pública concreta, a la carpeta real del repositorio cuando contienen archivos no publicables, o indican expresamente que no hay material publicado.
- Añadida `docs/guia-inicio.md` como ruta común portal → clonar o descargar → elegir el entorno indicado → ejecutar notebooks o prácticas.
- Documentado que no existe un entorno único para todo el curso: solo se enumeran los entornos presentes en `pixi.toml` y, para el resto, se remite al README o al enunciado de la actividad.
- Añadida `scripts/check_public_unit_links.py`, integrada en el workflow de publicación, para comprobar las 60 secciones: 55 con destino y 5 marcadas sin material; los destinos de GitHub se contrastan además con rutas locales existentes.
- Verificados `mkdocs build --strict` y el comprobador de navegación: 12 unidades, 55 enlaces de sección válidos, 5 secciones sin material y cero enlaces internos rotos.

### Pendiente real

- Continuar la revisión transversal por UD9, UD4 y UD8, sin ampliar prácticas que ya son utilizables salvo que el trabajo en aula revele una necesidad.
- Mantener como no bloqueantes las validaciones externas de Moodle y las comprobaciones multiplataforma.

### Siguiente paso recomendado

Revisar UD9 desde la perspectiva del alumnado: orientación, ejemplos, prácticas, evaluación y comandos realmente ejecutables.

## Continuación — 2026-07-31 (ruta CPU/GPU de UD9)

### Hecho

- [x] Resuelta la contradicción sobre la evidencia CPU/GPU de UD9 en el README, el enunciado, la guía de prácticas, el checklist y la rúbrica.
- La evidencia evaluable de cuDF, cuML y benchmarking GPU requiere una GPU NVIDIA verificable.
- Google Colab con runtime GPU queda como ruta canónica para quien no disponga de GPU NVIDIA local; el profesorado puede indicar un runtime cloud equivalente.
- La ejecución CPU se admite para preparación y depuración, pero no como evidencia equivalente de aceleración GPU.
- Añadido un preflight breve para comprobar `nvidia-smi`, librerías, versiones y backend/dispositivo antes de empezar.
- Añadidos al preflight los comandos concretos para terminal y notebook/Colab.
- Actualizada la plantilla activa `01_project_template.ipynb`: el preflight falla sin GPU/RAPIDS, cuDF/cuML forman la ruta mínima obligatoria y sklearn queda únicamente como baseline CPU del benchmark.
- Ajustados `02_jax_intro.ipynb` y `03_gpu_benchmarks.ipynb`: CPU queda como demostración/depuración, no como evidencia evaluable; las mediciones JAX esperan el resultado con `.block_until_ready()` y las de RAPIDS sincronizan el stream CUDA.
- Alineados checklist y rúbrica: EDA con cuDF, entrenamiento con cuML y benchmark CPU/GPU son las tres evidencias obligatorias; JAX queda solo como ampliación o complemento.
- Actualizados los enlaces de entrada para dirigir al preflight, el enunciado y la evaluación canónica.

### Siguiente paso recomendado

Continuar la revisión transversal por UD4, sin ampliar prácticas ya utilizables salvo que la experiencia de aula lo justifique.

## Continuación — 2026-08-01 (ruta canónica de UD4)

### Hecho

- [x] Corregidos los enlaces locales activos de los laboratorios, capítulos de fundamentos y README de ejemplos que todavía apuntaban a nombres anteriores de la teoría UD4.
- [x] Definida una ruta corta teoría → laboratorios → evaluación; el entorno Pixi `ud4` es la vía local principal para PyTorch cuando corresponde.
- [x] Las recetas Conda/pip y los scripts especializados de Keras, JAX, TensorFlow, ONNX o MLX quedan etiquetados como contexto docente, no como rutas paralelas por defecto.

### Pendiente real

- No quedan bloqueos de navegación o elección de ruta en la entrada canónica de UD4. Las variantes especializadas sólo se validarán si se necesitan durante el curso.

### Siguiente paso recomendado

Continuar la revisión transversal por UD8, sin ampliar prácticas que ya son utilizables salvo que la experiencia de aula lo justifique.

## Continuación — 2026-08-01 (ruta canónica de UD8)

### Hecho

- [x] Corregida la entrada activa de UD8: teoría, evaluación y recursos ya no aparecen como vacíos o pendientes.
- [x] Definida una única ruta para el alumnado: teoría por bloques → notebooks base → evidencias evaluables → checklist y rúbrica.
- [x] Alineada la evaluación con las ubicaciones reales: segmentación en `02-ejemplos/` y tracking/XAI en `03-practicas/`.
- [x] Sustituida la referencia inexistente a `79_maskrcnn_instances.ipynb` por el notebook canónico `79_maskrcnn_pytorch.ipynb`.
- [x] Corregidos dos enlaces heredados de la guía activa de visión que todavía apuntaban a la antigua carpeta `modelado-notebooks/vision/`.
- Las soluciones, paquetes ZIP y materiales heredados quedan identificados como apoyo docente o ampliación, no como rutas paralelas por defecto.

### Pendiente real

- No quedan bloqueos de navegación o elección de material en la entrada canónica de UD8. Los notebooks se profundizarán solo si el uso durante el curso revela una necesidad concreta.

### Siguiente paso recomendado

Continuar la revisión transversal de rutas canónicas por UD2, UD5, UD6 y UD10, y después revisar los enlaces comunes de entrega y uso de IA.

## Continuación — 2026-08-01 (rutas canónicas de UD2, UD5, UD6 y UD10)

### Hecho

- [x] UD2 dirige desde su guía de unidad a `EDA_Visual_Practicas.ipynb`, con entrega, evaluación y dependencias reales identificadas; la evaluación ya no figura como pendiente.
- [x] UD5 adopta la comparativa de herramientas cloud como tarea canónica; la práctica AWS heredada queda como alternativa opcional condicionada a indicación y acceso.
- [x] UD6 adopta como entrega un proyecto integrado por el alumnado: el notebook `100` aporta la base RAG/trazabilidad y el `103`, que sirve Iris de forma independiente, aporta un patrón FastAPI que debe adaptarse; el notebook `99` queda como introducción.
- [x] UD10 dirige al proyecto final y al Torneo de Modelos; `01-teoria/requirements.txt` queda identificado como fuente real del entorno y guía/notebook usan rutas portátiles hacia los datasets existentes en `05-recursos/`, sin duplicarlos.
- [x] UD2 identifica rúbrica y checklist como base revisable, no como evaluación definitiva independiente de la programación del grupo.
- [x] Los enunciados o instrucciones evaluables canónicos de las cuatro unidades enlazan `docs/normas-entregas-y-uso-de-ia.md`.

### Pendiente real

- Solo permanecen validaciones externas o no bloqueantes: GIFT en Moodle, comprobaciones Windows/macOS cuando haya equipos disponibles y mejoras que revele el uso real en aula.

### Siguiente paso recomendado

No ampliar más estas unidades antes del curso. Revisar o reforzar una práctica concreta únicamente cuando la experiencia del grupo aporte evidencia de una necesidad docente.

## Continuación — 2026-08-01 (cierre transversal de normas y portada)

### Hecho

- [x] Actualizada la portada raíz al estado real del curso: operativamente terminado / semicerrado, evaluación normalizada, MCP integrado y Pixi como gestor operativo.
- [x] Enlazadas las normas comunes desde las rutas evaluables canónicas que faltaban: actividad de UD1, laboratorios de UD4, proyecto de UD7, ruta de entrega de UD8, proyecto GPU de UD9 y proyecto integrado de UD12.
- [x] Confirmada la cobertura completa de las unidades con evaluación ordinaria activa: UD1–UD10 y UD12.
- [x] UD11 queda excluida deliberadamente: es un anexo sin prácticas obligatorias y la única actividad evaluable opcional permanece en `90-archivo/`; no se reactiva material archivado.

### Pendiente real

- No queda ningún enlace transversal de normas pendiente en una ruta evaluable canónica activa. Los nuevos enunciados deberán incorporar el mismo recordatorio breve cuando se creen.

### Siguiente paso recomendado

Continuar la revisión transversal solo sobre carencias que afecten al uso real del curso; profundizar tareas concretas durante el curso si la experiencia del grupo lo justifica.

## Continuación — 2026-08-01 (saneamiento previo al traslado)

### Hecho

- Sustituidas las rutas absolutas heredadas de UD5 que apuntaban al antiguo árbol local del módulo por enlaces relativos portables.
- Revisadas las guías activas de RAG sencillo, RAG con Ollama, PageIndex, recuperación avanzada, guion de clase y chuleta de modelos Ollama.
- No se alteraron rutas legítimas de sistemas externos ni logs, outputs o material archivado.
- No quedan referencias al path local actual del repositorio en la documentación activa de UD5.

### Siguiente paso recomendado

Tras ejecutar las comprobaciones globales, mover el repositorio a `/datos/RafaelAlberti/RafaelAlberti26_27/Modulos/` y regenerar los entornos Pixi allí.

## Continuación — 2026-08-01 (traslado al destino final)

### Hecho

- Trasladado el módulo a `/datos/RafaelAlberti/RafaelAlberti26_27/Modulos/PIA`.
- Verificado que el repositorio Git reconoce correctamente la nueva raíz.
- Confirmado que los 12 enlaces simbólicos de `docs/` son relativos y resuelven correctamente.
- Confirmado que no quedan referencias al nombre de la ruta antigua.
- `pixi lock --check` y el comprobador público de navegación pasan tras el traslado.

### Pendiente externo del entorno

- [x] Ejecutados `pixi install` y `mkdocs build --strict` en la nueva ubicación; ambos finalizaron correctamente el 2026-08-01.

### Siguiente paso recomendado

Trabajar ya desde la ruta final y atender únicamente incidencias que aparezcan durante el curso.

## Cierre de traslado — 2026-08-01

- [x] El módulo está en `/datos/RafaelAlberti/RafaelAlberti26_27/Modulos/PIA`.
- [x] `pixi install` y `mkdocs build --strict` ejecutados correctamente desde la ruta final.
- [x] La ruta antigua ya no existe.

### Siguiente paso

Trabajar desde la nueva ubicación y registrar únicamente incidencias o mejoras que surjan durante el curso.

## Cierre de sesión — 2026-08-04

### Hecho

- Confirmada la validación funcional de Streamlit en Linux: el entorno Pixi instaló correctamente, la aplicación arrancó y realizó predicciones.
- Confirmado que el aviso sobre `streamlit skills` es informativo y no requiere instalar dependencias adicionales para el curso.
- Reclasificadas las comprobaciones con modelo docente real y en Windows/macOS como tareas opcionales para cuando comience el curso y haya equipos disponibles.

### Pendientes

- Ningún pendiente técnico bloqueante para Streamlit ni para el uso actual del módulo.
- Durante el curso: comprobar Windows/macOS si aparecen incidencias o equipos disponibles.

### Siguiente paso

Continuar mañana desde esta ruta y atender incidencias reales del curso.

## Revisión — 2026-08-10 (bases de datos de grafos)

### Resultado

- No hay ninguna base de datos de grafos integrada en un flujo obligatorio ni en los entornos actuales del curso.
- La guía de datasets de UD3 menciona `Neo4j` únicamente como ampliación; `cuGraph` en UD2 es análisis de grafos en GPU, no almacenamiento en una base de datos de grafos; `LangGraph` en UD6 modela orquestación con estado, no persistencia de datasets.
- Se mantiene como posible apéndice o variante opcional para representar el dataset de películas como grafo (películas, actores, directores, géneros y relaciones), sin alterar el CSV canónico ni introducirlo en el itinerario principal.

### Pendiente opcional

- [x] Preparar un apéndice práctico de Neo4j/Cypher para UD3; completado el 2026-08-11. La puesta en aula y la variante Python quedan como ampliaciones posteriores.

## Preparación — 2026-08-11 (apéndice de dataset como grafo)

### Hecho

- Preparado el diseño inicial con objetivo, alcance, modelo, criterios de aceptación y plan de trabajo.
- Fijada la decisión de tratar el grafo como una representación derivada del dataset tabular ya integrado, no como sustituto del CSV/Parquet canónico.
- Delimitado el primer alcance a Neo4j/Cypher, fixture local, consultas de relaciones y exportación de características para ML.
- Adoptada una secuencia didáctica de demostración breve del profesor seguida de una mini-tarea práctica en clase, sin convertirla en otro proyecto de UD3.
- Documentado el guion operativo para el aula: preparación previa, comprobación del contenedor, plan alternativo sin Docker y evidencias formativas de la mini-tarea.

### Resultado — 2026-08-11

- Convertido el plan en el apéndice visible y opcional `03-machine-learning/01-teoria/apendice-dataset-grafos.md`.
- Documentado un fixture local reproducible de películas, con nodos `Movie`, `Genre`, `Director` y `Actor`.
- Añadida una ruta de ejecución con Neo4j Community en Docker, sin modificar `pixi.toml` ni los entornos comunes.
- Incluida una carga idempotente con restricciones y `MERGE`, cuatro consultas Cypher y una consulta de características exportable a CSV para continuar con ML.
- Enlazado desde el índice de teoría y desde la guía de películas, siempre marcado como ampliación opcional.

### Validación técnica — 2026-08-11

- Comprobada estáticamente la secuencia documentada: el fixture tiene 8 filas y 4 películas; la agregación produce 4 filas de características y las consultas esperadas devuelven 2 películas de `Science Fiction` y 3 directores.
- Verificada la presencia de las restricciones, la carga con `LOAD CSV`, los `MERGE` y las columnas `genre_count`, `actor_count` y `director_count` en el apéndice.
- Validación funcional completada por el usuario: contenedor `neo4j:5.26-community` activo, restricciones creadas, fixture cargado, recarga idempotente confirmada (`0 changes`, 4 películas), consultas de género/director/colaboraciones/conexiones correctas y exportación de características ejecutada.
- Durante la prueba se identificó una diferencia de interfaz: la vista Workspace no mostraba el editor; se resolvió entrando en **Go to old browser**. No se modificaron `pixi.toml` ni los entornos comunes.

### Pendientes posteriores

- Revisar el apéndice durante la preparación de la clase y decidir si se mantiene como lectura/actividad no evaluable.
- Preparar la demostración y comprobar que la mini-tarea cabe en una sesión de clase.
- Conservar una copia local del fixture y de los bloques Cypher para el aula.
- La interfaz reciente de Neo4j puede abrir Workspace sin editor multilínea; la guía debe indicar **Go to old browser** para usar el editor Cypher clásico.
- Durante la prueba, Neo4j mostró un error al ejecutar una línea `FOR ...` aislada; se aclaró en la guía que cada restricción debe pegarse y ejecutarse como sentencia completa `CREATE CONSTRAINT ... FOR ...`.
- La exportación CSV requiere ejecutar la consulta de características, cambiar a vista `Table` y usar el icono de descarga situado arriba a la derecha del marco de resultados; se aclaró en la guía.
- Confirmada por el usuario la descarga del CSV de características; queda validado el puente Neo4j → tabla reutilizable para ML.
- Documentada una variante posterior para consultar Neo4j desde Python con el driver oficial `neo4j`; se recomienda una feature/entorno `ud3-graph` en lugar de cargarlo en `base` para todo el alumnado.

### Fuera de alcance por ahora

- No añadir Neo4j al entorno Pixi común.
- No rehacer P2/P3, introducir GNN/GraphRAG ni convertir el grafo en requisito del curso.

## Cierre — 2026-08-12 (variante Python del apéndice de grafos)

### Hecho

- Documentada la instalación opcional del driver oficial `neo4j` para consultar Neo4j desde Python.
- Documentada la alternativa recomendada `ud3-graph`, separada del entorno común, con ejemplo de conexión, `verify_connectivity()`, ejecución de Cypher y conversión a pandas.
- Confirmado que añadir el driver no instala el servidor: Neo4j continúa ejecutándose aparte mediante Docker.

### Pendientes reales

- No modificar `pixi.toml` hasta decidir que la variante Python se impartirá realmente.
- Antes de clase, conservar el fixture y los bloques Cypher; preparar la demostración y ajustar la mini-tarea a una sesión.
- Mantener como opcional la validación multiplataforma y cualquier ampliación posterior.

## Continuación — 2026-08-18 (consolidación del apéndice de grafos)

### Hecho

- Versionado el apéndice `03-machine-learning/01-teoria/apendice-dataset-grafos.md`, que hasta entonces estaba sin trackear (`??`) y no se habría distribuido con el repositorio.
- Incluidos en el mismo commit los dos enlaces que lo referencian: `03-machine-learning/01-teoria/README.md` (fila 12 del índice) y `03-machine-learning/01-teoria/08-guia-dataset-peliculas-que-hacer.md` (sección Herramientas).
- Commit: `ce0acdd` (`docs(ud3): add optional Neo4j/Cypher graph appendix`).

### Pendiente real

- Preparación de aula (demo y mini-tarea en una sesión, conservar fixture/Cypher), pendiente de la fecha de impartición.
- El `environment.yml` raíz sigue sin trackear por ser de otro bloque (auditoría de entorno); no se ha incluido en este commit.

## Continuación — 2026-08-18 (kit de aula del apéndice de grafos)

### Hecho

- Creado el kit de aula `03-machine-learning/03-practicas/actividades/grafo-peliculas/`:
  - `README.md`: inventario del kit y checklist de preparación docente;
  - `mini-tarea-alumnado.md`: ficha del alumnado de ~50 min (tareas 1-4 ejecutables y tarea 5 de reflexión) con valores de autocomprobación;
  - `fixture/movies_graph.csv`: copia local del fixture (8 filas, 4 películas);
  - `cypher/00-restricciones.cypher`, `01-carga.cypher`, `02-consultas-ejemplo.cypher`, `03-caracteristicas.cypher` (públicos);
  - `demo-profesor.md` y `cypher/04-mini-tarea-solucion.cypher` quedan como **material docente local no versionado** (reglas `*profe*` y `*-sol*` del `.gitignore`), coherente con la política del repo; no se enlazan desde material público.
- Añadida excepción en `.gitignore` para versionar `fixture/movies_graph.csv` (mismo patrón que `boston-housing/data/housing.csv`).
- Enlazada la mini-tarea desde la secuencia didáctica del apéndice `03-machine-learning/01-teoria/apendice-dataset-grafos.md`; el guion docente y las soluciones se referencian solo de forma textual.
- Commits: `9fd99be` (`docs(ud3): add classroom kit for Neo4j graph appendix`) y `03cb640` (`fix(ud3): keep teacher-only graph kit material local`).
- Verificados `mkdocs build --strict` y el comprobador público de navegación (12 unidades, 60 secciones, cero enlaces rotos).

### Pendiente real

- Preparación de la clase propiamente dicha cuando haya fecha de impartición (arrancar contenedor, cargar fixture, repasar resultados esperados).
- La variante Python (`ud3-graph`) sigue sin decidirse para el curso; no se toca `pixi.toml` hasta esa decisión.

## Continuación — 2026-08-18 (ruta programática de grafos y cierre del punto UD4)

### Hecho

- Cerrado el punto "decidir el destino de `used-cars-dl-tabular`, `boston-housing` y `blackfriday`": ya estaba resuelto en `04-deep-learning/00-decisiones-reorganizacion.md` y `00-pendientes-revision.md`. Las tres se mantienen en UD4 (práctica documental, práctica documental, recurso opcional) y no pasan a evaluables reproducibles salvo necesidad real durante el curso.
- Implementada la **ruta programática** de Neo4j, que es el objetivo del módulo (Programación de IA):
  - `pixi.toml`: añadida la feature `ud3-graph` con `neo4j-python-driver = ">=6,<7"` (en conda-forge el paquete se llama así; en PyPI `neo4j`) y el entorno `ud3-graph = ["base", "ud3", "ud3-graph"]`.
  - `03-machine-learning/02-ejemplos/grafo-peliculas-python/`: ejemplo `grafo_a_ml.py` + `README.md` que consulta Neo4j, convierte a pandas y alimenta un `KMeans` de scikit-learn con las características del grafo.
  - Apéndice: la sección 5 pasa de "variante posterior" a "ruta programática" recomendada, con el paquete conda-forge correcto y el ejemplo.
  - Mini-tarea: añadida ampliación programática opcional; kit README actualizado.
- Validación funcional: contenedor `neo4j:5.26-community` arrancado, restricciones y fixture cargados (4 películas), `grafo_a_ml.py` ejecutado de extremo a extremo con características coincidentes y clústeres reproducibles (`random_state=42`). Fallo controlado sin `NEO4J_PASSWORD` comprobado (exit 2). Contenedor detenido después de la prueba.
- `pixi.lock` regenerado para las cuatro plataformas con la nueva feature.
- Gotcha documentado en apéndice y kit: al montar una carpeta del host como `/var/lib/neo4j/import`, la imagen Neo4j cambia su propietario al UID 7474 y bloquea el acceso del usuario; restaurar con `sudo chown -R $(id -u):$(id -g)` al terminar o montar una copia desechable. Ocurrió en esta validación y se resolvió con un contenedor root.

### Pendiente real

- El día de la clase de grafos: arrancar el contenedor, cargar el fixture y repasar `demo-profesor.md`.
- Validar la reconstrucción de `ud3-graph` en Windows/macOS cuando haya equipos (no bloqueante).

## Cierre de sesión — 2026-08-22 (repositorios, publicación y sincronización)

### Hecho

- [x] Confirmado `graphify` instalado y ejecutado en este proyecto: versión `0.9.46`, corpus de 564 archivos, 2.655 nodos, 3.508 aristas y 332 comunidades.
- [x] Creado el repositorio privado docente `IES-Rafael-Alberti/programacion-inteligencia-artificial-docente`.
- [x] Subida la rama docente local `teacher` al repositorio privado como `main`.
- [x] Incorporados al repositorio privado la planificación, el material `99-profesor`, el archivo histórico, Graphify, `environment.yml`, las notas de continuidad y la estrategia de trabajo.
- [x] Excluidos del repositorio privado los secretos de `99-sensible`, entornos instalados, `site`, configuración local del agente y el notebook docente de 225 MB rechazado por el límite de GitHub; este último permanece local.
- [x] Verificado que el repositorio público del alumnado sigue siendo `origin/main` y que GitHub Pages conserva el workflow configurado.
- [x] Corregidos los enlaces de recursos de UD3 y UD10 y publicado el arreglo en `origin/main`.
- [x] Workflow de GitHub Pages completado correctamente en el commit `27ae2799`; navegación validada: 12 unidades, 60 secciones, 55 destinos y 5 secciones explícitamente sin material.
- [x] Documentada en `ESTRATEGIA_REPOSITORIOS.md` la estrategia de dos remotos, publicación selectiva, trabajo con dos ordenadores, Unison y disco duro.
- [x] Configurada la rama local `main` para seguir `origin/main`; `teacher` sigue `teacher/main`.

### Pendientes reales

- Ningún pendiente técnico bloqueante de esta sesión.
- Antes de cambiar de ordenador, ejecutar Unison con editores, Jupyter, Pixi y Git cerrados, revisar las propuestas y después actualizar GitHub en el equipo receptor.
- Mantener como tareas de curso las comprobaciones Windows/macOS y la preparación de aula del apéndice de grafos; no bloquean la reorganización.

### Siguiente paso recomendado

En la próxima sesión, comprobar el resultado de la copia Unison y continuar trabajando desde `teacher`. Pasar cambios a `origin/main` sólo mediante selección explícita de archivos públicos, validación MkDocs y comprobador de navegación.


## Revisión — 2026-09-30 (Graphify, Moodle y orden de Python)

### Comprobado

- [x] Revisados `graphify-out/graph.json`, la hoja de ruta, la checklist Moodle, el paquete inicial y los índices y contenidos de teoría UD1. No se ha accedido a Moodle ni se ha publicado ningún recurso en esta revisión.
- [x] El JSON actual conserva 2.655 nodos, 3.508 aristas, 332 comunidades y 62 hiperconexiones: cero extremos ausentes en aristas e hiperconexiones y cero rutas de origen inexistentes. La cifra histórica de 423 no describe este JSON. `built_at_commit` apunta a `fb91cdcd` (2026-08-18); la fecha reciente del archivo no garantiza una extracción reciente.
- [x] El grafo no contiene nodos de origen para `00-planificación/CHECKLIST_MOODLE_UD1_2026_2027.md` ni `Moodle/00-inicio-ud1/README.md`; estos documentos deben consultarse directamente. La CLI Graphify no está disponible en el entorno revisado; se inspeccionó el JSON sin instalar ni regenerar nada.
- [x] Localizado el plan de publicación en `00-planificación/CHECKLIST_MOODLE_UD1_2026_2027.md` y su inventario de 10 archivos en `Moodle/00-inicio-ud1/README.md`. El paquete es de arranque, no reúne toda la teoría ni todos los notebooks UD1.
- [x] La única importación Moodle explícitamente registrada en esa checklist es el diagnóstico técnico inicial, no evaluable. El resto de las casillas de publicación siguen sin confirmar: preparar PDFs o publicar en GitHub Pages no demuestra una subida a Moodle.
- [x] La dosificación documentada consiste en publicar el siguiente notebook tras completar el inicio y abrir evaluación sólo con enunciado, rúbrica y plazo. No se ha encontrado una justificación técnica para retener toda la documentación de consulta de Python.
- [x] Detectada una incoherencia real en `01-fundamentos-python/01-teoria/05-guia-numpy-jax.md`: es una guía heredada de NumPy/Pandas, no una explicación de JAX; menciona notebooks con nombres antiguos. El commit `6e48e0df` renombró la guía semanal y la introducción NumPy sin cambiar sus contenidos. El índice actual coloca rendimiento (`05`) antes de introducción NumPy (`06`) y usa esa misma guía como apoyo de JAX (`08`).

### Recomendación pendiente de confirmación

- [ ] Publicar ya la documentación de consulta de Python y los ejemplos guiados destinados al alumnado, manteniendo el ritmo de trabajo indicado en clase. No incluir soluciones, `99-profesor/`, GIFT con respuestas ni abrir futuras tareas evaluables automáticamente.
- [x] Corregida la guía heredada y alineada la secuencia: teoría `05-numpy-introduccion.md` + notebook `05_numpy_fundamentos.ipynb` → `06_numpy_rendimiento.ipynb` → broadcasting `07` → guía `08-guia-numpy-jax.md` y notebook JAX `08`. La guía explica la mejora posterior a NumPy, sin presentar Pandas como contenido del bloque.
- [x] Actualizados el índice activo de teoría y los títulos de los notebooks renumerados. No se encontraron referencias a estas cuatro rutas antiguas en el guion docente, checklist Moodle o inventario del paquete inicial: sus 10 archivos de arranque no incluyen los materiales renombrados, por lo que no necesitan regenerarse.
- [ ] Confirmar con el docente o mediante acceso autorizado qué archivos están realmente visibles en Moodle; después actualizar la checklist y registrar fecha y alcance de publicación. La validación de los GIFT base UD1/UD2 sigue pendiente, pero no se atribuye a mantenimiento sin verificarlo.

### Rutas y siguiente paso

- [x] Revisión independiente de los cambios aprobada para consolidación docente; publicación web aún requiere build estricto y comprobación de navegación.
- [x] Generados 12 PDFs de teoría y recursos de consulta de Python UD1 en `Moodle/01-ud1-documentacion-python/`, con índice de fuentes y destinos. Se preservan los Markdown originales; no se convierten notebooks, ejercicios, evaluación ni documentos ajenos a Python.
- [ ] Subir los 12 PDFs de consulta de Python a Moodle y verificar su visibilidad con una cuenta de alumnado; la generación local no equivale a publicación.
- [ ] Antes de publicar el notebook `08_introduccion_jax_comparativa.ipynb`, ajustar el benchmark: tipos numéricos equivalentes en NumPy/JAX y tamaño de arrays adecuado para equipos de aula. Es una incidencia preexistente y no bloquea publicar la documentación teórica de consulta.
- Rutas modificadas: `ESTADO_ACTUAL_Y_PENDIENTES.md`, `01-fundamentos-python/01-teoria/README.md`, teoría NumPy `06` → `05`, guía NumPy/JAX `05` → `08`, notebook fundamentos `06` → `05` y notebook rendimiento `05` → `06`. El grafo y los archivos Moodle de arranque se han conservado.
- Siguiente paso recomendado: revisar la corrección NumPy/JAX y confirmar la publicación de consulta completa; después preparar el inventario ampliado Moodle y comprobarlo con una cuenta de alumnado. La subida real sigue pendiente.
- Las menciones a mantenimiento en cierres históricos describen su fecha de registro, no un bloqueo vigente. Para el estado actual prevalece esta revisión y los pendientes de cabecera.

- [x] Validaciones locales: notebooks renombrados parsean como JSON y conservan las celdas de código y sus salidas; enlaces locales de la guía y destinos del índice comprobados, sin referencias antiguas en documentos activos. `git diff --check` sin errores. Graphify no se actualiza porque su CLI no está disponible; sus rutas NumPy renombradas quedan pendientes de refresco.
