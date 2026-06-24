# 🐍 **Chuleta de Python Básico**
**Chuleta de Python básica** con todo lo esencial que los alumnos deben dominar antes de trabajar con librerías de IA o Big Data:

👉 **estructuras de control, comprensión, funciones, variables, operadores y sintaxis clave.**

---

## 🧩 **1. Asignación y tipos de variables**

| Tipo                       | Ejemplo             | Descripción                |
| -------------------------- | ------------------- | -------------------------- |
| Entero                     | `x = 5`             | Números sin decimales      |
| Decimal                    | `y = 3.14`          | Números con decimales      |
| Cadena                     | `nombre = "Ana"`    | Texto                      |
| Booleano                   | `activo = True`     | Verdadero/Falso            |
| Múltiple                   | `a, b, c = 1, 2, 3` | Asignación simultánea      |
| Intercambio                | `a, b = b, a`       | Intercambio de valores     |
| Constante (por convención) | `PI = 3.1416`       | Mayúsculas para constantes |

---

## 🧮 **2. Operadores básicos**

| Tipo        | Operadores        | Ejemplo           | Resultado          |
| ----------- | ----------------- | ----------------- | ------------------ |
| Aritméticos | `+ - * / // % **` | `5 // 2`          | `2`                |
| Comparación | `== != > < >= <=` | `3 != 2`          | `True`             |
| Lógicos     | `and or not`      | `a > 0 and b > 0` | `True`             |
| Asignación  | `= += -= *= /=`   | `x += 1`          | `x = x + 1`        |
| Identidad   | `is, is not`      | `a is b`          | Compara referencia |
| Pertenencia | `in, not in`      | `'a' in 'hola'`   | `True`             |

---

## 🧱 **3. Condicionales (if / elif / else)**

```python
x = 10
if x > 0:
    print("Positivo")
elif x == 0:
    print("Cero")
else:
    print("Negativo")
```
### Operador ternario en Python
💡 También puede escribirse en una sola línea:

```python
print("Positivo" if x > 0 else "Negativo")
```
o

```python
valor_if = "Positivo" if x > 0 else "Negativo"
```
---

## 🧩 **4. Estructura `match` (Python 3.10+)**

```python
comando = "saludar"

match comando:
    case "saludar":
        print("Hola!")
    case "adios":
        print("Adiós!")
    case _:
        print("Comando no reconocido")
```

📘 `_` es el **comodín** (equivalente a “default”).

---

## 🔁 **5. Bucles `for` y `while`**

### 🔹 `for` con secuencias

```python
for i in [1, 2, 3]:
    print(i)
```

```python
for i in range(5):
    print(i)  # 0,1,2,3,4
```

### 🔹 `for` con índice y valor

```python
for i, valor in enumerate(['a', 'b', 'c']):
    print(i, valor)
```

### 🔹 `while`

```python
x = 0
while x < 3:
    print(x)
    x += 1
```

💡 Puedes usar `break` (salir), `continue` (saltar) y `else` (si no hubo break).

```python
for n in range(5):
    if n == 3:
        break
else:
    print("No hubo break")  # Solo se ejecuta si no se rompió el bucle
```

---

## 🧠 **6. Comprensiones (comprehensions)**

Permiten crear estructuras de forma compacta.

| Tipo        | Ejemplo                            | Resultado       |
| ----------- | ---------------------------------- | --------------- |
| Lista       | `[x**2 for x in range(5)]`         | `[0,1,4,9,16]`  |
| Conjunto    | `{x for x in "banana"}`            | `{'b','a','n'}` |
| Diccionario | `{x:x**2 for x in range(3)}`       | `{0:0,1:1,2:4}` |
| Condicional | `[x for x in range(10) if x%2==0]` | `[0,2,4,6,8]`   |

---

## ⚙️ **7. Funciones**

### 🔹 Básica

```python
def saludar():
    print("Hola mundo")
```

### 🔹 Con parámetros

```python
def saludar(nombre):
    print("Hola", nombre)
```

### 🔹 Con valor de retorno

```python
def sumar(a, b):
    return a + b
```

### 🔹 Con valores por defecto

```python
def potencia(base, exponente=2):
    return base ** exponente
```

### 🔹 Con número variable de argumentos

```python
def sumar_todo(*args):
    return sum(args)

print(sumar_todo(1,2,3,4))  # 10
```

📘 `*args` → argumentos posicionales variables.

```python
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, "=", valor)

mostrar_info(nombre="Ana", edad=30)
```

📘 `**kwargs` → argumentos con nombre variables.

---

### 🔹 Funciones lambda (anónimas)

```python
doble = lambda x: x * 2
print(doble(5))  # 10
```

📘 Se usan cuando la función es muy corta o temporal (por ejemplo en `map`, `filter`, `sorted`).

---

## 🧰 **8. Otras construcciones útiles**

| Concepto                 | Ejemplo                   | Descripción                      |
| ------------------------ | ------------------------- | -------------------------------- |
| Desempaquetado           | `a,b = [1,2]`             | Asigna varios valores a la vez   |
| Desempaquetado extendido | `a, *b, c = [1,2,3,4,5]`  | `a=1, b=[2,3,4], c=5`            |
| Expresiones booleanas    | `x = a and b or c`        | Evalúa condiciones encadenadas   |
| F-strings                | `f"Hola {nombre}"`        | Interpolación de variables       |
| Comentarios              | `# Esto es un comentario` | Explicaciones en el código       |
| Docstrings               | `"""Texto"""`             | Descripción de funciones/módulos |

---

## 🧮 **9. Manejo de errores (try / except / else / finally)**

```python
try:
    n = int(input("Número: "))
    print(10 / n)
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except ValueError:
    print("Debes escribir un número.")
else:
    print("Todo ha ido bien.")
finally:
    print("Fin del programa.")
```

---

## 🧾 **10. Buenas prácticas esenciales**

✅ Usa nombres descriptivos: `total_ventas`, no `x`.
✅ Indenta con 4 espacios (no tabuladores).
✅ Documenta tus funciones con docstrings.
✅ Evita duplicar código, usa funciones.
✅ Escribe condicionales legibles:

```python
if not lista:  # mejor que len(lista) == 0
    ...
```

---

