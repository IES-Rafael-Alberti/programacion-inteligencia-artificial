# Resumen: Material Didáctico - Modelos Alternativos a Transformers
## UD4 · Modelado Avanzado

**Fecha de creación**: 14 de abril de 2026  
**Autor**: 

---

## 📁 Estructura del proyecto

```
modelos_alternativos/
│
├── 📄 DOCUMENTACIÓN PRINCIPAL
│   ├── Arquitecturas_comparativa.md       # Guía comparativa completa de arquitecturas
│   ├── 00-Tabla_Comparativa_Ejemplos.md   # Tabla resumen de los 4 ejemplos
│   ├── 01-Practica_Comparativa.md         # Guía de la práctica (tareas, rúbrica)
│   └── 02-Plantilla_Informe.md            # Plantilla de informe para alumnos
│
├── 📊 SCRIPTS DE ANÁLISIS
│   ├── metricas.py                       # Recopila y compara métricas
│   └── comparativa.py                     # Script completo de comparativa
│
├── 📁 scripts_mamba/                     # 4 ejemplos Mamba completos
│   ├── mamba_blocks.py                   # Módulo base con arquitecturas
│   ├── ejemplo_mamba_1_traduccion_en_es.py
│   ├── ejemplo_mamba_2_generacion_decoder_only.py
│   ├── ejemplo_mamba_3_clasificacion_intenciones.py
│   └── ejemplo_mamba_4_reformulacion.py
│
├── 📁 scripts_lfm/                       # 4 ejemplos LFM completos
│   ├── lfm_blocks.py                     # Módulo base con arquitecturas
│   ├── ejemplo_lfm_1_traduccion_en_es.py
│   ├── ejemplo_lfm_2_generacion_decoder_only.py
│   ├── ejemplo_lfm_3_clasificacion_intenciones.py
│   └── ejemplo_lfm_4_reformulacion.py
│
├── 📁 datos/                             # Datos compartidos
│   ├── mini_trad_es_en_ampliado.tsv
│   ├── mini_estilo_quijote.txt
│   ├── mini_clasificacion_intenciones.tsv
│   ├── mini_reformulacion_es.tsv
│   ├── mini_trad_es_en.tsv
│   ├── mini_qa_dataset.tsv
│   └── el_quijote.txt
│
├── 📓 NOTEBOOKS
│   ├── Mamba_quijote_comparativa.ipynb    # Notebook comparativo Mamba (profesor)
│   ├── Mamba_version_alumno.ipynb          # Notebook Mamba (alumno)
│   ├── LFM_quijote_comparativa.ipynb      # Notebook comparativo LFM (profesor)
│   ├── LFM_version_alumno.ipynb           # Notebook LFM (alumno)
│   ├── RWKV_quijote_comparativa.ipynb     # Notebook comparativo RWKV (profesor)
│   └── RWKV_version_alumno.ipynb          # Notebook RWKV (alumno)
│
└── 📄 DOCUMENTACIÓN ADICIONAL
    ├── LFM_version_profesor.md
    ├── LFM_version_alumno.md
    ├── Mamba_version_profesor.md
    ├── Mamba_version_alumno.md
    ├── RWKV_version_profesor.md
    └── RWKV_version_alumno.md
```

---

## 📋 Resumen de contenido

### 1. Arquitecturas implementadas

| Arquitectura | Tipo | Complejidad | Característica clave |
|-------------|------|-------------|---------------------|
| **Mamba** | Selective SSM | O(n × d_state) | Selección de contenido (B, C, dt input-dependent) |
| **LFM** | Liquid Models | O(n × kernel) | Conv1D + Gates dinámicos |
| **RWKV** | Linear Attention | O(n × d) | Entrena como Transformer, infiere como RNN |

### 2. Ejemplos por tarea

| # | Tarea | Tipo | Transformer | Mamba | LFM |
|---|-------|------|:-----------:|:-----:|:---:|
| 1 | Traducción EN→ES | Seq2Seq | ✅ | ✅ | ✅ |
| 2 | Generación Quijote | Decoder-Only | ✅ | ✅ | ✅ |
| 3 | Clasificación Intenciones | Encoder-Only | ✅ | ✅ | ✅ |
| 4 | Reformulación Sinónimos | Seq2Seq | ✅ | ✅ | ✅ |

### 3. Material por rol

#### Versión Profesor
- Notebook comparativo (código funcional, mínimo comentarios)
- Guía de sesión didáctica
- Secuencia de pasos para conducir la clase
- Puntos técnicos a destacar
- Posibles preguntas y respuestas

#### Versión Alumno
- Notebook educativo (explicaciones extensas, analogías)
- Código comentado paso a paso
- Ejercicios integrados
- Preguntas de reflexión
- Guía de estudio con glosario

### 4. Práctica de comparativa

**Objetivo**: Comparar experimentalmente Transformer, Mamba y LFM en la misma tarea.

**Tareas disponibles**:
1. Traducción EN→ES
2. Generación estilo Quijote
3. Clasificación de intenciones
4. Reformulación con sinónimos

**Métricas a comparar**:
- Loss final
- Tiempo de entrenamiento
- Tiempo de inferencia
- Número de parámetros
- Tamaño del modelo

**Entregables**:
- Código de los 3 modelos
- Gráficos comparativos (mínimo 3)
- Informe con análisis

---

## 🎯 Uso sugerido

### Para dar la clase
1. Usar notebooks de alumno para explicar conceptos
2. Ejecutar notebooks comparativos en vivo
3. Discutir resultados con la guía del profesor

### Para la práctica
1. Dividir en grupos de 2
2. Cada grupo implementa una tarea con los 3 modelos
3. Comparar resultados siguiendo la plantilla de informe

---

## 📚 Referencias

- **Transformer**: "Attention Is All You Need" (Vaswani et al., 2017)
- **Mamba**: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" (Gu & Dao, 2023)
- **LFM**: Liquid Foundation Models (Hasani et al.)
- **RWKV**: "RWKV: Reinventing RNNs for the Transformer Era" (Peng et al., 2023)

---

## 🔧 Requisitos

```bash
pip install torch matplotlib tqdm
```

---

*Material creado para UD4 · Modelado Avanzado*
*IES Rafael Alberti*
