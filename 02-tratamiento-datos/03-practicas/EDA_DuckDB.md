> y convertirlo a notebook:
>
> ```bash
> pip install jupytext duckdb
> jupytext --to notebook EDA_duckdb.md
> ```

# 🦆 EDA con DuckDB — Soluciones paso a paso (SQL puro)

Este cuaderno crea un dataset sintético en memoria y replica un EDA completo con SQL en DuckDB.  
**Objetivo:** comparar después con NumPy / Pandas / cuDF.

---

## 🔧 Inicialización (Python mínimo para abrir la conexión)

```python
import duckdb
con = duckdb.connect(database=':memory:')
````

---

## 🧪 Crear dataset sintético en DuckDB (SQL puro)

* 1.000 filas
* Columnas: `ID, Edad, Salario, Experiencia, Horas, Nivel, Satisfaccion`
* `Salario` ~ N(2500, 800²) con ~1% *outliers* (×4)
* `Satisfaccion` ~ N(7, 2²) con ~1.5% `NULL`
* `Horas` ~ N(40, 5²)
* `Nivel` entero 0..4

> Nota: Usamos **Box-Muller** para generar normales desde `random()`.

```python
con.execute(r"""
PRAGMA disable_progress_bar;

-- Limpiar si existe
DROP TABLE IF EXISTS empleados;

-- Crear tabla con base aleatoria y normales via Box-Muller
CREATE TABLE empleados AS
WITH base AS (
  SELECT
    row_number() OVER ()::INTEGER AS id,
    18 + CAST(floor(random()*47) AS INTEGER)             AS edad,          -- 18..64
    -- Normal(0,1) por Box-Muller
    (sqrt(-2*ln(random()))*cos(2*pi()*random()))         AS z1,
    (sqrt(-2*ln(random()))*sin(2*pi()*random()))         AS z2,
    40 + (sqrt(-2*ln(random()))*cos(2*pi()*random()))*5  AS horas_raw,     -- ~ N(40, 5)
    CAST(floor(random()*5) AS INTEGER)                   AS nivel_raw,
    random()                                             AS u_out,
    random()                                             AS u_nan
  FROM range(1000)
),
dens AS (
  SELECT
    id,
    edad,
    -- Salario ~ N(2500, 800)
    (2500 + z1*800) AS salario_base,
    -- Experiencia 0..(edad-18) aproximada (usamos z2 para algo de dispersión)
    GREATEST(0, CAST(edad - (18 + abs(z2*6)) AS INTEGER)) AS experiencia,
    horas_raw AS horas,
    nivel_raw AS nivel,
    u_out,
    u_nan
  FROM base
),
con_out_nan AS (
  SELECT
    id,
    edad,
    -- ~1% outliers: multiplica por 4
    CASE WHEN u_out < 0.01 THEN salario_base*4 ELSE salario_base END AS salario,
    experiencia,
    horas,
    nivel,
    -- Satisfacción ~ N(7,2), con ~1.5% NULL
    CASE WHEN u_nan < 0.015 THEN NULL
         ELSE 7 + (sqrt(-2*ln(random()))*cos(2*pi()*random()))*2
    END AS satisfaccion
  FROM dens
)
SELECT
  id AS ID,
  edad AS Edad,
  salario AS Salario,
  experiencia AS Experiencia,
  horas AS Horas,
  nivel AS Nivel,
  satisfaccion AS Satisfaccion
FROM con_out_nan;
""");
```

---

## 🧠 Tarea 1 — Descripción básica

```python
print("Filas x Columnas:", con.execute("SELECT COUNT(*) AS filas, COUNT(*) FILTER (WHERE 1=0) AS columnas FROM empleados").fetchall()[0][0], "x 7")
print("Primeras 5:")
print(con.execute("SELECT * FROM empleados LIMIT 5").fetchdf())
print("Esquema:")
print(con.execute("PRAGMA table_info('empleados')").fetchdf())
```

---

## 📏 Tarea 2 — Tipos y rangos

```python
print(con.execute("""
SELECT 
  MIN(Edad) AS min_edad, MAX(Edad) AS max_edad,
  MIN(Salario) AS min_salario, MAX(Salario) AS max_salario,
  AVG(Edad) AS media_edad, MEDIAN(Salario) AS mediana_salario,
  STDDEV_SAMP(Salario) AS std_salario
FROM empleados;
""").fetchdf())
```

---

## 💭 Tarea 3 — Filtrado de datos

```python
# 1) Salarios > 4000 €
print(con.execute("SELECT COUNT(*) AS n_altos FROM empleados WHERE Salario > 4000").fetchdf())

