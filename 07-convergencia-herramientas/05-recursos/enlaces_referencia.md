# Enlaces y Referencias — UD7 Convergencia de Herramientas IA

Recopilación de enlaces oficiales, tutoriales y recursos adicionales organizados por fase y herramienta.

---

## F0 — Gap de Producción

### Conceptos MLOps y Convergencia

| Recurso | Tipo | Enlace |
|---------|------|--------|
| MLops Foundation (Google Cloud) | Artículo | https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning |
| What is MLOps? (NVIDIA) | Artículo | https://www.nvidia.com/en-us/glossary/machine-learning-mlops/ |
| The ML Gap: From Notebook to Production (Dataiku) | Blog | https://blog.dataiku.com/from-notebook-to-production |
| Hidden Technical Debt in ML Systems (Google) | Paper | https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html |
| Machine Learning Engineering (Andriy Burkov) | Libro | https://www.mlebook.com/ |

### Referencias UD7

| Recurso | Tipo | Ruta |
|---------|------|------|
| Mapa RA/CE de la unidad | Documento | `01-teoria/00_RA_CE_UD7.md` |
| Gap de producción | Documento | `01-teoria/01_gap_produccion.md` |

---

## F1 — Desarrollo Asistido por IA

### Herramientas

| Recurso | Tipo | Enlace |
|---------|------|--------|
| GitHub Copilot | Oficial | https://github.com/features/copilot |
| Cursor IDE | Oficial | https://cursor.com |
| Claude Code (Anthropic) | Oficial | https://docs.anthropic.com/en/docs/claude-code/overview |
| Claude Chat | Oficial | https://claude.ai |
| GitHub Copilot Documentation | Docs | https://docs.github.com/en/copilot |
| Effective Prompt Engineering for Copilot | Guía | https://github.com/features/copilot/prompt-engineering |

### Tutoriales

| Recurso | Enlace |
|---------|--------|
| Copilot Quickstart | https://docs.github.com/en/copilot/quickstart |
| Cursor Tutorial | https://docs.cursor.com/get-started/overview |

---

## F2 — Pipeline de Datos

### Herramientas

| Recurso | Tipo | Enlace |
|---------|------|--------|
| Pandas Documentation | Oficial | https://pandas.pydata.org/docs/ |
| Pydantic Documentation | Oficial | https://docs.pydantic.dev/latest/ |
| Great Expectations | Oficial | https://greatexpectations.io |
| pandera (Data validation) | Docs | https://pandera.readthedocs.io/ |
| DVC (Data Version Control) | Oficial | https://dvc.org |

### Tutoriales

| Recurso | Enlace |
|---------|--------|
| Pandas Getting Started | https://pandas.pydata.org/docs/getting_started/index.html |
| Great Expectations Quickstart | https://docs.greatexpectations.io/docs/oss/guides/quickstart/ |
| DVC Tutorial | https://dvc.org/doc/start |

---

## F3 — Experimentación con MLflow

### Oficial

| Recurso | Tipo | Enlace |
|---------|------|--------|
| MLflow Documentation | Oficial | https://mlflow.org/docs/latest/index.html |
| MLflow Tracking | Docs | https://mlflow.org/docs/latest/tracking.html |
| MLflow Model Registry | Docs | https://mlflow.org/docs/latest/model-registry.html |
| MLflow GitHub | Repo | https://github.com/mlflow/mlflow |

### Tutoriales

| Recurso | Enlace |
|---------|--------|
| MLflow Quickstart | https://mlflow.org/docs/latest/getting-started/index.html |
| MLflow Tracking Examples | https://github.com/mlflow/mlflow/tree/master/examples |
| Comparing Models with MLflow | https://mlflow.org/docs/latest/tracking.html#comparing-runs |

---

## F4 — Orquestación con Prefect

### Oficial

| Recurso | Tipo | Enlace |
|---------|------|--------|
| Prefect Documentation | Oficial | https://docs.prefect.io/latest/ |
| Prefect Concepts | Docs | https://docs.prefect.io/latest/concepts/flows/ |
| Prefect Tasks | Docs | https://docs.prefect.io/latest/concepts/tasks/ |
| Prefect GitHub | Repo | https://github.com/PrefectHQ/prefect |

