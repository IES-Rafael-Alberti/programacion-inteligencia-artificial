# Banco de Ejemplos de Proyecto Final — PIA

## Para qué sirve este documento

Este banco de ejemplos ayuda al alumnado a elegir un proyecto final viable, suficientemente ambicioso y conectado con los resultados del módulo.

Los ejemplos no son enunciados cerrados. Son **familias de proyecto** que cada equipo debe adaptar con sus propias fuentes de datos, decisiones técnicas y alcance.

## Regla común para todos los proyectos

Todo proyecto debe cumplir:

- [ ] al menos dos fuentes de datos diferenciadas;
- [ ] integración real entre fuentes;
- [ ] limpieza, curación o transformación;
- [ ] componente IA/ML justificable;
- [ ] salida útil: API, dashboard, informe, asistente, ranking, recomendador, alerta, etc.;
- [ ] documentación y defensa oral.

## Ejemplos recomendados

### 1. Estrategia para videojuegos multijugador

**Idea**: analizar partidas, personajes, mapas y resultados para recomendar estrategias de equipo.

| Elemento | Ejemplo |
|---|---|
| Fuente 1 | Historial de partidas o estadísticas públicas |
| Fuente 2 | Datos de mapas, personajes, armas, roles o parches |
| Integración | Relacionar composición de equipo + mapa + resultado |
| IA/ML posible | Clasificación de victoria/derrota, recomendador de composición, clustering de estilos |
| Salida útil | Recomendador de estrategia o informe de fortalezas/debilidades |

**Versión mínima válida**: recomendar composiciones de equipo según mapa y estadísticas históricas.

**Ampliación**: detectar cambios tras parches o proponer rutas de ataque/defensa.

**Riesgo**: quedarse en gráficas descriptivas sin modelo ni recomendación.

### 2. Jugadores infravalorados en deporte

**Idea**: detectar jugadores con rendimiento alto respecto a salario, valor de mercado o minutos jugados.

| Elemento | Ejemplo |
|---|---|
| Fuente 1 | Estadísticas deportivas: goles, asistencias, defensa, minutos, eficiencia |
| Fuente 2 | Salarios, valor de mercado, edad, lesiones, posición |
| Integración | Comparar rendimiento real frente a coste o expectativa |
| IA/ML posible | Ranking, clustering, predicción de rendimiento, detección de outliers |
| Salida útil | Ranking de jugadores infravalorados y justificación |

**Versión mínima válida**: ranking razonado con métrica compuesta y explicación.

**Ampliación**: añadir predicción de evolución o riesgo de lesión.

**Riesgo**: copiar estadísticas sin definir una métrica propia.

### 3. Aparcamiento inteligente

**Idea**: gestionar entradas/salidas, matrículas, tarifas, ocupación y posibles incidencias.

| Elemento | Ejemplo |
|---|---|
| Fuente 1 | Registros de entrada/salida o matrículas |
| Fuente 2 | Tarifas, ocupación, abonos, incidencias o calendario |
| Integración | Relacionar vehículo + estancia + tarifa + ocupación |
| IA/ML posible | Predicción de ocupación, detección de anomalías, clasificación de incidencias |
| Salida útil | API de consulta, alerta de ocupación, facturación estimada, informe de uso |

**Versión mínima válida**: calcular estancia/facturación y predecir ocupación por franjas.

**Ampliación**: asistente sobre políticas del parking con indexación jerárquica.

**Riesgo**: limitarse a reconocer matrículas sin integrar negocio ni datos adicionales.

### 4. Recomendador de recursos educativos

**Idea**: recomendar materiales de refuerzo a estudiantes según progreso, entregas o resultados.

| Elemento | Ejemplo |
|---|---|
| Fuente 1 | Calificaciones, entregas o asistencia |
| Fuente 2 | Catálogo de recursos, dificultad, etiquetas, tiempo estimado |
| Integración | Relacionar necesidad del estudiante con recurso adecuado |
| IA/ML posible | Recomendador, clasificación de riesgo, clustering de perfiles |
| Salida útil | Informe docente o recomendador para alumnado |

**Versión mínima válida**: clasificar necesidades y recomendar recursos justificados.

**Ampliación**: asistente que explique por qué recomienda cada recurso.

**Riesgo**: usar datos sensibles sin anonimizar.

### 5. Predicción de demanda o precios

**Idea**: anticipar demanda, ocupación, ventas o precios en función de histórico y contexto.

| Elemento | Ejemplo |
|---|---|
| Fuente 1 | Histórico de ventas, reservas, demanda u ocupación |
| Fuente 2 | Calendario, festivos, clima, eventos, precios, promociones |
| Integración | Relacionar demanda con contexto externo |
| IA/ML posible | Series temporales, regresión, clasificación de picos, alertas |
| Salida útil | Predicción, alerta de demanda, recomendación de stock/precio |

