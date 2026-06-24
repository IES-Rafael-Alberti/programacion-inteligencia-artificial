---
title: "Transformers 11: Ejemplo de Generación de Texto con Decoder-Only"
output:
  html_document:
    toc: true
    toc_depth: 2
    toc_float: true
    number_sections: true
    fig_caption: true
    code_folding: hide
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true
    fig_caption: true
    latex_engine: xelatex
---


# Ejemplo de Generación de Texto con Decoder-Only

Este ejemplo muestra cómo usar un modelo **decoder-only** para generación autoregresiva de texto.

Aquí la tarea ya no es transformar una secuencia en otra, sino:

* dar un comienzo de texto,
* y pedir al modelo que continúe.

---

## 1. ¿Por qué ya no usamos el Transformer completo?

En traducción, resumen o reformulación sí tiene sentido usar:

* encoder,
* decoder,
* y cross-attention.

Pero en generación libre no hace falta una secuencia de entrada separada.

Solo necesitamos:

* una secuencia parcial,
* y un modelo que prediga el siguiente token.

Por eso, en este caso, es más natural usar un **decoder-only**.

---

## 2. Archivos del ejemplo

El ejemplo usa:

* Corpus pequeño:
  `mini_estilo_quijote.txt`

* Script autosuficiente:
  `ejemplo_transformers_2_generacion_decoder_only.py`

El script es independiente y no modifica `transformerPytorch.py`.

---

## 3. Tipo de corpus

El corpus usa frases breves con tono narrativo inspirado en el castellano literario.

No pretende reproducir fielmente el Quijote, sino ofrecer un pequeño conjunto de texto con:

* cierta coherencia de estilo,
* vocabulario relacionado,
* y frases suficientemente homogéneas para entrenar un ejemplo de aula.

---

## 4. Tokenización por carácter

En este ejemplo se usa tokenización por **carácter**.

### Ventajas

* el vocabulario es pequeño,
* no hay problemas graves con palabras desconocidas,
* el código es más simple,
* y es muy útil para una primera demostración.

### Inconvenientes

* el modelo aprende más lentamente estructuras largas,
* y la generación suele ser menos estable que con subwords o palabras.

Aun así, para un primer ejemplo de decoder-only es una opción muy práctica.

---

## 5. Cómo se construye el dataset

El texto se convierte en una secuencia larga de caracteres codificados.

Luego se toman ventanas de longitud fija.

Ejemplo simplificado:

```text
texto original:   "en un lugar..."
entrada:          "<sos>en un luga"
salida esperada:  "en un lugar"
```

Esto significa que el modelo aprende a predecir **el siguiente carácter** en cada posición.

---

## 6. Arquitectura usada

El script implementa una clase:

* `DecoderOnlyTransformer`

Sus componentes son:

* embedding,
* codificación posicional,
* varias capas `DecoderOnlyLayer`,
* capa final al vocabulario.

Cada capa `DecoderOnlyLayer` contiene:

* self-attention enmascarada,
* feed-forward,
* conexión residual,
* layer normalization.

No hay:

* encoder,
* cross-attention,
* ni segunda secuencia de referencia.

---

## 7. Papel de la máscara causal

La máscara causal es la pieza más importante de este ejemplo.

Sirve para que el modelo:

* no vea caracteres futuros,
* y solo use el contexto ya disponible.

Eso convierte el problema en generación autoregresiva real.

Si quitáramos esta máscara, el modelo podría “hacer trampa” durante el entrenamiento.

---

## 8. Entrenamiento

El entrenamiento sigue este esquema:

1. se toma una ventana del texto,
2. el modelo predice el siguiente carácter,
3. se compara con la secuencia objetivo,
4. se calcula la pérdida,
5. se actualizan los pesos.

Es decir, el objetivo es:

* aprender a continuar texto.

---

## 9. Generación

Una vez entrenado, el modelo recibe un prompt, por ejemplo:

```text
en un lugar
```

Entonces:

1. genera un carácter,
2. lo añade a la secuencia,
3. vuelve a predecir,
4. y repite el proceso.

En este script la elección del siguiente carácter se hace por muestreo con temperatura.

### ¿Para qué sirve la temperatura?

* temperatura baja: texto más conservador,
* temperatura alta: texto más variado, pero también más errático.

---

## 10. Qué enseña este ejemplo

Este ejemplo permite mostrar:

* cuándo ya no hace falta un encoder,
* qué significa decoder-only,
* cómo se entrena un modelo de siguiente token,
* cómo funciona la máscara causal,
* y cómo se genera texto paso a paso.

---

## 11. Diferencia con el ejemplo de traducción

La diferencia central es esta:

### Traducción

* arquitectura: encoder-decoder
* datos: pares `entrada -> salida`
* usa cross-attention

### Generación libre

* arquitectura: decoder-only
* datos: una sola secuencia de texto
* no usa cross-attention

Este contraste ayuda mucho a entender por qué la arquitectura depende del tipo de tarea.

---

## 12. Limitaciones del ejemplo

Este ejemplo:

* usa un corpus pequeño,
* trabaja a nivel carácter,
* no genera literatura de gran calidad,
* y está pensado para comprender la mecánica, no para competir con modelos grandes.

Su valor principal es didáctico.

---

## 13. Idea final

Después de comparar este ejemplo con el de traducción, debería quedar clara una idea importante:

* cuando la tarea es **transformar una secuencia en otra**, encoder-decoder;
* cuando la tarea es **continuar una secuencia**, decoder-only.

Esa distinción es una de las decisiones arquitectónicas más importantes de este tema.

---
