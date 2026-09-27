# Guion de primera clase - PIA - 29 de septiembre de 2026

> **Documento interno del profesorado. No publicar en GitHub Pages ni en Moodle.**

Duracion total prevista: 2 horas. La presentacion debe durar 15-20 minutos,
pero el guion conserva una ruta valida si llega a 30: se reduce el bloque de
instalacion y el diagnostico tecnico pasa a Moodle como tarea no evaluable antes
de la siguiente sesion.

## Antes de entrar al aula

- Abrir `docs/presentacion-curso.md` y la pagina `docs/unidades/ud01.md`.
- Tener preparada una terminal en la raiz del repositorio y JupyterLab o Google
  Colab como alternativa de demostracion.
- Tener visible el notebook
  `01-fundamentos-python/02-ejemplos/01_introduccion_entorno_python.ipynb`.
- Confirmar que Moodle contiene los recursos del checklist de
  `../../00-planificación/CHECKLIST_MOODLE_UD1_2026_2027.md`.
- Tener abierto el portal GitHub Pages y el cuestionario `Diagnostico tecnico
  inicial PIA`, sin nota y excluido del calificador.
- Preparar una pizarra con tres columnas: `Que quiero aprender`, `Que ya se`,
  `Incidencias de acceso`.

## Presentacion del modulo - 15 a 20 minutos

| Tiempo | Mensaje y accion docente |
|---:|---|---|
| 0-2 min | Bienvenida. "No vamos a pulsar botones de IA: vamos a construir soluciones que expliquen que datos usan, que modelo eligen y por que el resultado merece confianza." |
| 2-5 min | Mostrar el recorrido: Python y datos, ML, deep learning, cloud/MLOps, LLM y agentes, vision, GPU, series temporales y proyecto integrado. UD11 es ampliacion opcional. |
| 5-8 min | Explicar el producto final: una solucion pequena pero util, reproducible y defendible. El proyecto integrado usa al menos dos fuentes de datos y una salida util. |
| 8-11 min | Explicar la forma de trabajo: teoria breve, ejemplos ejecutables, practicas y rubricas. El portal orienta; el repositorio contiene notebooks y codigo. Pixi es el gestor operativo cuando la actividad lo indique. |
| 11-14 min | Uso responsable de IA: se permite como apoyo, pero hay que declarar lo relevante, verificar resultados y poder defender cada decision. Nunca subir claves, tokens, datos personales o datasets no autorizados. |
| 14-17 min | Evaluacion: Seneca calcula por RA/CE; Moodle organiza evidencias. Mostrar RA1 15 %, RA2 45 %, RA3 20 % y RA4 20 %. |
| 17-20 min | Reglas: plazos de Moodle, retraso del 5 % por cada periodo de 24 horas iniciado hasta un maximo del 35 %, comunicacion de incidencias antes del vencimiento y posible defensa individual. Cerrar preguntando que les gustaria automatizar o analizar. |

No leer el documento completo. Usar `docs/presentacion-curso.md` como apoyo visual
y reservar detalles de cada unidad para cuando se alcance.

## Ritmo principal - presentacion de 20 minutos

| Tiempo | Actividad | Resultado esperado |
|---:|---|
| 20-30 min | Abrir Moodle. Comprobar acceso, localizar la presentacion, la guia de inicio, UD1 y el portal GitHub Pages. Indicar el canal de incidencias. | Todo el grupo sabe donde encontrar cada recurso. |
| 30-45 min | Realizar el diagnostico tecnico inicial. Quien termine antes completa la encuesta Feedback de circunstancias y experiencia. | Punto de partida del grupo sin calificacion. |
| 45-55 min | Mostrar la estructura del repositorio. Quien pueda lo clona; el resto lo descarga como ZIP. Explicar Pixi y Google Colab como alternativa temporal. | Nadie queda bloqueado por una instalacion. |
| 55-70 min | Presentar UD1: automatizar una tarea requiere datos de entrada, reglas, resultados comprobables y codigo reutilizable. Abrir `01_introduccion_entorno_python.ipynb`. | Relaciona Python con la automatizacion de un problema sencillo. |
| 70-95 min | Trabajo guiado: ejecutar y modificar ejemplos de variables, operadores y conversiones. Pedir que cambien dos valores y expliquen el resultado. | Cada estudiante ejecuta o comprende el primer notebook. |
| 95-110 min | Mini-reto individual: conversor de euros a dolares con una variable de tipo de cambio. Ampliacion: validar una entrada o convertir una lista de importes. | Primera solucion propia y muy acotada. |
| 110-118 min | Puesta en comun: dos voluntarios explican una decision de codigo. Recoger en la pizarra dudas y conocimientos previos. | Se normaliza preguntar y se detectan apoyos necesarios. |
| 118-120 min | Cierre y siguiente paso. | Saben que deben completar el diagnostico o el notebook si les falta. |