**Versión mínima válida**: modelo baseline + comparación con variables externas.

**Ampliación**: API o dashboard de predicción por fecha.

**Riesgo**: predecir solo con histórico sin justificar variables externas.

### 6. Soporte e incidencias

**Idea**: clasificar, priorizar o enrutar tickets de soporte combinando texto y metadatos.

| Elemento | Ejemplo |
|---|---|
| Fuente 1 | Tickets o incidencias textuales |
| Fuente 2 | Logs, tiempos de resolución, base de conocimiento, usuarios, prioridad |
| Integración | Relacionar descripción + contexto + resolución histórica |
| IA/ML posible | Clasificación, priorización, recomendación de solución, RAG |
| Salida útil | API de clasificación o asistente de soporte |

**Versión mínima válida**: clasificador de categoría/prioridad con evaluación.

**Ampliación**: asistente RAG que sugiera soluciones documentadas.

**Riesgo**: chatbot sin evaluación ni fuentes verificables.

### 7. Análisis de opiniones y reputación

**Idea**: analizar comentarios, reseñas o redes sociales para detectar temas, sentimiento y alertas.

| Elemento | Ejemplo |
|---|---|
| Fuente 1 | Reseñas, comentarios o publicaciones |
| Fuente 2 | Producto, fecha, categoría, ventas, incidencias o campañas |
| Integración | Relacionar opinión con producto, fecha o evento |
| IA/ML posible | Sentiment analysis, topic modeling, clasificación de urgencia |
| Salida útil | Dashboard de reputación o alertas de riesgo |

**Versión mínima válida**: clasificar sentimiento y explicar tendencias por categoría.

**Ampliación**: detectar temas emergentes y generar informe automático.

**Riesgo**: hacer nube de palabras sin análisis útil.

### 8. Servicios urbanos y datos abiertos

**Idea**: usar datos abiertos para detectar patrones, predecir necesidades o priorizar recursos.

| Elemento | Ejemplo |
|---|---|
| Fuente 1 | Datos abiertos: tráfico, incidencias, contaminación, transporte |
| Fuente 2 | Clima, calendario, eventos, población, geografía |
| Integración | Relacionar fenómeno urbano con contexto externo |
| IA/ML posible | Predicción, clustering geográfico, detección de anomalías |
| Salida útil | Mapa, ranking de zonas, alerta o informe de priorización |

**Versión mínima válida**: detectar zonas/patrones y justificar decisiones.

**Ampliación**: dashboard geográfico o API de consulta.
**Riesgo**: quedarse en visualizaciones sin modelo ni criterio de decisión.

## Ejemplos insuficientes y cómo mejorarlos

| Propuesta inicial | Problema | Cómo convertirla en válida |
|---|---|---|
| “Voy a analizar un dataset de Kaggle de fútbol” | Una sola fuente y análisis genérico | Añadir salarios/mercado, definir métrica de valor y crear ranking |
| “Haré un chatbot sobre cualquier tema” | No hay datos propios ni evaluación | Conectar a documentos reales, medir recuperación y limitar respuestas |
| “Dashboard de ventas” | Puede ser solo descriptivo | Añadir predicción de demanda o alertas de anomalías |
| “Clasificador de imágenes descargadas” | Puede ser copia de tutorial | Añadir segunda fuente, caso de uso, evaluación y salida útil |
| “Datos de videojuegos y gráficos” | Falta objetivo IA/ML | Predecir victoria, recomendar composición o detectar estrategias |
| “Reconocer matrículas” | Técnica aislada | Integrar tarifas, ocupación, abonos y facturación |

## Cómo usar proyectos de años anteriores

Los proyectos de años anteriores pueden usarse como referencia, pero conviene presentarlos de forma crítica:

| Tipo de referencia | Uso recomendado |
|---|---|
| Proyecto muy bueno | Mostrar como ejemplo de integración y defensa |
| Proyecto correcto | Mostrar qué cumple y qué podría mejorar |
| Proyecto flojo | Usarlo como caso de mejora: qué faltaba y cómo reforzarlo |

Se recomienda anonimizar nombres de estudiantes y centrarse en decisiones técnicas, no en calificaciones.

## Plantilla rápida para proponer un proyecto

```text
Título:
Problema:
Usuarios o destinatarios:
Fuente de datos 1:
Fuente de datos 2:
Cómo se integran las fuentes:
Componente IA/ML previsto:
Salida útil prevista:
Versión mínima viable:
Riesgos principales:
```

## Criterio docente

Una propuesta debe responder claramente a esta pregunta:

> ¿Qué decisión, recomendación, predicción o automatización será mejor gracias a integrar varias fuentes de datos y aplicar IA/ML?

Si no puede responderse, la propuesta todavía no está preparada.
