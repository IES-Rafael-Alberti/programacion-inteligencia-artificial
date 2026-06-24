# Análisis y Visualización de Series Temporales

## Sesión 3: Escuchar a los datos antes de modelar

En la sesión anterior aprendimos a moldear, limpiar y estructurar nuestros datos en el formato temporal correcto. Ahora que tenemos un conjunto de datos robusto, es tentador saltar directamente a aplicar modelos predictivos de Machine Learning. **Esto es un error grave.** 

Antes de predecir el futuro, debemos comprender profundamente el pasado. Una serie temporal cuenta una historia: tiene ciclos repetitivos, movimientos tectónicos a largo plazo (tendencia) y ocasionalmente, sufre de sobresaltos inexplicables (outliers). Si no visualizas y analizas estos componentes, intentarás modelar un "eco" sin entender quién originó el sonido.

---

## Objetivos

Al terminar esta sesión deberías ser capaz de:

- Entender que visualizar no es solo "hacer gráficos bonitos", sino una herramienta de diagnóstico crítica en series temporales.
- Identificar y diferenciar conceptualmente los componentes de una serie: tendencia, estacionalidad, ciclo y ruido (residuo).
- Interpretar gráficos estacionales, boxplots temporales y mapas de calor para detectar patrones de negocio.
- Usar la Autocorrelación (ACF) para entender la "memoria" matemática de la serie (el eco temporal).
- Descomponer matemáticamente la señal usando métodos clásicos y avanzados (STL).
- Detectar valores atípicos (outliers) y, lo más importante, decidir filosóficamente si deben eliminarse o conservarse.

## Requisitos técnicos

Usaremos las herramientas estándar y añadiremos librerías estadísticas especializadas:

```bash
pip install numpy pandas matplotlib seaborn statsmodels scikit-learn
```

Importaciones habituales:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.seasonal import seasonal_decompose, STL
from sklearn.ensemble import IsolationForest
```

---

## 1. La anatomía de una serie temporal

Casi todas las series temporales del mundo real (ventas, temperatura, tráfico web) pueden entenderse como una suma matemática de distintas "fuerzas". Imagina que vas en un barco:
- **Tendencia (Trend):** Es la corriente del océano. Te mueve inexorablemente a largo plazo en una dirección.
- **Estacionalidad (Seasonality):** Son las mareas. Suben y bajan con una frecuencia matemática exacta y repetitiva (cada 12 horas, cada 7 días).
- **Ciclo (Cycle):** Son tormentas que duran años, como las crisis económicas. No tienen un periodo fijo (no ocurren exactamente cada X meses).
- **Componente Irregular (Ruido / Residuo):** Es el oleaje caótico contra el barco. Son las variaciones diarias que no podemos explicar con lo anterior.

```text
serie = tendencia + estacionalidad + ciclo + residuo
```

---

## 2. Visualización: Nuestro primer diagnóstico

Cargamos un conjunto de datos básico de consumo eléctrico (sin huecos, para no complicarnos).

```python
df = pd.read_csv("datos/consumo_basico.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").asfreq("h")
```

Si simplemente trazamos un gráfico de líneas (`df.plot()`), a menudo solo veremos una mancha densa de tinta. Para diagnosticar correctamente, debemos cambiar de perspectiva (zoom in / zoom out) y usar gráficos agregados.

### 2.1 Encontrar patrones estacionales ocultos

En lugar de ver la línea continua, agregamos los datos para buscar comportamientos humanos. Por ejemplo, agrupando por día de la semana.

```python
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
perfil_dia = df.groupby(df.index.dayofweek)["consumo_kwh"].mean()

sns.barplot(x=dias, y=perfil_dia.values, color="tab:blue")
plt.title("Media por día de semana")
plt.show()
```

Verás claramente que el consumo industrial/humano cae en fin de semana. Esto es la **estacionalidad semanal**.

### 2.2 Boxplots temporales: Detectando varianza

La media es mentirosa. Puede que los Lunes tengan la misma media de consumo que los Jueves, pero los Lunes podrían tener picos altísimos y valles profundos, mientras que los Jueves son muy estables. El Boxplot (diagrama de caja) nos permite ver la distribución completa de cada periodo temporal.

```python
df_plot = df.copy()
df_plot["hora"] = df_plot.index.hour

