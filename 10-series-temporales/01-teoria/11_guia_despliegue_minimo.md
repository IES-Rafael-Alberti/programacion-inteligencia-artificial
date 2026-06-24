# Guía de Despliegue Mínimo: Modelo de Series Temporales

Este documento describe la arquitectura y los pasos necesarios para convertir un modelo entrenado de Python en un servicio accesible mediante una API REST, además de incluir una opción para una demostración interactiva educativa.

## 1. Arquitectura del Despliegue
Para garantizar que el modelo sea portable y escalable, utilizaremos el siguiente stack:
- **Modelo:** Serializado en formato `.pkl` o `.joblib`.
- **API Framework:** FastAPI (estándar moderno por su velocidad y tipado).
- **Servidor ASGI:** Uvicorn (para ejecutar la API).
- **Contenerización:** Docker (para empaquetar dependencias y entorno).
- **Host:** Render / Railway / Azure Container Instances.

## 2. Estructura de Archivos Recomendada
```text
proyecto-despliegue/
├── app/
│   ├── main.py            # Lógica de la API
│   └── modelo_series.pkl   # El modelo ya entrenado
├── requirements.txt       # Dependencias (fastapi, uvicorn, scikit-learn, pandas, etc.)
└── Dockerfile             # Configuración de la imagen de contenedor
```

## 3. Componentes Técnicos

### A. La API (`main.py`)
El objetivo es crear un "endpoint" que reciba datos y devuelva la predicción. 
- **Método:** `POST /predict`
- **Entrada:** JSON con los últimos valores de la serie (lags).
- **Salida:** JSON con el valor predicho.

### B. El Entorno (`Dockerfile`)
El Dockerfile evita el problema de "en mi máquina funciona". Define:
1. La versión de Python.
2. La instalación de librerías necesarias.
3. El comando de arranque del servidor.

## 4. Pasos para el Despliegue (Flujo de Trabajo)

1. **Exportación:** Guardar el modelo entrenado usando `joblib.dump(model, 'modelo_series.pkl')`.
2. **Desarrollo Local:** Probar la API localmente con `uvicorn main:app --reload`.
3. **Contenerización:** Construir la imagen: `docker build -t modelo-series .`.
4. **Subida a Nube:** 
   - Subir el código a un repositorio de GitHub.
   - Conectar el repositorio a un servicio de despliegue (ej. Render).
   - El servicio detectará el `Dockerfile` y desplegará el endpoint automáticamente.

## 5. Cómo Consumir el Modelo
Una vez desplegado, el modelo se puede llamar desde cualquier lenguaje (Python, JS, Curl) enviando una petición HTTP:

```bash
curl -X POST "https://tu-servicio.com/predict" \
     -H "Content-Type: application/json" \
     -d '[12.5, 13.2, 11.8, 14.1]'
```

## 6. Demostración Interactiva para Alumnos con Gradio (Opcional)
Para hacer el taller más interactivo y permitir que los alumnos "jueguen" con el modelo, podemos crear una interfaz web sencilla usando **Gradio**. Esta es una herramienta excelente para la educación porque permite manipular parámetros en tiempo real y ver resultados visuales inmediatamente.

### 6.1 ¿Por qué Gradio en el contexto educativo?
- **Interfaz automática:** Genera sliders, cuadros de texto y áreas de salida sin necesidad de HTML/CSS/JS.
- **Feedback instantáneo:** Los alumnos cambian un parámetro y ven el efecto en el forecast al momento.
- **Enfoque conceptual:** Les permite concentrarse en entender el impacto de los lags, la estacionalidad, etc., sin distraerse con código de frontend.
- **Portabilidad:** Se puede ejecutar localmente o desplegar fácilmente junto con la API.

### 6.2 Estructura de Archivos Ampliada (para incluir demo)
```text
proyecto-despliegue/
├── app/
│   ├── main.py            # Lógica de la API (FastAPI)
│   ├── demo_gradio.py     # Interfaz interactiva para alumnos (Gradio)
│   └── modelo_series.pkl   # El modelo ya entrenado
├── requirements.txt       # Dependencias (fastapi, uvicorn, scikit-learn, pandas, gradio, etc.)
└── Dockerfile             # Configuración de la imagen de contenedor
```

