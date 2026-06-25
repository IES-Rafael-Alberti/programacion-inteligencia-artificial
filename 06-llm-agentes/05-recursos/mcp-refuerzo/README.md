# Refuerzo MCP: asistente con herramientas externas

Este recurso es un refuerzo opcional para recordar cómo una aplicación de IA puede combinar modelo, herramientas externas, contexto e interfaz. No es una unidad obligatoria: se usa solo si el test inicial muestra que el grupo necesita repasar MCP antes de avanzar con agentes.

## Cuándo usarlo

1. Pasar `00-test-inicial-mcp.md` al inicio.
2. Si el grupo responde bien, hacer solo un recordatorio breve.
3. Si aparecen dudas, trabajar este paquete como sesión guiada.

## Materiales

| Archivo | Uso |
|---------|-----|
| `00-test-inicial-mcp.md` | Diagnóstico para decidir si se imparte el refuerzo. |
| `asistente_mcp.py` | Ejemplo de asistente con interfaz Gradio, recuperación de contexto y herramientas externas. |
| `requirements.txt` | Dependencias necesarias para ejecutar el ejemplo. |
| `README.md` | Esta guía de uso. |

## Requisitos

Instala dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el asistente:

```bash
python asistente_mcp.py
```

## ¿Qué hace?

- Usa Wikipedia o una API REST para obtener contexto.
- Usa un modelo Hugging Face para responder.
- Guarda preguntas y respuestas en SQLite.
- Muestra historial en la interfaz.

## Lectura didáctica

En este ejemplo, MCP se trabaja como patrón de separación de responsabilidades:

| Parte | Papel en el ejemplo |
|-------|---------------------|
| Interfaz | Gradio recoge la pregunta y muestra respuesta/historial. |
| Contexto | Wikipedia aporta información externa cuando hace falta. |
| Herramienta externa | La consulta de clima simula una API REST usada por el asistente. |
| Modelo | El pipeline de Hugging Face genera la respuesta final. |
| Memoria local | SQLite guarda las interacciones para revisar el historial. |

## Guía rápida para el docente

- No dedicar una sesión completa si el alumnado ya entiende el patrón.
- Usarlo como práctica corta si confunden modelo, herramienta, contexto e interfaz.
- Insistir en validación y seguridad: un agente con herramientas externas no debe ejecutar acciones sin límites ni comprobaciones.
- Cerrar la actividad pidiendo al alumnado que identifique qué partes del script podrían sustituirse por un servidor MCP real.
