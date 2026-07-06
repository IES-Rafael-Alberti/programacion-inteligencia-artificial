# UD4 · RWKV: Receptance Weighted Key Values
## Versión alumno · Guía de estudio

---

## 🎯 Objetivo de esta sesión

Al terminar deberías poder:

1. **Explicar** qué es RWKV y cómo combina Transformer + RNN
2. **Entender** los componentes: R, K, V, W (decay)
3. **Comparar** eficiencia de inferencia entre arquitecturas
4. **Decidir** cuándo usar RWKV vs otras opciones

---

## 📖 1. El problema que resuelve

### Los dos mundos

```
TRANSFORMER          vs           RNN
──────────────────────────────────────────
Paralelo ✓           →          Secuencial ✗
Inferencia O(n)      →          Inferencia O(1) ✓
Memoria O(n²)        →          Memoria O(1) ✓
```

**RWKV = Lo mejor de ambos mundos**

---

## 🔑 2. La idea clave

RWKV usa **atención lineal** que puede reescribirse como **recurrencia**.

```
Atención estándar:
Attn = softmax(Q·K^T)·V  → O(n²)

RWKV:
RWKV_t = Σ(w^{t-i} · r_i · k_i) · v_i
       → Reescrito como:
state_t = state_{t-1} · decay + r_t · k_t · v_t
       → O(1) por token
```

---

## 📝 3. Los componentes

| Letra | Nombre | Significado |
|-------|--------|-------------|
| **R** | Receptance | Cuánto "acepta" el token actual |
| **K** | Key | La "clave" para matching |
| **V** | Value | El "valor" a propagar |
| **W** | Weight | Decay temporal (olvido) |

### El decay

```
Decay grande (w ≈ 1) → mantengo más información del pasado
Decay pequeño (w ≈ 0) → olvido más rápido
```

---

## 🔄 4. Time Shift

Antes de procesar, RWKV "desliza" el input:

```
Input original:  [x_1, x_2, x_3, x_4, x_5]
Con shift:      [x_0, x_1, x_2, x_3, x_4]
```

**Ventaja**: Cada posición "ve" la anterior sin recurrencia explícita.

---

## 📊 5. Comparativa de eficiencia

| Aspecto | Transformer | Mamba | RWKV |
|---------|-------------|-------|------|
| Entrenamiento | Paralelo ✓ | Parcial | **Paralelo ✓** |
| Inferencia | O(n) | O(n) | **O(1)** ✓ |
| Memoria | O(n²) | O(n·d) | O(n) |
| Estado | No | Sí | Sí |

### ¿Por qué importa O(1)?

```
Generando 1000 tokens:
- Transformer: 1 + 2 + 3 + ... + 1000 = 500K ops
- Mamba: 1000 × d_state ≈ 16K ops
- RWKV: 1000 × 1 ≈ 1K ops
```

---

## 🏗️ 6. Arquitectura de un bloque RWKV

```
Input
    ↓
Time Shift
    ↓
┌──────────────────────┐
│ TIME MIXING          │
│ r = sigmoid(Rx)      │
│ k = Kx                │
│ v = Vx                │
│ state = state*w + k*v│
│ o = r * O(state)      │
└──────────────────────┘
    ↓ + x
RMSNorm
    ↓
┌──────────────────────┐
│ CHANNEL MIXING        │
│ r = sigmoid(Rx)       │
│ k = relu(Kx)²         │
│ o = r * V(k)          │
└──────────────────────┘
    ↓ + x
Output
```

---

## ❓ 7. Preguntas de autoevaluación

### Básico
1. ¿Qué significa RWKV?
2. ¿Por qué RWKV puede entrenar en paralelo?
3. ¿Qué significa inferencia O(1)?

### Intermedio
4. ¿Qué hace el `time_decay`?
5. ¿Por qué `sigmoid` en receptance?
6. ¿Cuándo preferirías RWKV sobre Transformer?

### Avanzado
7. ¿Qué limitaciones tiene el mecanismo de decay?
8. ¿Cómo compararía RWKV con Mamba para agentes con memoria?

---

## 🧪 8. Experimentos sugeridos

1. **Decay**: Cambia el decay y observa el efecto
2. **Longitud**: Genera secuencias muy largas y compara
3. **Híbrido**: ¿RWKV + Atención?

---

## 📚 9. Glosario

| Término | Significado |
|---------|-------------|
| **Receptance** | Puerta de entrada (0-1) |
| **Time Shift** | Deslizar input para dar contexto |
| **Decay** | Cuánto "olvida" el modelo |
| **State** | Memoria comprimida del contexto |

---

## 💡 10. Frase clave

> **"RWKV: entrena como transformer, infiere como RNN."**

---

## 🔗 Recursos

- Paper: "RWKV: Reinventing RNNs for the Transformer Era"
- Repo: github.com/BlinkDL/RWKV-LM

---

*Material basado en el notebook de clase con Don Quijote.*
