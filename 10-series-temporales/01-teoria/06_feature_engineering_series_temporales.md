# Feature Engineering para Forecasting de Series Temporales

## Sesión 6: El Arte de exprimir el tiempo sin hacer trampas

En la sesión anterior logramos que un Random Forest "viera" el tiempo gracias a los *lags* (retrasos). Sin embargo, un modelo de Machine Learning es como un cocinero: por muy bueno que sea el chef (el algoritmo), si los ingredientes (las variables) son mediocres, el plato (la predicción) no ganará ninguna estrella Michelin.

El **Feature Engineering** (Ingeniería de Características) es el proceso artesanal de fabricar los mejores ingredientes. Es donde el Data Scientist demuestra si realmente entiende el negocio. ¿Importa más la temperatura de ayer o la temperatura media de la última semana? ¿Cómo le explicamos a un algoritmo que las 23:59 está temporalmente "pegado" a las 00:01, a pesar de que matemáticamente 23 y 0 están muy lejos?

En esta sesión convertiremos la intuición humana en variables matemáticas avanzadas que dispararán la precisión de tus modelos.

---

## Objetivos

Al terminar esta sesión deberías ser capaz de:

- **Dominar el Horizonte:** Entender cómo cambia la construcción de variables si predices a 1 hora vs a 24 horas vista.
- **Crear Resúmenes Móviles:** Usar ventanas móviles (`rolling`) para atrapar la variabilidad reciente.
- **Entender el Olvido Exponencial (EWMA):** Implementar medias móviles que prestan más atención a lo que pasó ayer que a lo que pasó hace un mes.
- **Cerrar el Círculo (Variables Cíclicas):** Transformar horas y días usando Trigonometría (seno/coseno) para evitar saltos artificiales.
- **Modelar Sinfonías (Fourier):** Construir patrones estacionales súper complejos usando ondas armónicas.

## Requisitos técnicos

Usaremos las librerías habituales.

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

Importaciones principales:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
```

Dataset principal:

```python
df = pd.read_csv("datos/consumo_con_eventos.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").asfreq("h")
```

---

## 1. El Horizonte de Predicción dicta las reglas

Antes de crear ni una sola variable, debes tatuarte a fuego esta pregunta: **¿A cuánto tiempo vista estoy prediciendo?**

- **Horizonte = 1 (La próxima hora):** Tienes acceso al Lag_1.
- **Horizonte = 24 (La misma hora de mañana):** **¡No tienes acceso al Lag_1!** Si a las 10:00 AM del lunes quieres predecir las 10:00 AM del martes, el valor de las 09:00 AM del martes es el futuro desconocido. Tu `Lag` más cercano utilizable es el `Lag_24`.

Para dejarlo claro, siempre desplazamos nuestro objetivo (Target) hacia el futuro:

```python
horizonte = 1
# Queremos que la X actual apunte a la Y del futuro
df["y"] = df["consumo_kwh"].shift(-horizonte)
```

### 1.1 Multi-horizonte: no todo es predecir el siguiente paso

En muchos proyectos no queremos solo `t+1`, sino varios futuros: las próximas 6, 12 o 24 horas. Hay tres estrategias habituales:

- **Recursive:** entrenas un modelo a 1 paso y reutilizas sus propias predicciones como entrada. Es simple, pero acumula error.
- **Direct:** entrenas un modelo distinto para cada horizonte (`t+1`, `t+6`, `t+24`). Es más robusto, pero cuesta más mantenerlo.
- **Multi-output:** entrenas un único modelo que devuelve varios horizontes a la vez. Es cómodo si el algoritmo lo soporta.

```python
horizontes = [1, 6, 24]

for h in horizontes:
    df[f"y_t+{h}"] = df["consumo_kwh"].shift(-h)

df[["consumo_kwh", "y_t+1", "y_t+6", "y_t+24"]].tail()
```

La regla de fuga de información se vuelve más estricta: si predices `t+24`, ninguna feature puede depender de valores entre `t+1` y `t+23`.

---

## 2. Ventanas Móviles (Atrapando la tendencia reciente)

Los lags individuales (`lag_1`, `lag_24`) son útiles, pero a veces son ruidosos. Imagina que ayer hubo un pequeño pico anómalo de consumo. Si el modelo solo mira el `lag_24`, pensará que hoy habrá otro pico. 

Es mejor darle al modelo "resúmenes" estables, como la media de las últimas 24 horas.

```python
# CUIDADO: El shift(1) es sagrado para evitar Data Leakage
serie_pasada = df["consumo_kwh"].shift(1)

