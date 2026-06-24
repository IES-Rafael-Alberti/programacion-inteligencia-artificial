# app.py – Streamlit para demo de predicción

import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Predicción de precio", layout="centered")

st.title("🏠 Predicción de precios de vivienda")
st.write("Este ejemplo usa un modelo entrenado para predecir el precio basado en características simples.")

# Cargar modelo entrenado
@st.cache_resource
def load_model():
    return joblib.load("outputs/modelo_regresion.pkl")

model = load_model()

# Entradas del usuario
st.header("Introduce los valores")

area = st.slider("Superficie (m²)", 30, 500, 100)
calidad = st.selectbox("Calidad general (1-10)", list(range(1, 11)))
garaje = st.selectbox("Número de plazas de garaje", [0, 1, 2, 3])
baños = st.radio("Número de baños", [1, 2, 3])

input_df = pd.DataFrame({
    "GrLivArea": [area],
    "OverallQual": [calidad],
    "GarageCars": [garaje],
    "FullBath": [baños]
})

# Predicción
if st.button("Predecir precio"):
    pred = model.predict(input_df)
    st.success(f"💰 Precio estimado: {int(pred[0]):,} €")

# Mostrar datos
with st.expander("Ver datos de entrada"):
    st.dataframe(input_df)
