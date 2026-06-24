# Baselines y Evaluación de Modelos de Forecasting

## Sesión 4: Construir una referencia sólida antes de usar modelos complejos

Existe un sesgo muy común en el Machine Learning moderno: creer que un problema solo se puede resolver con Deep Learning o algoritmos hiper-complejos como XGBoost. En forecasting, este sesgo es mortal. **Un modelo avanzado no es útil por ser avanzado, sino porque logra batir consistentemente a una referencia muy simple.**

Antes de entrenar arquitecturas complejas, necesitamos construir *Baselines* (líneas base). Un baseline es la respuesta de "sentido común" a tu problema de predicción. Si un equipo de ingenieros invierte meses en un modelo de Inteligencia Artificial que solo mejora un 1% frente a la estrategia de "predecir que mañana se venderá lo mismo que hoy", ese modelo no tiene valor de negocio.

En esta sesión aprenderemos a construir estos baselines implacables, a dividir el tiempo sin mirar al futuro (data leakage) y a juzgar nuestros errores con la severidad matemática adecuada.

---

## Objetivos

Al terminar esta sesión deberías ser capaz de:

- **Dividir el tiempo:** Crear conjuntos de entrenamiento, validación y test respetando la "flecha del tiempo", entendiendo por qué el `train_test_split` clásico arruina los modelos de forecasting.
- **Juzgar el error:** Elegir y comprender métricas de evaluación (MAE, RMSE, MAPE) y saber cuándo usar cada una según el coste del error en la vida real.
- **Implementar el "Sentido Común":** Construir predicciones baseline como *Naive* (ingenuo) y *Seasonal Naive*.
- **Comparar con justicia:** Evaluar múltiples modelos sobre exactamente la misma ventana temporal.
- **Diagnosticar la predecibilidad:** Analizar los residuos (errores) para saber si hemos extraído todo el "jugo" matemático de la serie o si aún quedan patrones ocultos.

## Requisitos técnicos

Usaremos las librerías habituales, incorporando algoritmos clásicos de `statsmodels` y métricas de `scikit-learn`.

```bash
pip install numpy pandas matplotlib scikit-learn statsmodels
```

Importaciones:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
```

Si estamos trabajando desde los notebooks del taller, también podremos usar el generador propio para tener una serie rica en matices:

```python
import sys
sys.path.append("src")

from series_temporales import generar_consumo_electrico
```

---

## 1. El escenario: Consumo eléctrico simulado

Para comparar modelos necesitamos un escenario justo. Generaremos una serie de consumo eléctrico que imite la realidad: con estacionalidad, meteorología y eventos.

```python
df = generar_consumo_electrico(
    fecha_inicio="2026-01-01",
    periodos=24 * 180,
    frecuencia="h",
    semilla=42,
    incluir_meteorologia=True,
    incluir_eventos=True,
)

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").asfreq("h")

serie = df["consumo_kwh"]
```

Si la visualizamos (`plt.plot(serie)`), veremos un patrón diario rítmico con fluctuaciones a lo largo de los meses.

---

## 2. El pecado capital: Cortar el tiempo aleatoriamente

En los problemas clásicos de Machine Learning (como clasificar imágenes de gatos y perros), mezclamos las imágenes aleatoriamente y guardamos el 20% para test. En forecasting, esto es **hacer trampas**. 

Si metes el dato del martes y del jueves en "entrenamiento", y le pides al modelo que prediga el dato del miércoles en "test", el modelo simplemente mirará hacia adelante y hacia atrás. **La regla de oro del forecasting es: nunca puedes entrenar con el futuro para predecir el pasado.**

La división correcta respeta la cronología:

- **Entrenamiento (Pasado Lejano):** Para que el modelo aprenda las reglas del juego. (Ej: primeros 120 días).
- **Validación (Pasado Reciente):** Para comparar baselines o ajustar "hiperparámetros" simulando que no conocemos el futuro. (Ej: siguientes 30 días).
- **Test (Futuro Desconocido):** La caja fuerte. Solo se usa **UNA VEZ** al final de todo el proyecto para reportar el error realista que el modelo tendría en producción. (Ej: últimos 30 días).

```python
# Un mes tiene aprox 30 días * 24 horas = 720 horas
train = serie.iloc[:24 * 120]
validacion = serie.iloc[24 * 120:24 * 150]
test = serie.iloc[24 * 150:]

