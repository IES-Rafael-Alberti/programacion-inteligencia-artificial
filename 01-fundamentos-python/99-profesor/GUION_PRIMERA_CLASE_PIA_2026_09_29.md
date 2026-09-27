# Guion de primera clase — PIA — 29 de septiembre de 2026

> **Documento interno del profesorado. No publicar en GitHub Pages ni en Moodle.**

Duración total prevista: 2 horas. La presentación debería durar entre 15 y 20
minutos, pero el guion conserva una ruta válida si llega a 30: se reduce el
bloque de instalación y el diagnóstico técnico pasa a Moodle como tarea no
evaluable antes de la siguiente sesión.

## Antes de entrar al aula

- Abrir `docs/presentacion-curso.md` y la página `docs/unidades/ud01.md`.
- Tener preparada una terminal en la raíz del repositorio y JupyterLab o Google
  Colab como alternativa de demostración.
- Tener visible el notebook
  `01-fundamentos-python/02-ejemplos/01_introduccion_entorno_python.ipynb`.
- Confirmar que Moodle contiene los recursos del checklist de
  `../../00-planificación/CHECKLIST_MOODLE_UD1_2026_2027.md`.
- Tener abierto el portal GitHub Pages y el cuestionario `Diagnóstico técnico
  inicial PIA`, sin nota y excluido del calificador.
- Preparar una pizarra con tres columnas: `Qué quiero aprender`, `Qué ya sé`,
  `Incidencias de acceso`.

## Presentación del módulo — 15 a 20 minutos

| Tiempo | Mensaje y acción docente |
| ---: | --- |
| 0–2 min | Bienvenida. «No vamos a pulsar botones de IA: vamos a construir soluciones que expliquen qué datos usan, qué modelo eligen y por qué el resultado merece confianza». |
| 2–5 min | Mostrar el recorrido: Python y datos, ML, deep learning, cloud/MLOps, LLM y agentes, visión, GPU, series temporales y proyecto integrado. UD11 es ampliación opcional. |
| 5–8 min | Explicar el producto final: una solución pequeña pero útil, reproducible y defendible. El proyecto integrado usa al menos dos fuentes de datos y una salida útil. |
| 8–11 min | Explicar la forma de trabajo: teoría breve, ejemplos ejecutables, prácticas y rúbricas. El portal orienta; el repositorio contiene notebooks y código. Pixi es el gestor operativo cuando la actividad lo indique. |
| 11–14 min | Uso responsable de IA: se permite como apoyo, pero hay que declarar lo relevante, verificar resultados y poder defender cada decisión. Nunca subir claves, tokens, datos personales o datasets no autorizados. |
| 14–17 min | Evaluación: Séneca calcula por RA/CE; Moodle organiza evidencias. Mostrar RA1 15 %, RA2 45 %, RA3 20 % y RA4 20 %. |
| 17–20 min | Reglas: plazos de Moodle, retraso del 5 % por cada periodo de 24 horas iniciado hasta un máximo del 35 %, comunicación de incidencias antes del vencimiento y posible defensa individual. Cerrar preguntando qué les gustaría automatizar o analizar. |

No leas el documento completo. Usa `docs/presentacion-curso.md` como apoyo visual
y reserva los detalles de cada unidad para cuando se trabaje.

## Ritmo principal — presentación de 20 minutos