# 2) >45h y >10 años experiencia (mostrar IDs)
print(con.execute("""
SELECT ID, Edad, Horas, Experiencia 
FROM empleados 
WHERE Horas > 45 AND Experiencia > 10
ORDER BY Horas DESC
""").fetchdf())

# 3) % nivel >= 3
print(con.execute("""
SELECT 100.0*AVG(CASE WHEN Nivel >= 3 THEN 1 ELSE 0 END) AS pct_nivel_ge3
FROM empleados
""").fetchdf())
```

---

## 🧹 Tarea 4 — Limpieza: valores faltantes (NULL)

```python
# Contar NULL en satisfacción
print(con.execute("SELECT COUNT(*) AS nan_sat FROM empleados WHERE Satisfaccion IS NULL").fetchdf())

# Rellenar NULLs con la media (ignorando NULLs)
con.execute("""
UPDATE empleados
SET Satisfaccion = (SELECT AVG(Satisfaccion) FROM empleados)
WHERE Satisfaccion IS NULL
""");

# Verificar
print(con.execute("SELECT COUNT(*) AS nan_sat FROM empleados WHERE Satisfaccion IS NULL").fetchdf())
```

---

## ⚠️ Tarea 5 — Detección de outliers (IQR)

```python
print(con.execute("""
WITH stats AS (
  SELECT 
    quantile_cont(Salario, 0.25) AS q1,
    quantile_cont(Salario, 0.75) AS q3
  FROM empleados
),
bounds AS (
  SELECT q1, q3, (q3-q1) AS iqr,
         q1 - 1.5*(q3-q1) AS lim_inf,
         q3 + 1.5*(q3-q1) AS lim_sup
  FROM stats
)
SELECT 
  (SELECT COUNT(*) FROM empleados, bounds 
   WHERE Salario < bounds.lim_inf OR Salario > bounds.lim_sup) AS n_outliers,
  lim_inf, lim_sup
FROM bounds;
""").fetchdf())
```

---

## 🧰 Tarea 6 — Sustitución de outliers (p95)

```python
# Calcular p95
print(con.execute("SELECT quantile_cont(Salario, 0.95) AS p95 FROM empleados").fetchdf())
# Reemplazar outliers por p95
con.execute("""
WITH stats AS (
  SELECT quantile_cont(Salario, 0.25) AS q1,
         quantile_cont(Salario, 0.75) AS q3,
         quantile_cont(Salario, 0.95) AS p95
  FROM empleados
),
bounds AS (
  SELECT q1, q3, p95,
         q1 - 1.5*(q3-q1) AS lim_inf,
         q3 + 1.5*(q3-q1) AS lim_sup
  FROM stats
)
UPDATE empleados
SET Salario = (SELECT p95 FROM bounds)
WHERE Salario < (SELECT lim_inf FROM bounds) OR Salario > (SELECT lim_sup FROM bounds);
""");
# Comprobar nuevos extremos
print(con.execute("SELECT MIN(Salario) AS min_salario, MAX(Salario) AS max_salario FROM empleados").fetchdf())
```

---

## 📊 Tarea 7 — Agrupaciones y resúmenes

```python
# Media de salario por nivel
print(con.execute("""
SELECT Nivel, AVG(Salario) AS salario_medio
FROM empleados
GROUP BY Nivel
ORDER BY Nivel
""").fetchdf())

