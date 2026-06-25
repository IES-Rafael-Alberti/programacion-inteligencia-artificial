# ⚔️ **Polars vs. Pandas con Arrow: comparación general**

## 🔥 **Velocidad**

| Operación             | Polars                         | Pandas con Arrow                                           |
| --------------------- | ------------------------------ | ---------------------------------------------------------- |
| Lectura CSV           | **Muy rápido (multihilo)**     | Rápido (pero no multihilo)                                 |
| Lectura Parquet       | **Rapidísimo (vectorizado)**   | Rápido                                                     |
| Filtros               | **Muy rápido**                 | Mucho más rápido que pandas clásico, pero menos que Polars |
| GroupBy               | **Extremadamente rápido**      | Mejor que antes, pero sigue siendo Python bound            |
| Joins                 | **Muy rápido**                 | Bastante más lento                                         |
| Apply/Transform       | **Vectorizado puro**           | `apply` sigue siendo Python y lento                        |
| Operaciones complejas | **Lazy evaluation** → optimiza | No existe lazy eval                                        |

👉 **Polars suele ser 5×–30× más rápido**, incluso si Pandas usa Arrow.

---

# 🧠 2. ¿Dónde está la diferencia real?

## ✔️ Polars

* Motor **nativo en Rust**
* **Multihilo automático**
* **Lazy execution**: optimiza el plan antes de ejecutar
* Usa **Apache Arrow internamente**, pero no depende de Python
* Mucho menos uso de RAM
* Mejor para datasets de millones de filas

## ✔️ Pandas con Arrow

* Pandas **tradicional** (Python + C)
* Solo algunas partes usan kernels Arrow
* **No es paralelizado**
* **No es lazy**
* Mejor compatibilidad (scikit-learn, seaborn, etc.)
* Mejor para EDA ligero y pipelines con muchas librerías Python

---

# 📊 3. Comparación de RAM

| operación | Polars                       | Pandas (Arrow)         |
| --------- | ---------------------------- | ---------------------- |
| Filtro    | **Baja RAM (copy-on-write)** | Media                  |
| GroupBy   | **Muy eficiente**            | Sube bastante          |
| Join      | **Estable**                  | Puede duplicar memoria |

Polars es **mejor para trabajar en máquinas con poca RAM**.

---

# 🧪 4. Ejemplo real (filtrar 10 millones de filas)

### **Pandas con Arrow**

```python
df = pd.read_csv("big.csv", engine="pyarrow")
df2 = df[df["col"] > 10]   # 1.0–1.5 segundos
```

### **Polars**

```python
df = pl.read_csv("big.csv")
df2 = df.filter(pl.col("col") > 10)   # 0.05–0.15 segundos
```

Polars es **10–20× más rápido** en filtros simples.

---

# 🧮 5. Ejemplo groupby (real benchmark)

### Pandas + Arrow

```python
df.groupby("category")["amount"].sum()
```

⏱️ 2.5–4 segundos (10M filas)

### Polars

```python
df.group_by("category").agg(pl.col("amount").sum())
```

⏱️ 0.1–0.4 segundos

**Polars es ~10× más rápido** en agregaciones.

---

# 🏋️ 6. Lazy mode: Polars aplasta a Pandas

Pandas no optimiza los pasos.
Polars **reanuda y optimiza el pipeline completo antes de ejecutarlo**.

Ejemplo:

```python
df.lazy().filter(...).group_by(...).agg(...).sort(...)
```

Polars:

* Elimina pasos innecesarios
* Reordena operaciones
* Fusiona filtros
* Ejecuta todo en paralelo

Pandas:
❌ ejecuta cada operación inmediatamente

---

# 🧩 7. Compatibilidad: el único terreno donde Pandas gana

| Área                               | Ganador    |
| ---------------------------------- | ---------- |
| Compatibilidad con sklearn         | **Pandas** |
| Integración con seaborn/matplotlib | **Pandas** |
| Ecosistema Python                  | **Pandas** |
| Curva de aprendizaje               | **Pandas** |
| Soporte lazy + paralelismo         | **Polars** |
| Velocidad total                    | **Polars** |
| Escalabilidad                      | **Polars** |

---

# 🧬 Conclusión global

### 👉 **Pandas con Arrow = Pandas clásico más rápido, NO un competidor de Polars**

### 👉 **Polars = Motor analítico moderno, rápido, ligero, Apache Arrow nativo + paralelismo + lazy**

**Para enseñanza**:

* Titanic y EDA → Pandas
* Performance, big data light y pipelines → Polars
* SQL + parquet + multi-GB → DuckDB

---