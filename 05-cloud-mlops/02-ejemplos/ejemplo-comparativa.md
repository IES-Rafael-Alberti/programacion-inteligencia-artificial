# Ejemplo de comparativa de herramientas cloud para IA

> Este documento es solo un modelo orientativo. Cada grupo debe adaptarlo a su propio proyecto.

## Proyecto de ejemplo

```text
Proyecto: Sistema de recomendación de películas
Fuentes de datos: valoraciones de usuarios en CSV, metadatos de películas desde API y tabla de usuarios
Problema a resolver: recomendar películas personalizadas y explicar la recomendación
Usuarios o contexto de uso: aplicación web para consulta de recomendaciones
```

---

## Ejemplo de entrega individual: Feature Store


# Comparativa: Feature Store

## Proyecto
- Proyecto: Sistema de recomendación de películas
- Fuentes de datos: valoraciones de usuarios en CSV, metadatos de películas desde API y tabla de usuarios
- Problema a resolver: recomendar películas personalizadas y explicar la recomendación
- Contexto de uso: aplicación web para consulta de recomendaciones

## 1. Alternativas investigadas
| Herramienta | Coste | Dificultad | Ventajas | Inconvenientes |
|-------------|-------|------------|----------|----------------|
| Feast | Bajo si se autogestiona | Media | Flexible y software libre | Requiere despliegue e integración |
| Hopsworks | Medio | Media | Solución muy integrada | Más compleja para un proyecto académico |
| SageMaker Feature Store | Medio | Baja | Integración con AWS | Más dependiente del ecosistema AWS |

## 2. Análisis para el proyecto
El proyecto necesita calcular variables de usuario y de película, como media de valoraciones, géneros preferidos y número de interacciones recientes. Estas variables pueden reutilizarse tanto en entrenamiento como en inferencia.

Un feature store tendría sentido si el sistema necesitara servir recomendaciones en tiempo real con variables actualizadas y si varias partes del proyecto compartieran esas mismas variables. Sin embargo, al tratarse de un proyecto académico con una arquitectura moderada, también podría resolverse con tablas preparadas en Parquet sin desplegar un feature store completo.

## 3. Herramienta elegida
No aplica como componente obligatorio.

## 4. Justificación
Aunque la categoría es relevante y se ha analizado, el grupo ha decidido no incorporar un feature store completo. La razón principal es que el proyecto puede trabajar con variables precalculadas en procesos por lotes y no necesita inferencia con latencias muy bajas ni reutilización compleja entre muchos modelos.

## 5. Ejemplo de uso
```python
import polars as pl

ratings = pl.read_csv("ratings.csv")

features = ratings.group_by("movie_id").agg(
    pl.col("rating").mean().alias("rating_medio"),
    pl.len().alias("n_valoraciones")
)

features.write_parquet("features_peliculas.parquet")
```

## 6. Fuentes consultadas
- Documentación oficial de Feast
- Documentación oficial de Hopsworks
- Documentación oficial de SageMaker Feature Store


---

## Ejemplo de entrega individual: Compute Cloud

# Comparativa: Compute Cloud

## Proyecto
- Proyecto: Sistema de recomendación de películas
- Fuentes de datos: valoraciones de usuarios en CSV, metadatos de películas desde API y tabla de usuarios
- Problema a resolver: recomendar películas personalizadas y explicar la recomendación
- Contexto de uso: aplicación web para consulta de recomendaciones

## 1. Alternativas investigadas
| Herramienta | Coste | Dificultad | Ventajas | Inconvenientes |
|-------------|-------|------------|----------|----------------|
| Google Colab | Bajo | Baja | Muy fácil para pruebas | Poco adecuado para flujos estables |
| AWS EC2 | Medio | Media | Control total e integración con AWS | Más configuración |
| SageMaker | Medio-alto | Baja | Entrenamiento y despliegue gestionados | Mayor dependencia de la plataforma |

## 2. Análisis para el proyecto
El sistema de recomendación no necesita entrenamiento intensivo con GPU. La mayor parte del trabajo puede hacerse con CPU y procesamiento tabular. Por tanto, lo importante no es disponer de una GPU muy potente, sino tener un entorno reproducible, cómodo y compatible con el almacenamiento elegido.

## 3. Herramienta elegida
AWS EC2

## 4. Justificación
El grupo ha elegido AWS EC2 porque ofrece suficiente control para instalar librerías, ejecutar el entrenamiento y conectar con S3 sin añadir demasiada complejidad. SageMaker sería una opción sólida, pero para este proyecto concreto EC2 resulta más sencillo de entender y suficiente en capacidad.

