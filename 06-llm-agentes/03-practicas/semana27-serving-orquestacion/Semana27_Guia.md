# Semana 27 – Lenguajes y herramientas emergentes para IA  
*(LangChain, DSPy, MCP, Gradio)*

---

## 🎯 Objetivos
- Explorar herramientas emergentes que facilitan la creación de interfaces y pipelines de IA.  
- Conocer **Gradio** como herramienta de prototipado rápido de interfaces web.  
- Entender los conceptos de **LangChain** y **DSPy** para estructuración y optimización de prompts.  
- Introducir **MCP (Model Context Protocol)** como estándar para conectar modelos y aplicaciones.  
- Aplicar estas tecnologías tanto en prácticas como en el **proyecto final** del módulo.  

---

## 🪜 Fase 1 – Introducción práctica (semana en curso)
### ✔️ Propósito
Familiarizarse con las herramientas de manera **sencilla y progresiva**, usando modelos ligeros ya vistos (ej. scikit-learn).

### 📚 Contenidos
1. **Gradio (intro)**: crear interfaz para clasificador de Iris.  
2. **LangChain (intro)**: ejemplo simulado de cadena de pasos.  
3. **DSPy (intro)**: simulación de optimización de prompts.  

### 📂 Notebooks trabajados
- **93_gradio_intro.ipynb**  
- **94_langchain_intro.ipynb**  
- **95_dspy_intro.ipynb**  

Versiones: base, soluciones, soluciones + autotests.  

### 🛠️ Actividades
- Ejecutar y modificar la demo de Gradio (añadir modelo alternativo).  
- Crear un *chain* de pasos textuales en LangChain simulado.  
- Optimizar un *prompt* aplicando transformaciones en DSPy.  

---

## 🪜 Fase 2 – Desarrollo avanzado (planificada para más adelante)
### ✔️ Propósito
Usar estas herramientas en un **contexto más realista**, integrándolas con modelos neuronales entrenados en clase.

### 📚 Contenidos
1. **Gradio (avanzado)**: interfaz para un modelo de clasificación de imágenes entrenado por los alumnos; despliegue local/remoto (ej. Hugging Face Spaces).  
2. **LangChain (avanzado)**: creación de pipelines con memoria y conexión a APIs externas.  
3. **DSPy (avanzado)**: optimización automática de prompts en pipelines de Q&A.  
4. **MCP (intro)**: exponer una base de datos SQLite como fuente de contexto para un modelo.  
5. **Herramientas adicionales**: visión integradora de RAG, grafos, salidas estructuradas, modelos locales, evaluación y tracking.  
6. **MLflow + LlamaIndex**: tracking de experimentos y RAG sobre documentos propios con Chroma/FAISS como pieza interna.  
7. **Extras de stack completo**: orquestación con LangGraph, modelos locales con Ollama y APIs de producción con FastAPI.  

### 📂 Notebooks previstos
- **96_gradio_model.ipynb**  
- **97_langchain_pipeline.ipynb**  
- **98_dspy_mcp.ipynb**  
- **99_herramientas_ia_integradas.ipynb**  
- **100_mlflow_llamaindex_rag.ipynb**  
- **101_langgraph_orquestacion.ipynb**  
- **102_ollama_modelos_locales.ipynb**  
- **103_fastapi_serving_modelos.ipynb**  

---

## ✅ Evaluación (RA2 y RA3)
- **RA2.b**: Identificación y caracterización de nuevas librerías de IA.  
- **RA2.d**: Implementación de aplicaciones interactivas con Gradio y LangChain.  
- **RA2.e**: Evaluación del valor añadido de estas herramientas en el modelado.  
- **RA3.b/c/d**: Conexión tecnológica y evaluación de aportes a la convergencia.  

**Criterios de evaluación:**  
- Correcta creación de interfaces con Gradio.  
- Funcionamiento básico de cadenas en LangChain/DSPy.  
- Reflexión sobre el papel de MCP y herramientas emergentes.  
- Participación activa en la modificación y ejecución de ejemplos.  

---

## 📌 Recursos recomendados
- [Documentación de Gradio](https://www.gradio.app/)  
- [LangChain Python](https://python.langchain.com/)  
- [DSPy](https://dspy-docs.vercel.app/)  
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

## 📄 Documentación añadida
- `Documentacion_Notebooks.md`: ruta de uso, progresión de ejemplos y evidencias evaluables.  
- `Gradio_Documentacion.md`: documentación práctica de Gradio como herramienta de interfaces y demos de IA.  
- `LangChain_Documentacion.md`: documentación práctica de LangChain como herramienta de cadenas, RAG, memoria y herramientas.  
- `DSPy_Documentacion.md`: documentación práctica de DSPy como enfoque de prompts evaluables y optimización programática.  
- `MLflow_Documentacion.md`: documentación práctica de MLflow para tracking de experimentos en modelos clásicos, deep learning y RAG.  
- `LlamaIndex_Documentacion.md`: documentación práctica de LlamaIndex para RAG con documentos propios y bases vectoriales como Chroma/FAISS.  
- `LangGraph_Documentacion.md`: documentación práctica de LangGraph para flujos con estado, decisiones y reintentos.  
- `Ollama_Documentacion.md`: documentación práctica de Ollama para modelos de lenguaje locales.  
- `FastAPI_Documentacion.md`: documentación práctica de FastAPI para servir modelos mediante APIs REST.  
- `Herramientas_IA_Programacion.md`: comparativa de herramientas adicionales útiles para programación de IA.  
- `Fase2/99_herramientas_ia_integradas.ipynb`: notebook único con ejemplos de LlamaIndex, LangGraph, Haystack, PydanticAI, Instructor, LiteLLM, Ollama, bases vectoriales, Ragas y MLflow desde patrones ejecutables ligeros.  
- `Fase2/100_mlflow_llamaindex_rag.ipynb`: notebook práctico centrado en MLflow y LlamaIndex sin añadir MCP como contenido nuevo.  
- `Fase2/101_langgraph_orquestacion.ipynb`: notebook extra sobre flujos con estado, decisiones y reintentos.  
- `Fase2/102_ollama_modelos_locales.ipynb`: notebook extra sobre modelos locales con Ollama.  
- `Fase2/103_fastapi_serving_modelos.ipynb`: notebook extra sobre servir modelos con una API REST.  
