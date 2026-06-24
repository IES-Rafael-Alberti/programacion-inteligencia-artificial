## 🐍 Parte 1: Juego Snake en `pyglet`

### 🎯 Objetivo

Crear una implementación mínima pero funcional del juego Snake con `pyglet`, para poder usarlo como entorno de entrenamiento más adelante.

### 📚 ¿Por qué usamos Pyglet?

* Permite **renderizar gráficos en tiempo real** de forma sencilla.
* Funciona bien con entornos personalizados que luego integraremos con `gymnasium`.
* Es ligero y multiplataforma.

---

### 🔧 Instalación necesaria

```bash
pip install pyglet
```

---

### 💻 Código base de Snake en Pyglet

A continuación te presento una primera versión con explicaciones por bloques:

```python
import pyglet
import random

# Configuración de la ventana
WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20

window = pyglet.window.Window(WIDTH, HEIGHT)
snake = [(5, 5)]
snake_dir = (1, 0)  # Dirección inicial (derecha)
food = (10, 10)

game_over = False


def draw_cell(x, y, color):
    size = CELL_SIZE - 2
    pyglet.shapes.Rectangle(
        x * CELL_SIZE + 1, y * CELL_SIZE + 1, size, size, color=color, batch=batch
    ).draw()


@window.event
def on_draw():
    window.clear()
    global batch
    batch = pyglet.graphics.Batch()

    # Dibujar comida (rojo)
    draw_cell(food[0], food[1], color=(255, 0, 0))

    # Dibujar serpiente (verde)
    for x, y in snake:
        draw_cell(x, y, color=(0, 255, 0))

    batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    global snake_dir
    from pyglet.window import key
    if symbol == key.UP and snake_dir != (0, -1):
        snake_dir = (0, 1)
    elif symbol == key.DOWN and snake_dir != (0, 1):
        snake_dir = (0, -1)
    elif symbol == key.LEFT and snake_dir != (1, 0):
        snake_dir = (-1, 0)
    elif symbol == key.RIGHT and snake_dir != (-1, 0):
        snake_dir = (1, 0)


def update(dt):
    global snake, food, game_over

    if game_over:
        return

    # Mover la cabeza
    head_x, head_y = snake[0]
    dx, dy = snake_dir
    new_head = (head_x + dx, head_y + dy)

    # Verificar colisiones con bordes o el cuerpo
    if (
        new_head in snake
        or not (0 <= new_head[0] < WIDTH // CELL_SIZE)
        or not (0 <= new_head[1] < HEIGHT // CELL_SIZE)
    ):
        print("Game Over")
        game_over = True
        return

    # Insertar nueva cabeza
    snake.insert(0, new_head)

    # Verificar si comió
    if new_head == food:
        food = (
            random.randint(0, WIDTH // CELL_SIZE - 1),
            random.randint(0, HEIGHT // CELL_SIZE - 1),
        )
    else:
        # Eliminar la cola si no comió
        snake.pop()


pyglet.clock.schedule_interval(update, 0.2)
pyglet.app.run()
```

---

### 🧠 Explicación pedagógica

#### 1. **Representación del entorno**

* La pantalla está dividida en **celdas** de `CELL_SIZE` píxeles.
* La serpiente es una lista de coordenadas (`(x, y)`).
* La comida es una coordenada aleatoria.

#### 2. **Dinámica del juego**

* En cada "tick" del reloj (`update`), se mueve la cabeza en la dirección indicada.
* Si come comida, crece; si no, se mueve eliminando la cola.
* Si choca contra su cuerpo o los bordes, el juego termina.

#### 3. **Control del jugador**

* Las teclas permiten cambiar la dirección de la serpiente, salvo en dirección opuesta a la actual.

---

### ✅ Resultado

Un juego jugable de Snake, que se puede controlar con flechas. Es la base visual que más adelante encapsularemos como un entorno de `gymnasium`.

---

### 📦 Próximo paso: **Parte 2: Adaptar Snake como entorno Gymnasium**

Aquí es donde comenzamos a hablar de *agente, estados, acciones y recompensas*.

---

Perfecto. Vamos con la **Parte 2: Adaptar Snake como entorno de aprendizaje por refuerzo con Gymnasium**.

---

## 🧩 Parte 2: Adaptación del juego Snake como entorno `gymnasium`

### 🎯 Objetivo

Convertir el juego Snake en un **entorno compatible con `gymnasium`**, que pueda ser usado por un agente de aprendizaje por refuerzo.

---

