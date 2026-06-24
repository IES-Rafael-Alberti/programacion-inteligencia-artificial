---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #f8f9fa
style: |
  section {
    font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  }
  h1 {
    color: #2b3a4a;
    border-bottom: 3px solid #e67e22;
    padding-bottom: 10px;
  }
  h2 {
    color: #34495e;
  }
  strong {
    color: #e74c3c;
  }
  code {
    background-color: #ecf0f1;
    color: #c0392b;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# Obtención y Procesamiento de Datos
## Taller de Forecasting Práctico con Python

**Sesión 02**
Del Laboratorio Sintético al Barro del Mundo Real.

---

# El mundo real no es limpio

En la primera sesión controlábamos perfectamente la tendencia, la estacionalidad y el ruido. 

En la vida real, te enfrentarás a:
*   Fechas guardadas como texto confuso ("02/01/2026" vs "01/02/2026").
*   Días enteros que directamente **no existen** en la base de datos.
*   Sensores estropeados durante semanas.
*   Formatos de tablas pensados para humanos, no para algoritmos.

> El 80% del éxito en Forecasting depende de una correcta preparación de los datos.

---

# 1. Entiende a tu paciente antes de operar

Antes de programar, responde a estas 4 preguntas críticas:

1.  **¿Qué representa cada fila?** (¿Medición, agregado, evento?)
2.  **¿Cuál es el eje temporal?** (¿Qué columna es la fecha?)
3.  **¿Cuál es la frecuencia esperada?** (Horaria, diaria, mensual).
4.  **¿Hay múltiples series mezcladas?** (Ej. Ventas de 10 tiendas distintas en la misma tabla).

---

# 2. El Formato Rey: Formato Largo (Long)

Los algoritmos de Machine Learning odian el Formato Ancho (cada columna es un mes). Necesitan **Formato Largo**:

*   **Timestamp:** Columna de tiempo explícita.
*   **Target:** La variable objetivo (`y`) a predecir.
*   **ID Serie:** Vital si predecimos múltiples ítems a la vez (Ej: `id_tienda`).
*   **Features:** Variables externas (Temperatura, Festivos).

```text
fecha        tienda   ventas
2026-01-01   A        120
2026-01-01   B        90
2026-01-02   A        135
```

---

# 3. Fechas de Cristal en Pandas

Jamás operes con fechas si son cadenas de texto (`object`).

**Paso 1: Convertir a fecha real**
```python
df["fecha"] = pd.to_datetime(df["fecha_texto"], dayfirst=True)
```

**Paso 2: Convertir la fecha en el "Corazón" (Índice)**
```python
df = df.set_index("fecha")
```
Al hacer esto, Pandas *sabe* que el DataFrame viaja en el tiempo. Operaciones como `df.loc["2026-01"]` se vuelven mágicamente sencillas.

---

# Extraer "El Latido" (Feature Engineering)

La estacionalidad está escondida en el calendario. Pandas nos permite extraerla fácilmente para dársela a los algoritmos:

```python
df["dia_semana"] = df.index.day_name()
df["mes"] = df.index.month
df["es_fin_de_semana"] = df.index.dayofweek >= 5
```

Estas columnas numéricas/categóricas serán nuestras **"pistas"** (predictores) para enseñarle al modelo cuándo ocurre el latido.

---

# 4. El Peligro Oculto: Huecos Implícitos

Existen dos tipos de nulos (`NaN`):
1. **Explícitos:** Hay una fila para el martes, pero el valor de ventas está vacío.
2. **Implícitos (Silenciosos):** La fila del martes **NO EXISTE**. Saltamos de lunes a miércoles.

Restar (lunes - miércoles) creyendo que ha pasado 1 día destruirá tu modelo.

**La Cura:** Forzar la aparición del hueco.
```python
# Obliga a crear una fila por día ("D"), revelando el martes como NaN
df_regular = df.asfreq("D") 
```

---

<div class="columns">
<div>

# 5. El Arte de Imputar

Imputar nulos con la "media global" en series temporales es **un crimen**. (Las ventas de Navidad no se rellenan con la media del verano).

*   **Forward Fill (`ffill`):** Arrastra el último valor conocido. (Seguro, evita espiar el futuro).
*   **Interpolación:** Traza una línea recta. (Peligroso: requiere conocer el futuro para dibujarse).

</div>
<div>

![Imputación](https://images.unsplash.com/photo-1543286386-2e659306cd6c?auto=format&fit=crop&q=80&w=600&h=400)

</div>
</div>

---

# Imputación Inteligente: Perfiles Estacionales

¿Qué pasa si un sensor se rompe durante **3 semanas**?
La interpolación creará una línea recta aburrida, ignorando el patrón de fines de semana frente a días de diario.

**Solución:** Rellenar con la historia pasada equivalente.
Si falta un "Domingo a las 20:00", imputaremos con la media histórica de *todos los domingos a las 20:00*. Así **preservamos el pulso vital** de la serie.

---

# 6. Enriqueciendo la Historia (Merge Temporal)

En el mundo real, los datos vienen divididos.
1. Una tabla que se mueve rápido (Serie temporal: Ventas diarias).
2. Una tabla estática (Catálogo: Ubicación de la tienda, tipo de producto).

```python
# Cruzamos el tiempo con el contexto estático
df_lecturas = pd.DataFrame({
    "id_contador": ["C001", "C002"],
    "consumo": [0.31, 0.42],
})

lecturas_enriquecidas = df_lecturas.merge(
    metadata, on="id_contador", how="left"
)
```
Esto permite crear modelos globales que diferencian el comportamiento de una tienda del "Centro" frente a una de las "Afueras".

---

# 🚀 ¡Al Barro del Mundo Real!

Abre el notebook `02_obtencion_procesamiento_datos.ipynb`

**Misiones:**
1. Cazar días desaparecidos con `asfreq()`.
2. Observar el desastre de una interpolación mal usada.
3. Crear perfiles estacionales para salvar datos perdidos.
