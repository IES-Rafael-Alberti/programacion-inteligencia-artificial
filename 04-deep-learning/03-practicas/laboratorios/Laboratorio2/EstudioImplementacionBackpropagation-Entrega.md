# 📄 Entrega — Laboratorio 2

## Análisis de Implementación de Backpropagation

### UD4 — Fundamentos de Deep Learning

---

## 👤 Datos del alumno/a

* Nombre:
* Grupo:
* Fecha:
* Versión analizada:

  * ☐ Implementación orientada a objetos
  * ☐ Implementación funcional
  * ☐ Ambas

---

# 1️⃣ Objetivo del laboratorio

Este laboratorio tiene como objetivo:

* Analizar una implementación real de backpropagation.
* Identificar las partes fundamentales del algoritmo.
* Relacionar el código con los conceptos teóricos estudiados.
* Comprender cómo se calculan y aplican los gradientes.

---

# 2️⃣ Identificación estructural del código

## 2.1 Forward Pass

Indica:

* ¿Dónde se calcula la salida de la red?
* ¿Qué funciones intervienen?
* ¿Cómo se almacenan los valores intermedios?

Explicación:

---

## 2.2 Cálculo de la pérdida

* ¿Dónde se define la función de pérdida?
* ¿Qué tipo de pérdida se utiliza?
* ¿Cómo se calcula el error respecto al valor real?

Explicación:

---

## 2.3 Backward Pass

Identifica:

* ¿Dónde comienza el proceso de retropropagación?
* ¿Cómo se calculan los gradientes?
* ¿Se aplica explícitamente la regla de la cadena?

Describe el flujo hacia atrás:

---

## 2.4 Actualización de pesos

* ¿Dónde se actualizan los parámetros?
* ¿Qué fórmula se utiliza?
* ¿Existe tasa de aprendizaje configurable?

Explicación:

---

# 3️⃣ Relación entre código y teoría

Completa la siguiente tabla:

| Concepto teórico       | Fragmento de código | Explicación |
| ---------------------- | ------------------- | ----------- |
| Forward pass           |                     |             |
| Función de pérdida     |                     |             |
| Gradiente              |                     |             |
| Regla de la cadena     |                     |             |
| Actualización de pesos |                     |             |

---

# 4️⃣ Análisis comparativo (si se analizan ambas versiones)

Si has analizado ambas implementaciones:

* ¿Cuál es más clara estructuralmente?
* ¿Cuál facilita mejor la comprensión del algoritmo?
* ¿Cuál sería más escalable a redes más profundas?
* ¿Qué diferencias observas en organización del código?

Conclusión comparativa:

---

# 5️⃣ Análisis conceptual

Responde de forma argumentada:

1. ¿Backpropagation es el algoritmo de aprendizaje? Justifica.
2. ¿Qué papel juega la función de activación en el cálculo de gradientes?
3. ¿Qué ocurriría si la derivada de la activación fuese cero?
4. ¿Qué relación tiene el código analizado con lo que hace internamente PyTorch o TensorFlow?
5. ¿Qué limitaciones tendría esta implementación para redes profundas?

---

# 6️⃣ Reflexión final

Explica con tus palabras:

> ¿Cómo calcula realmente una red neuronal qué pesos debe modificar?

---

# 7️⃣ Resultados de Aprendizaje implicados

Este laboratorio contribuye a la evaluación de:

### RA1

* Comprende los fundamentos matemáticos del aprendizaje automático.
* Interpreta el cálculo de gradientes.

### RA2

* Analiza implementaciones de modelos.
* Relaciona teoría y práctica.
* Identifica componentes de un algoritmo de IA.

---

# 8️⃣ Autoevaluación

Valora del 1 al 5 tu nivel de comprensión:

* Entiendo cómo funciona el forward pass:
* Entiendo cómo se calcula el gradiente:
* Entiendo cómo se aplica la regla de la cadena:
* Entiendo cómo se actualizan los pesos:

---
