# 🚀 Guía rápida – Despliegue de modelo con Streamlit

Esta guía te muestra cómo crear y ejecutar una aplicación web básica con [Streamlit](https://streamlit.io/) para predecir precios o clasificar datos usando un modelo entrenado en Python.

---

## 📦 1. Preparar el entorno de despliegue

En un proyecto Pixi independiente:

```bash
pixi init mi_proyecto
cd mi_proyecto
pixi add python=3.12 streamlit pandas numpy joblib scikit-learn
```

Pixi genera `pixi.toml` y `pixi.lock`; versiónalos y no instales paquetes globalmente.

---

## 📁 2. Estructura recomendada del proyecto

```
mi_proyecto/
├── app.py              # Aplicación Streamlit
├── outputs/
│   └── modelo.pkl      # Modelo de scikit-learn guardado con joblib
├── src/                # Código auxiliar (opcional)
├── data/               # Datos si se usan
└── pixi.toml          # Entorno y dependencias Pixi
```

---

## ✍️ 3. Estructura básica del archivo `app.py`

```python
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("outputs/modelo.pkl")

st.title("Predicción de precios")
area = st.slider("Superficie", 30, 500)
df = pd.DataFrame({ "GrLivArea": [area] })

if st.button("Predecir"):
    pred = model.predict(df)
    st.success(f"Precio estimado: {int(pred[0])} €")
```

---

## ▶️ 4. Ejecutar la app

```bash
pixi run streamlit run app.py
```

---

## 💡 Consejos

- Usa `st.selectbox`, `st.slider`, `st.radio` para capturar entradas.
- Usa `st.dataframe` o `st.plotly_chart` para visualizar datos.
- Usa `@st.cache_resource` para no recargar modelos cada vez.
- Si el modelo se guardó con scikit-learn, declara también `scikit-learn`: es necesario para deserializarlo con `joblib`.
- Versiona `pixi.toml` y `pixi.lock` si el despliegue vive en un proyecto independiente.

---

¿Listo para convertir tu modelo en una app web usable?