### 📚 ¿Qué es un entorno en `gymnasium`?

En `gymnasium`, un entorno (environment) define:

| Elemento      | Significado                                                 |
| ------------- | ----------------------------------------------------------- |
| `observation` | El estado que el agente puede "ver"                         |
| `action`      | Las acciones que el agente puede tomar                      |
| `reward`      | El valor numérico que informa si su acción fue buena o mala |
| `done`        | Indica si el episodio (partida) terminó                     |
| `info`        | Diccionario con información adicional                       |

---

### 💾 Instalación

```bash
pip install gymnasium
```

---

### 🧠 Conceptos clave que aplicaremos

* **Estados (observaciones)**: Posición de la cabeza, dirección, ubicación de la comida, colisiones.
* **Acciones**: `[0: izquierda, 1: adelante, 2: derecha]` en relación a la dirección actual.
* **Recompensa**:

  * +1 si come comida
  * -1 si muere
  * 0 en cualquier otro caso

---

### 🛠️ Código: `snake_env.py`

Creamos una clase heredada de `gymnasium.Env`:

```python
import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random

class SnakeEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 5}

    def __init__(self, grid_size=10):
        super().__init__()
        self.grid_size = grid_size
        self.action_space = spaces.Discrete(3)  # 0: izquierda, 1: recto, 2: derecha

        # Observación: 11 entradas binarias (como en Deep Q-Learning de Snake)
        self.observation_space = spaces.Box(low=0, high=1, shape=(11,), dtype=np.float32)

        self.reset()

    def _get_observation(self):
        # Simplificación: vector de 11 características
        # Ejemplo: [peligro_izq, peligro_frente, peligro_der, dir_izq, dir_der, dir_arriba, dir_abajo, comida_izq, ...]
        head_x, head_y = self.snake[0]
        fx, fy = self.food
        dx, dy = self.direction

        # Direcciones posibles
        left = (-dy, dx)
        right = (dy, -dx)

        def danger(pos):
            x, y = pos
            return (
                x < 0 or x >= self.grid_size or
                y < 0 or y >= self.grid_size or
                (x, y) in self.snake
            )

        obs = [
            danger((head_x + left[0], head_y + left[1])),
            danger((head_x + dx, head_y + dy)),
            danger((head_x + right[0], head_y + right[1])),
            int(dx == -1), int(dx == 1), int(dy == 1), int(dy == -1),
            int(fx < head_x), int(fx > head_x), int(fy < head_y), int(fy > head_y)
        ]
        return np.array(obs, dtype=np.float32)

    def reset(self, seed=None, options=None):
        self.snake = [(self.grid_size // 2, self.grid_size // 2)]
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.food = self._place_food()
        self.done = False
        return self._get_observation(), {}

    def _place_food(self):
        while True:
            pos = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
            if pos not in self.snake:
                return pos

    def step(self, action):
        if self.done:
            return self._get_observation(), 0, True, False, {}

        # Actualizar dirección
        dx, dy = self.direction
        if action == 0:   # izquierda
            self.direction = (-dy, dx)
        elif action == 2:  # derecha
            self.direction = (dy, -dx)

        # Mover la serpiente
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        reward = 0
        if (
            new_head in self.snake or
            not (0 <= new_head[0] < self.grid_size) or
            not (0 <= new_head[1] < self.grid_size)
        ):
            self.done = True
            reward = -1  # 🟥 Castigo por morir
            return self._get_observation(), reward, True, False, {}

        self.snake.insert(0, new_head)

        if new_head == self.food:
            reward = 1  # 🟩 Refuerzo por comer
            self.food = self._place_food()
        else:
            self.snake.pop()

        return self._get_observation(), reward, self.done, False, {}

    def render(self):
        grid = np.full((self.grid_size, self.grid_size), " ")
        for x, y in self.snake:
            grid[y][x] = "O"
        fx, fy = self.food
        grid[fy][fx] = "F"
        print("\n".join("".join(row) for row in grid))
        print("-" * self.grid_size)

    def close(self):
        pass
```

---

### 🧠 Explicación del diseño de RL

#### 🔄 Estados (observaciones)

El agente no ve el entorno completo (como una imagen), sino una representación reducida:

* Si hay peligro en 3 direcciones (frente, izquierda, derecha)
* La dirección actual
* Relación entre comida y cabeza

Esto reduce el **espacio de estados** y permite un entrenamiento más rápido.

#### 🎮 Acciones

* 0: gira a la izquierda respecto a su dirección actual
* 1: sigue recto
* 2: gira a la derecha

