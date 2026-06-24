# Datasets para visión y transfer learning

Este documento recoge varios datasets que podemos usar en clase o en proyectos para trabajar visión por computador, especialmente en tareas de clasificación y `transfer learning`.

La idea no es solo elegir un conjunto de imágenes, sino tener claro qué objetivo didáctico perseguimos con cada uno.

## Criterios de elección

Para actividades de aula conviene priorizar datasets que:

- tengan clases visualmente distinguibles
- no sean excesivamente grandes
- permitan obtener resultados razonables con modelos preentrenados
- no obliguen a dedicar demasiado tiempo a limpieza o preparación

Para proyectos más abiertos, en cambio, sí puede tener sentido usar datasets algo más complejos o menos estructurados.

## Datasets recomendados

## 1. Cats vs Dogs

- Tipo: clasificación binaria
- Nivel: inicial
- Descarga:
  [Microsoft PetImages](https://www.microsoft.com/en-us/download/details.aspx?id=54765)
- Objetivo docente:
  introducir el flujo completo de clasificación de imágenes con un problema muy intuitivo
- Qué trabajar con él:
  carga de imágenes, partición train/valid/test, primeras CNN, `transfer learning`
- Ventajas:
  muy fácil de entender, clases claras, motivador para empezar
- Limitación:
  al ser binario, se queda corto para discutir problemas multiclase

### Actividad recomendada

Entrenar primero una CNN sencilla y después comparar con `MobileNetV2` o `ResNet` preentrenadas.

## 2. Oxford Flowers 102

- Tipo: clasificación multiclase
- Nivel: intermedio
- Descarga:
  [Imágenes JPG](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz),
  [etiquetas](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat),
  [splits](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/setid.mat)
- Objetivo docente:
  mostrar un caso más realista de `transfer learning` con muchas clases y etiquetas externas
- Qué trabajar con él:
  uso de JPG con etiquetas en `.mat`, particiones oficiales, modelos preentrenados, evaluación multiclase
- Ventajas:
  muy adecuado para ver que no siempre existe una carpeta por clase
- Limitación:
  102 clases son muchas para un primer contacto si el alumnado aún no domina bien el flujo básico

### Actividad recomendada

Usar un modelo preentrenado y comparar dos formas de acceso a los datos:

- imágenes originales + `.mat`
- arrays preprocesados en `.npz`

## 3. Intel Image Classification

- Tipo: clasificación de escenas
- Nivel: inicial-intermedio
- Descarga:
  [Kaggle: Intel Image Classification](https://www.kaggle.com/datasets/puneet6060/intel-image-classification)
- Objetivo docente:
  trabajar clasificación multiclase con categorías comprensibles como `forest`, `sea`, `street` o `buildings`
- Qué trabajar con él:
  preprocesado, `transfer learning`, análisis de errores, confusión entre clases
- Ventajas:
  visualmente variado, útil para explicar que no siempre clasificamos objetos concretos sino escenas
- Limitación:
  algunas clases pueden solaparse visualmente

### Actividad recomendada

Comparar una CNN entrenada desde cero con un modelo preentrenado y analizar la matriz de confusión.

## 4. EuroSAT

- Tipo: clasificación de imágenes satelitales
- Nivel: intermedio
- Descarga:
  [GitHub oficial](https://github.com/phelber/EuroSAT),
  [Zenodo](https://zenodo.org/records/7711810)
- Objetivo docente:
  enseñar que visión por computador no se limita a fotos convencionales
- Qué trabajar con él:
  generalización, clasificación multiclase, aplicación a teledetección
- Ventajas:
  cambia el contexto habitual y amplía la idea de lo que puede hacer un modelo visual
- Limitación:
  requiere explicar brevemente el dominio para que las clases tengan sentido

### Actividad recomendada

Aplicar `transfer learning` y discutir hasta qué punto un modelo entrenado con imágenes generales puede reutilizarse en otro dominio.

## 5. Beans Dataset

- Tipo: clasificación de enfermedades en plantas
- Nivel: intermedio
- Descarga:
  [Repositorio oficial iBean](https://github.com/AI-Lab-Makerere/ibean/)
- Objetivo docente:
  conectar la clasificación visual con problemas reales en agricultura
- Qué trabajar con él:
  clasificación multiclase, `transfer learning`, impacto de los datos en aplicaciones reales
- Ventajas:
  dataset pequeño y manejable, con aplicación clara
- Limitación:
  menos intuitivo que gatos/perros para alumnado muy inicial

### Actividad recomendada

Comparar rendimiento entre imágenes sin aumento y con `data augmentation`.

## 6. Garbage / Waste Classification

- Tipo: clasificación multiclase
- Nivel: inicial-intermedio
- Descarga:
  [TrashNet (GitHub)](https://github.com/garythung/trashnet)
- Objetivo docente:
  plantear un problema cercano y con componente social o ambiental
- Qué trabajar con él:
  clasificación de objetos, `transfer learning`, despliegue sencillo de prototipos
- Ventajas:
  motiva bien y da pie a aplicaciones prácticas
- Limitación:
  muchos datasets de este tipo no están tan limpios como otros más académicos

### Actividad recomendada

Construir un clasificador de residuos y discutir errores que tendrían impacto en un sistema real.

## 7. Kather / tejidos histológicos

- Tipo: clasificación de imágenes médicas
- Nivel: intermedio-avanzado
- Descarga:
  [Kather texture 2016 en Zenodo](https://zenodo.org/records/53169)
- Objetivo docente:
  mostrar aplicaciones biomédicas de la visión por computador
- Qué trabajar con él:
  `transfer learning`, clasificación multiclase, limitaciones y responsabilidad en IA aplicada a salud
- Ventajas:
  muy buen ejemplo de aplicación real
- Limitación:
  requiere contexto adicional y conviene tratarlo con más cuidado que un dataset general

### Actividad recomendada

Usar un modelo preentrenado y discutir por qué un buen resultado en un dataset no equivale a un sistema médico listo para usar.

## 8. Fashion MNIST

- Tipo: clasificación sencilla
- Nivel: inicial
- Descarga:
  [Sitio oficial de Zalando Research](https://research.zalando.com/project/fashion_mnist/fashion_mnist/),
  [GitHub oficial](https://github.com/zalandoresearch/fashion-mnist)
- Objetivo docente:
  practicar rápido arquitecturas y métricas sin coste computacional alto
- Qué trabajar con él:
  primeras CNN, comparación de modelos, visualización de errores
- Ventajas:
  muy ligero y fácil de ejecutar
- Limitación:
  es demasiado simple para mostrar bien el valor del `transfer learning` en visión real

### Actividad recomendada

Usarlo como punto de partida para explicar CNN y pasar después a datasets en color y de mayor complejidad.

## Qué objetivo perseguimos con cada tipo de dataset

### Para introducir clasificación de imágenes

Datasets recomendados:

- Cats vs Dogs
- Fashion MNIST
- Intel Image Classification

Objetivo:
que el alumnado entienda el flujo básico de entrada, modelo, entrenamiento y evaluación.

### Para introducir transfer learning

Datasets recomendados:

- Oxford Flowers 102
- Intel Image Classification
- Beans Dataset
- Cats vs Dogs

Objetivo:
mostrar que reutilizar modelos preentrenados permite obtener mejores resultados más rápido y con menos datos.

### Para mostrar casos más realistas

Datasets recomendados:

- Oxford Flowers 102
- EuroSAT
- Kather
- Waste Classification

Objetivo:
salir del ejemplo “limpio” y enseñar que en problemas reales los datos pueden venir con metadatos, particiones oficiales o estructuras menos cómodas.

### Para proyectos finales

Datasets recomendados:

- Oxford Flowers 102
- Intel Image Classification
- EuroSAT
- Waste Classification
- Beans Dataset
- Kather

Objetivo:
permitir que el alumnado tome decisiones sobre preprocesado, modelo, métricas y presentación de resultados.

## Propuesta práctica para el aula

Una secuencia razonable podría ser esta:

1. Empezar con `Cats vs Dogs` o `Fashion MNIST` para fijar el flujo básico.
2. Pasar a `Oxford Flowers 102` para enseñar `transfer learning` con un dataset más realista.
3. Ofrecer `Intel`, `Beans`, `EuroSAT` o `Waste Classification` como base para proyectos.

## Recomendación final

Si hay que escoger pocos datasets y sacarles partido:

- Para empezar: `Cats vs Dogs`
- Para transfer learning en serio: `Oxford Flowers 102`
- Para proyecto aplicado: `Intel Image Classification` o `Waste Classification`
- Para un ejemplo más especializado: `EuroSAT` o `Kather`

Lo importante no es usar muchos datasets, sino usar pocos y que cada uno sirva para aprender algo distinto.
