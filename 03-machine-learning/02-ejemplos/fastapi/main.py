# main.py – API para predicción con FastAPI

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="API de predicción de precios")

# Modelo pydantic para la entrada
class InputData(BaseModel):
    GrLivArea: float
    OverallQual: int
    GarageCars: int
    FullBath: int

# Cargar modelo
model = joblib.load("outputs/modelo_regresion.pkl")

@app.get("/")
def index():
    return {"mensaje": "API para predicción de precios con FastAPI"}

@app.post("/predict")
def predict(data: InputData):
    input_df = pd.DataFrame([data.dict()])
    pred = model.predict(input_df)[0]
    return {"precio_estimado": round(pred, 2)}
