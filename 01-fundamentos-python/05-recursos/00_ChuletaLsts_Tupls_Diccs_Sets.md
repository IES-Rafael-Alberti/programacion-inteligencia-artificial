# Chuleta

# 🐍 **Funciones y Operaciones con Estructuras de Datos en Python**

---

## 🧱 **LISTAS**

### 🧩 **Creación y operaciones básicas**

| Operación         | Descripción                                             | Ejemplo                             |
| ----------------- | ------------------------------------------------------- | ----------------------------------- |
| Crear lista       | Se define con corchetes `[]`                            | `nums = [1, 2, 3, 4]`               |
| Lista vacía       | Sin elementos                                           | `vacia = []`                        |
| `list(iterable)`  | Convierte otro iterable (tupla, string, rango) en lista | `list('hola')  # ['h','o','l','a']` |
| Concatenar listas | Une dos listas con `+`                                  | `[1,2] + [3,4]  # [1,2,3,4]`        |
| Repetir lista     | Repite los elementos                                    | `[1,2]*3  # [1,2,1,2,1,2]`          |
| Longitud          | Número de elementos                                     | `len([10, 20, 30])  # 3`            |
| Pertenencia       | Comprueba si un elemento está                           | `3 in [1,2,3]  # True`              |

---

### 🪄 **Indexación y slicing**

| Operación       | Descripción          | Ejemplo                      |
| --------------- | -------------------- | ---------------------------- |
| Índice          | Acceder por posición | `a = [10,20,30]; a[1]  # 20` |
| Índice negativo | Desde el final       | `a[-1]  # 30`                |
| Slice simple    | Sublista             | `a[0:2]  # [10,20]`          |
| Slice con salto | Paso entre elementos | `a[::2]  # [10,30]`          |
| Reversa         | Copia invertida      | `a[::-1]  # [30,20,10]`      |

---

### ⚙️ **Modificación de listas**

| Método                  | Descripción                               | Ejemplo                          |
| ----------------------- | ----------------------------------------- | -------------------------------- |
| Asignar valor           | Cambia elemento                           | `a[1] = 99`                      |
| Asignar por rango       | Reemplaza porciones                       | `a[1:3] = [7,8]`                 |
| Añadir con `append()`   | Añade un elemento al final                | `a.append(4)`                    |
| Insertar con `insert()` | Inserta en posición concreta              | `a.insert(1, 'hola')`            |
| Extender con `extend()` | Añade varios elementos                    | `a.extend([5,6,7])`              |
| Eliminar con `del`      | Borra por índice o rango                  | `del a[0]`                       |
| `remove(x)`             | Elimina primera aparición de `x`          | `a.remove(3)`                    |
| `pop()`                 | Elimina y devuelve último (o índice dado) | `a.pop()  # último` / `a.pop(0)` |
| `clear()`               | Vacía la lista                            | `a.clear()`                      |

---

### 🔍 **Búsqueda y conteo**

| Método     | Descripción                      | Ejemplo                     |
| ---------- | -------------------------------- | --------------------------- |
| `index(x)` | Devuelve índice del primer `x`   | `[10,20,30].index(20)  # 1` |
| `count(x)` | Cuenta cuántas veces aparece `x` | `[1,2,2,3].count(2)  # 2`   |

---

### 🧮 **Orden y reversa**

| Método               | Descripción                       | Ejemplo                                      |
| -------------------- | --------------------------------- | -------------------------------------------- |
| `sort()`             | Ordena in place (modifica lista)  | `a = [3,1,2]; a.sort(); print(a)  # [1,2,3]` |
| `sort(reverse=True)` | Orden descendente                 | `a.sort(reverse=True)`                       |
| `sorted()`           | Devuelve una nueva lista ordenada | `sorted([3,1,2])  # [1,2,3]`                 |
| `reverse()`          | Invierte la lista actual          | `a.reverse()`                                |

---

### 🧠 **Copia y duplicación**

| Método    | Descripción                | Ejemplo        |
| --------- | -------------------------- | -------------- |
| `copy()`  | Crea una copia superficial | `b = a.copy()` |
| `list(a)` | Otra forma de copiar       | `b = list(a)`  |
| `a[:]`    | Copia por slicing          | `b = a[:]`     |

---

