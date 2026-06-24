# Tarea: Portar Transformer a otra librería - Instrucciones de Entrega

## Fecha de entrega

**Consultar fecha límite en plataforma del centro.**

---

## Formato de entrega

Se puede entregar:

1. **Notebook Jupyter** (`.ipynb`) con código y ejecución
2. **Script Python** (`.py`) + **informe** (PDF o Markdown)
3. **Repositorio GitHub/GitLab**

---

## Contenido obligatorio

### 1. Código

- Implementación del Transformer en la librería elegida
- Código de entrenamiento funcional
- Código de inferencia/generación
- Ambos códigos deben poder ejecutarse sin errores

### 2. Documentación técnica

Explicar brevemente:

- **Arquitectura**: Diagrama o esquema del modelo
- **Componentes**: Descripción de cada clase/capa principal
- **Diferencias** con la implementación original de PyTorch

### 3. Comparación

Incluir una tabla comparativa:

| Aspecto | PyTorch original | Nueva librería |
|---------|------------------|---------------|
| Vocabulario usado | ... | ... |
| d_model | ... | ... |
| num_heads | ... | ... |
| num_layers | ... | ... |
| Tiempo/epoch | ... | ... |
| Memoria GPU | ... | ... |

### 4. Ejemplos de ejecución

Mostrar al menos 5 ejemplos de entrada/salida del modelo portado.

### 5. Reflexión personal

Responde:

1. **¿Qué librería has elegido? ¿Por qué?**

2. **¿Qué ha sido lo más difícil del portado?**

3. **¿Qué ventajas tiene la nueva librería sobre PyTorch?**

4. **¿Qué desventajas?**

5. **¿Recomendarías usar esta librería para transformers? ¿Cuándo?**

6. **¿Has usado IA generativa para ayudarte? ¿Cómo?** (ChatGPT, Copilot, etc. - no es trampa, se valora la honestidad)

---

## Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Implementación funcional del Transformer | 3 |
| Código limpio y documentado | 2 |
| Comparación técnica detallada | 2 |
| Reflexión personal honesta | 2 |
| Ejecución sin errores | 1 |
| **Total** | **10** |

---

## Requisitos técnicos

- El modelo debe poder entrenar
- Debe funcionar en GPU si está disponible
- Debe poder generar/predzir con nuevos inputs
- No es necesario que los resultados sean perfectos, pero sí que el código funcione

---

## Estructura sugerida

```
proyecto/
├── src/
│   ├── transformer_keras.py    # Si elegiste Keras
│   ├── transformer_flax.py      # Si elegiste Flax
│   ├── transformer_lightning.py # Si elegiste Lightning
│   └── train.py                # Script de entrenamiento
├── notebooks/
│   └── demo.ipynb              # Notebook con ejemplos
├── datos/                      # Datos usados (link o copia)
├── informe.md                  # Documentación
└── README.md                  # Instrucciones
```

---

## Consejos

- **Empezar por el esqueleto** proporcionado en `Tarea-Transformer-Portado.md`
- **Probar componente a componente** antes de集成 todo
- **Usar los mismos datos** que en el ejemplo original para comparar
- **No complicarse**: una implementación simple pero funcional vale más que una compleja que no funciona
- **Documentar mientras se programa**: después no te acordarás

---

## Dudas

Consultar por email o en clase.