sns.boxplot(data=df_plot, x="hora", y="consumo_kwh", color="lightblue")
plt.title("Distribución de consumo por hora")
plt.show()
```

> **Pregunta para discutir:** Si observas que el boxplot de la hora 18:00 es mucho más "largo" (mayor rango intercuartílico) que el de la hora 03:00, ¿qué significa esto para la incertidumbre de nuestro futuro modelo predictivo a esa hora?

---

## 3. Autocorrelación: El "Eco" Matemático

El concepto más contraintuitivo de las series temporales es la **Autocorrelación**.
En el Machine Learning clásico, predecimos el precio de una casa ($Y$) mirando el número de habitaciones ($X_1$) y los metros cuadrados ($X_2$). 
En Series Temporales, **usamos el pasado de la variable para predecir su propio futuro**.

La autocorrelación mide: ¿cuánto se parece el valor de hoy ($Y_t$) al valor de ayer ($Y_{t-1}$)? ¿Y al de hace 7 días ($Y_{t-7}$)? 
Este salto hacia atrás en el tiempo se llama **Lag** (retraso).

```python
# Analizamos la autocorrelación hasta 192 horas (8 días) hacia atrás
fig, ax = plt.subplots(figsize=(12, 4))
plot_acf(df["consumo_kwh"], lags=24 * 8, ax=ax)
plt.show()
```

**¿Cómo se lee un gráfico ACF (Autocorrelation Function)?**
- El eje X es el Lag (cuántos pasos hacia atrás miramos).
- El eje Y (de -1 a 1) indica la fuerza matemática de la correlación.
- Si ves que el gráfico hace picos altos cada 24 horas, significa que la serie tiene una estacionalidad diaria violenta. El dato de hoy a las 14:00 es muy útil para predecir el dato de mañana a las 14:00.

---

## 4. Descomponiendo la señal (Matemáticamente)

Sabiendo que existe tendencia y estacionalidad, podemos pedirle a un algoritmo estadístico que separe nuestra serie en sus piezas fundacionales.

### 4.1 Descomposición Clásica

Usa medias móviles simples para extraer la tendencia, y luego promedia las desviaciones sobre esa tendencia para extraer la estacionalidad estática.

```python
# Usamos un periodo de 24 horas
descomposicion = seasonal_decompose(df["consumo_kwh"], model="additive", period=24)
descomposicion.plot()
plt.show()
```

### 4.2 Descomposición STL (Seasonal and Trend decomposition using LOESS)

El problema de la clásica es que asume que la estacionalidad es estática a lo largo de los años. STL es un algoritmo mucho más avanzado que permite que la estacionalidad mute con el tiempo, y es súper robusto contra outliers. Es el estándar actual de la industria.

```python
stl = STL(df["consumo_kwh"], period=24)
resultado_stl = stl.fit()
resultado_stl.plot()
plt.show()
```

Fíjate especialmente en el gráfico de abajo (el "Residuo"). Si este gráfico parece ruido de televisión totalmente blanco y sin patrones geométricos, ¡enhorabuena! Has capturado perfectamente toda la inteligencia temporal en la tendencia y estacionalidad.

---

## 5. Detección de "Cisnes Negros": Outliers en el Tiempo

Un *outlier* es un valor atípico. Pero en el tiempo, el concepto es engañoso. 
Un consumo de 5.000 kWh en Agosto puede ser la norma (por el aire acondicionado), pero en Abril sería un outlier masivo. Por tanto, **detectar outliers en la serie original es peligroso**; es mejor detectarlos sobre el *Residuo* de la descomposición de STL, porque el residuo ya no tiene estacionalidad temporal.

Carguemos unos datos con anomalías:

```python
df_out = pd.read_csv("datos/consumo_realista.csv")
df_out["timestamp"] = pd.to_datetime(df_out["timestamp"])
df_out = df_out.set_index("timestamp").asfreq("h")
```

Podemos usar algoritmos de ML no supervisado como **Isolation Forest**, que aísla puntos que son fundamentalmente extraños dado un contexto (como la hora y el día de la semana).

```python
variables = df_out[["consumo_kwh", "hora", "dia_semana", "mes"]].dropna()
modelo = IsolationForest(contamination=0.01, random_state=42)

