# 🧩 Cuaderno de Prácticas: Estructuras de Datos en Python

> **Objetivo:** practicar el uso de listas, tuplas, diccionarios y conjuntos en Python.  
> **Instrucciones:** lee cada enunciado, ejecuta el código y **escribe tu respuesta en los bloques vacíos** marcados con 👉.

---

## 🟦 1. LISTAS

### 🧱 Ejercicios

1️⃣ Crea una lista con tus tres comidas favoritas.  
👉 **Tu código:**
```python
# Escribe aquí tu código
````

2️⃣ Añade una nueva comida al final y otra en segunda posición.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

3️⃣ Muestra el primer y último elemento.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

4️⃣ Elimina el segundo elemento y muestra la lista resultante.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

5️⃣ Usa `pop()` para eliminar el último elemento y mostrarlo.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

6️⃣ Ordena la lista alfabéticamente e inviértela.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

7️⃣ Crea una nueva lista con las longitudes de cada palabra.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

---

### 🧠 Reto

Crea una lista de 5 números, elimina los impares, multiplica los pares por 2 y ordénalos de menor a mayor.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

---

## 🟨 2. TUPLAS

### 🧱 Ejercicios

1️⃣ Crea una tupla con tres colores.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

2️⃣ Muestra el primer color.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

3️⃣ Convierte la tupla en lista, cambia un color y vuelve a crear la tupla.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

4️⃣ Usa `count()` e `index()` con una tupla de números.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

5️⃣ Desempaqueta una tupla con tres valores.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

6️⃣ Genera una tupla con los cuadrados del 1 al 5.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

---

### 🧠 Reto

Crea una tupla con las temperaturas de la semana.
Calcula la temperatura media y muestra solo las que estén por encima de la media.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

---

## 🟩 3. DICCIONARIOS

### 🧱 Ejercicios

1️⃣ Crea un diccionario con tres alumnos y sus notas.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

2️⃣ Muestra la nota de uno de los alumnos.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

3️⃣ Añade un nuevo alumno y modifica la nota de otro.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

4️⃣ Muestra todas las claves, valores y pares.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

5️⃣ Usa `get()` para consultar una clave que no existe (con valor por defecto).
👉 **Tu código:**

```python
# Escribe aquí tu código
```

6️⃣ Recorre el diccionario mostrando alumno y nota.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

7️⃣ Crea un diccionario por comprensión con los cuadrados del 1 al 5.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

---

### 🧠 Reto

Crea un diccionario `precios` con tres productos y su precio.
Pide un producto por teclado y muestra su precio si existe o “No disponible” si no está.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

---

## 🟧 4. CONJUNTOS (SETS)

### 🧱 Ejercicios

1️⃣ Crea un conjunto con algunos números.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

2️⃣ Añade un número nuevo y elimina otro.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

3️⃣ Crea otro conjunto y calcula unión e intersección.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

4️⃣ Calcula diferencia y diferencia simétrica.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

5️⃣ Comprueba si un conjunto es subconjunto o superconjunto del otro.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

6️⃣ Genera un conjunto con los cuadrados del 1 al 5.
👉 **Tu código:**

```python
# Escribe aquí tu código
```

---

### 🧠 Reto

Crea dos conjuntos `A` y `B` con letras, y muestra:

* Las letras que están en ambos.
* Las que están solo en uno.
* Las totales sin duplicados.

👉 **Tu código:**

```python
# Escribe aquí tu código
```

---

## 🧾 5. RESUMEN Y COMPARACIÓN

| Tipo      | Mutable | Ordenado | Permite duplicados | Sintaxis principal | Ejemplo          |
| --------- | ------- | -------- | ------------------ | ------------------ | ---------------- |
| **list**  | ✅ Sí    | ✅ Sí     | ✅ Sí               | `[ ]`              | `[1, 2, 3]`      |
| **tuple** | ❌ No    | ✅ Sí     | ✅ Sí               | `( )`              | `(1, 2, 3)`      |
| **dict**  | ✅ Sí    | ✅ (3.7+) | ❌ Claves únicas    | `{clave: valor}`   | `{'a':1, 'b':2}` |
| **set**   | ✅ Sí    | ❌ No     | ❌ No               | `{ }` o `set()`    | `{1, 2, 3}`      |

---

## 🧠 Reto Final Global

1️⃣ Crea una lista de alumnos con tuplas: `(nombre, nota)`.
2️⃣ Convierte esa lista en un diccionario `{nombre: nota}`.
3️⃣ Muestra solo los nombres con nota mayor o igual a 7.
4️⃣ Guarda los nombres aprobados en un conjunto sin duplicados.

👉 **Tu código:**

```python
# Escribe aquí tu código
```

```

---