## 5. Ejemplo de uso
```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

train = pd.read_parquet("s3://bucket/datos_train.parquet")

X = train[["rating_medio", "n_valoraciones"]]
y = train["objetivo"]

model = RandomForestRegressor()
model.fit(X, y)
```

## 6. Fuentes consultadas
- Documentación oficial de Amazon EC2
- Documentación oficial de Amazon SageMaker
- Documentación oficial de Google Colab


---

## Ejemplo de entrega individual: APIs de LLM

# Comparativa: APIs de LLM

## Proyecto
- Proyecto: Sistema de recomendación de películas
- Fuentes de datos: valoraciones de usuarios en CSV, metadatos de películas desde API y tabla de usuarios
- Problema a resolver: recomendar películas personalizadas y explicar la recomendación
- Contexto de uso: aplicación web para consulta de recomendaciones

## 1. Alternativas investigadas
| Herramienta | Coste | Dificultad | Ventajas | Inconvenientes |
|-------------|-------|------------|----------|----------------|
| OpenAI | Medio | Baja | API sencilla y buen ecosistema | Coste por uso |
| Anthropic | Medio | Baja | Buen rendimiento en redacción | Menor familiaridad del equipo |
| Google AI | Bajo-medio | Media | Contexto amplio e integración con GCP | Menos alineado con la arquitectura del grupo |

## 2. Análisis para el proyecto
El LLM no es el componente central del sistema de recomendación, pero puede aportar valor al generar una explicación textual del motivo de la recomendación. En este caso interesa una API fácil de integrar y con coste moderado, ya que el volumen previsto de uso es bajo.

## 3. Herramienta elegida
OpenAI

## 4. Justificación
Se elige OpenAI porque permite integrar rápidamente la generación de explicaciones en Python, tiene buena documentación y encaja con un uso secundario del LLM dentro del proyecto. No hace falta un sistema complejo de agentes ni una ventana de contexto extrema.

## 5. Ejemplo de uso
```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

def explicar_recomendacion(pelicula, preferencias):
    prompt = f"""
    Usuario: {preferencias}
    Película recomendada: {pelicula}
    Explica en dos frases por qué esta recomendación tiene sentido.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
```

## 6. Fuentes consultadas
- Documentación oficial de OpenAI
- Documentación oficial de Anthropic
- Documentación oficial de Google AI


---

## Ejemplo de documento grupal consolidado

# Proyecto: Sistema de recomendación de películas

## 1. Descripción del proyecto
- Fuentes de datos: valoraciones de usuarios, metadatos de películas y tabla de usuarios
- Problema a resolver: recomendar películas personalizadas y explicar la recomendación
- Usuarios o contexto: aplicación web para consulta individual

## 2. Decisiones por categoría
| Categoría | Herramienta elegida | Justificación breve |
|-----------|---------------------|---------------------|
| Feature Store | No aplica | El proyecto puede trabajar con variables precalculadas por lotes |
| Compute | AWS EC2 | Entorno suficiente y controlado para entrenamiento y pruebas |
| MLOps | MLflow | Permite registrar experimentos sin añadir demasiada complejidad |
| Framework | scikit-learn | Adecuado para un sistema de recomendación tabular sencillo |
| APIs de LLM | OpenAI | Se usará solo para explicar recomendaciones |
| Orquestación | No aplica | No se necesita RAG ni agentes |
| Datos | Polars | Rápido y suficiente para el tamaño del dataset |
| Almacenamiento | S3 + Parquet | Integración simple con compute y artefactos |

## 3. Coherencia de la solución
La propuesta prioriza simplicidad, reproducibilidad y bajo coste. Polars prepara los datos, S3 almacena datasets y artefactos, EC2 ejecuta el entrenamiento y MLflow registra los experimentos. OpenAI solo se usa para generar una explicación textual de la recomendación final, por lo que no condiciona el resto de la arquitectura.

## 4. Arquitectura o flujo
Datos en CSV y API -> limpieza con Polars -> almacenamiento en S3/Parquet -> entrenamiento en EC2 con scikit-learn -> registro en MLflow -> recomendación final -> explicación breve con OpenAI

## 5. Fuentes principales
- Documentación oficial de Amazon S3 y EC2
- Documentación oficial de Polars
- Documentación oficial de scikit-learn
- Documentación oficial de MLflow
- Documentación oficial de OpenAI


---

## Qué muestra este ejemplo

- Cómo justificar que una categoría sí aplica o no aplica.
- Cómo conectar cada decisión con el proyecto concreto.
- Cómo sintetizar la parte grupal sin copiar sin más los documentos individuales.
