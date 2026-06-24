# Práctica 2 — Modelado exploratorio con PyCaret

## Contexto
En esta práctica utilizarás PyCaret como herramienta de AutoML para explorar
qué modelos funcionan mejor con el dataset.

PyCaret se usará como apoyo para la toma de decisiones, no como solución final.

## Objetivos
- Definir correctamente un problema de ML
- Comparar distintos modelos de forma objetiva
- Interpretar métricas
- Elegir un modelo de forma razonada

## Problema a resolver
(Elige uno)

- Clasificación: predecir si una película tendrá una valoración alta
- Regresión: predecir la valoración de una película

## Tareas a realizar

### 1. Preparación del dataset
- Selección de variables
- Definición de la variable objetivo
- Eliminación de columnas no relevantes

### 2. Configuración de PyCaret
- Setup del experimento
- Separación train/test
- Normalización y encoding automático

### 3. Comparación de modelos
- Uso de `compare_models()`
- Análisis de las métricas obtenidas

### 4. Elección del modelo
Selecciona **un único modelo** y justifica:
- Por qué lo eliges
- Qué métricas has priorizado
- Posibles limitaciones

## Entregable
Notebook: `P2_PyCaret_base.ipynb`

## Anexo I LazyClassifier vs Pycaret

**LazyPredict** y **PyCaret** son ambas bibliotecas de Python diseñadas para agilizar los flujos de trabajo de aprendizaje automático, pero difieren significativamente en alcance, funcionalidad y casos de uso.

### **LazyPredict**
- **Enfoque Principal**: Evaluación y comparación rápida de modelos.
- **Características Clave**:
  - Entrena y evalúa **docenas de modelos con solo dos líneas de código**.
  - **Sin ajuste de hiperparámetros** — proporciona estimaciones de rendimiento base.
  - Ligero y rápido — ideal para prototipado rápido o exploración inicial de modelos.
  - Los resultados son fácilmente replicables usando scikit-learn.
- **Mejor Para**: Científicos de datos que desean una **forma rápida y de bajo código para comparar múltiples modelos** sin personalización profunda.

### **PyCaret**
- **Enfoque Principal**: Automatización de extremo a extremo del ciclo de vida del aprendizaje automático.
- **Características Clave**:
  - Automatiza el **preprocesamiento de datos, ingeniería de características, selección de modelos, ajuste de hiperparámetros y despliegue**.
  - Ofrece **abstracciones de alto nivel** con amplias herramientas de visualización (ej. curvas ROC, matrices de confusión).
  - Soporta **interpretación de modelos, guardado de pipelines e integración con MLOps**.
  - Incluye capacidades avanzadas como **PLN, clustering, detección de anomalías y minería de reglas de asociación**.
- **Mejor Para**: Usuarios que buscan un **flujo de trabajo completo y listo para producción** con código mínimo, especialmente para proyectos complejos.

### **Resumen Comparativo**
| Característica | **LazyPredict** | **PyCaret** |
|--------|------------------|-------------|
| Entrenamiento de Modelos | Sí (base) | Sí (con ajuste) |
| Ajuste de Hiperparámetros | ❌ No | ✅ Sí |
| Preprocesamiento de Datos | ❌ Mínimo | ✅ Automatización completa |
| Despliegue de Modelos | ❌ No incluido | ✅ Soportado |
| Velocidad | ⚡ Muy rápido | ⏱️ Más lento (más características) |
| Caso de Uso | Comparación rápida de modelos | Automatización completa de pipeline ML |

### **Conclusión**
- Usa **LazyPredict** cuando necesites **benchmarking rápido y simple de modelos**.
- Usa **PyCaret** cuando quieras **construir y desplegar pipelines completos de aprendizaje automático** con mínimo esfuerzo.

> **Nota**: Ambas herramientas no son reemplazos del juicio experto. Se utilizan mejor como **aceleradores** en las etapas tempranas de un proyecto.

