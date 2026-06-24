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
    border-bottom: 3px solid #16a085;
    padding-bottom: 10px;
  }
  h2 { color: #34495e; }
  strong { color: #e74c3c; }
---

# Proyecto Final — Capstone Project
## Taller de Forecasting Práctico con Python

**Sesión 10** · El Barro del Mundo Real — Torneo de Modelos.

---

# Ha Llegado la Hora de la Verdad

Durante 9 sesiones has construido un arsenal completo:
- Limpieza y preparación de datos temporales.
- Feature Engineering (Lags, EWMA, Fourier, Seno/Coseno).
- Baselines y métricas de evaluación.
- Random Forest, LSTM, TCN y el debate sobre Transformers.

Ahora toca demostrar que sabes **integrar todo** en un problema real donde nada viene limpio.

---

# Las 3 Fases del Proyecto

1. **Parte Guiada (Retail):** Fusión de ventas diarias + tráfico peatonal horario. Debate sobre los domingos de cierre.

2. **Reto Autónomo (Energía):** Fusión de consumo eléctrico (15 min) + temperatura horaria. Downsampling e interpolación. El dilema del apagón.

3. **El Torneo de Modelos:** Enfrentar Baseline vs Random Forest vs Red Neuronal sobre los mismos datos y la misma ventana temporal.

---

# Parte 1: Retail — El Dilema del Domingo

Tienes ventas diarias y tráfico peatonal horario. Frecuencias distintas.

**Solución:** `resample("D").sum()` para comprimir el tráfico a diario.

Después del merge, los domingos aparecen como NaN.
- **Novato:** Interpola con la media → *inventa dinero*.
- **Experto:** `fillna(0)` → *el domingo la tienda estaba cerrada*.

> Rellenar un hueco sin entender su causa es el pecado original del Data Science.

---

# Parte 2: Energía — El Dilema del Apagón

Consumo a 15 min + Temperatura horaria. Hay que interpolar el clima.

La temperatura cambia suavemente → `.interpolate(method="time")` es legal.

¿Pero y los apagones de consumo? Si hubo un apagón, el consumo real fue **0**.
Interpolar un apagón le dice al modelo que la red funcionaba perfectamente. **Mentira.**

---

# Parte 3: El Torneo Final

Reporta una tabla comparativa con el **MAE** de:

| Contendiente | Paradigma |
| :--- | :--- |
| Seasonal Naive | Sentido Común |
| Random Forest + Features | Machine Learning Clásico |
| LSTM o TCN | Deep Learning |

Evaluados sobre la **misma ventana de validación**.
Separación temporal: 70/15/15 sin barajar.

---

# La Reflexión Crítica

Responde como parte de tu entrega:

1. ¿Logró el Deep Learning batir al Random Forest?
2. ¿Valió la pena la complejidad? (Tiempo de entrenamiento vs mejora de MAE).
3. ¿Cuánto mejoró el modelo al añadir la temperatura fusionada?
4. **¿Qué modelo elegiría el CEO y cuál el ingeniero?** ¿Son la misma persona?

---

# Coste-Beneficio

El mejor modelo no es siempre el de menor MAE.

*   Tiempo de entrenamiento.
*   Coste de mantenimiento.
*   Explicabilidad.
*   Mejora real frente al baseline.

Si la mejora es mínima, el modelo simple suele ganar en producción.

---

# 🏆 ¡A Competir!

Abre el notebook `10_proyecto_final.ipynb`

**Entregable:** Una tabla de resultados y una reflexión razonada.

> *El mundo real no premia al que usa el modelo más moderno. Premia al que entiende el problema, sabe de dónde viene cada NaN y puede explicarle a alguien no técnico por qué su modelo se equivocó.*
