# Búsqueda y juegos: una introducción a la IA clásica

> **Apéndice voluntario de UD11.** No forma parte de la evaluación ordinaria ni
> presupone conocimientos de ML. Duración orientativa: 3–4 horas.

## Para qué sirve este apéndice

En machine learning un modelo aprende patrones a partir de datos. En muchos
problemas, en cambio, conocemos las reglas y podemos explorar directamente las
posibles acciones. La búsqueda permite encontrar una ruta o una secuencia de
decisiones sin entrenar un modelo.

Este enfoque sigue siendo útil en planificación, navegación, juegos, resolución
de problemas y como pieza de sistemas más amplios. También ofrece una referencia
clara para comparar qué aporta el aprendizaje automático y qué aporta un agente
basado en un LLM.

## Resultados de aprendizaje del apéndice

Al terminar, podrás:

- describir un problema mediante estados, acciones, transiciones, objetivo y
  coste;
- comparar DFS, BFS y A* en un mapa pequeño;
- explicar por qué BFS encuentra una ruta mínima cuando todas las acciones
  cuestan lo mismo y qué información adicional usa A*;
- seguir una decisión de minimax en un juego determinista de dos jugadores;
- explicar cómo la poda alfa-beta reduce exploración sin cambiar la decisión
  minimax;
- distinguir búsqueda con reglas conocidas de aprendizaje a partir de datos y de
  generación de texto con LLM.

## 1. Representar un problema de búsqueda

Un problema de búsqueda suele definirse mediante:

| Elemento | Pregunta | Ejemplo: salir de un laberinto |
| --- | --- | --- |
| Estado | ¿Dónde estoy? | Coordenada de la casilla actual. |
| Estado inicial | ¿Dónde empiezo? | Casilla `S`. |
| Acciones | ¿Qué puedo hacer? | Moverme arriba, abajo, izquierda o derecha. |
| Transición | ¿Qué ocurre si actúo? | Paso a una casilla vecina transitable. |
| Objetivo | ¿Cuándo termino? | Al alcanzar la casilla `G`. |
| Coste | ¿Cuánto cuesta una solución? | Número de movimientos o coste del terreno. |

El algoritmo no aprende las reglas: las reglas están descritas en el problema.
Lo que busca es una secuencia de acciones que lleve del inicio al objetivo.

## 2. DFS, BFS y A*

### Búsqueda en profundidad (DFS)

DFS (*Depth-First Search*) explora una rama hasta donde puede y luego retrocede.
Es sencilla y puede usar poca memoria, pero no garantiza encontrar la ruta más
corta. En grafos con ciclos hay que registrar los estados ya visitados.

### Búsqueda en anchura (BFS)

BFS (*Breadth-First Search*) explora primero todos los estados a distancia 1,
después los de distancia 2 y así sucesivamente. Si todas las acciones tienen el
mismo coste, encuentra una ruta con el menor número de pasos. Su coste en memoria
puede crecer mucho con el factor de ramificación.

### Búsqueda A*

A* ordena los estados por:

```text
f(n) = g(n) + h(n)
```

- `g(n)`: coste real desde el inicio hasta `n`.
- `h(n)`: estimación del coste que falta desde `n` hasta el objetivo.
- `f(n)`: coste estimado de una solución que pasa por `n`.

Si la heurística no sobreestima el coste restante (es admisible), A* puede
encontrar una solución óptima. Una heurística más informativa suele evitar
explorar zonas irrelevantes. En una cuadrícula con movimientos ortogonales, la
distancia Manhattan es una heurística natural si no hay atajos ni movimientos
diagonales.

| Algoritmo | Usa información del objetivo | ¿Ruta mínima? | Memoria, en general |
| --- | --- | --- | --- |
| DFS | No | No | Menor que BFS en algunos casos. |
| BFS | No | Sí, si los costes son iguales. | Alta. |
| A* | Sí, mediante `h(n)`. | Sí, con una heurística admisible y las condiciones habituales. | Puede ser alta. |

La práctica `ia_clasica_busqueda.py` ejecuta los tres algoritmos sobre el mismo
laberinto y permite comparar la ruta y el número de estados expandidos.

