# Guía del Proyecto Final — PIA

## Resumen rápido

El proyecto final de PIA es un trabajo progresivo, realizado en equipo, en el que cada grupo elige un problema realista y construye una solución con datos, integración, IA/ML y una salida útil para usuarios o para la toma de decisiones.

La idea no es entregar un notebook aislado al final del curso. El proyecto debe crecer durante el módulo mediante hitos: propuesta, fuentes de datos, integración, modelo base, pipeline, interfaz, seguimiento responsable y defensa final.

> **Regla clave:** el tema es libre, pero el proyecto debe integrar al menos dos fuentes de datos de forma real y justificada.

> **Relación con UD7**: el proyecto de stack convergente de UD7 (`../../07-convergencia-herramientas/01-teoria/10_stack_convergente.md`) puede servir como ensayo, checkpoint técnico o base reutilizable. Para que cuente dentro del proyecto final de módulo, debe adaptarse al tema del equipo, incorporar al menos dos fuentes de datos e integrarlas con sentido.

## Modelo de trabajo del módulo

Durante el curso se combinarán dos líneas de trabajo:

| Línea | Finalidad | Resultado esperado |
|---|---|---|
| Mini-proyectos guiados comunes | Practicar técnicas concretas con apoyo docente | Base técnica compartida para todo el grupo |
| Proyecto final progresivo | Aplicar esas técnicas a un problema elegido por el equipo | Producto defendible, documentado y con integración real |

Los mini-proyectos sirven como andamiaje. El proyecto final sirve para demostrar autonomía, criterio técnico y capacidad de integrar piezas.

La UD7 aporta una referencia especialmente útil para la parte de ingeniería de producción: Prefect como orquestador principal, FastAPI, MLflow, Evidently, explicabilidad e indexación jerárquica con LlamaIndex + CrewAI cuando el proyecto incluya RAG o agentes.

## Qué debe demostrar el proyecto

Al finalizar, el equipo debe poder explicar con claridad:

1. Qué problema aborda.
2. Qué datos utiliza y por qué son adecuados.
3. Cómo integra varias fuentes de información.
4. Qué limpieza, transformación o curación ha realizado.
5. Qué componente de IA/ML aporta valor.
6. Qué salida útil ofrece.
7. Cómo se ha construido, probado y documentado.
8. Qué limitaciones, riesgos y mejoras futuras tiene.

## Requisitos obligatorios

### Checklist mínimo

- [ ] El tema es elegido libremente por el equipo y está validado por el profesor.
- [ ] Usa al menos dos fuentes de datos diferenciadas.
- [ ] Integra esas fuentes de forma real, no mediante una simple concatenación sin criterio.
- [ ] Incluye limpieza, curación o transformación de datos.
- [ ] Contiene un componente de IA/ML justificable.
- [ ] Produce una salida útil: API, dashboard, informe, asistente, recomendador, predicción, alerta, ranking u otra interfaz razonada.
- [ ] Mantiene una estructura de repositorio clara.
- [ ] Documenta decisiones técnicas, uso, datos y limitaciones.
- [ ] Se defiende oralmente con evidencias del trabajo realizado.

### Tema libre, pero con ambición suficiente

El proyecto puede pertenecer a cualquier dominio: videojuegos, deporte, movilidad, educación, economía, atención al cliente, medio ambiente, cultura, redes sociales, comercio, industria u otros.

La libertad de tema no significa que cualquier alcance sea válido. Si la propuesta es demasiado simple, el profesor podrá devolverla para ampliar fuentes, integración, dificultad técnica o utilidad.

### Mínimo de dos fuentes de datos

Una fuente de datos puede ser, por ejemplo:

- API pública o privada.
- Dataset descargado.
- Base de datos propia.
- Datos abiertos de administraciones públicas.
- Web scraping permitido y documentado.
- Logs o eventos generados por una aplicación.
- Documentos, PDFs o textos usados como base de conocimiento.
- Imágenes, audio o vídeo si el proyecto lo justifica.

