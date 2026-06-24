# 🧠 NLP 04 — Comparación de enfoques (TF-IDF vs LSTM vs BERT)

---

## 🎯 Objetivo

En este bloque vamos a dejar de “aprender modelos” y empezar a pensar como ingenieros:

- comparar enfoques
- entender sus diferencias reales
- tomar decisiones justificadas

---

## 🧩 El problema real

En un proyecto real, no preguntas:

❌ ¿Cuál es el modelo más potente?  
✔ ¿Cuál es el modelo adecuado para ESTE problema?

---

## 🔁 Recordatorio progresivo

### 1. TF-IDF (NLP clásico)

Transforma texto en vectores dispersos.

✔ rápido  
✔ interpretable  
❌ sin contexto  

---

### 2. LSTM (Deep Learning)

Procesa secuencias y aprende embeddings.

✔ captura orden  
✔ aprende representaciones  
❌ necesita más datos  

---

### 3. BERT (Transformers)

Modelo preentrenado con contexto completo.

✔ entiende contexto  
✔ muy potente  
❌ más coste  

---

## ⚖️ Comparación estructurada

| Factor | TF-IDF | LSTM | BERT |
|------|--------|------|------|
| Contexto | ❌ | parcial | ✅ |
| Datos | bajo | medio | bajo |
| Tiempo | muy bajo | medio | alto |
| Facilidad | alta | media | media |
| Rendimiento | medio | bueno | muy bueno |

---

## 🧠 Qué debes analizar SIEMPRE

- rendimiento
- overfitting
- tiempo
- complejidad
- facilidad de despliegue

---

## 🚧 Error típico

> usar BERT siempre “porque es mejor”

---

## 💡 Idea clave

> Elegir modelo = equilibrio entre coste y rendimiento

---

## 🧠 Conclusión

Has pasado de:
- ejecutar modelos  
a  
- decidir modelos
