# 🚀 Guía rápida – Despliegue de modelo con FastAPI

Esta guía explica cómo desplegar un modelo de machine learning como una API REST usando [FastAPI](https://fastapi.tiangolo.com/).

---

## 📦 1. Instalar FastAPI y dependencias

```bash
poetry add fastapi uvicorn pydantic joblib
```

---

## 🗂️ 2. Estructura recomendada del proyecto

```
mi_api/
├── main.py                     # API principal con endpoints
├── outputs/modelo.pkl          # Modelo entrenado
└── pyproject.toml              # Proyecto Poetry
```

---

## ✍️ 3. Estructura básica del archivo `main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: int

model = joblib.load("outputs/modelo.pkl")

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    return {"resultado": prediction}
```

---

## ▶️ 4. Ejecutar servidor

```bash
poetry run uvicorn main:app --reload
```

---

## 📬 5. Probar la API

Accede a la documentación automática:

```
http://127.0.0.1:8000/docs
```

Ejemplo de JSON para POST:

```json
{
  "feature1": 135.0,
  "feature2": 7
}
```

---

## 📦 6. Opcional: Despliegue en producción

Para producción usa:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2
```

Puedes combinarlo con Docker, Nginx, o plataformas cloud como Render o Railway.

---

## ✅ Ventajas

- Validación automática de entrada
- Documentación integrada
- Rápido, escalable y fácil de extender

---

¿Listo para convertir tu modelo en un servicio web?
