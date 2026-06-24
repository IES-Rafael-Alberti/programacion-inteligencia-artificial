---
output:
  pdf_document: default
  html_document: default
---
# Taller de Series Temporales con Python

## Sesión 1: Introducción a las series temporales

Este documento sirve como punto de partida para trabajar series temporales en Python. La idea de esta primera sesión es entender qué diferencia a una serie temporal de otros tipos de datos, cómo se pueden generar datos sintéticos y qué conceptos básicos necesitamos antes de construir modelos de predicción.

El enfoque de la sesión será práctico: primero construiremos series temporales artificiales para controlar sus componentes y después las usaremos para razonar sobre tendencia, estacionalidad, ruido y predicción.

## Objetivos

Al terminar esta sesión deberías ser capaz de:

- Explicar qué es una serie temporal.
- Identificar ejemplos reales de series temporales.
- Diferenciar entre tendencia, estacionalidad, ciclos y ruido.
- Crear una serie temporal sintética con Python.
- Visualizar una serie temporal e interpretar su comportamiento.
- Entender por qué el orden temporal importa al entrenar y evaluar modelos.
- Reconocer la diferencia entre una serie estacionaria y una no estacionaria.

## Requisitos técnicos

Para esta sesión usaremos Python y algunas librerías habituales de análisis de datos.

```bash
pip install numpy pandas matplotlib scikit-learn
```

Librerías principales:

- `numpy`: generación de datos numéricos y ruido aleatorio.
- `pandas`: manejo de fechas, índices temporales y tablas.
- `matplotlib`: visualización de series temporales.
- `scikit-learn`: métricas sencillas para evaluar predicciones.

## 1. Qué es una serie temporal

Una serie temporal es una secuencia de observaciones ordenadas en el tiempo.

Ejemplos:

- Temperatura diaria de una ciudad.
- Ventas mensuales de una tienda.
- Consumo eléctrico por hora.
- Precio de una acción cada minuto.
- Número de visitas diarias a una página web.
- Nivel de contaminación medido cada hora.

La diferencia principal respecto a otros conjuntos de datos es que el orden importa. En una serie temporal, una observación no es independiente del momento en que ocurre.

Por ejemplo, si queremos predecir las ventas de mañana, normalmente nos interesará saber qué ha pasado hoy, ayer, la semana pasada o el mismo mes del año anterior.

## 2. Tipos de series temporales

Podemos clasificar las series temporales desde varios puntos de vista.

### Según la frecuencia

- Horarias: consumo eléctrico, tráfico web, sensores.
- Diarias: ventas, temperatura, visitas.
- Semanales: demanda agregada, informes comerciales.
- Mensuales: facturación, desempleo, turismo.
- Anuales: población, PIB, matriculaciones.

### Según el número de variables

- Univariante: solo observamos una variable a lo largo del tiempo.
- Multivariante: observamos varias variables relacionadas en el tiempo.

Ejemplo univariante:

```text
fecha        ventas
2026-01-01   120
2026-01-02   135
2026-01-03   128
```

Ejemplo multivariante:

```text
fecha        ventas   temperatura   festivo
2026-01-01   120      11.2          1
2026-01-02   135      10.8          0
2026-01-03   128      12.1          0
```

### Según su comportamiento

- Con tendencia: aumenta o disminuye a largo plazo.
- Con estacionalidad: repite patrones cada cierto periodo.
- Con ruido: contiene variaciones aleatorias.
- Estacionaria: mantiene propiedades estadísticas relativamente constantes.
- No estacionaria: cambia su media, varianza o estructura a lo largo del tiempo.

## 3. Aplicaciones de las series temporales

Las series temporales aparecen en muchos campos:

- Empresa: ventas, demanda, inventario, facturación.
- Energía: consumo eléctrico, producción renovable, demanda horaria.
- Sanidad: pacientes atendidos, epidemias, señales fisiológicas.
- Finanzas: precios, volumen, riesgo, tipos de interés.
- Industria: sensores, mantenimiento predictivo, control de calidad.
- Educación: asistencia, matriculaciones, evolución de notas.
- Medio ambiente: temperatura, lluvia, contaminación, caudales.

