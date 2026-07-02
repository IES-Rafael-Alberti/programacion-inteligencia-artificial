# Más allá del entrenamiento
## Técnicas para adaptar y ampliar modelos de IA

### Transfer learning 


### RAG (Retrieval-Augmented Generation)

### Diferencias clave entre `Transfer learning` y `RAG`

`Transfer learning` y `RAG` no hacen lo mismo.

`Transfer learning` consiste en reutilizar un modelo ya entrenado y adaptarlo a una tarea nueva. Por ejemplo, coger una red entrenada con millones de imágenes y reajustarla para clasificar flores. Aquí el conocimiento queda dentro del modelo.

`RAG` significa `Retrieval-Augmented Generation`. En vez de “meter” el conocimiento nuevo dentro del modelo mediante entrenamiento, el sistema busca información relevante en una base de datos o documentos y se la pasa al modelo en el momento de responder. Aquí el conocimiento está fuera del modelo y se recupera bajo demanda.

En corto:
- `Transfer learning`: adaptar el modelo con entrenamiento adicional.
- `RAG`: no reentrenar necesariamente; buscar contexto externo y usarlo al generar la respuesta.

Ejemplo rápido:
- Visión: usar `MobileNetV2` preentrenada para clasificar flores es `transfer learning`.
- Chat con apuntes: buscar fragmentos de tus PDFs y responder con ellos es `RAG`.

También pueden combinarse: un sistema puede tener un modelo afinado con `transfer learning` y además usar `RAG` para consultar información actualizada.