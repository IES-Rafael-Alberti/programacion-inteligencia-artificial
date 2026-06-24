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
    border-bottom: 3px solid #9b59b6;
    padding-bottom: 10px;
  }
  h2 {
    color: #34495e;
  }
  strong {
    color: #e74c3c;
  }
  code {
    background-color: #ecf0f1;
    color: #c0392b;
  }
---

# Baselines y Evaluación
## Taller de Forecasting Práctico con Python

**Sesión 04**
Construir una referencia sólida antes de usar modelos complejos.

---

# El Sesgo de la Complejidad

Existe una creencia muy peligrosa en Data Science: *"Solo el Deep Learning o XGBoost pueden resolver mi problema"*.

En forecasting, un modelo avanzado no es útil por ser avanzado, sino porque **logra batir consistentemente a una referencia de sentido común**.

Si tu red neuronal que tardó semanas en programarse solo mejora un 1% la predicción frente a la estrategia de *"Mañana venderé lo mismo que hoy"*, tu modelo no tiene valor de negocio.

---

# El Pecado Capital: Cortar el tiempo al azar

En Machine Learning clásico mezclamos los datos y sacamos un 20% aleatorio para Test (usando `train_test_split`). 

**Hacer esto en Forecasting es hacer trampas.**
Si usas datos del jueves para entrenar y predices el miércoles, estás usando el futuro para predecir el pasado.

**División Cronológica Obligatoria:**
1.  **Entrenamiento (Pasado Lejano):** Para aprender las reglas del juego.
2.  **Validación (Pasado Reciente):** Para elegir el mejor modelo.
3.  **Test (Futuro Desconocido):** La caja fuerte. Se abre solo una vez al final.

---

# ¿Cómo Castigamos al Modelo? (Métricas)

La métrica se elige dependiendo de **cuánto dinero pierdes al fallar**.

*   **MAE (Mean Absolute Error):** El error promedio puro. 
    *Uso:* Cuando fallar por 20 duele exactamente el doble que fallar por 10.
*   **RMSE (Root Mean Squared Error):** La "lupa". Al elevar al cuadrado, castiga brutalmente los errores grandes. 
    *Uso:* Cuando fallar por poco no importa, pero fallar por mucho es catastrófico (Ej: colapso de un hospital).
*   **MAPE (Error Porcentual):** Mide el error en %. 
    *Uso:* Para hablar con directivos. (¡Cuidado si la demanda es cero, el porcentaje se va a infinito!).

---

# Generando Baselines Fuertes

Antes de Machine Learning, probamos algoritmos de "Sentido Común".

1.  **Naive (El Ingenuo):** Asume que el mundo se congeló. *El consumo de hoy será exactamente el mismo que el de la última hora.*
2.  **Seasonal Naive (El Ingenuo con Memoria):** Implacable en Retail y Energía. *El consumo de este Martes a las 10:00 será exactamente el mismo que el Martes pasado a las 10:00.*
3.  **Holt-Winters:** Suavizado exponencial. Entiende que hay tendencia y estacionalidad, y le da más peso al pasado reciente que al pasado lejano.
4.  **ARIMA:** El clásico matemático puro.

---

# La Prueba del Algodón: Análisis de Residuos

Comparamos nuestros 4 baselines en el bloque de **Validación**.
Supongamos que el *Seasonal Naive* gana (suele pasar).

Ahora miramos sus **Residuos (Errores = Predicción - Real)**:
*   Si la gráfica del residuo parece **Ruido Blanco** (caos total): ¡Enhorabuena! El baseline es tan bueno que no hace falta Machine Learning.
*   Si el residuo tiene **ondas o patrones claros**: El baseline es ciego a ciertos patrones. **Aquí es donde el Machine Learning nos salvará.**

---

# Backtesting e Incertidumbre

Un solo corte temporal puede engañar.

*   Evaluar en varios cortes consecutivos.
*   Comprobar estabilidad del MAE.
*   Usar residuos para un primer rango empírico de error.

**Regla:** una predicción puntual sin rango puede dar falsa seguridad.

---

# 🚀 A Construir la Base

Abre el notebook `04_baselines_evaluacion_forecasting.ipynb`

**Misiones:**
1. Separar temporalmente el dataset sin hacer trampa.
2. Construir los baselines y enfrentar `Naive` vs `Seasonal Naive`.
3. Detectar qué métrica delata los "picos de error" (RMSE).
4. Probar backtesting y un intervalo empírico con residuos.
