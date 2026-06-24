# 🧩 **Chuleta R para estudiantes que vienen de Python (Pandas → dplyr)**

*(Edición compacta yorientada a los ejercicios con Titanic)*

---

# 1. Crear variables y tipos básicos

### Python

```python
x = 10
name = "Juan"
```

### R

```r
x <- 10
name <- "Juan"
```

**IMPORTANTE**: en R se usa `<-` para asignar (aunque `=` también funciona).

---

# 2. DataFrames en R

### Cargar librerías

```r
library(readr)   # lectura rápida de CSV
library(dplyr)   # filtrado, selección, agrupación...
```

### Leer un CSV (similar a `pd.read_csv`)

```r
titanic <- read_csv("titanic.csv")
```

### Ver primeras filas

```r
head(titanic)
```

---

# 3. Seleccionar columnas

### Python

```python
df[["Age", "Fare"]]
```

### R (dplyr)

```r
titanic %>% select(Age, Fare)
```

### Seleccionar solo columnas numéricas

```r
titanic %>% select(where(is.numeric))
```

---

# 4. Filtrar filas

### Python

```python
df[df["Age"] > 30]
```

### R

```r
titanic %>% filter(Age > 30)
```

---

# 5. Crear nuevas columnas

### Python

```python
df["ratio"] = df["Age"] / df["Fare"]
```

### R

```r
titanic %>% mutate(ratio = Age / Fare)
```

---

# 6. Agrupar y resumir (GroupBy)

### Python

```python
df.groupby("Pclass")["Fare"].mean()
```

### R

```r
titanic %>%
  group_by(Pclass) %>%
  summarise(mean_fare = mean(Fare, na.rm = TRUE))
```

**nota**: `na.rm = TRUE` es necesario para ignorar NA en R.

---

# 7. Ordenar (Sort)

### Python

```python
df.sort_values("Fare", ascending=False)
```

### R

```r
titanic %>% arrange(desc(Fare))
```

---

# 8. Seleccionar filas por posición

### Python

```python
df.iloc[0:5]
```

### R

```r
titanic[1:5, ]
```

---

# 9. Comprobar tipos de variables

### Python

```python
df.dtypes
```

### R

```r
str(titanic)
```

---

# 10. Tuberías (%>%): equivalente al chaining de Pandas

### Python

```python
df[df["Age"] > 30][["Age","Fare"]].sort_values("Fare")
```

### R

```r
titanic %>%
  filter(Age > 30) %>%
  select(Age, Fare) %>%
  arrange(Fare)
```

---

# 11. NA vs None

| Python      | R           |
| ----------- | ----------- |
| `None`      | `NA`        |
| `df.isna()` | `is.na(df)` |

---

# 12. Comprobar si un objeto existe (especialmente útil para tests)

```r
exists("titanic")
```

---

# 13. Resumen rápido de equivalencias

| Acción                | Pandas                       | R (dplyr)                   |
| --------------------- | ---------------------------- | --------------------------- |
| Seleccionar columnas  | `df[["Age","Fare"]]`         | `select(Age, Fare)`         |
| Filtrar               | `df[df.Age > 30]`            | `filter(Age > 30)`          |
| Crear columna         | `df["X"] = ...`              | `mutate(X = ...)`           |
| Agrupar               | `groupby("col")`             | `group_by(col)`             |
| Resumen               | `.agg({"col":"mean"})`       | `summarise(mean(col))`      |
| Ordenar               | `sort_values("col")`         | `arrange(col)`              |
| Seleccionar numéricas | `df.select_dtypes("number")` | `select(where(is.numeric))` |

---

# 14. Patrón general para resolver ejercicios en R

Con dplyr, casi todo sigue el patrón:

```r
df %>%
  filter(...) %>%
  select(...) %>%
  mutate(...) %>%
  group_by(...) %>%
  summarise(...)
```

---

# 15. ¿Por qué R puede parecer diferente?

* Usa **tuberías** en vez de chaining con `.`
* Tiene **tipos más estrictos** y NA se comporta distinto
* El ecosistema **dplyr** está muy estandarizado (más que pandas)
* Las funciones suelen ser **más cortas y verbosas** (`filter`, `select`, `summarise`), pero el patrón es siempre el mismo
