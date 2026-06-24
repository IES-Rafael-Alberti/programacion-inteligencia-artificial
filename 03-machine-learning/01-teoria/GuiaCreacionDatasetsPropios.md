# Guía Teórica para la Creación de Datasets Propios en Aprendizaje Automático

En este documento se presenta una guía exhaustiva sobre cómo obtener, construir y servir datasets propios para proyectos de Machine Learning. Abarca desde la justificación de crear un dataset desde cero hasta las fuentes de datos disponibles, el proceso de construcción, los formatos de almacenamiento más comunes, un mini-ejemplo práctico y nociones de herramientas avanzadas como Poetry (gestión de entornos) y FastAPI (exposición de datos vía API). Cada sección amplía detalladamente los puntos clave para convertir datos crudos en conjuntos de datos útiles para aprendizaje automático, con ejemplos claros en Python.

## Justificación: ¿Por qué construir tu propio dataset?

Existen numerosos datasets públicos de alta calidad disponibles, entonces ¿por qué tomarse el trabajo de crear uno desde cero? Las razones abarcan tanto aspectos prácticos como estratégicos:

Adecuación al problema: Un dataset propio se diseña exactamente para la tarea o el dominio específico que te interesa. Los datasets públicos suelen ser más generales; en cambio, un conjunto de datos personalizado puede incluir justo las variables, formatos y ejemplos relevantes (por ejemplo, idioma o contexto local) que tu proyecto necesita[1]. Como señala un análisis reciente, “los datasets preconstruidos ofrecen un comienzo rápido, pero los personalizados se orientan a la precisión y relevancia para casos de uso más específicos”[2]. En resumen, mientras los datos genéricos pueden no alinearse perfectamente con tu realidad operativa, un dataset propio sí lo hará.

Calidad y control: Al recolectar datos por tu cuenta, tienes control total sobre la calidad, cantidad y actualización de los datos. Puedes definir criterios de recolección, asegurar diversidad en las muestras y minimizar sesgos. Cualquier error o sesgo en los datos será identificable y corregible por ti mismo, en lugar de confiar ciegamente en datos externos. Este control ayuda a evitar el “deuda de calidad” de datos genéricos, que a veces llevan a tener que rehacer modelos más adelante por problemas en datos poco adecuados[3].

Disponibilidad de datos únicos: En muchos casos no existe un dataset público para el problema que intentas resolver. Si trabajas en un nicho muy novedoso, en un idioma minoritario o con datos privados de una empresa, no tendrás más opción que crearlo. Un dataset propio puede darte ventaja competitiva, ya que estarás usando datos que otros no tienen.

Aprendizaje y habilidades de ingeniería de datos: La tarea de recopilar, limpiar y estructurar datos es una parte fundamental (a menudo la más laboriosa) de los proyectos de ciencia de datos. Crear un dataset desde cero te obliga a desarrollar habilidades de ingeniería de datos: interacción con APIs, web scraping, manejo de formatos, gestión de calidad, etc. Esta experiencia “end-to-end” es muy valiosa en entornos profesionales, donde se estima que los científicos de datos dedican gran parte de su tiempo a preparar los datos más que a modelarlos. Como dice un autor, muchos cursos se enfocan en modelos y limpieza, pero “¿de dónde sacamos esos datos sucios?” – entender cómo obtenerlos es clave para completar el ciclo completo de un proyecto[4].

En definitiva, construir tu propio dataset te permite obtener datos pertinentes, de alta calidad y personalizados a tus objetivos, a la vez que refuerzas tus capacidades prácticas. Una vez que tengas datos relevantes y bien curados para tu problema, podrás entrenar modelos de IA más confiables y efectivos.

## Principales Fuentes de Datos para Construir un Dataset

Para crear un dataset es fundamental saber dónde obtener los datos brutos. A continuación, se describen las principales fuentes de datos que puedes explotar, desde datos accesibles en internet hasta aquellos generados en sistemas y dispositivos:

### APIs públicas y privadas

Una API (Application Programming Interface) es una interfaz que permite acceder a datos o funcionalidad de un servicio a través de internet, generalmente mediante peticiones HTTP. Muchas organizaciones ofrecen APIs para consultar sus datos, ya sean públicas (abiertas a cualquier desarrollador, a veces con registro gratuito) o privadas (requieren autenticación especial, suscripción o son de uso interno en empresas).

Tipos de APIs y autenticación: La mayoría de las APIs web modernas son de tipo REST (RESTful), donde se realizan peticiones HTTP (GET, POST, etc.) a URLs que representan recursos (por ejemplo /usuarios, /datos_climaticos). Suelen responder en formatos como JSON (JavaScript Object Notation), muy conveniente para procesar en Python, aunque algunas usan XML u otros formatos. Las APIs públicas a veces no requieren autenticación, pero muchas APIs (públicas y privadas) exigen usar una clave de API (API key) o mecanismos de OAuth 2.0 para autorización. Por ejemplo, para usar la API de Twitter o de Google Maps necesitas registrar una aplicación y obtener credenciales.

Uso desde Python: Librerías como requests (o alternativas como httpx) simplifican enormemente la invocación de APIs REST. Con requests puedes enviar una petición GET y recibir directamente la respuesta en JSON como un diccionario Python. Por ejemplo, el siguiente código realiza una petición a una API hipotética de clima:

import requests

url = "https://api.ejemplo.com/v1/clima"
params = {"ciudad": "Cádiz", "formato": "json"}
resp = requests.get(url, params=params)  # Petición GET con parámetros
if resp.status_code == 200:
    datos = resp.json()  # parsea la respuesta JSON a dict
    print(datos)
else:
    print(f"Error {resp.status_code}: {resp.text}")

En este ejemplo, construimos la URL de la API con ciertos parámetros de consulta (params) y obtenemos la respuesta JSON convertida directamente a un objeto Python con resp.json(). Librerías como httpx ofrecen funcionalidad similar, con soporte asíncrono si se necesita alto rendimiento.

Formato de respuesta (JSON): JSON es el formato de respuesta más común en APIs web. Es un formato de texto estructurado con pares clave-valor, fácilmente serializable/deserializable. Python tiene soporte nativo vía el módulo json para convertir cadenas JSON en diccionarios (json.loads) o viceversa (json.dumps). Es habitual navegar por el JSON resultante para extraer los campos relevantes que formarán parte de tu dataset.

Ejemplos concretos de APIs: Existen infinidad de APIs útiles para crear datasets:

APIs abiertas de clima: como OpenWeatherMap (requiere clave) u Open-Meteo (libre, sin clave). Por ejemplo, Open-Meteo permite obtener el pronóstico del tiempo dado latitud/longitud y devuelve temperaturas, precipitaciones, etc., en JSON.

APIs de redes sociales: Twitter (hoy X) ofrece endpoints para buscar tuits por hashtag, lo cual permite construir fácilmente un dataset de textos con cierto tema[5]. Instagram, Reddit, etc., tienen APIs (aunque muchas requieren autenticación y/o ofrecen datos limitados).

APIs financieras: por ejemplo CoinGecko para datos de criptomonedas, o Yahoo Finance (vía yfinance en Python) para históricos de bolsas.

APIs de servicios web: GitHub tiene una API pública para obtener datos de repositorios, commits, etc. Google Maps API para datos geográficos, Wikipedia API para extraer contenido de artículos, etc.

APIs privadas internas: En entornos corporativos, muchas aplicaciones expuestas internamente ofrecen APIs (por ejemplo, una base de datos de clientes con endpoint REST). Si trabajas dentro de una empresa, puedes aprovechar APIs privadas con los permisos adecuados.

Usar APIs suele ser la vía más limpia y estructurada de obtener datos, ya que el proveedor controla el formato (habitualmente JSON bien organizado). Debes revisar las tasas de petición (rate limits) que impone cada API para no excederlas, y respetar los términos de uso. En resumen, aprovechar APIs (públicas o privadas) es una estrategia fundamental para nutrir tu dataset con datos actualizados y de fuentes confiables.

### Web Scraping

