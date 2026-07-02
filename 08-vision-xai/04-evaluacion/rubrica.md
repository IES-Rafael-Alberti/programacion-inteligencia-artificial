# Rúbrica — UD8 Visión por Computadora y XAI

Rúbrica sobre 10 puntos para entregas prácticas de la unidad. Ajustar si el enunciado concreto limita el alcance a uno o dos bloques temáticos.

## Escala de desempeño

| Nivel | Referencia |
| --- | --- |
| Insuficiente | No cumple el criterio o no hay evidencia verificable. |
| Básico | Cumple parcialmente, con errores o sin justificación suficiente. |
| Adecuado | Cumple de forma correcta y revisable. |
| Excelente | Cumple con solidez, visualizaciones claras y análisis bien argumentado. |

## Criterios

| Criterio | Peso |
| --- | ---: |
| 1. Funcionamiento e implementación | 2,0 |
| 2. Métricas cuantitativas | 2,0 |
| 3. Visualizaciones y evidencias visuales | 2,0 |
| 4. Análisis e interpretación de resultados | 2,0 |
| 5. Documentación y reproducibilidad | 2,0 |
| **Total** | **10,0** |

---

## 1. Funcionamiento e implementación — 2,0 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | El notebook no ejecuta o falta la parte principal de la entrega. |
| Básico | Ejecuta parcialmente o requiere correcciones manuales importantes para obtener resultados. |
| Adecuado | El flujo principal ejecuta sin errores críticos con el dataset o las imágenes de prueba indicadas. |
| Excelente | Ejecuta de forma robusta, maneja correctamente las dependencias y contempla casos límite o variaciones. |

**Indicadores por bloque:**
- *Segmentación*: U-Net o Mask R-CNN entrena y predice máscaras sobre imágenes.
- *Tracking*: YOLOv8 o SORT procesa el vídeo o secuencia de fotogramas y produce trayectorias.
- *XAI*: LIME, SHAP o Grad-CAM genera explicaciones sobre el modelo y los datos indicados.

---

## 2. Métricas cuantitativas — 2,0 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No se calculan métricas o los valores son claramente incorrectos. |
| Básico | Se calculan métricas, pero con errores de implementación o sin interpretar su significado. |
| Adecuado | Las métricas están bien calculadas, se presentan en tabla o texto y se comentan brevemente. |
| Excelente | Se comparan métricas entre configuraciones, modelos o umbrales y se razona sobre diferencias. |

**Métricas esperadas por bloque:**
- *Segmentación*: IoU (Intersection over Union) y Dice Score.
- *Tracking*: MOTA (Multiple Object Tracking Accuracy) y MOTP (Multiple Object Tracking Precision).
- *XAI*: importancias SHAP, pesos LIME o intensidades Grad-CAM con coherencia respecto al modelo.

---

## 3. Visualizaciones y evidencias visuales — 2,0 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay visualizaciones o no permiten revisar los resultados. |
| Básico | Hay visualizaciones, pero son poco legibles, están mal anotadas o no corresponden al problema. |
| Adecuado | Las visualizaciones muestran el resultado esperado de forma clara y referenciada. |
| Excelente | Las visualizaciones son informativas, incluyen anotaciones o leyendas y permiten comparar resultados. |

**Visualizaciones esperadas por bloque:**
- *Segmentación*: imagen original, máscara predicha y máscara real superpuestas.
- *Tracking*: fotograma con bounding boxes, identificadores de trayectoria y trazas de movimiento.
- *XAI*: mapa de calor Grad-CAM, gráfico de barras de importancias SHAP o highlight de tokens LIME.

---

## 4. Análisis e interpretación de resultados — 2,0 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay reflexión sobre los resultados o el análisis está copiado sin comprensión. |
| Básico | Se describe superficialmente qué se ha obtenido, sin conectar con conceptos de la unidad. |
| Adecuado | Se comenta qué funciona bien, qué falla y se relaciona con el funcionamiento del modelo o los datos. |
| Excelente | El análisis identifica causas de errores, compara variantes y propone mejoras concretas y razonadas. |

**Aspectos a analizar por bloque:**
- *Segmentación*: zonas donde falla la máscara, efecto del umbral, comparación entre modelos.
- *Tracking*: identidad swap, oclusiones, degradación de métricas en secuencias densas.
- *XAI*: coherencia entre importancias y dominio del problema; limitaciones del método de explicación usado.

---

## 5. Documentación y reproducibilidad — 2,0 puntos

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | Faltan instrucciones; no es posible reproducir sin conocimiento previo del autor. |
| Básico | Hay instrucciones mínimas, pero incompletas o con rutas absolutas dependientes del entorno personal. |
| Adecuado | Se indica cómo ejecutar el notebook, qué datos se usan y cómo obtenerlos o dónde están. |
| Excelente | La documentación permite reproducción completa: entorno declarado, rutas relativas, pasos ordenados y advertencias sobre requisitos. |

---

## Nota sobre entregas parciales

Si el enunciado evalúa solo uno o dos bloques (por ejemplo, solo XAI), el profesorado puede redistribuir los pesos entre los cinco criterios manteniendo el total en 10. En ese caso, el criterio de métricas y el de visualizaciones se ponderan según las técnicas incluidas en la entrega.
