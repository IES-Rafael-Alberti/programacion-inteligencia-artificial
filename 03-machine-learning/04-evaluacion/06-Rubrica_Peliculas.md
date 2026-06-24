# 📊 Rúbrica — Proyecto Dataset de Películas (PIA)

Proyecto consistente en la **construcción de un dataset propio de películas**, su **análisis exploratorio**, **preparación para aprendizaje automático**, **entrenamiento de modelos**, **evaluación**, y **despliegue mínimo** del resultado.

---

## 🎯 Resultados de Aprendizaje y Criterios Evaluados

- **RA1**: Caracteriza lenguajes, herramientas y estructuras de programación para IA.
  - CE a), b), c)
- **RA2**: Desarrolla aplicaciones de IA aplicando técnicas de análisis, modelado y evaluación.
  - CE a), b), c), d), e)
- **RA4**: Integra modelos de IA en soluciones automatizadas.
  - CE c), d)

> ⚠️ **Es obligatorio alcanzar un nivel mínimo “Adecuado” en todos los RA para superar el proyecto.**

---

## 🧩 Desglose de la evaluación

### 1️⃣ Construcción del dataset (RA1 – CE a, b) — **20%**

| Nivel | Descripción |
|-----|------------|
| **Excelente (9–10)** | Dataset construido a partir de **múltiples fuentes** (OMDb, TMDB, etc.), integración correcta, resolución de duplicados (IDs, títulos, fechas), estructura clara y documentada. |
| **Notable (7–8)** | Dataset funcional a partir de una o dos fuentes, integración correcta con pequeñas incoherencias no críticas. |
| **Adecuado (5–6)** | Dataset generado y usable, aunque con integración simple o estructura mejorable. |
| **Insuficiente (<5)** | Dataset incompleto, mal integrado o descargado sin tratamiento propio. |

---

### 2️⃣ Análisis Exploratorio de Datos (EDA) (RA2 – CE a, b) — **20%**

| Nivel | Descripción |
|-----|------------|
| **Excelente** | EDA completo y razonado: estadísticas, visualizaciones claras (Seaborn/Matplotlib), detección de patrones, outliers y problemas de calidad de datos. |
| **Notable** | EDA correcto con visualizaciones relevantes y conclusiones coherentes. |
| **Adecuado** | EDA básico pero funcional; visualizaciones simples con conclusiones evidentes. |
| **Insuficiente** | EDA superficial, sin visualización o sin interpretación. |

---

### 3️⃣ Preparación de datos y feature engineering (RA2 – CE b, c) — **20%**

| Nivel | Descripción |
|-----|------------|
| **Excelente** | Tratamiento correcto de nulos, codificación adecuada de variables categóricas, escalado justificado y creación de nuevas características relevantes. |
| **Notable** | Preparación correcta con técnicas estándar bien aplicadas. |
| **Adecuado** | Preparación mínima suficiente para entrenar modelos. |
| **Insuficiente** | Datos mal preparados o directamente usados sin transformación. |

---

### 4️⃣ Modelado y evaluación (RA2 – CE c, d, e) — **25%**

| Nivel | Descripción |
|-----|------------|
| **Excelente** | Comparación de varios modelos, selección razonada mediante métricas, optimización de hiperparámetros (Grid/Random/AutoML) y análisis crítico de resultados. |
| **Notable** | Entrenamiento correcto de varios modelos con métricas bien calculadas. |
| **Adecuado** | Entrenamiento de al menos un modelo con métricas básicas correctas. |
| **Insuficiente** | Modelo mal entrenado, métricas incorrectas o inexistentes. |

---

### 5️⃣ Persistencia y despliegue del modelo (RA4 – CE c, d) — **15%**

| Nivel | Descripción |
|-----|------------|
| **Excelente** | Modelo guardado y desplegado correctamente mediante **FastAPI o Streamlit**, con explicación clara del flujo. |
| **Notable** | Modelo guardado y desplegado de forma funcional pero básica. |
| **Adecuado** | Modelo guardado correctamente sin despliegue completo. |
| **Insuficiente** | Modelo no persistido o no reutilizable. |

---

## 🧮 Calificación final

| Bloque | Peso |
|-----|----|
| Construcción del dataset | 20% |
| EDA | 20% |
| Preparación de datos | 20% |
| Modelado y evaluación | 25% |
| Despliegue | 15% |
| **TOTAL** | **100%** |

---

## ❗ Condiciones importantes

- El proyecto puede realizarse **por parejas**.
- El uso de librerías externas (PyCaret, cuML, etc.) **debe justificarse**.
- Copiar datasets ya preparados **sin proceso propio** invalida el proyecto.
- El despliegue es **obligatorio** (mínimo funcional).

---

## 🧠 Observación final

Este proyecto evalúa **capacidad técnica**, **criterio**, y **visión profesional**, no solo que “el código funcione”.
