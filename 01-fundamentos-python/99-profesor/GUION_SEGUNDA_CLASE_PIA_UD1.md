# Guion de la segunda clase de PIA — continuación de UD1

> **Documento interno del profesorado. No publicar en GitHub Pages ni en Moodle.**

**Duración:** 2 horas.  
**Punto de continuidad:** en la primera clase se presentó el módulo y se llegó
hasta control de flujo. Aunque al principio parecía que el grupo dominaba Python,
un estudiante indicó que nunca lo había utilizado; por eso se continuó con los
fundamentos y se adaptó el ritmo.

## Propósito

Consolidar condicionales y bucles mediante una breve recuperación activa, y
avanzar a funciones con parámetros y valores de retorno. Si el grupo responde
bien, se introduce el recorrido y modificación de listas como base para las
próximas prácticas. No hace falta llegar a diccionarios, NumPy ni a los
parámetros avanzados de funciones en esta sesión.

Al terminar, cada estudiante debería poder:

- leer una condición y un bucle sencillos y predecir su resultado;
- definir y llamar a una función con un parámetro;
- diferenciar entre mostrar un resultado con `print` y devolverlo con `return`;
- aplicar una función a varios valores de una lista usando un bucle.

## Preparación previa

- Abrir `01-fundamentos-python/02-ejemplos/03_control_flujo_y_funciones.ipynb`.
- Tener preparados en el notebook o la pizarra estos ejemplos breves:

  ```python
  nota = 7
  if nota >= 5:
      print("Aprobado")
  else:
      print("Hay que revisar")

  for numero in range(1, 4):
      print(numero)
  ```

- Abrir también `01-fundamentos-python/02-ejemplos/04_estructuras_datos_basicas.ipynb`,
  pero usar únicamente la introducción a listas si el ritmo lo permite.
- Dejar el entorno abierto antes de la clase. Si falla Pixi, tener Colab listo
  como alternativa y no dedicar la sesión a resolver instalaciones individuales.
- Preparar una pizarra con tres rótulos: **Entrada**, **Proceso**, **Resultado**.

## Ritmo principal — grupo con niveles diversos

| Tiempo | Actividad | Resultado esperado |
| ---: | --- | --- |
| 0–8 min | Bienvenida y continuidad: recordar que la clase anterior llegó hasta condicionales y bucles. Explicar que hoy se consolidan y se añaden funciones. | Nadie siente que debería haber llegado sabiendo Python. |
| 8–23 min | Recuperación breve: predecir la salida de los dos ejemplos preparados; después cambiar `nota` y el límite de `range`. | Se comprueba comprensión real sin hacer un examen ni señalar niveles individuales. |
| 23–35 min | Revisar las respuestas y corregir errores comunes: condición, indentación, rango final de `range` y número de iteraciones. | Se afianza el control de flujo antes de añadir conceptos. |
| 35–55 min | Presentar una función pequeña: parámetro, cuerpo, llamada y retorno. Comparar `return` con imprimir desde dentro de la función. | Comprende que una función recibe datos y produce un resultado reutilizable. |
| 55–70 min | Práctica guiada: escribir y probar `es_aprobado(nota)` y `clasificar_nota(nota)`. Probar valores por debajo, en el límite y por encima de 5. | Cada estudiante llama a una función con entradas distintas y comprueba los resultados. |
| 70–78 min | Pausa breve y revisión de dudas. | Se detectan bloqueos antes del ejercicio principal. |
| 78–93 min | Mostrar una lista pequeña de notas y recorrerla con `for`; aplicar dentro del bucle la función creada. | Conecta listas, bucles y funciones sin introducir todavía demasiadas estructuras. |
| 93–110 min | Mini-reto individual o por parejas: clasificar una lista de notas y contar aprobados y pendientes de revisión. | Produce una solución corta, comprensible y comprobable. |
| 110–117 min | Puesta en común: comparar dos soluciones y hablar de nombres, entradas y resultados. | Practica explicar el código y no solo ejecutarlo. |
| 117–120 min | Ticket de salida y anticipo de la próxima sesión: estructuras de datos y más práctica con listas. | El alumnado identifica qué ha entendido y qué necesita repasar. |