Cuando los datos no están disponibles mediante una API pública, una alternativa es recurrir al Web Scraping, que consiste en extraer información directamente de páginas web. En este enfoque, tu código actúa como un navegador: descarga el HTML de una página y luego parsea ese HTML para obtener los datos deseados (por ejemplo, el precio de un producto, titulares de noticias, comentarios de un foro, etc.).

Herramientas de scraping: Existen múltiples herramientas y librerías Python para scraping:

requests + BeautifulSoup: combinación clásica. requests obtiene el HTML y BeautifulSoup lo parsea para navegar por el árbol DOM (permite buscar etiquetas por nombre, clases CSS, id, etc.). También se puede usar lxml para parseo más rápido o expresiones XPath.

Selenium: herramienta para automatizar navegadores web (controla un navegador real como Chrome/Firefox). Útil para páginas con contenido dinámico (JavaScript) que un simple requests no puede obtener. Permite cargar la página, ejecutar JS y luego extraer elementos. Como alternativa más moderna está Playwright, que también controla navegadores con soporte nativo para operaciones asíncronas y múltiples navegadores.

Frameworks especializados: Scrapy es un framework de scraping muy potente para rastrear múltiples páginas (crawling) con manejo de concurrencia, colas, etc., ideal para proyectos grandes de extracción web.

Servicios en la nube: existen APIs y plataformas (Apify, Scrapinghub, etc.) que realizan scraping y te devuelven los datos, útiles si no quieres lidiar con el bloqueo de IPs o mantenimiento de infraestructura.

En resumen, hay una variada gama de librerías disponibles para obtener datos de fuentes en línea[6][7]. La elección depende de la complejidad del sitio objetivo: para HTML estático suele bastar requests+BeautifulSoup; para sitios muy dinámicos, Selenium o Playwright son más adecuados.

Límites legales y técnicos: El scraping plantea consideraciones importantes:

Legales: Debes revisar los términos de servicio del sitio web. Algunos prohíben explícitamente el scraping no autorizado. Asimismo, respeta las normas de un sitio señaladas en el archivo robots.txt, que indica qué áreas se pueden rastrear. Aunque robots.txt no es legalmente vinculante, es una cortesía importante. Evita usar los datos de forma que viole derechos de autor o privacidad.

Técnicas: Un scraper descontrolado puede saturar un sitio web. Es crucial implementar throttling (pausas entre peticiones) y no descargar contenido más rápido de lo que un usuario normal lo haría. También conviene aleatorizar tiempos entre peticiones para no lucir como un bot agresivo, y usar encabezados adecuados (user-agent) para identificarse. Algunos sitios pueden bloquear IPs si detectan scraping; usar proxies o servicios especializados puede ser necesario en esos casos.

Calidad de datos: El HTML de la web fue diseñado para visualización, no para consumo automatizado. Debes estar preparado para lidiar con HTML mal formado, cambios frecuentes en el diseño del sitio (que rompen tu extractor), o la necesidad de descartar mucho contenido irrelevante.

Ventajas y riesgos: La ventaja del scraping es que te permite acceder a información pública que no se ofrece mediante APIs. Por ejemplo, puedes extraer precios de productos directamente de páginas de comercio electrónico para armar un dataset de seguimiento de precios, o recopilar reseñas de películas desde un sitio web. Si necesitas comentarios de noticias y no hay API, puedes scrapear la sección de comentarios de la página web de noticias. De hecho, muchas webs de noticias ofrecen versiones en formato feed (RSS/XML) que facilitan la extracción[8]. El riesgo es la fragilidad: si el sitio cambia su estructura, tu código debe adaptarse. Además, consumir páginas enteras es menos eficiente que una API bien diseñada, por lo que se debe usar con moderación y responsabilidad.

Ejemplo básico de scraping: Supongamos que queremos extraer los títulos de artículos de un blog. Podríamos hacerlo así:

import requests
from bs4 import BeautifulSoup

url = "https://blog.ejemplo.com"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
titulos = [h2.get_text() for h2 in soup.find_all('h2', class_='titulo-articulo')]
print(titulos)

Aquí buscamos todos los <h2> con clase CSS titulo-articulo y extraemos su texto. Este tipo de lógica se adapta según la estructura HTML de cada sitio.

En conclusión, el web scraping requiere más esfuerzo de mantenimiento y cuidado legal, pero es una herramienta poderosa cuando no hay APIs disponibles. Permite ingeniarse fuentes de datos donde aparentemente “no hay dataset armado”, usando creatividad para recopilar información pública y convertirla en un dataset utilizable[9][10].

### Logs del sistema

Los logs son registros cronológicos de eventos que producen los sistemas informáticos, aplicaciones o dispositivos. Son como un diario detallado de todo lo que ocurre, desde acciones de usuarios hasta eventos del sistema operativo. Constituyen una fuente valiosa de datos, especialmente en contextos de monitoreo, seguridad o análisis de rendimiento.

¿Qué tipo de datos hay en los logs? Prácticamente cualquier sistema genera logs: el sistema operativo anota eventos esenciales (inicios/apagados, errores de kernel), las aplicaciones registran operaciones o errores internos, los servidores web guardan cada petición recibida, etc. En general, se suelen clasificar en:

Logs de sistema: eventos del sistema operativo, por ejemplo, mensajes de arranque, apagado, carga de drivers, errores críticos.

Logs de seguridad: eventos relacionados con seguridad y accesos, como intentos de inicio de sesión, usos de privilegios, detección de intrusiones.

Logs de aplicaciones: cada aplicación puede generar su propio log detallando acciones del usuario, transacciones, accesos a base de datos, etc.

Logs de errores: archivos dedicados a errores y excepciones, recopilando trazas de fallos para depuración[11].

Logs de red/servidores: registros de servidores web, proxies, firewalls, con información de peticiones, IPs, puertos, etc.

Por ejemplo, un log de servidor web Apache típico contiene líneas con la IP del cliente, fecha, recurso pedido, código de respuesta HTTP y tamaño de respuesta. Un fragmento podría ser:

192.168.1.100 - - [10/Dec/2025:14:32:16 +0100] "GET /index.html HTTP/1.1" 200 1245

Cada línea incluye campos separados (IP, fecha, método y recurso, código, bytes). Otros logs, como los de aplicaciones, pueden estar en formato más libre o incluso en JSON.

Cómo se generan y almacenan: Normalmente los logs se escriben en archivos de texto plano (a veces rotando diariamente o cuando alcanzan cierto tamaño). En Linux, por ejemplo, existen archivos bajo /var/log/ para distintos servicios (auth.log, syslog, kern.log, etc.). Aplicaciones como servidores web o bases de datos generan sus logs en rutas específicas. También existen sistemas centralizados de logging (p. ej., usar Syslog para centralizar, o herramientas como Elastic Stack o Splunk para recopilar y analizar logs en grandes volúmenes).

Procesamiento de logs en Python: Los logs, al ser texto (a veces semi-estructurado), se pueden procesar en Python usando técnicas de manejo de strings:

Lectura línea a línea: Puedes abrir el archivo de log y leerlo línea por línea. Por ejemplo:

with open("mi_aplicacion.log") as f:
    for line in f:
        # Procesar cada línea
        ...

Esto es esencial para no cargar archivos muy grandes completos en memoria, sino procesar streaming.

Búsqueda de patrones (regex): La librería re de Python permite definir expresiones regulares para extraer información de cada línea. Por ejemplo, si un log de aplicación tiene líneas como ERROR [2025-12-11 16:00:00] Cód:1234 - Desc: Falla de conexión, podríamos usar re.search(r"Cód:(\d+)", line) para capturar el código numérico de error.

Parsing manual o split: Si el log tiene separadores claros (comas, espacios), a veces un simple .split() puede bastar para dividir la línea en campos. Muchos logs están separados por espacios o tabuladores.

Logs en JSON: Cada vez más aplicaciones generan logs en formato JSON (una línea JSON por evento). En esos casos, procesarlos en Python es sencillo usando json.loads(line) para cada línea y obteniendo un diccionario. Esto elimina la necesidad de regex, aprovechando que ya está estructurado.

Ejemplo de procesamiento: Supongamos un log de aplicación con formato sencillo: "[nivel] fecha - mensaje". Podríamos querer contar cuántos mensajes de nivel ERROR ocurrieron:

import re
conteo_error = 0
with open("app.log") as f:
    for line in f:
        if line.startswith("[ERROR]"):
            conteo_error += 1
            # Extraer fecha y mensaje si se desea
            m = re.match(r"\[ERROR\]\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.*)", line)
            if m:
                fecha = m.group(1)
                descripcion = m.group(2)
                # ... (almacenar o analizar)
print(f"Cantidad de errores: {conteo_error}")

En este código contamos líneas que comienzan con "[ERROR]" y usamos una regex para separar la fecha y la descripción del error. En casos más complejos, podríamos construir estructuras como listas o dataframes con los datos extraídos de cada línea.

Uso de logs como datasets: Una vez procesados, los logs pueden transformarse en datasets muy valiosos. Por ejemplo:

Un log de servidor puede convertirse en un dataset para análisis de tráfico web (campos: IP, timestamp, URL, código, etc.) y usarlo para detectar patrones o entrenar modelos de detección de intrusos.

Logs de aplicaciones pueden ser usados para encontrar cuellos de botella (tiempos de respuesta), analizar comportamiento de usuarios, o predecir fallos (si combinamos con eventos de error posteriores).

Logs de sistemas de sensores (IoT) pueden alimentar modelos de series temporales para predicción (ver siguiente sección).

En resumen, los logs son datos ya disponibles que solo esperan ser extraídos y estructurados. Python ofrece las herramientas necesarias (lectura eficiente, regex, JSON) para convertir esos textos en filas y columnas aptas para análisis y Machine Learning. Además, dado que la generación de logs es automática en la mayoría de sistemas[12], son una fuente continua y en tiempo real de información de la cual podemos construir datasets actualizados.

### Datos de sensores e IoT

En la era del Internet de las Cosas (IoT), multitud de dispositivos y sensores están constantemente generando datos: mediciones de temperatura, humedad, movimientos, consumos de energía, señales biométricas, etc. Estos datos de sensores son otra fuente crucial para construir datasets, especialmente en proyectos de tiempo real, domótica, ciudades inteligentes, industria 4.0, etc.

Características de los datos IoT: Suelen ser datos de series temporales (lecturas con marca de tiempo) provenientes de dispositivos físicos. Ejemplos: un sensor de temperatura que da una lectura cada minuto, un acelerómetro en un smartphone registrando movimientos, un contador inteligente de electricidad enviando consumos horarios. Por lo general, cada dato es relativamente simple (un número o estado) acompañado de una timestamp y posiblemente un identificador de dispositivo.

Comunicación y protocolos: Los sensores IoT usan diversos protocolos para transmitir sus datos:

MQTT (Message Queuing Telemetry Transport): es un protocolo ligero de mensajería, ideal para IoT por su bajo consumo y simplicidad. Funciona con un modelo publicación/suscripción: los dispositivos (clientes) publican mensajes en “topics” (temas) y un broker (como Eclipse Mosquitto) los distribuye a los clientes suscritos a esos temas[13]. Por ejemplo, un sensor de temperatura publica en el tema casa/salon/temperatura el valor cada X segundos, y cualquier cliente suscrito (una aplicación Python, una base de datos, etc.) recibe esos valores en tiempo real.

HTTP/REST: algunos dispositivos más potentes simplemente hacen peticiones HTTP a un servidor central enviando sus datos (o exponen los datos en un pequeño servidor web embebido). Por ejemplo, un sensor podría tener un endpoint /data que devuelve la última lectura en JSON, o enviar un POST con cada lectura a un servidor.

Otros: protocolos industriales (Modbus, OPC-UA), Bluetooth Low Energy para dispositivos cercanos, Zigbee/Z-Wave en domótica, etc. Cada ecosistema puede tener su estándar, pero finalmente desde Python normalmente recibiremos los datos vía red (socket, HTTP, MQTT, archivos).

Almacenamiento temporal vs persistente: Con sensores que emiten datos constantemente, es importante diseñar cómo almacenarlos:

Temporal (en memoria): A veces se usan brokers en memoria o colas de mensajes para retener datos recientes, actuando más en tiempo real (por ejemplo, para activar una alerta si un valor supera umbral).

Persistente: Para análisis histórico o entrenamiento de modelos, querrás guardar los datos en almacenamiento duradero. Opciones comunes:

Archivos de log o CSV: simple y directo, el dispositivo o servidor anexa cada nueva lectura a un archivo (con fecha, valor, etc.).

Bases de datos de serie temporal: p.ej. InfluxDB, diseñada específicamente para datos indexados por tiempo. En InfluxDB cada registro tiene un timestamp y una serie de campos (valores de sensores, metadatos) en formato similar a JSON[14]. Estas BBDD permiten consultas por rangos de tiempo muy eficientes y agregaciones (promedios por minuto, máximos diarios, etc.).

Bases de datos relacionales o NoSQL: según el volumen, se puede usar SQLite, PostgreSQL (con extensiones de time-series) o MongoDB para almacenar lecturas. Si el volumen es altísimo (millones de puntos diarios), se opta por soluciones escalables o particionamiento por tiempo.

Servicios en la nube: por ejemplo, Google Cloud IoT Core (ahora reemplazado por otras soluciones en GCP) o AWS IoT permiten recibir datos de dispositivos y enrutarlo a otras bases de datos o servicios (como BigQuery, DynamoDB, etc.) para almacenamiento y análisis.

Herramientas y plataformas IoT: Para facilitar la gestión de múltiples sensores y sus datos, existen plataformas especializadas:

Node-RED: una plataforma de código abierto muy popular en IoT. Basada en Node.js, provee una interfaz gráfica tipo diagrama de flujo para conectar nodos que representan fuentes de datos, transformaciones y destinos[15]. Por ejemplo, puedes arrastrar un nodo que recibe datos MQTT, conectarlo a un nodo que los transforma (p. ej. convierte unidades) y luego a otro que los almacena en una base de datos o los visualiza. Node-RED simplifica la orquestación de datos IoT sin mucho código, ideal para prototipos.

Plataformas cloud IoT: AWS, Azure y Google Cloud tienen servicios gestionados para IoT donde puedes registrar dispositivos, asegurar la comunicación, y procesar/almacenar datos a escala. Por ejemplo, Azure IoT Hub o AWS IoT Core actúan como concentradores de mensajes de dispositivos, con integraciones a streaming y almacenamiento.

Hardware/Software intermedio: Si trabajas con dispositivos como Arduino, Raspberry Pi, ESP32, etc., puede que programes en otros lenguajes (C, MicroPython) para capturar los datos del sensor y enviarlos. Pero del lado del servidor (o de recolección central), Python puede suscribirse a los datos vía MQTT (paho-mqtt es la librería Python estándar para MQTT), o exponer una API REST donde los dispositivos reporten.

Conversión a datasets ML: Los datos de sensores muchas veces necesitan agregación o combinación antes de ser un dataset para ML:

Resampling y ventanas de tiempo: Por ejemplo, si tienes un sensor de temperatura con lecturas cada segundo, pero para tu modelo necesitas características por minuto, debes agrupar (ej. tomar promedio o máximos por minuto).

Unir múltiples sensores: En IoT es común tener que unir datos de varios sensores. Por ejemplo, combinar en un mismo dataset la temperatura y la humedad (de sensores distintos) sincronizados por tiempo, o datos de un acelerómetro en X, Y, Z en una sola tabla por timestamp.

Etiquetado o eventos: Si se busca predecir un evento (p. ej. fallo de una máquina), habrá que etiquetar periodos de datos como normal o fallo según registros históricos. Esto puede implicar fusionar datos de sensor con registros de mantenimiento, etc.

Limpieza de ruidos y valores perdidos: Los sensores a veces tienen lecturas espurias (picos anómalos) o periodos sin datos (conexión caída). Es importante limpiar o imputar esos casos antes de usar el dataset para entrenar.

En resumen, los datos de sensores/IoT permiten crear datasets de gran valor para modelos predictivos en tiempo real y análisis de series temporales. Con las herramientas adecuadas (brokers MQTT, plataformas como Node-RED, bases de datos de series temporales, librerías Python para protocolos), podemos recopilar ese flujo continuo de datos y convertirlo en conjuntos de datos estructurados listos para la ciencia de datos.

