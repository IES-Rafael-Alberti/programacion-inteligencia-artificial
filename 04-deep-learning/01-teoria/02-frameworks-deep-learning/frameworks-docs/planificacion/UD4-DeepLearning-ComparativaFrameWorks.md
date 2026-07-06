Perfecto. Cerramos la UD4 como debe ser, con **JAX** y **la comparación final**.

---

## ✅ Apéndice JAX — Notebook listo

Ya tienes el **apéndice en JAX**, alineado exactamente con lo visto en Keras y PyTorch:

📓 **Descargar notebook**
[UD4_Apendice_JAX_FashionMNIST.ipynb](sandbox:/mnt/data/UD4_Apendice_JAX_FashionMNIST.ipynb)

### Qué aporta este notebook (y por qué está bien así)

* Mismo problema: **clasificación binaria (zapato vs no-zapato)**
* Enfoque **funcional puro**
* Uso explícito de:

  * tensores
  * forward
  * función de pérdida
  * `jax.grad`
* Sin clases, sin magia
* Ideal para:

  * explicar *qué es backprop realmente*
  * enlazar con investigación y TPUs
  * justificar por qué JAX **no es para empezar**, pero sí para crecer

Esto encaja **perfecto como apéndice**, no como bloque central.

---

## 📘 Comparación final: Keras vs PyTorch vs JAX

Te dejo la comparación estructurada, para documento o diapositiva final.

---

### 🧠 Filosofía

| Framework   | Filosofía                                   |
| ----------- | ------------------------------------------- |
| **Keras**   | Alto nivel, declarativo, productividad      |
| **PyTorch** | Imperativo, control total, depuración fácil |
| **JAX**     | Funcional, matemático, compilable           |

---

### 📈 Curva de aprendizaje

| Framework   | Dificultad |
| ----------- | ---------- |
| **Keras**   | ⭐ Muy baja |
| **PyTorch** | ⭐⭐ Media   |
| **JAX**     | ⭐⭐⭐⭐ Alta  |

---

### 🔬 Investigación y modelos grandes

| Framework   | Adecuación                   |
| ----------- | ---------------------------- |
| **Keras**   | Media                        |
| **PyTorch** | Alta                         |
| **JAX**     | ⭐ Muy alta (TPUs, multi-GPU) |

---

### 🏭 Producción y despliegue

| Framework   | Producción                       |
| ----------- | -------------------------------- |
| **Keras**   | Muy buena (TensorFlow ecosystem) |
| **PyTorch** | Muy buena (TorchServe, ONNX)     |
| **JAX**     | Más compleja                     |

---

### 🧑‍🎓 Para tu módulo PIA

| Objetivo docente          | Recomendado        |
| ------------------------- | ------------------ |
| Entender redes neuronales | **Keras primero**  |
| Saber “qué está pasando”  | **PyTorch**        |
| Investigación / HPC       | **JAX (apéndice)** |

---

### 📌 Mensaje clave para el alumnado

> **No hay un “mejor framework” universal.**
> Hay herramientas adecuadas según:
>
> * el problema
> * los recursos
> * el objetivo (aprender, investigar, producir)

---

## 🔚 Estado de la UD4

✔ Fundamentos matemáticos
✔ Visualización
✔ Keras (binario + multiclase)
✔ PyTorch (binario + multiclase)
✔ JAX (apéndice)
✔ Comparativa clara y honesta