# Satisfacción media por grupo de edad
print(con.execute("""
WITH grupos AS (
  SELECT *,
    CASE 
      WHEN Edad < 30 THEN '<30'
      WHEN Edad <= 50 THEN '30–50'
      ELSE '>50'
    END AS GrupoEdad
  FROM empleados
)
SELECT GrupoEdad, AVG(Satisfaccion) AS sat_media
FROM grupos
GROUP BY GrupoEdad
ORDER BY CASE GrupoEdad WHEN '<30' THEN 1 WHEN '30–50' THEN 2 ELSE 3 END
""").fetchdf())
```

---

## 🧩 Tarea 8 — Normalización y z-score

```python
# Normalizar Salario [0,1] y estandarizar Horas (z)
con.execute("ALTER TABLE empleados ADD COLUMN Salario_norm DOUBLE");
con.execute("ALTER TABLE empleados ADD COLUMN Horas_z DOUBLE");

con.execute("""
UPDATE empleados
SET Salario_norm = (Salario - (SELECT MIN(Salario) FROM empleados)) 
                   / ((SELECT MAX(Salario) FROM empleados) - (SELECT MIN(Salario) FROM empleados)),
    Horas_z = (Horas - (SELECT AVG(Horas) FROM empleados)) / (SELECT STDDEV_SAMP(Horas) FROM empleados);
""");

print(con.execute("""
SELECT MIN(Salario_norm) AS min_norm, MAX(Salario_norm) AS max_norm,
       AVG(Horas_z) AS media_z, STDDEV_SAMP(Horas_z) AS std_z
FROM empleados
""").fetchdf())
```

---

## 🧮 Tarea 9 — Correlaciones

```python
# Corr(Salario, Experiencia) y Corr(Edad, Satisfaccion)
print(con.execute("""
SELECT 
  corr(Salario, Experiencia) AS corr_sal_exp,
  corr(Edad, Satisfaccion)   AS corr_edad_sat
FROM empleados
""").fetchdf())
```

---

## 🧾 Tarea 10 — Estadísticas generales por columna

```python
print(con.execute("""
SELECT 
  'Edad'          AS columna, AVG(Edad) AS media, STDDEV_SAMP(Edad) AS std, MIN(Edad) AS min, MAX(Edad) AS max, 
   100.0*AVG(CASE WHEN Edad IS NULL THEN 1 ELSE 0 END) AS pct_null
UNION ALL
SELECT 'Salario', AVG(Salario), STDDEV_SAMP(Salario), MIN(Salario), MAX(Salario),
   100.0*AVG(CASE WHEN Salario IS NULL THEN 1 ELSE 0 END)
FROM empleados
UNION ALL
SELECT 'Experiencia', AVG(Experiencia), STDDEV_SAMP(Experiencia), MIN(Experiencia), MAX(Experiencia),
   100.0*AVG(CASE WHEN Experiencia IS NULL THEN 1 ELSE 0 END)
FROM empleados
UNION ALL
SELECT 'Horas', AVG(Horas), STDDEV_SAMP(Horas), MIN(Horas), MAX(Horas),
   100.0*AVG(CASE WHEN Horas IS NULL THEN 1 ELSE 0 END)
FROM empleados
UNION ALL
SELECT 'Nivel', AVG(Nivel), STDDEV_SAMP(Nivel), MIN(Nivel), MAX(Nivel),
   100.0*AVG(CASE WHEN Nivel IS NULL THEN 1 ELSE 0 END)
FROM empleados
UNION ALL
SELECT 'Satisfaccion', AVG(Satisfaccion), STDDEV_SAMP(Satisfaccion), MIN(Satisfaccion), MAX(Satisfaccion),
   100.0*AVG(CASE WHEN Satisfaccion IS NULL THEN 1 ELSE 0 END)
FROM empleados
ORDER BY columna;
""").fetchdf())
```

---

## ✅ Conclusión

Has realizado un EDA completo **usando solo SQL en DuckDB**:

* Generación del dataset (normales, `NULL`, *outliers*)
* Descriptivos, filtrado, limpieza (`UPDATE ... SET ... WHERE`)
* IQR y *winsorizing* (reemplazo por p95)
* Agrupaciones, normalización, correlaciones

**Siguiente paso** (en cuadernos aparte):

* Comparativa **NumPy vs Pandas vs DuckDB** (líneas, legibilidad, ergonomía)
* EDA con **cuDF** (RAPIDS) para GPU

```

---