No cuenta como segunda fuente dividir artificialmente un único CSV en dos ficheros.

### Integración real

La integración debe aportar información nueva o permitir una decisión mejor que la que ofrecería cada fuente por separado.

Ejemplos de integración válida:

| Proyecto | Fuente 1 | Fuente 2 | Integración real |
|---|---|---|---|
| Jugadores infravalorados | Estadísticas deportivas | Salarios o valor de mercado | Comparar rendimiento frente a coste |
| Aparcamiento inteligente | Cámaras/matrículas | Tarifas y ocupación | Calcular estancia, facturación y disponibilidad |
| Estrategia en videojuego | Historial de partidas | Datos de mapas/personajes | Recomendar composiciones o rutas de ataque |
| Soporte al cliente | Tickets históricos | Base de conocimiento | Clasificar incidencias y sugerir respuestas fundamentadas |

Ejemplos de integración débil:

- Unir dos CSV porque tienen una columna parecida, sin explicar qué mejora aporta.
- Mostrar varias gráficas independientes sin relación entre ellas.
- Entrenar un modelo con una fuente y mencionar otra solo en la memoria.
- Añadir datos manuales decorativos que no afectan al análisis ni al resultado.

### Limpieza y curación de datos

El equipo debe demostrar que los datos no se han usado “tal cual” sin revisión.

Debe quedar documentado, según proceda:

- Valores nulos, duplicados o inconsistentes.
- Normalización de formatos, fechas, unidades o nombres.
- Filtrado de registros irrelevantes.
- Enriquecimiento o unión entre fuentes.
- Tratamiento de categorías raras o valores extremos.
- Trazabilidad básica del origen de los datos.

### Componente de IA/ML

El proyecto debe incluir una técnica de IA, aprendizaje automático o procesamiento inteligente de información.

Puede ser, entre otras:

- Clasificación.
- Regresión o predicción.
- Clustering o segmentación.
- Sistemas de recomendación.
- Búsqueda semántica o RAG.
- Detección de anomalías.
- Visión por computador.
- Procesamiento de lenguaje natural.
- Optimización o priorización asistida por datos.

La técnica elegida debe estar conectada con el problema. No basta con “poner un modelo” si no mejora la solución.

### Salida útil

El proyecto debe producir algo que pueda ser usado, evaluado o interpretado.

Opciones válidas:

- API con endpoints documentados.
- Dashboard interactivo.
- Informe analítico con conclusiones reproducibles.
- Asistente basado en datos propios o documentos del proyecto.
- Sistema de recomendación.
- Predicción, ranking o alerta.
- Prototipo de aplicación con interfaz sencilla.
- Pipeline que genere resultados periódicamente.

La salida debe estar alineada con el usuario objetivo del proyecto.

## Fase inicial de validación

Antes de construir, cada equipo debe presentar una propuesta breve. El objetivo es detectar pronto proyectos demasiado vagos, demasiado simples o inviables.

### Plantilla de propuesta

El equipo entregará una propuesta con esta estructura:

| Apartado | Pregunta que debe responder |
|---|---|
| Título provisional | ¿Cómo se llama el proyecto? |
| Problema | ¿Qué necesidad, decisión o proceso se quiere mejorar? |
| Usuarios | ¿Quién usaría el resultado? |
| Fuentes de datos | ¿Qué dos o más fuentes se usarán? |
| Integración | ¿Cómo se relacionarán esas fuentes? |
| IA/ML previsto | ¿Qué técnica se plantea y para qué? |
| Salida final | ¿Qué se entregará: API, dashboard, asistente, informe, recomendador...? |
| Versión mínima viable | ¿Qué versión reducida permitiría demostrar que la idea funciona? |
| Riesgos | ¿Qué puede fallar: datos, permisos, dificultad, tiempo...? |

