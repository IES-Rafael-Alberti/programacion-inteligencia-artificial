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
    border-bottom: 3px solid #3498db;
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

# Introducción a las Series Temporales
## Taller de Forecasting Práctico con Python

**Módulo:** PIA
**Profesor/a:** (Tu Nombre)

---

# ¿Qué es una Serie Temporal?

No es solo una tabla de datos. Es la **historia contada a través del tiempo**.

*   El orden importa: el dato de hoy depende del dato de ayer.
*   Es la huella digital de un proceso en movimiento.
*   Ejemplos: Consumo eléctrico ⚡, Ventas en un supermercado 🛒, Visitantes a una web 🌐.

---

# ¿Qué NO es una Serie Temporal?

Imagina un Excel con los datos de 1000 clientes: 
*Edad, Sueldo, Altura, Código Postal.*

*   Si ordenas esa tabla de mayor a menor sueldo, **la información no cambia**.
*   Si barajas las filas aleatoriamente, **el modelo predictivo aprende igual**.

> En una serie temporal, si barajas las filas, **destruyes** la información. El tiempo es el hilo conductor.

---

# Anatomía de una Serie Temporal

Toda serie se puede descomponer (generalmente) en **4 piezas clave**:

1.  **Tendencia:** El viaje a largo plazo (Ej. Calentamiento global).
2.  **Estacionalidad:** El latido constante y predecible (Ej. Más ventas en Navidad).
3.  **Ciclos:** Olas largas y variables (Ej. Ciclos económicos de 7 años).
4.  **Ruido (Irregular):** Lo impredecible. La vida real golpeando tus datos.

---

<div class="columns">
<div>

# Tendencia + Estacionalidad

**Analogía Visual:**
Imagina que vas caminando por la playa hacia el mar (*Tendencia*) mientras haces botar una pelota de baloncesto (*Estacionalidad*). 

La trayectoria general va hacia abajo (te acercas al agua), pero el movimiento inmediato es arriba y abajo (botes regulares).

</div>
<div>

![Visualización mental](https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&q=80&w=600&h=400)

</div>
</div>

---

# El Proceso Generador de Datos (DGP)

Antes de intentar predecir el futuro (Machine Learning), necesitamos entender el mecanismo oculto que crea los datos en el presente.

En este taller usaremos **Datos Sintéticos de Consumo Eléctrico**:
- Empezamos con una base sencilla.
- Le sumamos un latido diario.
- Le bajamos el volumen los fines de semana.
- Le añadimos olas de calor (ruido).

**¿Por qué sintético?** Porque para aprender a volar, primero usamos un simulador de vuelo, no un avión real en plena tormenta.

---

# Estacionariedad: El concepto fantasma

Un modelo clásico de estadística necesita que las reglas del juego no cambien a mitad de partido.

*   **Serie Estacionaria:** La media y la varianza son constantes a lo largo del tiempo. (Ruido blanco).
*   **Serie No Estacionaria:** La media sube (tendencia) o la volatilidad cambia. (Bolsa de valores).

**¡Cuidado!** Casi ninguna serie real es estacionaria. Nuestro trabajo consistirá en transformarlas para poder predecirlas.

---

# Terminología de Supervivencia

Para no perdernos en las próximas sesiones:

*   **Horizonte de Predicción:** ¿A cuántos pasos hacia el futuro queremos mirar?
*   **Lag (Rezagos):** Mirar por el retrovisor. `Lag 1` es el dato de ayer. `Lag 7` es el dato de la semana pasada.
*   **Forecasting vs Predicción:** 
    *   Predicción: ¿Este cliente se dará de baja?
    *   Forecasting: ¿Cuántos clientes se darán de baja el próximo mes? (Hay un eje de tiempo implícito).

---

# Nuestro Primer "Modelo": La Predicción Inocente (Naïve)

Antes de sacar la artillería pesada del Machine Learning, siempre hazte esta pregunta:

> "¿Qué pasaría si mi predicción para mañana fuera exactamente el mismo valor de hoy?"

*   Ese es el modelo **Naïve**. 
*   Será nuestro "suelo". Si tu red neuronal súper compleja no es capaz de batir al modelo Naïve... tienes un problema.

---

# 🚀 ¡A los Notebooks!

Es hora de ensuciarse las manos.
Abre el notebook `01_introduccion_series_temporales.ipynb`

Vamos a:
1. Generar nuestra primera serie temporal.
2. Añadirle ruido y señales estacionales manualmente.
3. Observar cómo interactúan.
