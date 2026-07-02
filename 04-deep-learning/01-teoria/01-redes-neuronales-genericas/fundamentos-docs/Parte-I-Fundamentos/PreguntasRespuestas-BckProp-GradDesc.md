## La Cocina del Aprendizaje Profundo y el Gradiente
Para entender mejor cómo funciona el aprendizaje profundo a través de la analogía de la cocina y los conceptos técnicos de los fuentes, aquí tienes las respuestas a tus dudas:
1. ¿Qué ocurre si la sensibilidad de un peso es cero?
Si la sensibilidad (∂w∂Error​) es cero, significa que el error final no se "enterará" de ningún cambio que realice ese cocinero en su estación. Por mucho que muevas ese mando de control (el peso), el sabor de la sopa (la pérdida) no variará en absoluto. Técnicamente, esto implica que ese peso no está contribuyendo al error, pero tampoco puede ser ajustado para mejorarlo, lo que a veces ocurre con neuronas "muertas" o gradientes que desaparecen.
2. ¿Cómo decide el optimizador cuánto girar el mando?
El optimizador utiliza un parámetro crítico llamado Learning Rate (tasa de aprendizaje).
• La dirección: La indica el gradiente (si es positivo, giramos a la izquierda; si es negativo, a la derecha).
• La magnitud: El optimizador multiplica el gradiente por el learning rate para decidir el tamaño del paso.
    ◦ Si el learning rate es muy grande, das giros bruscos y podrías pasarte del punto exacto de sal.
    ◦ Si es muy pequeño, el ajuste es tan minúsculo que tardarías una eternidad en mejorar la receta.
3. ¿Qué pasa si hay demasiadas estaciones en la cocina?
Añadir más capas (estaciones) aumenta la capacidad de la red para aprender representaciones complejas. Sin embargo, esto conlleva riesgos:
• Gradientes que desaparecen (Vanishing Gradients): La señal del "grito del juez" se va multiplicando por sensibilidades pequeñas en cada estación; si hay demasiadas, la información llega casi a cero a las primeras estaciones, y estas dejan de aprender.
• Mayor coste: Se requiere más potencia de cómputo (como tener muchas más hornillas y personal).
• Dificultad de entrenamiento: El equilibrio se vuelve mucho más frágil y el modelo puede volverse inestable.
4. La Regla de la Cadena para principiantes
Imagina que es el "Teléfono de la Culpa". Funciona bajo una lógica simple: "Si A influye en B, y B influye en C, entonces A influye en C". En la cocina, para saber cuánto castigar al cocinero de la Estación A, multiplicamos los impactos:
1. ¿Cuánto gritó el Juez por la sopa?
2. × ¿Cuánto de esa sopa dependía del caldo?
3. × ¿Cuánto de ese caldo dependía de la estación A? Al multiplicar estas sensibilidades, conectamos el mando del primer cocinero directamente con el resultado final.
5. ¿Qué significa que una neurona tenga una sensibilidad alta o baja?
La sensibilidad es un indicador de influencia o responsabilidad:
• Sensibilidad Alta: Significa que un "toquecito" en ese peso hace que el error salte por los aires. Esa neurona es vital para el resultado; un pequeño error ahí arruina todo el plato.
• Sensibilidad Baja: Significa que puedes cambiar mucho ese peso y al error "le da igual". Esa neurona apenas tiene impacto en el sabor final en ese momento del entrenamiento.