print(f"Train: {len(train)}, Valid: {len(validacion)}, Test: {len(test)}")
```

> **Pregunta para discutir:** ¿Por qué necesitamos una ventana de "validación" separada de la de "test"? ¿Qué pasaría si probamos 10 modelos distintos directamente contra el bloque de "test" y elegimos el mejor?

---

## 3. ¿Cómo castigamos al modelo? (Métricas)

No hay una única métrica perfecta. Cada métrica cuenta una historia diferente sobre tus errores y debes elegirla dependiendo de **cuánto dinero pierdes por fallar en la vida real**.

### MAE (Mean Absolute Error)
Mide el error "promedio". Es muy intuitivo porque está en la misma unidad que lo que predices.
*Si predigo 100 kWh y el consumo real es 120 kWh, el error es 20.*
- **Cuándo usarlo:** Cuando todos los errores (grandes o pequeños) duelen de forma lineal. Equivocarte por 20 duele exactamente el doble que equivocarte por 10.

### RMSE (Root Mean Squared Error)
Al elevar el error al cuadrado antes de promediar, el RMSE actúa como una "lupa" que magnifica los errores gigantes.
*Equivocarte por 20 duele MUCHO MÁS del doble que equivocarte por 10.*
- **Cuándo usarlo:** Cuando fallar por mucho es catastrófico. (Ejemplo: predecir la demanda hospitalaria. Equivocarte por 2 camas no pasa nada; equivocarte por 50 implica colapsar urgencias).

### MAPE (Mean Absolute Percentage Error)
Mide el error en porcentaje respecto al valor real.
*Me he equivocado en un 5%.*
- **Cuándo usarlo:** Cuando comunicas resultados a directivos ("nuestro modelo tiene un error del 4%"). 
- **El peligro:** Si en algún momento la demanda real es cercana a cero, el porcentaje se dispara hacia el infinito, colapsando la métrica.

```python
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def mape(y_true, y_pred):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    mascara = y_true != 0 # Protección contra división por cero
    return np.mean(np.abs((y_true[mascara] - y_pred[mascara]) / y_true[mascara])) * 100

def evaluar(y_true, y_pred):
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": rmse(y_true, y_pred),
        "MAPE": mape(y_true, y_pred),
    }
```

---

## 4. Generar Baselines Fuertes (El "Sentido Común")

Vamos a implementar varias estrategias que competirán contra los modelos de Machine Learning que hagamos en el futuro.

### 4.1 Naive Forecast (El Ingenuo)
El modelo naive asume que el mundo se ha congelado en el tiempo: el futuro será exactamente igual al último valor observado en entrenamiento.

```python
ultimo_valor = train.iloc[-1]
pred_naive = pd.Series(ultimo_valor, index=validacion.index)
```
*Si la serie fluctúa como un electrocardiograma, este baseline fallará estrepitosamente dibujando una línea recta.*

### 4.2 Seasonal Naive (El Ingenuo con Memoria)
Es el baseline más difícil de batir en la industria del Retail y la Energía. Asume que hoy pasará exactamente lo mismo que pasó en el mismo ciclo anterior.
En demanda eléctrica (horaria), el "mismo ciclo" suele ser hace 24 horas, o hace una semana (para distinguir laborables de festivos).

```python
historia = pd.concat([train, validacion])
# Predecimos usando lo que pasó exactamente hace 7 días (168 horas)
pred_seasonal_7d = historia.shift(24 * 7).loc[validacion.index]
```

### 4.3 Suavizado Exponencial (El Sabio del Pasado Reciente)
Los métodos de suavizado entienden que el mundo cambia y confían más en lo que pasó ayer que en lo que pasó hace dos meses.
El modelo **Holt-Winters** es capaz de aprender simultáneamente nivel, tendencia y estacionalidad sin necesitar redes neuronales.

```python
# Le decimos explícitamente que busque un patrón de 24 horas
modelo_hw = ExponentialSmoothing(
    train, trend="add", seasonal="add", seasonal_periods=24
).fit()

pred_hw = modelo_hw.forecast(len(validacion))
pred_hw.index = validacion.index
```

### 4.4 ARIMA (El Clásico Matemático)
ARIMA (Autoregressive Integrated Moving Average) busca explicar la serie relacionando sus valores pasados con sus propios errores pasados. Es elegante, pero pesado de computar para series largas con alta estacionalidad horaria.

```python
# Usamos solo los últimos 45 días de train para que entrene rápido
train_arima = train.tail(24 * 45)
modelo_arima = ARIMA(train_arima, order=(2, 1, 2)).fit()

pred_arima = modelo_arima.forecast(steps=len(validacion))
pred_arima.index = validacion.index
```

---

## 5. El Veredicto: El Cuadro de Honor

Agrupamos nuestras predicciones y calculamos el error sobre el **mismo conjunto de validación**.

```python
predicciones = {
    "naive": pred_naive,
    "seasonal_7d": pred_seasonal_7d,
    "holt_winters": pred_hw,
    "arima": pred_arima,
}

resultados = []
for nombre, pred in predicciones.items():
    metricas = evaluar(validacion, pred)
    metricas["modelo"] = nombre
    resultados.append(metricas)

tabla_resultados = pd.DataFrame(resultados).set_index("modelo").sort_values("MAE")
print(tabla_resultados)
```

Aquí descubrirás rápidamente que el *Seasonal Naive* y *Holt-Winters* suelen barrer al resto en series con estacionalidad rígida. ¡Ese es tu verdadero enemigo a batir con Machine Learning!

---

## 6. La Prueba del Algodón: Análisis de Residuos

Si tu baseline es bueno, le habrá extraído toda la "información útil" a la serie. Lo que queda (el error o residuo) debería ser impredecible, puro ruido caótico.

```python
residuos = validacion - pred_seasonal_7d