df_out["outlier"] = False
df_out.loc[variables.index, "outlier"] = modelo.fit_predict(variables) == -1
```

### 5.1 El Dilema del Outlier: ¿Borrar o No Borrar?

El impulso inicial del científico de datos principiante es eliminar o interpolar todos los outliers para que la línea quede bonita. **No lo hagas sin pensar.**

1. **Error de Sistema:** El sensor se rompió y envió un -999. **Decisión:** Interpolar (Eliminar y rellenar).
2. **Evento Real Excepcional:** Cayó una tormenta de nieve histórica y el consumo se disparó. Si lo borras, tu modelo nunca aprenderá a predecir picos bajo estrés climático. **Decisión:** Conservarlo, pero crear una variable externa booleana llamada `ola_de_frio=1` para explicarle al modelo por qué subió tanto la demanda.

> **Pregunta para discutir:** Durante los confinamientos de 2020 por la pandemia, la demanda de tráfico aéreo se volvió cercana a 0, rompiendo todos los modelos predictivos del mundo. Si hoy en 2026 vas a predecir la demanda de 2027, ¿entrenarías a tu modelo con los datos "outliers" de 2020 o los eliminarías de la historia?

---

## 6. Actividades de clase

### Actividad 1: El pulso oculto de la autocorrelación
Carga el `consumo_basico.csv`. Dibuja el gráfico ACF con un `lags` de 720 horas (30 días). Verás un patrón complejo. 
Describe verbalmente la estacionalidad principal (el pico más grande) y las sub-estacionalidades. 

### Actividad 2: Descomposición STL al límite
Cambia el parámetro `period` en la descomposición STL de 24 a 168 (horas en una semana). ¿Qué ocurre con la gráfica del Residuo en comparación a cuando era 24? ¿Es mejor modelo uno que absorbe los patrones de fin de semana en la Estacionalidad o el que los deja en el Residuo?

### Actividad 3: El veredicto sobre los Outliers
Toma el dataset `consumo_realista.csv`. Extrae los 5 días que el Isolation Forest marque como la máxima concentración de outliers. Revisa las noticias (o imagina un contexto) e indica si aplicarías una interpolación destructiva o añadirías una "feature" booleana de evento externo (como festivo nacional, partido del mundial, etc.).

---

## 7. Ideas clave

- **Visualiza siempre:** Los números no sienten el contexto. Mirar la gráfica, sus boxplots temporales y los mapas de calor ahorran semanas de mal modelado algorítmico.
- **La memoria está en el Lag:** El ACF nos demuestra matemáticamente que la serie "recuerda" el pasado, y es esta memoria lo que intentaremos exprimir con modelos predictivos.
- **El residuo es el juez:** Una buena descomposición estacional (STL) deja un residuo en el que ya no puedes predecir nada (ruido blanco).
- **Los Outliers son información pura:** A veces el outlier es un error técnico que hay que limpiar, pero muchas otras veces, el outlier es el comportamiento extremo (Cisne Negro) que precisamente tu empresa te está pagando para anticipar.

## Continuación

Una vez limpios, entendidos, descompuestos y mapeados nuestros datos, por fin estamos listos para modelar. En la próxima sesión aprenderemos sobre el ciclo de vida del **Forecasting**: cómo dividir temporalmente los datos sin hacer trampas (sin mirar al futuro), baselines fundamentales (Naive, Seasonal Naive) y cómo medir matemáticamente el éxito de nuestras predicciones (MAE, RMSE, MAPE).