df["media_24h"] = serie_pasada.rolling(24).mean()
df["max_24h"] = serie_pasada.rolling(24).max()
df["min_24h"] = serie_pasada.rolling(24).min()
df["volatilidad_24h"] = serie_pasada.rolling(24).std()
```

Estas variables responden a preguntas humanas:
- ¿Viene la serie subiendo en general? (`media_24h`)
- ¿Estamos en un momento de caos absoluto o de calma? (`volatilidad_24h`)

---

## 3. EWMA (Exponentially Weighted Moving Average)

La media móvil normal de 24h es "tonta": el dato de hace 24 horas pesa exactamente lo mismo en la media que el dato de hace 1 hora. En el mundo real, la memoria humana y la económica se desvanecen. Lo que pasó hace 1 hora es muchísimo más relevante que lo que pasó ayer.

La **Media Móvil Exponencial** soluciona esto dando más peso al presente y un peso que decae exponencialmente hacia el pasado.

```python
# Span=24 significa que el "centro de gravedad" de la media ponderada recae sobre las últimas 24 observaciones
df["ewma_24h"] = serie_pasada.ewm(span=24, adjust=False).mean()
df["ewma_7d"] = serie_pasada.ewm(span=24 * 7, adjust=False).mean()
```

*Los modelos avanzados adoran las variables EWMA porque representan una "memoria suave y realista" del sistema.*

---

## 4. Trigonometría Temporal (El truco del Seno y Coseno)

Si le das a un modelo de regresión (o a una Red Neuronal) la hora del día como un número entero del `0` al `23`, el modelo asumirá que matemáticamente hay una distancia gigantesca entre las 23:00 de la noche y las 00:00 de la madrugada. ¡Falso! Están a un minuto de distancia.

Para evitar esta ruptura de la realidad, proyectamos el tiempo en un reloj circular usando seno y coseno.

```python
# Mapeamos la hora en un círculo de 24 horas
df["hora_sin"] = np.sin(2 * np.pi * df.index.hour / 24)
df["hora_cos"] = np.cos(2 * np.pi * df.index.hour / 24)

# Mapeamos la semana en un círculo de 7 días
df["dia_semana_sin"] = np.sin(2 * np.pi * df.index.dayofweek / 7)
df["dia_semana_cos"] = np.cos(2 * np.pi * df.index.dayofweek / 7)
```

Al pasarle estas dos coordenadas al modelo, hemos "cerrado el círculo" temporal y eliminado el salto brusco de fin de ciclo.

---

## 5. Modelando Sinfonías: Términos de Fourier

A veces una estacionalidad es tan compleja que un par de variables categóricas o cíclicas no bastan. Jean-Baptiste Joseph Fourier demostró en 1822 que **cualquier señal repetitiva (por extraña que sea) puede ser replicada sumando muchas ondas senoidales simples**.

Podemos inyectar estos "armónicos" a nuestro DataFrame para que un modelo lineal (o de árboles) capte patrones ultra-precisos de estacionalidad sin tener que aprenderlos de cero.

```python
def crear_fourier(index, periodo, orden):
    t = np.arange(len(index))
    features = pd.DataFrame(index=index)

    for k in range(1, orden + 1):
        features[f"sin_{periodo}_orden{k}"] = np.sin(2 * np.pi * k * t / periodo)
        features[f"cos_{periodo}_orden{k}"] = np.cos(2 * np.pi * k * t / periodo)

    return features

# Creamos una señal de Fourier para el ciclo diario (periodo=24) con un detalle de orden 3
fourier_diario = crear_fourier(df.index, periodo=24, orden=3)
df = pd.concat([df, fourier_diario], axis=1)
```

- **Orden bajo (Ej: 1):** Dibuja una onda suave general (Día/Noche).
- **Orden alto (Ej: 5):** Permite replicar los "picos" exactos de la hora de la cena y el desayuno. ¡Cuidado con poner órdenes muy altos porque generarás sobreajuste (overfitting)!

---

## 6. Ensamblaje Final y Evaluación del Impacto

La gran pregunta del Feature Engineering es: **¿De verdad sirven para algo todas estas nuevas columnas complejas?** 

La única forma de saberlo es enfrentar a tu modelo base contra tu modelo enriquecido.

```python
# Limpiamos los NaNs creados por los Lags
datos_completos = df.dropna()

