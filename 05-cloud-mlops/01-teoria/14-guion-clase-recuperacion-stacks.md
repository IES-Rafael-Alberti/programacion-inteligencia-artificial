# Guion de clase: recuperación avanzada y stacks típicos de IA

## Propósito

Este guion está pensado para el tramo final del curso, cuando el alumnado ya está centrado en su proyecto final y no conviene abrir demasiados frentes técnicos nuevos. El objetivo no es que implementen todas las herramientas, sino que entiendan qué opciones existen, vean ejemplos realistas y puedan decidir si alguna encaja en su proyecto.

## Objetivos de la sesión

Al terminar, el alumnado debería ser capaz de:

- Diferenciar entre RAG clásico y enfoques de recuperación más avanzados.
- Entender cuándo el `chunking` puede ser suficiente y cuándo empieza a fallar.
- Identificar al menos un stack razonable para un proyecto final.
- Justificar por qué una herramienta o combinación de herramientas sí o no compensa.

---

## Opción A: una sola sesión

### Duración orientativa

- 60 a 90 minutos

### Estructura propuesta

#### 1. Contexto inicial

Duración orientativa: 10-15 minutos

Qué explicar:

- No todas las aplicaciones de IA usan el mismo stack.
- RAG no es solo “trocear documentos y meterlos en una base vectorial”.
- En el proyecto final interesa elegir bien y no añadir complejidad innecesaria.

Material de apoyo:

- [12-recuperacion-avanzada-rag.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/12-recuperacion-avanzada-rag.md)
- [13-ejemplos-stacks-ia.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Documentacion/13-ejemplos-stacks-ia.md)
- [18-demo-pageindex-rag.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.md)

#### 2. Explicación de recuperación avanzada

Duración orientativa: 20-25 minutos

Qué explicar:

- Flujo del RAG clásico.
- Problemas del `chunking`.
- Búsqueda híbrida.
- `Reranking`.
- Recuperación jerárquica.
- Caso de `PageIndex` como alternativa para documentos largos.

Qué insistir:

- No se trata de sustituir siempre el RAG clásico.
- Se trata de saber cuándo el enfoque básico deja de ser suficiente.

#### 3. Demo breve

Duración orientativa: 15-20 minutos

Demo recomendada:

- Mostrar un flujo simple de documentos -> fragmentación -> embeddings -> recuperación -> respuesta.
- Compararlo con la demo de `PageIndex` sin `chunking` manual.
- Enseñar que ambos enfoques responden a necesidades distintas.

No hace falta implementar todo en directo. Basta con enseñar:

- Un ejemplo de RAG sencillo.
- Un ejemplo de recuperación estructurada con `PageIndex`.
- Qué tipo de preguntas fallan más con troceado simple.

#### 4. Ejemplos de stacks típicos

Duración orientativa: 15-20 minutos

Qué enseñar:

- `Stack 1`: RAG sencillo para documentación.
- `Stack 2`: RAG documental robusto.
- `Stack 3`: ML clásico tabular.
- `Stack 4`: modelo abierto servido localmente.

Qué remarcar:

- No todos los grupos necesitan observabilidad, serving propio, feature store o MLOps completo.
- Un buen stack de aula suele ser más pequeño de lo que parece en los diagramas.

#### 5. Cierre y conexión con proyectos

Duración orientativa: 10 minutos

Pregunta de cierre para los grupos:

1. ¿Nuestro proyecto necesita recuperación?
2. ¿Con documentos simples basta un RAG clásico?
3. ¿Nos compensa usar modelo abierto o API?
4. ¿Qué herramienta añadiría valor real y cuál sería solo complejidad?

---

## Opción B: dos sesiones cortas

## Sesión 1: recuperación avanzada para RAG

### Objetivo

Dar contexto sobre alternativas al `chunking` clásico y presentar `PageIndex` como ejemplo de recuperación estructurada.

### Estructura

1. Recordatorio de RAG clásico.
2. Problemas típicos del troceado simple.
3. Búsqueda híbrida, `reranking` y recuperación jerárquica.
4. `PageIndex` como ejemplo.
5. Mini debate aplicado a los proyectos del aula.

### Actividad rápida

Cada grupo responde en 5-10 minutos:

- Tipo de documentos que usa.
- Si necesita citas o trazabilidad.
- Si el `chunking` simple le bastaría.
- Si le interesaría investigar una alternativa.

## Sesión 2: stacks típicos para proyectos finales

### Objetivo

Ayudar al alumnado a aterrizar herramientas en combinaciones realistas.

### Estructura

1. Presentación de 4 o 5 stacks típicos.
2. Comparación entre stack mínimo y stack más ambicioso.
3. Relación con proyectos del grupo.
4. Elección argumentada de un stack provisional.

### Actividad rápida

Cada grupo redacta un mini esquema:

```text
Datos -> herramienta de preparación -> modelo o LLM -> recuperación si aplica -> despliegue o uso final
```

Y añade una breve justificación:

- qué han elegido,
- qué han descartado,
- y por qué.

---

## Demo recomendable para clase

## Demo 1: RAG sencillo y asumible

Herramientas:

- `pandas` o `Polars`
- `Chroma` o `Qdrant`
- `LlamaIndex`
- `OpenAI` o `Anthropic`

Qué mostrar:

1. Carga de un conjunto pequeño de documentos.
2. Fragmentación e indexación.
3. Consulta simple.
4. Ejemplo de respuesta correcta y ejemplo de respuesta mejorable.

Qué aprender:

- Cómo se montan las piezas.
- Dónde aparecen los límites del chunking.

## Demo 2: comparación conceptual con recuperación estructurada

Herramientas:

- Documento largo o PDF técnico
- Esquema de RAG clásico
- Demo o notebook de `PageIndex`

Qué mostrar:

1. Pregunta sobre una sección concreta.
2. Cómo el troceado puede repartir el contexto.
3. Cómo un índice jerárquico intenta conservar la estructura.
4. Cómo una respuesta puede venir acompañada de páginas o secciones relevantes.

Material de apoyo:

- [18-demo-pageindex-rag.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.md)
- [18-demo-pageindex-rag.ipynb.md](/datos/RafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD5/Demos/18-demo-pageindex-rag.ipynb.md)

No hace falta montar un sistema completo en directo si no compensa en tiempo. También puede usarse el notebook explicativo como apoyo visual.

---

## Qué no conviene hacer ahora

- No abrir demasiadas herramientas nuevas a la vez.
- No plantear implementaciones largas de observabilidad o serving si no están ligadas al proyecto.
- No exigir que todos los grupos usen RAG, agentes o modelos abiertos.
- No convertir estas sesiones en una lista enciclopédica de servicios.

---

## Actividad de investigación breve

Cada grupo puede investigar una sola mejora posible para su proyecto:

- búsqueda híbrida,
- `reranking`,
- `PageIndex`,
- modelo abierto servido localmente,
- evaluación de prompts,
- o base vectorial alternativa.

Entrega breve sugerida:

```text
Herramienta o enfoque investigado:
Qué problema resuelve:
Cómo encajaría en nuestro proyecto:
Qué ventaja tendría:
Qué coste o complejidad añade:
Decisión final: lo aplicaríamos / no lo aplicaríamos
```

---

## Recomendación didáctica final

Con el tiempo que queda, el enfoque más rentable es:

1. Dar mapa general.
2. Enseñar 1 demo sencilla.
3. Mostrar 2 o 3 stacks realistas.
4. Pedir una decisión argumentada aplicada a cada proyecto.

Eso permite cerrar la unidad con sentido práctico sin desviar demasiado al alumnado de su proyecto final.