---
## La Anatomía del Error: El Algoritmo de Backpropagation
El reparto de la "culpa" del error entre las capas de una red neuronal se realiza mediante el algoritmo de Backpropagation, que utiliza la Regla de la Cadena para rastrear la responsabilidad desde la salida hacia la entrada.
Siguiendo la analogía de la cocina y los conceptos técnicos de las fuentes, así es como se distribuye esa responsabilidad:
1. El punto de partida: El error final
Todo comienza cuando la sopa llega al Juez (función de pérdida). Él detecta un error (por ejemplo, "sobra sal") y emite un grito: este es el valor de la pérdida que cuantifica el fallo total. Sin este punto de referencia, no habría "culpa" que repartir.
2. La Regla de la Cadena: El "Teléfono de la Culpa"
Para saber cuánto debe cambiar cada cocinero, no se puede simplemente gritarles a todos por igual. Se utiliza la Regla de la Cadena, que permite conectar la sensibilidad de cada etapa de forma sistemática.
• Sensibilidad (∂): Se interpreta como el impacto. Si cambiamos un gramo de sal en la Estación B, ¿cuántos gramos extra aparecen en el plato final?.
• Matemáticamente, la "culpa" de un peso específico se calcula multiplicando las sensibilidades de todas las etapas que hay entre ese peso y el error final.
3. El proceso de retropropagación (Backward Pass)
A diferencia de la cocina (forward pass), el aprendizaje ocurre en el backward pass:
• De la salida a la penúltima capa: Se calcula cuánto influyó el último paso (el caldo final) en el sabor.
• Hacia las capas ocultas: Ese error se propaga hacia atrás. Si el caldo final estaba salado porque el sofrito ya venía salado, la "culpa" se transfiere a la estación del sofrito.
• Reutilización de cálculos: El algoritmo es eficiente porque reutiliza los cálculos intermedios de la pasada hacia delante, evitando repetir operaciones innecesarias mientras retrocede por la red.
4. La asignación individual de responsabilidad
Cada peso o "mando de control" recibe una corrección proporcional a su influencia:
• Alta sensibilidad: Si un pequeño giro en un mando provocó un gran cambio en el error, ese parámetro es considerado muy responsable y recibirá un ajuste mayor.
• Baja sensibilidad: Si por mucho que se mueva un mando el error apenas cambia, su "culpa" es mínima y el ajuste será casi nulo.
5. El ajuste final (Gradiente Descendente)
Una vez que el Backpropagation ha terminado de repartir la culpa (calculando los gradientes), el optimizador entra en juego. Utiliza esa información para decidir cuánto girar cada mando (ajustar el peso) en la dirección opuesta al error para que, en la siguiente iteración, la sopa esté más cerca de la perfección.
En resumen, la culpa no se reparte al azar; se rastrea matemáticamente multiplicando los impactos locales de cada capa hasta llegar al origen del error.

---
## Recetas del Aprendizaje Profundo: Pesos, Gradientes y Sensibilidad

Para entender mejor cómo funciona el aprendizaje profundo a través de la analogía de la cocina y los conceptos técnicos de los fuentes, aquí tienes las respuestas a tus dudas:
1. ¿Qué ocurre si la sensibilidad de un peso es cero?
Si la sensibilidad (∂w∂Error​) es cero, significa que el error final no se "enterará" de ningún cambio que realice ese cocinero en su estación. Por mucho que muevas ese mando de control (el peso), el sabor de la sopa (la pérdida) no variará en absoluto. Técnicamente, esto implica que ese peso no está contribuyendo al error, pero tampoco puede ser ajustado para mejorarlo, lo que a veces ocurre con neuronas "muertas" o gradientes que desaparecen.
2. ¿Cómo decide el optimizador cuánto girar el mando?
El optimizador utiliza un parámetro crítico llamado Learning Rate (tasa de aprendizaje).
• La dirección: La indica el gradiente (si es positivo, giramos a la izquierda; si es negativo, a la derecha).
• La magnitud: El optimizador multiplica el gradiente por el learning rate para decidir el tamaño del paso.
    ◦ Si el learning rate es muy grande, das giros bruscos y podrías pasarte del punto exacto de sal.
    ◦ Si es muy pequeño, el ajuste es tan minúsculo que tardarías una eternidad en mejorar la receta.
3. ¿Qué pasa si hay demasiadas estaciones en la cocina?
Añadir más capas (estaciones) aumenta la capacidad de la red para aprender representaciones complejas. Sin embargo, esto conlleva riesgos:
• Gradientes que desaparecen (Vanishing Gradients): La señal del "grito del juez" se va multiplicando por sensibilidades pequeñas en cada estación; si hay demasiadas, la información llega casi a cero a las primeras estaciones, y estas dejan de aprender.
• Mayor coste: Se requiere más potencia de cómputo (como tener muchas más hornillas y personal).
• Dificultad de entrenamiento: El equilibrio se vuelve mucho más frágil y el modelo puede volverse inestable.
4. La Regla de la Cadena para principiantes
Imagina que es el "Teléfono de la Culpa". Funciona bajo una lógica simple: "Si A influye en B, y B influye en C, entonces A influye en C". En la cocina, para saber cuánto castigar al cocinero de la Estación A, multiplicamos los impactos:
1. ¿Cuánto gritó el Juez por la sopa?
2. × ¿Cuánto de esa sopa dependía del caldo?
3. × ¿Cuánto de ese caldo dependía de la estación A? Al multiplicar estas sensibilidades, conectamos el mando del primer cocinero directamente con el resultado final.
5. ¿Qué significa que una neurona tenga una sensibilidad alta o baja?
La sensibilidad es un indicador de influencia o responsabilidad:
• Sensibilidad Alta: Significa que un "toquecito" en ese peso hace que el error salte por los aires. Esa neurona es vital para el resultado; un pequeño error ahí arruina todo el plato.
• Sensibilidad Baja: Significa que puedes cambiar mucho ese peso y al error "le da igual". Esa neurona apenas tiene impacto en el sabor final en ese momento del entrenamiento.

