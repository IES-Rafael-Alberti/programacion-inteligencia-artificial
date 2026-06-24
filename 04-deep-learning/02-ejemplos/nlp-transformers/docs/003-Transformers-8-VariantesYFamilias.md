---
title: "Transformers 8: Variantes y Familias de Arquitecturas"
output:
  html_document:
    toc: true
    toc_depth: 2
    toc_float: true
    number_sections: true
    fig_caption: true
    code_folding: hide
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true
    fig_caption: true
    latex_engine: xelatex
---


# Variantes y Familias de Arquitecturas Transformer

Hasta ahora hemos trabajado con el **Transformer original**, es decir, con el mecanismo de **atención completa** (*full attention*), donde cada token puede atender a todos los demás tokens de la secuencia.

Ese diseño es muy potente, pero tiene un coste importante:

* requiere mucha memoria,
* necesita muchos cálculos,
* y se vuelve poco práctico cuando la secuencia es muy larga.

Por eso, a partir de la arquitectura original han surgido muchas variantes. Algunas intentan **aligerar la atención**, otras **aumentar el contexto**, otras **hacer crecer la capacidad del modelo sin activar toda la red a la vez**, y otras combinan varias ideas.

Este documento ofrece una visión general, agrupando las variantes por **familias**.

---

## 1. Punto de partida: el Transformer original

En el Transformer clásico:

* cada token se compara con todos los demás,
* la matriz de atención es completa,
* el coste crece aproximadamente como `O(n²)` con la longitud de la secuencia.

### ¿Qué se consigue?

* Muy buena capacidad para capturar relaciones complejas.
* Gran flexibilidad para traducción, generación, clasificación, resumen, etc.

### ¿Cuál es el problema?

* Cuando `n` crece mucho, la memoria y el tiempo de cómputo crecen demasiado.
* Eso limita el tamaño del contexto.

---

## 2. Primera gran familia: atención local, dispersa o incompleta

La idea básica de esta familia es muy simple:

> En lugar de dejar que cada token mire a todos los demás, se restringe la atención a una parte de la secuencia.

Es decir, se pasa de una **atención completa** a una **atención parcial, local o dispersa**.

### ¿Qué cambian?

* Se eliminan muchas conexiones de atención.
* Un token ya no atiende a todos los demás, sino solo a algunos:
  * los cercanos,
  * unos pocos especiales,
  * o una mezcla de atención local y global.

### ¿Qué se consigue?

* Reducir el coste de memoria y cálculo.
* Trabajar con secuencias más largas.
* Mantener gran parte del contexto útil.

### ¿Qué se pierde?

* El modelo ya no tiene acceso directo a todas las relaciones posibles.
* Algunas dependencias lejanas pueden capturarse peor si el patrón de atención está muy restringido.

### Ejemplos típicos

#### Longformer

* Usa atención **local por ventanas** y añade algunos tokens con atención **global**.
* Está pensado para documentos largos.

**Qué añade:** atención local + global.  
**Qué elimina:** la atención completa entre todos los pares.  
**Qué consigue:** manejar textos largos con menos coste.

#### BigBird

* Combina atención local, atención aleatoria y atención global.

**Qué añade:** conexiones aleatorias además de las locales.  
**Qué consigue:** mejor cobertura del contexto con coste mucho menor que la atención completa.

#### Reformer

* Agrupa tokens mediante técnicas de *hashing* y evita comparar todos con todos.

**Qué cambia:** sustituye la atención completa por una versión aproximada.  
**Qué consigue:** menos memoria y más eficiencia en secuencias largas.

---

## 3. Segunda familia: atención aproximada, lineal o de bajo rango

Esta familia no siempre restringe la atención a posiciones concretas, sino que intenta **reformular matemáticamente** el cálculo para hacerlo más barato.

La idea general es:

> En vez de calcular exactamente toda la matriz de atención, se aproxima o se factoriza de una manera más eficiente.

### ¿Qué cambian?

* Se modifica la forma de calcular `QK^T`.
* A veces se aproxima la matriz de atención.
* A veces se proyectan `K` y `V` a espacios más pequeños.

### ¿Qué se consigue?

* Reducir complejidad y memoria.
* Hacer viable el uso de contextos más largos.

### ¿Qué se pierde?

* En algunos casos, se pierde precisión con respecto a la atención exacta.
* Algunas variantes son más difíciles de entender o de entrenar.

### Ejemplos típicos

#### Linformer

* Proyecta `K` y `V` a una dimensión menor.

