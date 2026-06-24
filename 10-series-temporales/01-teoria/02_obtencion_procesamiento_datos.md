# Obtención y Procesamiento de Datos de Series Temporales

## Sesión 2: Preparar datos temporales para analizarlos y predecirlos

En la primera sesión trabajamos con series temporales sintéticas. Eso nos permitió controlar a la perfección la tendencia, la estacionalidad y el ruido, creando un entorno ideal de laboratorio. Sin embargo, en esta segunda parte nos acercamos al mundo real: los datos rara vez vienen limpios. Tendremos que obtenerlos, entender su estructura, convertir formatos de fechas que a menudo son texto, ordenar registros, lidiar con huecos silenciosos y tratar valores perdidos.

En el modelado de series temporales, **gran parte del éxito no reside en el algoritmo que uses, sino en cómo preparas los datos.** Si las fechas están mal interpretadas, si hay huecos sin detectar porque los sistemas simplemente no registraron datos esos días, o si la frecuencia temporal no es estrictamente regular, cualquier predicción que intentes hacer estará fundamentada sobre arena y será engañosa.

---

## Objetivos

Al terminar esta sesión deberías ser capaz de:

- Entender conceptualmente por qué el formato de los datos temporales es más estricto que el de los datos tabulares tradicionales.
- Cargar un conjunto de datos temporal y convertir columnas de texto engañosas en verdaderos objetos de fecha (`DatetimeIndex`) en `pandas`.
- Filtrar, indexar y remuestrear datos basándote en el tiempo.
- Identificar el peligro de los "huecos implícitos" (fechas que directamente no existen en la tabla).
- Distinguir y transformar entre formato compacto, expandido (largo) y ancho, comprendiendo por qué el formato largo es el estándar en forecasting.
- Aplicar estrategias de imputación de valores perdidos con criterio: entendiendo cuándo usar interpolación, arrastre de valores (ffill) o perfiles estacionales.

## Requisitos técnicos

Usaremos las librerías estándar de análisis de datos:

```bash
pip install numpy pandas matplotlib scikit-learn
```

Importaciones habituales para esta sesión:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

---

## 1. Entender el conjunto de datos temporal

Antes de escribir la primera línea de código, el paso más importante es sentarse a comprender la naturaleza del conjunto de datos. A diferencia de un dataset tabular normal (por ejemplo, clientes de un banco donde cada fila es independiente), en una serie temporal el orden lo es todo. 

Debes responder siempre a estas preguntas críticas:
- **¿Qué representa cada fila?** (¿Es una medición, una agregación diaria, un evento puntual?)
- **¿Cuál es el eje de tiempo continuo?** (¿Es una columna, son varias, está en el nombre del archivo?)
- **¿Cada cuánto se espera una medición?** (Frecuencia: horaria, diaria, cada milisegundo).
- **¿Hay múltiples series mezcladas?** (Por ejemplo, ventas de distintas tiendas mezcladas en la misma tabla).

### Ejemplo de dataset múltiple (Formato Largo)

```text
fecha        tienda   ventas
2026-01-01   A        120
2026-01-02   A        135
2026-01-03   A        128
2026-01-01   B        90
2026-01-02   B        94
2026-01-03   B        97
```

Este dataset no contiene *una* única serie temporal, sino varias: una por cada tienda. Si intentas trazar (plot) la columna de ventas directamente, verás ruido incomprensible porque el tiempo va hacia adelante y hacia atrás al saltar de la tienda A a la B.

> **Pregunta para discutir:** Si ignorásemos la columna `tienda` y ordenáramos todo por `fecha`, ¿qué pasaría si calculamos el "valor anterior" (lag) para intentar predecir las ventas?

---

## 2. Preparar un modelo de datos

Un "modelo de datos" en este contexto significa acordar una estructura estandarizada para que nuestros algoritmos la consuman. 
Para un problema de forecasting, la estructura ideal y más robusta es el formato largo (Long Format), que normalmente consta de:

- **Una columna temporal explícita** (el `timestamp`).
- **Una variable objetivo** (la `y` que queremos predecir).
- **Una columna de identificador** (el `id_serie`, vital si predecimos múltiples ítems o tiendas a la vez).
- **Variables externas opcionales** (temperatura, festivos, campañas de marketing).

Al tener un modelo mental claro, sabremos si el dataset crudo (raw) que recibimos necesita pivotarse, aplanarse o transformarse antes de empezar a trabajar.

---

## 3. Operaciones vitales con fechas en pandas

A menudo, al cargar un CSV, `pandas` inferirá que una columna de fecha es simplemente una cadena de texto (tipo `object`). Trabajar con fechas como si fueran texto es extremadamente peligroso (por ejemplo, alfanuméricamente "01/02/2026" va antes que "31/01/2026").

### 3.1 Convertir columnas de texto a `pd.Timestamp`

