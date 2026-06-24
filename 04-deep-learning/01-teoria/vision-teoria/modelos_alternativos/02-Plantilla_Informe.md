# Informe: Comparativa de Arquitecturas Secuenciales

## Transformer vs Mamba vs Liquid Foundation Models

---

**Alumno(s)**: _______________________________

**Fecha**: _______________________________

**Tarea elegida**: _______________________________

---

## 1. Introducción

### 1.1 Objetivo
[Describe el objetivo de la práctica]

### 1.2 Justificación de la tarea
[¿Por qué elegiste esta tarea? ¿Qué te pareció más interesante?]

### 1.3 Arquitecturas comparadas
| Arquitectura | Descripción breve |
|--------------|------------------|
| Transformer | [descripción] |
| Mamba | [descripción] |
| LFM | [descripción] |

---

## 2. Metodología

### 2.1 Dataset
- **Tamaño**: __________ ejemplos
- **División train/test**: __________ / __________
- **Vocabulary size**: __________

### 2.2 Hiperparámetros comunes
| Parámetro | Valor |
|-----------|-------|
| `d_model` | |
| `batch_size` | |
| `learning_rate` | |
| `epochs` | |
| `num_layers` | |

### 2.3 Métricas utilizadas
- [ ] Cross-Entropy Loss
- [ ] Accuracy (especificar si aplica)
- [ ] Tiempo de entrenamiento
- [ ] Tiempo de inferencia
- [ ] Memoria GPU peak
- [ ] Número de parámetros

---

## 3. Resultados

### 3.1 Tabla comparativa de métricas

| Métrica | Transformer | Mamba | LFM |
|---------|-------------|-------|-----|
| Loss final | | | |
| Loss mínimo | | | |
| Épocas para convergencia | | | |
| Tiempo total (s) | | | |
| Tiempo por época (s) | | | |
| Tiempo inferencia (ms) | | | |
| Parámetros | | | |
| Tamaño (MB) | | | |

### 3.2 Curvas de convergencia

[Incluir gráfico: Loss vs Época para los 3 modelos]

```
[Pegar gráfico aquí]
```

### 3.3 Análisis de convergencia

[¿Cuál converge más rápido? ¿Por qué?]

_____________________________________________

_____________________________________________

### 3.4 Tiempo de entrenamiento

[Incluir gráfico: Tiempo de entrenamiento por modelo]

```
[Pegar gráfico aquí]
```

### 3.5 Análisis de eficiencia

| Modelo | Velocidad relativa | Eficacia relativa |
|--------|-------------------|-------------------|
| Transformer | 1.0x (referencia) | 1.0x (referencia) |
| Mamba | | |
| LFM | | |

---

## 4. Análisis Detallado

### 4.1 Transformer
**Fortalezas:**
- _____________________________________________
- _____________________________________________

**Debilidades:**
- _____________________________________________
- _____________________________________________

### 4.2 Mamba
**Fortalezas:**
- _____________________________________________
- _____________________________________________

**Debilidades:**
- _____________________________________________
- _____________________________________________

### 4.3 Liquid Foundation Models
**Fortalezas:**
- _____________________________________________
- _____________________________________________

**Debilidades:**
- _____________________________________________
- _____________________________________________

---

## 5. Preguntas de Análisis

### 5.1 ¿Cuál converge más rápido?
[Tu respuesta]

_____________________________________________

### 5.2 ¿Cuál genera mejor texto / es más preciso?
[Tu respuesta]

_____________________________________________

### 5.3 ¿El modelo más rápido es el más preciso?
[Comenta la relación velocidad/precisión]

_____________________________________________

### 5.4 ¿Cómo afecta `d_model` a cada arquitectura?
[Discute el escalado]

_____________________________________________

### 5.5 ¿Qué limitaciones observas en Mamba vs LFM?
[Comparación cualitativa]

_____________________________________________

### 5.6 ¿Recomendarías algún modelo para producción?
| Escenario | Modelo recomendado | Justificación |
|-----------|-------------------|---------------|
| Baja latencia | | |
| Máxima calidad | | |
| Balance | | |
| Memoria limitada | | |

---

## 6. Conclusiones

### 6.1 Resumen de hallazgos
- _____________________________________________
- _____________________________________________
- _____________________________________________

### 6.2 Aprendizajes clave
- _____________________________________________
- _____________________________________________

### 6.3 Posibles mejoras
- _____________________________________________
- _____________________________________________

---

## 7. Anexo: Código

[Incluye las partes más relevantes de tu código]

### A.1 Transformer
```python
# Pegar código del Transformer
```

### A.2 Mamba
```python
# Pegar código del Mamba
```

### A.3 LFM
```python
# Pegar código del LFM
```

---

## 8. Referencias

- Paper Transformer: "Attention Is All You Need"
- Paper Mamba: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
- Paper LFM: [referencia]
- Documentación PyTorch

---

## Checklist de entrega

- [ ] Código de los 3 modelos
- [ ] Métricas recogidas
- [ ] Gráficos comparativos (mínimo 3)
- [ ] Informe completado
- [ ] Comparativa justificada

---

*Fin del informe*
