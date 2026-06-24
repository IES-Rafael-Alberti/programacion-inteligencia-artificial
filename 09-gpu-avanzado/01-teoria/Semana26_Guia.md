# Semana 26 – RAPIDS y JAX para acelerar en GPU

## 🎯 Objetivos
- Explorar librerías modernas que aprovechan **GPU** para acelerar cálculos.  
- Familiarizarse con el ecosistema **RAPIDS** (cuDF, cuML).  
- Introducir **JAX** como alternativa de arrays y autodiferenciación.  
- Comparar tiempos de ejecución frente a NumPy en CPU.  

---

## 📚 Contenidos principales

### 1. RAPIDS (cuDF, cuML)
- Ecosistema de NVIDIA para ciencia de datos en GPU.  
- **cuDF**: DataFrames acelerados con sintaxis casi idéntica a Pandas.  
- **cuML**: algoritmos de Machine Learning optimizados para GPU.  
- Ideal para conjuntos de datos grandes y flujos productivos en GPU.  

### 2. JAX
- Desarrollado por Google.  
- Arrays con sintaxis estilo NumPy, pero ejecutados en **CPU/GPU/TPU**.  
- **Autodiferenciación automática** (`jax.grad`).  
- **Compilación just-in-time** (`jax.jit`).  
- Orientado a investigación y deep learning de alto rendimiento.  

### 3. Comparación práctica
- Benchmarks simples de multiplicación de matrices.  
- Entrenamiento básico de un modelo de regresión logística con cuML.  
- Cálculo de gradientes y funciones con JAX.  

---

## 📂 Notebooks trabajados
- **90_rapids_intro.ipynb** → Introducción a RAPIDS (cuDF y cuML).  
- **91_jax_intro.ipynb** → Arrays y diferenciación automática con JAX.  
- **92_gpu_benchmarks.ipynb** → Comparación de rendimiento entre NumPy, RAPIDS y JAX.  

Versiones disponibles:  
- Base.  
- Soluciones.  
- Soluciones + Autotests.  

---

## 🛠️ Actividades prácticas
1. Crear un DataFrame en cuDF y calcular medias y sumas.  
2. Entrenar un modelo de regresión logística en cuML y compararlo con scikit-learn en CPU.  
3. Usar JAX para derivar funciones matemáticas y comprobar resultados.  
4. Medir tiempos de ejecución de multiplicación de matrices con NumPy y JAX.  
5. Reflexionar sobre ventajas e inconvenientes de GPU vs CPU.  

---

## ✅ Evaluación (RA2)
- **RA2.b**: Identificación y caracterización de nuevas librerías de IA.  
- **RA2.d**: Implementación de ejemplos con GPU.  
- **RA2.e**: Evaluación comparativa de rendimiento CPU vs GPU.  

**Criterios de evaluación:**  
- Comprensión del papel de RAPIDS y JAX en IA.  
- Ejecución correcta de notebooks y benchmarks.  
- Análisis crítico de resultados y reflexión escrita.  

---

## 📌 Recursos recomendados
- [RAPIDS AI](https://rapids.ai/)  
- [Documentación de cuDF](https://docs.rapids.ai/api/cudf/stable/)  
- [Documentación de cuML](https://docs.rapids.ai/api/cuml/stable/)  
- [Documentación de JAX](https://jax.readthedocs.io/)  
- [Tutoriales de JAX](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html)  
