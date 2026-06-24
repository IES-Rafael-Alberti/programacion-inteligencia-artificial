# 🧠 Introducción a Feature Stores con Hopsworks

## ¿Qué es una Feature Store?

Una *feature store* es un sistema diseñado para **almacenar, versionar y servir características (features)** de manera centralizada en proyectos de Machine Learning. Sirve como punto de conexión entre:

- La etapa de **preprocesamiento y limpieza**
- El **entrenamiento de modelos**
- El **despliegue en producción**

---

## ¿Por qué usar una Feature Store?

- ✅ Evita re-calcular las mismas features en entrenamiento y en inferencia
- ✅ Permite reutilizar y compartir transformaciones
- ✅ Versiona los datos utilizados por modelos distintos
- ✅ Escala mejor cuando hay muchos equipos o flujos de datos

---

## ¿Qué es Hopsworks?

Hopsworks es una plataforma de Feature Store con una versión gratuita para educación. Permite:

- Subir datasets como "feature groups"
- Visualizar y explorar con interfaz web
- Consultar desde Python, notebooks, APIs o flujos de entrenamiento

➡️ Registro gratuito: https://www.hopsworks.ai/signup

---

## Cuándo usar una Feature Store (y cuándo no)

| Cuándo usarla                              | Cuándo no es necesario                       |
|--------------------------------------------|-----------------------------------------------|
| Si el dataset se usa en varios proyectos   | Si solo se usa localmente                    |
| Si se entrena el modelo varias veces       | Si solo se entrena una vez                   |
| Si varios usuarios acceden a los mismos datos | Si es un trabajo individual o por pareja |
| Si se automatiza despliegue y reentrenamiento | Si todo ocurre en notebooks locales       |

---

## Ejemplo: usar Hopsworks con un dataset meteorológico

1. Crear una cuenta en Hopsworks
2. Crear un *Feature Group* (ej. `meteo_sevilla`)
3. Subir el dataset (`df.to_csv`, luego importar desde interfaz)
4. Desde tu notebook o script de entrenamiento, conectar vía API:
```python
import hopsworks

project = hopsworks.login()
fs = project.get_feature_store()

dataset = fs.get_feature_group("meteo_sevilla", version=1).read()
```

---

## ¿Es obligatorio?

No. Es una herramienta **profesional** para flujos reales en producción. Aquí puedes usarla como *experimento opcional avanzado* o para practicar cómo conectar un sistema real a tus modelos.

---

¿Te gustaría probarlo con tu dataset de películas o meteo?

> Si es así, sigue el notebook de ejemplo que acompaña esta actividad.
