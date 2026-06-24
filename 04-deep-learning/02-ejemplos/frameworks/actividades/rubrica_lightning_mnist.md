# Rúbrica corta · Lightning + CNN sobre MNIST

## Finalidad
Evaluar si el alumnado ha comprendido el uso básico de **PyTorch Lightning** para entrenar una CNN, modificar la arquitectura y comparar decisiones de entrenamiento.

## Criterios de evaluación

### 1. Arquitectura del modelo (0–3 puntos)
- **3 puntos**: modifica la arquitectura correctamente (por ejemplo, cambia filtros, añade capas o dropout) y ajusta bien las dimensiones.
- **2 puntos**: realiza cambios válidos, aunque simples o poco justificados.
- **1 punto**: intenta modificarla, pero con errores parciales o dependencia excesiva de copia.
- **0 puntos**: no modifica la arquitectura o la rompe.

### 2. Optimización e hiperparámetros (0–2 puntos)
- **2 puntos**: cambia optimizador y/o hiperparámetros con criterio y compara resultados.
- **1 punto**: hace cambios, pero sin apenas interpretación.
- **0 puntos**: no realiza pruebas o no entiende su efecto.

### 3. Uso de Lightning (0–2 puntos)
- **2 puntos**: comprende la estructura básica (`LightningModule`, `training_step`, `validation_step`, `configure_optimizers`, `Trainer`).
- **1 punto**: identifica algunas piezas, pero con comprensión parcial.
- **0 puntos**: no entiende el papel de Lightning.

### 4. Interpretación de resultados (0–2 puntos)
- **2 puntos**: analiza loss/accuracy y comenta si hay mejora, estancamiento u overfitting.
- **1 punto**: describe resultados de forma superficial.
- **0 puntos**: no interpreta las métricas.

### 5. Presentación y claridad (0–1 punto)
- **1 punto**: notebook ordenado, comentado y entendible.
- **0 puntos**: trabajo desordenado o difícil de revisar.

## Escala rápida
- **9–10**: muy buen dominio, modifica, compara y justifica bien.
- **7–8.9**: correcto y funcional, con alguna explicación limitada.
- **5–6.9**: suficiente, pero con comprensión parcial o poca justificación.
- **<5**: no alcanza lo mínimo esperado.

## Errores típicos a vigilar
- Cambiar capas y no ajustar la entrada de `fc1`.
- Cambiar optimizador sin revisar `lr`.
- Confundir `train_loss` con `val_loss`.
- Pensar que Lightning “entrena solo” sin entender la lógica del batch.
- No justificar por qué un modelo mejora o empeora.

## Observación para el profesor
Valorar especialmente la **comprensión** y la **capacidad de experimentación razonada**.  
No es necesario penalizar pequeñas diferencias de rendimiento si el proceso está bien explicado.
