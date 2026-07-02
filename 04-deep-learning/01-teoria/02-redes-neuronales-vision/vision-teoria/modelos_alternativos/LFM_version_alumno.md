# UD4 · Liquid Foundation Models
## Versión alumno · Guía de estudio

---

## 🎯 Objetivo de esta sesión

Al terminar deberías poder explicar:

1. **Qué son** los Liquid Foundation Models y por qué se llaman "líquidos"
2. **Qué problema intentan resolver** los LFMs vs Transformers
3. **Qué papel tienen** las convoluciones locales sobre texto
4. **Qué hace un gate** y por qué se usa
5. **Por qué un modelo híbrido** puede ser una buena solución

---

## 📖 1. Introducción: ¿Qué son los Liquid Foundation Models?

Los **Liquid Foundation Models (LFMs)** son una nueva generación de modelos de IA desarrollados por **Liquid AI**, una empresa derivada del MIT (Massachusetts Institute of Technology).

### La idea central

A diferencia de los Transformers (GPT, Llama, Gemini), los LFMs se construyen desde **principios fundamentales** ("from first principles") usando:

- Teoría de **sistemas dinámicos**
- Procesamiento de señales
- Álgebra lineal numérica
- Inspiración biológica (redes neuronales líquidas del MIT)

### ¿Por qué "líquidos"?

El término "liquid" (líquido) hace referencia a su naturaleza **dinámica y adaptable**:
- Permiten un flujo más fluido de información
- Mayor capacidad de adaptación en tiempo real
- Eficiencia computacional superior

> **Analogía**: Si un Transformer es como una tubería rígida donde el agua fluye en una dirección fija, un LFM es como un fluido que se adapta y fluye según el terreno.

---

## 🏢 2. ¿Qué problema resuelven los Transformers?

Un Transformer usa **atención global**: cada token puede "mirar" a todos los demás tokens de la secuencia.

### Ventajas de los Transformers:
- Captura dependencias a cualquier distancia
- Muy potente para muchas tareas
- Revolucionó el NLP moderno

### Problemas:
- Coste computacional O(n²) donde n es la longitud de la secuencia
- En secuencias largas, el coste crece muy rápido
- Mucha memoria (KV cache grande)
- Alto consumo energético

**Pregunta para pensar:**
> Si tienes una secuencia de 1000 tokens, ¿cuántas comparaciones hace la atención?

| Longitud | Operaciones de atención |
|----------|------------------------|
| 128      | 16.384                |
| 512      | 262.144               |
| 2048     | 4.194.304             |

---

## 🔧 3. La solución de los LFMs: Arquitectura híbrida

Los LFMs proponen una **arquitectura híbrida** que combina:

| Componente | Descripción | Frecuencia |
|------------|-------------|------------|
| **Gated Short Convolution** | Convolución local con gating | ~70-80% del total |
| **Grouped Query Attention (GQA)** | Atención agrupada | ~20-30% del total |

### ¿Por qué funciona?

> "Usa operaciones baratas donde puedas, y reserva la atención cara para donde realmente importa."

---

## 🧩 4. Los bloques fundamentales

### 4.1 AttentionBlock (igual que en Transformer)

```
Input (batch, seq_len, d_model)
    ↓
MultiheadAttention (self-attention)  ← Mira TODA la secuencia
    ↓
LayerNorm + Residual
    ↓
Feed-Forward (FFN)
    ↓
Salida (batch, seq_len, d_model)
```

Cada capa de atención permite que cualquier posición "mire" a todas las demás.

### 4.2 LiquidBlock (el bloque central del LFM)

```
Input (batch, seq_len, d_model)
    ↓
LayerNorm
    ↓
Gate1 × Proyección  ← Primera puerta (decide qué entra)
    ↓
Conv1D (ventana local, ej: 5 caracteres)  ← Solo mira ±2 posiciones
    ↓
Gate2  ← Segunda puerta (decide qué sale)
    ↓
Proyección + Residual
    ↓
LayerNorm + Feed-Forward
    ↓
Salida
```