### 🧩 **Funciones integradas útiles**

| Función               | Descripción                                | Ejemplo                                          |
| --------------------- | ------------------------------------------ | ------------------------------------------------ |
| `sum(lista)`          | Suma los elementos numéricos               | `sum([1,2,3])  # 6`                              |
| `max(lista)`          | Máximo                                     | `max([4,9,2])  # 9`                              |
| `min(lista)`          | Mínimo                                     | `min([4,9,2])  # 2`                              |
| `all(lista)`          | True si todos los elementos son verdaderos | `all([1, True, 5])  # True`                      |
| `any(lista)`          | True si al menos uno es verdadero          | `any([0, False, 3])  # True`                     |
| `enumerate(lista)`    | Itera con índice y valor                   | `for i,v in enumerate(['a','b']): print(i,v)`    |
| `zip()`               | Combina varias listas                      | `list(zip([1,2],[3,4]))  # [(1,3),(2,4)]`        |
| `map(func, lista)`    | Aplica una función a cada elemento         | `list(map(str, [1,2,3]))  # ['1','2','3']`       |
| `filter(func, lista)` | Filtra según condición                     | `list(filter(lambda x:x>2, [1,2,3,4]))  # [3,4]` |
| `reversed(lista)`     | Iterador invertido                         | `list(reversed([1,2,3]))  # [3,2,1]`             |

---

### 🧠 **Comprensión de listas**

| Tipo               | Ejemplo                                                              |
| ------------------ | -------------------------------------------------------------------- |
| Comprensión simple | `[x**2 for x in [1,2,3]]  # [1,4,9]`                                 |
| Con condición      | `[x for x in range(10) if x%2==0]  # [0,2,4,6,8]`                    |
| Anidada            | `[(x,y) for x in [1,2] for y in [3,4]]  # [(1,3),(1,4),(2,3),(2,4)]` |

---

### 🧰 **Otras operaciones útiles**

| Operación                    | Descripción                          | Ejemplo                         |
| ---------------------------- | ------------------------------------ | ------------------------------- |
| Unpacking                    | Extraer valores directamente         | `a,b,c = [1,2,3]`               |
| Multiplicación en asignación | Repetir valores iniciales            | `a = [0]*5  # [0,0,0,0,0]`      |
| `==`                         | Compara igualdad                     | `[1,2]==[1,2]  # True`          |
| `is`                         | Compara identidad (misma referencia) | `a is b  # False (si es copia)` |

---

## 🔹 **TUPLAS**

*(Estructura inmutable similar a la lista)*

| Operación / Método     | Descripción                    | Ejemplo                           |
| ---------------------- | ------------------------------ | --------------------------------- |
| Crear tupla            | Con paréntesis o sin ellos     | `t = (1,2,3)` / `t = 1,2,3`       |
| Tupla vacía            | Sin elementos                  | `v = ()`                          |
| Tupla unitaria         | Un solo elemento               | `t1 = (5,)`                       |
| Convertir a tupla      | Desde lista o string           | `tuple([1,2,3])` / `tuple('abc')` |
| Concatenar             | Une tuplas                     | `(1,2)+(3,4)`                     |
| Repetir                | Repite elementos               | `(1,2)*2  # (1,2,1,2)`            |
| Longitud               | Tamaño                         | `len(t)`                          |
| Pertenencia            | Comprueba si está              | `2 in t`                          |
| Acceso                 | Índice o slicing               | `t[0]`, `t[1:3]`                  |
| `count(x)`             | Cuántas veces aparece          | `t.count(1)`                      |
| `index(x)`             | Posición de elemento           | `t.index(2)`                      |
| Desempaquetado         | Extrae valores                 | `a,b,c = t`                       |
| Desempaquetado parcial | Con `*`                        | `a,*b,c = (1,2,3,4,5)`            |
| Conversión             | Cambiar a lista para modificar | `list(t)`                         |
| Iteración              | En bucle                       | `for x in t:`                     |
| Funciones integradas   | `sum(t)`, `max(t)`, `min(t)`   |                                   |
| Revertir               | `tuple(reversed(t))`           |                                   |
| Comparar               | `(1,2) < (1,3)` → `True`       |                                   |
| Uso en diccionario     | Como clave                     | `{(1,2):"inicio"}`                |

---

