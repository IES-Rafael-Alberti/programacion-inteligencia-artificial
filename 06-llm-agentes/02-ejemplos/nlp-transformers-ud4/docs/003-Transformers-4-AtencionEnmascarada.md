---
title: "Transformers 4: Atención Enmascarada en el Decoder"
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


# Atención Enmascarada (Masked Self-Attention) en el Decoder

## 🔐 Introducción

En tareas de generación de texto como traducción, autocompletado o creación de secuencias, el modelo Transformer debe producir una salida **palabra por palabra**, sin acceder a información futura. Para lograr esto, se utiliza una técnica conocida como **atención enmascarada** (*masked self-attention*).

---

## 🤖 ¿Por qué es necesaria?

En el bloque de **decodificador (decoder)** del Transformer, cada palabra generada se basa en las anteriores. Por ejemplo:

```
Entrada: "El gato"
Salida esperada: "is sleeping"
```

Cuando el modelo está generando la palabra "sleeping", **no debe ver que la próxima palabra es "soundly"** (ni ninguna posterior). Si pudiera acceder a esa información, estaría haciendo trampa.

---

## 🔒 Mecanismo de la Máscara

Durante el cálculo de los **pesos de atención**, el modelo genera una matriz de puntuaciones (scores) entre cada par de posiciones en la secuencia. Para evitar que el modelo "vea el futuro", se aplica una **máscara triangular inferior**:

### ✉️ Ejemplo: secuencia de 4 posiciones

|    | t1 | t2 | t3 | t4 |
| -- | -- | -- | -- | -- |
| t1 | 1  | 0  | 0  | 0  |
| t2 | 1  | 1  | 0  | 0  |
| t3 | 1  | 1  | 1  | 0  |
| t4 | 1  | 1  | 1  | 1  |

Los ceros representan posiciones **bloqueadas**. Esto impide que, por ejemplo, la tercera palabra vea la cuarta.

Se implementa usando una matriz booleana o multiplicando los scores por `-inf` antes del softmax.

---

## 📊 Ejemplo en Código (NumPy)

```python
import numpy as np
import matplotlib.pyplot as plt

seq_len = 5
mask = np.triu(np.ones((seq_len, seq_len)), k=1) * -1e9

plt.figure(figsize=(5, 4))
plt.imshow(mask, cmap="gray")
plt.title("Máscara triangular (evita ver el futuro)")
plt.xlabel("Key")
plt.ylabel("Query")
plt.colorbar(label="Valor de Score")
plt.show()
```

---

## 🔄 Aplicación dentro del Transformer

La máscara se aplica **solo en el bloque de self-attention del decoder**. No se aplica:

* En el encoder (toda la entrada ya está disponible).
* En la atención encoder-decoder (la salida puede mirar libremente la entrada).

---

## 🔹 Resumen

* El modelo genera texto paso a paso.
* Para que no "mire hacia adelante", se enmascaran las posiciones futuras.
* Esto se logra aplicando una máscara triangular a los scores antes del softmax.
* Es fundamental para tareas de generación autoregresiva (como GPT o traducción secuencia-a-secuencia).

---

## 🔁 Reexplicación Intuitiva

En esta sección se retoma la misma idea con una redacción más intuitiva y un ejemplo alternativo, para reforzar el concepto.

El modelo **Transformer**, cuando se usa en tareas de generación de texto, debe producir cada palabra sin conocer las siguientes, porque en un escenario real, la salida aún no ha sido escrita. Para evitar que el modelo "haga trampa" y mire palabras futuras, se usa la técnica de **atención enmascarada** (*masked self-attention*).

### **¿Por qué no puede ver información futura?**
1. **Proceso de generación palabra por palabra**  
   - En traducción automática, autocompletado o generación de texto, el modelo no tiene acceso a palabras futuras porque estas aún no existen. Solo puede basarse en las palabras ya generadas.
   
2. **Máscara aplicada sobre la matriz de atención**  
   - En el mecanismo de **autoatención**, cada palabra en la secuencia compara su relevancia con todas las demás.
   - Si no se aplicara una restricción, el modelo podría mirar toda la oración, incluyendo partes que aún no ha generado.
   - Para evitar esto, se usa una **máscara** (una matriz que bloquea ciertas posiciones) que impide que un token vea palabras que aparecen después de él.

### **¿Cómo funciona la atención enmascarada?**
- Cuando el modelo procesa una oración, genera una matriz de atención.
- En esta matriz, las posiciones correspondientes a palabras futuras se rellenan con **valores negativos extremos** (como -∞) antes de aplicar la función *softmax*.
- Esto fuerza a *softmax* a asignar una probabilidad cercana a **cero** a las palabras futuras, bloqueando su influencia en la generación actual.

### **Ejemplo práctico**
Si la frase que se quiere generar es:  
✅ *"Me gusta la música clásica"*, el modelo primero generará **"Me"**, después **"Me gusta"**, luego **"Me gusta la"**, y así sucesivamente.  
Sin la máscara, cuando el modelo intenta predecir **"la"**, podría mirar directamente el siguiente token **"música"** y hacer una elección errónea basada en información futura.  

Gracias a la **atención enmascarada**, el modelo solo ve la información que tiene hasta ese punto, garantizando coherencia en la generación paso a paso.

Aquí tienes un código ilustrativo que muestra cómo aplicar **atención enmascarada** en un Transformer para evitar que el modelo vea información futura durante la generación de texto:

```python
import torch
import torch.nn.functional as F

# Simulación de una matriz de puntuaciones de atención (antes de aplicar Softmax)
attention_scores = torch.tensor([
    [0.8, 0.9, 1.0, 1.2],
    [0.7, 0.8, 0.9, 1.0],
    [0.6, 0.7, 0.8, 0.9],
    [0.5, 0.6, 0.7, 0.8]
], dtype=torch.float32)

# Crear una máscara de atención triangular superior
mask = torch.triu(torch.ones_like(attention_scores), diagonal=1) * float('-inf')

# Aplicar la máscara antes de Softmax
masked_attention_scores = attention_scores + mask

# Aplicar la función Softmax para obtener las probabilidades de atención
attention_weights = F.softmax(masked_attention_scores, dim=-1)

# Mostrar los resultados
print("Matriz de atención antes de la máscara:")
print(attention_scores)

print("\nMáscara aplicada:")
print(mask)

print("\nMatriz de atención después de la máscara:")
print(masked_attention_scores)

print("\nPesos de atención finales tras aplicar Softmax:")
print(attention_weights)
```

### **Explicación:**
1. Se genera una **matriz de puntuaciones de atención**, que representa qué tan relevante es cada palabra para cada otra palabra en la secuencia.
2. Se crea una **máscara triangular superior**, que bloquea la información de palabras futuras (las posiciones superiores se llenan con `-inf`).
3. Se suma la máscara a la matriz de atención, eliminando la influencia de tokens futuros.
4. Se aplica la función **Softmax** para obtener los pesos de atención, asegurando que el modelo solo considere palabras previas.

Este código simula cómo el modelo Transformer impide que los tokens vean información futura en tareas como traducción y generación de texto.
