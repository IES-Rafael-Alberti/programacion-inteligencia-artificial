# Serving e inferencia de modelos abiertos

## Introducción

No todos los proyectos de IA consumen modelos mediante APIs cerradas. En muchos casos interesa desplegar modelos abiertos para controlar costes, privacidad, personalización o dependencia de proveedor.

## Qué problema resuelve esta categoría

- Servir modelos open weight mediante API propia.
- Ejecutar inferencia local o en infraestructura propia.
- Reducir dependencia de APIs comerciales.
- Aprovechar GPUs propias o alquiladas.

---

## Conceptos básicos

### Serving

Proceso de exponer un modelo para que otras aplicaciones puedan consultarlo mediante API o endpoint.

### Inferencia

Ejecución del modelo sobre entradas reales para producir una salida.

### Batch frente a tiempo real

- Batch: procesamiento de muchos registros en lote.
- Tiempo real: respuesta a petición con baja latencia.

---

## Alternativas habituales

### Ollama

- Muy sencillo para ejecutar modelos abiertos en local.
- Muy útil en docencia, prototipos y pruebas rápidas.

### vLLM

- Open source.
- Muy popular para serving eficiente de modelos de lenguaje.
- Buena opción para GPU y despliegues más serios.

### Text Generation Inference

- Open source de Hugging Face.
- Orientado a servir modelos generativos con buen rendimiento.

### BentoML

- Open source.
- Permite empaquetar y desplegar servicios de inferencia.
- Útil más allá de LLM, también para modelos clásicos o de deep learning.

### Ray Serve

- Open source.
- Muy potente si ya se trabaja con Ray o con despliegues distribuidos.

### TorchServe y Triton

- Opciones habituales para serving de modelos de deep learning.
- Más comunes en escenarios de producción.

---

## Comparativa rápida

| Herramienta | Tipo | Mejor encaje | Limitación |
|-------------|------|--------------|------------|
| Ollama | Open source | Local, docencia y prototipos | Menos orientado a gran escala |
| vLLM | Open source | Serving eficiente de LLM | Requiere infraestructura |
| TGI | Open source | Modelos generativos de Hugging Face | Más técnico que Ollama |
| BentoML | Open source | APIs de inferencia variadas | Requiere diseño del servicio |
| Ray Serve | Open source | Despliegues distribuidos | Curva mayor |
| Triton | Open source | Producción con alto rendimiento | Más complejo |

---

## Cuándo tiene sentido usar modelos abiertos

1. Cuando importa el control sobre los datos.
2. Cuando el coste por llamada a API sería demasiado alto.
3. Cuando se necesita personalización o ajuste fino.
4. Cuando el proyecto quiere estudiar serving y despliegue, no solo consumo de API.

Si el objetivo es solo prototipar rápido, una API cerrada suele ser más sencilla.

---

## Aplicación al proyecto

Esta categoría es especialmente relevante si el proyecto:

- Usa modelos de lenguaje o embeddings de forma intensiva.
- Necesita privacidad o control de despliegue.
- Quiere comparar API cerrada frente a modelo abierto.
- Dispone de GPU o entorno cloud para servir modelos.

En proyectos de aula, `Ollama` y `vLLM` son dos referencias muy útiles porque muestran bien dos niveles distintos de complejidad.

---

## Recomendaciones generales

| Caso | Recomendación |
|------|---------------|
| Primer contacto con modelos abiertos | Ollama |
| Serving eficiente de LLM | vLLM |
| Ecosistema Hugging Face | TGI |
| API propia para modelos diversos | BentoML |
| Despliegue distribuido | Ray Serve |

---

## Ejemplo mínimo con Ollama

```bash
ollama run llama3.1
```

## Ejemplo mínimo conceptual con vLLM

```bash
python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.2
```

---

## Fuentes recomendadas

- Documentación oficial de Ollama.
- Documentación oficial de vLLM.
- Documentación oficial de Text Generation Inference.
- Documentación oficial de BentoML.
- Documentación oficial de Ray Serve.
- Documentación oficial de NVIDIA Triton Inference Server.
