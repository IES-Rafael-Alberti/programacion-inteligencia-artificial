# Guion de la tercera clase de PIA — estructuras adicionales y POO

> **Documento interno del profesorado. No publicar en GitHub Pages ni en Moodle.**

**Duración:** 2 horas.  
**Punto de continuidad:** en la segunda clase el grupo completó un cuestionario y
ejercicios básicos de Python, y llegó hasta las estructuras de datos básicas. La
sesión de mañana prioriza algunas estructuras adicionales de la biblioteca
estándar; la introducción a POO es opcional y solo se aborda si queda tiempo.

## Propósito

Mostrar que las listas, tuplas, diccionarios y conjuntos son una base útil, pero
que Python ofrece estructuras especializadas para tareas frecuentes. Introducir
`Counter`, `defaultdict` y `deque` mediante ejemplos breves y cercanos. Si el
ritmo lo permite, presentar clases e instancias como preparación conceptual para
PyTorch y PyTorch Lightning.

No se pretende cubrir todas las estructuras de `collections`, `queue` y la
biblioteca estándar en una sola clase. `heapq`, `array`, `bisect`, `ChainMap` y
las colas concurrentes se pueden mencionar o dejar para consulta.

## Objetivos de salida

Al finalizar la parte principal, el alumnado podrá:

- reconocer cuándo un contador especializado simplifica el conteo de elementos;
- usar `defaultdict(list)` para agrupar datos sin inicializar cada clave a mano;
- describir `deque` como una cola de doble extremo adecuada para añadir o extraer
  elementos por ambos lados;
- elegir una estructura según la operación dominante, en vez de usar siempre una
  lista.

Si se alcanza el bloque opcional de POO, podrá además distinguir clase e
instancia, identificar atributos y métodos, y explicar el papel básico de
`__init__` y `self`.

## Preparación previa

- Abrir `01-fundamentos-python/02-ejemplos/04b-estructuras-datos-adicionales.ipynb`.
- Tener disponible `01-fundamentos-python/01-teoria/04b-estructuras-datos-adicionales.md`.
- Si hay margen, abrir `01-fundamentos-python/02-ejemplos/05_orientacion_objetos_python.ipynb`
  y `01-fundamentos-python/01-teoria/04c-orientacion-objetos-python.md`.
- Preparar un ejemplo con calificaciones o etiquetas de una actividad: contar
  frecuencias y agrupar registros por categoría.
- Confirmar que el notebook está disponible en Moodle o indicar cómo abrirlo
  desde el repositorio local.
- No instalar dependencias para esta sesión: las estructuras mostradas pertenecen
  a la biblioteca estándar de Python.

## Guion de 120 minutos

| Tiempo | Actividad | Resultado esperado |
| ---: | --- | --- |
| 0–8 min | Reencuentro. Recuperar dos ideas del cuestionario y los ejercicios básicos; pedir dudas concretas sobre estructuras básicas. | Se retoma el progreso real sin repetir el cuestionario ni toda la clase anterior. |
| 8–18 min | Comparar una lista, una tupla, un diccionario y un conjunto: qué guardan y qué operación resulta natural en cada uno. | Se conecta lo aprendido con la necesidad de estructuras especializadas. |
| 18–35 min | Presentar `Counter` con frecuencias de notas o etiquetas; probar `most_common`. | Cuenta repeticiones con una intención clara y código breve. |
| 35–50 min | Presentar `defaultdict(list)` para agrupar personas o resultados por categoría. Comparar con un diccionario que exige inicializar cada clave. | Comprende el valor por defecto de una estructura y cuándo facilita la agrupación. |
| 50–62 min | Mostrar `deque` como cola: `append`, `appendleft`, `pop` y `popleft`. Relacionarlo con una fila de tareas y, de pasada, con BFS. | Distingue una cola de una lista usada como si fuera cola. |
| 62–72 min | Mini-práctica: contar etiquetas y agruparlas por categoría con los datos de ejemplo. | Aplica `Counter` o `defaultdict` y justifica su elección. |
| 72–78 min | Puesta en común y pausa breve. | Se comprueba si el grupo está listo para abrir el bloque opcional de POO. |
| 78–90 min | **Si hay tiempo:** presentar clase, instancia, atributo y método con el ejemplo `Alumno` o `Producto` del notebook de POO. | Comprende la diferencia entre describir una clase y crear un objeto concreto. |
| 90–105 min | **Si hay tiempo:** seguir `__init__` y `self`; modificar un atributo y llamar a un método. Relacionar los objetos con datos y comportamiento. | Puede leer una clase sencilla sin confundir `self` con un valor que se escribe al llamar. |
| 105–114 min | **Si hay tiempo:** mini-ejercicio guiado: una clase `Producto` con nombre, precio y método `importe()`. Si no se llegó a POO, ampliar agrupación y conteos. | Refuerza el bloque que se alcanzó, sin acelerar para «cubrirlo todo». |
| 114–120 min | Ticket de salida y continuidad. | Se sabe qué estructura comprendió cada estudiante y si POO queda para la siguiente clase. |

