# Semana 28 – Agentes y Automatización

---

## 🎯 Objetivos
- Comprender qué es un **agente virtual** y sus aplicaciones.  
- Construir agentes simples con **LangChain** (simulado) y **Gradio**.  
- Introducir la **orquestación de flujos** con **Prefect** (alternativa a Airflow).  
- Explorar la **convergencia tecnológica**: agentes que integran APIs externas (IoT, Cloud).  

---

## 📚 Contenidos principales

### 1. Virtual Agents
- Definición y usos (chatbots, asistentes virtuales, soporte).  
- Herramientas: LangChain (chains + memoria), Gradio para interfaz.  
- Ejemplo: agente Q&A sobre un dataset local.  

### 2. Automatización de flujos
- Concepto de **orquestación**.  
- Prefect como introducción ligera (versus Airflow).  
- Ejemplo: **ETL** sencillo (extraer, transformar, cargar).  

### 3. Convergencia con APIs externas
- Ejemplo: integración con API pública (Chuck Norris jokes, OpenWeather, etc.).  
- Discusión: agentes conectados a IoT o servicios Cloud.  

---

## 📂 Notebooks trabajados
- **99_virtual_agent_intro.ipynb** → Agente conversacional con memoria.  
- **100_prefect_intro.ipynb** → Flujo ETL simple con Prefect.  
- **101_agent_api.ipynb** → Agente que consulta una API externa.  

Versiones disponibles: base, soluciones, soluciones + autotests.  

---

## 🛠️ Actividades prácticas
1. Extender el agente con memoria configurable (`k`).  
2. Reemplazar la tarea `extract()` por lectura de CSV y guardar en JSON.  
3. Sustituir la API de ejemplo por otra pública (ej. OpenWeather).  
4. Reflexionar: ¿qué riesgos tiene depender de APIs externas para un agente?  

---

## ✅ Evaluación (RA2, RA3, RA4)
- **RA2.d**: implementación de aplicaciones con agentes básicos.  
- **RA2.e**: evaluación de los resultados obtenidos.  
- **RA3.b/c**: ventajas de la convergencia tecnológica.  
- **RA4.c/d**: evaluación de modelos de automatización.  

**Criterios de evaluación:**  
- Creación de un agente funcional.  
- Ejecución correcta de un flujo orquestado.  
- Integración con una API externa.  
- Reflexión crítica sobre aplicaciones y limitaciones.  

---

## 📌 Recursos recomendados
- [Gradio Docs](https://www.gradio.app/)  
- [Prefect Docs](https://docs.prefect.io/)  
- [LangChain Python](https://python.langchain.com/)  
- [APIs públicas](https://github.com/public-apis/public-apis)  