---
## Optimización de Gradientes y Activación en Redes Neuronales

Para profundizar en el entrenamiento de redes neuronales, a continuación se detallan las respuestas a tus dudas basándome en los conceptos de los fuentes:
1. ¿Cómo se resuelve el problema de las neuronas muertas?
El problema de las neuronas muertas ocurre principalmente cuando se utiliza la función de activación ReLU. Debido a que ReLU bloquea todos los valores negativos (rango [0, +infinito)), una neurona puede quedarse en un estado donde siempre emite cero y deja de aprender.
Para resolverlo, se suelen emplear variantes de ReLU. Aunque los fuentes no detallan cada variante, mencionan que estas funciones alternativas ayudan a mantener gradientes más estables y evitan que la neurona quede totalmente inactiva, permitiendo que la información siga fluyendo incluso para entradas negativas.
2. ¿Cómo elegir la tasa de aprendizaje ideal para mi modelo?
Elegir el learning rate (tasa de aprendizaje) es un equilibrio crítico, ya que es el parámetro más importante para controlar la velocidad y estabilidad del entrenamiento.
• El riesgo de los extremos: Un paso demasiado largo (learning rate grande) puede hacer que el modelo "se pase" del mínimo y no converja; un paso demasiado corto (learning rate pequeño) hace que el aprendizaje sea extremadamente lento o se quede atrapado en zonas llanas.
• La estrategia práctica: Los fuentes sugieren que no hay una cifra mágica fija, sino que se debe experimentar. En la práctica, se utilizan frameworks como PyTorch o Keras para probar diferentes valores y observar cómo afectan la convergencia de la pérdida. Además, los optimizadores modernos como Adam o RMSprop ayudan a gestionar esta tasa de forma más eficiente que el gradiente descendente básico.
3. ¿Por qué las redes profundas sufren de gradientes que desaparecen?
El fenómeno de los gradientes que desaparecen (vanishing gradients) es especialmente problemático en redes con muchas capas y está estrechamente ligado a la elección de la función de activación.
• Saturación: Funciones como la Sigmoid pueden "saturarse", lo que significa que para valores muy altos o bajos, su pendiente (derivada) es casi cero.
• El efecto multiplicativo: Según la Regla de la Cadena, el gradiente de una capa profunda se calcula multiplicando las sensibilidades de todas las capas anteriores. Si estas sensibilidades son menores a 1 (como ocurre en las zonas de saturación), al multiplicarlas sucesivamente a través de muchas estaciones, el valor final se vuelve tan pequeño que los primeros cocineros (las primeras capas) no reciben ninguna instrucción clara para ajustar sus pesos.
• Consecuencia: El "grito del juez" (el error) se va atenuando hasta que llega a ser imperceptible en las capas iniciales, deteniendo el aprendizaje en la parte más profunda de la red.

---
## Dinámica y Causas de los Gradientes Explosivos en Redes Neuronales