```python
df = pd.DataFrame({
    "fecha_texto": ["2026-01-01", "2026-01-02", "2026-01-03"],
    "ventas": [120, 135, 128],
})

# Convertimos la columna de texto en verdaderas fechas
df["fecha"] = pd.to_datetime(df["fecha_texto"])
print(df.dtypes)
```

**Cuidado con los formatos locales:** Si tus datos vienen de sistemas europeos, `02/01/2026` es el 2 de enero. En sistemas americanos, es el 1 de febrero. Usa `dayfirst=True` para forzar la interpretación europea:

```python
df["fecha"] = pd.to_datetime(df["fecha_texto"], dayfirst=True)
```

### 3.2 El poder del `DatetimeIndex`

En `pandas`, convertir la columna temporal en el "Índice" del DataFrame desbloquea operaciones de series temporales súper optimizadas (slicing, resample, asfreq).

```python
df = df.set_index("fecha")
```

A partir de este momento, `pandas` "sabe" que este DataFrame es una entidad que avanza en el tiempo. Podemos seleccionar rangos temporalmente con suma facilidad:

```python
# Seleccionar todo enero de 2026
df.loc["2026-01"]

# Seleccionar un rango específico
df.loc["2026-01-03":"2026-01-07"]
```

### 3.3 Extracción de componentes (Feature Engineering inicial)

Podemos extraer características del calendario que a menudo explican la estacionalidad (el componente que vimos en la Sesión 1). Para esto usamos el accesor `.dt` si la fecha es una columna, o `.index` si es el índice.

```python
# Si 'fecha' es el índice:
df["dia_semana"] = df.index.day_name()
df["mes"] = df.index.month
df["es_fin_de_semana"] = df.index.dayofweek >= 5
```

Estas extracciones numéricas o categóricas serán los "predictores" que le daremos a los algoritmos de Machine Learning para que aprendan los patrones periódicos.

---

## 4. El peligro oculto: Huecos implícitos y `asfreq`

En las series temporales, existen dos tipos de valores perdidos:
1. **Explícitos:** Hay una fila para "2026-01-05", pero la columna ventas pone `NaN`.
2. **Implícitos (Silenciosos):** La fila "2026-01-05" directamente **no existe** en el archivo.

Los huecos implícitos son el peor enemigo del analista de series temporales. Si calculamos una diferencia entre días y falta una fila, estaremos restando datos separados por 48 horas creyendo que están separados por 24 horas.

Para forzar la aparición de estos huecos implícitos y convertirlos en explícitos (y por tanto tratables), usamos `.asfreq()` o `.resample()`.

```python
df_irregular = pd.DataFrame({
    "fecha": ["2026-01-01", "2026-01-02", "2026-01-04"], # Faltan el 3
    "ventas": [120, 135, 150],
})

df_irregular["fecha"] = pd.to_datetime(df_irregular["fecha"])
df_irregular = df_irregular.set_index("fecha")

# Obligamos a pandas a rellenar el índice para que sea diario (Daily = "D")
df_regular = df_irregular.asfreq("D")
print(df_regular)
```

Al forzar la frecuencia, el día 3 aparecerá milagrosamente en el DataFrame, pero con ventas igual a `NaN`. ¡Ahora ya podemos identificar el problema y tratarlo!

---

## 5. Tratamiento e Imputación de Valores Perdidos

A diferencia de un problema de Machine Learning clásico donde imputamos nulos con la "media global" de toda la columna, **en series temporales usar la media global destruye la tendencia y la estacionalidad**. Un valor de ventas en Navidad no debería rellenarse con la media del verano.

Debemos usar la naturaleza temporal de los datos.

### 5.1 Estrategias ingenuas (Naive) pero robustas

```python
# Generamos una serie de ejemplo con un hueco
fechas = pd.date_range(start="2026-01-01", periods=10, freq="D")
ventas = [120, 135, np.nan, 140, 150, 160, np.nan, 138, 155, 170]
df_na = pd.DataFrame({"ventas": ventas}, index=fechas)

# 1. Propagación hacia adelante (Forward Fill)
df_na["ffill"] = df_na["ventas"].ffill()

# 2. Interpolación lineal
df_na["interpolacion"] = df_na["ventas"].interpolate()
```

- **Forward Fill (`ffill`):** Asume que el mundo no ha cambiado desde la última observación válida. Es seguro porque no usa información del futuro (evita el temido *data leakage*).
- **Interpolación Lineal:** Traza una línea recta entre el valor anterior y el posterior. Genera datos más suaves, pero **cuidado**: requiere conocer el valor futuro para calcularse. Solo es válido en análisis históricos, no en sistemas en tiempo real donde no tienes datos del futuro.

### 5.2 Huecos largos: El colapso de la interpolación

