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
    border-bottom: 3px solid #e74c3c;
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

# Feature Engineering
## Taller de Forecasting Práctico con Python

**Sesión 06**
El arte de exprimir el tiempo sin hacer trampas.

---

# El Chef y los Ingredientes

En la sesión anterior usamos un Random Forest.
Un algoritmo de Machine Learning es como un cocinero: por muy bueno que sea el Chef (Random Forest), si los ingredientes (las variables) son mediocres, el plato será mediocre.

El **Feature Engineering** es el arte de fabricar ingredientes gourmet a partir de datos crudos. Es donde demuestras si de verdad entiendes el negocio.

---

# 1. El Horizonte Dicta las Reglas

Tu primera pregunta siempre debe ser: **¿A cuánto tiempo vista estoy prediciendo?**

*   **Horizonte = 1 hora:** Tienes acceso al `Lag_1` (hace 1 hora).
*   **Horizonte = 24 horas:** **¡NO tienes acceso al Lag_1!** El valor de las próximas 23 horas es futuro desconocido. Tu Lag más cercano utilizable es el `Lag_24`.

*No adaptar tus lags al horizonte es la forma más común de fracasar en producción.*

---

# 2. Ventanas Móviles (Resumiendo el caos)

Un Lag individual es ruidoso. Si ayer hubo un pico anómalo, el `Lag_24` asustará a tu modelo.
Le damos "resúmenes" estables de las últimas 24 horas:

```python
# shift(1) es sagrado para NO incluir el futuro
serie_pasada = df["consumo"].shift(1)

df["media_24h"] = serie_pasada.rolling(24).mean()
df["volatilidad_24h"] = serie_pasada.rolling(24).std()
```

Responden a: *¿Viene la serie subiendo? ¿Estamos en un momento caótico?*

---

# 3. EWMA (El Poder del Olvido)

La media normal es "tonta": el dato de hace 24h pesa lo mismo que el dato de hace 1h.
En la vida real, **la memoria se desvanece**. Lo que pasó hace 1 hora es más importante que lo de ayer.

**Media Móvil Exponencial (EWMA):**
Pondera más el presente y decae exponencialmente hacia el pasado.

```python
# Memoria suave y realista
df["ewma_24h"] = serie_pasada.ewm(span=24).mean()
```

---

# 4. Trigonometría Temporal

Si al modelo le das la hora del día del `0` al `23`, el modelo pensará que hay una distancia enorme entre las `23:59` y las `00:01`.

**Proyectamos el tiempo en un círculo (Seno y Coseno):**
```python
df["hora_sin"] = np.sin(2 * np.pi * df.index.hour / 24)
df["hora_cos"] = np.cos(2 * np.pi * df.index.hour / 24)
```
Al graficar esto, verás un círculo perfecto. Hemos eliminado matemáticamente el "salto de medianoche".

---

# 5. Sinfonías de Fourier

Si la estacionalidad es hiper-compleja, transformamos el tiempo usando la matemática de Fourier.
*Cualquier señal repetitiva se puede replicar sumando muchas ondas senoidales simples.*

Con unas pocas líneas, generamos ondas perfectas (`orden 1`, `orden 2`...) que el modelo Lineal o el Árbol pueden usar para entender exactamente la forma del ciclo diario o anual.

*(Ojo con meter órdenes muy altos o causarás Overfitting).*

---

# Forecast Multi-Horizonte

No siempre predecimos solo `t+1`.

*   Recursive: un modelo a 1 paso reutilizado.
*   Direct: un modelo por horizonte.
*   Multi-output: un modelo devuelve varios futuros.

Cuanto más lejano el horizonte, más estricta la prevención del leakage.

---

# 🚀 ¡A Cocinar Features!

Abre el notebook `06_feature_engineering_series_temporales.ipynb`

**Misiones:**
1. Graficar Media Simple vs EWMA y ver la "fluidez".
2. Dibujar el círculo trigonométrico de las horas.
3. Evaluar el MAE final y descubrir si de verdad ha servido de algo añadir toda esta matemática.
4. Comparar cómo cambian las features legales para horizonte 1 y 24.