El fenómeno de los exploding gradients (gradientes explosivos) es, efectivamente, el polo opuesto de los gradientes que desaparecen y ocurre cuando los valores de los gradientes crecen de forma descontrolada durante el proceso de Backpropagation.
Este problema se produce principalmente por las siguientes razones:
1. El efecto multiplicativo de la Regla de la Cadena
La causa fundamental reside en cómo funciona la Regla de la Cadena. Como se ha explicado en la analogía de la cocina, para calcular la "culpa" de un peso en las capas iniciales, debemos multiplicar las sensibilidades (derivadas) de todas las capas intermedias.
• Si esas sensibilidades son mayores que 1, al multiplicarlas sucesivamente a través de muchas capas, el valor resultante crece exponencialmente.
• Ejemplo técnico: Si tienes 10 capas y cada una tiene una sensibilidad de 2, el impacto total se multiplica por 210 (1024). Si tienes 50 capas, el número se vuelve astronómico.
2. Pesos iniciales demasiado grandes
Si los pesos (w) de la red se inicializan con valores muy altos, la combinación lineal en cada neurona genera resultados muy grandes. Dado que el gradiente depende directamente de estos valores, un peso inicial elevado puede actuar como un amplificador que dispara la magnitud del gradiente desde el inicio del entrenamiento.
3. La acumulación del "grito del Juez"
En la metáfora de la cocina, si el Juez (función de pérdida) detecta un error y cada estación de la cadena tiene una sensibilidad alta (un "mando de control" muy sensible), el mensaje de corrección se amplifica en cada paso hacia atrás.
• Para cuando el mensaje llega a los primeros cocineros, el ajuste que deben hacer es tan masivo que "rompen" la receta.
Consecuencias en el modelo
Cuando los gradientes "explotan", ocurren varios problemas críticos:
• Actualizaciones drásticas: El optimizador realiza cambios gigantescos en los pesos (debido a que el paso es learning rate × gradiente), lo que hace que el modelo no converja y salte de un lado a otro del "paisaje de pérdida" sin encontrar nunca el mínimo.
• Inestabilidad numérica: Los pesos pueden alcanzar valores tan grandes que la computadora ya no puede representarlos, resultando en errores de tipo NaN (Not a Number) o infinito.
En resumen, mientras que el vanishing gradient hace que la red deje de aprender porque el mensaje se debilita, el exploding gradient hace que el aprendizaje sea caótico e inestable porque el mensaje de error se vuelve demasiado ruidoso y potente.

---

## Estabilidad y Optimización en el Entrenamiento de Redes Neuronales

Para abordar tus dudas sobre los desafíos técnicos en el entrenamiento de redes neuronales, me basaré en la información de las fuentes proporcionadas y nuestra conversación previa:
1. ¿Cómo se soluciona la explosión del gradiente?
La explosión del gradiente ocurre cuando las multiplicaciones sucesivas de la regla de la cadena resultan en valores astronómicos que hacen que el modelo sea inestable. Según las fuentes, se puede mitigar mediante:
• Mejores inicializaciones de pesos: Las fuentes señalan que el uso de técnicas de inicialización modernas es una de las razones por las que las redes funcionan hoy en día donde antes fallaban. Esto evita que los pesos comiencen con valores que actúen como amplificadores descontrolados.
• Ajuste del Learning Rate (Tasa de aprendizaje): Un learning rate demasiado grande puede exacerbar la inestabilidad. Si el gradiente es muy alto y se multiplica por un paso largo, el error puede divergir en lugar de converger.
• Funciones de activación adecuadas: La elección de la activación influye en cómo se propaga el error; algunas pueden atenuar o amplificar el gradiente significativamente.
• Optimizadores avanzados: El uso de herramientas como Adam o RMSprop introduce mejoras de estabilidad frente al gradiente descendente básico.
2. ¿Qué herramientas tiene PyTorch para ver los gradientes?
Las fuentes destacan que los frameworks modernos como PyTorch automatizan el proceso de cálculo, permitiendo al desarrollador centrarse en la arquitectura:
• Autograd: Es el sistema de diferenciación automática que construye el grafo de operaciones por nosotros.
• loss.backward(): Al llamar a esta función, PyTorch recorre el grafo hacia atrás (backward pass) y calcula automáticamente todos los gradientes de la pérdida respecto a cada peso de la red.
• Visualización en práctica: Las fuentes mencionan que es posible observar los gradientes en acción dentro del entorno de desarrollo para realizar labores de debugging y optimización.
3. ¿Cómo afecta un batch size pequeño a la estabilidad?
El batch size (tamaño del lote) determina cuántos ejemplos de datos se usan antes de actualizar los pesos. Su tamaño impacta directamente en la estabilidad de la siguiente manera:
• Batch size pequeño (hacia el Stochastic Gradient Descent): Utilizar pocos ejemplos (o solo uno) genera más ruido en la actualización de los parámetros. Esto provoca una trayectoria inestable durante el entrenamiento. Aunque esto puede ayudar a "escapar" de mínimos locales, hace que el camino hacia la solución sea mucho más caótico.
• Batch size mediano (Mini-batch): Es el estándar actual porque ofrece un compromiso. Ayuda a reducir el ruido extremo y mejora la estabilidad del entrenamiento en comparación con usar un solo dato, permitiendo además aprovechar la capacidad de procesamiento paralelo de las GPUs.
• Batch size grande: Proporciona un gradiente más preciso y estable, pero consume mucha más memoria y puede dificultar la capacidad del modelo para generalizar si es excesivo.
En resumen, un batch size muy pequeño sacrifica estabilidad por velocidad y ruido, mientras que los lotes más grandes (mini-batches) proporcionan el equilibrio necesario para que el modelo aprenda de forma constante.

