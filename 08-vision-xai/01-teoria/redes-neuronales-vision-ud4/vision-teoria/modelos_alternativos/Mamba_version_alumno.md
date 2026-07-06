# UD4 · Mamba: Selective State Space Models
##  Guía de estudio

---

## 🎯 Objetivo de esta sesión

Al terminar deberías poder explicar:

1. **Qué es** un State Space Model (SSM)
2. **Cómo** Mamba selecciona qué recordar
3. **Por qué** escala linealmente
4. **Cuándo** usar cada arquitectura

---

## 📖 1. El problema de base

Los **Transformers** usan atención global:
- Cada token puede mirar a todos los demás
- Complejidad: **O(n²)** donde n es la longitud de secuencia
- Para secuencias largas, esto es muy caro

**Pregunta**: Si tienes 2048 tokens, ¿cuántas operaciones hace la atención?

---

## 🔍 2. State Space Models: la alternativa

Un SSM tiene una **memoria de tamaño fijo** (el estado) que se actualiza con cada input.

### La idea básica

```
Imagina que tu cerebro tiene solo 16 "cajones" de memoria.
Cuando lees un texto, decides qué guardar en cada cajón.
El contenido de los cajones = el "estado".
```

### Las ecuaciones

```
h_t = A·h_{t-1} + B·u_t    ← Cómo cambia el estado
y_t = C·h_t + D·u_t         ← Cómo sale el resultado
```

Donde:
- **h** = el estado (memoria)
- **u** = el input actual
- **y** = la salida
- **A, B, C, D** = parámetros aprendibles

---

## 🐍 3. La innovación de Mamba

### SSM tradicional vs Mamba

| Aspecto | SSM tradicional | Mamba |
|---------|----------------|-------|
| A, B, C | Fijos | Dependen del input |
| Memoria | Una memoria para todo | Selección dinámica |
| Expresividad | Limitada | Alta |

### ¿Qué significa "input-dependent"?

En Mamba, todo cambia según el contenido:

```
B_t = Linear(x_t)    ← Qué del input va al estado
C_t = Linear(x_t)    ← Qué del estado sale
dt_t = softplus(x_t) ← Cuánto tiempo recordar
```

**Resultado**: El modelo puede "decidir" qué olvidar y qué recordar.

---

## 🔢 4. El parámetro dt (delta)

**dt** controla el "tiempo de retención":

- dt grande → el input influye mucho en el estado
- dt pequeño → el input se "olvida" rápido

Piensa en dt como un **dimmer** (regulador de luz):
- Brillante (dt alto) = información muy presente
- Oscuro (dt bajo) = información desvanecida

---

## 📊 5. Complejidad comparada

| Método | Complejidad | Para n=128 | Para n=2048 |
|--------|-------------|------------|------------|
| Atención | O(n²) | 16K ops | 4M ops |
| Mamba | O(n × d_state) | 2K ops | 33K ops |
| **Speedup** | - | **8x** | **128x** |

---

## 🧩 6. Arquitectura de un MambaBlock

```
Entrada x
    ↓
Proyección x → (x_inner, z)
    ↓
Convolución local (kernel=4)
    ↓
Proyección x_inner → (B, C, dt)
    ↓
SSM Scan:
  for t in seq:
    h_t = dt[t] * (A @ h_{t-1} + B[t] @ x[t])
    y_t = C[t] @ h_t
    ↓
y = y * sigmoid(z)  ← Gate
y = y + x * sigmoid(D)  ← Skip connection
    ↓
Proyección de salida
    ↓
Salida
```

---

## 📝 7. Los tres modelos

### MiniTransformer
- Solo atención (6 capas)
- Complejo: O(n²)
- Calidad: Alta

### MiniMamba
- Solo SSM (12 capas)
- Eficiente: O(n)
- Capacidad: Variable

### HybridMamba
- Atención cada 3 capas
- Balance: Calidad + eficiencia

---

## ❓ 8. Preguntas de autoevaluación

### Básico
1. ¿Qué es un State Space Model?
2. ¿Qué hace el parámetro dt?
3. ¿Por qué Mamba escala mejor que Transformer?

### Intermedio
4. Si sequences tiene 1000 tokens y d_state=16, ¿cuántas operaciones hace Mamba?
5. ¿Por qué inicializamos A como negativo?
6. ¿Qué hace el gate z?

### Avanzado
7. ¿Qué limitaciones tiene la recurrencia de Mamba?
8. ¿En qué casos prefirieses Transformer sobre Mamba?

---

## 🧪 9. Experimentos sugeridos

Después de ejecutar el notebook:

1. **d_state**: Prueba con 8, 16, 32. ¿Cambia la calidad?
2. **Temperatura**: Compara 0.5 vs 1.2
3. **Híbrido**: ¿Y si la atención fuera cada 5 capas?

---

## 📚 10. Glosario

| Término | Significado |
|---------|-------------|
| **Estado (h)** | Memoria comprimida de la secuencia |
| **d_state** | Tamaño del estado (16 por defecto) |
| **dt** | Tiempo de retención de cada input |
| **Selección** | Parámetros que dependen del input |
| **SSM Scan** | Proceso recursivo de actualizar el estado |
| **A_log** | Parámetro de transición del estado (negativo) |

---

## 💡 11. Frase clave

> **"Mamba no es 'sin atención'. Es atención lineal: aprende a seleccionar qué recordar, cómo recordarlo, y cuándo olvidarlo."**

---

## 🔗 Recursos

- Paper: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" (Gu & Dao, 2023)
- Prueba con código: ¡experimenta con los parámetros!

---

*Material basado en el notebook de clase con Don Quijote.*