### Open Data (Datos Abiertos)

El movimiento de Datos Abiertos proporciona una enorme cantidad de información pública y gratuita que podemos convertir en datasets. Gobiernos e instituciones de todo el mundo publican datos de interés general: desde estadísticas socioeconómicas hasta datos meteorológicos históricos, pasando por registros de transporte, salud, educación, etc. Aprovechar estos portales de Open Data es una forma rápida de obtener datos de calidad sin empezar de cero.

Portales gubernamentales: La mayoría de los gobiernos nacionales y muchos regionales/municipales tienen sitios de datos abiertos. Por ejemplo:

En España, el portal datos.gob.es reúne datasets de distintas administraciones (INE, ministerios, ayuntamientos). Puedes encontrar desde el censo de población hasta datos de contaminación por ciudad.

Argentina tiene https://datos.gob.ar/ y México https://datos.gob.mx/, por citar algunos ejemplos latinoamericanos[16]. Estos portales permiten buscar datasets por tema (economía, transporte, etc.) y descargar en diversos formatos.

La Unión Europea cuenta con data.europa.eu que centraliza datos de instituciones europeas y de países miembros. A nivel mundial, data.gov (EE.UU) es muy extenso, y hay portales de Naciones Unidas, Banco Mundial, etc.

Instituciones y ONGs: Además de gobiernos, muchas instituciones científicas, ONGs y universidades comparten datos abiertos. Por ejemplo, la OMS publica datos de salud global, la NASA distribuye gratuitamente enormes cantidades de datos satelitales y climáticos, etc. También existen repositorios temáticos, como datos geoespaciales (Natural Earth, OpenStreetMap), datos genómicos (NCBI), entre otros.

Formatos disponibles: En open data es común encontrar formatos variados:

CSV/TSV: muy frecuentes para datos tabulares. Fáciles de cargar con pandas.

JSON: especialmente si ofrecen una API además de la descarga directa.

XML: en datasets antiguos o en ciertos dominios (por ej. algunos datos geográficos vienen en XML).

Geo formatos: shapefiles, GeoJSON, KML para datos espaciales.

Otros: Excel, PDF (no ideal pero a veces sucede), o formatos especializados (HDF5, NetCDF para datos científicos).

Muchos portales también ofrecen APIs de consulta para acceder a subconjuntos de los datos sin descargar archivos enormes. Por ejemplo, Socrata es una plataforma usada en varios portales que permite usar un API REST (o SODA API) para filtrar/consultar datos abiertos.

Ejemplos de datasets relevantes: Algunos casos interesantes de open data:

Datos meteorológicos e informes climáticos (ej. AEMET en España libera datos históricos del clima).

Transporte público: horarios y posiciones de buses/trenes (GTFS feeds), índices de uso.

Salud: registros de enfermedades, vacunaciones, calidad del aire.

Educación: resultados académicos, estadísticas de universidades.

Gobierno y cívicos: presupuesto público, resultados electorales, delitos reportados, etc.

Mapas y geografía: cartografía, imágenes satelitales abiertas (Landsat, Sentinel).

Uso en la práctica: Imagina que quieres un dataset para un proyecto de predicción del mercado inmobiliario. Podrías combinar open data de censos poblacionales (para características de barrios), datos abiertos de transacciones inmobiliarias (si existen en tu país), más quizás datos de transporte o escuelas cercanas. Todo ello son piezas que diferentes portales proporcionan. El trabajo está en descargarlos, comprender los esquemas, fusionarlos por alguna clave común (ej. código postal, distrito) y limpiar inconsistencias.

Comunidades de datasets abiertos: Además de portales oficiales, sitios como Kaggle o Google Dataset Search facilitan encontrar datasets públicos. Kaggle en particular alberga miles de conjuntos de datos subidos por la comunidad, muchos provenientes de open data oficiales pero ya preprocesados o actualizados por usuarios. Kaggle es conocido como la “meca” de los data scientists y no solo ofrece los datos sino también notebooks con análisis de ejemplo y una comunidad activa[17]. Sin embargo, es importante citar la fuente original cuando un dataset viene de open data oficial.

En conclusión, Open Data es un tesoro para crear datasets sin recolectar manualmente cada dato. La información ya está ahí, solo hay que descargarla (o consultarla vía API) y darle el formato adecuado para tu proyecto. Siempre revisa las licencias asociadas (suelen ser abiertas tipo CC BY), atribuye la fuente y, por supuesto, enriquece tu dataset combinando múltiples fuentes abiertas si es posible para obtener un conjunto más completo y útil.

## Proceso de Creación de un Dataset desde Cero

Habiendo visto de dónde obtener datos, detallaremos el proceso completo para crear un dataset desde cero. Este proceso abarca desde la concepción inicial hasta obtener un archivo final listo para usar en Machine Learning. De forma general, podemos dividirlo en pasos:

Definir el problema y los datos necesarios: Comienza planteando claramente el objetivo de tu proyecto de ML. ¿Qué quieres predecir o analizar? Por ejemplo: "predecir la probabilidad de que un usuario abandone nuestra aplicación en el próximo mes". A partir de eso, define qué variables podrían ser relevantes (edad, frecuencia de uso, etc.). Esta fase es crucial: piensa qué formato tendrá el dataset (¿filas representan usuarios? ¿columnas representan atributos demográficos, de actividad, etc.?). En resumen, dibuja un boceto de tu dataset ideal: cuántas columnas y cuáles, y qué representa cada fila.

Recopilación de datos brutos: Con la lista de datos necesarios, utiliza las fuentes de datos vistas (APIs, scraping, logs, sensores, open data, bases internas) para obtener la materia prima. Es posible que los datos vengan en varios orígenes y formatos:

Puede que parte venga de una API en JSON, otra parte de un CSV descargado de un portal, y otra de logs locales, por ejemplo.

Documenta cada fuente y asegúrate de guardar copias crudas (por si necesitas reprocesar más adelante). Por ejemplo, guarda el JSON original de la API en disco, o los HTML crudos de scraping si son pequeños, de manera que puedas replicar o depurar el proceso sin hacer fetch de nuevo cada vez.

Integración y unificación: Si los datos vienen de fuentes heterogéneas, toca unirlos. Esto puede implicar:

Concatenar datos similares: por ejemplo, descargaste datos de clima de 5 ciudades en archivos separados, los unes en un solo dataset añadiendo quizá una columna "ciudad".

Fusionar por claves: si tienes datos de diferentes fuentes sobre la misma entidad, por ejemplo un dataset con información económica por país y otro con datos demográficos por país, los unes por la columna "país".

Alinear en el tiempo: para datos de series temporales de diferentes frecuencias (ej. uno diario y otro mensual), podrías necesitar agregarlos a granularidad común (mensual, trimestral).

Resolver inconsistencias: asegurarte de que los identificadores coinciden exactamente (ej. "EE.UU." vs "Estados Unidos" vs "USA" en distintas fuentes: normalizar a un estándar).

Limpieza de datos: Ahora con datos integrados (o mientras los integras) aplica las técnicas de data cleaning:

Eliminar duplicados: registros repetidos exactamente, o entradas con el mismo identificador. Por ejemplo, si scrapear una API inserta duplicados por error, quitarlos.

Manejar valores faltantes: decidir cómo tratar missing values (¿eliminar filas? ¿imputar con media/mediana? ¿dejar nulos pero conscientes?).

Corrección de errores: buscar outliers evidentes o datos imposibles (ej. edad = 200 años) y decidir si eliminarlos o corregirlos si es factible.

Normalización de formatos: asegurar que todas las columnas tengan el tipo correcto (fechas en formato datetime, números en formato numérico, categorías consistentes). Estandarizar unidades (por ejemplo, todas las temperaturas en °C, todas las monedas convertidas a una misma).

Filtrado si aplica: quizás no toda la data recabada es útil. Por ejemplo, si estás creando un dataset de imágenes de gatos y perros, y tu scraping trajo algunas imágenes vacías o irrelevantes, descartarlas aquí.

Transformación y feature engineering: Este paso comienza a convertir datos crudos en variables más procesables o más informativas para modelos:

Derivar columnas: crear nuevas columnas a partir de las existentes. Ej: a partir de una fecha de nacimiento, calcular la edad; de un timestamp, extraer hora del día o día de la semana como variable.

Discretizar o agrupar: si un valor numérico tiene mucha dispersión, quizás creas rangos (ej: convertir salario en rangos "bajo/medio/alto").

One-hot encoding o categorías numéricas: si tienes variables categóricas en texto, podrías convertirlas en formato adecuado (números o múltiples columnas dummy).

Estandarización o normalización: especialmente para modelos sensibles a escala, podrías aplicar escalado (pero a veces esto se hace justo antes del modelado; aquí podrías dejarlo pendiente y solo anotar la necesidad).

Etiquetado (si es supervisado): añade la columna objetivo (label) si no estaba explícita. Por ejemplo, después de recopilar datos de clientes, determinas quiénes sí cancelaron el servicio y quiénes no, marcándolo en el dataset. Este paso puede implicar obtener datos adicionales (p.ej., consultar en la base quién canceló) y fusionarlos por ID de cliente.

Verificación y análisis exploratorio: Una vez armado el dataset casi final, es bueno hacer un exploratory data analysis (EDA) ligero para verificar que todo tiene sentido:

Ver dimensiones: ¿número de filas y columnas es el esperado?

Ver muestra de filas aleatorias para confirmar que los valores parecen coherentes.

Estadísticas descriptivas: medias, distribuciones, conteos de categorías, para identificar si hay aún anomalías (ej: una categoría inesperada, o una columna numérica con valores absurdos).

Corroborar que no hay leaks (en problemas supervisados, asegurarse de que no incluiste información del futuro en las variables, etc.).

Guardar el dataset final: Por último, persistir el dataset en el formato más conveniente:

Si es tabular y no demasiado grande: CSV es una buena opción de interoperabilidad. Guardar un .csv permite abrirlo fácilmente y compartir.

Para grandes volúmenes o mejor eficiencia: formatos binarios como Parquet (ver sección siguiente) son preferibles.

Si el dataset se usará dentro de un pipeline Python exclusivamente, incluso un pickle de pandas DataFrame puede ser útil (aunque menos portable).

Documenta el esquema: es buena práctica acompañar el dataset con una breve descripción de cada columna, unidades, significado, etc., para uso futuro.

Vale mencionar que este proceso no es lineal; es iterativo. Por ejemplo, al limpiar datos puedes descubrir que faltan datos y debas volver al paso de recolección para conseguir esos datos faltantes de otra fuente. O al hacer EDA notas que una variable no sirve y decides quitarlá, etc. La creación de un dataset propio suele implicar idas y vueltas antes de estar satisfecho con la calidad del conjunto.

En resumen, crear un dataset desde cero implica: entender el problema, reunir datos diversos, fusionarlos coherentemente, limpiarlos a fondo, transformarlos en variables útiles y finalmente guardarlos en un formato para su posterior uso. Con práctica, estos pasos se vuelven más naturales y podrás automatizar partes del proceso para futuros proyectos.

## Formatos y Herramientas de Almacenamiento de Datasets

Una vez que tienes tu dataset preparado, ¿en qué formato y dónde lo guardas? La elección del formato de almacenamiento es importante por razones de eficiencia, compatibilidad y escalabilidad. A continuación, se describen los formatos de archivo más comunes para datasets y algunas herramientas de bases de datos locales, así como una mención a soluciones avanzadas de almacenaje para Machine Learning.

Formatos de archivo principales:

CSV (Comma-Separated Values): El clásico formato de texto plano, donde cada línea es un registro y los campos se separan por comas (u otro delimitador, como punto y coma o tabulación). Es legible, simple y compatible con multitud de herramientas (Excel, Google Sheets, pandas, etc.). Ventajas: humano-legible, fácil de manipular con cualquier lenguaje. Desventajas: tamaño voluminoso (no comprimido), no guarda tipos de datos (todo es texto, al leer hay que inferir números, fechas), y no soporta estructuras anidadas. Aun así, para datasets medianos (~hasta algunos cientos de MB) es perfectamente utilizable y conveniente para compartir abiertamente.

JSON: Como formato de datos, JSON también se usa para almacenar datasets, especialmente si la estructura no es puramente tabular. Por ejemplo, podrías tener una lista de objetos JSON, cada uno con campos anidados. JSON es textuoso como CSV pero soporta jerarquías (diccionarios anidados, listas). Es muy útil para datos semiestructurados (por ejemplo, un dataset de artículos donde cada artículo tiene una lista de autores, un listado de secciones, etc.). En Python, se puede usar json o pandas read_json para cargarlo. Inconveniente: ocupa más que CSV normalmente (tiene muchos caracteres extra { } []) y no es tan eficiente para leer/escribir en bloque. A veces se combina con compresión (por ejemplo, almacenar JSON.gz).

Parquet: Es un formato columnar binario, parte del ecosistema Apache Hadoop. Altamente recomendado para datos tabulares grandes. Parquet guarda los datos por columnas, con compresión eficiente y tipo de datos preservados. Esto significa que archivos Parquet suelen pesar mucho menos que el CSV equivalente (por compresión y por no repetir cabeceras en cada fila), y pueden leerse selectivamente (por columnas) muy rápido. Con pandas, mediante el motor pyarrow, podemos hacer df.to_parquet("data.parquet") y pd.read_parquet("data.parquet"). Es ideal para big data y se integra con herramientas de análisis distribuido (Spark, Hive, etc.). Si tu dataset tiene millones de filas, Parquet manejará mejor la lectura/escritura que CSV.

Feather: Similar a Parquet en que se basa en Apache Arrow para ser un formato columnar binario. Feather está pensado específicamente para intercambiar data frames entre Python (pandas) y R de forma muy rápida. Un .feather es básicamente la representación en memoria de un DataFrame guardada en disco. Ofrece velocidades de lectura/escritura sorprendentes para datos tabulares. Sin embargo, Feather no tiene tantas opciones de compresión avanzada como Parquet ni es tan estándar en ecosistemas big data. Útil si necesitas pasar datasets entre Python/R o almacenar localmente con rendimiento, pero para archivos a largo plazo Parquet puede ser preferible.

Excel (.xlsx): Aunque no es ideal para grandes datasets, a veces se usa para compartir datos de tamaño pequeño/medio con usuarios no técnicos. Pandas puede leer/escribir Excel (pd.read_excel, df.to_excel), pero tiene limitaciones (por ejemplo, más de 1 millón de filas no caben en una hoja Excel). Además, Excel puede introducir formatos extraños, formulas, etc., así que como formato de intercambio reproducible no es lo óptimo. Mejor usar CSV/Parquet para proyectos de ML. Aun así, en entorno empresarial uno termina manejando Excel a menudo para extraer datos iniciales.

Otros formatos binarios: Existen más, p. ej. HDF5 (pandas to_hdf), que es eficiente para ciertos accesos rápidos a subsets, y Pickle de Python (que guarda objetos serializados, útil para guardar DataFrames tal cual pero ojo con la portabilidad y seguridad). Para imágenes, audio, etc., hay formatos propios (JPEG, PNG, WAV, etc.) pero esos suelen ser datos brutos más que dataset tabular.

Bases de datos locales:

A veces conviene guardar el dataset en una pequeña base de datos en lugar de un archivo plano, sobre todo si quieres hacer consultas complejas o parcialmente sobre los datos:

SQLite: es una base de datos SQL embebida en un archivo. Muy práctica para datasets pequeños o medianos. Puedes guardar tu conjunto de datos en una tabla SQLite y luego hacer consultas SQL para exploración. Por ejemplo, import sqlite3 en Python, crear una base mydata.db y usar pd.to_sql para volcar el DataFrame a una tabla. Ventajas: no necesitas servidor, todo está en un .db portable, y puedes indexar columnas para búsquedas rápidas. Desventaja: para ML al final igual tendrás que extraer todos los datos a memoria, pero sirve durante la fase de análisis exploratorio o para combinar datos mediante JOINs SQL si viene de múltiples tablas. SQLite maneja hasta gigabytes, pero el rendimiento baja si crece mucho el tamaño.

