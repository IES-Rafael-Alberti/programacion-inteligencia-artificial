# Sesión compactada - Semana 27

Fecha: 2026-04-28

## Estado final

Tarea completada. La unidad queda revisada, ampliada, documentada y empaquetada.

Se trabajó sobre los notebooks de `Fase1` y `Fase2`, se añadieron explicaciones Markdown antes de las celdas de código, se creó documentación específica por herramienta y se regeneraron los paquetes `.zip`.

## Estructura actual

### Fase 1

- `Fase1/93_gradio_intro.ipynb`
- `Fase1/93_gradio_intro_SOLUCIONES.ipynb`
- `Fase1/93_gradio_intro_SOLUCIONES_TESTS.ipynb`
- `Fase1/94_langchain_intro.ipynb`
- `Fase1/94_langchain_intro_SOLUCIONES.ipynb`
- `Fase1/94_langchain_intro_SOLUCIONES_TESTS.ipynb`
- `Fase1/95_dspy_intro.ipynb`
- `Fase1/95_dspy_intro_SOLUCIONES.ipynb`
- `Fase1/95_dspy_intro_SOLUCIONES_TESTS.ipynb`
- `Fase1/Semana27_Fase1_Guia.md`

### Fase 2

- `Fase2/96_gradio_model.ipynb`
- `Fase2/96_gradio_model_SOLUCIONES.ipynb`
- `Fase2/96_gradio_model_SOLUCIONES_TESTS.ipynb`
- `Fase2/97_langchain_pipeline.ipynb`
- `Fase2/97_langchain_pipeline_SOLUCIONES.ipynb`
- `Fase2/97_langchain_pipeline_SOLUCIONES_TESTS.ipynb`
- `Fase2/98_dspy_mcp.ipynb`
- `Fase2/98_dspy_mcp_SOLUCIONES.ipynb`
- `Fase2/98_dspy_mcp_SOLUCIONES_TESTS.ipynb`
- `Fase2/99_herramientas_ia_integradas.ipynb`
- `Fase2/100_mlflow_llamaindex_rag.ipynb`
- `Fase2/101_langgraph_orquestacion.ipynb`
- `Fase2/102_ollama_modelos_locales.ipynb`
- `Fase2/103_fastapi_serving_modelos.ipynb`
- `Fase2/Semana27_Fase2_Guia.md`

### Documentación

Carpeta `Documentacion/`:

- `Documentacion_Notebooks.md`
- `Herramientas_IA_Programacion.md`
- `Gradio_Documentacion.md`
- `LangChain_Documentacion.md`
- `DSPy_Documentacion.md`
- `LlamaIndex_Documentacion.md`
- `MLflow_Documentacion.md`
- `FastAPI_Documentacion.md`
- `Ollama_Documentacion.md`
- `LangGraph_Documentacion.md`

Guía principal:

- `Semana27_Guia.md`

### Paquetes generados

- `Semana27_Fase1_Notebooks_Base.zip`
- `Semana27_Fase1_SOLUCIONES.zip`
- `Semana27_Fase1_SOLUCIONES_TESTS.zip`
- `Semana27_Fase2_Notebooks_Base.zip`
- `Semana27_Fase2_SOLUCIONES.zip`
- `Semana27_Fase2_SOLUCIONES_TESTS.zip`
- `Semana27_Guias.zip`

## Cambios principales realizados

### Notebooks 93-98

- Se ampliaron los notebooks base y de soluciones con una sección de `Ampliación progresiva`.
- Se añadieron ejemplos más completos de Gradio, LangChain y DSPy.
- Se añadieron explicaciones Markdown antes de celdas de código.
- Se mantuvieron los notebooks `_SOLUCIONES_TESTS` como pruebas ligeras, añadiendo explicaciones donde faltaban.

### Notebook 99

`Fase2/99_herramientas_ia_integradas.ipynb` integra ejemplos ligeros de:

- RAG estilo `LlamaIndex` y `Haystack`.
- Bases vectoriales tipo `Chroma`, `FAISS` y `Qdrant`.
- Flujo con estado inspirado en `LangGraph`.
- Salidas estructuradas tipo `PydanticAI` e `Instructor`.
- Abstracción de proveedor tipo `LiteLLM` y `Ollama`.
- Evaluación estilo `Ragas`.
- Registro estilo `MLflow`.

Incluye celda de preparación para Google Colab con instalación condicional de librerías opcionales.

### Notebook 100

`Fase2/100_mlflow_llamaindex_rag.ipynb` añade:

- Tracking estilo `MLflow`.
- Comparación de modelos sencillos.
- RAG mínimo tipo `LlamaIndex`.
- `Chroma` y `FAISS` como piezas internas de recuperación vectorial.
- Fallback JSON si MLflow no está disponible.

### Notebooks 101-103

- `101_langgraph_orquestacion.ipynb`: estado compartido, nodos, validación, rutas condicionales y reintentos inspirados en LangGraph.
- `102_ollama_modelos_locales.ipynb`: cliente local con fallback simulado, conversación con historial, RAG mínimo y registro de configuración.
- `103_fastapi_serving_modelos.ipynb`: lógica de predicción separada, esquemas Pydantic, endpoints FastAPI y prueba sin arrancar servidor.

## Decisiones docentes

- `MCP` no se amplió como documento independiente porque ya aparece en `98_dspy_mcp.ipynb` y puede haberse visto en el módulo de modelos de IA.
- `Chroma` y `FAISS` se tratan como piezas internas de RAG, no como herramientas principales independientes.
- `LangGraph`, `Ollama` y `FastAPI` se añadieron como extras para completar el stack.
- La documentación se mantuvo en español claro y se eliminaron restos de gallego, mezclas de idioma y cadenas corruptas.

## Validación realizada

Último repaso completado:

- Todos los notebooks son JSON válido.
- Todas las celdas Python tienen sintaxis correcta con `ast.parse`.
- Todas las celdas de código tienen explicación Markdown previa.
- Los notebooks nuevos 101, 102 y 103 se ejecutaron secuencialmente en modo seguro.
- Las guías contienen referencias cruzadas a los notebooks y documentos nuevos.
- La documentación de `Documentacion/` fue revisada en español.
- Todos los paquetes `.zip` pasan `zip -T`.

## Comandos de validación usados

Validación de notebooks:

```bash
python3 - <<'PY'
import ast, json
from pathlib import Path
for path in sorted(Path('.').glob('Fase*/*.ipynb')):
    data = json.loads(path.read_text(encoding='utf-8'))
    for cell in data.get('cells', []):
        if cell.get('cell_type') == 'code':
            ast.parse(''.join(cell.get('source', [])))
print('OK')
PY
```

Integridad de zips:

```bash
for z in *.zip; do zip -T "$z" || exit 1; done
```

## Próximos pasos posibles

1. Ejecutar notebooks completos manualmente en Jupyter/Colab para comprobar dependencias reales y comportamiento interactivo.
2. Añadir autotests específicos para los notebooks nuevos 99-103 si se quiere evaluarlos automáticamente.
3. Exportar documentación a HTML/PDF si se necesita entregarla en formato no Markdown.
4. Revisar si los `.zip` deben mantener rutas internas o estructura plana según cómo se entreguen al alumnado.