#### 🟩 Recompensas

* **+1 si come comida** → esto incentiva que el agente aprenda a buscarla.
* **-1 si muere** → castigo claro para evitar errores.
* **0 si sobrevive sin comer** → neutral, no castiga ni recompensa.

> 📌 **Este tipo de refuerzo funciona bien porque tiene una señal clara de éxito (comer) y una penalización clara de fallo (morir).**

---

### ✅ Resultado

Ya tenemos un entorno compatible con `gymnasium`, donde:

* Se puede usar `.step()` para avanzar con una acción
* Se recibe el nuevo estado, recompensa, si ha terminado, etc.
* Se puede entrenar un agente.

---

### 🚀 Próximo paso: Parte 3: Crear un agente de RL que aprenda a jugar


Perfecto, excelente enfoque didáctico. Empezaremos con una versión más **simple** usando una **Q-Table**, ideal para explicar los fundamentos del aprendizaje por refuerzo. Luego pasaremos a una versión con red neuronal (DQN).

---

## 🧠 Parte 3.1: Entrenamiento con Q-Table

### 🎯 Objetivo

Enseñar al agente a jugar Snake **usando una Q-table**, que mapea observaciones discretas a acciones.

---

### ❓ ¿Qué es una Q-Table

Una Q-table es una **tabla que almacena los valores esperados de recompensa** para cada combinación posible de:

* Estado (s)
* Acción (a)

Se actualiza usando la fórmula:

