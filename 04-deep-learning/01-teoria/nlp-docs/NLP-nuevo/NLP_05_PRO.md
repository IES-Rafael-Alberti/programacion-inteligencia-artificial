# 🧠 NLP 05 — Embeddings de frases y búsqueda semántica (PRO)

---

## 🎯 Objetivo

Aprender a representar texto con **embeddings semánticos** y construir un sistema de:

- similitud entre frases
- búsqueda por significado

---

## 🧩 Problema

TF-IDF falla en búsquedas semánticas:

"gato juega"
"felino jugando"

👉 TF-IDF los ve distintos  
👉 un embedding semántico los acerca

---

## 🔢 Embeddings de frases

Un embedding es un vector denso que representa significado:

"el gato juega" → [0.21, -0.4, ...]

Propiedad clave:
👉 frases similares → vectores cercanos

---

## 📏 Similitud

Se mide con **coseno**:

- 1 → muy similares
- 0 → no relacionadas

---

## 🔄 Pipeline

Texto
↓
Modelo de embeddings
↓
Vector
↓
Comparación (coseno)

---

## ⚖️ Comparación con TF-IDF

| Método | Semántica | Contexto |
|--------|----------|---------|
| TF-IDF | ❌ | ❌ |
| Embeddings | ✅ | parcial |

---

## 💡 Casos de uso

- buscadores inteligentes
- FAQ automático
- recomendación
- deduplicación

---

## 🧠 Idea clave

> No buscamos palabras iguales,
> buscamos significado similar
