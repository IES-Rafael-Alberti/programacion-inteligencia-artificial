---
title: "Transformers 12: Ejemplo Completo de Reformulación de Texto"
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


# Ejemplo Completo de Reformulación de Texto

Este ejemplo muestra otro uso del **Transformer completo encoder-decoder**. En lugar de traducir de un idioma a otro, la tarea consiste en:

* recibir una frase,
* y generar otra frase con el mismo significado, pero redactada de otra forma.

Es decir, una tarea de **reformulación** o **paráfrasis**.

---

## 1. ¿Por qué este ejemplo también usa el Transformer completo?

Porque la tarea sigue teniendo estructura:

* **entrada**: una secuencia,
* **salida**: otra secuencia diferente.

Aunque ambos textos estén en el mismo idioma, la lógica sigue siendo seq2seq:

* el encoder comprende la frase original,
* el decoder genera una nueva versión.

Por eso, igual que en traducción, aquí encaja bien el modelo encoder-decoder.

---

## 2. Archivos del ejemplo

Este ejemplo usa:

* Dataset de reformulación:
  `mini_reformulacion_es.tsv`

* Script:
  `ejemplo_transformers_3_reformulacion.py`

Aquí sí se reutiliza el Transformer original mediante:

```python
from transformerPytorch import Transformer
```

No se modifica el archivo original. Solo se usa su clase principal.

---

## 3. Tipo de dataset

El dataset contiene pares de frases en español:

```text
el coche es rojo    el automóvil es rojo
tengo hambre        necesito comer
estoy cansado       me encuentro cansado
```

Cada línea representa una pareja:

* frase original,
* frase reformulada.

---

## 4. Preparación de los datos

La preparación es muy parecida a la traducción:

* `src`: frase de entrada,
* `tgt_input`: frase de salida con `<sos>`,
* `tgt_output`: frase de salida desplazada con `<eos>`.

Ejemplo:

```text
src        = [tengo, hambre]
tgt_input  = [<sos>, necesito, comer]
tgt_output = [necesito, comer, <eos>]
```

El modelo aprende así a generar la reformulación palabra a palabra.

---

## 5. Papel del DataLoader

Como en el ejemplo de traducción, el `DataLoader`:

* agrupa muestras,
* aplica padding,
* y devuelve batches listos para entrenar.

La lógica es la misma que en un problema seq2seq clásico.

---

## 6. Qué enseña este ejemplo

Este ejemplo es importante porque muestra que el Transformer completo no solo sirve para traducir idiomas.

También sirve para tareas como:

* reformulación,
* paráfrasis,
* simplificación de texto,
* corrección gramatical,
* resumen.

Todas esas tareas comparten la misma idea:

* una secuencia entra,
* otra secuencia sale.

---

## 7. Diferencia con traducción

La arquitectura es la misma, pero cambia el tipo de relación entre entrada y salida.

### Traducción

* cambia el idioma,
* cambia el vocabulario,
* cambia la estructura lingüística.

### Reformulación

* el idioma es el mismo,
* el significado se conserva,
* cambia la forma de expresarlo.

Eso hace que este ejemplo sea conceptualmente muy útil: muestra que lo importante no es el idioma, sino la estructura **secuencia -> secuencia**.

---

## 8. Diferencia con decoder-only

Este ejemplo también sirve para contrastar con el ejemplo de generación libre.

### Reformulación

* encoder-decoder
* salida condicionada por una entrada concreta

### Generación libre

* decoder-only
* salida condicionada solo por el texto ya generado

Esto ayuda a entender mejor cuándo conviene cada arquitectura.

---

## 9. Limitaciones del ejemplo

Este ejemplo:

* usa un dataset pequeño,
* no pretende producir paráfrasis complejas,
* sirve sobre todo para comprender el flujo seq2seq.

Su valor didáctico está en que muestra otro uso del mismo Transformer completo, distinto de la traducción.

---

## 10. Idea final

Después de este ejemplo, el alumnado debería ver con claridad tres casos:

* **Transformers 10**: traducción con encoder-decoder,
* **Transformers 11**: generación libre con decoder-only,
* **Transformers 12**: reformulación con encoder-decoder.

Así se entiende mejor que la elección de arquitectura depende del tipo de tarea, no del nombre del modelo.

---