$$
Q(s,a) \leftarrow Q(s,a) + \alpha \cdot \left[ r + \gamma \cdot \max_{a'} Q(s',a') - Q(s,a) \right]
$$

Donde:

* $\alpha$: tasa de aprendizaje
* $\gamma$: factor de descuento
* $r$: recompensa
* $s', a'$: próximo estado y mejor acción futura

---

### 📌 Limitación

Este enfoque solo funciona si el número de **estados es manejable** (como ahora, con 11 observaciones binarias: $2^{11} = 2048$ estados posibles).

---

### 🛠️ Paso previo: Discretizar el estado

Usamos la función de observación del entorno anterior (vector binario de 11 elementos) y la convertimos en una **clave entera** para indexar la tabla.

```python
def obs_to_index(obs):
    return int("".join(str(int(x)) for x in obs), 2)
```

---

### 💻 Código del agente Q-Table

```python
import numpy as np
from snake_env import SnakeEnv
from collections import defaultdict
import random

env = SnakeEnv(grid_size=10)

alpha = 0.1          # Tasa de aprendizaje
gamma = 0.9          # Factor de descuento
epsilon = 1.0        # Exploración inicial
epsilon_min = 0.01
epsilon_decay = 0.995
episodes = 1000

q_table = defaultdict(lambda: np.zeros(env.action_space.n))


def obs_to_index(obs):
    return int("".join(str(int(x)) for x in obs), 2)


for ep in range(episodes):
    obs, _ = env.reset()
    state = obs_to_index(obs)
    total_reward = 0
    done = False

    while not done:
        # Política epsilon-greedy
        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_obs, reward, done, _, _ = env.step(action)
        next_state = obs_to_index(next_obs)

        # Actualizar Q-table
        q_table[state][action] += alpha * (
            reward + gamma * np.max(q_table[next_state]) - q_table[state][action]
        )

        state = next_state
        total_reward += reward

    epsilon = max(epsilon * epsilon_decay, epsilon_min)

    if ep % 100 == 0:
        print(f"Ep {ep}: Recompensa total = {total_reward:.2f} | Epsilon = {epsilon:.3f}")
```

---

### 📚 Explicación pedagógica

#### 🔁 Bucle de entrenamiento

En cada episodio, el agente:

1. Observa el estado del entorno
2. Toma una acción (aleatoria o basada en Q)
3. Recibe una recompensa
4. Actualiza su tabla Q
5. Repite hasta que el juego termine

#### 🎲 Política ε-greedy

* $\varepsilon = 1.0$: al principio actúa al azar
* Con el tiempo, se vuelve más “inteligente” (explotando lo aprendido)

#### ✅ Recompensas

* +1 por comer (aprende a ir por la comida)
* -1 por chocar (aprende a evitarlo)
* 0 por vivir sin comer (neutral)

---

### 📊 Resultado esperado

* Inicialmente fallará mucho (recompensa total negativa o 0)
* Con el tiempo, empezará a sobrevivir más y comer
* En unos cientos de episodios ya se ven mejoras claras

---

### 🧪 ¿Y si lo ejecutamos?

Al final puedes probar episodios de prueba:

```python
obs, _ = env.reset()
done = False
while not done:
    state = obs_to_index(obs)
    action = np.argmax(q_table[state])
    obs, _, done, _, _ = env.step(action)
    env.render()
```

---

### ✅ Hasta aquí: Snake con Q-table

Ventajas:

* Fácil de entender
* Muy didáctico

Limitaciones:

* No escala a observaciones continuas o entornos complejos

---

### 🚀 Próximo paso: **Parte 3.2: Entrenamiento con DQN (Deep Q-Network)**


Perfecto. Vamos con la **Parte 3.2: Entrenamiento del agente Snake con DQN usando PyTorch**. Esto nos permitirá escalar el aprendizaje por refuerzo a entornos con observaciones continuas o complejas.

---

## 🧠 Parte 3.2: Agente DQN con PyTorch

### 🎯 Objetivo

Crear un agente que use una **red neuronal** para estimar los valores Q, en lugar de una tabla.

---

### 🧪 ¿Qué es un DQN (Deep Q-Network)?

Un DQN reemplaza la Q-table con una red neuronal que aprende a predecir $Q(s, a)$, es decir, **el valor esperado de tomar una acción en un estado**.

La función de pérdida para entrenar el DQN:

$$
\mathcal{L} = \left[ r + \gamma \cdot \max_{a'} Q_{\text{target}}(s', a') - Q(s, a) \right]^2
$$

---

### 🛠️ Requisitos

```bash
pip install torch gymnasium
```

---

### 🧠 Estructura del agente

1. Red neuronal para aproximar $Q(s, a)$
2. Búfer de experiencia (replay buffer)
3. Entrenamiento con mini-lotes
4. Política epsilon-greedy

---

### 💻 Código completo paso a paso

#### 1. 📦 `dqn_agent.py`

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from collections import deque
from snake_env import SnakeEnv

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, output_dim)
        )

    def forward(self, x):
        return self.net(x)


class DQNAgent:
    def __init__(self, state_dim, action_dim):
        self.model = DQN(state_dim, action_dim).to(device)
        self.target_model = DQN(state_dim, action_dim).to(device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=1e-3)
        self.criteria = nn.MSELoss()

        self.memory = deque(maxlen=10000)
        self.batch_size = 64
        self.gamma = 0.99
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.update_target_every = 10
        self.step_count = 0

    def act(self, state):
        if np.random.rand() < self.epsilon:
            return random.randint(0, 2)
        state = torch.FloatTensor(state).unsqueeze(0).to(device)
        with torch.no_grad():
            q_values = self.model(state)
        return torch.argmax(q_values).item()

    def remember(self, s, a, r, s_, done):
        self.memory.append((s, a, r, s_, done))

    def replay(self):
        if len(self.memory) < self.batch_size:
            return

        batch = random.sample(self.memory, self.batch_size)
        s, a, r, s_, done = zip(*batch)

        s = torch.FloatTensor(s).to(device)
        a = torch.LongTensor(a).unsqueeze(1).to(device)
        r = torch.FloatTensor(r).unsqueeze(1).to(device)
        s_ = torch.FloatTensor(s_).to(device)
        done = torch.BoolTensor(done).unsqueeze(1).to(device)

        q_values = self.model(s).gather(1, a)
        with torch.no_grad():
            max_next_q = self.target_model(s_).max(1, keepdim=True)[0]
            target = r + (1 - done.float()) * self.gamma * max_next_q

        loss = self.criteria(q_values, target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        self.step_count += 1
        if self.step_count % self.update_target_every == 0:
            self.target_model.load_state_dict(self.model.state_dict())

        self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)
```

---

#### 2. 🚀 Entrenamiento: `train_dqn.py`

```python
from dqn_agent import DQNAgent
from snake_env import SnakeEnv

env = SnakeEnv(grid_size=10)
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

agent = DQNAgent(state_dim, action_dim)

episodes = 1000

for ep in range(episodes):
    state, _ = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = agent.act(state)
        next_state, reward, done, _, _ = env.step(action)
        agent.remember(state, action, reward, next_state, done)
        agent.replay()
        state = next_state
        total_reward += reward

    if ep % 100 == 0:
        print(f"Ep {ep} | Total reward: {total_reward} | Epsilon: {agent.epsilon:.3f}")
```

---

### 📚 Explicación pedagógica del DQN

#### 🧠 ¿Por qué funciona?

* La red neuronal **aprende a predecir valores Q** para cada acción en cada estado.
* Las acciones buenas (como comer) obtienen valores altos.
* Acciones malas (como chocar) bajan el valor Q.
* El agente elige la acción con mayor valor Q (o explora al azar si $\epsilon$ es alto).

#### 🔁 Target network

Se mantiene una copia congelada del modelo (`target_model`) para evitar inestabilidad.

#### 🎲 Política epsilon-greedy

Similar al Q-table, se empieza explorando y se va explotando lo aprendido progresivamente.

---

### 🔍 Visualización (opcional)

```python
# Probar comportamiento del agente entrenado
state, _ = env.reset()
done = False
while not done:
    action = agent.act(state)
    state, _, done, _, _ = env.step(action)
    env.render()
```

---

### ✅ Resultado

* El agente puede aprender a jugar Snake sin intervención humana
* Mejora progresivamente su estrategia
* Aprende de la **recompensa** y el **castigo**, sin ser explícitamente programado

---

Aquí tienes una sección resumen pedagógica que puedes mostrar a tus alumnos junto con el código y la gráfica:

---

## 🧠 Resumen didáctico: Aprendizaje por refuerzo con DQN aplicado a Snake

### 🎮 ¿Qué es el aprendizaje por refuerzo?

Es una técnica donde un **agente aprende a tomar decisiones** observando un entorno, tomando acciones, y recibiendo recompensas o castigos. El objetivo es **maximizar las recompensas acumuladas**.

---

### 🧩 Elementos clave en nuestro ejemplo

| Componente         | Ejemplo en Snake                                       |
| ------------------ | ------------------------------------------------------ |
| **Agente**         | La serpiente                                           |
| **Entorno**        | El tablero donde se mueve la serpiente                 |
| **Estado (s)**     | Posición de comida, dirección, peligro de colisión     |
| **Acción (a)**     | Girar a la izquierda, seguir recto, girar a la derecha |
| **Recompensa (r)** | +1 si come, -1 si muere, 0 si no pasa nada             |

---

### 🔢 ¿Qué es un DQN?

Un **Deep Q-Network** usa una red neuronal para aprender el valor de cada acción en un estado dado:

$$
Q(s, a) \approx \text{Red Neuronal}(s)
$$

Esto permite resolver problemas donde los estados posibles son muchos o continuos (como vectores de observación).

---

### ⚙️ ¿Cómo aprende el agente?

1. **Explora** acciones al azar al principio (política ε-greedy).
2. **Almacena experiencias** (estado, acción, recompensa, siguiente estado).
3. **Entrena** la red para aproximar los mejores valores Q.
4. **Actualiza** una red objetivo periódicamente para estabilizar el aprendizaje.

---

### 📈 Resultados esperados

Con el tiempo, el agente:

* Aprende a **evitar morir**
* Aprende a **buscar comida**
* Mejora su rendimiento episodio tras episodio

---

### 📊 Visualización del rendimiento

La gráfica muestra cómo la **recompensa promedio** obtenida por el agente **aumenta con los episodios** de entrenamiento:

* Al principio, el agente muere rápido (recompensa negativa).
* Luego empieza a sobrevivir y comer (recompensas positivas).
* El aprendizaje se estabiliza al final.

---


Perfecto. Continuamos con la **Parte 4: Evaluación y análisis del agente entrenado**. Aquí se observa cómo se comporta el agente tras el entrenamiento y se analizan sus decisiones.

---

## 🧪 Parte 4: Evaluación y análisis del agente (Q-Table o DQN)

### 🎯 Objetivo

* Observar cómo se comporta el agente sin exploración (es decir, ya entrenado).
* Analizar decisiones correctas o errores.
* Validar si ha aprendido una estrategia útil o solo reglas básicas.

---

### 🧠 Comportamiento esperado tras el entrenamiento

| Agente      | Comportamiento esperado                                           |
| ----------- | ----------------------------------------------------------------- |
| **Q-Table** | Sobrevive más, evita muros, encuentra comida cercana              |
| **DQN**     | Busca comida con eficacia, evita trampas, puede generalizar mejor |

---

### 🖥️ Código de evaluación

#### Para Q-Table

```python
obs, _ = env.reset()
state = obs_to_index(obs)
done = False
total_reward = 0

while not done:
    action = np.argmax(q_table[state])
    obs, reward, done, _, _ = env.step(action)
    state = obs_to_index(obs)
    total_reward += reward
    env.render()

print(f"Recompensa total (Q-Table): {total_reward}")
```

#### Para DQN

```python
obs, _ = env.reset()
done = False
total_reward = 0

while not done:
    state_tensor = torch.FloatTensor(obs).unsqueeze(0).to(device)
    with torch.no_grad():
        action = torch.argmax(agent.model(state_tensor)).item()
    obs, reward, done, _, _ = env.step(action)
    total_reward += reward
    env.render()

print(f"Recompensa total (DQN): {total_reward}")
```

---

### 📚 Evaluación pedagógica

#### 🔍 ¿Qué observar en la evaluación?

1. **¿Evita morir rápidamente?**
2. **¿Se orienta hacia la comida?**
3. **¿Sigue patrones predecibles o reacciona al entorno?**

#### 🔁 ¿Es necesario volver a entrenar?

* Si el agente muere muy pronto: revisa recompensas, tasa de aprendizaje, o el tamaño de la red.
* Si se queda girando en bucle: podría estar aprendiendo una política local subóptima.

---

### 🧰 Métricas útiles

Además de la recompensa total, puedes registrar:

* Número de episodios superados sin morir
* Número de comidas consumidas por episodio
* Tiempo promedio de supervivencia (en ticks)

---

Perfecto. Cerramos con la **Parte 5: Por qué funcionan los refuerzos y castigos en aprendizaje por refuerzo**, centrándonos en su impacto sobre el comportamiento del agente.

---

## 🧠 Parte 5: ¿Por qué funcionan los refuerzos y castigos?

### 🎯 Objetivo

Explicar de forma clara y pedagógica cómo y por qué las **recompensas positivas** y los **castigos negativos** modifican la conducta del agente para que aprenda estrategias útiles.

---

## 🔄 El bucle de aprendizaje por refuerzo

Cada decisión que toma el agente genera consecuencias en forma de recompensa. A través de muchas repeticiones, el agente **aprende a predecir y maximizar** aquellas acciones que llevan a mejores resultados.

```text
Estado s → Acción a → Nueva observación s' → Recompensa r → Actualizar conocimiento
```

---

## ✅ Recompensas: refuerzos positivos

### 🟩 ¿Qué es una recompensa?

Es un valor numérico que **informa al agente de lo buena que fue su acción**.

### 🧠 ¿Qué genera una recompensa positiva?

* Fortalece la asociación entre un estado y una acción.
* El agente “memoriza” que esa acción trae beneficios.
* En Snake: comer comida → +1 → el agente aprende a dirigirse hacia ella.

> Ejemplo:
> Si en el estado `s` ir a la derecha lleva a comida, se aumenta $Q(s, \text{derecha})$.

---

## ❌ Castigos: refuerzos negativos

### 🟥 ¿Qué es un castigo?

Es una recompensa negativa que **informa de una mala acción**.

### 🧠 ¿Qué genera una penalización?

* Debilita la tendencia a repetir una acción en ese contexto.
* En Snake: chocar con un muro o consigo mismo → -1 → el agente evita esas acciones.

> Sin castigo por morir, el agente podría repetir patrones peligrosos sin consecuencia.

---

## 🔍 ¿Por qué no recompensamos solo al final?

Si el agente solo recibiera una recompensa al final de un episodio (por ejemplo, al morir o ganar), sería difícil **asociar qué decisiones fueron útiles**.

El aprendizaje por refuerzo funciona mejor cuando hay señales frecuentes:

* 🍎 Comer comida: **recompensa intermedia**
* 💀 Morir: **castigo claro**
* ➖ Sobrevivir sin novedad: **recompensa neutra (0)**

---

## 📈 ¿Qué ocurre con el tiempo?

* Al principio, el agente **explora** todo tipo de acciones.
* Luego, aprende a **explotar** las que llevan a mayor recompensa acumulada.
* Gracias a la retroalimentación continua (refuerzo/castigo), mejora su rendimiento.

---

## 🧬 ¿Por qué esto funciona tan bien?

Este proceso está **inspirado en el aprendizaje animal** y humano:

* Se aprende por **ensayo y error**
* Se recuerda lo que **funciona**
* Se evita lo que **genera consecuencias negativas**

> En inteligencia artificial, esta lógica es implementada mediante fórmulas de actualización de valor (Q-learning o redes neuronales en DQN).

---

### ✅ Conclusión

Los refuerzos y castigos funcionan porque:

* Proveen una **señal inmediata** del valor de cada acción.
* Permiten **aprender sin supervisión explícita**.
* Incentivan al agente a **mejorar su estrategia** con cada experiencia.

---

