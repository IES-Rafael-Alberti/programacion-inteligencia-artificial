# UD4 · Arquitecturas de Modelización Secuencial
## Guía Comparativa: Transformers, Liquid Models, Mamba/SSM y más

---

## 📋 Índice

1. [Introducción](#1-introducción)
2. [Comparativa General](#2-comparativa-general)
3. [Transformers](#3-transformers)
4. [Liquid Foundation Models](#4-liquid-foundation-models-lfm)
5. [Mamba / Selective SSM](#5-mamba--selective-ssm)
6. [Otras Arquitecturas Relevantes](#6-otras-arquitecturas-relevantes)
7. [Tabla Comparativa Completa](#7-tabla-comparativa-completa)
8. [Cuándo Usar Cada Arquitectura](#8-cuándo-usar-cada-arquitectura)
9. [Evolución Histórica](#9-evolución-histórica)
10. [Recursos](#10-recursos)

---

## 1. Introducción

La modelización de secuencias es una tarea fundamental en IA:

- **NLP**: traducción, generación de texto, resumen
- **Audio**: reconocimiento de voz, síntesis, música
- **Video**: predicción de frames, acción recognition
- **Time series**: forecasting, anomaly detection
- **Genómica**: análisis de secuencias de ADN

Durante años, las arquitecturas han evolucionado para equilibrar:

| Factor | Descripción |
|--------|-------------|
| **Expresividad** | Capacidad de capturar patrones complejos |
| **Eficiencia** | Coste computacional y memoria |
| **Escalabilidad** | Cómo behave con secuencias largas |
| **Estabilidad** | Facilidad de entrenamiento |

---

## 2. Comparativa General

```
                    EXPRESIVIDAD (captura dependencias)
                           ↑
                           │    ★ Transformers
                           │      ★ Hybrid
                           │      ★ RetNet
                           │    ★ Mamba
                           │      ★ Liquid
                           │    ★ LSTM/GRU
                           │
    ───────────────────────────────────────────────────→
                           │        EFICIENCIA (velocidad/memoria)
                           │
                           │
                           │
```

| Aspecto | Transformers | Liquid Models | Mamba/SSM |
|---------|-------------|---------------|-----------|
| **Complejidad** | O(n²) | O(n × k) | O(n × d) |
| **Memoria** | O(n²) | O(n × k) | O(n × d) |
| **Selección** | Atención completa | Gates locales | Selección global |
| **Estado** | Sin estado explícito | Sin estado explícito | Estado comprimido |
| **Paralelización** | Completa | Completa | Parcial (scan) |

---

## 3. Transformers

### 3.1 ¿Qué son?

Arquitectura basada en **auto-atención multi-cabeza** (Vaswani et al., 2017).

```
Arquitectura básica:
Input → Embedding → [Positional Encoding + MultiHead Attention + FFN] × N → Output
```

**Mecanismo clave**: La atención permite que cada token preste atención a todos los demás.

### 3.2 Ventajas

| Ventaja | Descripción |
|---------|-------------|
| ✅ **Atención completa** | Cada token puede attends a cualquier otro token |
| ✅ **Paralelización total** | Entrenamiento muy eficiente en GPU/TPU |
| ✅ **Captura long-range** | Dependencias a cualquier distancia |
| ✅ **Transfer learning** | Modelos pre-entrenados funcionan muy bien |
| ✅ **Ecosistema maduro** | Librerías, optimizaciones, hardware dedicado |
| ✅ **Escalabilidad probada** | GPT-4, Claude, LLaMA... miles de millones de parámetros |

### 3.3 Inconvenientes

| Inconveniente | Descripción |
|---------------|-------------|
| ❌ **Complejidad O(n²)** | Problemas con secuencias largas |
| ❌ **Memoria voraz** | O(n²) en atención, limitando contexto |
| ❌ **KV Cache** | En inferencia, el cache crece con la longitud |
| ❌ **Posiciones fuera de distribución** | Longitudes no vistas en entrenamiento |
| ❌ **Costo en inferencia** | Generar tokens uno a uno es caro |

### 3.4 Variantes para mejorar eficiencia

| Variante | Técnica | Reducción complejidad |
|----------|---------|----------------------|
| **Flash Attention** | IO-aware attention | O(n) memoria |
| **Sparse Attention** | Solo attends a tokens cercanos | O(n × k) |
| **Linear Attention** | Kernel trick | O(n) |
| **Longformer** | Ventana local + global | O(n) |
| **BigBird** | Sparse + random + global | O(n) |
| **ReLoRA** | Low-rank updates | Menos parámetros entrenables |

### 3.5 Ejemplos de uso típico

```
✅ IDEALES PARA TRANSFORMERS:
├── Generación de texto largo (LLMs)
├── Traducción de alta calidad
├── Resumen de documentos extensos
├── Question answering con contexto amplio
├── Código generation (Copilot)
└── Multimodal tasks (vision-language)

❌ MENOS IDEALES:
├── Audio en tiempo real (latencia alta)
├── Secuencias > 100K tokens
├── Dispositivos edge/móviles
└── Streaming de datos continuos
```

---

## 4. Liquid Foundation Models (LFM)

### 4.1 ¿Qué son?

Arquitectura híbrida que combina:
- **Convoluciones locales** (short-range dependencies)
- **Gates dinámicos** (selección de información)
- **Pocas capas de atención** (long-range cuando necesario)

Inspiración: Los LFMs reales usan TCNC (Time-Continuous Neural Circuits) + atención estratégica.

### 4.2 Arquitectura del LiquidBlock

```
Input x
    ↓
LayerNorm
    ↓
Proyección + Gate1 (decide qué entra)
    ↓
Conv1D (kernel_size=5, depthwise)
    ↓
Gate2 (decide qué sale)
    ↓
Proyección + Skip Connection
    ↓
LayerNorm + FFN
    ↓
Output
```

### 4.3 Ventajas

| Ventaja | Descripción |
|---------|-------------|
| ✅ **Eficiencia local** | O(n × k) para convoluciones |
| ✅ **Gates dinámicos** | Selección de contenido por input |
| ✅ **Trade-off controlable** | Balance atención/local según diseño |
| ✅ **Bueno para audio** | Audio tiene fuerte estructura local |
| ✅ **Menor memoria** | No cache de KV completo |

### 4.4 Inconvenientes

| Inconveniente | Descripción |
|---------------|-------------|
| ❌ **Dependencias lejanas** | Necesita stacking o atención |
| ❌ **Kernel size fijo** | Limitación inherente de la conv |
| ❌ **Menos expresivo** | Que atención global para long-range |
| ❌ **Menos maduro** | Ecosistema más pequeño que Transformers |

### 4.5 Ejemplos de uso típico

```
✅ IDEALES PARA LFM:
├── Procesamiento de audio (speech recognition)
├── Música generation
├── Señales biomédicas (ECG, EEG)
├── Time series cortas/medias
├── Robotics y control
└── edge computing

❌ MENOS IDEALES:
├── Texto muy largo
├── Tareas que requieren atención global constante
└── Cuando necesitas reasoning complejo
```

### 4.6 Liquid vs Transformer en Audio

```
Secuencia de audio: |S|A|M|P|L|E| (una palabra hablada)

TRANSFORMER:
Cada fonema atiende a TODOS los demás
S↔A↔M↔P↔L↔E  (conexiones globales)

LIQUID:
Cada fonema atiende solo a sus VECINOS (ventana local)
S-A, A-M, M-P, P-L, L-E  (conexiones locales)

Para audio, la estructura LOCAL es muy importante
(sílabas, fonemas adyacentes), así que Liquid puede ser eficiente.
```

---

## 5. Mamba / Selective SSM

### 5.1 ¿Qué son?

**Selective State Space Models** propuestos por Gu & Dao (2023).

La idea clave: hacer que los parámetros del SSM dependan del input, permitiendo **selección de contenido**.

```
SSM TRADICIONAL (S4):
A, B, C, D = FIJOS (parámetros globales)
→ El modelo procesa toda secuencia igual

MAMBA:
A_t, B_t, C_t, dt_t = f(x_t)  (dependen del input)
→ El modelo decide qué recordar en cada paso
```

### 5.2 Ecuaciones de Mamba

```
Entrada: x_t en dimensión d_model
Estado: h_t en dimensión d_state (típico: 16)

1. Proyectar: x_t → (x_inner, z)
2. Calcular selección:
   - B_t = Linear(x_inner)  → qué va al estado
   - C_t = Linear(x_inner)  → qué sale del estado
   - dt_t = softplus(Linear(x_inner))  → tiempo de retención
3. SSM scan:
   h_t = dt_t * (A * h_{t-1} + B_t * x_t)
   y_t = C_t * h_t
4. Puerta: y_t = y_t * sigmoid(z)
```

### 5.3 Ventajas

| Ventaja | Descripción |
|---------|-------------|
| ✅ **Complejidad O(n)** | Escala linealmente con la secuencia |
| ✅ **Selección de contenido** | Decide qué recordar dinámicamente |
| ✅ **Estado comprimido** | Memoria fija independiente de seq length |
| ✅ **Inducción kuat** | Puede copiar patrones observados |
| ✅ **Buen balance** | Calidad cercana a Transformer con eficiencia |

### 5.4 Inconvenientes

| Inconveniente | Descripción |
|---------------|-------------|
| ❌ **SSM scan secuencial** | No paralelizable como atención |
| ❌ **Estado fijo** | Puede perder información si d_state pequeño |
| ❌ **Dependencias lejanas** | Stacking necesario para muy largo alcance |
| ❌ **Menos mature** | Optimizaciones hardware en desarrollo |

### 5.5 Variantes de Mamba

| Variante | Descripción |
|----------|-------------|
| **Mamba-1** | Versión original |
| **Mamba-2** | SSD (State Space Duality), más eficiente |
| **Jamba** | Mamba + Attention (Mixtral-style MoE) |
| **Mamba-XXL** | 1.3B parámetros |
| **Grok** | Modelo de xAI basado en Mamba |

### 5.6 Ejemplos de uso típico

```
✅ IDEALES PARA MAMBA:
├── Secuencias muy largas (> 10K tokens)
├── Genómica y DNA (CADDI, HyenaDNA)
├── Audio largo (music generation)
├── Time series forecasting
├── Agentes con memoria
├── edge computing con constraints

❌ MENOS IDEALES:
├── Tareas que requieren atención precisa posicional
├── Contexto muy extenso sin estructura
└── Cuando tienes mucho presupuesto compute
```

### 5.7 Mamba vs Liquid: Diferencias clave

```
                    MAMBA                          LIQUID
                    
Estado:        Comprimido (d_state)           Sin estado explícito
               Memoria fija                    Memoria en parámetros
               
Selección:     B_t, C_t, dt_t                 Gate1, Gate2
               (global, aprendido)             (local, aprendido)
               
Mecanismo:     SSM scan (recurrencia)         Conv1D + gates
               "cómo fluye el estado"         "qué filtro paso"
               
Captura:       Puede recordar tokens           Patrones locales
               específicos observados         secuencialmente
               
Eficiencia:    O(n × d_state)                 O(n × k)
               d_state típicamente 16         k típicamente 5
```

---

## 6. Otras Arquitecturas Relevantes

### 6.1 LSTM / GRU

```
LSTM (Long Short-Term Memory):
┌──────────────────────────────────────┐
│  Gate de entrada:   qué guardar      │
│  Gate de olvido:     qué olvidar      │
│  Gate de salida:     qué leer        │
└──────────────────────────────────────┘

h_t = h_{t-1} * forget_gate + input_gate * new_value
```

| Aspecto | LSTM/GRU | Mamba |
|---------|----------|-------|
| **Selección** | Gates fijos | Input-dependent |
| **Paralelización** | No | Parcial (scan) |
| **Estado** | Completo | Comprimido |
| **Complejidad** | O(n × d) | O(n × d) |

**Uso actual**: LSTM/GRU se usan menos para texto, pero siguen siendo populares en:
- Robótica (control)
- Time series financieras
- Cualquier dominio con secuencias cortas

### 6.2 RWKV

**Receptance Weighted Key Values** (Peng et al., 2023)

```
Arquitectura: Transformer - Attention + RNN

"Cuantizamos el transformer a una RNN,
 conservando su capacidad de parallel training"
```

```
                    RWKV
┌─────────────────────────────────────┐
│  Tiempo discretizado (no recursivo)  │
│  gates tipo WKV                      │
│  Linear attention (no softmax)        │
│  Puede entrenar como transformer      │
│  Puede inferir como RNN              │
└─────────────────────────────────────┘
```

**Ventajas**:
- ✅ Entrenamiento paralelo (como Transformer)
- ✅ Inferencia constante (como RNN)
- ✅ Sin KV cache explosivo
- ✅ Modelo abierto (RWKV-4 de 14B)

**Inconvenientes**:
- ❌ Less expressive que atención completa
- ❌ Menos optimizaciones de hardware

### 6.3 RetNet

**Retention Networks** (Microsoft, 2023)

```
Arquitectura: Linear attention con decay multi-escala

"Retentive Attention = Linear attention + Decay + Chunk"
```

| Propiedad | RetNet | Mamba | RWKV |
|-----------|--------|-------|------|
| Paralel train | ✅ | Parcial | ✅ |
| Inferencia | O(1) | O(n) | O(1) |
| Long context | ✅ | ✅ | ✅ |
| Código abierto | ⚠️ | ✅ | ✅ |

### 6.4 Hyena

**Hyena: Implicit Attention is All You Need** (Poli et al., 2023)

```
Idea: Reemplazar atención con...

H(x) = Σ w_i * x(t-i)  (convolución suave)

Donde w_i son filtros aprendidos, no fija.
```

**Ventajas**:
- ✅ O(n log n) en lugar de O(n²)
- ✅ Sin operaciones de softmax
- ✅ Bueno para secuencias muy largas

### 6.5 gMLP

**Gated Multilayer Perceptron** (Liu et al., 2021)

```
Arquitectura: 
- Sin atención
- Solo gates y convs

┌─────────────────────────────────┐
│  Spatial Gating Unit (SGU)      │
│  x * W + U * x + b              │
└─────────────────────────────────┘
```

**Resultado**: Funciona bien en NLP sin atención.

### 6.6 Fast Weight Programmers

```
Idea: Redes que "programan" los pesos de otra red

w_new = w_old + α * f(x)

Donde f es una función learnable.
```

Pionero de este paradigma: Schmidhuber (1992).

---

## 7. Tabla Comparativa Completa

| Arquitectura | Complejidad | Memoria | Paralelismo | Estado | Selection | Uso Típico |
|-------------|------------|---------|-------------|--------|-----------|------------|
| **Transformer** | O(n²) | O(n²) | Total | No | Atención | LLM, traducción |
| **Flash Attention** | O(n) | O(n) | Total | No | Atención | LLM optimizado |
| **LSTM/GRU** | O(n×d) | O(n×d) | No | Sí | Fijo | Time series |
| **Liquid (LFM)** | O(n×k) | O(n×k) | Total | No | Local | Audio, señales |
| **Mamba** | O(n×d) | O(n×d) | Parcial | Sí | Global | Genómica, agentes |
| **RWKV** | O(n×d) | O(n×d) | Total | Sí | Global | LLM eficiente |
| **RetNet** | O(n) | O(n) | Total | Sí | Global | LLM optimizado |
| **Hyena** | O(n log n) | O(n) | Parcial | No | Filtros | Secuencias largas |
| **gMLP** | O(n) | O(n) | Total | No | No | NLP sin atención |

### Leyenda de la tabla

```
n  = longitud de secuencia
d  = dimensión del modelo
k  = tamaño del kernel (típico 5)
```

---

## 8. Cuándo Usar Cada Arquitectura

### 8.1 Decision Tree

```
START: ¿Cuál es tu caso de uso?
│
├─► ¿Procesando texto?
│   ├─► ¿Longitud < 8K tokens?
│   │   └─► Transformer (o Flash Attention)
│   ├─► ¿Longitud > 8K tokens?
│   │   ├─► ¿Prioridad eficiencia?
│   │   │   └─► Mamba, RWKV, RetNet
│   │   └─► ¿Prioridad calidad máxima?
│   │       └─► Longformer, Flash Attention 2
│   └─► ¿edge device?
│       └─► RWKV, Mamba
│
├─► ¿Procesando audio?
│   ├─► ¿Audio continuo/largo?
│   │   └─► Mamba, Liquid
│   └─► ¿Clasificación/short clips?
│       └─► Liquid, CNN+RNN
│
├─► ¿Genómica/DNA?
│   └─► HyenaDNA, Mamba
│
├─► ¿Time series?
│   ├─► ¿Largas?
│   │   └─► Mamba
│   └─► ¿Cortas?
│       └─► LSTM/GRU, Transformer
│
└─► ¿Agentes con memoria?
    └─► Mamba (estado persistente)
```

### 8.2 Matriz de Decisión

```
                    CORTO (<1K)          MEDIO (1K-8K)        LARGO (>8K)
                    
┌─────────────────┬─────────────────────┬─────────────────────┬────────────────────┐
│ BAJO PRESUPUESTO│ LSTM/GRU            │ RWKV, Mamba         │ Mamba, Hyena       │
├─────────────────┼─────────────────────┼─────────────────────┼────────────────────┤
│ PRESUPUESTO     │ Transformer (Tiny)  │ Flash Attention     │ Flash Attention 2   │
│ MODERADO        │ Liquid              │ Liquid + Attn       │ Longformer         │
├─────────────────┼─────────────────────┼─────────────────────┼────────────────────┤
│ ALTO PRESUPUESTO│ Transformer (Base)  │ Transformer (Base)  │ Transformer + HA   │
│                 │                     │                     │ (si calidad crítica)│
└─────────────────┴─────────────────────┴─────────────────────┴────────────────────┘
```

### 8.3 Comparación de Escenarios

| Escenario | Mejor Opción | Segunda Opción | Por qué |
|-----------|-------------|----------------|---------|
| **Chatbot general** | Transformer | RWKV | Calidad y ecosistema |
| **Resumen largo** | Flash Attn + chunk | Longformer | Necesitas contexto |
| **Transcripción audio** | Mamba | Liquid | Audio largo eficiente |
| **Trading algorítmico** | LSTM | Transformer | Secuencias cortas, velocidad |
| **Análisis ADN** | HyenaDNA | Mamba | Contexto genómico |
| **Música generation** | Mamba | Liquid | Longitud, coherencia |
| **Robótica** | LSTM | Liquid | Control en tiempo real |
| **Edge NLP** | RWKV | Mamba | Inferencia eficiente |
| **Agente con memoria** | Mamba | RWKV | Estado persistente |

---

## 9. Evolución Histórica

```
2013: LSTM (Hochreiter & Schmidhuber)
     └─► RNNs con gates para long-range dependencies

2017: Transformer (Vaswani et al.)
     └─► Atención reemplaza recurrencia
     └─► GPT, BERT, T5...

2019-2020: Eficiencia para Transformers
     └─► Longformer, Reformer, Linformer...
     └─► Flash Attention

2021: gMLP, MLP-Mixer
     └─► "¿Necesitamos atención?"

2022: S4 (State Space Models)
     └─► SSM para secuencias largas
     └─► Hyena

2023: Mamba (Gu & Dao)
     └─► Selective SSM = selección de contenido
     └─► RWKV, RetNet

2024: Mamba-2, Jamba, Grok
     └─► Híbridos, MoE + SSM
     └─► Optimizaciones hardware
```

### Línea temporal conceptual

```
        CAPACIDAD DE SELECCIÓN (qué recordar)
               ↑
               │    ★ Transformer
               │      ★ Hybrid
               │    ★ RWKV
               │    ★ Mamba
               │    ★ RetNet
               │  ★ LSTM/GRU
               │  ★ Liquid
               │
    ───────────────────────────────────────────────────→
               │        EFICIENCIA (para largo contexto)
               │
```

---

## 10. Recursos

### Papers fundamentales

| Paper | Año | Contribución |
|-------|-----|--------------|
| "Attention is All You Need" | 2017 | Transformer |
| "LSTM" | 1997 | LSTM |
| "Mamba" | 2023 | Selective SSM |
| "S4" | 2021 | SSM para secuencias largas |
| "RWKV" | 2023 | Linear transformer + RNN |
| "RetNet" | 2023 | Linear retention |
| "Hyena" | 2023 | Implicit attention |
| "Flash Attention" | 2022 | Attention eficiente |
| "Liquid" | 2023 | LFM |

### Implementaciones

```
TRANSFORMERS:
├── Hugging Face Transformers
├── vLLM, TGI (inferencia)
└── Flash Attention

MAMBA:
├── mamba-ssm (official)
├── causal-conv1d
└── transformers-mamba

RWKV:
├── rwkv-infctx-trainer
└── rwkv.cpp (quantized)

LIQUID:
└── Implementación propia (como en los notebooks)
```

---

## 📝 Resumen Final

### Regla mnemotécnica

```
T-R-A-N-S:
Transformer → Todo, Rápido entrenamiento, Atención global
              N → No para largo contexto sin optimizaciones
              S → Scaling funciona

M-A-M-B-A:
Mamba → Memoria comprimida, Atención lineal, Bueno para largo
        B → Balance calidad-velocidad
        A → Amplio uso (genómica, audio, agentes)

L-I-Q-U-I-D:
Liquid → Local primero, Ideal para audio, Quiet (eficiente)
         U → Usa gates, No todo es atención
         D → Dynamic selection
```

### Frases clave

> **Transformer**: *"Puedo attends a cualquiera, pero el precio sube con n²."*

> **Mamba**: *"Elijo qué recordar y qué olvidar, escalo lineal."*

> **Liquid**: *"Miro mi vecindario eficientemente, con ayuda ocasional de atención."*

> **RWKV**: *"Entreno como transformer, infiero como RNN."*

---

*Documento creado para UD4 · Modelado Avanzado*
*Basado en papers originales y estado del arte 2024*
