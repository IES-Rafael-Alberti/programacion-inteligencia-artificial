# 🧭 Guía de pasos – Proyecto de IA con Python y Poetry

Esta guía reúne los pasos clave para desarrollar un proyecto completo de Inteligencia Artificial desde cero usando buenas prácticas, herramientas modernas y entornos controlados.

---

## 🔧 1. Crear estructura del proyecto con Poetry

```bash
poetry new mi_proyecto_ia
cd mi_proyecto_ia
```

O usar la plantilla descargable:
> `proyecto_poetry_ia.zip`

---

## 📦 2. Instalar dependencias

```bash
poetry add pandas seaborn matplotlib scikit-learn pycaret jupyterlab python-dotenv
```

---

## 🚀 3. Activar entorno

```bash
poetry shell
```

---

## 📁 4. Estructura recomendada

- `data/` → datos sin procesar
- `notebooks/` → análisis exploratorio (EDA), pruebas
- `src/` → scripts: `preprocessing/`, `training/`, `inference/`
- `outputs/` → modelos, resultados
- `.env` → claves secretas
- `pyproject.toml` → dependencias y configuración

---

## 📊 5. Explorar datos con pandas + seaborn

Usar notebooks como `notebooks/eda_basico.ipynb` o uno propio.

---

## 🧠 6. Modelado automático con PyCaret

```python
from pycaret.regression import *

setup(data=df, target='target', ...)
best = compare_models()
tuned = tune_model(best)
save_model(tuned, 'modelo_final')
```

---

## 🧪 7. Modelado manual con scikit-learn

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y)
model = RandomForestRegressor().fit(X_train, y_train)
print(r2_score(y_test, model.predict(X_test)))
```

---

## 🧾 8. Exportar dependencias

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

---

## 🌐 9. Despliegue con FastAPI o Streamlit (opcional)

---

## 🔐 10. Seguridad

Guardar claves API en `.env` y acceder desde Python con `os.getenv`.

---

¿Listo para comenzar tu proyecto?
