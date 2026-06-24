---
output: 
    pdf_document:
        latex_engine: xelatex
        toc: true
        toc_depth: 3
        number_sections: true
        includes:
            in_header: header.tex

---

## 🧠 1. Introducción al Aprendizaje por Refuerzo (Reinforcement Learning)

### 🎯 1.1 ¿Qué es el Reinforcement Learning (RL)?

**Definición simple:**  
El aprendizaje por refuerzo es una técnica de inteligencia artificial donde un agente aprende **interactuando con un entorno** para lograr un objetivo, **recibiendo recompensas** o castigos por sus acciones.

> 📌 **Idea clave:** el agente aprende **por experiencia**, como un niño que aprende a montar en bici: prueba → cae → prueba otra vez → mejora.

---

### 🎮 1.2 Analogía visual: El Agente en un videojuego

Imagina que eres un personaje en un videojuego:
- Tienes un entorno (el mapa del juego),
- Puedes realizar acciones (moverte, saltar, atacar...),
- Y recibes recompensas o penalizaciones (monedas, vidas perdidas...).

🎨 **Visualización básica:**

```
  [ENTORNO]
       ↑
Recompensa/Penalización
       ↓
[AGENTE] → Acción → [ENTORNO]
```

---

### 🧩 1.3 Elementos clave del RL

| Elemento   | Descripción breve | Ejemplo en un videojuego |
|------------|-------------------|---------------------------|
| **Agente** | El que toma decisiones | El jugador/personaje |
| **Entorno** | Lo que rodea al agente | El mundo del juego |
| **Acciones (A)** | Lo que puede hacer el agente | Moverse, atacar, saltar |
| **Estado (S)** | La situación actual del entorno | Posición del jugador, enemigos cerca |
| **Recompensa (R)** | Lo que gana o pierde | +10 por ganar, -5 por perder vida |
| **Política (π)** | La estrategia del agente | “Si hay enemigo cerca, atacar” |
| **Función de valor (V)** | Cuánto vale un estado a largo plazo | ¿Estoy en una buena posición? |
| **Q-Valor (Q)** | Valor de una acción en un estado | ¿Qué tan buena es esta acción aquí? |

---

### 🔁 1.4 Cómo aprende el agente: Ciclo de interacción

1. El **agente observa** el estado actual del entorno.
2. Elige una **acción** según su estrategia (política).
3. El entorno **cambia** y entrega una **recompensa**.
4. El agente **aprende** y repite.

📊 **Ejemplo visual (CartPole):**
```plaintext
[Ver posición del palo] → [Mover carrito] → [¿Se cayó?] → [+1 o 0] → [Aprender y repetir]
```

---

### 🤖 1.5 Diferencias con otros tipos de aprendizaje

| Tipo | Supervision | Datos disponibles | Ejemplo |
|------|-------------|-------------------|---------|
| **Supervisado** | Etiquetas conocidas | Sí | Imagen → "gato" |
| **No supervisado** | No hay etiquetas | No | Agrupar clientes por comportamiento |
| **Por refuerzo** | Recompensas según acciones | Se descubren interactuando | Entrenar un robot a caminar |

---

### 🧪 1.6 Actividad práctica guiada (sin código aún)

**Mini-juego en clase:**
- Simula un agente en un laberinto con recompensas (dibujado en la pizarra).
- Un alumno hace de "agente" y otro de "entorno".
- Reglas:
  - Cada casilla tiene un valor oculto (el entorno lo sabe).
  - El agente elige acciones y recibe recompensa.
  - Objetivo: encontrar la ruta más valiosa.

> Así comprenden el **rol de las decisiones, la política y la recompensa** sin tocar aún el código.

---

### ✅ Resumen práctico del punto 1

- RL se basa en **interacción continua**.
- El agente **aprende a través de prueba y error**.
- La **recompensa guía** al aprendizaje.
- Es útil para videojuegos, robótica, toma de decisiones y más.

---

## 📐 2. Fundamentos Matemáticos (explicados visualmente)

> 🎯 Objetivo: entender las **ideas clave detrás del aprendizaje por refuerzo** sin necesidad de ecuaciones complejas, para luego poder aplicar estas ideas al programar.

---

### 🧱 2.1 ¿Qué es un MDP (Proceso de Decisión de Markov)?

Un **MDP** (Markov Decision Process) es un modelo que usamos para representar **cómo el agente toma decisiones en un entorno que cambia**.

🎮 **Ejemplo visual:**  
Imagina un robot que está en una sala con 4 casillas. Desde cada casilla puede:
- moverse a otra (acción),
- y recibe una recompensa (buena o mala).

🔁 La idea de *Markov* es que **el futuro solo depende del presente**, no del pasado.

```plaintext
[Casilla A] --(Derecha)--> [Casilla B] --(Izquierda)--> [Casilla A]
  Estado        Acción         Nuevo Estado
```

---

### 🗺️ 2.2 Funciones de valor

Son maneras de **medir lo bueno o malo que es un estado** o una acción para el agente.

#### 🎲 2.2.1 Función de valor \( V(s) \)
"¿Qué tan bueno es estar en este estado?"

📦 Ejemplo: Si estás en una casilla con salida cercana, probablemente sea buena → valor alto.

#### 🎯 2.2.2 Función Q o Q-valor \( Q(s, a) \)
"¿Qué tan buena es la **acción a** si estoy en el estado **s**?"

🔁 Nos ayuda a **decidir la mejor acción** entre varias.

---

### 🧠 2.3 Políticas (π): cómo actúa el agente

Una **política** es simplemente una **estrategia**: indica qué acción tomar en cada estado.

- Puede ser **determinista**: “si estoy en A, siempre voy a la derecha”.
- O **estocástica**: “si estoy en A, voy a la derecha un 70% de las veces, y a la izquierda un 30%”.

🎲 **Visual**: Un dado con diferentes probabilidades por acción.

---

### 🔁 2.4 El ciclo de Bellman (sin fórmula)

La **ecuación de Bellman** dice básicamente esto:

> “El valor de un estado es igual a la **recompensa inmediata** más lo que esperas conseguir **más adelante** si sigues actuando bien.”

📦 Ejemplo:
- Si hoy estás en una casilla buena (+5 puntos),
- y puedes llegar a otra aún mejor (+10 puntos) con una acción,
- entonces el valor de tu estado actual también sube.

---

### ⏳ 2.5 Descuento de recompensa

El **factor de descuento (γ)** representa cuánto te importa el futuro.

- Si γ = 0 → Solo te importa el **premio inmediato**.
- Si γ ≈ 1 → Te importa más el **premio a largo plazo**.

🏦 Analogía: como el valor del dinero con el tiempo (mejor tener 10 € hoy que dentro de un año, a menos que confíes en el futuro).

---

### 🧪 Actividad visual práctica (sin código)

**Mapa de valores:**
1. Dibuja un tablero 5x5.
2. Marca casillas con premios y castigos.
3. Pide a los alumnos que valoren (con post-its) las casillas según lo cerca que están de los premios.
4. Después, que propongan una política (camino óptimo).

🎯 Objetivo: entender **cómo se construyen los valores y las decisiones sin código**.

---

### ✅ Resumen del Punto 2

- Un **MDP** es un entorno donde se decide paso a paso.
- Las **funciones de valor** ayudan al agente a saber dónde ir.
- Las **políticas** definen cómo actuar.
- El **descuento** nos dice si nos interesa más el corto o el largo plazo.

---

