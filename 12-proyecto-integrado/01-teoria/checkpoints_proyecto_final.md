# Checkpoints del Proyecto Final — PIA

## Resumen

El proyecto final no debe aparecer al final del curso como una entrega aislada. Debe avanzar por checkpoints breves, revisables y con evidencias concretas.

Cada checkpoint tiene tres objetivos:

1. Evitar proyectos inviables o demasiado simples.
2. Obligar a integrar lo aprendido en los mini-proyectos.
3. Detectar problemas antes de la entrega final.

## Vista rápida

| Checkpoint | Momento orientativo | Entrega | Decisión docente |
|---|---|---|---|
| CP0 | Inicio del proyecto | Idea inicial | Aceptar, ajustar o rechazar |
| CP1 | Tras tratamiento de datos | Fuentes de datos | Validar viabilidad de datos |
| CP2 | Tras integración | Dataset integrado | Confirmar integración real |
| CP3 | Tras ML básico | Baseline | Comprobar que hay componente IA/ML |
| CP4 | Tras MLOps | Trazabilidad | Revisar experimentos y reproducibilidad |
| CP5 | Tras APIs/interfaz | Producto mínimo | Verificar salida útil |
| CP6 | Tras observabilidad/IA responsable | Calidad y límites | Revisar evaluación, sesgos y riesgos |
| CP7 | Final | Defensa | Evaluación final |

El trabajo de UD7 sobre stack convergente puede aportar evidencias para CP4, CP5 o CP6 si el equipo lo adapta a su proyecto final de módulo. No sustituye CP1 ni CP2: siguen siendo obligatorias al menos dos fuentes de datos diferenciadas y una integración real.

## CP0 — Idea inicial

### Entrega

Documento breve de 1 página o formulario con:

- título provisional;
- problema que se quiere resolver;
- usuarios o destinatarios;
- utilidad esperada;
- primeras fuentes de datos posibles;
- posible salida final: API, dashboard, informe, asistente, recomendador, ranking, alerta, etc.

### Criterios de aceptación

- [ ] El problema es comprensible.
- [ ] Tiene relación con datos e IA/ML.
- [ ] No depende de datos imposibles de conseguir.
- [ ] La dificultad parece adecuada para el módulo.
- [ ] Puede evolucionar durante el curso.

### Motivos para devolver la propuesta

- Tema demasiado amplio: “hacer una IA de fútbol”.
- Tema demasiado pobre: “analizar un CSV y hacer gráficas”.
- No hay datos identificados.
- No se ve componente IA/ML.
- La salida final no tiene usuario ni utilidad clara.

## CP1 — Fuentes de datos

### Entrega

Ficha de datos con al menos dos fuentes:

| Campo | Fuente 1 | Fuente 2 |
|---|---|---|
| Nombre | | |
| Origen | API / CSV / scraping / BD / logs / documentos | |
| Formato | | |
| Licencia o permisos | | |
| Variables principales | | |
| Frecuencia de actualización | | |
| Problemas esperados | | |

### Criterios de aceptación

- [ ] Hay al menos dos fuentes diferenciadas.
- [ ] Las fuentes son accesibles legal y técnicamente.
- [ ] No son duplicados artificiales del mismo dataset.
- [ ] Se puede explicar qué aporta cada fuente.

## CP2 — Integración de datos

### Entrega

Notebook o script que genere un dataset integrado inicial.

Debe incluir:

- carga de las fuentes;
- limpieza mínima;
- unión o relación entre fuentes;
- explicación de claves de unión o estrategia de integración;
- primeras métricas de calidad: nulos, duplicados, tamaños, rangos.

### Criterios de aceptación

- [ ] La integración aporta información nueva.
- [ ] Está justificada la relación entre fuentes.
- [ ] Hay limpieza o curación documentada.
- [ ] El proceso puede repetirse.

### No válido

- Concatenar dos CSV sin explicar relación.
- Usar dos hojas del mismo Excel como “dos fuentes”.
- Hacer limpieza manual sin dejar script.

## CP3 — Baseline IA/ML

### Entrega

Primer modelo, análisis inteligente o sistema IA mínimo.

Puede ser:

- modelo de clasificación;
- regresión;
- clustering;
- ranking/recomendación;
- predicción temporal;
- RAG o asistente con datos propios;
- sistema de reglas + ML si está justificado.

### Criterios de aceptación

- [ ] Hay una métrica o criterio de evaluación.
- [ ] Existe una versión simple de referencia.
- [ ] El equipo puede explicar por qué ese enfoque tiene sentido.
- [ ] Se identifican errores o limitaciones iniciales.

## CP4 — Trazabilidad y reproducibilidad

### Entrega

Evidencia de experimentos y ejecución reproducible.

Opciones válidas:

- MLflow con varios runs;
- tabla técnica de experimentos si MLflow no aplica;
- pipeline con Prefect;
- scripts reproducibles con instrucciones claras.

### Criterios de aceptación

- [ ] Se pueden comparar varios experimentos.
- [ ] Queda claro qué datos y parámetros se usaron.
- [ ] El proceso no depende de ejecutar celdas sueltas al azar.
- [ ] Hay instrucciones para repetir el resultado.

## CP5 — Producto mínimo útil

### Entrega

Primera salida usable del proyecto:

- API con FastAPI;
- dashboard;
- informe automatizado;
- recomendador;
- ranking;
- asistente;
- alerta;
- interfaz sencilla.

### Criterios de aceptación

- [ ] La salida responde al problema inicial.
- [ ] Tiene usuario o destinatario claro.
- [ ] Usa el componente IA/ML del proyecto.
- [ ] Puede demostrarse en clase.

## CP6 — Calidad, límites e IA responsable

### Entrega

Breve análisis de calidad:

- errores frecuentes;
- sesgos o limitaciones;
- explicabilidad si procede;
- deriva o monitorización si procede;
- riesgos de uso;
- mejoras futuras.

### Criterios de aceptación

- [ ] El equipo reconoce limitaciones reales.
- [ ] Hay alguna evidencia: métricas, ejemplos de error, SHAP/LIME, drift, revisión manual, etc.
- [ ] Se proponen mejoras concretas.

## CP7 — Defensa final

### Entrega

- repositorio o ZIP;
- README;
- informe técnico;
- presentación;
- demo o evidencias de ejecución.

### Estructura recomendada de defensa

1. Problema y utilidad.
2. Fuentes de datos e integración.
3. Modelo o sistema IA.
4. Resultado final.
5. Decisiones técnicas.
6. Limitaciones.
7. Demo.

## Seguimiento docente

| Situación | Acción recomendada |
|---|---|
| Proyecto demasiado simple | Pedir segunda fuente, integración real o salida útil |
| Proyecto demasiado ambicioso | Recortar a versión mínima viable |
| Grupo bloqueado con datos | Ofrecer familia de proyecto alternativa |
| Mucho código copiado | Exigir explicación oral y adaptación documentada |
| Sin componente IA/ML claro | Replantear objetivo antes de avanzar |
| Sin avance entre checkpoints | Reducir alcance y fijar entrega mínima obligatoria |

## Regla de cierre

Un proyecto no debería llegar a la defensa final si no ha superado al menos:

- CP1 — fuentes de datos;
- CP2 — integración;
- CP3 — baseline IA/ML;
- CP5 — producto mínimo útil.

Si falta alguno de esos hitos, el proyecto necesita una revisión urgente antes de la entrega final.
