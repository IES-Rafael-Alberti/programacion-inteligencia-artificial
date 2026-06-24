# Registro de errores, soluciones, preguntas y respuestas

## Error 1: fallo al entrenar `MLPForecaster`

### Problema

Al ejecutar:

```python
modelo = MLPForecaster(window_size=12, n_features=n_features)
trainer.fit(modelo, train_loader, val_loader)
```

aparecía un error durante el entrenamiento.

### Causa probable

Los datasets y dataloaders se habían creado con ventanas de tamaño 24:

```python
train_ds = TimeSeriesDataset(train_df, target_col="consumo_kwh", window_size=24)
val_ds   = TimeSeriesDataset(val_df,   target_col="consumo_kwh", window_size=24)
```

Por tanto, cada lote tenía entradas con forma aproximada:

```python
torch.Size([batch_size, 24, 3])
```

Pero el modelo MLP se había creado con:

```python
window_size=12
```

Eso hacía que el modelo esperase una entrada aplanada de:

```python
12 * 3 = 36
```

mientras que los datos reales tenían:

```python
24 * 3 = 72
```

### Solución recomendada

Crear el modelo usando el mismo `window_size` que los datasets:

```python
modelo = MLPForecaster(window_size=24, n_features=n_features)
```

Después, reejecutar las celdas desde la creación de datasets/loaders hasta:

```python
trainer.fit(modelo, train_loader, val_loader)
```

### Solución alternativa

Si se quiere entrenar el MLP con ventanas de 12 pasos, entonces hay que recrear los datasets y dataloaders también con `window_size=12`:

```python
train_ds = TimeSeriesDataset(train_df, target_col="consumo_kwh", window_size=12)
val_ds   = TimeSeriesDataset(val_df,   target_col="consumo_kwh", window_size=12)

train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
val_loader   = DataLoader(val_ds,   batch_size=32, shuffle=False)

modelo = MLPForecaster(window_size=12, n_features=n_features)
```

---

## Pregunta 1: ¿cómo obtengo un batch del `train_loader`?

### Respuesta

Se puede obtener un batch usando un iterador:

```python
X_batch, y_batch = next(iter(train_loader))
```

Para comprobar sus formas:

```python
print(X_batch.shape)
print(y_batch.shape)
```

Ejemplo esperado:

```python
torch.Size([32, 24, 3])
torch.Size([32])
```

También se puede inspeccionar el primer elemento del batch:

```python
X_batch[0]
y_batch[0]
```

O recorrer el `DataLoader` con un bucle:

```python
for X_batch, y_batch in train_loader:
    print(X_batch.shape, y_batch.shape)
    break
```

---

## Pregunta 2: ¿se puede obtener el primero o siempre hay que usar el iterador?

### Respuesta

Se puede obtener el primer ejemplo individual directamente desde el dataset:

```python
X, y = train_ds[0]
```

Esto devuelve una sola ventana, por ejemplo:

```python
print(X.shape)
print(y)
```

Forma esperada:

```python
torch.Size([24, 3])
tensor(...)
```

Pero para obtener un batch completo desde el `DataLoader`, lo normal es usar el iterador:

```python
X_batch, y_batch = next(iter(train_loader))
```

### Importante

Si el `DataLoader` se creó con:

```python
shuffle=True
```

entonces el primer batch no tiene por qué contener `train_ds[0]`, porque los datos se mezclan en cada época.

Para que el orden sea reproducible:

```python
train_loader = DataLoader(train_ds, batch_size=32, shuffle=False)
```

Resumen:

```python
train_ds[0]                 # primer ejemplo individual
next(iter(train_loader))    # primer batch
```

---

## Pregunta 3: What did we do so far?

### Respuesta

Se resumió el trabajo realizado hasta ese momento:

- Se localizó el notebook `07_deep_learning_intro.ipynb`.
- Se revisó que `TimeSeriesDataset` genera ventanas según `window_size`.
- Se identificó un desajuste entre `window_size=24` en los datasets/loaders y `window_size=12` en `MLPForecaster`.
- Se propuso usar `MLPForecaster(window_size=24, n_features=n_features)` o recrear datasets/loaders con `window_size=12`.
- Se indicó que, si el error continuaba, haría falta ver el traceback completo.
