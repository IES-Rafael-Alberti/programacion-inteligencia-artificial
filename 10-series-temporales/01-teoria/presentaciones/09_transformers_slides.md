---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #f8f9fa
style: |
  section {
    font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  }
  h1 {
    color: #2b3a4a;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
  }
  h2 { color: #34495e; }
  strong { color: #e74c3c; }
  table { font-size: 0.82em; }
---

# Transformers en Series Temporales
## Taller de Forecasting Práctico con Python

**Sesión 09** · ¿Es la Atención todo lo que necesitas?

---

# La Promesa del Transformer

En 2017, Google publicó *"Attention is All You Need"*.
Los Transformers conquistaron: lenguaje (GPT), imágenes (ViT).

**La promesa para el tiempo:** capturar dependencias infinitas sin los problemas de las LSTMs.

Pero en 2023, un paper sacudió los cimientos:
*"Are Transformers Effective for Time Series Forecasting?"*

**Resultado:** Dos capas lineales batían sistemáticamente a los Transformers más sofisticados.

---

# El Problema: Tokenismo Punto a Punto

En lenguaje, cada token ("banco") tiene **semántica rica**.
En tiempo, un punto (`1.85 kWh`) **no significa nada por sí solo**.

La atención calcula similitud entre todos los pares de puntos.
Si los puntos no tienen significado individual, la matriz de atención es **ruido puro**.

Además, el coste es $O(L^2)$. Con $L=8760$ (un año horario): **76 millones** de cálculos.

---

# DLinear: La Lección de Humildad

El modelo que puso en jaque a los Transformers tiene solo **dos capas lineales**:

1. Descomponer la serie en **Tendencia + Residuo** (media móvil).
2. Aplicar una capa lineal a cada componente.

¿Resultado? Iguala o supera a Autoformer, FEDformer e Informer en benchmarks estándar.

> *A veces, la mejor arquitectura es la más simple.*

---

# PatchTST: La Salvación

Si el problema es que cada punto no tiene semántica, la solución es obvia: **usa segmentos**.

```text
Serie:    [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12]
Parches:  [h1..h3]  [h4..h6]  [h7..h9]  [h10..h12]
           Token 1    Token 2    Token 3    Token 4
```

Cada token ahora tiene forma, tendencia y contexto local.
La atención entre tokens **por fin tiene sentido**.

---

# Foundation Models (Zero-Shot)

Modelos pre-entrenados con **billones de puntos temporales**:

- **TimeGPT (Nixtla):** Le pasas tu CSV → devuelve predicción. Sin entrenar.
- **Lag-Llama:** Basado en LLaMA, detecta lags automáticamente.
- **Chronos (Amazon):** Open-source, desplegable en local.

**Limitaciones:** Caja negra, coste computacional, pueden fallar en series muy locales.

---

# ¿Cuándo Sí y Cuándo No?

| Situación | ¿Transformer? |
| :--- | :---: |
| Series cortas, pocos datos | ❌ DLinear o RF |
| Miles de series, Cross-Learning masivo | ✅ PatchTST |
| Horizonte corto, estacionalidad fuerte | ❌ Seasonal Naive |
| Sin datos históricos propios | ✅ Foundation Model |

---

# 🚀 ¡Al Debate!

Abre el notebook `09_transformers_series_temporales.ipynb`

**Misiones:**
1. Implementar DLinear y comparar contra el Seasonal Naive.
2. Visualizar la matriz de atención para 24 horas de consumo.
3. Debate en clase: ¿Transformers o Feature Engineering?
