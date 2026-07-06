# Tarea: Ampliación de Vocabulario - Instrucciones de Entrega

## Fecha de entrega

**Consultar fecha límite en plataforma del centro.**

---

## Formato de entrega

Se puede entregar:

1. **Notebook Jupyter** (`.ipynb`) con todo el código, ejecución y resultados
2. **Script Python** (`.py`) + **documentación** (informe en PDF o Markdown)
3. **Repositorio GitHub/GitLab** con el código y documentación

---

## Contenido obligatorio

### 1. Código

- Código del transformer ampliado y entrenado
- Código de carga y uso del modelo pre-entrenado
- Notebook o script ejecutable de principio a fin

### 2. Vocabulario ampliado

- **Vocabulario original**: tamaño y muestra de tokens
- **Vocabulario ampliado**: tamaño y muestra de tokens
- **Datos añadidos**: indicar fuente y cantidad
- **Preprocesamiento**: técnicas aplicadas (limpieza, normalización, etc.)

**Ejemplo de tabla:**

| Métrica | Original | Ampliado |
|---------|----------|----------|
| Tamaño vocabulario | X | Y |
| Tokens unknown (%) | Z% | W% |
| Datos entrenamiento | X oraciones | Y oraciones |

### 3. Resultados del entrenamiento

- **Curvas de loss** (training y validation si aplica)
- **Métricas** relevantes al tipo de tarea
- **Ejemplos de salida** del modelo entrenado:
  - Traducción: 5 ejemplos input → output
  - Generación: 3 textos generados con diferentes prompts
  - Reformulación: 5 ejemplos
  - Clasificación: matriz de confusión o accuracy

### 4. Comparación con modelo pre-entrenado

- **Mismos inputs** para ambos modelos
- **Outputs de cada modelo** (side by side)
- **Análisis**:
  - ¿Cuál funciona mejor en cada caso?
  - ¿Cuándo entrenaste? ¿Cuánto entrenó el pre-entrenado?
  - ¿Merece la pena entrenar desde cero?

### 5. Preguntas de reflexión

Responde a las siguientes preguntas (incluye en el notebook o en un documento):

1. **¿Cuánto tardaste en entrenar el modelo desde cero?** ¿Cuántas horas/épocas?

2. **¿Cuánto tarda el modelo pre-entrenado en inferencia?** ¿Y tu modelo?

3. **¿En qué casos tu modelo entrenado desde cero podría ser mejor** que el pre-entrenado?

4. **¿Cuántos datos necesitas para entrenar desde cero** y que sea competitivo?

5. **¿Qué mejoras implementarías** si tuvieras más tiempo y recursos?

---

### 6. Preguntas específicas (especialmente para el ejemplo del Quijote)

Si has trabajado con el ejemplo de generación de texto estilo Quijote, responde también:

6. **¿Has usado el Quijote completo (`el_quijote.txt`)** o solo el archivo con frases reducidas (`mini_estilo_quijote.txt`)?

7. **¿Funciona mejor con el libro completo?** Justifica con datos (vocabulario, loss, calidad de los textos generados).

8. **¿Qué datos has tenido que ampliar desde internet?** ¿Has bajado más textos de Cervantes u otros autores del Siglo de Oro?

9. **¿Dónde has entrenado el modelo?**
   - [ ] En tu propio ordenador (especifica specs si puedes: RAM, GPU, etc.)
   - [ ] En Google Colab (¿con GPU gratuita o Pro?)
   - [ ] En Kaggle (con GPU)
   - [ ] Otro (especificar)

10. **¿Cuánto tiempo ha tardado el entrenamiento?** (aproximado)

11. **¿Has tenido que optimizar algo** (reducir batch size, epochs, etc.) por limitaciones de hardware?

12. **¿Qué limitaciones has encontrado?** ¿Cómo las has resuelto?

---

## Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Ampliación significativa del vocabulario | 2 |
| Código funcional y reproducible | 2 |
| Entrenamiento con buenos resultados | 2 |
| Comparación detallada con pre-entrenado | 2 |
| Reflexión y análisis crítico | 1 |
| Documentación clara | 1 |
| **Total** | **10** |

---

## Nota sobre el Quijote completo

Dispones del archivo `el_quijote.txt` con el texto completo. Se valorará especialmente si:

- Comparas resultados usando solo `mini_estilo_quijote.txt` vs `el_quijote.txt`
- Investigas a partir de qué cantidad de texto el modelo deja de mejorar significativamente
- Has tenido que ampliar los datos desde internet (indicar fuente)
- Documentas las limitaciones de hardware encontradas (y cómo las has resuelto)

---

## Estructura sugerida del repositorio/notebook

```
proyecto/
├── datos/                    # Datos originales y ampliados
├── modelos/                  # Modelos guardados (.pt)
├── notebooks/
│   └── experimento.ipynb    # Notebook principal
├── src/
│   ├── transformer.py       # Código del transformer (modificado)
│   └── train.py             # Script de entrenamiento
├── informe.md               # Documentación y reflexión
└── README.md                # Instrucciones de uso
```

---

## Consejos

- **Empezar pronto**: el entrenamiento puede tardar horas
- **Guardar checkpoints**: no perder el progreso
- **GPU**: usar GPU si es posible (verificar con `torch.cuda.is_available()`)
- **Comentar el código**: explicar qué hace cada parte
- **Ser crítico**: no todo lo pre-entrenado es mejor, ¡demuéstralo!

---

## Dudas

Para dudas sobre la tarea, consultar por email o en clase.
