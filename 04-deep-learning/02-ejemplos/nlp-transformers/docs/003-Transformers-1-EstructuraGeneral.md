---
title: "Transformers 1: Estructura General y Componentes"
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

# Modelo Transformer: Estructura General y Componentes

El modelo **Transformer**, introducido en el paper "Attention is All You Need" (Vaswani et al., 2017), es una arquitectura de red neuronal especialmente diseñada para procesar secuencias completas en paralelo, y es la base de modelos como BERT, GPT, T5 y otros.

Este documento presenta una explicación sencilla pero precisa de las partes fundamentales de un Transformer, y remite al documento sobre el *mecanismo de atención* para entender en detalle uno de sus componentes clave.

------------------------------------------------------------------------

## 🔎 1. Visión General

Un Transformer completo está compuesto por dos bloques principales:

-   **Codificador (Encoder)**: procesa la secuencia de entrada.
-   **Decodificador (Decoder)**: genera la secuencia de salida (en tareas como traducción o generación de texto).

Cada uno de estos bloques está formado por varias capas repetidas que incluyen:

-   Mecanismo de atención (self-attention o cross-attention).
-   Capas lineales (feed-forward).
-   Normalización y conexiones residuales.

------------------------------------------------------------------------

![Estructura del modelo Transformer](./EstructuraTransformer.png)

## 🧰 2. Componentes del Codificador (Encoder)

Cada capa del codificador contiene:

1.  **Mecanismo de Auto-Atención (Self-Attention)**

    -   Permite que cada palabra de la entrada se relacione con todas las demás.
    -   Calcula una nueva representación para cada palabra basada en su contexto.
    -   Detallado en el documento: “*Mecanismo de Atención*”.

2.  **Capa de Feed-Forward**

    -   Una red neuronal totalmente conectada aplicada a cada posición por separado.
    -   Generalmente incluye dos capas lineales con una función de activación intermedia (ReLU o GELU).

3.  **Normalización y conexiones residuales**

    -   Cada subbloque (atención o feed-forward) se envuelve con una conexión residual y una capa de normalización de capa (LayerNorm):

        ```         
        x = LayerNorm(x + Subbloque(x))
        ```

------------------------------------------------------------------------

## 🔄 3. Componentes del Decodificador (Decoder)

Cada capa del decodificador contiene:

1.  **Mecanismo de Auto-Atención enmascarado (Masked Self-Attention)**

    -   Impide que el modelo vea las siguientes palabras futuras al generar texto paso a paso.

2.  **Atención sobre la salida del codificador (Encoder-Decoder Attention)**

    -   Permite que cada posición del decodificador se enfoque en las salidas del codificador.

3.  **Capa de Feed-Forward** y **normalización/residuales**, igual que en el encoder.

------------------------------------------------------------------------

## 📈 4. Positional Encoding (Codificación Posicional)

El Transformer no tiene estructura secuencial interna como una RNN, por lo que se le debe indicar el orden de las palabras:

-   Se suma un vector posicional (sinusoidal o aprendido) a cada embedding de palabra.
-   Esto permite que el modelo distinga entre "El gato duerme" y "Duerme el gato".

------------------------------------------------------------------------

## 🔑 5. ¿Qué son Q, K y V?

En el mecanismo de atención, cada token de entrada se transforma en tres vectores:

-   **Q (Query o consulta)**: representa lo que ese token "busca" en los demás tokens.
-   **K (Key o clave)**: representa qué información ofrece cada token para ser comparada.
-   **V (Value o valor)**: representa el contenido que finalmente se combinará para construir la nueva representación contextual.

La idea es la siguiente:

1.  Se compara cada **Q** con todas las **K** para obtener puntuaciones de relevancia.
2.  Esas puntuaciones se normalizan con **softmax**.
3.  Los pesos resultantes se aplican sobre los **V**.

Así, el modelo decide **a qué tokens atender** y **qué información extraer de ellos**.

------------------------------------------------------------------------

## 🌟 6. Multi-Head Attention

