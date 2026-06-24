# 🧠 **Funciones y Operaciones de NumPy**

> Importación base:
>
> ```python
> import numpy as np
> ```

---

## 🧩 **1. Creación de Arrays**

| Función         | Descripción                                 | Ejemplo                                        |
| --------------- | ------------------------------------------- | ---------------------------------------------- |
| `np.array()`    | Crea un array a partir de una lista o tupla | `a = np.array([1, 2, 3])`                      |
| `np.zeros()`    | Array de ceros                              | `np.zeros((2,3))`                              |
| `np.ones()`     | Array de unos                               | `np.ones((3,3))`                               |
| `np.empty()`    | Array vacío (sin inicializar)               | `np.empty((2,2))`                              |
| `np.full()`     | Array lleno con un valor                    | `np.full((2,2), 5)`                            |
| `np.arange()`   | Secuencia con paso fijo                     | `np.arange(0,10,2)` → `[0,2,4,6,8]`            |
| `np.linspace()` | Secuencia con número de puntos fijo         | `np.linspace(0,1,5)` → `[0.,0.25,0.5,0.75,1.]` |
| `np.eye()`      | Matriz identidad                            | `np.eye(3)`                                    |
| `np.identity()` | Igual que `eye()`                           | `np.identity(4)`                               |
| `np.diag()`     | Crea o extrae diagonal                      | `np.diag([1,2,3])`                             |

---

## 🎲 **2. Arrays aleatorios**

| Función               | Descripción                               | Ejemplo                         |
| --------------------- | ----------------------------------------- | ------------------------------- |
| `np.random.rand()`    | Aleatorios uniformes \[0,1)               | `np.random.rand(2,3)`           |
| `np.random.randn()`   | Aleatorios normales (media 0, varianza 1) | `np.random.randn(3)`            |
| `np.random.randint()` | Enteros aleatorios                        | `np.random.randint(0,10,(2,3))` |
| `np.random.choice()`  | Elección aleatoria                        | `np.random.choice([1,2,3,4])`   |
| `np.random.seed()`    | Fija semilla aleatoria                    | `np.random.seed(42)`            |

---

## 🧮 **3. Propiedades de los arrays**

| Propiedad   | Descripción               | Ejemplo      |
| ----------- | ------------------------- | ------------ |
| `.shape`    | Dimensiones del array     | `a.shape`    |
| `.ndim`     | Número de dimensiones     | `a.ndim`     |
| `.size`     | Número total de elementos | `a.size`     |
| `.dtype`    | Tipo de datos             | `a.dtype`    |
| `.itemsize` | Bytes por elemento        | `a.itemsize` |

---

## 🧱 **4. Indexado y slicing**

| Operación | Descripción                 | Ejemplo    |
| --------- | --------------------------- | ---------- |
| `a[0,1]`  | Acceso a elemento           | `mat[0,1]` |
| `a[:,1]`  | Toda la columna 1           | `mat[:,1]` |
| `a[1,:]`  | Toda la fila 1              | `mat[1,:]` |
| `a[::2]`  | Elementos cada 2 posiciones | `a[::2]`   |
| `a[a>5]`  | Filtrado booleano           | `a[a>5]`   |

---

## 🔄 **5. Operaciones básicas**

| Función / Operador | Descripción                     | Ejemplo            |
| ------------------ | ------------------------------- | ------------------ |
| `+`, `-`, `*`, `/` | Operaciones elemento a elemento | `a+b`, `a*b`       |
| `np.add()`         | Suma                            | `np.add(a,b)`      |
| `np.subtract()`    | Resta                           | `np.subtract(a,b)` |
| `np.multiply()`    | Multiplicación                  | `np.multiply(a,b)` |
| `np.divide()`      | División                        | `np.divide(a,b)`   |
| `np.power()`       | Potencia                        | `np.power(a,2)`    |
| `np.sqrt()`        | Raíz cuadrada                   | `np.sqrt(a)`       |
| `np.exp()`         | Exponencial                     | `np.exp(a)`        |
| `np.log()`         | Logaritmo natural               | `np.log(a)`        |

---

## 📊 **6. Estadística y agregación**

| Función           | Descripción         | Ejemplo                |
| ----------------- | ------------------- | ---------------------- |
| `np.sum()`        | Suma total          | `np.sum(a)`            |
| `np.mean()`       | Media               | `np.mean(a)`           |
| `np.median()`     | Mediana             | `np.median(a)`         |
| `np.std()`        | Desviación estándar | `np.std(a)`            |
| `np.var()`        | Varianza            | `np.var(a)`            |
| `np.min()`        | Mínimo              | `np.min(a)`            |
| `np.max()`        | Máximo              | `np.max(a)`            |
| `np.argmin()`     | Índice del mínimo   | `np.argmin(a)`         |
| `np.argmax()`     | Índice del máximo   | `np.argmax(a)`         |
| `np.percentile()` | Percentil           | `np.percentile(a, 50)` |

---

## 🧩 **7. Álgebra lineal (np.linalg)**

