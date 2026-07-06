# UD4 · Práctica: Comparativa de Arquitecturas Secuenciales
## Transformer vs Mamba vs Liquid Foundation Models

---

## 🎯 Objetivo de la Práctica

Comparar experimentalmente tres arquitecturas de modelización secuencial en la misma tarea:

1. **Transformer** (referencia)
2. **Mamba** (Selective State Spaces)
3. **LFM** (Liquid Foundation Models)

---

## 📋 Tareas Disponibles

Elige **UNA** de las siguientes tareas para comparar:

| # | Tarea | Descripción | Dataset | Dificultad |
|---|-------|-------------|---------|------------|
| 1 | **Traducción EN→ES** | Traducir frases inglés a español | `mini_trad_es_en_ampliado.tsv` | ⭐⭐⭐ |
| 2 | **Generación Quijote** | Generar texto estilo Quijote | `mini_estilo_quijote.txt` | ⭐⭐ |
| 3 | **Clasificación Intenciones** | Clasificar frases por tipo | `mini_clasificacion_intenciones.tsv` | ⭐ |
| 4 | **Reformulación** | Reformular con sinónimos | `mini_reformulacion_es.tsv` | ⭐⭐⭐ |

---

## 📁 Estructura del Proyecto

```
comparativa_practica/
├── transformer/              # Tu implementación Transformer
│   ├── transformer_blocks.py
│   └── tu_modelo.py
│
├── mamba/                   # Tu implementación Mamba
│   ├── mamba_blocks.py
│   └── tu_modelo.py
│
├── lfm/                     # Tu implementación LFM
│   ├── lfm_blocks.py
│   └── tu_modelo.py
│
├── datos/                   # Datos (copiados de transformers)
│
├── metricas.py             # Script para medir tiempos
│
└── comparativa.py          # Script final de comparación
```

---

## 📊 Métricas a Recopilar

Para cada modelo, registra:

### 1. Eficacia
- [ ] Pérdida final (cross-entropy)
- [ ] Accuracy (si aplica: clasificación, traducción exacta)
- [ ] Pérdida por época (guarda la curva)

### 2. Tiempo de Entrenamiento
- [ ] Tiempo total (segundos)
- [ ] Tiempo por época
- [ ] Tiempo por batch

### 3. Tiempo de Inferencia
- [ ] Tiempo por predicción (ms)
- [ ] Tiempo para generar N tokens (si aplica)

### 4. Recursos
- [ ] Memoria GPU peak (MB)
- [ ] Número de parámetros
- [ ] Tamaño del modelo en disco (MB)

---

## 📝 Plantilla de Resultados

```python
# resultados_modelos.py

RESULTADOS = {
    "traduccion": {
        "transformer": {
            "epochs": 300,
            "tiempo_total_s": ...,
            "tiempo_por_epoca_s": ...,
            "loss_final": ...,
            "accuracy": ...,
            "parametros": ...,
            "tamano_mb": ...,
            "tiempo_inferencia_ms": ...,
        },
        "mamba": {
            # mismo formato
        },
        "lfm": {
            # mismo formato
        },
    },
    # repetir para otras tareas
}
```

---

## 🧪 Experimentos Obligatorios

### Experimento 1: Misma arquitectura, distintos tamaños
Compara cómo escala cada modelo con `d_model` creciente (32, 64, 128).

### Experimento 2: Misma capacidad, distinta eficiencia
Iguala el número de parámetros y compara calidad y velocidad.

### Experimento 3: Análisis de convergencia
Grafica la curva de pérdida de los tres modelos en la misma figura.

---

## 📈 Plantilla de Gráficos

Genera estos gráficos con matplotlib:

1. **Curvas de pérdida**: Los tres modelos en la misma figura
2. **Tiempo de entrenamiento**: Barras comparativas
3. **Accuracy vs Tiempo**: Scatter plot
4. **Uso de memoria**: Barras por época (opcional)

---

## 📋 Rúbrica de Evaluación

| Aspecto | Puntos | Criterio |
|---------|--------|----------|
| **Implementación** | 30 | Los 3 modelos funcionan correctamente |
| **Métricas** | 25 | Todas las métricas recogidas |
| **Gráficos** | 20 | Al menos 3 gráficos comparativos |
| **Análisis** | 25 | Conclusiones fundamentadas |

---

## ⏱️ Entrega

- **Fecha**: [definir]
- **Formato**: Carpeta comprimida con código + informe PDF
- **Informe**: 3-5 páginas con análisis de resultados

---

## 📚 Recursos

### Scripts de Referencia (Transformers)
```
/home/jmsa/IESRafaelAlberti/RafaelAlberti25_26/Modulos/PIA/UD4/04-modelado-avanzado/nlp/transformers/scripts/
```

### Scripts a Implementar
```
modelos_alternativos/scripts_mamba/
modelos_alternativos/scripts_lfm/
```

### Documentación
```
modelos_alternativos/Arquitecturas_comparativa.md
modelos_alternativos/Mamba_version_profesor.md
modelos_alternativos/LFM_version_profesor.md
```

---

## 🔍 Preguntas de Análisis

Responde en tu informe:

1. **¿Cuál converge más rápido?** ¿Por qué crees que ocurre?

2. **¿Cuál genera mejor texto?** (si aplicas tareas generativas)

3. **¿El modelo más rápido es el más preciso?** Comenta la relación velocidad/precisión.

4. **¿Cómo afecta `d_model` a cada arquitectura?**

5. **¿Qué limitaciones observas en Mamba vs LFM?**

6. **¿Recomendarías algún modelo para producción?** Justifica.

---

## 💡 Consejos

1. **Empieza simple**: Haz que funcione primero con d_model=32
2. **Mide desde el principio**: Añade timing al código inicial
3. **Guarda checkpoints**: No quieras entrenar 300 épocas de golpe
4. **Compara en mismas condiciones**: Mismos datos, mismos hiperparámetros
5. **Usa GPU si puedes**: Las comparativas en CPU son mucho más lentas

---

## 📝 Plantilla de Informe

```
# Informe: Comparativa de Arquitecturas Secuenciales

## 1. Introducción
   - Objetivo
   - Tarea elegida
   - Justificación

## 2. Metodología
   - Datasets utilizados
   - Hiperparámetros
   - Métricas

## 3. Resultados
   - Tablas con métricas
   - Gráficos comparativos
   - Análisis de convergencia

## 4. Discusión
   - Respuestas a las preguntas
   - Limitaciones
   - Posibles mejoras

## 5. Conclusiones
   - Resumen de hallazgos
   - Recomendaciones

## 6. Referencias
   - Papers, documentación
```

---

*Práctica para UD4 · Modelado Avanzado*
*Fecha de entrega: [definir]*
