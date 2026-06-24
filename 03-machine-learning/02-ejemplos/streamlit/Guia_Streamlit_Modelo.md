# 🚀 Guía rápida – Despliegue de modelo con Streamlit

Esta guía te muestra cómo crear y ejecutar una aplicación web básica con [Streamlit](https://streamlit.io/) para predecir precios o clasificar datos usando un modelo entrenado en Python.

---

## 📦 1. Instalar Streamlit

Si usas Poetry, añade:

```bash
poetry add streamlit joblib
```

---

## 📁 2. Estructura recomendada del proyecto

```
mi_proyecto/
├── app.py              # Aplicación Streamlit
├── outputs/
│   └── modelo.pkl      # Modelo entrenado (scikit-learn o PyCaret)
├── src/                # Código auxiliar (opcional)
├── data/               # Datos si se usan
└── pyproject.toml      # Dependencias
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
poetry run streamlit run app.py
```

---

## 💡 Consejos

- Usa `st.selectbox`, `st.slider`, `st.radio` para capturar entradas.
- Usa `st.dataframe` o `st.plotly_chart` para visualizar datos.
- Usa `@st.cache_resource` para no recargar modelos cada vez.
- Usa `poetry export` si vas a desplegar en cloud.

---

¿Listo para convertir tu modelo en una app web usable?
