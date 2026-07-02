# Gradio: documentación práctica

Gradio es una librería de Python para crear interfaces web sobre modelos, funciones o pipelines de IA. Es especialmente útil para construir demos rápidas sin programar una aplicación web completa.

## Para qué sirve

1. Probar modelos con entradas reales de usuario.
2. Enseñar resultados de IA de forma visual.
3. Compartir prototipos con personas no técnicas.
4. Depurar errores de preprocesado.
5. Publicar demos sencillas en Hugging Face Spaces.

## Estructura típica

Una demo Gradio suele tener tres partes:

1. Un modelo o función Python.
2. Una función `predict` que adapta las entradas al formato esperado.
3. Una interfaz con entradas, salidas y ejemplos.

```python
import gradio as gr

def predict(texto):
    return texto.upper()

demo = gr.Interface(fn=predict, inputs="text", outputs="text")
demo.launch()
```

## Componentes habituales

### Entradas

1. `gr.Textbox`: texto.
2. `gr.Number`: valores numéricos.
3. `gr.Slider`: valores numéricos acotados.
4. `gr.Dropdown`: selección entre opciones.
5. `gr.Image`: imágenes.
6. `gr.Audio`: audio.
7. `gr.Dataframe`: tablas.
8. `gr.File`: archivos.

### Salidas

1. `gr.Textbox`: texto.
2. `gr.Label`: clasificación con probabilidades.
3. `gr.JSON`: información estructurada o depuración.
4. `gr.Dataframe`: resultados tabulares.
5. `gr.Image`: imagen generada o procesada.

## `Interface` frente a `Blocks`

`gr.Interface` es la opción más rápida cuando hay una función, unas entradas y unas salidas.

```python
demo = gr.Interface(
    fn=predict,
    inputs=[gr.Number(), gr.Number()],
    outputs=gr.Label(),
)
```

`gr.Blocks` permite interfaces más flexibles con filas, columnas, pestañas, botones y eventos.

```python
with gr.Blocks() as demo:
    entrada = gr.Textbox(label="Pregunta")
    boton = gr.Button("Responder")
    salida = gr.Textbox(label="Respuesta")
    boton.click(fn=predict, inputs=entrada, outputs=salida)
```

## Funcionalidades avanzadas

### Estado

`gr.State` permite conservar información entre interacciones.

```python
with gr.Blocks() as demo:
    contador = gr.State(0)
    boton = gr.Button("Sumar")
    salida = gr.Number()

    def incrementar(n):
        return n + 1, n + 1

    boton.click(incrementar, inputs=contador, outputs=[contador, salida])
```

### Eventos

Además de `click`, Gradio permite eventos como `change`, `submit` o `upload`.

```python
texto = gr.Textbox()
resultado = gr.Textbox()
texto.submit(fn=predict, inputs=texto, outputs=resultado)
```

### Ejemplos y caché

```python
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(),
    outputs=gr.Label(),
    examples=[["./imagenes/gato.jpg"], ["./imagenes/perro.jpg"]],
    cache_examples=True,
)
```

### Feedback de usuarios

Gradio puede permitir que los usuarios marquen respuestas incorrectas.

```python
demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(),
    outputs=gr.Textbox(),
    flagging_mode="manual",
)
```

### Streaming

Útil para respuestas generadas progresivamente por un LLM.

```python
def generar(prompt):
    for palabra in prompt.split():
        yield palabra + " "
```

## Ejemplo más completo

```python
import gradio as gr

def predict(image, threshold):
    result = modelo.predict(image)
    return result, {"threshold": threshold}

with gr.Blocks(title="Clasificador de imágenes") as demo:
    gr.Markdown("# Clasificador de imágenes")
    with gr.Row():
        imagen = gr.Image(type="pil", label="Sube una imagen")
        threshold = gr.Slider(0, 1, value=0.5, label="Umbral")
    salida = gr.Label(label="Predicción")
    debug = gr.JSON(label="Depuración")
    boton = gr.Button("Clasificar")
    boton.click(predict, inputs=[imagen, threshold], outputs=[salida, debug])
```

## Buenas prácticas

1. Probar `predict` antes de conectarlo a la interfaz.
2. Separar preprocesado, modelo y postprocesado.
3. Añadir ejemplos para facilitar la prueba.
4. Usar `gr.JSON` durante la depuración.
5. No lanzar servidores automáticamente en notebooks de corrección.
6. Controlar qué ocurre si faltan pesos o dependencias.

## Errores frecuentes

1. La función espera un array, pero Gradio entrega una imagen PIL o una ruta.
2. Las dimensiones de entrada no coinciden con las del modelo.
3. Las probabilidades no se devuelven en el formato esperado por `gr.Label`.
4. Se lanza `demo.launch()` en una celda que debería ejecutarse automáticamente.
5. No se normalizan las entradas igual que en entrenamiento.

## Relación con los notebooks

`Fase1/93_gradio_intro.ipynb` trabaja una demo tabular con Iris.

`Fase2/96_gradio_model.ipynb` trabaja una demo de imágenes con preprocesado y salida de depuración.

## Cuándo usar Gradio

Usa Gradio para demos rápidas, prototipos y presentaciones. Si necesitas una API profesional, autenticación avanzada o integración con otros sistemas, usa FastAPI.

Documentación oficial: https://www.gradio.app/