### Tutoriales

| Recurso | Enlace |
|---------|--------|
| Prefect Tutorial | https://docs.prefect.io/latest/tutorial/ |
| Prefect ML Pipeline Example | https://docs.prefect.io/latest/guides/ml-pipeline/ |
| Prefect + MLflow Integration | https://docs.prefect.io/latest/integrations/prefect-mlflow/ |

---

## F5 — Serving y APIs

### FastAPI

| Recurso | Tipo | Enlace |
|---------|------|--------|
| FastAPI Documentation | Oficial | https://fastapi.tiangolo.com/ |
| FastAPI Security (API Keys) | Docs | https://fastapi.tiangolo.com/tutorial/security/ |
| FastAPI Versioning | Patterns | https://fastapi.tiangolo.com/tutorial/versioning/ |
| Pydantic Documentation | Docs | https://docs.pydantic.dev/latest/ |
| slowapi (Rate Limiting) | Repo | https://github.com/laurentS/slowapi |

### Tutoriales

| Recurso | Enlace |
|---------|--------|
| FastAPI First Steps | https://fastapi.tiangolo.com/tutorial/first-steps/ |
| Deploy ML Models with FastAPI | https://fastapi.tiangolo.com/deployment/ |
| FastAPI + MLflow Integration | https://mlflow.org/docs/latest/deployment/index.html |

---

## F6 — Agentes y RAG

### Frameworks

| Recurso | Tipo | Enlace |
|---------|------|--------|
| CrewAI Documentation | Oficial | https://docs.crewai.com/ |
| AutoGen Documentation | Oficial | https://microsoft.github.io/autogen/stable/ |
| LlamaIndex Documentation | Oficial | https://docs.llamaindex.ai/ |
| LlamaIndex Node Parsers | Docs | https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/ |
| LlamaIndex Retrievers | Docs | https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/ |
| LangChain Documentation | Background UD6 | https://python.langchain.com/docs/introduction/ |
| ChromaDB Documentation | Background UD6 | https://docs.trychroma.com/ |
| LangSmith | Oficial | https://smith.langchain.com/ |

### Tutoriales

| Recurso | Enlace |
|---------|--------|
| CrewAI Quickstart | https://docs.crewai.com/quickstart |
| AutoGen Tutorial | https://microsoft.github.io/autogen/stable/tutorial/introduction.html |
| LlamaIndex Recursive Retriever Pack | https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/ |
| LlamaIndex Hierarchical Node Parser | https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/ |
| LangChain RAG Tutorial (repaso UD6) | https://python.langchain.com/docs/tutorials/rag/ |
| ChromaDB Getting Started (repaso UD6) | https://docs.trychroma.com/getting-started |

### Modelos Locales

| Recurso | Enlace |
|---------|--------|
| Ollama | https://ollama.com |
| Ollama GitHub | https://github.com/ollama/ollama |
| HuggingFace Embeddings | https://huggingface.co/models?pipeline_tag=feature-extraction |

---

## F7 — Observabilidad

### Evidently

| Recurso | Tipo | Enlace |
|---------|------|--------|
| Evidently Documentation | Oficial | https://docs.evidentlyai.com/ |
| Evidently GitHub | Repo | https://github.com/evidentlyai/evidently |
| Data Drift Detection | Docs | https://docs.evidentlyai.com/presets/data-drift |
| Evidently + MLflow Integration | Docs | https://docs.evidentlyai.com/integrations/mlflow |

### LangSmith

| Recurso | Tipo | Enlace |
|---------|------|--------|
| LangSmith Documentation | Oficial | https://docs.smith.langchain.com/ |
| LangSmith Tracing | Docs | https://docs.smith.langchain.com/tracing |

### Conceptos

| Recurso | Enlace |
|---------|--------|
| ML Monitoring vs Observability | https://www.evidentlyai.com/blog/ml-observability-vs-monitoring |
| A comprehensive guide to data drift | https://www.evidentlyai.com/blog/data-drift |

