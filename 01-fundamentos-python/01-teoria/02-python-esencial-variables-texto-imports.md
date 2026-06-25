# 02 — Python esencial: variables, texto e imports

Este documento fija el mínimo de Python que debe quedar claro antes de trabajar con NumPy, Pandas o librerías de IA. El desarrollo guiado está en `../02-ejemplos/02_variables_tipos_operadores.ipynb`; aquí queda la referencia breve.

## Qué debe dominar el alumnado

| Bloque | Debe saber hacer |
|--------|------------------|
| Variables | Crear nombres claros y reasignar valores sin perder de vista el tipo. |
| Tipos básicos | Usar `int`, `float`, `bool`, `str` y conversiones explícitas. |
| Operadores | Combinar operadores aritméticos, relacionales y lógicos. |
| Texto | Construir mensajes con f-strings, acceder a caracteres y usar métodos básicos. |
| Imports | Importar módulos y reconocer alias habituales como `np`. |

## Texto y f-strings

En IA y análisis de datos se trabaja mucho con nombres de columnas, rutas de ficheros, etiquetas, logs y mensajes. Por eso no basta con saber números.

```python
nombre = "Ada"
accuracy = 0.9234
mensaje = f"Modelo de {nombre}: accuracy={accuracy:.2%}"
```

Operaciones mínimas:

```python
texto = "  gato,perro,pez  "
texto.strip()
texto.lower()
texto.split(",")
texto[0:4]
```

## Imports

Un programa de IA combina código propio con librerías. El alumnado debe reconocer estos patrones desde el principio:

```python
import math
import numpy as np
from pathlib import Path
```

La idea importante no es memorizar librerías, sino entender que `import` incorpora herramientas externas al programa.

## Señales de dominio

- Puede explicar qué tipo tiene un dato y por qué importa.
- Usa nombres de variables legibles.
- Construye condiciones con operadores lógicos.
- Usa f-strings para mostrar resultados.
- Entiende que `np.array(...)` funciona porque antes se importó NumPy como `np`.
