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
    border-bottom: 3px solid #f1c40f;
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

# Forecasting como Regresión
## Taller de Forecasting Práctico con Python

**Sesión 05**
Machine Learning: Cruzando de 1D a 2D.

---

# El Problema de los Árboles

Modelos potentes como **Random Forest** o **XGBoost** no entienden el tiempo.
Para ellos, el tiempo no fluye; solo ven filas y columnas independientes.

**Nuestro trabajo:** Transformar una serie temporal pura (1D) en una tabla típica de Machine Learning Supervisado (2D).

*Tenemos que inyectarle "memoria" a las columnas.*

---

# El Gran Truco: Supervisión Artificial

Queremos predecir el Target ($y$). Creamos "Features temporales" ($X$) usando fotografías del pasado:

**Antes (Serie pura):**
```text
timestamp          consumo
10:00              1.85
11:00              1.66
```

**Después (Tabla ML):**
```text
timestamp    consumo_hora_anterior (X1)   hora (X2)  |   y (Target)
11:00        1.85                         11             1.66
```

Ahora cada fila es independiente. El modelo aprenderá reglas como: *"Si la hora es 11 y el consumo anterior fue 1.85, predice 1.66"*.

---

# Time Delay Embedding (El poder del Lag)

Usamos la función `.shift()` para desplazar los datos hacia abajo.

```python
df["lag_1"] = df["consumo_kwh"].shift(1)       # Hace 1 hora
df["lag_24"] = df["consumo_kwh"].shift(24)     # Hace 1 día
df["lag_168"] = df["consumo_kwh"].shift(24*7)  # Hace 1 semana
```

**¿Cómo elegimos qué lags usar?**
No se eligen al azar. Miramos el gráfico de Autocorrelación (ACF) de la Sesión 3 y escogemos los picos matemáticamente más fuertes.

---

# El Mayor Pecado: Fuga de Información

La Fuga de Información (*Data Leakage*) ocurre cuando le das al modelo información que **sería imposible conocer** el día de mañana.

*Ejemplo: El código que te despedirá.*
Quieres incluir la media de las últimas 24 horas:

```python
# MAL: La media móvil INCLUYE el valor de hoy que intentas predecir
df["media_24h"] = df["consumo"].rolling(24).mean()
```
```python
# BIEN: Primero mueves el pasado 1 paso, y luego calculas
df["media_24h"] = df["consumo"].shift(1).rolling(24).mean()
```

---

# El Duelo: Baseline vs Machine Learning

Una vez armada nuestra tabla con `Lags`, `Medias Móviles seguras` y `Contexto de Calendario` (hora, día de la semana), entrenamos un **Random Forest**.

**¿Por qué un Random Forest?**
Porque a diferencia del Baseline, el bosque puede hacer razonamientos complejos:
*"Si es domingo por la tarde, y el Lag_1 es alto, pero la media 24h es baja, entonces la demanda caerá."*

Al final, comparamos el MAE de nuestro Random Forest contra el implacable *Seasonal Naive*.

---

# Mirando en la Caja Negra

El Random Forest nos regala la métrica **Feature Importance**.

Nos dice en qué variables se fijó más para tomar sus decisiones.
Si el `lag_168` (lo que pasó hace 7 días) sale como la barra más grande del gráfico, el modelo ha "descubierto" la estacionalidad semanal del consumo eléctrico de forma 100% automática.

---

# Extensión Tabular Fuerte

`HistGradientBoostingRegressor`

*   Incluido en `scikit-learn`.
*   Competitivo en datos tabulares.
*   Sin dependencias extra.

Nota avanzada: XGBoost, LightGBM y CatBoost son potentes, pero requieren instalación aparte.

---

# 🚀 ¡A Entrenar Árboles!

Abre el notebook `05_forecasting_como_regresion.ipynb`

**Misiones:**
1. Crear variables `lag` de manera segura usando `.shift()`.
2. Provocar Fuga de Información (*Data Leakage*) a propósito para ver cómo el error baja mágicamente a cero.
3. Competir: Linear Regression vs Seasonal Naive vs Random Forest.
4. Añadir HistGradientBoosting como modelo tabular fuerte.
