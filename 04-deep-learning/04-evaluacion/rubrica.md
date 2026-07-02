# Rúbrica consolidada — UD4 Deep Learning

Rúbrica sobre 10 puntos que pondera los tres laboratorios según su peso en la unidad. Para el detalle de cada criterio dentro de un lab concreto, consultar la rúbrica específica en su carpeta.

## Pesos y puntuación máxima por laboratorio

| Laboratorio | Peso | Puntos máximos |
| --- | ---: | ---: |
| Lab 1 — TF Playground | 25 % | 2,5 |
| Lab 2 — Backpropagation | 30 % | 3,0 |
| Lab 3 — Playground → código real | 45 % | 4,5 |
| **Total** | **100 %** | **10,0** |

## Escala de desempeño

| Nivel | Referencia |
| --- | --- |
| Insuficiente | No cumple el criterio o no hay evidencia verificable. |
| Básico | Cumple parcialmente, con errores o sin justificación suficiente. |
| Adecuado | Cumple de forma correcta y revisable. |
| Excelente | Cumple con solidez, razonamiento técnico claro y análisis bien argumentado. |

---

## Laboratorio 1 — TF Playground (2,5 puntos)

### L1.1 Diseño experimental — 0,75 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No experimenta o realiza cambios aleatorios sin documentar. |
| Básico | Varía algún parámetro pero sin sistemática ni justificación. |
| Adecuado | Experimenta de forma variada (capas, activaciones, learning rate) con registro de resultados. |
| Excelente | Diseño experimental sistemático, con hipótesis previas y conclusiones documentadas para cada variación. |

### L1.2 Interpretación de resultados — 0,875 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No interpreta los resultados o los describe de forma incorrecta. |
| Básico | Identifica algún fenómeno (convergencia o sobreajuste) de forma superficial. |
| Adecuado | Interpreta correctamente convergencia, sobreajuste y frontera de decisión con sus causas. |
| Excelente | Relaciona los fenómenos observados con el tamaño de la red, la función de activación y los datos usados. |

### L1.3 Relación con teoría — 0,625 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No conecta los experimentos con conceptos teóricos. |
| Básico | Menciona conceptos teóricos pero sin relacionarlos con los resultados observados. |
| Adecuado | Relaciona claramente experimentos con gradiente, activaciones y profundidad. |
| Excelente | Explica por qué ciertos comportamientos emergen de la interacción entre arquitectura, datos y optimización. |

### L1.4 Presentación — 0,25 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | El informe es ilegible, desordenado o incompleto. |
| Básico | Comprensible pero con estructura deficiente o capturas irrelevantes. |
| Adecuado | Documento claro, con capturas representativas y estructura coherente. |
| Excelente | Documento bien organizado, con anotaciones en capturas y conclusiones explícitas. |

---

## Laboratorio 2 — Backpropagation (3,0 puntos)

### L2.1 Identificación estructural del algoritmo — 0,9 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No identifica las partes del algoritmo o las confunde. |
| Básico | Identifica algunas partes (forward, pérdida) pero no el backward ni la actualización de pesos. |
| Adecuado | Identifica correctamente forward, cálculo de pérdida, backward y actualización, con explicación de cada paso. |
| Excelente | Explica con precisión cada parte y señala correspondencias con el código línea a línea. |

### L2.2 Relación código ↔ teoría — 0,9 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No establece ninguna relación entre el código y la teoría. |
| Básico | Menciona conceptos (gradiente, activación) pero sin anclarlos a fragmentos concretos del código. |
| Adecuado | Relaciona cada fragmento relevante con su concepto teórico (regla de la cadena, función de activación, etc.). |
| Excelente | La relación es bidireccional: explica también cómo la teoría condiciona las decisiones de implementación. |

### L2.3 Análisis crítico y reflexión — 0,75 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay reflexión o se limita a describir sin opinar. |
| Básico | Reflexión superficial sobre alguna limitación del código scratch. |
| Adecuado | Reflexiona sobre limitaciones de escala, estabilidad numérica o diferencias con frameworks modernos. |
| Excelente | Argumenta con criterio técnico por qué los frameworks automatizan la diferenciación y qué se gana o pierde respecto a la implementación manual. |

### L2.4 Claridad y rigor técnico — 0,45 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | El documento es confuso, con errores técnicos graves. |
| Básico | Comprensible pero con imprecisiones terminológicas o errores menores. |
| Adecuado | Documento técnicamente correcto, estructurado y con terminología precisa. |
| Excelente | Exposición rigurosa y precisa, con notas o referencias a fórmulas cuando aportan claridad. |

---

## Laboratorio 3 — De Playground a código real (4,5 puntos)

### L3.1 Implementación funcional — 1,35 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | El modelo no implementa, no entrena o no produce salida. |
| Básico | Ejecuta parcialmente o con errores que distorsionan los resultados. |
| Adecuado | Modelo correctamente implementado y entrenado con el framework indicado, reproducible. |
| Excelente | Implementación robusta, bien estructurada, con manejo de dependencias y reproducibilidad garantizada. |

### L3.2 Visualización y análisis — 1,125 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay visualizaciones útiles o no corresponden al modelo entrenado. |
| Básico | Visualizaciones presentes pero poco legibles o sin interpretación. |
| Adecuado | Visualiza correctamente la curva de pérdida y la frontera de decisión, con interpretación básica. |
| Excelente | Las visualizaciones están anotadas, permiten identificar fenómenos concretos (sobreajuste, underfitting, plateau) y se explican sus causas. |

### L3.3 Experimentación y comparación — 1,125 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No hay comparación entre configuraciones. |
| Básico | Compara dos configuraciones pero sin criterio técnico o sobre métricas inconsistentes. |
| Adecuado | Compara profundidad, activaciones u otros hiperparámetros y explica las diferencias observadas. |
| Excelente | La comparación es sistemática, incluye tabla de resultados y razona qué configuración es mejor y por qué para el problema dado. |

### L3.4 Conexión conceptual — 0,45 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | No conecta los resultados con conceptos de backpropagation ni de la superficie de pérdida. |
| Básico | Mención superficial a conceptos del curso. |
| Adecuado | Relaciona los resultados prácticos con backpropagation, superficie de pérdida y capacidad de representación. |
| Excelente | La conexión es explícita y enriquece el análisis con referencias concretas a conceptos trabajados en el taller. |

### L3.5 Calidad técnica — 0,45 pts

| Nivel | Evidencias observables |
| --- | --- |
| Insuficiente | Código desordenado, sin comentarios y difícil de seguir. |
| Básico | Código funcional pero con estructura poco clara o sin documentación mínima. |
| Adecuado | Código limpio, estructurado y con comentarios suficientes para revisar la lógica. |
| Excelente | Código idiomático, con funciones bien delimitadas, nombres descriptivos y documentación que facilita la reproducción. |
