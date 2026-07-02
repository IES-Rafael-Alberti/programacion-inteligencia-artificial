---
title: "Métricas para regresión"
output: pdf_document
date: "2025-03-12"
---

# Guía Exhaustiva de Métricas para Modelos de Regresión

En problemas de regresión, el objetivo es predecir valores continuos. Para evaluar el rendimiento de un modelo de regresión, es crucial utilizar métricas adecuadas que midan la precisión de las predicciones. Esta guía cubre las métricas más comunes para regresión, su implementación en Python (usando bibliotecas como Scikit-learn y TensorFlow/Keras), y cuándo usarlas.

---

## 1. **Métricas Comunes para Regresión**

### 1.1. **Error Cuadrático Medio (MSE - Mean Squared Error)**
Mide el promedio de los errores al cuadrado entre los valores reales y los predichos. Es sensible a valores atípicos (outliers).

**Fórmula**:
\[
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
\]

**Implementación**:
```python
from sklearn.metrics import mean_squared_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mse = mean_squared_error(y_true, y_pred)
print(f"MSE: {mse}")  # Salida: 0.375
```

---

### 1.2. **Raíz del Error Cuadrático Medio (RMSE - Root Mean Squared Error)**
Es la raíz cuadrada del MSE. Tiene las mismas unidades que la variable objetivo, lo que facilita su interpretación.

**Fórmula**:
\[
\text{RMSE} = \sqrt{\text{MSE}}
\]

**Implementación**:
```python
import numpy as np
from sklearn.metrics import mean_squared_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
print(f"RMSE: {rmse}")  # Salida: 0.612
```

---

### 1.3. **Error Absoluto Medio (MAE - Mean Absolute Error)**
Mide el promedio de los errores absolutos entre los valores reales y los predichos. Es menos sensible a valores atípicos que el MSE.

**Fórmula**:
\[
\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
\]

**Implementación**:
```python
from sklearn.metrics import mean_absolute_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mae = mean_absolute_error(y_true, y_pred)
print(f"MAE: {mae}")  # Salida: 0.5
```

---

### 1.4. **Coeficiente de Determinación (R² - R-Squared)**
Mide la proporción de la varianza en la variable dependiente que es predecible a partir de las variables independientes. Un valor de 1 indica un ajuste perfecto.

**Fórmula**:
\[
R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}
\]

**Implementación**:
```python
from sklearn.metrics import r2_score

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
r2 = r2_score(y_true, y_pred)
print(f"R²: {r2}")  # Salida: 0.948
```

---

### 1.5. **Error Absoluto Medio Porcentual (MAPE - Mean Absolute Percentage Error)**
Mide el error porcentual promedio entre los valores reales y los predichos. Útil cuando el error relativo es más importante que el absoluto.

**Fórmula**:
\[
\text{MAPE} = \frac{100\%}{n} \sum_{i=1}^n \left| \frac{y_i - \hat{y}_i}{y_i} \right|
\]

**Implementación**:
```python
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mape = mean_absolute_percentage_error(y_true, y_pred)
print(f"MAPE: {mape}")  # Salida: 33.33
```

---

### 1.6. **Error Logarítmico Medio (MSLE - Mean Squared Logarithmic Error)**
Mide el error cuadrático medio en la escala logarítmica. Útil cuando los valores objetivo tienen un rango amplio.

**Fórmula**:
\[
\text{MSLE} = \frac{1}{n} \sum_{i=1}^n (\log(1 + y_i) - \log(1 + \hat{y}_i))^2
\]

**Implementación**:
```python
from sklearn.metrics import mean_squared_log_error

y_true = [3, 5, 2.5, 7]
y_pred = [2.5, 5, 4, 8]
msle = mean_squared_log_error(y_true, y_pred)
print(f"MSLE: {msle}")  # Salida: 0.0397
```

---

## 2. **Métricas en Keras para Regresión**

Keras proporciona métricas integradas para regresión, como `MeanSquaredError`, `MeanAbsoluteError`, y `MeanSquaredLogarithmicError`.

**Ejemplo**:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import MeanSquaredError, MeanAbsoluteError

# Crear modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1)  # Capa de salida para regresión
])

# Compilar modelo con métricas
model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=[MeanSquaredError(), MeanAbsoluteError()])

# Entrenar modelo
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
```

---

## 3. **Cuándo Usar Cada Métrica**

1. **MSE/RMSE**:
   - Útil cuando los errores grandes son más significativos.
   - Sensible a valores atípicos.

2. **MAE**:
   - Útil cuando todos los errores tienen la misma importancia.
   - Menos sensible a valores atípicos.

3. **R²**:
   - Útil para comparar modelos en términos de varianza explicada.
   - No indica la magnitud del error.

4. **MAPE**:
   - Útil cuando el error relativo es más importante que el absoluto.
   - No funciona con valores reales iguales a cero.

5. **MSLE**:
   - Útil cuando los valores objetivo tienen un rango amplio.
   - Penaliza menos los errores en valores grandes.

---

## 4. **Métricas Personalizadas en Keras**

Si necesitas una métrica específica, puedes crear una métrica personalizada subclasificando `tf.keras.metrics.Metric`.

**Ejemplo: Error Absoluto Medio Porcentual (MAPE)**:
```python
import tensorflow as tf

class MeanAbsolutePercentageError(tf.keras.metrics.Metric):
    def __init__(self, name='mape', **kwargs):
        super(MeanAbsolutePercentageError, self).__init__(name=name, **kwargs)
        self.total_error = self.add_weight(name='total_error', initializer='zeros')
        self.total_samples = self.add_weight(name='total_samples', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_true = tf.cast(y_true, tf.float32)
        y_pred = tf.cast(y_pred, tf.float32)
        error = tf.abs((y_true - y_pred) / y_true)
        self.total_error.assign_add(tf.reduce_sum(error))
        self.total_samples.assign_add(tf.cast(tf.size(y_true), tf.float32))

    def result(self):
        return (self.total_error / self.total_samples) * 100.0

    def reset_states(self):
        self.total_error.assign(0.0)
        self.total_samples.assign(0.0)

# Uso
mape_metric = MeanAbsolutePercentageError()
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mape_metric.update_state(y_true, y_pred)
print(mape_metric.result().numpy())  # Salida: MAPE
```

---

## 5. **Conclusión**

Las métricas para modelos de regresión son esenciales para evaluar la precisión de las predicciones. Dependiendo del problema, puedes elegir entre MSE, RMSE, MAE, R², MAPE, MSLE, o incluso crear métricas personalizadas. Keras y Scikit-learn proporcionan herramientas poderosas para calcular estas métricas de manera eficiente.