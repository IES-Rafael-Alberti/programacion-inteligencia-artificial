# Análisis Exploratorio de Datos (EDA) – Titanic Dataset

## Carga de datos con Polars y Pandas
Se carga el dataset Titanic con `polars`, se convierte a `pandas` para visualización.

```python
import polars as pl
import pandas as pd

df_pl = pl.read_csv('titanic.csv')
df = df_pl.to_pandas()
df.info()
df.head()
```

## Estructura del dataset y valores ausentes
- Columnas clave: `Survived`, `Pclass`, `Sex`, `Age`, `Fare`, `SibSp`, `Parch`, `Embarked`
- Valores nulos: `Age`, `Cabin`, `Embarked`

## Distribuciones univariadas
- `Survived`: desbalance (62% no sobreviven)
- `Sex`: más hombres que mujeres
- `Age`: media ~30 años, imputación necesaria
- `Fare`: altamente asimétrica, log-transform sugerida
- `Embarked`: mayoría desde Southampton (S)

## Análisis bivariado
- `Survived` vs `Sex`: 74% mujeres sobrevivieron vs 19% hombres
- `Survived` vs `Pclass`: 63% 1ª clase, 24% 3ª clase
- `Survived` vs `Age`: niños pequeños mayor tasa
- `Fare`: correlaciona con `Pclass` y `Survived`

## Correlaciones
- `Fare` vs `Pclass`: -0.55
- `Sex` codificado correlaciona 0.54 con `Survived`
- `Age`: ligera correlación negativa con `Survived`

## Limpieza
- Imputar `Age` con mediana
- Eliminar `Cabin`
- Imputar `Embarked` con moda ('S')
- Guardar en Parquet:

```python
df.to_parquet('titanic_clean.parquet')
```

## Conclusiones
- Ser mujer, clase alta, pagar tarifa alta → mayor probabilidad de supervivencia
- Niños pequeños también priorizados
- Sexo y clase son las variables más influyentes

## Datasets alternativos para alumnos
1. **Adult Income (UCI)** – Ingreso >50K, 48K filas
2. **Bank Marketing (UCI)** – Éxito en campaña bancaria, 45K filas
3. **Credit Default (UCI)** – Incumplimiento pago tarjeta, 30K filas
4. *(Opcional)* **Telco Churn (IBM)** – Baja de clientes, 7K filas
