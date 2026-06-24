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
    border-bottom: 3px solid #2ecc71;
    padding-bottom: 10px;
  }
  h2 {
    color: #34495e;
  }
  strong {
    color: #e74c3c;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# Análisis y Visualización
## Taller de Forecasting Práctico con Python

**Sesión 03**
Escuchar a los datos antes de modelar.

---

# El Error del Científico Impaciente

Es muy tentador coger nuestros datos limpios de la sesión anterior y lanzárselos directamente a un modelo de Machine Learning. **Esto es un error grave.**

Antes de predecir el futuro, debemos comprender el pasado.
Si no visualizas y analizas los componentes de la serie, intentarás modelar el *"eco"* sin saber quién originó el *"sonido"*.

> Visualizar no es "hacer gráficos bonitos". Es una herramienta de **diagnóstico clínico**.

---

<div class="columns">
<div>

# Las 4 Fuerzas

Imagina que vas en un barco:
1.  **Tendencia:** La corriente del océano que te arrastra a largo plazo.
2.  **Estacionalidad:** Las mareas. Suben y bajan con exactitud matemática.
3.  **Ciclo:** Las tormentas (Ej. Crisis económicas de 7 años). No tienen periodo fijo.
4.  **Residuo (Ruido):** El oleaje caótico que golpea tu barco.

</div>
<div>

![Barco en el mar](https://images.unsplash.com/photo-1518331558296-38cb44186411?auto=format&fit=crop&q=80&w=600&h=400)

</div>
</div>

---

# Boxplots Temporales: Detectando Varianza

La media miente. El lunes y el jueves pueden tener la misma media de consumo, pero el lunes tener picos altísimos y el jueves ser muy estable.

El **Boxplot** por hora o por día nos revela la incertidumbre real de la serie.
Si la "caja" de las 18:00h es enorme, significa que nuestro modelo futuro tendrá mucho margen de error a esa hora.

---

# Autocorrelación (ACF): El Eco Matemático

En forecasting predictivo, predecimos el futuro usando el **pasado de la propia variable**. (El valor de hoy predice el de mañana).

El gráfico ACF responde a: *¿Cuánto se parece el dato de hoy al de hace $N$ pasos (Lags)?*

*   Si ves picos muy altos cada 24 horas (Lags = 24, 48, 72...), la serie tiene un "eco" diario violentamente fuerte.
*   El dato de hoy a las 14:00 será el mejor predictor para mañana a las 14:00.

---

# Descomponiendo la Señal (STL)

No tenemos que adivinar las fuerzas a ojo. Podemos separarlas matemáticamente.
El algoritmo **STL** (*Seasonal and Trend decomposition using LOESS*) es el estándar de la industria.

Rompe tu serie temporal en 3 gráficos:
1.  La curva suave de la **Tendencia**.
2.  El patrón repetitivo de la **Estacionalidad**.
3.  El **Residuo**: Lo que sobra.

> **Objetivo:** Si el gráfico del Residuo parece ruido de televisión ("ruido blanco"), enhorabuena, has capturado toda la inteligencia en las otras dos variables.

---

# Cisnes Negros: Outliers en el Tiempo

Un *outlier* en el tiempo es un concepto engañoso. 
Consumir 5000 kWh en agosto es normal, pero en abril es una anomalía masiva.

**¿Borrar o No Borrar? Esa es la cuestión.**

1.  **Error Técnico:** El sensor envió un -999. *Decisión:* Interpolamos (lo borramos).
2.  **Evento Extremo Real:** Tormenta de nieve histórica (Filomena). *Decisión:* **Conservarlo**, pero crear una columna externa (`ola_de_frio=1`) para que el modelo entienda *por qué* pasó.

Si borras las crisis, tu modelo jamás aprenderá a sobrevivir a ellas.

---

# 🚀 ¡A Diagnosticar!

Abre el notebook `03_analisis_visualizacion_series_temporales.ipynb`

**Misiones:**
1. Rastrear el pulso de la autocorrelación en distintos Lags.
2. Jugar con la descomposición STL modificando los periodos.
3. Debatir qué hacer con los outliers detectados.
