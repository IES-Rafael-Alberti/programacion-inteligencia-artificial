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
    border-bottom: 3px solid #f39c12;
    padding-bottom: 10px;
  }
  h2 {
    color: #34495e;
  }
  strong {
    color: #e74c3c;
  }
---

# Redes Convolucionales Temporales (TCN)
## Taller de Forecasting Práctico con Python

**Sesión 08**
Mirando el tiempo a través de una rendija.

---

# ¿Por qué Convoluciones para el Tiempo?

Las CNNs no son solo para fotos de gatos. Una serie temporal es una señal 1D.

**Ventajas frente a las LSTMs:**
1.  **Paralelismo:** Procesan toda la ventana de golpe (mucho más rápidas).
2.  **Estabilidad:** No sufren los problemas de gradientes de las redes recurrentes.
3.  **Memoria Controlada:** Decidimos exactamente cuántas horas atrás mira la red.

---

# Causalidad: El Primer Mandamiento

En una foto, un píxel depende de sus vecinos a izquierda y derecha. 
**En el tiempo, el presente NO puede depender del futuro.**

Usamos **Convoluciones Causales**:
Aseguramos que para calcular el valor en el tiempo $t$, la red solo pueda ver datos de $t, t-1, t-2...$

---

# Dilatación: El Superpoder de la TCN

Si queremos que una red mire 1000 horas atrás, ¿necesitamos 1000 capas? **No.**

Usamos **Convoluciones Dilatadas**:
*   Capa 1: Mira cada paso (1).
*   Capa 2: Salta de 2 en 2.
*   Capa 3: Salta de 4 en 4.

Con solo 10 capas, ¡podemos ver más de 1000 pasos atrás! Esto permite capturar estacionalidades semanales o mensuales con muy poca memoria.

---

# Arquitectura en PyTorch Lightning ⚡

Definimos un bloque convolucional con `dilation` y lo repetimos en un `Sequential`.

Lo más importante:
- Entrada: `[Batch, Features, Sequence]`
- Salida: Un único valor escalar (la predicción).

*(El código completo está detallado en el documento 08_redes_convolucionales_tcn.md)*

---

# TCN vs LSTM: El Duelo

| LSTM | TCN |
| :--- | :--- |
| Memoria "borrosa" basada en estado | Memoria "rígida" basada en campo receptivo |
| Lenta de entrenar | Muy rápida (paralela) |
| Buena para patrones muy rítmicos | Mejor para patrones complejos y lejanos |

---

# 🚀 ¡A Convolucionar!

Abre el notebook `08_redes_convolucionales_tcn.ipynb`

Vamos a:
1. Implementar un bloque TCN desde cero.
2. Jugar con el parámetro de `dilation` para ver cómo cambia lo que la red "ve".
3. Comparar el tiempo de entrenamiento vs la LSTM de la sesión anterior.