| Tiempo | Actividad | Resultado esperado |
| ---: | --- | --- |
| 20–30 min | Abrir Moodle. Comprobar el acceso y localizar la presentación, la guía de inicio, UD1 y el portal GitHub Pages. Indicar el canal de incidencias. | Todo el grupo sabe dónde encontrar cada recurso. |
| 30–45 min | Realizar el diagnóstico técnico inicial. Quien termine antes completa la encuesta Feedback sobre circunstancias y experiencia. | Punto de partida del grupo, sin calificación. |
| 45–55 min | Mostrar la estructura del repositorio. Quien pueda lo clona; el resto lo descarga como ZIP. Explicar Pixi y Google Colab como alternativa temporal. | Nadie queda bloqueado por una instalación. |
| 55–70 min | Presentar UD1: automatizar una tarea requiere datos de entrada, reglas, resultados comprobables y código reutilizable. Abrir `01_introduccion_entorno_python.ipynb`. | Relaciona Python con la automatización de un problema sencillo. |
| 70–95 min | Trabajo guiado: ejecutar y modificar ejemplos de variables, operadores y conversiones. Pedir que cambien dos valores y expliquen el resultado. | Cada estudiante ejecuta o comprende el primer notebook. |
| 95–110 min | Mini-reto individual: conversor de euros a dólares con una variable de tipo de cambio. Ampliación: validar una entrada o convertir una lista de importes. | Primera solución propia y muy acotada. |
| 110–118 min | Puesta en común: dos voluntarios explican una decisión de código. Recoger en la pizarra dudas y conocimientos previos. | Se normaliza preguntar y se detectan apoyos necesarios. |
| 118–120 min | Cierre y siguiente paso. | Saben qué deben completar del diagnóstico o del notebook, si les falta. |

## Ritmo alternativo — presentación de hasta 30 minutos

No recortes la presentación a costa de acelerar el bloque práctico. Si el grupo
pregunta o necesita contexto, usa este orden:

| Tiempo | Actividad |
| ---: | --- |
| 0–30 min | Presentación de PIA, sin añadir detalles de unidades futuras. |
| 30–40 min | Moodle, portal y acceso a los materiales. |
| 40–55 min | Estructura del repositorio y explicación breve de Pixi/Colab. |
| 55–80 min | Notebook inicial guiado: variables, operaciones y salida. |
| 80–105 min | Mini-reto del conversor y puesta en común. |
| 105–115 min | Registrar incidencias y explicar que el diagnóstico técnico se completa en Moodle antes de la próxima sesión. |
| 115–120 min | Cierre. |

No abras repositorios individuales, no instales dependencias adicionales ni inicies
el cuestionario base de UD1 en esta primera clase. Son pasos posteriores y no
deben desplazar el arranque práctico.

## Qué decir en el bloque de UD1

### Transición tras la presentación

> Ya sabemos hacia dónde va el módulo. Ahora empezamos por la herramienta que
> nos permitirá construir y comprobar esas soluciones: Python. No hace falta que
> todos partáis del mismo nivel; el diagnóstico y las primeras prácticas sirven
> precisamente para que sepamos desde donde empezamos.

### Antes del notebook

Explica solo estas cuatro ideas:

1. Un programa recibe datos, aplica reglas y produce un resultado comprobable.
2. Una variable da nombre a un dato para poder usarlo y modificarlo.
3. Ejecutar código no basta: hay que mirar si el resultado tiene sentido.
4. Un notebook mezcla explicación, código y resultados; por eso lo usaremos para
   aprender, experimentar y documentar.

No adelantes NumPy, modelos ni LLM en este bloque. Menciónalos solo como destino
del recorrido, no como contenidos que deban comprender hoy.

### Mini-reto

Escribe primero el enunciado en la pizarra:

```text
Convierte una cantidad en euros a dólares.
Usa una variable para el importe y otra para el tipo de cambio.
Muestra un mensaje que permita comprobar el resultado.
```

Si alguien termina, pide una ampliación, no otro ejercicio distinto: convertir
varios importes, redondear el resultado o explicar en una celda de texto qué
ocurriría si cambia el tipo de cambio.

## Cierre y continuidad

Pide un ticket de salida, en Moodle o en papel:

```text
Una cosa que ya manejo:
Una cosa que necesito repasar:
Una incidencia de acceso, si la tengo:
```

Tarea no evaluable para la siguiente sesión:

- Completar el diagnóstico técnico si no se realizó en clase.
- Ejecutar o revisar el notebook inicial y modificar al menos dos valores.
- Registrar una incidencia con el equipo, sistema operativo, comando y mensaje
  de error completo; no instalar paquetes al azar para resolverla.

## Criterio de salida de la sesión

- El alumnado sabe dónde están Moodle, el portal y el repositorio.
- Todo el grupo conoce las reglas de entregas y uso de IA.
- Cada estudiante ha abierto o ejecutado el primer notebook y realizado una
  modificación sencilla.
- Las incidencias de acceso quedan registradas; no se califican actividades en
  esta primera sesión.