### Criterios de devolución o rechazo

La propuesta se devolverá para revisión si ocurre alguno de estos casos:

- Solo hay una fuente de datos real.
- Las fuentes no se integran entre sí.
- El proyecto se limita a un notebook descriptivo.
- No existe componente de IA/ML claro.
- La salida final no tiene utilidad identificable.
- El alcance es tan amplio que no se puede completar durante el módulo.
- El alcance es tan pequeño que no demuestra competencias suficientes.
- Depende de datos inaccesibles, privados o no autorizados.
- Es una copia directa de un notebook de Kaggle u otro recurso.

### Versión mínima viable

Cada proyecto debe definir una versión mínima viable. Esta versión no es el proyecto completo, sino la primera prueba seria de que la idea puede funcionar.

Debe incluir:

- Una muestra de las fuentes de datos.
- Una integración inicial entre ellas.
- Una limpieza básica.
- Un modelo o baseline sencillo.
- Una salida mínima interpretable.

Ejemplo: en un proyecto de jugadores infravalorados, la versión mínima podría combinar estadísticas de rendimiento y salarios, calcular un indicador simple de valor y mostrar un ranking inicial antes de entrenar modelos más avanzados.

## Hitos del proyecto durante el curso

Los hitos ayudan a repartir el trabajo y evitan que el proyecto aparezca de golpe al final.

| Momento | Hito | Evidencia esperada |
|---|---|---|
| Inicio | Propuesta validada | Documento breve con problema, fuentes, integración y salida prevista |
| Primer tramo | Fuentes de datos e integración | Datos localizados, permisos revisados y primer cruce entre fuentes |
| Desarrollo inicial | Baseline de modelo | Modelo simple o regla base para comparar mejoras posteriores |
| Desarrollo medio | Pipeline y seguimiento | Proceso reproducible, idealmente con MLflow u otra trazabilidad equivalente |
| Desarrollo medio-final | API o interfaz | Forma usable de consultar resultados o interactuar con el sistema |
| Cierre técnico | Monitorización y uso responsable | Limitaciones, sesgos, métricas, errores y riesgos documentados |
| Final | Defensa | Presentación, demo, repositorio y memoria técnica |

## Familias de proyectos posibles

Los siguientes ejemplos son orientativos. Se pueden adaptar, combinar o sustituir por otras ideas con suficiente integración.

### Videojuegos multijugador y estrategia de equipo

**Idea:** analizar datos de partidas, mapas, personajes, armas o roles para recomendar estrategias de ataque, defensa o composición de equipo.

| Posibles fuentes | Posible IA/ML | Salida útil |
|---|---|---|
| Historial de partidas, estadísticas de personajes, mapas, resultados competitivos | Recomendación, clustering, predicción de victoria | Panel de estrategia o recomendador de composición |

Clave de calidad: relacionar el rendimiento con el contexto de partida y explicar cuándo la recomendación es fiable.

### Deporte y jugadores infravalorados

**Idea:** encontrar deportistas con alto rendimiento relativo a su coste, salario, edad, posición o valor de mercado.

| Posibles fuentes | Posible IA/ML | Salida útil |
|---|---|---|
| Estadísticas deportivas, salarios, valor de mercado, lesiones, minutos jugados | Ranking, regresión, clustering | Informe de scouting o recomendador de fichajes |

Clave de calidad: comparar por posición o rol, normalizar por contexto y justificar qué significa “infravalorado”.

### Aparcamiento inteligente, matrículas y facturación

**Idea:** gestionar entradas y salidas de vehículos, reconocer matrículas, estimar ocupación, calcular importes o localizar vehículos.

| Posibles fuentes | Posible IA/ML | Salida útil |
|---|---|---|
| Imágenes de matrículas, registros de entrada/salida, tarifas, plazas, incidencias | Visión por computador, predicción de ocupación, reglas de facturación | API o panel de gestión del aparcamiento |

