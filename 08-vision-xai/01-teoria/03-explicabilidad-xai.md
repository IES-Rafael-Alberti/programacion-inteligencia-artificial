# Explicabilidad en IA: LIME, SHAP y Grad-CAM

## ¿Por qué necesitamos XAI?

Los modelos de deep learning son a menudo **cajas negras**: toman decisiones precisas pero no explican cómo. En aplicaciones críticas (medicina, finanzas, justicia) no basta con un resultado correcto — hace falta entender por qué.

La **IA Explicable (XAI)** agrupa técnicas que intentan abrir esas cajas negras. Se distinguen dos enfoques:

- **Métodos intrínsecos**: modelos interpretables por diseño (regresión lineal, árboles de decisión pequeños).
- **Métodos post-hoc**: se aplican después del entrenamiento para explicar modelos ya entrenados.

Dentro de los post-hoc se distingue entre:

- **Explicaciones globales**: qué aprende el modelo en conjunto (qué variables son más importantes).
- **Explicaciones locales**: por qué el modelo tomó una decisión concreta para una instancia específica.

## LIME

LIME (Local Interpretable Model-agnostic Explanations) genera explicaciones locales para cualquier modelo:

1. **Muestreo**: crea versiones perturbadas de la instancia a explicar.
2. **Predicción**: obtiene la predicción del modelo original para cada versión perturbada.
3. **Pesado**: asigna mayor peso a las muestras más cercanas a la instancia original.
4. **Modelo sustituto**: entrena un modelo interpretable (regresión lineal ponderada) sobre las muestras perturbadas.
5. **Explicación**: los coeficientes del modelo sustituto indican qué features contribuyen más a la decisión.

LIME es **agnóstico al modelo** — funciona con cualquier clasificador. Pero las explicaciones pueden ser inestables: pequeñas variaciones en la entrada producen explicaciones distintas.

## SHAP

SHAP (SHapley Additive exPlanations) usa teoría de juegos para asignar a cada feature su contribución a la predicción:

1. Calcula el **valor de Shapley** para cada feature: la contribución marginal promedio considerando todas las combinaciones posibles de features.
2. La suma de los valores SHAP de todas las features más el valor base (predicción media) da la predicción final.

SHAP proporciona explicaciones **consistentes** y con **base teórica sólida**. Las visualizaciones más habituales son:

- **summary_plot**: importancia global de features.
- **force_plot**: contribución local para una instancia.
- **dependence_plot**: cómo varía el impacto de una feature con su valor.

SHAP es más costoso computacionalmente que LIME, pero ofrece explicaciones más estables y fiables. Existen versiones optimizadas para árboles (TreeSHAP) y deep learning (DeepSHAP).

## Grad-CAM

Grad-CAM (Gradient-weighted Class Activation Mapping) visualiza las regiones de una imagen que más activan la decisión de una CNN:

1. Obtiene el gradiente de la clase predicha respecto a los mapas de activación de la última capa convolucional.
2. Calcula pesos promediando los gradientes globalmente.
3. Combina los mapas de activación ponderados por esos pesos.
4. Aplica una función ReLU para quedarse solo con las regiones que tienen influencia positiva.
5. Redimensiona el mapa de calor al tamaño de la imagen original y lo superpone.

Grad-CAM funciona con cualquier CNN que tenga capas convolucionales. Es útil para depurar modelos de visión: si el mapa de calor no se alinea con el objeto que debería clasificar, el modelo está aprendiendo patrones espurios.

## Limitaciones de XAI

Ninguna técnica de XAI es perfecta:

- **LIME**: explicaciones inestables, sensible al muestreo.
- **SHAP**: coste computacional alto en modelos complejos.
- **Grad-CAM**: solo accede a la última capa convolucional; no explica capas completamente conectadas.

Todas comparten el riesgo de **sobreinterpretación**: una explicación visualmente atractiva no implica que el modelo sea correcto o justo.

## Referencias

- [LIME: "Why Should I Trust You?"](https://arxiv.org/abs/1602.04938)
- [SHAP: A Unified Approach to Interpret Model Predictions](https://arxiv.org/abs/1705.07874)
- [Grad-CAM: Visual Explanations from Deep Networks](https://arxiv.org/abs/1610.02391)
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/)