**Los gates** son "puertas numéricas" con valores entre 0 y 1:
- Cerca de 0 → bloquea la información
- Cerca de 1 → deja pasar la información
- Entre medias → atenúa

---

## 🔢 5. ¿Por qué Conv1D sobre texto?

Piensa en la secuencia de texto como una línea temporal:

```
Posición:   0    1    2    3    4    5    6    7    8    9
Caracteres: E    n    _    u    n    _    l    u    g    a    r
```

**Con kernel_size = 5:**
- Para calcular algo en la posición 5, el modelo mira: 3, 4, 5, 6, 7
- Solo ve los 5 caracteres más cercanos

**Complejidad:**

| Método | Operaciones (n=128) |
|--------|---------------------|
| Atención | 128 × 128 = 16.384 |
| Conv1D (k=5) | 128 × 5 = 640 |

¡25 veces menos operaciones!

### ¿Qué es "short" en "short convolution"?

"Short" se refiere al **kernel** o filtro pequeño: 3, 5 o 7 posiciones.  
No es el tamaño del modelo ni el número de neuronas.

---

## 📊 6. Las tres arquitecturas que comparamos

### MiniTransformer
- Solo capas de atención
- Todas las capas pueden mirar a toda la secuencia
- Referencia de **calidad**
- Coste: O(n²) en todas las capas

### MiniLiquid
- Solo bloques Liquid
- Solo mira contexto local (ventana de 5 por defecto)
- Referencia de **eficiencia**
- Coste: O(n) en todas las capas

### HybridLiquid (como los LFMs reales)
- Cada 3 capas: 1 atención + 2 Liquid
- Combina ambos enfoques
- **Equilibrio** entre calidad y eficiencia

---

## 🌟 7. Características clave de los LFMs

### Eficiencia extrema
- Rendimiento comparable o superior a Transformers de tamaño similar
- Menor huella de memoria (RAM)
- Inferencia más rápida (especialmente en CPUs y dispositivos edge)
- Consumo energético mucho más bajo

### Multimodalidad nativa
Pueden procesar y generar datos de cualquier tipo:
- Texto
- Imágenes
- Audio
- Video
- Series temporales
- Señales

### Optimizados para dispositivos edge
- Funcionan muy bien en teléfonos, laptops, wearables, IoT
- Baja latencia (milisegundos)
- Privacidad de datos (sin enviar a la nube)
- Resiliencia sin conexión

### Tamaños disponibles
- **Nanos**: 350M-2.6B parámetros
- **Medium**: 1-8B parámetros
- **Large**: hasta ~40B parámetros

---

## 🔬 8. Analogía con redes neuronales líquidas

Los LFMs se inspiran en las **Liquid Neural Networks (LNN)** del MIT:

- Estudian sistemas nerviosos simples (como los de gusanos nematodos)
- Crean redes que cambian su comportamiento según el input
- El "estado" evoluciona dinámicamente

**Diferencia clave**: Las LNN originales usaban ecuaciones diferenciales; los LFMs implementan una versión eficiente usando convoluciones gated.

---

## 🎚️ 9. La temperatura en generación

Cuando generamos texto, usamos la **temperatura** para controlar la aleatoriedad:

| Temperatura | Efecto |
|-------------|--------|
| 0.5 | Muy determinista, texto repetitivo |
| **0.8** | **Equilibrado (recomendado)** |
| 1.2 | Creativo, pero puede ser incoherente |

---

## 🧮 10. Complejidad computacional comparada

| Aspecto | Transformer | LFM (Híbrido) |
|---------|-------------|---------------|
| Coste por bloque atención | O(n²) | O(n²) |
| Coste por bloque liquid | O(n²) (si es attention) | O(n) |
| Memoria KV cache | Grande | Mucho menor |
| Profundidad típica (1-8B) | 24-48 capas | 16-32 bloques |
| Eficiencia en CPU | Baja | Alta |
| Latencia en secuencia larga | Alta | Muy baja |

---

## 📈 11. Comparación de rendimiento