Clave de calidad: integrar reconocimiento, estancia y tarifas, teniendo en cuenta errores de lectura y privacidad.

### Sistemas de recomendación

**Idea:** recomendar productos, contenidos, rutas, actividades o recursos educativos combinando comportamiento de usuarios y metadatos.

| Posibles fuentes | Posible IA/ML | Salida útil |
|---|---|---|
| Historial de interacciones, catálogo, valoraciones, perfiles | Recomendación colaborativa o basada en contenido | API de recomendaciones o interfaz de consulta |

Clave de calidad: evitar recomendaciones genéricas y explicar qué datos influyen en cada resultado.

### Predicción de demanda o precios

**Idea:** anticipar demanda, ocupación, ventas, precios o necesidades de stock usando datos históricos y variables externas.

| Posibles fuentes | Posible IA/ML | Salida útil |
|---|---|---|
| Histórico de ventas o demanda, calendario, meteorología, eventos, precios | Regresión, series temporales, modelos de predicción | Dashboard de previsión o alerta operativa |

Clave de calidad: integrar variables externas con sentido y comparar contra una predicción simple.

### Sentimiento, tickets y atención al usuario

**Idea:** clasificar mensajes, detectar urgencias, resumir incidencias o sugerir respuestas basadas en documentación.

| Posibles fuentes | Posible IA/ML | Salida útil |
|---|---|---|
| Tickets históricos, correos, chats, base de conocimiento, FAQ | NLP, clasificación, RAG, resumen automático | Asistente de soporte o priorizador de tickets |

Clave de calidad: fundamentar las respuestas en datos concretos y medir errores de clasificación o recuperación.

### Asistente educativo

**Idea:** crear un asistente que ayude a estudiar, localizar contenidos, generar preguntas o recomendar recursos según dificultades del alumnado.

| Posibles fuentes | Posible IA/ML | Salida útil |
|---|---|---|
| Apuntes, ejercicios, criterios de evaluación, consultas frecuentes, progreso del alumnado | RAG, recomendación, clasificación de dudas | Asistente o buscador inteligente de apoyo |

Clave de calidad: usar datos propios, citar fuentes internas y evitar que sea un chatbot genérico.

### Datos abiertos y servicios urbanos

**Idea:** analizar movilidad, transporte, calidad del aire, incidencias, turismo, equipamientos o servicios municipales.

| Posibles fuentes | Posible IA/ML | Salida útil |
|---|---|---|
| Open data municipal, mapas, meteorología, horarios, incidencias, sensores | Predicción, clustering, detección de anomalías | Mapa, dashboard, alerta o informe de mejora |

Clave de calidad: combinar datos espaciales, temporales o contextuales y traducirlos en recomendaciones comprensibles.

## Qué no es suficiente

Estos planteamientos pueden servir como punto de partida, pero no bastan como proyecto final:

| Propuesta insuficiente | Por qué no basta | Cómo mejorarla |
|---|---|---|
| Un CSV y un notebook | No hay integración ni producto | Añadir otra fuente, pipeline y salida usable |
| Dashboard sin IA | Solo visualiza datos | Incorporar predicción, recomendación o clasificación |
| Chatbot sin datos fundamentados | Puede inventar respuestas | Usar RAG con documentos propios y evaluación básica |
| Modelo aislado sin integración | No resuelve un flujo completo | Conectar datos, modelo y salida final |
| Notebook copiado de Kaggle | No demuestra diseño propio | Adaptar problema, añadir fuentes y justificar decisiones |
| Proyecto meramente descriptivo | No toma decisiones ni automatiza nada | Definir usuario, acción recomendada o predicción útil |

## Estructura esperada del repositorio

La estructura puede adaptarse a cada tecnología, pero debe ser clara y reproducible.

