# Configuracion del diagnostico inicial - PIA 2026/2027

El formulario historico de Google Forms mezclaba situacion personal, experiencia
tecnica y conocimientos de Big Data. Para 2026/2027 se divide en dos actividades
de Moodle, ambas no evaluables. Asi se conserva informacion util para el inicio
del curso sin mezclar contenidos que corresponden a SBD.

## 1. Encuesta inicial PIA - actividad Feedback

Crear una actividad **Feedback** anonima, sin item de calificacion y con un plazo
corto durante la primera semana. No pedir nombre, empresa, direccion ni detalles
personales. Su finalidad es anticipar apoyos y adaptar el ritmo inicial.

| Pregunta | Tipo recomendado | Obligatoria |
|---|---|---|
| Durante el curso, tienes o preves tener trabajo con contrato? (Si / No / Tal vez) | Eleccion multiple | No |
| Existe alguna circunstancia que pueda dificultar tu asistencia regular? | Si/No | No |
| Si lo deseas, indica que tipo de apoyo o anticipacion de materiales te ayudaria. | Texto largo | No |
| Como valoras tu experiencia previa con programacion? (0 ninguna - 5 alta) | Eleccion multiple | Si |
| Como valoras tu experiencia previa con Python o notebooks? (0 ninguna - 5 alta) | Eleccion multiple | Si |
| Como valoras tu experiencia previa con IA, machine learning o deep learning? (0 ninguna - 5 alta) | Eleccion multiple | Si |
| Que asistentes conversacionales has usado? (ChatGPT, Claude, Gemini, Copilot, Perplexity, ninguno u otro) | Seleccion multiple | No |
| Que herramientas de desarrollo asistido o agentes has usado? (GitHub Copilot, Cursor, Claude Code, Codex, OpenCode, ninguna u otra) | Seleccion multiple | No |
| Has ejecutado algun modelo local? (Ollama, llama.cpp, LM Studio, otra herramienta, no) | Seleccion multiple | No |
| Que herramientas generales has usado? (Python, Jupyter/Colab, Git, VS Code, ninguna u otra) | Seleccion multiple | No |

La pregunta sobre dificultades no debe usarse para valorar asistencia ni
calificacion. Solo sirve para detectar necesidades de apoyo o comunicacion.

## 2. Diagnostico tecnico PIA - cuestionario Moodle GIFT

Importar `01-fundamentos-python/04-evaluacion/cuestionario-diagnostico-inicial-pia.gift`.
Contiene 20 preguntas de opcion multiple sobre Python, notebooks, IA, machine
learning, deep learning, evaluacion, LLM, RAG, agentes de IA, modelos locales y
uso responsable de asistentes de IA. Las opciones `No lo se todavia` permiten
distinguir desconocimiento de una eleccion incorrecta.

Configurar el cuestionario asi:

- Nombre: `Diagnostico tecnico inicial PIA`.
- Proposito: conocer el punto de partida y comentar resultados generales.
- Calificacion: sin peso en la categoria de UD1 ni en el total Moodle; ocultar o
  excluir el item de calificacion.
- Intentos: uno; retroalimentacion general disponible al cerrar el intento.
- Tiempo orientativo: 15 minutos.
- Mostrar una explicacion breve tras cada respuesta si se desea, sin usar el
  resultado para acreditacion de RA/CE.

## Del formulario anterior a la version actual

- Se conservan las preguntas sobre trabajo, regularidad de asistencia,
  programacion, Python, IA, machine learning y deep learning.
- Se transforman las autoevaluaciones tecnicas en un test breve con respuestas
  corregibles, que permite identificar mejor los conceptos a repasar.
- Se anaden experiencia declarada y preguntas tecnicas sobre LLM, RAG, agentes
  de codigo y modelos locales, porque son contenidos activos de UD6 y UD7.
- Se retiran las preguntas de Big Data, bases de datos y SQL: se incorporaran al
  diagnostico especifico del modulo SBD.
