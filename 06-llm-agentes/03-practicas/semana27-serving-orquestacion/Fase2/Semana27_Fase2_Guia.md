# Semana 27 – Fase 2: Desarrollo avanzado  
*(Gradio, LangChain, DSPy + MCP y herramientas adicionales)*

---

## 🎯 Objetivos
- Aplicar herramientas emergentes en escenarios más realistas.  
- Desplegar un modelo propio con **Gradio**.  
- Usar pipelines más complejos en **LangChain**.  
- Optimizar prompts y usar **contexto externo** con **DSPy + MCP**.  
- Relacionar herramientas adicionales como **LlamaIndex**, **LangGraph**, **Ollama**, **Ragas** y **MLflow** con patrones prácticos de IA.  

---

## 📚 Contenidos
1. **Gradio (avanzado)**: interfaz para un modelo de imágenes entrenado en Keras/TensorFlow.  
2. **LangChain (avanzado)**: pipeline con memoria y consulta a una API (Wikipedia u otra).  
3. **DSPy + MCP**: mejora de prompts y uso de base de datos SQLite como fuente de contexto.  
4. **Herramientas adicionales**: RAG, bases vectoriales, grafos, salidas estructuradas, modelos locales, evaluación y tracking.  
5. **MLflow + LlamaIndex**: registro de experimentos y RAG sobre documentos propios con Chroma/FAISS como pieza interna.  
6. **Extras de stack completo**: LangGraph, Ollama y FastAPI.  

---

## 📂 Notebooks trabajados
- `96_gradio_model.ipynb`  
- `97_langchain_pipeline.ipynb`  
- `98_dspy_mcp.ipynb`  
- `99_herramientas_ia_integradas.ipynb`  
- `100_mlflow_llamaindex_rag.ipynb`  
- `101_langgraph_orquestacion.ipynb`  
- `102_ollama_modelos_locales.ipynb`  
- `103_fastapi_serving_modelos.ipynb`  

Versiones de los notebooks 96-98: base, soluciones, soluciones + autotests. Los notebooks 99-103 son ejemplos integradores o extras únicos.  

Documentación relacionada:

- `Documentacion/LangGraph_Documentacion.md`
- `Documentacion/Ollama_Documentacion.md`
- `Documentacion/FastAPI_Documentacion.md`

---

## 🛠️ Actividades
1. Cargar pesos entrenados en el modelo de imágenes y probar la interfaz.  
2. Sustituir Wikipedia por otra API pública en el pipeline de LangChain.  
3. Añadir un ranker TF-IDF en el retriever de MCP.  
4. Validar que la respuesta de un modelo incluye información del contexto recuperado.  
5. Ejecutar el notebook integrador y completar el reto de comparar dos ejecuciones como si fueran runs de MLflow.  
6. Registrar comparativas de modelos y configuraciones RAG en el notebook MLflow + LlamaIndex.  
7. Probar los notebooks extra de LangGraph, Ollama y FastAPI para completar el stack.  

---

## ✅ Evaluación
- **RA2.d**: implementación de ejemplos prácticos avanzados.  
- **RA2.e**: análisis del valor añadido de estas herramientas.  
- **RA3.b/c/d**: evaluación de la convergencia tecnológica.  
- **Criterios:** funcionamiento de demos, integración de APIs/contexto, reflexión sobre aplicaciones prácticas.  