| Función            | Descripción                  | Ejemplo             |
| ------------------ | ---------------------------- | ------------------- |
| `np.dot()`         | Producto escalar o matricial | `np.dot(a,b)`       |
| `np.matmul()`      | Multiplicación de matrices   | `np.matmul(A,B)`    |
| `np.linalg.inv()`  | Inversa de una matriz        | `np.linalg.inv(A)`  |
| `np.linalg.det()`  | Determinante                 | `np.linalg.det(A)`  |
| `np.linalg.eig()`  | Autovalores y autovectores   | `np.linalg.eig(A)`  |
| `np.linalg.norm()` | Norma vectorial              | `np.linalg.norm(a)` |

---

## 🧱 **8. Manipulación de forma (shape)**

| Función            | Descripción                     | Ejemplo                     |
| ------------------ | ------------------------------- | --------------------------- |
| `np.reshape()`     | Cambia la forma                 | `a.reshape(2,3)`            |
| `np.ravel()`       | Aplana el array                 | `a.ravel()`                 |
| `np.flatten()`     | Crea copia aplanada             | `a.flatten()`               |
| `np.transpose()`   | Transpone filas y columnas      | `a.T`                       |
| `np.expand_dims()` | Añade nueva dimensión           | `np.expand_dims(a, axis=0)` |
| `np.squeeze()`     | Elimina dimensiones de tamaño 1 | `np.squeeze(a)`             |

---

## 🧱 **9. Concatenación y división**

| Función            | Descripción            | Ejemplo                         |
| ------------------ | ---------------------- | ------------------------------- |
| `np.concatenate()` | Une arrays             | `np.concatenate((a,b), axis=0)` |
| `np.hstack()`      | Une por columnas       | `np.hstack((a,b))`              |
| `np.vstack()`      | Une por filas          | `np.vstack((a,b))`              |
| `np.split()`       | Divide en subarrays    | `np.split(a,3)`                 |
| `np.hsplit()`      | Divide horizontalmente | `np.hsplit(a,2)`                |
| `np.vsplit()`      | Divide verticalmente   | `np.vsplit(a,2)`                |

---

## 🧮 **10. Comparación y condiciones**

| Función                | Descripción                  | Ejemplo               |
| ---------------------- | ---------------------------- | --------------------- |
| `np.equal(a,b)`        | Igualdad elemento a elemento | `np.equal(a,b)`       |
| `np.not_equal()`       | Diferente                    | `np.not_equal(a,b)`   |
| `np.greater()`         | Mayor que                    | `np.greater(a,b)`     |
| `np.less()`            | Menor que                    | `np.less(a,b)`        |
| `np.where(cond, x, y)` | Selección condicional        | `np.where(a>0, a, 0)` |
| `np.all()`             | True si todos son True       | `np.all(a>0)`         |
| `np.any()`             | True si alguno es True       | `np.any(a>0)`         |

---

## 📦 **11. Conversión y tipos**

| Función         | Descripción          | Ejemplo              |
| --------------- | -------------------- | -------------------- |
| `a.astype()`    | Cambia tipo de datos | `a.astype(float)`    |
| `np.asfarray()` | Convierte a float    | `np.asfarray([1,2])` |
| `np.copy()`     | Copia el array       | `b = np.copy(a)`     |

---

## 📈 **12. Otras funciones matemáticas**

| Función                                   | Descripción                  | Ejemplo               |
| ----------------------------------------- | ---------------------------- | --------------------- |
| `np.sin()` / `np.cos()` / `np.tan()`      | Trigonométricas              | `np.sin(a)`           |
| `np.arcsin()` / `np.arccos()`             | Inversas trig.               | `np.arcsin(a)`        |
| `np.degrees()` / `np.radians()`           | Conversión grados ↔ radianes | `np.degrees(np.pi)`   |
| `np.abs()`                                | Valor absoluto               | `np.abs([-1,2])`      |
| `np.sign()`                               | Signo de cada elemento       | `np.sign([-2,0,3])`   |
| `np.floor()` / `np.ceil()` / `np.round()` | Redondeos                    | `np.floor(3.7)` → `3` |

---

## 🔍 **13. Ordenación y búsqueda**

| Función                       | Descripción                     | Ejemplo                            |
| ----------------------------- | ------------------------------- | ---------------------------------- |
| `np.sort()`                   | Devuelve array ordenado         | `np.sort(a)`                       |
| `np.argsort()`                | Índices que ordenarían el array | `np.argsort(a)`                    |
| `np.unique()`                 | Elementos únicos                | `np.unique([1,2,2,3])` → `[1,2,3]` |
| `np.argmax()` / `np.argmin()` | Índice de máximo/mínimo         | `np.argmax(a)`                     |
| `np.nonzero()`                | Índices de valores ≠ 0          | `np.nonzero(a)`                    |

---

## ⚙️ **14. Guardar y cargar datos**

| Función        | Descripción      | Ejemplo                     |
| -------------- | ---------------- | --------------------------- |
| `np.save()`    | Guarda en `.npy` | `np.save('datos.npy', a)`   |
| `np.load()`    | Carga `.npy`     | `b = np.load('datos.npy')`  |
| `np.savetxt()` | Guarda en texto  | `np.savetxt('out.txt', a)`  |
| `np.loadtxt()` | Carga texto      | `a = np.loadtxt('out.txt')` |

---