En este taller usaremos ejemplos cercanos como ventas, consumo o visitas web porque son fáciles de interpretar.

## 4. Proceso generador de datos

Cuando observamos una serie temporal, normalmente solo vemos el resultado final. Sin embargo, esa serie puede haberse generado por la combinación de varios componentes.

Una forma sencilla de pensar en una serie temporal es:

```text
serie = tendencia + estacionalidad + ruido
```

Donde:

- Tendencia: movimiento general a largo plazo.
- Estacionalidad: patrón que se repite cada cierto periodo.
- Ruido: variación aleatoria que no sigue un patrón claro.

Ejemplo: ventas diarias de una tienda online.

- La tienda vende cada vez más porque gana clientes: tendencia creciente.
- Los fines de semana vende de forma diferente: estacionalidad semanal.
- Algunos días hay subidas o bajadas inesperadas: ruido.

## 5. Generación de series temporales sintéticas

Generar datos sintéticos es útil porque nos permite controlar lo que ocurre. Si sabemos exactamente cómo hemos creado la serie, podemos entender mejor qué debería detectar un modelo.

### 5.1 Crear un índice temporal

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fechas = pd.date_range(start="2026-01-01", periods=180, freq="D")
fechas[:5]
```

Este código crea 180 fechas diarias desde el 1 de enero de 2026.

### 5.2 Crear una tendencia

```python
n = len(fechas)
tendencia = np.linspace(50, 100, n)
```

La tendencia empieza en 50 y termina en 100. Representa un crecimiento progresivo.

### 5.3 Crear estacionalidad semanal

```python
dias = np.arange(n)
estacionalidad = 10 * np.sin(2 * np.pi * dias / 7)
```

Esta señal se repite aproximadamente cada 7 días.

### 5.4 Añadir ruido

```python
np.random.seed(42)
ruido = np.random.normal(loc=0, scale=5, size=n)
```

El ruido introduce variaciones aleatorias alrededor del patrón principal.

### 5.5 Combinar componentes

```python
ventas = tendencia + estacionalidad + ruido

df = pd.DataFrame({
    "fecha": fechas,
    "ventas": ventas,
    "tendencia": tendencia,
    "estacionalidad": estacionalidad,
    "ruido": ruido,
})

df = df.set_index("fecha")
df.head()
```

### 5.6 Visualizar la serie

```python
plt.figure(figsize=(12, 4))
plt.plot(df.index, df["ventas"], label="ventas")
plt.title("Serie temporal sintética de ventas")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.legend()
plt.grid(True)
plt.show()
```

## 6. Ruido blanco y ruido rojo

El ruido representa variaciones que no explicamos con los componentes principales.

### Ruido blanco

El ruido blanco es aleatorio y no tiene memoria. El valor de hoy no depende del valor de ayer.

```python
ruido_blanco = np.random.normal(0, 1, 200)

plt.figure(figsize=(12, 3))
plt.plot(ruido_blanco)
plt.title("Ruido blanco")
plt.grid(True)
plt.show()
```

### Ruido rojo

El ruido rojo tiene memoria. Cada valor depende en parte del anterior, por lo que suele verse más suave.

```python
np.random.seed(42)
ruido_rojo = [0]

for i in range(1, 200):
    nuevo_valor = 0.8 * ruido_rojo[i - 1] + np.random.normal(0, 1)
    ruido_rojo.append(nuevo_valor)