DuckDB: es una base de datos SQL embebida moderna, optimizada para análisis de columnas (similar en filosofía a Parquet). Ha ganado popularidad porque combina la facilidad de SQLite (un solo archivo .duckdb o en memoria) con un excelente rendimiento analítico, capaz de manejar datos más grandes en la propia máquina. DuckDB se integra muy bien con Python (puedes correr consultas SQL directamente sobre DataFrames pandas o archivos Parquet/CSV sin cargarlos completamente). Puede ser interesante usar DuckDB si tu dataset es enorme pero quieres filtrar/agregar datos antes de cargarlos al modelo.

PostgreSQL/MySQL local: Montar un servidor de base de datos completo localmente para un dataset puede ser útil si quieres aprender SQL o la naturaleza de los datos encaja mejor en un modelo relacional (varias tablas normalizadas). Sin embargo, para propósitos de crear un dataset de ML normalmente terminamos con una tabla simple combinada. Aun así, puedes usar un servidor SQL local si tu flujo de trabajo prefiere SQL para limpiar/join y luego extraer un CSV final.

Feature Stores y almacenes distribuidos (mención breve):

En proyectos de Machine Learning a escala empresarial, surgen necesidades de compartir y servir características (features) de forma consistente. Ahí entran los Feature Stores, que son sistemas (a menudo distribuidos) diseñados para almacenar los datasets de características de forma versionada, accesible tanto para entrenar modelos como para servir predicciones en producción. Empresas como Uber, Airbnb, etc., han popularizado esta idea. Un Feature Store típico se monta sobre una base de datos rápida (puede ser NoSQL, KV store, o SQL optimizado) y ofrece APIs para obtener conjuntos de datos listos para ML.

Por otro lado, cuando hablamos de almacenamiento distribuido, nos referimos a manejar datasets tan grandes o con necesidades de acceso concurrente tan altas que un solo archivo o base local no basta. En Big Data se usan lagos de datos en la nube (tipo Amazon S3, HDFS en Hadoop) donde los datasets pueden estar particionados en múltiples archivos Parquet, por ejemplo, y herramientas como Spark para procesarlos en paralelo. También entran aquí las bases de datos NoSQL distribuidas, que almacenan datos masivos y permiten consultas escalables (Cassandra, Bigtable, etc.).

Nota: Para esta guía nos centramos en datasets locales o de pequeño/mediano tamaño. Los feature stores y soluciones distribuidas son temas avanzados que se suelen ver más adelante (los mencionamos para tener contexto, pero profundizaremos en ellos en la Unidad 6).

En conclusión, elegir el formato de almacenamiento depende de las dimensiones del dataset y de cómo lo usarás: - Para portabilidad y compatibilidad: CSV es el rey. - Para eficiencia en Python: Parquet/Feather son excelentes. - Para consulta interactiva: SQLite/DuckDB te permiten filtrar antes de cargar. - Y si tu proyecto escala a nivel producción, quizá consideres feature stores o data lakes en el futuro.

## Mini-Ejemplo Integrado: Datos Climáticos de Open-Meteo API a CSV y Parquet

Para ilustrar el proceso completo de obtención y almacenamiento de un dataset, realicemos un mini-ejemplo práctico. El objetivo: obtener datos climáticos de una API pública y guardarlos en dos formatos (CSV y Parquet) para su uso posterior. Usaremos la API de Open-Meteo (una API meteorológica libre que no requiere API key) para conseguir la previsión del tiempo, y pandas para convertir los datos a un DataFrame y guardarlos.

Descripción del ejemplo: Supongamos que queremos un dataset con la previsión meteorológica de los próximos 7 días (temperaturas máximas y mínimas diarias) para una cierta ubicación geográfica. Elegiremos, por ejemplo, la ciudad de Cádiz, España (latitud ~36.5, longitud ~-6.3) y obtendremos el pronóstico de temperatura. Luego almacenaremos ese dataset en un archivo CSV y en un archivo Parquet.

Pasos que seguiremos: 1. Llamar a la API de Open-Meteo para obtener la previsión diaria de temperatura máxima y mínima. 2. Convertir la respuesta JSON a un pandas.DataFrame. 3. Guardar el DataFrame en clima_cadiz.csv y clima_cadiz.parquet.

Veamos el código en Python:

import requests
import pandas as pd

# 1. Definir parámetros y llamar a la API Open-Meteo
lat, lon = 36.53, -6.30  # Coordenadas aproximadas de Cádiz, España
api_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat,
    "longitude": lon,
    "daily": ["temperature_2m_max", "temperature_2m_min"],  # variables diarias a obtener
    "forecast_days": 7,         # días de pronóstico (hasta 7 días en este caso)
    "timezone": "Europe/Madrid" # zona horaria para las fechas
}
response = requests.get(api_url, params=params)
response.raise_for_status()      # lanza error si la petición falló
data = response.json()          # parsear respuesta JSON a dict

# 2. Extraer la parte relevante del JSON y convertir a DataFrame
daily_data = data.get("daily")   # en la estructura JSON, los datos diarios están bajo la clave "daily"
df = pd.DataFrame(daily_data)    # crea DataFrame con columnas: time, temperature_2m_max, temperature_2m_min
df.head()  # imprimir las primeras filas para inspeccionar

Tras la llamada, el JSON de Open-Meteo nos proporciona un objeto daily que contiene arrays con fechas, temp max y temp min[18]. Con pd.DataFrame(daily_data) pandas crea un DataFrame donde cada clave del JSON (time, temperature_2m_max, etc.) es una columna, y los valores son listas por día[19]. Por ejemplo, df tendrá esta pinta:

time  temperature_2m_max  temperature_2m_min
0  2025-12-12               18.5               12.3
1  2025-12-13               19.0               13.1
2  2025-12-14               17.8               11.8
... (hasta 7 filas)

Cada fila es un día, con su fecha y las temperaturas pronosticadas (ficticias en este ejemplo). Ahora continuamos con el guardado:

# 3. Guardar el DataFrame a CSV y Parquet
df.to_csv("clima_cadiz.csv", index=False)     # guardar a CSV sin índice extra
df.to_parquet("clima_cadiz.parquet", index=False)
print("Datasets guardados en CSV y Parquet.")

Y listo. Ahora tendríamos dos archivos: - clima_cadiz.csv: que se puede abrir en un editor de texto o Excel para verificar su contenido (7 filas, 3 columnas separadas por comas). - clima_cadiz.parquet: un archivo binario comprimido. Aunque no legible directamente, es eficiente si lo volvemos a cargar en pandas: pd.read_parquet("clima_cadiz.parquet") nos daría el mismo DataFrame.

¿Por qué guardar en ambos formatos? Quizá queremos compartir el CSV con compañeros o abrirlo rápidamente, mientras que Parquet lo usaremos en código Python para rapidez (imaginemos que en lugar de 7 días fueran 10 años de datos horarios; Parquet sería mucho más manejable en tamaño). Este ejemplo a pequeña escala muestra cómo integrar API + pandas para construir y persistir un dataset.

(Nota: Open-Meteo ofrece muchos más datos y opciones, incluyendo históricos. Aquí simplificamos a temperaturas diarias para ilustrar.)

Este mini-ejemplo cubre varias partes del flujo: - Uso de una API pública con requests. - Manejo de JSON de respuesta para construir una estructura tabular. - Almacenamiento en formatos comunes. - Todo ello con muy pocas líneas de código, gracias a la potencia de las librerías usadas. En proyectos reales, habría pasos adicionales (ej. validar que los datos son correctos, quizás combinar con datos de otras ciudades, etc.), pero la idea base es la misma.

## Introducción a Poetry (Gestión de Entornos y Dependencias)

Al desarrollar proyectos de ciencia de datos o Machine Learning, es importante manejar bien las dependencias (librerías) y el entorno de ejecución (versiones de Python, etc.). Poetry es una herramienta moderna que facilita enormemente esta tarea. A continuación, introduciremos qué es Poetry, cómo se usa para estructurar proyectos Python y cuáles son sus ventajas frente a usar simplemente pip y entornos virtuales (venv).

