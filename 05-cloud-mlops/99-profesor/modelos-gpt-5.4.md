# Modelos GPT-5.4: diferencias y recomendación de uso

## Diferencias generales

En general, las variantes suelen diferenciarse en 4 ejes:

1. Calidad
- `gpt-5.4`: versión más capaz y consistente.
- `mini`: menos capacidad, pero más barato y rápido.
- `fast`: prioriza latencia.
- `fast mini`: prioriza aún más velocidad/coste, con más recorte en calidad.

2. Velocidad
- `fast` responde antes que la variante base.
- `mini` normalmente también es ágil.
- `fast mini` suele ser la más rápida.

3. Coste
- Base > `fast`/`mini` > `fast mini` en capacidad.
- Normalmente `mini` y `fast mini` son las opciones más económicas.

4. Casos de uso
- `gpt-5.4`: tareas complejas, razonamiento, código delicado, análisis largos.
- `gpt-5.4-fast`: chat interactivo, agentes, tareas donde importa mucho la latencia.
- `gpt-5.4-mini`: clasificación, extracción, resúmenes, automatizaciones baratas.
- `gpt-5.4-fast-mini`: alto volumen y respuestas simples en tiempo real.

## Tabla comparativa breve

| Modelo | Calidad | Velocidad | Coste | Mejor para |
|---|---|---|---|---|
| `gpt-5.4` | Muy alta | Media | Alto | Código complejo, análisis, tareas delicadas |
| `gpt-5.4-fast` | Alta | Alta | Medio-alto | Chat fluido, copilots, agentes interactivos |
| `gpt-5.4-mini` | Media | Alta | Bajo | Clasificación, extracción, resúmenes, pipelines |
| `gpt-5.4-fast-mini` | Baja-media | Muy alta | Muy bajo | Alto volumen, respuestas cortas, tiempo real |

## Recomendación rápida

- Programación seria: `gpt-5.4`
- Asistente de desarrollo rápido: `gpt-5.4-fast`
- Automatizaciones baratas: `gpt-5.4-mini`
- Bots simples a gran escala: `gpt-5.4-fast-mini`

## Ejemplos

- Revisar arquitectura o depurar algo difícil: `gpt-5.4`
- Autocompletado/chat en IDE: `gpt-5.4-fast`
- Etiquetar tickets o resumir documentos: `gpt-5.4-mini`
- FAQ, routing, respuestas muy cortas: `gpt-5.4-fast-mini`

## Regla simple

- Si dudas, empieza con `fast`.
- Si falla por calidad, sube a base.
- Si sobra calidad y quieres ahorrar, baja a `mini`.

## Recomendación según tu uso

Como lo usas en chat, pero también en VS Code, OpenCode y Codex CLI, la recomendación práctica sería esta:

| Uso | Modelo recomendado | Motivo |
|---|---|---|
| Chat general | `gpt-5.4-fast` | Buen equilibrio entre rapidez y calidad |
| VS Code | `gpt-5.4` o `gpt-5.4-fast` | `gpt-5.4` para cambios delicados; `fast` para iterar rápido |
| OpenCode | `gpt-5.4` | Suele compensar más calidad al leer, editar y razonar sobre código real |
| Codex CLI | `gpt-5.4-fast` o `gpt-5.4` | `fast` para flujo ágil; base para tareas complejas o refactors |

## Recomendación concreta

- Modelo por defecto: `gpt-5.4-fast`
- Sube a `gpt-5.4` cuando:
  - haya refactors grandes
  - estés depurando un bug raro
  - el modelo tenga que entender varias piezas del proyecto
  - quieras más fiabilidad en cambios de código
- Baja a `mini` solo cuando:
  - quieras ahorrar coste
  - hagas tareas repetitivas
  - el trabajo sea simple: resúmenes, renombres pequeños, generación mecánica

## Configuración práctica por herramienta

1. VS Code
- Por defecto: `gpt-5.4-fast`
- Para refactors, debugging serio o cambios multiarchivo: `gpt-5.4`

2. OpenCode
- Por defecto: `gpt-5.4`
- Si solo estás iterando rápido o haciendo consultas ligeras: `gpt-5.4-fast`

3. Codex CLI
- Por defecto: `gpt-5.4-fast`
- Para tareas complejas en repos grandes: `gpt-5.4`

4. Chat general
- Por defecto: `gpt-5.4-fast`

5. Opción ahorro
- Usa `gpt-5.4-mini` para:
  - resumir
  - reescribir texto
  - generar borradores
  - tareas mecánicas simples

## Configuración resumida

- `fast` como modelo diario
- `base` para trabajo serio de código
- `mini` para abaratar tareas simples

## Perfil recomendado

- Si solo quieres una elección única: `gpt-5.4-fast`
- Si aceptas cambiar según la tarea:
  - conversación y flujo rápido: `fast`
  - codigo importante: `gpt-5.4`

## Qué usar por defecto

| Contexto | Modelo por defecto |
|---|---|
| Chat diario | `gpt-5.4-fast` |
| VS Code | `gpt-5.4-fast` |
| OpenCode | `gpt-5.4` |
| Codex CLI | `gpt-5.4-fast` |
| Tareas simples y baratas | `gpt-5.4-mini` |

## Resumen final

- Si quieres elegir solo uno: `gpt-5.4-fast`.
- Si el modelo va a tocar código importante o resolver algo complejo: `gpt-5.4`.
- Si buscas ahorrar en tareas simples: `gpt-5.4-mini`.