```text
proyecto-pia/
├── README.md
├── docs/
│   ├── propuesta.md
│   ├── fuentes-datos.md
│   ├── decisiones.md
│   └── defensa.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── notebooks/
│   └── exploracion.ipynb
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── api_o_interfaz/
│   └── utils/
├── tests/
├── models/
├── reports/
├── requirements.txt / pyproject.toml / environment.yml
└── .gitignore
```

### README mínimo

El `README.md` debe permitir entender y ejecutar el proyecto sin explicaciones orales: problema, integrantes, fuentes, permisos, instalación, ejecución, ejemplos de uso, métricas principales y limitaciones conocidas.

### Datos y privacidad

No deben subirse al repositorio datos sensibles, credenciales, tokens ni información personal no autorizada.

Si se usan datos pesados o privados, se documentará cómo obtenerlos o se proporcionará una muestra segura.

## Criterios generales de evaluación

La evaluación concreta podrá detallarse en una rúbrica aparte. A alto nivel, se valorará lo siguiente:

| Criterio | Qué se observará |
|---|---|
| Integración de datos | Variedad, relación real entre fuentes y utilidad de la combinación |
| Calidad de datos | Limpieza, trazabilidad, transformaciones y tratamiento de problemas |
| Componente de IA/ML | Adecuación técnica, comparación con baseline y utilidad para el problema |
| Calidad de ingeniería | Estructura, reproducibilidad, código, pipeline, API/interfaz y pruebas razonables |
| Documentación y defensa | Claridad, justificación de decisiones, demo, limitaciones y respuesta a preguntas |

Un proyecto técnicamente sencillo puede ser válido si está muy bien integrado, documentado y defendido. Un proyecto con un modelo complejo puede ser insuficiente si no resuelve un problema claro o no integra datos de forma real.

## Defensa final

La defensa debe centrarse en evidencias, no solo en una presentación estética.

El equipo debe mostrar:

1. Problema y usuario objetivo.
2. Fuentes de datos y proceso de integración.
3. Limpieza y preparación de datos.
4. Modelo, baseline y métricas principales.
5. Demo de la salida final.
6. Decisiones técnicas relevantes.
7. Limitaciones, riesgos y mejoras futuras.
8. Reparto de trabajo y aprendizaje obtenido.

## Notas para el profesorado

### Cómo gestionar propuestas débiles

Cuando una propuesta sea demasiado simple, conviene devolverla con una mejora concreta y verificable: añadir una segunda fuente que cambie la decisión final, definir el usuario, convertir el análisis en ranking/predicción/recomendación/API o separar una versión mínima viable de las ampliaciones.

Las propuestas históricamente más débiles pueden usarse como ejemplos de advertencia para mostrar qué les faltaba en ambición, integración o utilidad.

### Cómo atender grupos irregulares

Puede haber equipos con perfiles muy distintos. Para mantener exigencia sin bloquear el aprendizaje:

- Validar pronto una versión mínima viable alcanzable.
- Permitir que la complejidad crezca por capas.
- Exigir integración real aunque el modelo inicial sea sencillo.
- Valorar especialmente la trazabilidad, la explicación y la reproducibilidad.
- Proponer ampliaciones opcionales a los equipos que avancen más rápido.
- Evitar que los equipos con menos base elijan proyectos imposibles por falta de datos o exceso de ingeniería.

### Señales de alerta durante el seguimiento

- El equipo no puede explicar de dónde salen los datos.
- Solo existe un notebook sin estructura de proyecto.
- La segunda fuente aparece en la memoria, pero no en el código.
- El modelo se entrena, pero nadie sabe cómo se usaría el resultado.
- La demo depende de pasos manuales no documentados.
- No hay baseline ni criterio para saber si el modelo mejora algo.

### Cierre recomendado

Antes de aceptar el proyecto como listo para defensa, comprobar que el repositorio se entiende desde el README, hay evidencias de integración, la salida final funciona o está reproducida, el equipo explica errores y limitaciones, y la defensa muestra aprendizaje propio.