¿Qué es Poetry? Es un gestor de dependencias y empaquetado para proyectos Python. En palabras de su documentación, "Poetry te permite declarar las librerías de las que tu proyecto depende y se encargará de instalarlas/actualizarlas por ti, ofreciendo además un lockfile para instalaciones reproducibles"[20]. En otras palabras, Poetry combina en una sola herramienta lo que antes se hacía con pip (instalar paquetes) + venv (aislar entornos) + setup.py (definir un paquete). Con Poetry, cada proyecto tiene su propio entorno virtual aislado y un archivo de configuración pyproject.toml donde están listadas las dependencias exactas (y un poetry.lock que fija las versiones precisas instaladas, para garantizar que en cualquier máquina se instalen las mismas versiones).

Instalación de Poetry: Se instala de manera independiente a tus proyectos. Puedes instalarlo vía pip (pip install poetry) o mediante su instalador oficial. Una vez instalado, tienes el comando poetry disponible en terminal. Poetry es compatible con Python 3.9+ y funciona en Linux, macOS y Windows.

Ventajas frente a pip + venv:

Gestión automática del entorno virtual: Con Poetry no necesitas ejecutar manualmente python -m venv env ni activar el entorno. Al crear un proyecto, Poetry generará un entorno virtual aislado (normalmente en una ubicación central o dentro del proyecto) y todas las instalaciones de paquetes irán allí. Puedes usar poetry shell para entrar al entorno o poetry run <comando> para ejecutarlo dentro del entorno.

Archivo de dependencias declarativas: En pip, muchas veces uno acaba con un requirements.txt escrito a mano o generado con pip freeze (que incluye versiones). Poetry hace esto más elegante con el pyproject.toml: allí declaras por ejemplo que tu proyecto depende de pandas ^2.0 y fastapi ^0.100. Poetry resolverá versiones compatibles y las fijará en poetry.lock. Esto evita conflictos y asegura que todos los colaboradores usen las mismas versiones, reduciendo “pero en mi máquina funciona”.

Publicación sencilla: Si algún día quieres empacar tu proyecto como librería, Poetry puede generar archivos de distribución (wheel) fácilmente a partir de la misma configuración, sin tener que escribir setup.py.

Comandos integrados: Poetry ofrece comandos para tareas comunes: add para agregar dependencia (similar a pip install pero actualiza pyproject y lock), update para actualizar todas, remove para quitar, etc. También run para ejecutar comandos dentro del entorno sin activarlo manualmente, y export para exportar a requirements.txt si lo necesitas.

Comparado con pipenv: Poetry es similar a pipenv (otro gestor) pero muchos lo prefieren por ser más rápido y tener mayor predictibilidad en resolución de versiones.

Crear la estructura de un proyecto con Poetry: Supongamos que quieres empezar un nuevo proyecto de ciencia de datos llamado "MiProyecto". Usando Poetry harías:

$ poetry new MiProyecto

Esto creará una carpeta MiProyecto/ con una estructura básica:

MiProyecto/
├── pyproject.toml
├── README.md
├── MiProyecto/__init__.py
└── tests/

Aquí MiProyecto/ (subcarpeta) es un paquete Python vacío por ahora, y Poetry ya inicializó pyproject.toml con el nombre del proyecto y la dependencia de Python. Para un proyecto de data science quizá prefieras una estructura ligeramente distinta. Muchas veces se usa:

MiProyecto/
├── pyproject.toml
├── README.md
├── data/
├── notebooks/
├── src/          (código fuente, a veces en lugar del paquete nombrado)
├── MiProyecto/   (paquete con código fuente principal)
└── tests/

No estás obligado a seguir una plantilla fija, pero es importante organizar: podrías tener tus notebooks Jupyter en una carpeta separada, los datos brutos o procesados en data/, el código Python (funciones, scripts, etc.) dentro de src/ o directamente en el paquete nominal. Poetry no impone cómo trabajas dentro, solo se encarga de las dependencias.

Añadir dependencias (librerías) con Poetry: Imaginemos que nuestro proyecto necesitará pandas, requests y fastapi. Podemos agregar esas librerías haciendo:

$ cd MiProyecto/
$ poetry add pandas requests fastapi

Poetry resolverá las últimas versiones compatibles (respetando posibles restricciones) e instalará los paquetes en el entorno del proyecto. Tras esto, en pyproject.toml verás algo así:

[tool.poetry.dependencies]
python = ">=3.10,<3.12"
pandas = "^2.1.0"
requests = "^2.31.0"
fastapi = "^0.103.0"

Y en poetry.lock quedarán las versiones exactas elegidas (por ejemplo pandas 2.1.1, requests 2.31.0, fastapi 0.103.2, además de sub-dependencias como numpy, pydantic, Starlette, etc.). Ahora, si otro desarrollador clona este proyecto, solo debe hacer poetry install dentro de la carpeta y Poetry leerá el lockfile e instalará exactamente esas versiones.

Usando Poetry en el día a día: Una vez que tienes todo configurado, trabajas así:

Puedes abrir tus notebooks Jupyter dentro del entorno de Poetry. Por ejemplo, poetry run jupyter notebook lanzará Jupyter con las dependencias disponibles. (También puedes instalar ipykernel y crear un kernel específico, pero no es obligatorio).

Si vas a correr un script Python, poetry run python script.py.

Si quieres depurar dentro del entorno, poetry shell te da una terminal con el venv activo.

Cuando termines el proyecto o quieras compartirlo, tus archivos .toml y .lock garantizan replicabilidad. Incluso puedes usar poetry export -f requirements.txt > requirements.txt si necesitas un requirements.txt clásico.

Ventajas resumidas de Poetry: - Centraliza la configuración del proyecto (nombre, versión, dependencias) en un solo archivo. - Hace más fácil recrear entornos exactamente iguales. - Evita instalar paquetes globalmente por error: siempre todo va al venv del proyecto. - Puede manejar múltiples entornos/proyectos en la misma máquina sin conflictos. - En proyectos colaborativos, elimina el "¿qué versión de X usaste?" ya que todo está en pyproject/lockfile.

En conclusión, Poetry es una herramienta muy útil para proyectos de datos donde sueles depender de muchas librerías. Facilita comenzar con buen pie en la gestión de entornos, algo crucial para que tu proyecto de creación de datasets (y posteriores modelos) sea reproducible y mantenible.

## Introducción a Servir Datos con FastAPI

Una vez que has construido un dataset, a veces surge la necesidad de compartirlo o exponerlo a otras personas o sistemas de forma dinámica. Por ejemplo, podrías querer construir una pequeña aplicación web que entregue cierta porción del dataset bajo demanda, o un servicio interno donde los modelos puedan solicitar datos. Aquí es donde entra FastAPI, un framework web ligero y muy veloz para construir APIs con Python. Veamos qué es FastAPI y cómo podemos usarlo para servir datos de manera sencilla.

¿Qué es FastAPI? FastAPI es un framework web de alto rendimiento para construir APIs con Python 3.7+ basado en las anotaciones de tipo estándar de Python[21]. Se ha vuelto popular por ser muy rápido (aprovecha internamente Starlette y Pydantic para rendimiento similar a Node.js o Go[22]), y muy sencillo de usar: con muy pocas líneas puedes crear endpoints (URLs que devuelven datos) y automáticamente obtienes documentación interactiva. En resumen, FastAPI te permite pasar de una función Python a un servicio web REST completo con mínimo código, aprovechando la asincronía y la validación de datos.

¿Por qué exponer datos con una API? Tener los datos en un archivo o DataFrame está bien para análisis offline, pero si quieres integrarlos en una aplicación necesitas una interfaz. Por ejemplo:

Una aplicación web frontend (JavaScript) podría pegarle a tu API para obtener los datos filtrados y mostrar gráficos al usuario.

Un equipo diferente podría consumir tus datos mediante peticiones en lugar de compartir archivos por correo.

Puedes restringir o procesar sobre la marcha qué entregas: quizá tu dataset es enorme, pero ofreces un endpoint que solo devuelve un resumen o los últimos N registros.

También permite desacoplar: tu sistema de datos permanece separado del código de otros, comunicándose solo vía la API. Esto sigue la arquitectura de microservicios o simplemente client-server, donde las APIs son la columna vertebral de la arquitectura moderna, permitiendo modularizar y mantener fácilmente las aplicaciones[23].

