# 🚀 Guía rápida – Despliegue de modelo con FastAPI

Esta guía explica cómo desplegar un modelo de machine learning como una API REST usando [FastAPI](https://fastapi.tiangolo.com/).

---

## 📦 1. Preparar el entorno de despliegue

En un proyecto Pixi independiente:

```bash
pixi init mi_api
cd mi_api
pixi add python=3.12 fastapi uvicorn pandas joblib scikit-learn
```

Pixi genera `pixi.toml` y `pixi.lock`; versiónalos y no instales paquetes globalmente.
`scikit-learn` es necesario para cargar el modelo del ejemplo incluido; si usas un
modelo creado con otra biblioteca, añade también su dependencia de ejecución.

---

## 🗂️ 2. Estructura recomendada del proyecto

```
mi_api/
├── main.py                     # API principal con endpoints
├── outputs/modelo.pkl          # Modelo entrenado
└── pixi.toml                  # Entorno y dependencias Pixi
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
pixi run uvicorn main:app --reload
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
pixi run uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2
```

Puedes combinarlo con Docker, Nginx, o plataformas cloud como Render o Railway.

---

## ✅ Ventajas

- Validación automática de entrada
- Documentación integrada
- Rápido, escalable y fácil de extender

---

¿Listo para convertir tu modelo en un servicio web?
