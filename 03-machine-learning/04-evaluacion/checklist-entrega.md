# Checklist de entrega — UD3 Machine Learning

Usa esta lista antes de entregar. El profesorado indica cuál o cuáles de las prácticas son evaluables en cada momento.

## Imprescindible (todas las prácticas)

- [ ] El fichero entregado coincide con la práctica indicada.
- [ ] El trabajo es propio y se declara el uso de IA si se ha utilizado.
- [ ] No se entregan claves API, tokens, contraseñas ni credenciales reales.
- [ ] Se incluyen instrucciones o contexto suficiente para revisar el trabajo.

---


## Laboratorios de creación de dataset (Lab1, Lab2, Lab3)

**Enunciados:** `03-practicas/laboratorios/Lab1/`, `Lab2/`, `Lab3/`
**Rúbrica:** `04-evaluacion/rubrica_datasets_peliculas.md`

- [ ] El notebook o script crea el dataset correctamente con la fuente indicada (TheMovieDB, OpenMeteo/AEMET, o fuente propia).
- [ ] El dataset resultante tiene las columnas y el número de registros mínimos indicados en el enunciado.
- [ ] Se documenta el proceso de obtención: objetivo, API usada, parámetros, transformaciones, limpieza aplicada y limitaciones (trazabilidad CRISP-DM mínima).
- [ ] Se incluye al menos una visualización o análisis exploratorio básico del dataset generado.
- [ ] El código está limpio, comentado y ejecuta sin errores críticos.
- [ ] No se incluyen claves API en el notebook; se usan variables de entorno o fichero `.env.example`.

---

## Midterm Capstone — Películas (EDA + PyCaret + modelo final)

**Enunciado:** `03-practicas/midterm-capstone/`
**Rúbrica:** `04-evaluacion/RubricaPeliculas.md`

- [ ] El notebook ejecuta el flujo completo: carga → EDA → preprocesado → PyCaret → modelo final.
- [ ] El EDA incluye análisis de distribuciones, valores nulos y relaciones entre variables relevantes.
- [ ] PyCaret está configurado correctamente con la tarea indicada (clasificación o regresión).
- [ ] Se comparan al menos dos modelos y se selecciona el candidato mediante validación cruzada o un conjunto de validación dentro de entrenamiento; el conjunto de test queda reservado para una única evaluación final.
- [ ] La separación train/test se realiza antes de ajustar imputadores, escaladores, codificadores o selectores; el conjunto de test no se usa para `fit`.
- [ ] El modelo final está justificado con criterio técnico (no solo por ser el de mayor métrica).
- [ ] Las visualizaciones son legibles y tienen título o descripción.
- [ ] El informe explica las decisiones tomadas y los resultados obtenidos.

---

## Tarea Bank Marketing (Tarea07 o Tarea08)

**Enunciado:** `03-practicas/tarea07/` o `03-practicas/tarea08/`
**Cuestionario:** `04-evaluacion/Cuestionario-Bank-Marketing.gift`

- [ ] Se responden todas las preguntas del enunciado con argumentación técnica.
- [ ] Se usa el dataset Bank Marketing indicado, sin sustituirlo por otro.
- [ ] La selección y el ajuste del modelo se realizan mediante validación cruzada o un conjunto de validación dentro de entrenamiento; el conjunto de test queda reservado para una única evaluación final.
- [ ] La selección del modelo está justificada con las métricas de validación y el objetivo (no solo "tiene mejor accuracy").
- [ ] El análisis de variables/características está documentado.

---

## Comprobaciones finales (todas las prácticas)

- [ ] He revisado la rúbrica correspondiente antes de entregar.
- [ ] El notebook ejecuta desde cero (kernel reiniciado) sin errores críticos.
- [ ] Las rutas de archivos son relativas o están documentadas.
- [ ] Los errores conocidos o limitaciones están documentados brevemente.
- [ ] El trabajo puede revisarse sin acceder a recursos externos no indicados.

## Formato de entrega

- Según las instrucciones del profesorado: carpeta comprimida, repositorio o plataforma indicada.
- Incluir solo los archivos necesarios; no subir datasets completos si son de gran tamaño.
- Usar nombres de archivo claros que identifiquen la práctica.