plt.figure(figsize=(14, 4))
plt.plot(residuos)
plt.axhline(0, color="black", linewidth=1)
plt.title("Residuos del Seasonal Naive a 7 días")
plt.show()
```

- Si los residuos **parecen ruido blanco**, felicidades, el baseline está haciendo un trabajo fenomenal. Probablemente no necesitas un modelo más complejo.
- Si los residuos **siguen mostrando un patrón en forma de ondas**, significa que el modelo es ciego a alguna estacionalidad o tendencia. ¡Ahí es donde el Machine Learning puede aportar valor real!

---

## 7. Backtesting: una sola validación no basta

Un único corte train/valid/test puede engañarnos si justo elegimos una ventana fácil o difícil. En forecasting profesional se usa **backtesting** o validación walk-forward: evaluar el mismo método en varios cortes temporales consecutivos.

```python
def backtesting_seasonal_naive(serie, seasonal_period=168, horizon=24 * 7, initial_train=24 * 60):
    resultados = []

    for inicio_validacion in range(initial_train, len(serie) - horizon + 1, horizon):
        fin_validacion = inicio_validacion + horizon
        validacion_bt = serie.iloc[inicio_validacion:fin_validacion]
        pred_bt = serie.shift(seasonal_period).loc[validacion_bt.index]
        resultados.append({
            "inicio_validacion": validacion_bt.index[0],
            "fin_validacion": validacion_bt.index[-1],
            "MAE": mean_absolute_error(validacion_bt, pred_bt),
        })

    return pd.DataFrame(resultados)

tabla_backtesting = backtesting_seasonal_naive(serie)
tabla_backtesting
```

Si el MAE cambia mucho entre cortes, el modelo no es estable o la serie cambia de régimen.

---

## 8. Incertidumbre: no basta con un número puntual

En producción rara vez basta decir "mañana consumirás 2.1 kWh". También interesa dar un rango plausible. Un primer intervalo empírico puede construirse con los cuantiles de los residuos del baseline.

```python
q_inferior, q_superior = residuos.quantile([0.05, 0.95])

intervalo = pd.DataFrame({
    "prediccion": pred_seasonal_7d,
    "limite_inferior": pred_seasonal_7d + q_inferior,
    "limite_superior": pred_seasonal_7d + q_superior,
})

intervalo.head()
```

Este intervalo es simple y no sustituye a modelos probabilísticos, pero introduce una idea esencial: el error también se modela.

---

## 9. Actividades de clase

### Actividad 1: El pulso de las métricas
Calcula MAE y RMSE para los baselines. ¿Observas que en algún modelo el RMSE es desproporcionadamente más grande que el MAE en comparación con los otros modelos? Si es así, significa que ese modelo tiene "picos de error" (se equivoca poco normalmente, pero cuando falla, falla a lo grande). Intenta razonar por qué pasa.

### Actividad 2: Batalla Estacional
Crea un `Seasonal Naive` de 24 horas y compáralo con el `Seasonal Naive` de 7 días. Observa en la tabla quién gana. Luego grafica la predicción de ambos sobre el primer fin de semana del bloque de validación. Entenderás visualmente por qué el de 24 horas hace el ridículo los sábados por la mañana.

### Actividad 3: La Evaluación Final (El Test de Fuego)
Selecciona el modelo que haya ganado en validación. Ahora, asumiendo que ya estamos en producción, evalúa su rendimiento contra el bloque de `test` que guardamos bajo llave al principio de la sesión. Compara el MAE de test con el MAE de validación. ¿Son parecidos? (Si el error en test es gigantescamente peor, algo ha cambiado en el mundo real durante ese último mes).

---

## 10. Ideas clave

- **Train/Valid/Test:** Nunca rompas el orden temporal. El tiempo solo fluye en una dirección.
- **Backtesting:** Un modelo no debe ganar solo en una ventana cómoda; debe ser estable en varios cortes temporales.
- **Entiende tu métrica:** MAE para el día a día, RMSE para evitar desastres y MAPE para convencer a la junta directiva (cuidado con los ceros).
- **Incertidumbre:** Una predicción puntual sin rango de error puede dar una falsa sensación de seguridad.
- **Respeta a los ancianos:** Métodos clásicos como Seasonal Naive o Holt-Winters (creados hace décadas) pueden y suelen destrozar a algoritmos modernos si la serie es muy cíclica.
- **Escucha al residuo:** El residuo te dice "cuánto potencial de mejora te queda". Si el residuo es caos, tu trabajo ha terminado.

## Continuación

Ya sabemos cuál es el límite mínimo exigido para nuestro proyecto. En la siguiente sesión cruzaremos el puente: convertiremos nuestra serie temporal en una tabla típica de Machine Learning (creando variables `lag`) para entrenar modelos potentes como *Random Forest* y ver si son capaces de destronar al rey *Seasonal Naive*.
