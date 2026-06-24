# Script de exportación de modelos

Este script sirve para pasar del notebook de entrenamiento a la mini API FastAPI.

## Archivos generados

- `tfidf_vectorizer.joblib`
- `tfidf_model.joblib`
- `lstm_model.keras`
- `lstm_tokenizer.json`
- `label_mapping.json` (opcional)

## Uso mínimo en notebook

```python
from export_models import export_tfidf_assets, export_lstm_assets

export_tfidf_assets(vectorizer, clf)
export_lstm_assets(model, tokenizer)
```

## Copiar a la API

```python
from export_models import copy_to_api_models

copy_to_api_models(export_dir="exported_models", api_models_dir="models")
```

## Recomendación didáctica

Haz que los alumnos:
1. entrenen en notebook
2. exporten artefactos
3. prueben la API con `curl` o Swagger