## Ritmo alternativo - presentacion de hasta 30 minutos

No recortar la presentacion a costa de correr el bloque practico. Si el grupo
pregunta o necesita contexto, usar este orden:

| Tiempo | Actividad |
|---:|---|
| 0-30 min | Presentacion PIA, sin anadir detalles no previstos de unidades futuras. |
| 30-40 min | Moodle, portal y acceso a los materiales. |
| 40-55 min | Estructura del repositorio y explicacion breve de Pixi/Colab. |
| 55-80 min | Notebook inicial guiado: variables, operaciones y salida. |
| 80-105 min | Mini-reto del conversor y puesta en comun. |
| 105-115 min | Registrar incidencias y explicar que el diagnostico tecnico se completa en Moodle antes de la proxima sesion. |
| 115-120 min | Cierre. |

No abrir repositorios individuales, instalar dependencias adicionales ni iniciar
el cuestionario base de UD1 en esta primera clase. Son pasos posteriores y no
deben desplazar el arranque practico.

## Que decir en el bloque de UD1

### Transicion, tras la presentacion

> Ya sabemos hacia donde va el modulo. Ahora empezamos por la herramienta que
> nos permitira construir y comprobar esas soluciones: Python. No hace falta que
> todos partais del mismo nivel; el diagnostico y las primeras practicas sirven
> precisamente para que sepamos desde donde empezamos.

### Antes del notebook

Explica solo estas cuatro ideas:

1. Un programa recibe datos, aplica reglas y produce un resultado comprobable.
2. Una variable da nombre a un dato para poder usarlo y modificarlo.
3. Ejecutar codigo no basta: hay que mirar si el resultado tiene sentido.
4. Un notebook mezcla explicacion, codigo y resultados; por eso lo usaremos para
   aprender, experimentar y documentar.

No adelantes NumPy, modelos ni LLM en este bloque. Mencionalos solo como destino
del recorrido, no como contenidos que deban comprender hoy.

### Mini-reto

Escribe primero el enunciado en la pizarra:

```text
Convierte una cantidad en euros a dolares.
Usa una variable para el importe y otra para el tipo de cambio.
Muestra un mensaje que permita comprobar el resultado.
```

Si alguien termina, pide una ampliacion, no otro ejercicio distinto: convertir
varios importes, redondear el resultado o explicar en una celda de texto que
ocurriria si cambia el tipo de cambio.

## Cierre y continuidad

Pide un ticket de salida, en Moodle o en papel:

```text
Una cosa que ya manejo:
Una cosa que necesito repasar:
Una incidencia de acceso, si la tengo:
```

Tarea no evaluable para la siguiente sesion:

- Completar el diagnostico tecnico si no se realizo en clase.
- Ejecutar o revisar el notebook inicial y modificar al menos dos valores.
- Registrar una incidencia con el equipo, sistema operativo, comando y mensaje
  de error completo; no instalar paquetes al azar para resolverla.

## Criterio de salida de la sesion

- El alumnado sabe donde estan Moodle, el portal y el repositorio.
- Todo el grupo conoce las reglas de entregas y uso de IA.
- Cada estudiante ha abierto o ejecutado el primer notebook y realizado una
  modificacion sencilla.
- Las incidencias de acceso quedan registradas; no se califican actividades en
  esta primera sesion.
