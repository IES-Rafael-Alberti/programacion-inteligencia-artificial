# 🧠 NLP Fase 3 — Transformers (BERT) y Comparativa

---

## 🎯 Objetivo de esta fase

En esta fase vamos a dar el salto final en NLP:

- Usar un modelo moderno: **BERT**
- Comparar con:
  - TF-IDF (clásico)
  - LSTM (deep learning)
- Entender cuándo usar cada uno

---

## 🔁 Recordatorio del camino

Hemos visto:

### Fase 1
Texto → TF-IDF → Modelo

### Fase 2
Texto → Embeddings → LSTM → Modelo

Ahora:

### Fase 3
Texto → Transformer (BERT) → Modelo

---

## 🤖 ¿Qué es BERT?

BERT es un modelo basado en **Transformers** que:

- entiende contexto
- analiza la frase completa a la vez
- genera representaciones dinámicas

Ejemplo:

"banco" en:
- "me senté en el banco"
- "trabajo en un banco"

👉 tiene significados diferentes

---

## ⚙️ ¿Qué hace diferente a BERT?

A diferencia de TF-IDF o embeddings simples:

- usa **self-attention**
- tiene en cuenta el contexto completo
- está **preentrenado** en grandes corpus

---

## 🔄 Transfer learning en NLP

Igual que en visión:

- MobileNet → imágenes
- BERT → texto

Podemos:

- usarlo directamente
- hacer fine-tuning

---

## 🔁 Pipeline con BERT

Texto
↓
Tokenización (BERT tokenizer)
↓
Modelo BERT
↓
Capa de clasificación
↓
Predicción

---

## ⚖️ Comparativa global

| Modelo | Representación | Contexto | Coste |
|--------|--------------|---------|------|
| TF-IDF | dispersa | ❌ | bajo |
| LSTM | embeddings | parcial | medio |
| BERT | contextual | ✅ | alto |

---

## 🧠 ¿Cuándo usar cada uno?

### TF-IDF
- datasets pequeños
- baseline rápido

### LSTM
- secuencias simples
- aprendizaje desde cero

### BERT
- mejor rendimiento
- problemas reales

---

## 🚧 Limitaciones de BERT

- más lento
- más recursos
- más complejo

---

## 💡 Idea clave

> No siempre el mejor modelo es el más complejo.
> En ingeniería, importa el equilibrio.

---

## 🔗 Conexión con visión

Esto es equivalente a:

| Visión | NLP |
|-------|-----|
| CNN | LSTM |
| MobileNet | BERT |

---

## 🧠 Conclusión

Hemos completado el pipeline completo:

TF-IDF → LSTM → BERT

👉 ahora podemos comparar enfoques reales de industria
