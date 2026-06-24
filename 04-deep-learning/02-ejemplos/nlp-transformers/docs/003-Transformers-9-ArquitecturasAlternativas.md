---
title: "Arquitecturas Alternativas a Transformers"
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


# Arquitecturas Alternativas a Transformers

Los Transformers dominan gran parte del aprendizaje profundo actual en lenguaje, visión y modelos multimodales. Sin embargo, no son la única forma de procesar secuencias.

Han aparecido otras familias de arquitecturas que intentan resolver algunos de sus límites, sobre todo:

* el coste de memoria,
* el coste de la atención en secuencias largas,
* la dificultad para escalar el contexto,
* o la necesidad de modelos más ligeros y eficientes.

Este documento presenta una visión general de algunas arquitecturas **fuera de la familia Transformer**, con suficiente detalle para entender la idea general, pero sin entrar todavía en la profundidad matemática que veremos en otra unidad.

---

## 1. ¿Por qué buscar alternativas?

El Transformer original tiene muchas ventajas:

* procesa la secuencia en paralelo,
* capta bien dependencias largas,
* y se adapta muy bien a muchas tareas.

Pero también tiene costes:

* la atención completa puede ser cara,
* la memoria crece mucho con contextos largos,
* y en algunos entornos el modelo puede resultar excesivamente pesado.

Por eso se han explorado otras arquitecturas que intentan:

* modelar secuencias de otra manera,
* reducir el coste computacional,
* o representar el contexto sin depender totalmente de la atención.

---

## 2. Dos grandes ideas fuera de Transformers

Si simplificamos mucho, muchas alternativas modernas se apoyan en una de estas dos ideas:

### 2.1. Mantener un estado y actualizarlo

En lugar de comparar cada token con todos los demás, el modelo mantiene una especie de **memoria interna** o **estado** que se va actualizando con cada nuevo token.

Esta idea conecta con lo que ya conocemos de:

* RNN,
* GRU,
* LSTM.

La diferencia es que las arquitecturas modernas intentan hacerlo de forma más estable, más escalable o más eficiente.

### 2.2. Sustituir o reducir la atención

Otra posibilidad es no abandonar del todo la atención, pero sí:

* usarla solo en algunos bloques,
* combinarla con otros mecanismos,
* o reemplazar parte de su función por dinámicas más baratas.

Aquí entran arquitecturas híbridas o modelos que mezclan atención con otros tipos de bloques.

---

## 3. Modelos de espacio de estados y familia Mamba

Una de las familias más relevantes hoy es la de los **State Space Models (SSM)**, es decir, modelos de espacio de estados.

### Idea básica

En lugar de construir el contexto comparando explícitamente todos los tokens, el modelo:

* mantiene un estado interno,
* lo actualiza al recibir nueva información,
* y usa ese estado para representar lo importante del pasado.

Dicho de forma intuitiva:

* el modelo no “mira” toda la secuencia una y otra vez,
* sino que va arrastrando una representación comprimida y dinámica del contexto.

### ¿Dónde encaja Mamba?

**Mamba** pertenece a esta familia. Su objetivo es construir modelos secuenciales potentes sin depender del coste típico de la atención completa.

### ¿Qué cambia respecto a un Transformer?

* Se elimina el bloque de atención como pieza principal.
* El núcleo del modelo pasa a ser un bloque secuencial basado en dinámica de estado.
* La información se propaga a través de actualizaciones internas del estado.

### ¿Qué se consigue?

* Mejor escalado en secuencias largas.
* Menor coste de memoria en muchos escenarios.
* Un procesamiento más natural para tareas muy secuenciales.

### Ventajas

* Más eficiencia en contextos largos.
* Menor dependencia de la atención completa.
* Buena conexión conceptual con lo que ya se conoce de LSTM/GRU: hay estado, actualización y memoria.

### Desventajas o dificultades

* La intuición es menos inmediata que en atención.
* Cuesta más “ver” qué parte del contexto está usando el modelo.
* La conexión entre bloques puede resultar menos transparente al principio que en un Transformer.

### Qué conviene recordar

Para estudiar esta familia, el alumnado puede apoyarse en una idea conocida:

> Igual que en LSTM/GRU hay una memoria que se actualiza, aquí también hay una representación del pasado, pero construida con un mecanismo más moderno y escalable.

---

## 4. Familia Liquid Neural Networks y Liquid Foundation Models

Otra línea distinta es la de los llamados **Liquid Neural Networks** y modelos relacionados.

### Idea básica

Estos modelos intentan representar sistemas más **dinámicos**, donde el estado interno cambia de forma continua o adaptativa según la entrada.

En lugar de pensar solo en capas fijas que transforman vectores, se pone más énfasis en:

* la evolución del estado,
* la dependencia temporal,
* y el comportamiento dinámico del sistema.

### Intuición general

Podemos imaginarlo así:

* un Transformer trabaja con bloques bastante definidos y repetidos,
* un modelo liquid intenta comportarse más como un sistema dinámico que evoluciona con el tiempo.

### ¿Qué cambia respecto a un Transformer?

* El flujo de información puede ser más continuo y dependiente del estado.
* El modelo se apoya más en dinámicas internas que en matrices de atención completas.
* En algunos diseños modernos pueden aparecer bloques híbridos, combinando partes secuenciales con atención.

### ¿Qué se consigue?

* Modelar mejor ciertos comportamientos temporales.
* Mayor flexibilidad dinámica.
* En algunos casos, modelos más compactos o adaptativos.

### Ventajas

* Buena capacidad para representar dinámica temporal.
* Interesantes para tareas secuenciales donde importa mucho la evolución del estado.
* Conceptualmente se pueden entender bien si ya se conocen CNN, capas feed-forward y Transformers.

### Desventajas o dificultades

* La matemática subyacente puede ser menos familiar.
* La intuición de “qué hace cada bloque” no siempre es tan inmediata.
* La parte más difícil suele ser entender **cómo se conectan los bloques** y qué papel cumple cada uno en el flujo global del modelo.

### Qué conviene recordar

Para el alumnado, probablemente lo más útil sea esta idea:

> No hay que pensar estos modelos como “Transformers raros”, sino como arquitecturas dinámicas donde el estado y la evolución temporal pesan más que la atención completa.

---

## 5. Arquitecturas híbridas

Entre los extremos “todo atención” y “nada de atención” existe un espacio muy amplio de arquitecturas híbridas.

### ¿Qué hacen?

Combinan bloques diferentes, por ejemplo:

* bloques de atención,
* bloques secuenciales tipo SSM,
* bloques feed-forward,
* mecanismos de memoria,
* módulos convolucionales.

### ¿Por qué aparecen?

Porque muchas veces no interesa sustituir completamente el Transformer, sino:

* conservar lo que funciona bien,
* añadir bloques más baratos,
* o especializar distintas partes del modelo.

### Ventajas

* Permiten combinar fortalezas de varias familias.
* Ofrecen más flexibilidad de diseño.
* Pueden adaptarse mejor a tareas concretas.

### Desventajas

* Son más difíciles de explicar.
* La arquitectura global puede volverse más compleja.
* La conexión entre bloques suele ser la parte menos intuitiva.

Esto encaja con una idea importante para clase:

> En muchas arquitecturas modernas, lo más difícil no es entender cada bloque por separado, sino entender cómo se encadenan y por qué el modelo alterna unos con otros.

---

## 6. Comparación intuitiva entre familias

| Familia | Idea principal | Ventaja destacada | Dificultad típica |
| ------- | -------------- | ----------------- | ----------------- |
| Transformers | Atención entre tokens | Contexto global explícito | Coste alto en secuencias largas |
| LSTM / GRU | Estado recurrente | Intuición secuencial clara | Dificultad para dependencias muy largas |
| Mamba / SSM | Estado dinámico escalable | Eficiencia en secuencias largas | Intuición menos visible que la atención |
| Liquid models | Dinámica interna adaptativa | Flexibilidad temporal | Comprender la dinámica y las conexiones |
| Híbridos | Mezcla de mecanismos | Equilibrio entre capacidades | Arquitectura más compleja |

---

## 7. Qué conviene explicar al alumnado

Para una primera aproximación, no hace falta entrar en toda la matemática.

Basta con fijar estas ideas:

1. **Transformer**: construye contexto mirando entre tokens con atención.
2. **LSTM/GRU**: construyen contexto manteniendo un estado recurrente.
3. **Mamba y SSM**: recuperan la idea de estado, pero de forma más moderna y escalable.
4. **Liquid models**: ponen mucho peso en la dinámica interna del sistema.
5. **Modelos híbridos**: mezclan varios bloques porque no siempre interesa una solución pura.

---

## 8. Idea final

La historia reciente de estas arquitecturas no consiste en “reemplazar totalmente” a los Transformers, sino en explorar distintas formas de resolver un mismo problema:

* cómo representar el contexto,
* cómo recordar el pasado,
* cómo escalar a secuencias largas,
* y cómo hacerlo con un coste razonable.

Por eso, más que pensar en una única arquitectura ganadora, conviene pensar en un **ecosistema de soluciones**.

En unas tareas dominarán los Transformers; en otras, serán más interesantes los modelos de espacio de estados, los liquid models o las arquitecturas híbridas.

---