plt.figure(figsize=(12, 3))
plt.plot(ruido_rojo)
plt.title("Ruido rojo")
plt.grid(True)
plt.show()
```

Pregunta para discutir:

```text
Si una serie tiene memoria, ¿podemos aprovechar los valores pasados para predecir 
los futuros?
```

## 7. Señales cíclicas o estacionales

Una serie tiene estacionalidad cuando repite un patrón cada cierto intervalo.

Ejemplos:

- Más ventas en Navidad.
- Más consumo eléctrico en determinadas horas.
- Menos actividad los fines de semana.
- Más turismo en verano.

Ejemplo de estacionalidad anual:

```python
fechas = pd.date_range(start="2024-01-01", periods=365, freq="D")
dias = np.arange(len(fechas))

estacionalidad_anual = 20 * np.sin(2 * np.pi * dias / 365)

plt.figure(figsize=(12, 3))
plt.plot(fechas, estacionalidad_anual)
plt.title("Componente estacional anual")
plt.grid(True)
plt.show()
```

## 8. Señales autorregresivas

Una señal autorregresiva es aquella en la que el valor actual depende de valores anteriores.

Ejemplo:

```text
valor_hoy = 0.7 * valor_ayer + ruido
```

Código:

```python
np.random.seed(42)

serie_ar = [10]

for i in range(1, 200):
    valor = 0.7 * serie_ar[i - 1] + np.random.normal(0, 2)
    serie_ar.append(valor)

plt.figure(figsize=(12, 3))
plt.plot(serie_ar)
plt.title("Serie autorregresiva")
plt.grid(True)
plt.show()
```

Este tipo de comportamiento es muy importante en predicción porque indica que el pasado contiene información útil sobre el futuro.

## 9. Mezclar componentes

En los datos reales, los componentes suelen aparecer mezclados.

```python
np.random.seed(42)

fechas = pd.date_range(start="2026-01-01", periods=365, freq="D")
n = len(fechas)
dias = np.arange(n)

tendencia = np.linspace(100, 180, n)
estacionalidad_semanal = 15 * np.sin(2 * np.pi * dias / 7)
estacionalidad_anual = 25 * np.sin(2 * np.pi * dias / 365)
ruido = np.random.normal(0, 8, n)

serie = tendencia + estacionalidad_semanal + estacionalidad_anual + ruido

df = pd.DataFrame({"ventas": serie}, index=fechas)

plt.figure(figsize=(14, 4))
plt.plot(df.index, df["ventas"])
plt.title("Serie sintética con tendencia, estacionalidad y ruido")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()
```

Actividad:

- Cambia la intensidad de la tendencia.
- Cambia la amplitud de la estacionalidad.
- Cambia el nivel de ruido.
- Observa qué ocurre con la gráfica.

## 10. Series estacionarias y no estacionarias

Una serie estacionaria mantiene un comportamiento estadístico relativamente estable en el tiempo.

De forma simplificada, una serie estacionaria tiene:

- Media aproximadamente constante.
- Varianza aproximadamente constante.
- Patrones que no cambian demasiado con el tiempo.

Una serie no estacionaria puede tener:

- Cambio en la media.
- Cambio en la varianza.
- Tendencia clara.
- Estacionalidad fuerte.
- Cambios bruscos de comportamiento.

### Cambio en la media

```python
np.random.seed(42)

parte_1 = np.random.normal(50, 5, 100)
parte_2 = np.random.normal(80, 5, 100)
serie_cambio_media = np.concatenate([parte_1, parte_2])

plt.figure(figsize=(12, 3))
plt.plot(serie_cambio_media)
plt.title("Serie con cambio en la media")
plt.grid(True)
plt.show()
```

### Cambio en la varianza

```python
np.random.seed(42)

parte_1 = np.random.normal(50, 2, 100)
parte_2 = np.random.normal(50, 12, 100)
serie_cambio_varianza = np.concatenate([parte_1, parte_2])

plt.figure(figsize=(12, 3))
plt.plot(serie_cambio_varianza)
plt.title("Serie con cambio en la varianza")
plt.grid(True)
plt.show()
```

## 11. Qué podemos predecir

En forecasting no siempre queremos predecir lo mismo.

Podemos predecir:

- El siguiente valor.
- Los próximos 7 días.
- La demanda del próximo mes.
- Si se superará un umbral.
- El valor máximo o mínimo de un periodo.
- La tendencia esperada.

Ejemplo:

```text
Si tenemos ventas diarias hasta el 30 de abril, podemos intentar predecir:

- las ventas del 1 de mayo
- las ventas de la próxima semana
- las ventas totales del mes siguiente
```

## 12. Terminología básica de forecasting

Algunos términos que usaremos durante el taller:

- Observación: cada valor registrado en un instante temporal.
- Frecuencia: separación entre observaciones, por ejemplo diaria, horaria o mensual.
- Horizonte de predicción: distancia hacia el futuro que queremos predecir.
- Ventana temporal: conjunto de observaciones pasadas que usamos como contexto.
- Lag: valor retrasado de la serie, por ejemplo ventas de ayer o de hace 7 días.
- Baseline: modelo sencillo que sirve como referencia.
- Train: parte de la serie usada para entrenar.
- Test: parte futura usada para evaluar.

## 13. Primera predicción baseline

Antes de usar modelos complejos, conviene construir una predicción sencilla.

Una opción simple es usar como predicción el último valor conocido.

```python
from sklearn.metrics import mean_absolute_error

np.random.seed(42)

fechas = pd.date_range(start="2026-01-01", periods=180, freq="D")
n = len(fechas)
dias = np.arange(n)

tendencia = np.linspace(50, 100, n)
estacionalidad = 10 * np.sin(2 * np.pi * dias / 7)
ruido = np.random.normal(0, 5, n)
ventas = tendencia + estacionalidad + ruido

df = pd.DataFrame({"ventas": ventas}, index=fechas)

train = df.iloc[:-30]
test = df.iloc[-30:]

ultimo_valor = train["ventas"].iloc[-1]
prediccion = np.repeat(ultimo_valor, len(test))

mae = mean_absolute_error(test["ventas"], prediccion)
mae
```

Visualización:

```python
plt.figure(figsize=(12, 4))
plt.plot(train.index, train["ventas"], label="train")
plt.plot(test.index, test["ventas"], label="test")
plt.plot(test.index, prediccion, label="predicción naive", linestyle="--")
plt.title(f"Predicción naive - MAE: {mae:.2f}")
plt.legend()
plt.grid(True)
plt.show()
```

Pregunta para discutir:

```text
¿Este modelo es bueno? ¿Qué tendría que hacer un modelo más avanzado para merecer la pena?
```

## 14. Actividades de clase

### Actividad 1

Crea una serie temporal sintética de 90 días que represente visitas a una página web.

Debe tener:

- Tendencia creciente.
- Estacionalidad semanal.
- Ruido aleatorio.

### Actividad 2

Modifica la serie anterior para simular una campaña publicitaria a mitad del periodo.

Pistas:

- Puedes sumar una cantidad fija durante varios días.
- Puedes hacer que el efecto suba y después baje.

### Actividad 3

Divide la serie en entrenamiento y test.

Condición:

- Los últimos 14 días deben ser el conjunto de test.

### Actividad 4

Construye una predicción naive usando el último valor del conjunto de entrenamiento.

Calcula el error medio absoluto.

### Actividad 5

Compara la predicción naive con otra predicción simple:

- La media de los últimos 7 días.
- El valor observado 7 días antes.

## 15. Ideas clave

- Una serie temporal es una secuencia ordenada en el tiempo.
- El orden temporal no se debe romper al entrenar y evaluar modelos.
- Muchas series combinan tendencia, estacionalidad y ruido.
- Los datos sintéticos son útiles para aprender porque controlamos el proceso que los genera.
- Antes de usar modelos avanzados necesitamos un baseline sencillo.
- Una predicción compleja solo merece la pena si mejora claramente a una predicción simple.

## Continuación

En la siguiente sesión trabajaremos con:

- Separación correcta entre entrenamiento y test.
- Métricas de error.
- Lags y variables derivadas del calendario.
- Modelos supervisados sencillos para forecasting.
