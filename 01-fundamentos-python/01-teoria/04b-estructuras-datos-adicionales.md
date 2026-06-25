
# 🧱 **Estructuras de Datos Adicionales en la Librería Estándar**
**Además de las cuatro estructuras básicas** (`list`, `tuple`, `dict`, `set`), **Python incluye en la librería estándar varias estructuras adicionales** que *no requieren instalar nada* (no son externas como NumPy o Pandas).

Estas estructuras están sobre todo en el módulo **`collections`** y en **`array`** y **`queue`**, y amplían las capacidades de las básicas.

Os dejo un resumen con las **principales y sus usos**, para que sepas cuáles merece la pena mencionar o practicar:

---

## 🧩 1. `collections.namedtuple()`

👉 Es una **tupla con nombre de campos**, que permite acceder por índice o por nombre.

```python
from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'edad'])
p = Persona('Ana', 25)

print(p.nombre)  # Ana
print(p[1])      # 25
```

📘 *Ideal cuando necesitas tuplas inmutables pero con significado semántico (tipo registro o fila).*

---

## 🔁 2. `collections.deque`

👉 Es una **cola doble** (doble-ended queue), más eficiente que las listas para añadir o quitar elementos al principio o al final.

```python
from collections import deque

cola = deque([1, 2, 3])
cola.append(4)        # añade al final
cola.appendleft(0)    # añade al principio
print(cola)           # deque([0, 1, 2, 3, 4])
cola.pop()            # quita del final
cola.popleft()        # quita del principio
```

📘 *Muy útil para implementar colas, buffers, o recorridos en anchura (BFS).*

---

## 📦 3. `collections.Counter`

👉 Es un **contador de elementos**, como un diccionario especializado para contar repeticiones.

```python
from collections import Counter

frutas = ['manzana', 'pera', 'manzana', 'uva', 'pera', 'manzana']
c = Counter(frutas)
print(c)              # Counter({'manzana': 3, 'pera': 2, 'uva': 1})
print(c.most_common(1))  # [('manzana', 3)]
```

📘 *Perfecto para frecuencias, histogramas o conteo de palabras.*

---

## 🧮 4. `collections.defaultdict`

👉 Es un **diccionario con valor por defecto**, que evita errores `KeyError` al acceder a claves inexistentes.

```python
from collections import defaultdict

d = defaultdict(int)
d['x'] += 1
d['y'] += 3
print(d)  # defaultdict(<class 'int'>, {'x': 1, 'y': 3})
```

📘 *Ideal para agrupar datos o acumular contadores sin inicializar claves.*

---

## 🗂️ 5. `collections.OrderedDict`

👉 Como un diccionario normal, pero **mantiene el orden de inserción** (aunque desde Python 3.7 los dict normales ya lo hacen).

```python
from collections import OrderedDict

od = OrderedDict()
od['uno'] = 1
od['dos'] = 2
print(od)  # OrderedDict([('uno', 1), ('dos', 2)])
```

📘 *Sigue siendo útil para versiones antiguas o para garantizar orden explícitamente.*

---

## 📚 6. `collections.ChainMap`

👉 Agrupa varios diccionarios como si fueran uno solo, sin copiarlos.

```python
from collections import ChainMap

config_default = {'color': 'azul', 'modo': 'claro'}
config_usuario = {'modo': 'oscuro'}
config = ChainMap(config_usuario, config_default)
print(config['color'])  # azul
print(config['modo'])   # oscuro (toma prioridad el primero)
```

📘 *Útil para gestionar configuraciones con herencia o prioridades.*

---

## 🧱 7. `array.array`

👉 Es una **lista optimizada de números del mismo tipo**, más compacta en memoria que una lista normal.

```python
from array import array

a = array('i', [1, 2, 3, 4])  # 'i' = entero
a.append(5)
print(a)
print(a[0])   # 1
```

📘 *Buena alternativa si trabajas con grandes volúmenes de datos numéricos sin llegar a usar NumPy.*

---

## 🕒 8. `queue.Queue`, `LifoQueue`, `PriorityQueue`

👉 Colas seguras para **procesos concurrentes o multi-hilo**.

```python
from queue import Queue

cola = Queue()
cola.put('tarea1')
cola.put('tarea2')
print(cola.get())  # tarea1
```

📘 *Muy útil si en el futuro tus alumnos ven procesamiento en paralelo o asincronía.*

---

## 🧰 9. `heapq`

👉 Implementa **colas de prioridad** (min-heaps) usando listas.

```python
import heapq

nums = [5, 3, 8, 1]
heapq.heapify(nums)
print(heapq.heappop(nums))  # 1 (mínimo)
```

📘 *Ideal para algoritmos de búsqueda, Dijkstra, A*, o manejo eficiente de prioridades.*

---

## 🧾 10. `bisect`

👉 Permite **insertar elementos en una lista ordenada** manteniendo el orden sin tener que ordenar de nuevo.

```python
import bisect

lista = [1, 3, 4, 7]
bisect.insort(lista, 5)
print(lista)  # [1, 3, 4, 5, 7]
```

📘 *Útil en estructuras de búsqueda ordenadas sin librerías externas.*

---

# ✅ **Resumen: Cuándo usar cada una**

| Tipo          | Mutable | Ordenado | Duplicados      | Ideal para…                 |
| ------------- | ------- | -------- | --------------- | --------------------------- |
| `list`        | ✅ Sí    | ✅ Sí     | ✅ Sí            | Secuencias generales        |
| `tuple`       | ❌ No    | ✅ Sí     | ✅ Sí            | Datos inmutables            |
| `dict`        | ✅ Sí    | ✅ (3.7+) | ❌ Claves únicas | Pares clave–valor           |
| `set`         | ✅ Sí    | ❌ No     | ❌ No            | Eliminación de duplicados   |
| `deque`       | ✅ Sí    | ✅ Sí     | ✅ Sí            | Colas y pilas eficientes    |
| `Counter`     | ✅ Sí    | ❌ No     | ✅ Sí            | Conteos rápidos             |
| `defaultdict` | ✅ Sí    | ❌ No     | ✅ Sí            | Agrupaciones por defecto    |
| `array`       | ✅ Sí    | ✅ Sí     | ✅ Sí            | Listas numéricas compactas  |
| `heapq`       | ✅ Sí    | ❌ No     | ✅ Sí            | Colas de prioridad          |
| `Queue`       | ✅ Sí    | ❌ No     | ✅ Sí            | Hilos y concurrencia        |
| `ChainMap`    | ✅ Sí    | ✅ Sí     | ✅ Sí            | Configuraciones jerárquicas |

---