### 6.3 Ejemplo de Implementación (`demo_gradio.py`)
Este archivo crea una interfaz donde los alumnos pueden ajustar los valores de los lags y ver la predicción resultante:

```python
import gradio as gr
import joblib
import numpy as np

# Cargar el modelo entrenado
model = joblib.load("modelo_series.pkl")

def forecast_con_lags(lag1, lag2, lag3):
    """
    Función que hace la predicción basada en los últimos 3 valores de la serie.
    Los alumnos pueden manipular estos valores con sliders.
    """
    # Preparar la entrada para el modelo (asumiendo que espera 3 lags)
    input_data = np.array([[lag1, lag2, lag3]])
    prediction = model.predict(input_data)
    return f"Predicción para el próximo período: {prediction[0]:.2f} unidades"

# Crear la interfaz de Gradio
iface = gr.Interface(
    fn=forecast_con_lags,
    inputs=[
        gr.Slider(0, 100, step=0.1, label="Lag 1 (Valor de ayer)", value=25.0),
        gr.Slider(0, 100, step=0.1, label="Lag 2 (Valor de anteayer)", value=23.5),
        gr.Slider(0, 100, step=0.1, label="Lag 3 (Valor de hace 3 días)", value=22.0)
    ],
    outputs=gr.Label(label="Resultado del Forecast"),
    title="🔮 Demo Interactiva: Forecasting de Series Temporales",
    description="""
    Ajusta los sliders para cambiar los valores históricos de la serie y observa 
    cómo afecta la predicción del modelo. Este ejercicio ayuda a entender:
    - La importancia de los valores recientes (lags)
    - Cómo el modelo aprende patrones de dependencia temporal
    - El concepto de 'horizonte de predicción'
    """,
    article="""
    ### Instrucciones para el ejercicio:
    1. Comienza con los valores por defecto y observa la predicción base.
    2. Incremente gradualmente el Lag 1 (ayer) y note cómo cambia el forecast.
    3. Prueba valores extremos (muy altos o muy bajos) para ver la sensibilidad del modelo.
    4. Intente replicar un patrón estacional: establezca valores altos en Lag 1 y bajos en Lag 2-3.
    """
)

# Para lanzar la interfaz (en desarrollo local)
if __name__ == "__main__":
    iface.launch()
```

### 6.4 Cómo usar la demo en el taller
1. **Ejecutar localmente:** Los alumnos pueden correr `python demo_gradio.py` en sus máquinas para experimentar.
2. **Desplegar junto con la API:** Modificar el `Dockerfile` para exponer ambos servicios (API en `/predict` y demo en `/demo` o en un puerto diferente).
3. **Enfoque híbrido profesional:** La API (`main.py`) sirve como backend serio para integraciones reales, mientras que la demo (`demo_gradio.py`) es una herramienta pedagógica que consume esa misma API (o accede directamente al modelo para simplificar).

### 6.5 Buenas prácticas para el entorno educativo
- **Separación de preocupaciones:** Mantener la lógica del modelo pura y reutilizable entre ambas interfaces.
- **Version control:** Incluir tanto `main.py` como `demo_gradio.py` en el repositorio.
- **Requirements actualizados:** Añadir `gradio` al `requirements.txt`.
- **Documentación clara:** Explicar cuándo usar cada herramienta (API para integración, demo para exploración).

## 7. Elección entre Enfoques
- **Use FastAPI solo** cuando el objetivo es crear un servicio de producción o enseñar prácticas de backend profesional.
- **Añada Gradio** cuando el objetivo sea maximizar la participación y comprensión intuitiva en un contexto educativo o de demostración.
- **Considere ambos** cuando quiera mostrar la diferencia entre una herramienta de producción (FastAPI) y una de exploración (Gradio), ambas alimentadas por el mismo modelo subyacente.
