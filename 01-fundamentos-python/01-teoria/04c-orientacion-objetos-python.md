# Orientación a objetos en Python

La orientación a objetos (POO) permite agrupar datos y operaciones relacionadas en unidades reutilizables. Esta guía prepara conceptos que volverán a aparecer al trabajar con PyTorch.

## Clases e instancias

Una **clase** describe una estructura y su comportamiento; una **instancia** es un objeto concreto creado a partir de ella.

```python
class Alumno:
    pass

ana = Alumno()
ana.nombre = "Ana"
print(ana.nombre)  # Ana
```

Es preferible declarar el estado inicial en `__init__` y recibir siempre `self`, que representa la instancia:

```python
class Alumno:
    def __init__(self, nombre, nota=0.0):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        return self.nota >= 5

ana = Alumno("Ana", 7.5)
print(ana.nombre, ana.aprobado())  # Ana True
```

Los atributos (`nombre`, `nota`) guardan el estado y los métodos (`aprobado`) definen operaciones. `__init__` se ejecuta al construir la instancia; no es el constructor en sentido estricto, sino el inicializador del objeto.

## Composición y encapsulación por convención

La **composición** consiste en que un objeto contiene otros objetos. Suele expresar mejor una relación «tiene un» que la herencia:

```python
class Curso:
    def __init__(self, titulo, alumnos):
        self.titulo = titulo
        self.alumnos = list(alumnos)

    def numero_de_alumnos(self):
        return len(self.alumnos)

curso = Curso("Python", [Alumno("Ana", 7), Alumno("Luis", 4)])
print(curso.numero_de_alumnos())  # 2
```

Python no impone encapsulación privada fuerte. Un atributo `_nombre` significa «uso interno: no forma parte de la API pública» y es una convención. Un atributo `__nombre` activa *name mangling*: Python lo transforma aproximadamente en `_Clase__nombre` para evitar colisiones accidentales en subclases; no constituye secreto ni impide el acceso deliberado.

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo
        self.__codigo = "interno"

cuenta = Cuenta(10)
print(cuenta._saldo)           # Convención: se puede leer, pero no se debería usar desde fuera.
print(cuenta._Cuenta__codigo)  # Es accesible; __ no proporciona seguridad.
```

## Herencia y `super()`

La herencia especializa una clase cuando existe una relación «es un». `super()` permite reutilizar la implementación de la clase base:

```python
class AlumnoBecado(Alumno):
    def __init__(self, nombre, nota, beca):
        super().__init__(nombre, nota)
        self.beca = beca

    def descripcion(self):
        return f"{self.nombre}: {self.nota}, beca={self.beca}"

becado = AlumnoBecado("Irene", 8, True)
print(becado.descripcion())
```

Conviene preferir composición cuando la relación no sea realmente «es un» y mantener jerarquías pequeñas.

## Métodos especiales

Los métodos especiales conectan una clase con operaciones habituales de Python:

```python
class Grupo:
    def __init__(self, nombre, alumnos):
        self.nombre = nombre
        self.alumnos = list(alumnos)

    def __repr__(self):
        return f"Grupo(nombre={self.nombre!r}, alumnos={len(self.alumnos)})"

    def __len__(self):
        return len(self.alumnos)

    def __getitem__(self, posicion):
        return self.alumnos[posicion]

grupo = Grupo("A", ["Ana", "Luis", "Irene"])
print(grupo)       # Grupo(nombre='A', alumnos=3)
print(len(grupo))  # 3
print(grupo[1])    # Luis
```

- `__repr__` ofrece una representación útil para depuración y consola.
- `__len__` permite usar `len(objeto)`.
- `__getitem__` permite indexar y, si se implementa adecuadamente, trabajar también con rebanadas.

## `@dataclass`

Cuando una clase almacena principalmente datos, `@dataclass` genera automáticamente métodos habituales como `__init__` y `__repr__`:

```python
from dataclasses import dataclass

@dataclass
class Ejemplo:
    entrada: float
    etiqueta: int

muestra = Ejemplo(2.5, 1)
print(muestra)  # Ejemplo(entrada=2.5, etiqueta=1)
```

Es una buena opción para registros sencillos; no sustituye a una clase con métodos cuando existe comportamiento relevante.

## Puente hacia PyTorch

Estos conceptos se reutilizan después, sin cambiar los fundamentos:

- Un modelo que hereda de `torch.nn.Module` es una clase especializada. Su `__init__` configura capas y `super().__init__()` inicializa la parte heredada; sus métodos describen el comportamiento del modelo.
- Un `torch.utils.data.Dataset` suele ser una clase con `__len__` y `__getitem__`, de modo que puede indicar cuántos ejemplos contiene y devolver uno por índice.
- Un `DataLoader` compone un `Dataset` con agrupación (*batching*), barajado y, si procede, carga paralela. La composición permite separar los datos de la forma de recorrerlos.

La guía de PyTorch explicará estos tipos y sus tensores más adelante; aquí sólo se prepara el modelo mental de clase, herencia, composición y protocolo de objetos.

## Comprobación

1. Crea una clase `Producto` con `nombre`, `precio` y un método `con_iva()`. Instancia dos productos.
2. Añade `__repr__` y comprueba que `print(producto)` es útil.
3. Crea `Catalogo` por composición, con `__len__` y `__getitem__`.
4. Revisa que puedes explicar la diferencia entre `_atributo` y `__atributo` sin llamarlos privados fuertes.
5. Relaciona cada método de `Catalogo` con la interfaz que necesitaría un `Dataset`.
