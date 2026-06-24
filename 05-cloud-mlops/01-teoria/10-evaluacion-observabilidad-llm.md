# Evaluación y observabilidad de aplicaciones con LLM

## Introducción

Cuando una aplicación usa modelos de lenguaje no basta con que "parezca funcionar". Hay que evaluar la calidad de las respuestas, detectar fallos y observar qué está ocurriendo en producción.

## Qué problema resuelve esta categoría

- Medir si las respuestas son útiles, correctas y relevantes.
- Comparar prompts, modelos o configuraciones.
- Detectar errores en sistemas RAG.
- Analizar costes, latencia y trazas de ejecución.

---

## Diferencia entre evaluación y observabilidad

### Evaluación

Comprueba la calidad del sistema con métricas, casos de prueba o conjuntos de ejemplos.

### Observabilidad

Permite inspeccionar trazas, tiempos, llamadas, errores y comportamiento real en ejecución.

Ambas son complementarias.

---

## Alternativas habituales

### LangSmith

- Muy integrado con LangChain.
- Útil para trazas, depuración y evaluación de cadenas o agentes.

### Ragas

- Open source.
- Muy usado para evaluar sistemas RAG con métricas específicas.

### Promptfoo

- Open source.
- Permite comparar prompts, modelos y salidas de forma sistemática.

### Arize Phoenix

- Open source.
- Útil para observabilidad y análisis de aplicaciones de IA.

### Helicone

- Observabilidad centrada en aplicaciones con llamadas a LLM.
- Interesante para costes, latencia y seguimiento de uso.

### DeepEval

- Open source.
- Orientado a pruebas y evaluación automatizada de sistemas con LLM.

---

## Comparativa rápida

| Herramienta | Tipo | Mejor encaje | Limitación |
|-------------|------|--------------|------------|
| LangSmith | SaaS | Proyectos con LangChain | Muy ligado a ese ecosistema |
| Ragas | Open source | Evaluación de RAG | Más centrado en retrieval |
| Promptfoo | Open source | Comparación de prompts | Menos orientado a trazas |
| Arize Phoenix | Open source | Observabilidad y análisis | Requiere algo más de montaje |
| Helicone | Mixto | Seguimiento de llamadas y costes | Menos centrado en calidad semántica |
| DeepEval | Open source | Tests automatizados | Requiere diseñar bien los casos |

---

## Qué se puede evaluar

- Corrección factual.
- Relevancia de la respuesta.
- Fidelidad al contexto recuperado.
- Calidad de la recuperación en RAG.
- Coste por llamada.
- Latencia.
- Tasa de error.

---

## Aplicación al proyecto

Esta categoría cobra sentido si el proyecto:

1. Usa LLM como parte importante del flujo.
2. Implementa RAG.
3. Necesita comparar prompts o proveedores.
4. Quiere justificar calidad y no solo mostrar una demo.

En proyectos académicos, aunque no se monte observabilidad completa, sí conviene introducir al menos una forma de evaluación básica.

---

## Recomendaciones generales

| Caso | Recomendación |
|------|---------------|
| Proyecto docente con prompts | Promptfoo |
| Proyecto RAG | Ragas |
| Proyecto con LangChain | LangSmith |
| Observabilidad open source | Arize Phoenix |
| Control de uso y costes | Helicone |

---

## Ejemplo mínimo de evaluación

```python
casos = [
    {"pregunta": "¿Qué es un embedding?", "respuesta_esperada": "representación vectorial"},
    {"pregunta": "¿Qué es RAG?", "respuesta_esperada": "recuperación y generación"}
]

for caso in casos:
    respuesta = sistema_responde(caso["pregunta"])
    print(caso["pregunta"], respuesta)
```

La idea no es solo ejecutar ejemplos, sino definir criterios para juzgar si la respuesta es aceptable.

---

## Fuentes recomendadas

- Documentación oficial de LangSmith.
- Documentación oficial de Ragas.
- Documentación oficial de Promptfoo.
- Documentación oficial de Arize Phoenix.
- Documentación oficial de Helicone.
- Documentación oficial de DeepEval.