**Qué elimina:** parte de la dimensionalidad original de la atención.  
**Qué consigue:** menos coste y menos memoria.

#### Performer

* Usa una aproximación matemática de la atención mediante funciones kernel.

**Qué cambia:** reemplaza la atención exacta por una aproximación lineal.  
**Qué consigue:** complejidad más baja y mejor escalado con secuencias largas.

#### Otras variantes lineales

Existen muchos modelos que siguen esta misma filosofía:

* no eliminar por completo la atención,
* pero sí calcularla de forma más ligera o aproximada.

La idea central siempre es la misma:

* menos coste,
* más contexto,
* a cambio de cierta simplificación.

---

## 4. Tercera familia: optimización de la atención sin cambiar la idea básica

Aquí la arquitectura sigue siendo, en esencia, la del Transformer original. No se elimina la atención completa, pero sí se intenta hacerla **más eficiente en la práctica**.

### ¿Qué cambian?

* No cambian tanto la teoría como la implementación.
* Se reorganizan cálculos y accesos a memoria.

### ¿Qué se consigue?

* Más velocidad.
* Menor uso de memoria.
* Posibilidad de usar secuencias mayores o lotes más grandes.

### Ejemplo típico

#### FlashAttention

* Calcula la atención exacta, pero de forma mucho más eficiente en GPU.

**Qué añade:** una implementación optimizada.  
**Qué elimina:** parte del coste práctico asociado a la memoria intermedia.  
**Qué consigue:** entrenar e inferir más rápido sin abandonar la atención exacta.

Es importante notar que **FlashAttention no cambia la lógica del Transformer**, sino la forma de ejecutarla.

### Otra línea cercana: compresión de la caché KV

En modelos autoregresivos grandes, otro cuello de botella importante no es solo el cálculo de atención, sino también la **memoria ocupada por la caché KV** (*key-value cache*).

Recordemos que, durante la generación:

* se guardan las claves `K` y los valores `V` de los tokens anteriores,
* esa memoria crece con la longitud del contexto,
* y puede llegar a limitar mucho el tamaño del contexto o el número de peticiones simultáneas.

Por eso han surgido métodos que no cambian la arquitectura base del Transformer, pero sí **cómo se almacenan `K` y `V`**.

#### TurboQuant

TurboQuant es una propuesta reciente de Google Research orientada a **comprimir fuertemente la caché KV** sin necesidad de reentrenar el modelo.

**Qué cambia:**

* no modifica la idea de atención del Transformer,
* pero sí la forma en que se almacenan los vectores de la caché KV,
* aplicando una cuantización muy agresiva para reducir memoria.

**Qué consigue:**

* reducir mucho el tamaño de la caché KV,
* permitir contextos mayores o más concurrencia,
* y acelerar parte del cálculo asociado a la atención en inferencia.

**Idea general, en palabras:**

* comprime los vectores de la caché para que ocupen muchos menos bits,
* intentando conservar las relaciones geométricas que la atención necesita para funcionar bien.

En otras palabras: no pretende cambiar qué hace el Transformer, sino **hacer más barata la memoria que necesita para seguir recordando el contexto anterior**.

Este tipo de técnicas es especialmente importante en modelos grandes de tipo decoder, donde la caché KV puede llegar a ser uno de los principales límites prácticos del sistema.

---

## 5. Cuarta familia: modelos con memoria o contexto extendido

Otra línea de variantes intenta resolver el problema del contexto largo no solo con una atención más barata, sino también con mecanismos que permitan **recordar información más allá del bloque actual**.

### ¿Qué cambian?

* Añaden mecanismos de memoria.
* Reutilizan estados anteriores.
* Procesan la secuencia en fragmentos enlazados.

### ¿Qué se consigue?

* Capturar dependencias más largas.
* Trabajar con textos extensos sin recalcular todo desde cero.

### ¿Qué se complica?

* La arquitectura deja de ser tan simple como el Transformer original.
* La gestión del contexto se vuelve más difícil de explicar e implementar.

### Ejemplos típicos

#### Transformer-XL

* Reutiliza representaciones de segmentos anteriores como memoria.

**Qué añade:** memoria entre segmentos.  
**Qué consigue:** contexto efectivo más largo.

#### Modelos con compresión o memoria externa

* Algunas variantes añaden módulos que resumen o almacenan información pasada.

**Qué añaden:** mecanismos externos de persistencia del contexto.  
**Qué consiguen:** extender la capacidad de “recordar” más allá de la ventana inmediata.