¿Qué pasa si el sensor se estropea durante 3 semanas?
Si usamos interpolación lineal en una serie estacional (como el consumo eléctrico diario), dibujaremos una línea recta aburrida cruzando todo el gráfico, ignorando por completo que los domingos se consume menos y los lunes más.

**La solución:** Imputación basada en perfiles (o interpolación estacional).

```python
# Rellenar con la media específica del mismo día de la semana y la misma hora
perfil_hora_dia = df.groupby([df.index.dayofweek, df.index.hour])["ventas"].mean()

for idx in df[df["ventas"].isna()].index:
    clave = (idx.dayofweek, idx.hour)
    df.loc[idx, "ventas_imputadas"] = perfil_hora_dia.loc[clave]
```
De esta forma, si falta el dato de un Domingo a las 20:00, lo rellenamos con lo que *suele* pasar los Domingos a las 20:00, preservando el pulso vital de la serie (la estacionalidad).

> **Pregunta para discutir:** ¿Se te ocurre algún caso de la vida real donde rellenar un hueco largo usando perfiles estacionales pueda dar un resultado terriblemente malo? Piensa en eventos climáticos extremos o pandemias.

---

## 6. Mapear y Enriquecer Información (Merge Temporal)

En un proyecto real de forecasting, rara vez predecimos basándonos solo en la propia serie. Si estamos analizando el consumo de 50 contadores eléctricos, tendremos una tabla con la serie temporal, y otra tabla estática con información técnica de esos contadores (¿está en el centro o en las afueras? ¿qué tarifa tiene contratada?).

```python
df_lecturas = pd.DataFrame({
    "timestamp": pd.date_range("2026-01-01", periods=4, freq="h"),
    "id_contador": ["C001", "C001", "C002", "C002"],
    "consumo": [0.31, 0.34, 0.42, 0.39],
})

# Y un catálogo de metadatos
metadata = pd.DataFrame({
    "id_contador": ["C001", "C002"],
    "barrio": ["Centro", "Norte"],
    "tipo_vivienda": ["piso", "casa"],
})

# Fusionamos usando el identificador
lecturas_enriquecidas = df_lecturas.merge(metadata, on="id_contador", how="left")
lecturas_enriquecidas
```

Esto añade columnas estáticas a cada observación temporal, permitiendo más tarde entrenar modelos globales que entiendan que el "C001" se comporta de forma diferente porque es un "piso" en el "Centro".

---

## 7. Actividades de clase

### Actividad 1: Combatiendo el desorden temporal
Crea un DataFrame con una columna `fecha` en formato texto donde los registros estén desordenados y falten días intermedios aleatorios. Tu misión:
1. Convertir la columna a datetime.
2. Fijarla como índice.
3. Ordenar el índice temporalmente.
4. Usar `asfreq("D")` para revelar los días desaparecidos.

### Actividad 2: Peligros de la interpolación ciega
Genera una onda senoidal estacional (`np.sin`) para simular la demanda horaria de electricidad durante 7 días. Genera un hueco enorme forzando que todo el miércoles y jueves sean `NaN`. 
1. Intenta rellenarlo con `interpolate()`. Visualiza el desastre y comenta el resultado.
2. Rellénalo usando un perfil medio por hora calculando la media de las horas correspondientes en los días que sí tienen datos. Visualiza y compara.

### Actividad 3: Reestructuración masiva
A veces nos entregan archivos Excel donde cada fila es una "Tienda", y cada columna representa las ventas de un "Mes" específico (Formato ancho). Usa `pandas.melt()` para convertir una estructura similar inventada por ti en un formato largo canónico (`id_tienda`, `fecha`, `ventas`), asegurándote de que `fecha` sea del tipo correcto.

---

## 8. Ideas clave

- **Las fechas son de cristal:** Deben convertirse a tipos temporales reales explícitamente y a menudo establecerse como índice para poder manipular la serie.
- **Lo que no se ve también importa:** Los sistemas informáticos omiten las mediciones vacías. Exponer los huecos implícitos con remuestreo o `asfreq` es vital antes de evaluar la calidad de los datos.
- **Imputar no es hacer magia:** Cada técnica de imputación conlleva suposiciones matemáticas. Un `ffill` asume constancia; una interpolación asume linealidad; un perfil asume repetición de la historia pasada. Elegir mal deforma la realidad.
- **Formato Largo = Formato Rey:** Casi todas las librerías de Machine Learning orientadas a series temporales consumen datos en los que cada fila es un timestamp, un id (opcional) y el target, en lugar de gigantescas matrices anchas por periodos.

## Continuación

En la siguiente sesión daremos un paso atrás para observar la belleza estructural de los datos limpios que acabamos de preparar. Nos centraremos en **visualizar**, extraer estacionalidades complejas, descomponer la señal matemáticamente (tendencia, ciclos y ruido) y cómo afrontar los "cisnes negros" u outliers atípicos.