# Definimos tres niveles de "Cocinero"
features_basicas = ["hora_sin", "hora_cos", "dia_semana_sin", "dia_semana_cos"]
features_medias = features_basicas + ["media_24h", "ewma_24h", "volatilidad_24h"]
# Asumimos que ya hemos hecho los lags 1, 24, 168 en el DataFrame
columnas_objetivo = ["consumo_kwh", "y"] + [col for col in datos_completos.columns if col.startswith("y_t+")]
features_todas = [col for col in datos_completos.columns if col not in columnas_objetivo + ["timestamp"]]

def evaluar_conjunto(features_a_usar):
    X = datos_completos[features_a_usar]
    y = datos_completos["y"]
    
    fin_train = int(len(X) * 0.8)
    X_train, y_train = X.iloc[:fin_train], y.iloc[:fin_train]
    X_val, y_val = X.iloc[fin_train:], y.iloc[fin_train:]
    
    modelo = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)
    return mean_absolute_error(y_val, modelo.predict(X_val))

print("MAE solo con Reloj:", evaluar_conjunto(features_basicas))
print("MAE con Medias Móviles y EWMA:", evaluar_conjunto(features_medias))
print("MAE con Todas (Lags + Fourier + EWMA):", evaluar_conjunto(features_todas))
```

> **Pregunta para discutir:** Si ves que al pasar de `features_medias` a `features_todas` el error (MAE) **aumenta** en lugar de disminuir, ¿qué fenómeno del Machine Learning está ocurriendo y por qué haber metido tantas variables fue mala idea?

---

## 7. Actividades de clase

### Actividad 1: El poder del olvido
Calcula y grafica en una misma ventana (para una semana de datos) la variable `media_24h` y la variable `ewma_24h`. Observa cómo la media normal es un "bloque" torpe que tarda en reaccionar a los cambios, mientras que el EWMA se adapta de forma orgánica y fluida a los picos de demanda.

### Actividad 2: Reconstruyendo el reloj
Dibuja un gráfico de dispersión (`scatter plot`) donde el eje X sea `hora_sin` y el eje Y sea `hora_cos`. Si lo has hecho bien, no verás una línea ni una nube de puntos, verás un círculo perfecto. Estás viendo la forma en que los algoritmos percibirán el transcurso del día a partir de ahora.

### Actividad 3: La paradoja del Horizonte
Cambia el horizonte de predicción a `horizonte = 24`. Rehaz todo el Feature Engineering. Si no borras el `lag_1` ni las `medias_24h` construidas con `shift(1)`, estarás cometiendo Data Leakage masivo (porque no puedes saber lo que pasó hace una hora si estás prediciendo a 24 horas vista). Adapta el `shift` de todas tus variables de agregación para que sean legales en Horizonte 24. 

---

## 8. Ideas clave

- **Las Variables determinan el techo:** Puedes usar el algoritmo de Google más potente, que si tus features son malas, perderás contra una regresión lineal con features brillantes.
- **EWMA > Media Simple:** Las variables con olvido exponencial son representaciones mucho más naturales de la realidad humana y económica.
- **Ciclos vs Escalones:** Usar Seno y Coseno para transformar variables temporales discretas (hora, mes) evita que los modelos interpreten "cortes" falsos al final del día o del año.
- **La Maldición de la Dimensionalidad:** Meter 500 términos de Fourier y 300 variables Lags no hace a tu modelo más listo, lo hace propenso a memorizar el ruido (Overfitting). Solo crea las features que tengan sentido físico y de negocio.

## Continuación

¡Felicidades! Tienes en tus manos el arsenal completo del Feature Engineering temporal. Estás listo para enfrentarte a la realidad pura y dura. En las sesiones finales, dejaremos de jugar con una sola serie temporal local, para escalar a **Modelos Globales**, donde predeciremos simultáneamente cientos de series distintas usando el mismo modelo único. El auténtico reto del Big Data.