## Bloque central: funciones

Empieza con una versión que solo imprime:

```python
def mostrar_estado(nota):
    if nota >= 5:
        print("Aprobado")
    else:
        print("Hay que revisar")

mostrar_estado(7)
```

Después cambia el diseño para que devuelva un valor:

```python
def es_aprobado(nota):
    return nota >= 5

resultado = es_aprobado(7)
print(resultado)
```

Explica que `return` permite reutilizar la respuesta: guardarla, mostrarla,
combinarla con otra operación o comprobarla con un `if`. No profundices en
anotaciones de tipos, `*args`, `**kwargs`, `lambda` ni `match-case`.

### Comprobación guiada

Pide que prueben estos casos y predigan primero el resultado:

```python
print(es_aprobado(4))
print(es_aprobado(5))
print(es_aprobado(8))
```

Pregunta al grupo:

> ¿Qué diferencia hay entre que la función escriba «Aprobado» en pantalla y que
> devuelva `True` o `False`?

Respuesta que se busca: imprimir comunica directamente; devolver produce un
valor que el resto del programa puede reutilizar.

## Mini-reto: resumen de notas

Plantea el ejercicio en pasos. No entregues el código completo de inmediato.

```python
notas = [4, 7, 5, 3, 9, 6]
```

1. Usa `es_aprobado(nota)` para decidir si una nota alcanza el 5.
2. Recorre la lista con `for` y muestra cada nota con su resultado.
3. Cuenta cuántas están aprobadas.
4. Si queda tiempo, escribe una función `contar_aprobados(notas)` que devuelva
   el número total.

### Ampliación para quien ya domina el bloque

- Hacer que la función compruebe una nota límite distinta recibida como segundo
  parámetro.
- Calcular la media de las notas con acumulador y devolverla desde una función.
- Probar la función con una lista vacía y discutir qué resultado tendría sentido.
- Si ya pasan listas a funciones, explicar la [trampa de las listas como parámetros por defecto](../01-teoria/03-python-esencial-control-funciones-patrones.md#trampa-común-listas-como-parámetros-por-defecto): es fácil olvidarla si hace tiempo que no se usan listas; el `[]` de la definición no se crea de nuevo en cada llamada. Usar `None` cuando se necesita una lista independiente.

Estas ampliaciones no deben convertirse en requisito para el resto del grupo.

## Ruta alternativa si el grupo necesita más refuerzo

Si en la recuperación activa aparecen dudas generalizadas:

1. Dedica hasta 25 minutos a condicionales, indentación y `range`.
2. Presenta únicamente `es_aprobado(nota)` con una entrada y un `return`.
3. Recorre una lista juntos, línea a línea; no añadas el contador de aprobados.
4. Cierra con una prueba corta de lectura de código.

En ese caso, deja el mini-reto de resumen para la siguiente clase. Es preferible
que comprendan funciones y bucles a cubrir rápidamente más sintaxis.

## Ruta alternativa si el grupo avanza con soltura

Si la mayoría resuelve pronto el mini-reto:

- introduce `append` para construir una lista de resultados;
- pide explicar por qué la función recibe una nota en vez de usar una variable
  global;
- muestra cómo contar aprobados con un acumulador y contrasta esa solución con
  una comprensión, solo como anticipo;
- utiliza el tiempo restante para pruebas con datos límite y revisión por parejas.

No adelantes NumPy todavía: primero conviene que el grupo pueda leer y escribir
funciones y recorrer estructuras básicas con seguridad.

## Cierre y continuidad

Ticket de salida, en papel o en Moodle:

```text
Una función que hoy puedo explicar:
La diferencia entre print y return, con mis palabras:
Una duda que me queda:
```

Para la próxima sesión, pedir que revisen las funciones del notebook y completen
el mini-reto si no lo terminaron. No se califica.

## Criterio de salida

- El grupo puede explicar un `if` y un bucle `for` sencillos.
- Cada estudiante ha definido o modificado una función con parámetro.
- Cada estudiante puede identificar qué valor devuelve la función.
- La mayoría ha aplicado una función a los valores de una lista; si no, ese será
  el primer bloque de la clase siguiente.
