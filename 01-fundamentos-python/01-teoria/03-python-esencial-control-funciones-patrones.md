# 03 — Python esencial: control, funciones y patrones útiles

Este documento completa la base mínima de Python antes de entrar en computación numérica. El desarrollo guiado está en `../02-ejemplos/03_control_flujo_y_funciones.ipynb`; aquí se añaden patrones que conviene reconocer pronto.

## Qué debe dominar el alumnado

| Bloque | Debe saber hacer |
|--------|------------------|
| Condicionales | Tomar decisiones con `if`, `elif`, `else`. |
| Bucles | Recorrer secuencias con `for` y repetir con `while` cuando tenga sentido. |
| Funciones | Definir funciones con parámetros y valor de retorno. |
| Comprensiones | Crear listas o diccionarios de forma compacta y legible. |
| Excepciones | Entender `try/except` como mecanismo de control de errores, no como parche. |
| Ficheros | Reconocer el patrón `with open(...)` aunque el trabajo fuerte de datos llegue después. |

## Comprensiones

Las comprensiones aparecen constantemente en preparación de datos, generación de features y limpieza previa.

```python
notas = [4.5, 7.0, 8.5, 3.0]
aprobados = [nota for nota in notas if nota >= 5]
etiquetas = {nota: "apto" if nota >= 5 else "revisar" for nota in notas}
```

Úsalas cuando mejoren la claridad. Si la expresión se vuelve difícil de leer, es mejor escribir un bucle normal.

## Funciones pequeñas

En IA interesa separar pasos: cargar datos, limpiar, transformar, entrenar, evaluar. Esa separación empieza con funciones pequeñas.

```python
def normalizar(valor, minimo, maximo):
    return (valor - minimo) / (maximo - minimo)
```

Una función útil tiene una responsabilidad clara y un nombre que explica la intención.

### Cuidado con las listas como parámetros por defecto

Los valores por defecto de los parámetros se evalúan una sola vez, cuando Python
ejecuta la definición de la función. Si el valor por defecto es una lista,
diccionario o conjunto, las llamadas que omiten ese argumento comparten el mismo
objeto mutable.

Este ejemplo puede sorprender:

```python
def agregar_elemento(elemento, elementos=[]):
    elementos.append(elemento)
    return elementos

print(agregar_elemento("a"))  # ['a']
print(agregar_elemento("b"))  # ['a', 'b'] — conserva la lista de la llamada anterior
```

La función no crea una lista nueva en cada llamada. Para obtener una lista nueva
cuando no se proporciona ninguna, usa `None` como valor centinela:

```python
def agregar_elemento(elemento, elementos=None):
    if elementos is None:
        elementos = []
    elementos.append(elemento)
    return elementos

print(agregar_elemento("a"))  # ['a']
print(agregar_elemento("b"))  # ['b'] — llamada independiente
```

Si quien llama proporciona explícitamente una lista, la función modificará esa
lista. Eso puede ser intencional; conviene documentarlo y tenerlo en cuenta.

## Errores y ficheros

No hace falta profundizar aún en entrada/salida, pero sí reconocer el patrón básico:

```python
from pathlib import Path

ruta = Path("datos.txt")

try:
    with ruta.open("r", encoding="utf-8") as fichero:
        contenido = fichero.read()
except FileNotFoundError:
    contenido = ""
```

Más adelante se trabajará con CSV, Parquet y datasets reales; aquí basta con entender que los datos suelen venir de fuera del programa y pueden fallar.

## Señales de dominio

- Puede transformar una lista con un bucle y con una comprensión sencilla.
- Escribe funciones con nombres claros y retorno explícito.
- No mezcla toda la lógica en una única celda.
- Entiende que los errores previsibles deben gestionarse.
- Reconoce cuándo una función o import pertenece a una librería externa.