Conceptos básicos de FastAPI: Al usar FastAPI se suele:

Crear una instancia de la aplicación: app = FastAPI().

Definir operaciones de ruta (endpoints) usando decoradores. Por ejemplo @app.get("/datos") encima de una función la convierte en un manejador para peticiones GET a la URL /datos.

Dentro de la función, puedes acceder a parámetros de query, cuerpo, etc., y finalmente devolver datos (Python dict, list, Pydantic model, etc.). FastAPI se encarga de serializarlos a JSON automáticamente.

Ejemplo básico sirviendo un dataset: Supongamos que tenemos un archivo CSV con datos (por simplicidad, usamos el clima_cadiz.csv del ejemplo anterior) y queremos que FastAPI ofrezca dos endpoints:

GET /clima – que devuelve todo el dataset en formato JSON.

GET /clima/{dia} – que dado un día específico (p. ej. "2025-12-14") devuelva la fila de ese día o un mensaje si no existe.

Podemos implementar esto así:

from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Cargar datos al iniciar (puede ser global para simplicidad; en real, usar async db etc.)
df = pd.read_csv("clima_cadiz.csv")  # nuestro dataset de ejemplo

@app.get("/clima")
def leer_clima_completo():
    # Convertir DataFrame a lista de dicts
    datos = df.to_dict(orient="records")
    return datos

@app.get("/clima/{fecha}")
def leer_clima_por_fecha(fecha: str):
    # Filtrar el DataFrame por la fecha solicitada
    fila = df[df["time"] == fecha]
    if fila.empty:
        raise HTTPException(status_code=404, detail="Fecha no encontrada")
    resultado = fila.to_dict(orient="records")[0]
    return resultado

En este código: - Leemos el CSV una vez. (Nota: si el CSV es grande, quizás se use una base de datos o similar. Pero para ejemplo está bien). - El endpoint /clima convierte el DataFrame completo a una lista de registros Python (cada registro es un dict con las columnas) y FastAPI lo devolverá como JSON automáticamente. - El endpoint /clima/2025-12-14 aceptará ese parámetro en la URL, lo busca en la columna "time" del DataFrame. Si no encuentra, lanza un error 404. Si encuentra, convierte esa única fila a dict y la retorna. - Gracias a FastAPI y Pydantic, incluso la validación de que fecha es str se realiza (podríamos mejor parsear a date, pero mantuvimos str para simplicidad).

FastAPI automáticamente genera documentación interactiva (Swagger UI) en /docs donde verías estos endpoints y podrías probarlos.

Ejecutar la aplicación FastAPI: Para poner esto en marcha localmente, usamos Uvicorn, un servidor ASGI que ejecuta aplicaciones FastAPI. Desde la terminal, estando en tu proyecto (y con el entorno Poetry o venv activo con fastapi instalado), ejecutas:

uvicorn nombre_del_archivo:app --reload

Por ejemplo, si el código anterior está en servidor.py, harías:

uvicorn servidor:app --reload

La opción --reload es útil en desarrollo: recarga el servidor si detecta cambios en el código. Una vez corriendo (por defecto en http://127.0.0.1:8000), puedes abrir en un navegador http://127.0.0.1:8000/clima y ver el JSON completo, o http://127.0.0.1:8000/clima/2025-12-14 para la fecha específica. También http://127.0.0.1:8000/docs mostrará la UI de documentación donde puedes probar los endpoints sin salir del navegador.

Integración con Poetry: Si usaste Poetry para gestionar este proyecto, puedes correr el servidor via Poetry sin problemas:

$ poetry run uvicorn servidor:app --reload

Esto utiliza el uvicorn instalado en el entorno Poetry. También podrías agregar uvicorn como dependencia de desarrollo via poetry add -D uvicorn para que quede registrado.

Consideraciones al servir datos: Ten en cuenta:

Si el dataset es grande, mejor implementar paginación o filtros en la API para no enviar miles de registros en cada request.

Para datos muy sensibles, habría que agregar autenticación/autorización a las rutas (FastAPI tiene soporte para OAuth2, JWT, etc.).

FastAPI permite fácilmente formatear la respuesta en otros formatos también (puedes devolver FileResponse para entregar un CSV como descarga, por ejemplo). Un ejemplo simple:

from fastapi.responses import FileResponse

@app.get("/descarga_csv")
def descargar_csv():
    return FileResponse("clima_cadiz.csv", media_type="text/csv", filename="clima.csv")

Esto serviría el archivo CSV completo para descarga cuando se acceda a /descarga_csv. Así ofreces ambas opciones: ver JSON en línea o descargar el dataset.

FastAPI es asíncrono por naturaleza, por lo que si la obtención de datos implicara llamadas lentas (db, otro API), podrías marcar las funciones con async def y usar await para mayor rendimiento con muchas peticiones concurrentes.

¿Por qué FastAPI y no otros frameworks? En Python existían ya Flask, Django, etc. FastAPI destaca por su rendimiento superior y por la productividad que brinda (menos código repetitivo, documentación automática, validación de tipos). Para una simple API de datos como la del ejemplo, podrías hacerlo en Flask con funcionalidad similar, pero FastAPI te da ya una capa adicional de robustez y velocidad sin complicación extra. De hecho, en pruebas de rendimiento, FastAPI suele superar a la mayoría de frameworks web Python[24], acercándose al rendimiento de lenguajes más bajos, lo que significa que incluso sirviendo datos a usuarios reales tendrás buen desempeño.

En resumen, FastAPI te permite convertir tu dataset en un servicio web rápida y fácilmente. Puedes empezar exponiendo un simple endpoint que devuelva datos crudos o resumidos, e ir construyendo más funcionalidad (filtros, agregaciones, incluso endpoints que corran modelos ML) dentro de la misma aplicación. Para nuestros propósitos iniciales, saber que con unas pocas líneas podemos servir un CSV o un fragmento de DataFrame vía HTTP abre la puerta a crear prototipos de data products útiles, donde otros sistemas puedan aprovechar los datos que hemos recopilado y preparado.

¡Conclusión: Crear tu propio dataset de aprendizaje automático es un proceso desafiante pero gratificante. Requiere combinar habilidades de recolección (APIs, scraping, IoT, logs, open data), ingeniería de datos (limpieza, transformación, almacenamiento) y también buenas prácticas de desarrollo (gestión de dependencias con Poetry, servir resultados con FastAPI). Siguiendo esta guía, tienes un panorama completo para iniciarte en la construcción de datasets a medida. Desde la justificación teórica hasta la implementación práctica con Python, ahora cuentas con las bases para desarrollar conjuntos de datos personalizados** que te permitan abordar problemas de Machine Learning del mundo real con datos relevantes y bien gestionados. ¡Manos a la obra con tus propios datos![10][25]

[1] [2] [3] [25] Custom vs Pre-Built Datasets – How to Choose, When to Build

https://groupbwt.com/blog/custom-vs-pre-built-datasets/

[4] [5] [6] [7] [8] [9] [10] [16] [17] ¿Dónde están los datos? Arma tu propio dataset | by Farid Murzone | EscuelaDeInteligenciaArtificial | Medium

https://medium.com/escueladeinteligenciaartificial/d%C3%B3nde-est%C3%A1n-los-datos-arma-tu-propio-dataset-2040959ffb08

[11] [12] Logs: Qué son y cómo se usan para monitorizar sistemas y seguridad

https://www.godaddy.com/resources/latam/tecnologia/log-que-es

[13] [14] [15] 13 paquetes de software Open Source para IoT - Tu fuente experta en IoT

https://iotconsulting.tech/10-paquetes-de-software-open-source-para-iot/

[18] [19] Weather Forecast using OpenMeteo API — Geospatial Python Tutorials

https://www.geopythontutorials.com/notebooks/openmeteo_weather_forecast.html

[20]  Introduction | Documentation | Poetry - Python dependency management and packaging made easy

https://python-poetry.org/docs/

[21] [23] [24] Tutorial de FastAPI: Introducción al uso de FastAPI | DataCamp

https://www.datacamp.com/es/tutorial/introduction-fastapi-tutorial

[22] FastAPI

https://fastapi.tiangolo.com/es/