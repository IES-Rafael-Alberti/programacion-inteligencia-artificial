# Feature Store

## Definición

Un feature store es un repositorio de variables predictivas para sistemas de machine learning. Su función principal es almacenar, servir y reutilizar las mismas variables tanto en entrenamiento como en inferencia.

### Ejemplos de variables

- Número de compras en los últimos 7 días.
- Edad del cliente.
- Tiempo desde la última transacción.
- Embedding de producto para recomendación.

## Problemas que resuelve

1. Reutilización de variables entre modelos.
2. Consistencia entre entrenamiento e inferencia.
3. Acceso rápido a variables actualizadas.
4. Gobierno del dato: documentación, trazabilidad y control.

---

## Arquitectura dual

```text
+-----------------------------------------------------------+
|                       Feature Store                       |
+---------------------------+-------------------------------+
|   Almacén offline         |   Almacén online             |
|   Entrenamiento           |   Inferencia                 |
+---------------------------+-------------------------------+
| Datos históricos          | Datos actualizados           |
| Spark, Iceberg            | Redis, RonDB u otros         |
| Procesos por lotes        | Baja latencia                |
+---------------------------+-------------------------------+
```

El almacén offline se usa para entrenamiento y análisis histórico. El almacén online se usa para servir variables en tiempo real durante la inferencia.

---

## Ejemplo práctico

En un sistema de detección de fraude:

- En entrenamiento se calculan variables históricas con meses o años de datos.
- En inferencia se necesitan esas mismas variables con latencia muy baja.

Si la lógica de cálculo no es idéntica, aparece el problema de inconsistencia entre entrenamiento e inferencia.

---

## Inconsistencia entre entrenamiento e inferencia

Este problema aparece cuando una variable se calcula de una forma durante el entrenamiento y de otra distinta en producción.

### Por qué ocurre

1. Se usan fuentes de datos distintas.
2. Se reimplementa la lógica manualmente.
3. Cambian las ventanas temporales o la lógica de negocio.
4. El código evoluciona en un sitio y no en otro.

### Consecuencia

El modelo se entrena con unas variables y luego recibe otras diferentes en producción. El resultado es una degradación del rendimiento o incluso errores difíciles de detectar.

### Ejemplo

```python
# Entrenamiento
df["tiempo_desde_ultima_compra"] = (fecha_actual - ultima_compra).days

# Producción
df["tiempo_desde_ultima_compra"] = (ultima_compra - fecha_actual).days
```

El modelo aprende con valores positivos, pero en producción recibe valores negativos.

### Cómo ayuda un feature store

```text
Definición única de la variable
        |
        +--> cálculo para entrenamiento
        |
        +--> cálculo para inferencia
```

La lógica queda centralizada y se reutiliza en ambos contextos.

---

## Alternativas habituales

### Feast

- Software libre.
- Flexible y muy usado en entornos de aprendizaje.
- Requiere desplegar parte de la infraestructura.

### Feathr

- Software libre.
- Orientado a pipelines de variables y reutilización entre entrenamiento e inferencia.
- Interesante si se quiere una alternativa abierta al ecosistema de plataformas gestionadas.

### Tecton

- Plataforma gestionada.
- Buena experiencia de uso, pero más dependiente del proveedor.

### Hopsworks

- Solución integrada con orientación a proyectos de datos y ML.
- Buen encaje cuando se quiere un enfoque más completo.

### Servicios integrados de plataforma

| Plataforma | Servicio |
|------------|----------|
| AWS | SageMaker Feature Store |
| Google Cloud | Vertex AI Feature Store |
| Azure | Azure ML Feature Store |
| Databricks | Feature Engineering / Feature Store |

### Alternativas libres o gratuitas

| Herramienta | Tipo | Comentario |
|-------------|------|------------|
| Feast | Software libre | La referencia más habitual en docencia |
| Feathr | Software libre | Buen ejemplo de alternativa abierta |
| Hopsworks Community / free tier | Gratuita con límites | Útil para pruebas o aprendizaje |

---

## Comparativa rápida

| Herramienta | Tipo | Ventaja principal | Limitación |
|-------------|------|-------------------|------------|
| Feast | Software libre | Flexibilidad | Más trabajo de despliegue |
| Feathr | Software libre | Alternativa abierta orientada a producción | Menor adopción en clase |
| Tecton | Gestionada | Facilidad y experiencia de uso | Dependencia del proveedor |
| Hopsworks | Gestionada / plataforma | Solución integrada | Mayor complejidad y coste |

---

## Aplicación al proyecto

Antes de elegir esta categoría, conviene responder:

1. ¿El proyecto necesita reutilizar variables entre varios modelos?
2. ¿Hace falta inferencia en tiempo real?
3. ¿Es importante asegurar la misma lógica entre entrenamiento e inferencia?
4. ¿Compensa la complejidad adicional para el tamaño del proyecto?

En muchos proyectos académicos un feature store completo puede no ser imprescindible. Aun así, entender su papel ayuda a justificar cuándo conviene usarlo y cuándo no.

---

## Fuentes recomendadas

- Documentación oficial de Feast.
- Documentación oficial de Feathr.
- Documentación oficial de Tecton.
- Documentación oficial de Hopsworks.
- Documentación oficial de SageMaker Feature Store, Vertex AI Feature Store y Azure ML.
