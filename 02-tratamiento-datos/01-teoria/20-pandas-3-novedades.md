# 20 — Pandas 3: novedades y nueva forma de trabajar

> Material para el alumnado del módulo. Explica qué cambia con pandas 3.x y
> cómo adaptar el código que ya conoces de la serie 2.x. Está pensado para
> cuando el curso migre a pandas 3; **hoy seguimos en pandas 2.3.x** y este
> documento sirve de visión de futuro y de guía de migración.

## 1. Contexto: por qué existe pandas 3

pandas fue estable y estable desde hace años (todo dentro de la serie 2.x),
pero arrastraba decisiones de diseño que complicaban el trabajo con los
DataFrames grandes y con datos de texto:

- Las cadenas se guardaban como **`object`** (un tipo genérico, no de texto).
- Modificar una copia podía **modificar por sorpresa el DataFrame original**
  (el famoso `SettingWithCopyWarning`).
- Métodos como `drop`, `rename` o `sort_values` tenían dos formas de usarse
  (`inplace=True` o reasignación), lo que creaba código confuso.

pandas 3.0 (octubre de 2025) y pandas 3.1.0 (octubre de 2026) resuelven estos
tres puntos. Suponen un **cambio de filosofía**, no solo un cambio de número:

| | pandas 2.x | pandas 3.x |
|---|---|---|
| Texto | `object` (genérico) | **`str` dedicado** (`StringDtype`) |
| Modificar copias | puede alterar el original (con aviso) | **Copy-on-Write**: nunca altera el original |
| `inplace=True` | era habitual | **deprecado, se elimina** |
| Requisitos | Python ≥3.9 (según versión) | **Python ≥3.11**, NumPy ≥1.26 |