---
## Optimización y Flujos de Gradientes en Redes Neuronales

A continuación, se explica cómo las inicializaciones de pesos, las herramientas de PyTorch y el uso de mini-batches optimizan el entrenamiento de las redes neuronales según las fuentes proporcionadas:
1. Inicialización de pesos y gradientes explosivos
Las mejores inicializaciones de pesos son fundamentales para evitar los gradientes explosivos porque controlan cómo se transmite el error a través de las capas.
• El efecto multiplicativo: En el backpropagation, las "sensibilidades" (derivadas) de cada etapa se multiplican siguiendo la regla de la cadena.
• Control de la amplitud: Si los pesos iniciales son muy grandes, actúan como amplificadores; al multiplicarse a través de muchas capas, el gradiente crece exponencialmente hasta "explotar".
• Estabilidad: Las inicializaciones modernas buscan que estas sensibilidades se mantengan en rangos que no disparen los valores, permitiendo que el entrenamiento sea viable a gran escala, algo que antes de estas técnicas era casi imposible.
2. Herramientas de PyTorch para ver gradientes
PyTorch facilita la observación y el cálculo de gradientes mediante procesos automatizados:
• Autograd: Es el sistema central que construye automáticamente el grafo de operaciones.
• loss.backward(): Es la función clave que, al ser llamada, recorre el grafo hacia atrás y calcula todos los gradientes de la pérdida respecto a los pesos.
• Visualización: El framework permite observar el comportamiento de estos gradientes (mencionado en las fuentes como GradientTape en acción en contextos de debugging) para entender cómo está aprendiendo el modelo y realizar optimizaciones.
3. El equilibrio del Mini-batch frente al SGD puro
El uso de mini-batches se considera el estándar en la práctica porque ofrece un compromiso ideal entre la eficiencia y la estabilidad:
• Reducción del ruido: A diferencia del SGD puro, que usa un solo ejemplo y genera una trayectoria muy inestable y ruidosa, el mini-batch suaviza las actualizaciones de los parámetros.
• Estabilidad del entrenamiento: Al procesar pequeños lotes, se mejora la estabilidad general del proceso en comparación con la volatilidad de actualizar el modelo tras cada dato individual.
• Paralelismo: Una ventaja crítica es que permite aprovechar el procesamiento en paralelo de las GPUs y CPUs, algo que no es eficiente con el SGD puro, acelerando significativamente el tiempo de entrenamiento.
• Capacidad de escape: Aunque es más estable que el SGD, aún conserva suficiente "ruido" comparado con el Batch GD (todo el dataset) para ayudar al modelo a escapar de mínimos locales.

---

## ReLU y la Superación del Gradiente Desvanecido