En lugar de usar una sola cabeza de atención, el modelo ejecuta varias de manera paralela.
Cada cabeza puede enfocarse en diferentes aspectos de la secuencia:

-   Sintaxis
-   Semántica
-   Relaciones a largo plazo

Sus salidas se concatenan y se proyectan de nuevo:

```         
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
```

Cada cabeza se calcula como:

```         
head_i = Attention(Q W^Q_i, K W^K_i, V W^V_i)
```

------------------------------------------------------------------------

## 🔹 7. Flujo General

1.  El **input** se convierte en embeddings + codificación posicional.
2.  Pasa por varias **capas de codificador**.
3.  La salida del codificador se pasa al decodificador junto con la entrada parcial generada.
4.  El decodificador genera paso a paso la **salida final** (tokens), que luego se transforman en palabras.

------------------------------------------------------------------------

## ✅ Referencia complementaria

Para entender con más detalle el funcionamiento interno del mecanismo de atención (una parte clave del Transformer), consulta el documento:

➡️ *Mecanismo de Atención: explicación con ejemplos y código*

➡️ [Transformer con PyTorch](https://www.datacamp.com/es/tutorial/building-a-transformer-with-py-torch)

## Modelos Transformer optimizados

La arquitectura Transformer original es muy potente, pero **tiene un cuello de botella importante**: el **mecanismo de atención tiene coste cuadrático** respecto a la longitud de la secuencia (`O(n²)`), lo que hace que sea poco escalable para secuencias largas.
Por eso han surgido variantes como **Longformer**, **Performer**, **FlashAttention**, entre otras.

A continuación, se muestra una comparativa clara:

------------------------------------------------------------------------

## 🔍 Comparativa: Transformer vs Longformer, Performer, FlashAttention

| Modelo | Complejidad de atención | Técnica principal | Ventaja clave | Limitación principal |
|----|----|----|----|----|
| **Transformer** | `O(n²)` | Atención completa (full attention) | Alta capacidad contextual y precisión | Poco eficiente con secuencias largas |
| **Longformer** | `O(n)` | Atención **local + global** | Maneja textos largos (\> 4K tokens) eficientemente | Puede perder contexto lejano si no se usa atención global |
| **Performer** | `O(n)` | Atención aproximada (kernel-based) | Escalable, bajo consumo de memoria | Ligera pérdida de precisión comparado con full attention |
| **FlashAttention** | `O(n²)` (pero optimizada) | Atención exacta pero optimizada en GPU | Mucho más rápida y eficiente que la estándar | Requiere hardware compatible (GPUs modernas) |
| **Linformer** | `O(n)` | Proyección lineal de K y V | Muy rápido, especialmente para tareas largas | Reducción agresiva puede afectar la calidad |
| **Reformer** | `O(n log n)` | Locality-sensitive hashing (LSH) | Manejo eficiente de textos muy largos | Más compleja de implementar y entrenar |

------------------------------------------------------------------------

## 🧠 ¿Qué cambian estas variantes?

En lugar de calcular atención sobre todos los pares posibles (como el Transformer original), estas variantes:

-   **Limitan** el número de posiciones atendidas (ej: *Longformer*).
-   **Aproximan** los cálculos de atención (ej: *Performer*).
-   **Optimización en GPU** (ej: *FlashAttention* realiza los mismos cálculos pero reduciendo accesos a memoria).

------------------------------------------------------------------------

## ✅ ¿Cuándo usar cada uno?

-   **Transformer estándar**: secuencias cortas a medias (traducción, clasificación, codificación de texto).
-   **Longformer**: documentos largos, tareas de NLP como QA o resumen de textos largos.
-   **Performer**: visión por computadora o biología (secuencias muy largas, necesidad de bajo consumo).
-   **FlashAttention**: cuando se dispone de buena GPU y se quiere mantener precisión sin cambiar arquitectura.
-   **Linformer/Reformer**: en investigación o cuando se requiere memoria ultrabaja.

------------------------------------------------------------------------