Este documento adapta a los contenidos del módulo las guías oficiales:
– [Pandas Migration Guides](https://pandas.pydata.org/docs/user_guide/migration.html)
– [String migration guide](https://pandas.pydata.org/docs/user_guide/migration-3-strings.html)
– Notas de [3.0.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html) y [3.1.0](https://pandas.pydata.org/docs/whatsnew/v3.1.0.html)
– PDEP-7 (Copy-on-Write), PDEP-8 (`inplace`) y PDEP-14 (string dtype).

## 2. Change nº 1: texto como `str`, no como `object`

En 2.x, al leer un CSV o crear un DataFrame con texto, la columna era de tipo
`object`:

```python
df = pd.DataFrame({"ciudad": ["Sevilla", "Cádiz"]})
df.dtypes
# ciudad    object   <- en 2.x
```

En 3.x, esa misma columna pasa a **`str`**:

```python
df.dtypes
# ciudad    str   <- en 3.x (StringDtype)
```

Consecuencias prácticas (las que te encontrarás en las prácticas):

- **`dtype == object` deja de detectar texto.** Para comprobar si una columna
  es texto, usa `pd.api.types.is_string_dtype(df["col"])` en lugar de comparar
  con `object`.
- **No asignes números a una columna de texto** para luego operar con ellos;
  pandas 3 es estricto con el tipo.
- `.values` de una columna `str` **no devuelve `numpy.ndarray`** directamente;
  usa `.to_numpy()`.
- Para ver valores ausentes sigue valiendo `pd.isna()` (funciona igual).
- Si PyArrow está instalado, pandas lo usa por debajo para el texto; si no,
  usa un fallback sobre `object`. En el módulo, la práctica de pandas usa
  PyArrow cuando se indica el backend.

**Cómo probarlo en pandas 2.3 sin instalar 3.x:**

```python
pd.options.future.infer_string = True
```

Con esta línea, pandas 2.3 se comporta como 3.x con el texto y puedes ir
probando tus notebooks antes de migrar.

## 3. Change nº 2: Copy-on-Write (CoW)

En 2.x, hacer así era un **error clásico que parecía funcionar**:

```python
df_dos_primeras = df.head(2)      # esto es una VISTA en 2.x
df_dos_primeras["ciudad"] = "X"   # muta df original sin querer
```

pandas 3 activa **Copy-on-Write**: cualquier objeto derivado de otro se trata
como una **copia**. Modificar `df_dos_primeras` **nunca** toca `df`.

Lo que cambia de verdad para ti:

- **Las operaciones de filtrado/selección ya no devuelven vistas** que se
  puedan modificar "por detrás". Devuelven copias (lógicas).
- **`SettingWithCopyWarning` desaparece**, porque el problema ya no puede
  ocurrir.
- La **asignación encadenada** (`df[df.a > 0]["b"] = 5`) sencillamente **no
  actualiza nada** en 3.x (y en 2.x puede dar falsa sensación de que funciona).

→ La forma correcta en 3.x (y la **única** que debes usar desde ya):

```python
df.loc[df["edad"] > 40, "nota"] = 9    # asignación directa con .loc
df.iloc[0, 2] = 100                    # con .iloc
```

Regla práctica: **si quieres modificar un DataFrame o una selección, hazlo
con `.loc`/`.iloc` sobre el propio objeto**, nunca encadenando sobre el
resultado de un filtro. Se activa con todos los métodos de selección que ya
usan los cuadernos (`.head()`, `.loc`, `.iloc`, máscaras booleanas).
Tener este hábito ahora te ahorra migrar luego.

## 4. Change nº 3: adiós al `inplace=True`

PDEP-8 propone eliminar `inplace` porque, con Copy-on-Write, no aporta nada:
internamente pandas **ya hace una copia y reasigna**, así que `inplace=True`
era casi "azúcar" que además rompía el encadenamiento.

En **3.0** la asignación encadenada con `inplace` deja de modificar al padre,
y en **3.1** el propio `inplace` empieza a emitir avisos (`Pandas4Warning`) y
se eliminará en pandas 4.

**Lo que tenías (2.x):**

```python
df.drop(columns=["x"], inplace=True)
df.rename(columns={"a": "b"}, inplace=True)
df.sort_values("ingresos", ascending=False, inplace=True)
df.set_index("id", inplace=True)
df.dropna(inplace=True)
dataset.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
```

**Lo mismo en 3.x (reasignación):**

```python
df = df.drop(columns=["x"])
df = df.rename(columns={"a": "b"})
df = df.sort_values("ingresos", ascending=False)
df = df.set_index("id")
df = df.dropna()
dataset = dataset.drop_duplicates()
df = df.reset_index(drop=True)
```

Equivalente, **sencillo y sin pérdida de rendimiento** (medido por pandas: la
reasignación no es más lenta que `inplace`, e incluso aprovecha mejor las
optimizaciones de CoW).

Cambio de estilo que también conviene adoptar desde ahora:

```python
# Antes (2.x): mutación "silenciosa"
df.dropna(inplace=True)

# Ahora: encadenamiento y resultado explícito
df = (df
      .dropna()
      .sort_values("precio", ascending=False)
      .reset_index(drop=True))
```

Los métodos de **asignación sobre los datos** (`fillna`, `replace`, `ffill`,
`bfill`, `interpolate`) **sí** siguen funcionando sin reasignación; no
deprecarán `inplace`.

> A cuento del curso: en `02-tratamiento-datos/02-ejemplos/01_pandas_fundamentos.ipynb`
> hay `df.sort_values(..., inplace=True)`; ya sabe que al migrar basta con
> cambiar esa línea por la reasignación.

## 5. Cambios menores que también notarás

- **Tiempos (`datetime64`)**: pandas 3 usa resolución **microsegundos (`us`)**
  en muchos resultados en lugar de `ns`. Si hacías `astype("int64")` con
  fechas, normaliza primero con `.as_unit("ns")`.
- **Zonas horarias**: por defecto se usa `zoneinfo`, no `pytz`. En el módulo
  no trabajas zonas horarias con pandas, así que no te afecta.
- **APIs antiguas eliminadas**: en 3.0 se quitaron muchas cosas ya deprecadas
  en 2.x (como `.ix`). Si un día te sale "deprecated" en algún antiguo
  ejemplo, esa es la razón.
- **Ecosistema**: pandas 3 requiere Python **≥3.11** y NumPy **≥1.26**, y se
  integra mejor con PyArrow. Para el resto (scikit-learn, matplotlib) no hay
  cambios de API especiales por pandas 3; los notebooks del módulo ya trabajan
  con esas librerías sobre pandas 2.x sin problemas.

## 6. Cómo migrar tu código (receta en 4 pasos)

La estrategia oficial de pandas es: **no saltes directo a 3.x**. Migra en
orden:

1. **Actualiza a pandas 2.3.x** (último de la serie 2, con soporte a largo
   plazo). Es la serie que usa el módulo hoy: `pandas = ">=2.2,<3"`.
2. **Activa las opciones de aviso** para ver exactamente qué romperá:

   ```python
   pd.options.mode.copy_on_write = "warn"
   pd.options.future.infer_string = True
   ```

3. **Corrige todos los `FutureWarning`/`DeprecationWarning`** que salgan:
   - sustituye `inplace=True` por reasignación (sección 4);
   - usa `.loc`/`.iloc` para asignaciones (sección 3);
   - cambia `dtype == object` por `is_string_dtype` donde detectes texto
     (sección 2);
   - **no dejes ningún warning**: es la lista de tareas de la migración.
4. **Ya en pandas 3**, ejecuta tus notebooks y usa las opciones de pandas 3
   (`PandasChangeWarning`, `PandasFutureWarning`, etc.) para el último repaso.

**Detector automático:** Ruff (linter de Python) con el conjunto `pandas-vet`
detecta muchos de estos patrones; la regla **PD002** marca directamente el uso
de `inplace=True`. No hay un migrador oficial automático completo: los
avances se hacen guiados por los warnings.

## 7. Resumen: la nueva "forma de trabajar"

| Regla nueva | En lugar de | Frecuencia en el módulo |
|---|---|---|
| `df = df.metodo(...)` | `df.metodo(..., inplace=True)` | **alta** (drop, dropna, sort_values, set_index, reset_index, rename, drop_duplicates) |
| `df.loc[...] = valor`, `df.iloc[...] = valor` | asignación sobre vistas/filtros encadenados | **alta** (filtros por condiciones) |
| `is_string_dtype(col)` | `col.dtype == object` para detectar texto | media |
| `.to_numpy()` | `col.values` esperando `ndarray` en texto | baja |
| probar con `pd.options.future.infer_string = True` | adivinar si romperá | útil ahora, en 2.3 |

**Conclusión:** pandas 3 no cambia *qué* puedes hacer (filtrar, agrupar,
ordenar, limpiar… lo de siempre), sino *cómo* lo escribes: resultados
explícitos, sin mutaciones por sorpresa y con texto de verdad. Adoptar ya la
forma nueva en pandas 2.x hace que la migración **no sea una migración**:
será un cambio de versión con cero sustos.