---

## 6. Quinta familia: Mixture of Experts (MoE)

Esta es una de las familias más importantes en modelos grandes actuales.

La idea principal es distinta de la anterior:

> En lugar de hacer el modelo más profundo o activar toda la red para todos los tokens, se añaden muchos submódulos especializados y solo se activan algunos en cada paso.

### ¿Qué cambian?

* La red *feed-forward* tradicional se sustituye o amplía con varios **expertos**.
* Un mecanismo de enrutamiento (*router*) decide qué expertos se activan para cada token.

### ¿Qué añade?

* Especialización interna.
* Enrutamiento dinámico.
* Mucha capacidad total sin usar toda la red a la vez.

### ¿Qué se consigue?

* Aumentar mucho el tamaño efectivo del modelo.
* Escalar la capacidad “en horizontal” más que “en vertical”.
* Mantener un coste por token más controlado que si toda la red estuviera activa siempre.

### ¿Qué se complica?

* El entrenamiento.
* El balance entre expertos.
* El enrutamiento y la estabilidad.

### Ejemplos típicos

#### Switch Transformer

* Usa un router que selecciona un experto principal por token.

**Qué añade:** expertos especializados y enrutamiento.  
**Qué consigue:** modelos mucho más grandes sin multiplicar el coste activo de cada paso.

#### GShard y otros MoE

* Distribuyen el trabajo entre múltiples expertos.

**Qué consiguen:** más capacidad y escalado en modelos enormes.

En resumen, los MoE no cambian sobre todo la atención, sino la **parte densa de la red**, especialmente la FFN.

---

## 7. Sexta familia: variaciones en la estructura general del Transformer

No todas las variantes se centran en la atención. Algunas cambian directamente la estructura global del modelo.

### Ejemplos de cambios posibles

* usar solo **encoder**,
* usar solo **decoder**,
* reorganizar capas,
* cambiar el tipo de normalización,
* modificar la FFN,
* añadir módulos multimodales.

### ¿Qué se consigue?

* adaptar la arquitectura a una tarea concreta,
* simplificar partes del modelo,
* o especializarlo para texto, visión, audio o tareas multimodales.

### Ejemplos conocidos

* **BERT**: solo encoder.
* **GPT**: solo decoder.
* **T5**: encoder-decoder, pero formulado como transformación de texto a texto.

Estas variantes no pretenden siempre reducir coste, sino **adaptar el Transformer a distintos usos**.

---

## 8. Resumen por familias

| Familia | Qué cambian | Qué consiguen | Coste o trade-off |
| ------- | ----------- | ------------- | ----------------- |
| Atención local o dispersa | Eliminan parte de las conexiones de atención | Más contexto y menos coste | Menor acceso directo a dependencias lejanas |
| Atención aproximada o lineal | Reformulan el cálculo de la atención | Más eficiencia | Posible pérdida de precisión |
| Optimización de implementación | Mejoran cómo se ejecuta la atención | Más velocidad y menos memoria | Menos cambio conceptual, más dependencia de implementación |
| Memoria o contexto extendido | Añaden mecanismos de memoria | Recordar más contexto | Arquitectura más compleja |
| Mixture of Experts | Activan solo parte de la red para cada token | Más capacidad total con coste controlado | Entrenamiento y enrutamiento más complejos |
| Variaciones estructurales | Cambian encoder, decoder o bloques internos | Mejor adaptación a tareas concretas | Depende de cada arquitectura |

---

## 9. Idea clave para recordar

Todas estas variantes nacen, en el fondo, de una misma necesidad:

* **hacer el modelo más eficiente,**
* **hacerlo más escalable,**
* **darle más contexto,**
* o **aumentar su capacidad sin disparar el coste**.

Dicho de otra forma:

* unas variantes **recortan** la atención,
* otras la **aproximan**,
* otras la **optimizan**,
* otras añaden **memoria**,
* y otras amplían la red mediante **expertos**.

Pero todas siguen partiendo de la idea central del Transformer: construir representaciones contextuales mediante mecanismos de atención.

---

## 10. Conclusión

No existe una única “mejor” variante del Transformer. La elección depende de lo que se quiera priorizar:

* **máxima calidad**,
* **más contexto**,
* **menos memoria**,
* **más velocidad**,
* o **más capacidad del modelo**.

Por eso es útil pensar en estas arquitecturas no como modelos aislados, sino como **familias de soluciones** a distintos problemas del Transformer original.

---
