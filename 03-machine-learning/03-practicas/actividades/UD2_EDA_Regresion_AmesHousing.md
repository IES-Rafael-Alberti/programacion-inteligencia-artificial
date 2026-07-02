# Análisis Exploratorio de Datos (EDA) – Ames Housing (Regresión)

## Carga de los Datos
Uso de Polars para cargar y Pandas para visualizar. Variable objetivo: `SalePrice`.

## Tipos de Datos y Valores Ausentes
- 81 columnas (79 features + Id + SalePrice)
- 43 columnas categóricas, 38 numéricas
- NA significativos: PoolQC, Alley, Fence, FireplaceQu, LotFrontage, Garage*, Bsmt*, etc.

## Análisis de Outliers
- `GrLivArea` vs `SalePrice`: se eliminan 3 outliers con área > 4000 sqft y bajo precio
- Boxplots de variables numéricas para ver extremos

## Distribución de `SalePrice`
- Sesgada a la derecha (Right-skewed)
- Aplicable log-transform para modelos lineales

## Correlaciones Clave con `SalePrice`
- OverallQual: 0.79
- GrLivArea: 0.71
- GarageCars, TotalBsmtSF, 1stFlrSF, etc. correlaciones >0.5

## Visualizaciones Relevantes
- Boxplot: SalePrice vs OverallQual
- Regresión: YearBuilt vs SalePrice
- Heatmap de correlaciones

## Limpieza de Datos
- Imputación:
  - NA por ausencia → "None" o 0
  - LotFrontage → mediana global
  - GarageYrBlt → 0
  - MasVnrType/Area → "None" y 0
  - Electrical (1 caso) → moda
- Codificación:
  - Ordinales: map de calidad (Ex=5..Po=1)
  - Nominales: one-hot encoding (Neighborhood, etc.)
- Eliminación: `Id`, `Utilities`
- Guardado:
```python
df.to_parquet('ames_housing_clean.parquet', index=False)
```

## Conclusiones
- Factores clave: calidad, tamaño, año de construcción
- Codificación y limpieza adecuadas permiten modelado efectivo
- Dataset listo para regresión
- Recomendación: probar transformación log(SalePrice), ingeniería de features como TotalSF, TotalBath, Age

## Siguientes pasos
- Modelos: regresión lineal, árboles, boosting
- Métricas: RMSE, MAE, R2 sobre log y valores reales
- Validación cruzada para selección de modelos