Los LFMs destacan en benchmarks:
- Excelente balance performance/tamaño
- Superan a Llama 3.2, Qwen, Gemma en categorías de 1B-3B
- Tareas de razonamiento, instruction following, multimodalidad

---

## ❓ 12. Preguntas de autoevaluación

### Básico
1. ¿Qué diferencia hay entre atención global y convolución local?
2. ¿Qué hace un gate en términos simples?
3. ¿Por qué el híbrido intercala atención y liquid?
4. ¿Por qué se llaman "líquidos" estos modelos?

### Intermedio
5. Si sequences es 512, ¿cuántas operaciones hace la atención?
6. ¿Qué esperas que ocurra si pones `kernel_size=1`? ¿Y `kernel_size=31`?
7. ¿Por qué el Liquid necesita más capas que el Transformer?
8. ¿Qué es una "depthwise convolution"?

### Avanzado
9. ¿Qué limitaciones tiene el enfoque líquido puro?
10. ¿En qué tipo de tareas crees que el híbrido funcionaría mejor? ¿Y peor?
11. ¿Cómo se relaciona el LFM con las Liquid Neural Networks del MIT?
12. ¿Por qué los LFMs son buenos para dispositivos edge?

---

## 🧪 13. Experimentos sugeridos

Después de ejecutar el notebook, prueba:

1. **Cambia la temperatura** a 0.5, 0.8, 1.0, 1.2 y compara resultados
2. **Modifica kernel_size** entre 3 y 9, observa el efecto
3. **Reduce epochs** a 3 para ver convergencia rápida
4. **Compara tiempos** de entrenamiento entre modelos
5. **Cambia la proporción** de atención en el híbrido (cada 2, cada 4 capas)

---

## 📝 14. Glosario completo

| Término | Significado |
|---------|-------------|
| **Embedding** | Representación vectorial de cada token |
| **d_model** | Dimensión de los vectores internos |
| **kernel_size** | Tamaño de la ventana de la convolución |
| **gate** | Mecanismo que filtra información (0-1) |
| **residual** | Conexión que suma la entrada original |
| **LayerNorm** | Normalización para estabilizar |
| **temperature** | Controla aleatoriedad en generación |
| **Conv1D** | Convolución unidimensional sobre secuencias |
| **Depthwise** | Cada canal se procesa independientemente |
| **GQA** | Grouped Query Attention (atención agrupada) |
| **FFN** | Feed-Forward Network (red feed-forward) |
| **RoPE** | Rotary Positional Embedding (codificación posicional) |
| **RMSNorm** | Normalización más eficiente que LayerNorm |
| **SwiGLU** | Activación gated usada en LFMs |
| **Edge computing** | Computación en dispositivos locales (no en nube) |

---

## 💡 15. Frases clave para recordar

> **"Los Transformers nos enseñaron que atender globalmente funciona muy bien. Los LFMs nos recuerdan que no siempre hace falta pagar ese coste en todas las capas."**

> **"Un LFM es como un fluido: fluye y se adapta dinámicamente según el input, en lugar de procesar todo con la misma operación rígida."**

---

## 🔗 16. Uso práctico de LFMs

### ¿Cómo usar modelos LFM reales?

Los LFMs están disponibles en:
- **Hugging Face** (bajo LiquidAI)
- **Ollama** (formato GGUF)
- Compatible con Continue.dev, VS Code, IDEs de JetBrains

### Modelos populares:
- LFM2-1.2B
- LFM2.5-1.2B-Thinking
- LFM-VL (multimodal)

---

## 📚 Recursos adicionales

Si quieres profundizar:

1. **Paper técnico de LFM2** (arXiv:2511.23404)
2. **Repositorio de Liquid AI** en Hugging Face
3. Experimenta con el código: ¡cambia parámetros y observa!
4. Busca información sobre "State Space Models" (otro enfoque similar)
5. Lee sobre "Liquid Neural Networks" del MIT

---

*Material basado en el notebook de clase con Don Quijote de Cervantes.*