## 🟢 **DICCIONARIOS**

*(Estructura clave-valor mutable)*

| Operación / Método         | Descripción                        | Ejemplo                   |
| -------------------------- | ---------------------------------- | ------------------------- |
| Crear diccionario          | Con llaves `{}`                    | `d = {'a':1, 'b':2}`      |
| Vacío                      | Sin elementos                      | `v = {}`                  |
| `dict()`                   | Desde pares o listas               | `dict([(1,'a'),(2,'b')])` |
| Acceso                     | Por clave                          | `d['a']  # 1`             |
| Asignar / Modificar        | Agregar o cambiar valor            | `d['c'] = 3`              |
| Eliminar clave             | Con `del`                          | `del d['b']`              |
| `pop(clave)`               | Elimina y devuelve valor           | `d.pop('a')`              |
| `popitem()`                | Elimina último par                 | `d.popitem()`             |
| `clear()`                  | Vacía el diccionario               | `d.clear()`               |
| `keys()`                   | Devuelve claves                    | `list(d.keys())`          |
| `values()`                 | Devuelve valores                   | `list(d.values())`        |
| `items()`                  | Devuelve pares (tuplas)            | `list(d.items())`         |
| `get(clave, valor_def)`    | Devuelve valor o por defecto       | `d.get('x', 0)`           |
| `update(otro_dict)`        | Fusiona diccionarios               | `d.update({'c':3})`       |
| `in`                       | Comprueba clave existente          | `'a' in d`                |
| `len()`                    | Número de pares                    | `len(d)`                  |
| Copiar                     | `d.copy()`                         |                           |
| Iterar                     | `for k,v in d.items(): print(k,v)` |                           |
| Comprensión de diccionario | `{x:x**2 for x in range(3)}`       |                           |

---

## 🔸 **SETS (Conjuntos)**

*(Estructura sin duplicados, mutable y no ordenada)*

| Operación / Método       | Descripción                        | Ejemplo                            |     |     |
| ------------------------ | ---------------------------------- | ---------------------------------- | --- | --- |
| Crear conjunto           | `{}` o `set()`                     | `s = {1,2,3}` / `s = set([1,2,3])` |     |     |
| Vacío                    | Con `set()`                        | `v = set()`                        |     |     |
| Añadir                   | `add()`                            | `s.add(4)`                         |     |     |
| Eliminar                 | `remove()` o `discard()`           | `s.remove(2)` / `s.discard(5)`     |     |     |
| Extraer                  | `pop()` elimina elemento aleatorio | `s.pop()`                          |     |     |
| Vaciar                   | `clear()`                          | `s.clear()`                        |     |     |
| Unión                    | `union()` o `                      | `                                  | `s1 | s2` |
| Intersección             | `intersection()` o `&`             | `s1 & s2`                          |     |     |
| Diferencia               | `difference()` o `-`               | `s1 - s2`                          |     |     |
| Diferencia simétrica     | `symmetric_difference()` o `^`     | `s1 ^ s2`                          |     |     |
| Subconjunto              | `issubset()`                       | `s1.issubset(s2)`                  |     |     |
| Superconjunto            | `issuperset()`                     | `s1.issuperset(s2)`                |     |     |
| Disjuntos                | `isdisjoint()`                     | `s1.isdisjoint(s2)`                |     |     |
| Longitud                 | `len(s)`                           |                                    |     |     |
| Pertenencia              | `in`                               | `2 in s`                           |     |     |
| Copiar                   | `copy()`                           |                                    |     |     |
| Comprensión de conjuntos | `{x**2 for x in range(5)}`         |                                    |     |     |

---

## 🧩 **Resumen rápido de mutabilidad**

| Tipo      | Mutable | Ordenado | Permite duplicados | Sintaxis principal |
| --------- | ------- | -------- | ------------------ | ------------------ |
| **list**  | ✅ Sí    | ✅ Sí     | ✅ Sí               | `[ ]`              |
| **tuple** | ❌ No    | ✅ Sí     | ✅ Sí               | `( )`              |
| **dict**  | ✅ Sí    | ✅ (3.7+) | ❌ Claves únicas    | `{clave: valor}`   |
| **set**   | ✅ Sí    | ❌ No     | ❌ No               | `{ }` o `set()`    |

---

