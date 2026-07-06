# Actividad crítica — Euromillones y límites del aprendizaje automático

Esta carpeta se conserva en UD4 como actividad crítica sobre redes recurrentes, evaluación honesta y límites del aprendizaje automático. No debe presentarse como una práctica para “predecir la lotería”, sino como un caso deliberadamente problemático para analizar qué ocurre cuando se aplica un modelo potente a un proceso dominado por azar.

## Camino rápido

1. Revisar los notebooks y scripts como material histórico de experimentación.
2. Ejecutar sólo si el profesorado quiere trabajar la crítica metodológica.
3. Comparar resultados de entrenamiento y validación.
4. Concluir por qué una LSTM puede ajustar patrones aparentes sin obtener capacidad predictiva real.

## Qué se aprende

| Eje | Idea clave |
|---|---|
| Azar frente a patrón | No todo histórico temporal contiene señal útil. |
| Sobreajuste | Un modelo puede mejorar en entrenamiento sin generalizar. |
| Métricas | La métrica debe tener sentido para el problema; `accuracy` puede inducir a error. |
| Validación temporal | En secuencias, la separación debe respetar el orden temporal. |
| Responsabilidad | No se deben vender predicciones donde sólo hay ajuste retrospectivo. |

## Material incluido

```text
euromillones/
├── notebooks/
│   ├── euromPytorch.ipynb
│   ├── euromill-boosting.ipynb
│   ├── euromill-premio.ipynb
│   └── euromillions-3.ipynb
├── scripts/
│   ├── LSTM-euromillions.py
│   ├── LSTM_PytorchMultiVariate.py
│   └── LSTM_PytorchUniVariate.py
└── data/                  # datos locales no versionados por defecto
```

Los CSV de `data/` pueden existir en la copia local, pero no forman parte del material versionado por la regla global de ignorar `*.csv`. Si se usa en clase, el profesorado debe proporcionar el dataset por Moodle, aula virtual o una fuente controlada.

## Uso docente recomendado

Usar esta actividad como debate guiado:

1. ¿Qué hipótesis está haciendo el modelo?
2. ¿Hay una razón estadística para esperar patrón predictivo?
3. ¿Qué diferencia hay entre ajustar el pasado y predecir el futuro?
4. ¿Qué métrica sería honesta para evaluar el experimento?
5. ¿Cómo comunicarías el resultado sin crear falsas expectativas?

## Señales de alerta

- No interpretar una predicción numérica como recomendación real de apuesta.
- No usar el histórico completo para escalar o preparar datos antes de separar entrenamiento y validación.
- No confundir pérdida baja en entrenamiento con capacidad predictiva.
- No presentar resultados sin comparar contra una línea base aleatoria o ingenua.

## Decisión de saneamiento

La carpeta se mantiene en UD4 porque permite discutir redes recurrentes, sobreajuste y validación temporal desde un caso llamativo. Queda fuera del itinerario canónico salvo que el profesorado quiera trabajar explícitamente pensamiento crítico sobre ML.