---

## F8 — IA Responsable

### Guardrails

| Recurso | Tipo | Enlace |
|---------|------|--------|
| NeMo Guardrails (NVIDIA) | Oficial | https://github.com/NVIDIA/NeMo-Guardrails |
| NeMo Guardrails Documentation | Docs | https://docs.nvidia.com/nemo/guardrails/ |
| Guardrails AI (Python) | Oficial | https://www.guardrailsai.com/ |
| Guardrails AI GitHub | Repo | https://github.com/guardrails-ai/guardrails |

### Equidad y Sesgo

| Recurso | Tipo | Enlace |
|---------|------|--------|
| Fairlearn Documentation | Oficial | https://fairlearn.org/ |
| Fairlearn GitHub | Repo | https://github.com/fairlearn/fairlearn |
| AIF360 (IBM) | Repo | https://github.com/Trusted-AI/AIF360 |
| Google PAIR (People + AI Research) | Guía | https://pair.withgoogle.com/ |

### Explicabilidad

| Recurso | Tipo | Enlace |
|---------|------|--------|
| SHAP Documentation | Oficial | https://shap.readthedocs.io/ |
| SHAP GitHub | Repo | https://github.com/shap/shap |
| LIME GitHub | Repo | https://github.com/marcotcr/lime |
| Interpretable ML Book (Molnar) | Libro | https://christophm.github.io/interpretable-ml-book/ |

### Regulación

| Recurso | Tipo | Enlace |
|---------|------|--------|
| EU AI Act (Official) | Oficial | https://artificialintelligenceact.eu/ |
| EU AI Act Summary (DataGuard) | Resumen | https://www.dataguard.co.uk/blog/eu-ai-act/ |
| GDPR Right to Explanation | Artículo | https://ico.org.uk/for-organisations/guide-to-data-protection/key-data-protection-themes/explaining-decisions-made-with-artificial-intelligence/ |

---

## Proyecto Final

### Arquitectura y Referencia

| Recurso | Enlace |
|---------|--------|
| MLflow + Prefect + FastAPI Integration Example | https://github.com/mlflow/mlflow/tree/master/examples/prefect |
| Full-Stack ML Project Template | https://github.com/khuyentran1401/machine-learning-template |
| Cookiecutter Data Science | https://drivendata.github.io/cookiecutter-data-science/ |

### Despliegue y Producción

| Recurso | Enlace |
|---------|--------|
| Uvicorn + FastAPI Deployment | https://fastapi.tiangolo.com/deployment/ |
| Dockerizing ML Models | https://docs.docker.com/guides/use-case/machine-learning/ |
| ONNX Model Export | https://onnx.ai/ |

---

## Generales

### Cursos y Formación

| Recurso | Enlace |
|---------|--------|
| Made With ML (MLOps) | https://madewithml.com/ |
| Full Stack Deep Learning | https://fullstackdeeplearning.com/ |
| CS329x (Stanford) | https://stanford-cs329s.github.io/ |
| MLOps Zoomcamp (DataTalks) | https://github.com/DataTalksClub/mlops-zoomcamp |

### Comunidad

| Recurso | Enlace |
|---------|--------|
| MLflow Community | https://mlflow.org/community |
| Prefect Community Slack | https://www.prefect.io/community |
| Evidently Community | https://evidentlyai.com/community |
| LangChain Discord | https://discord.gg/langchain |

---

## Notas para el Alumno

1. **Prioriza las fuentes oficiales** —la documentación oficial es siempre la más actualizada.
2. **Los tutoriales de UD7 asumen que tienes las herramientas instaladas** —consulta esta guía si necesitas ayuda con la instalación.
3. **Los enlaces se comprobaron en junio de 2026** —si algún enlace no funciona, búscalo en el repositorio oficial de GitHub de la herramienta.
4. **Contribuye a la comunidad** —si encuentras un recurso útil que no está aquí, compártelo con el profesor para añadirlo.
