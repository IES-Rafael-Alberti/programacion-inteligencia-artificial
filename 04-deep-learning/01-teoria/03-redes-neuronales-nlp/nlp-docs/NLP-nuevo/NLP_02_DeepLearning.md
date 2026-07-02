# 🧠 NLP Fase 2 — Deep Learning (Embeddings + LSTM)

## 🎯 Objetivo
Pasar de modelos clásicos (TF-IDF) a modelos que aprenden representaciones:
- Embeddings
- LSTM
- Comparativa con TF-IDF

---

## 🔗 Recordatorio

En Fase 1:
Texto → TF-IDF → Modelo

Problema:
❌ No entiende contexto  
❌ No entiende orden  

---

## 🔢 Embeddings

Los embeddings representan palabras como vectores densos.

Ejemplo conceptual:
gato → [0.21, -0.44, 0.78, ...]

Ventaja:
- palabras similares → vectores cercanos

---

## 🔄 De TF-IDF a Embeddings

TF-IDF:
- vector disperso
- sin semántica

Embeddings:
- vector denso
- con significado

---

## 🧠 LSTM

Las LSTM son redes que procesan secuencias:

- tienen memoria
- capturan orden
- mejoran contexto

---

## 🔄 Pipeline Deep Learning

Texto
↓
Tokenización
↓
Embeddings
↓
LSTM
↓
Clasificación

---

## ⚖️ Comparativa

| Modelo | Ventajas | Desventajas |
|--------|---------|------------|
| TF-IDF | rápido | no contexto |
| LSTM | contexto | más coste |

---

## 💡 Idea clave

> Cambiar la representación cambia todo el modelo