La función de activación ReLU (Rectified Linear Unit) soluciona el problema del vanishing gradient (gradiente que se desvanece) al proporcionar un flujo de gradientes mucho más estable y robusto en comparación con funciones clásicas como la Sigmoid.
A continuación, se detalla cómo logra esto basándose en la lógica del "reparto de la culpa" descrita en las fuentes:
1. El problema de la saturación (El "atascamiento" de la Sigmoid)
Funciones como la Sigmoid tienen el inconveniente de que se saturan. Esto significa que para valores de entrada muy grandes o muy pequeños, la pendiente de la función es casi plana (cercana a cero).
• En términos de la cocina, si un cocinero usa Sigmoid, su sensibilidad al error es bajísima; por mucho que el "Juez" grite, el impacto de sus cambios en la receta final es minúsculo.
• Al aplicar la Regla de la Cadena, multiplicamos estas sensibilidades pequeñas capa tras capa. Multiplicar muchos números cercanos a cero resulta en un valor final que "se desvanece", haciendo que las capas iniciales no reciban ninguna instrucción de ajuste.
2. La solución de ReLU: Gradientes estables
A diferencia de la Sigmoid, la función ReLU tiene un rango de [0,+∞). Su comportamiento es simple: si la entrada es positiva, deja pasar el valor tal cual; si es negativa, lo bloquea (devuelve cero).
• Impacto constante: Para cualquier valor positivo, la "pendiente" o sensibilidad de ReLU es constante (no disminuye ni se satura).
• Evita el desvanecimiento: Al mantener un gradiente fuerte y constante para las señales positivas, el "mensaje" del error (el grito del Juez) puede viajar hacia atrás a través de muchas capas sin perder fuerza. Esto permite que el modelo se entrene de forma más rápida y eficiente.
3. El reparto de la culpa sin "pérdida de señal"
En el Backpropagation, el objetivo es que cada peso sepa cuánto influyó en el error final.
• Con ReLU, la tasa de influencia (derivada) no se debilita artificialmente por la forma de la función de activación en las zonas positivas.
• Esto asegura que el "Teléfono de la Culpa" funcione correctamente: la multiplicación de sensibilidades en la cadena de operaciones no tiende a cero de forma inevitable, permitiendo que incluso las neuronas de la primera estación de la cocina (capa de entrada) reciban una corrección clara sobre cómo mejorar.
Sin embargo, las fuentes advierten que ReLU tiene su propio riesgo: las "neuronas muertas". Si una neurona cae en la zona negativa, su sensibilidad se vuelve cero absoluto y deja de aprender por completo, lo que se soluciona utilizando variantes de ReLU que permiten el paso de una señal mínima incluso en valores negativos

---

## Optimización y Evaluación en el Entrenamiento de Redes Neuronales

Para evaluar el rendimiento de una red neuronal y asegurar la estabilidad de su entrenamiento, se utilizan diversos mecanismos técnicos y herramientas de software. A continuación, se detalla la respuesta a tus dudas basándose en las fuentes:
Uso de métricas para evaluar el rendimiento
Es fundamental distinguir entre la función de pérdida y las métricas, ya que cumplen roles diferentes en el ciclo de vida del modelo:
• Diferencia de propósito: Mientras que la pérdida se utiliza exclusivamente para guiar el entrenamiento y ajustar los parámetros, las métricas se emplean para evaluar el rendimiento final de una forma que sea interpretable para los humanos.
• Naturaleza matemática: La pérdida debe ser obligatoriamente diferenciable para que el algoritmo pueda calcular gradientes; en cambio, las métricas no necesitan serlo.
• Ejemplos comunes: Una métrica muy utilizada para interpretar resultados en clasificación es el Accuracy (precisión), aunque esta no suele usarse como función de pérdida para entrenar el modelo.
Herramientas de PyTorch para observar gradientes
Los frameworks modernos como PyTorch automatizan el complejo proceso del cálculo de gradientes, permitiendo a los desarrolladores monitorear el aprendizaje:
• Autograd: Es el motor central de PyTorch que construye automáticamente el grafo de operaciones (grafo computacional).
• loss.backward(): Esta es la función clave que dispara el backward pass. Al ejecutarla, PyTorch recorre el grafo hacia atrás y calcula los gradientes de la pérdida respecto a cada peso de la red utilizando la regla de la cadena.
• Observación del flujo: Las fuentes mencionan que es posible observar herramientas como GradientTape (o sistemas equivalentes en PyTorch) en acción para realizar labores de debugging y entender cómo fluyen los gradientes a través de las capas.
Efecto de un batch size pequeño en la estabilidad
El batch size (tamaño del lote) determina cuántos datos procesa la red antes de actualizar sus pesos, lo cual impacta directamente en la estabilidad del entrenamiento:
• Inestabilidad y ruido: Un batch size muy pequeño (como en el SGD puro, que usa un solo ejemplo) genera mucho ruido en las actualizaciones. Esto se traduce en una trayectoria muy inestable hacia el mínimo de la función de pérdida.
• Ventaja del ruido: A pesar de la inestabilidad, ese ruido puede ser beneficioso en ocasiones porque permite al modelo escapar de mínimos locales.
• El equilibrio del Mini-batch: La práctica estándar es usar mini-batches, que ofrecen un compromiso entre la rapidez del SGD y la precisión del Batch GD. El uso de lotes de tamaño moderado reduce el ruido extremo y mejora significativamente la estabilidad del entrenamiento, permitiendo además aprovechar la capacidad de procesamiento paralelo de las GPUs.




