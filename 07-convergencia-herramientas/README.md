# UD7 — Convergencia de Herramientas IA

## Estado

✅ **Completa**

## Resumen

Unidad diseñada con enfoque **workflow-based + problem-first**: parte del problema real de llevar un notebook a producción y recorre el stack convergente completo, desde datos y experimentación hasta serving, agentes, observabilidad e IA responsable.

El proyecto final de UD7 debe dejar explícitos el impacto sobre el negocio o el proceso afectado, la seguridad del sistema y la conveniencia de la solución elegida frente a alternativas más simples.

## Estructura

- `01-teoria/`: guías teóricas F0–F8 y proyecto integrador.
- `02-ejemplos/`: scripts de referencia para el pipeline completo.
- `03-practicas/`: notebooks P1–P8.
- `04-evaluacion/`: criterios, rúbrica y examen teórico.
- `05-recursos/`: cheatsheet y enlaces de referencia.
- `99-profesor/`: guía docente.

## Herramientas clave

Prefect, MLflow, FastAPI, LlamaIndex con indexación jerárquica, CrewAI, Evidently, Fairlearn, SHAP y Guardrails.

## Nota sobre F6

El RAG tradicional se trata solo como recordatorio de la unidad **Modelos de la IA**. En UD7, F6 trabaja **LlamaIndex con indexación jerárquica** (`HierarchicalNodeParser` + `RecursiveRetriever`) y el caso ParkingCorp, con CrewAI como capa de orquestación multi-agente.
