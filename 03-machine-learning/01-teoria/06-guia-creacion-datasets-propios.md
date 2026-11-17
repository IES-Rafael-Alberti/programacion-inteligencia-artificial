# Crear un dataset propio para un proyecto de ML

Un proyecto de machine learning no empieza eligiendo un algoritmo: empieza por aclarar qué problema se quiere resolver y qué datos hacen falta. Esta guía recorre las decisiones básicas para construir un conjunto de datos útil, trazable y adecuado para la pregunta.

La guía complementa el [marco CRISP-DM](05a-marco-crisp-dm.md) y la [preparación de Titanic para modelado](05-preparacion-datos-ml.md). No es necesario crear un dataset desde cero si ya existe uno que responde bien al problema.

## Ruta rápida

1. Define el problema, la población y qué representa cada fila.
2. Busca primero datos existentes y comprueba si puedes usarlos.
3. Si hace falta, recoge datos de fuentes autorizadas y conserva los originales.
4. Integra las fuentes con claves, unidades y periodos coherentes.
5. Revisa calidad, etiquetas, ausencias y posibles sesgos.
6. Documenta el esquema, la procedencia y las transformaciones.
7. Guarda una versión reproducible y prepara el uso posterior en ML.

## 1. Define qué datos necesitas

Antes de recopilar datos, escribe la pregunta que quieres responder. Concreta:

- **Problema y uso:** ¿qué decisión o análisis se quiere apoyar y quién utilizará el resultado?
- **Población:** ¿sobre qué personas, objetos o periodos se quiere aprender?
- **Unidad de observación:** ¿qué representa una fila: una persona, una película, un día o una medición?
- **Objetivo:** si es aprendizaje supervisado, ¿qué columna será `y` y cómo se obtendrá su etiqueta?
- **Momento de predicción:** ¿en qué instante habría que producir la predicción y qué información estaría disponible entonces?

La última pregunta ayuda a evitar **fuga de información**. Si quieres predecir un hecho futuro, no incluyas como característica una variable que solo se conocería después. La separación entre entrenamiento y prueba y el ajuste correcto de transformaciones se trabajan en la [guía de preparación de datos](05-preparacion-datos-ml.md).

### Ejemplo: estimar la temperatura máxima del día siguiente

Una fila puede representar una ciudad y una fecha. La variable objetivo sería la temperatura máxima del día siguiente. Solo podrían usarse como características los datos disponibles en el momento de hacer esa predicción; la temperatura observada mañana no puede formar parte de `X`.

| fecha | ciudad | temperatura mínima hoy | precipitación hoy | temperatura máxima mañana (`y`) |
|---|---|---:|---:|---:|
| 2026-01-10 | Cádiz | 11.2 | 0.0 | 17.4 |

Los valores son ilustrativos. En un proyecto real habría que definir la fuente, las unidades, la zona horaria y cómo se resuelven los días sin mediciones.

## 2. Elige una fuente adecuada

Busca primero si existe un conjunto de datos que se ajuste al problema. Crear y mantener uno propio cuesta tiempo; puede bastar con seleccionar, combinar o ampliar fuentes existentes.

| Fuente posible | Ejemplo de uso | Comprobaciones importantes |
|---|---|---|
| Datos abiertos o repositorios públicos | Estadísticas, transporte, meteorología | Licencia, fecha de actualización, cobertura y diccionario de datos |
| API | Datos de un servicio en línea | Condiciones de uso, límites de consulta, autenticación y cambios de versión |
| Encuestas u observaciones propias | Respuestas o mediciones recogidas para el proyecto | Consentimiento, privacidad, diseño de la muestra y criterios de etiquetado |
| Registros o sensores | Eventos de una aplicación o mediciones físicas | Permisos de acceso, calidad, frecuencia, unidades e identificadores |
| Páginas web | Información no ofrecida en un formato estructurado | Condiciones del sitio, derechos sobre el contenido, privacidad y restricciones de acceso |

Antes de usar los datos, comprueba quién los publica, qué licencia o condiciones se aplican, si contienen datos personales y si su uso previsto está permitido. No publiques claves API, contraseñas ni datos personales en el código o en el repositorio. No intentes eludir límites técnicos o controles de acceso.

## 3. Conserva la procedencia

Guarda una copia sin modificar de cada fuente descargada cuando las condiciones de uso lo permitan. Registra junto al proyecto:

- URL o entidad de origen y fecha de obtención;
- licencia y condiciones relevantes;
- periodo y población cubiertos;
- filtros, consultas o parámetros de descarga;
- versión de la fuente y transformaciones realizadas.

Mantener los originales separados de las versiones procesadas permite revisar errores y repetir la integración. No guardes secretos ni copias de datos personales que no sean necesarios.

## 4. Integra las fuentes con cuidado

Al combinar fuentes, define cómo se identifica cada entidad y qué significa cada fila. Antes de hacer un `merge` o `join`, comprueba:

- que las claves tienen el mismo significado y formato;
- si la clave es única o aparecen varias filas por entidad;
- que fechas, zonas horarias y unidades son compatibles;
- qué hacer con entidades que solo aparecen en una fuente;
- si la unión ha creado o eliminado duplicados.

No unas tablas solo porque tengan una columna con el mismo nombre. Una clave incorrecta puede multiplicar filas o asociar datos a entidades equivocadas.

## 5. Revisa la calidad antes de modelar

Haz una exploración inicial del conjunto integrado. Comprueba, al menos:

- número de filas y columnas y significado de cada fila;
- nombres, tipos y unidades de las columnas;
- valores ausentes, duplicados y categorías inesperadas;
- rangos imposibles o inconsistencias entre fuentes;
- distribución de la variable objetivo y posibles problemas de etiquetado;
- representación de los grupos relevantes para el problema.

Decide y documenta cómo tratar cada problema; no elimines filas ni imputes valores de forma automática. El análisis describe el conjunto que tienes, no demuestra que represente a toda la población.

## 6. Construye una tabla entendible

Para un problema tabular, cada fila debe representar una observación y cada columna una variable con un significado definido. Acompaña el archivo con un diccionario de datos:

| Columna | Significado | Tipo/unidad | Procedencia |
|---|---|---|---|
| `fecha` | Día de la observación | Fecha, zona horaria indicada | Fuente meteorológica |
| `temperatura_minima` | Mínima observada ese día | °C | Fuente meteorológica |
| `temperatura_maxima_manana` | Objetivo: máxima del día siguiente | °C | Fuente meteorológica |

Separa identificadores, características y objetivo de manera explícita. En el entrenamiento, `y` no debe aparecer dentro de `X`, ni tampoco una copia o variable derivada que revele directamente su valor.

Las transformaciones que **aprenden parámetros de los datos** —por ejemplo, imputación, escalado o codificación basada en categorías observadas— deben ajustarse después de separar entrenamiento y prueba, y solo con entrenamiento. En scikit-learn, un `Pipeline` ayuda a mantener ese orden; véase la [guía de preparación de datos](05-preparacion-datos-ml.md).

## 7. Elige un formato de almacenamiento

| Formato | Útil cuando | Consideraciones |
|---|---|---|
| CSV | Se quiere compartir una tabla sencilla y legible | No conserva tipos de forma fiable; acuerda delimitador, codificación y representación de ausentes |
| Parquet | Se trabaja con tablas y conviene preservar tipos y comprimir | Es binario; se lee con herramientas compatibles, como pandas con PyArrow |
| JSON | La fuente tiene objetos anidados o estructura variable | Puede requerir normalización antes de convertirlo en una tabla para ML |

Conserva los datos brutos separados del dataset integrado y de cualquier resultado generado por el modelado. El formato final debe facilitar tanto el uso previsto como la repetición del proceso.

## 8. Checklist antes de compartir

- [ ] La pregunta, población y unidad de observación están definidas.
- [ ] La fuente y sus condiciones de uso están registradas.
- [ ] Cada fila y columna tienen un significado claro.
- [ ] Se han comprobado duplicados, ausencias, tipos, unidades y etiquetas.
- [ ] Las uniones entre fuentes se han validado.
- [ ] No se han incluido secretos ni datos personales innecesarios.
- [ ] El objetivo `y` está separado de las características `X`.
- [ ] Las transformaciones que aprenden de los datos se ajustan solo con entrenamiento.
- [ ] El formato, la procedencia y los pasos para reproducir el dataset están documentados.

## Referencias y continuidad

- [CRISP-DM en UD3](05a-marco-crisp-dm.md): ciclo de trabajo y evidencia esperada.
- [Preparación de Titanic para ML](05-preparacion-datos-ml.md): separación train/test y pipeline sin fuga.
- [Portal de datos abiertos de España](https://datos.gob.es/).
- [Reglamento General de Protección de Datos (RGPD)](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