## Bloque principal: estructuras adicionales

### 1. `Counter`: contar frecuencias

```python
from collections import Counter

etiquetas = ["python", "datos", "python", "ia", "datos", "python"]
frecuencias = Counter(etiquetas)

print(frecuencias)
print(frecuencias.most_common(2))
```

Pregunta al grupo qué tendría que escribir con un diccionario normal para
obtener el mismo resultado. Acepta primero una solución con `if clave not in
conteo`; después muestra que `Counter` expresa directamente la intención.

### 2. `defaultdict(list)`: agrupar

```python
from collections import defaultdict

por_tema = defaultdict(list)
actividades = [
    ("python", "variables"),
    ("datos", "tablas"),
    ("python", "funciones"),
]

for tema, actividad in actividades:
    por_tema[tema].append(actividad)

print(dict(por_tema))
```

Aclara que el valor predeterminado se crea al acceder a una clave ausente. No lo
confundas con pasar `[]` como argumento por defecto a una función: son dos
mecanismos distintos. Si sale la duda, remite a la nota de UD1 sobre [listas como
parámetros por defecto](../01-teoria/03-python-esencial-control-funciones-patrones.md#trampa-común-listas-como-parámetros-por-defecto).

### 3. `deque`: una cola práctica

```python
from collections import deque

pendientes = deque(["cargar datos", "revisar resultado"])
pendientes.append("guardar informe")
actual = pendientes.popleft()

print("Ahora:", actual)
print("Quedan:", pendientes)
```

Deja `heapq`, `array`, `bisect` y las colas con varios hilos como ejemplos de
consulta, no como nuevos objetivos de la sesión.

## Mini-práctica: resumen de una actividad

```python
respuestas = [
    ("Python", "básico"),
    ("Python", "básico"),
    ("NumPy", "inicial"),
    ("Python", "medio"),
    ("NumPy", "básico"),
]
```

1. Usa `Counter` para contar cuántas respuestas hay de cada herramienta.
2. Usa `defaultdict(list)` para agrupar los niveles por herramienta.
3. Explica qué estructura usarías para atender solicitudes en orden de llegada.
4. Si queda tiempo, cambia los datos y comprueba que el programa sigue
   funcionando.

## Bloque opcional: primera toma de contacto con POO

### Mensaje central

> Una clase agrupa datos y operaciones relacionadas; un objeto es una instancia
> concreta de esa clase.

Usa `05_orientacion_objetos_python.ipynb` como demostración guiada. En esta
primera presentación céntrate en:

1. crear una clase sencilla;
2. construir dos instancias y comprobar que son objetos distintos;
3. inicializar atributos con `__init__`;
4. leer un atributo y llamar a un método;
5. explicar que `self` se refiere a la instancia actual.

No intentes cubrir composición, herencia, métodos especiales y `@dataclass` en
profundidad. Si el grupo ya ha comprendido la base, muestra la composición como
anticipo; deja la herencia y el ejercicio largo para otra sesión.

### Puente a PyTorch

Explica solo la relación conceptual:

- `torch.nn.Module` es una clase base que se extiende para definir modelos;
- `Dataset` suele ofrecer `__len__` y `__getitem__` para consultar ejemplos;
- hoy no se importa PyTorch ni se crean redes neuronales.

El objetivo es que, al encontrar estas estructuras más adelante, la sintaxis de
clases no aparezca por primera vez junto con tensores, entrenamiento y
backpropagation.

## Si el tiempo se reduce

- Completa `Counter` y `defaultdict`; muestra `deque` en una demostración breve.
- Omite el mini-ejercicio POO si todavía cuesta interpretar bucles o funciones.
- Cierra identificando qué queda pendiente; no sacrifiques la comprensión por
  terminar el notebook.

## Si el grupo avanza con soltura

- Compara `deque.popleft()` con eliminar el primer elemento de una lista.
- Completa la clase `Producto` del notebook de ejercicios de POO.
- Muestra composición (`Curso` contiene alumnado) y explica que es distinta de
  herencia.
- Deja como reflexión por qué un `Dataset` de PyTorch debe dar longitud y acceso
  a una muestra.

## Criterio de salida

- Cada estudiante puede asociar `Counter`, `defaultdict` y `deque` con un uso.
- El grupo ha aplicado al menos una de estas estructuras a datos sencillos.
- Si se impartió POO, cada estudiante distingue clase e instancia y reconoce un
  atributo y un método.
- Quedan identificados los conceptos que deben retomarse al inicio de la sesión
  siguiente.
