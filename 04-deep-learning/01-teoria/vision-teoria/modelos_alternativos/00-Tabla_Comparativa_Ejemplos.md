# UD4 · Ejemplos Comparativos: Transformer, Mamba y LFM

## Tabla Resumen de Ejemplos

| # | Tarea | Tipo | Arquitecura | Datos | Comparativa |
|---|-------|------|-------------|-------|-------------|
| 1 | Traducción EN→ES | Seq2Seq | Encoder-Decoder | `mini_trad_es_en_ampliado.tsv` | Los 3 aprenden a traducir |
| 2 | Generación Quijote | Generative | Decoder-Only | `mini_estilo_quijote.txt` | Los 3 generan texto estilo Quijote |
| 3 | Clasificación Intenciones | Clasificación | Encoder-Only | `mini_clasificacion_intenciones.tsv` | Los 3 clasifican intenciones |
| 4 | Reformulación Sinónimos | Seq2Seq | Encoder-Decoder | `mini_reformulacion_es.tsv` | Los 3 reformulan con sinónimos |

---

## Arquitectura de los Bloques

### Transformer (referencia)
```
Encoder: [MultiHeadAttention + FFN] × N
Decoder: [MaskedAttn + CrossAttn + FFN] × N
```

### Mamba Blocks
```
Encoder: [MambaBidirectional + FFN] × N
Decoder: [MambaCausal + FFN] × N

MambaBlock internamente:
  - Proyección entrada → (x_inner, z)
  - Conv1D local (kernel=4)
  - SSM Scan con selección B, C, dt
  - Gate z + skip D
```

### Liquid Blocks
```
Encoder: [LiquidBidirectional + FFN] × N
Decoder: [LiquidCausal + FFN] × N

LiquidBlock internamente:
  - LayerNorm
  - Gate1 + Proyección
  - Conv1D (kernel=5, depthwise)
  - Gate2
  - Skip connection
```

---

## Parámetros Clave

### Mamba
| Parámetro | Valor típico | Descripción |
|-----------|--------------|-------------|
| `d_model` | 64 | Dimensión del embedding |
| `d_state` | 16 | Tamaño del estado SSM |
| `d_conv` | 4 | Tamaño kernel conv |
| `expand` | 2 | Factor expansión |

### LFM
| Parámetro | Valor típico | Descripción |
|-----------|--------------|-------------|
| `d_model` | 64 | Dimensión del embedding |
| `kernel_size` | 5 | Tamaño del filtro conv |
| `num_layers` | 6-8 | Número de capas |

---

## Ejecución

### Mamba
```bash
cd modelos_alternativos/scripts_mamba

# Traducción
python ejemplo_mamba_1_traduccion_en_es.py

# Generación
python ejemplo_mamba_2_generacion_decoder_only.py

# Clasificación
python ejemplo_mamba_3_clasificacion_intenciones.py

# Reformulación
python ejemplo_mamba_4_reformulacion.py
```

### LFM
```bash
cd modelos_alternativos/scripts_lfm

# Traducción
python ejemplo_lfm_1_traduccion_en_es.py

# Generación
python ejemplo_lfm_2_generacion_decoder_only.py

# Clasificación
python ejemplo_lfm_3_clasificacion_intenciones.py

# Reformulación
python ejemplo_lfm_4_reformulacion.py
```

---

## Comparativa de Complejidad

| Arquitectura | Complejidad | Ventaja |
|--------------|-------------|---------|
| **Transformer** | O(n²) | Máxima expresividad |
| **Mamba** | O(n × d_state) | Balance eficiencia/capacidad |
| **LFM** | O(n × k) | Muy eficiente para locales |

Para secuencias cortas (~20 tokens), las diferencias son mínimas.
Para secuencias largas, Mamba y LFM escalan mejor.

---

## Notas de Implementación

### Mamba
- Usa SSM Scan para mantener estado
- d_state controla la "memoria" del modelo
- Bidireccional en encoder, causal en decoder

### LFM
- Usa solo convoluciones + gates
- kernel_size controla el contexto local
- Bidireccional en encoder, causal en decoder

---

## Preguntas de Reflexión

1. **¿Cuál converge más rápido?**
   - LFM y Mamba suelen necesitar menos épocas para tareas locales
   - Transformer puede ser mejor para dependencias lejanas

2. **¿Cuál genera mejor texto?**
   - Transformer: más coherente pero lento
   - Mamba: buen balance
   - LFM: puede repetir más

3. **¿Cuál para clasificación?**
   - Los 3 funcionan bien con datasets pequeños
   - Mamba y LFM pueden ser más eficientes

---

## Estructura de Archivos

```
modelos_alternativos/
├── scripts_mamba/
│   ├── mamba_blocks.py              # Módulo base con arquitecturas
│   ├── ejemplo_mamba_1_traduccion_en_es.py
│   ├── ejemplo_mamba_2_generacion_decoder_only.py
│   ├── ejemplo_mamba_3_clasificacion_intenciones.py
│   └── ejemplo_mamba_4_reformulacion.py
│
├── scripts_lfm/
│   ├── lfm_blocks.py                # Módulo base con arquitecturas
│   ├── ejemplo_lfm_1_traduccion_en_es.py
│   ├── ejemplo_lfm_2_generacion_decoder_only.py
│   ├── ejemplo_lfm_3_clasificacion_intenciones.py
│   └── ejemplo_lfm_4_reformulacion.py
│
├── datos/
│   ├── mini_trad_es_en_ampliado.tsv
│   ├── mini_estilo_quijote.txt
│   ├── mini_clasificacion_intenciones.tsv
│   └── mini_reformulacion_es.tsv
│
└── modelos/                         # Se crean al entrenar
    ├── mamba_*.pt
    └── lfm_*.pt
```

---

*Material para UD4 · Modelado Avanzado*