## 3. Juegos adversarios: minimax

En una búsqueda de rutas, el entorno no intenta frustrar nuestro objetivo. En un
juego adversario, cada jugador elige acciones y sus objetivos compiten.

Minimax se aplica a juegos deterministas, por turnos, de suma cero y con
información completa:

1. Construye o explora el árbol de jugadas posibles.
2. Asigna una utilidad a los estados terminales (por ejemplo, victoria, empate o
   derrota).
3. Supone que ambos jugadores eligen siempre la mejor respuesta para sí mismos.
4. En los turnos propios maximiza la utilidad; en los del rival la minimiza.

En tres en raya, se puede usar `+1` para victoria de `X`, `-1` para victoria de
`O` y `0` para empate. El algoritmo elige una jugada que no depende de que el
rival cometa un error.

### Poda alfa-beta

La poda alfa-beta deja de explorar ramas que ya no pueden cambiar la decisión:

- `alfa`: mejor resultado que puede garantizar el jugador maximizador;
- `beta`: mejor resultado que puede garantizar el jugador minimizador.

Cuando `alfa >= beta`, explorar más esa rama no puede mejorar la decisión. La
poda conserva el resultado de minimax; su eficacia depende del orden en que se
examinen las jugadas.

La práctica `ia_clasica_minimax.py` compara el número de nodos examinados con y
sin poda alfa-beta y muestra una jugada óptima para una posición de tres en raya.

## 4. Qué relación tiene con la IA actual

| Enfoque | De dónde obtiene la decisión | Ejemplo |
| --- | --- | --- |
| Búsqueda clásica | Reglas, acciones y objetivo explícitos. | A* encuentra una ruta de coste mínimo. |
| ML/DL | Patrones aprendidos de ejemplos o interacción. | Un clasificador aprende a reconocer imágenes. |
| LLM | Patrones lingüísticos aprendidos durante el entrenamiento y el contexto recibido. | Generar una explicación o proponer código. |
| Agente | Coordina un modelo, estado, herramientas y un ciclo de acciones. | Consultar datos, ejecutar una herramienta y comprobar el resultado. |

Un agente con LLM puede planificar pasos en lenguaje, pero eso no lo convierte
automáticamente en un buscador óptimo. Cuando las reglas y el espacio de estados
son explícitos, un algoritmo de búsqueda puede ofrecer garantías más claras. En
otros problemas, los modelos aprendidos manejan mejor datos ambiguos o patrones
difíciles de especificar a mano. Se pueden combinar ambos enfoques.

## Secuencia sugerida (3–4 horas)

| Bloque | Duración | Actividad |
| --- | ---: | --- |
| Modelado del problema | 20–30 min | Definir estados, acciones y objetivo con un laberinto en la pizarra. |
| DFS y BFS | 45–60 min | Ejecutar `ia_clasica_busqueda.py`, comparar rutas y explicar estados visitados. |
| Heurística y A* | 35–45 min | Examinar la distancia Manhattan; cambiar mapa u objetivo y comparar expansiones. |
| Minimax | 45–60 min | Seguir el árbol de tres en raya y comprobar jugadas ganadoras y defensivas. |
| Alfa-beta y cierre | 30–45 min | Comparar nodos examinados y relacionar búsqueda, ML, LLM y agentes. |

## Preguntas para discutir

1. ¿Por qué DFS puede encontrar una ruta más larga que BFS?
2. ¿Qué puede pasar si la heurística de A* sobreestima el coste que falta?
3. ¿Por qué minimax supone que el rival responde bien?
4. ¿La poda alfa-beta cambia la jugada elegida o reduce el trabajo para hallarla?
5. ¿Qué parte de un agente real convendría resolver con reglas y búsqueda, y qué
   parte podría beneficiarse de un modelo aprendido?

## Material de trabajo

- [Ejemplos de búsqueda, BFS, DFS y A*](../02-ejemplos/ia_clasica_busqueda.py).
- [Ejemplo de minimax y poda alfa-beta](../02-ejemplos/ia_clasica_minimax.py).

El apéndice es formativo y optativo. No añade una calificación ni cambia la
ponderación de RA/CE del módulo.
