# Checklist de entrega — UD6 LLM y agentes

Usa esta lista antes de entregar. Primero verifica lo imprescindible; después revisa los detalles que facilitan la corrección.



## Imprescindible

- [ ] La entrega incluye el notebook, script o proyecto que resuelve la práctica indicada.
- [ ] El flujo principal ejecuta sin errores críticos en el entorno previsto.
- [ ] Hay al menos una evidencia de funcionamiento: captura, log, ejemplo de entrada/salida o respuesta de API/interfaz.
- [ ] No se entregan claves API, tokens, contraseñas, ficheros `.env` reales ni credenciales.
- [ ] Se indica cómo ejecutar o revisar la solución.

## Formato de entrega

- Entregar una carpeta comprimida o repositorio según indique el profesorado.
- Mantener nombres de archivos claros y estructura ordenada.
- Incluir solo material necesario para revisar la práctica.
- Si se entrega un notebook, dejarlo ejecutado o con salidas relevantes cuando el tamaño lo permita.
- Si se entrega una API o interfaz, explicar cómo arrancarla y cómo probarla.

## Archivos requeridos

- [ ] Código fuente o notebook principal.
- [ ] `README.md` o apartado equivalente con instrucciones de ejecución.
- [ ] Fichero de dependencias si ya forma parte del proyecto: `requirements.txt`, `environment.yml`, `pyproject.toml` u otro equivalente.
- [ ] Datos de ejemplo permitidos o instrucciones para obtenerlos, si son necesarios.
- [ ] Evidencias de prueba: capturas, logs, ejemplos de consulta/respuesta o métricas.

No inventes dependencias nuevas si la práctica no las necesita.

## Evidencias mínimas

| Área | Evidencia recomendada |
| --- | --- |
| Interfaz/API | Captura de Gradio, ejemplo de petición FastAPI o salida de endpoint. |
| Orquestación | Diagrama breve, explicación del pipeline o fragmento que muestre nodos/cadenas/herramientas. |
| RAG | Ejemplo de documento cargado, consulta realizada y respuesta generada con contexto recuperado. |
| Evaluación | Métrica, comparación, log de MLflow o tabla de pruebas si la práctica lo incorpora. |
| Uso responsable | Nota sobre límites, posibles errores del modelo y protección de datos o claves. |

## Comprobaciones antes de entregar

- [ ] He reiniciado el kernel o proceso y he probado el flujo desde cero.
- [ ] Las rutas son relativas o están explicadas; no dependen de mi ordenador personal.
- [ ] Las instrucciones permiten reproducir la ejecución sin adivinar pasos.
- [ ] Las salidas mostradas corresponden a la versión entregada.
- [ ] Los errores conocidos están documentados con una explicación breve.
- [ ] Los nombres de variables, funciones y archivos son comprensibles.

## Claves, APIs y secretos

- No subas claves reales a notebooks, scripts, capturas ni historial del repositorio.
- Usa variables de entorno o ficheros `.env.example` sin valores reales.
- Si usas un proveedor externo, indica solo el nombre del servicio y las variables necesarias.
- Si has expuesto una clave por error, avisa al profesorado y revócala antes de entregar.

## Cuestionarios

Si el profesorado activa los cuestionarios GIFT en Moodle, complétalos como verificación conceptual. Son complemento de la entrega práctica, no sustituto automático de las evidencias técnicas.
