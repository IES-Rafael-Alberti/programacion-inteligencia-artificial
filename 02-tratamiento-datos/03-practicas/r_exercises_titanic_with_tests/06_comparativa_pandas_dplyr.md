# Comparativa operativa — Pandas ↔ dplyr

| Tarea | Pandas | R / dplyr |
|---|---|---|
| Leer CSV | `pd.read_csv("file.csv")` | `read_csv("file.csv")` |
| Primeras filas | `df.head()` | `head(df)` |
| Estructura | `df.info()` | `glimpse(df)` |
| Seleccionar columnas | `df[["Age", "Fare"]]` | `select(df, Age, Fare)` |
| Filtrar filas | `df[df["Age"] > 30]` | `filter(df, Age > 30)` |
| Crear columna | `df.assign(ratio=df.Age / df.Fare)` | `mutate(df, ratio = Age / Fare)` |
| Ordenar | `df.sort_values("Fare")` | `arrange(df, Fare)` |
| Agrupar | `df.groupby("Pclass")` | `group_by(df, Pclass)` |
| Agregar | `.agg({"Fare": "mean"})` | `summarise(mean_fare = mean(Fare, na.rm = TRUE))` |
| Join | `df.merge(tabla, on="Pclass", how="left")` | `left_join(df, tabla, by = "Pclass")` |
| Valores perdidos | `df.isna().sum()` | `colSums(is.na(df))` |
| Histograma | `sns.histplot(data=df, x="Age")` | `ggplot(df, aes(x = Age)) + geom_histogram()` |
| Boxplot | `sns.boxplot(data=df, x="Pclass", y="Fare")` | `ggplot(df, aes(x = factor(Pclass), y = Fare)) + geom_boxplot()` |

## Idea clave

La sintaxis cambia, pero el razonamiento es el mismo: cargar datos, entender estructura, transformar, resumir, visualizar y comunicar conclusiones.
