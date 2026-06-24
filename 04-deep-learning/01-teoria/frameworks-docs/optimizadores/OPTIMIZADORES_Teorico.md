# Documento teórico: Optimizadores para redes neuronales

Resumen: este documento explica los principios y fórmulas centrales detrás de los optimizadores usados en entrenamiento de redes neuronales, compara los algoritmos más empleados y da recomendaciones prácticas para elegir y ajustar optimizadores.

## 1. Introducción
- ¿Qué es optimizar una red neuronal? Encontrar parámetros $\theta$ que minimicen una función de pérdida $L(\theta)$ mediante iteraciones basadas en el gradiente.
- Objetivo: reducir la pérdida sobre el conjunto de entrenamiento mientras se mantiene buena generalización.
- Información utilizada por los optimizadores: gradiente $\nabla_\theta L$, momentos (media/varianza), historial de actualizaciones.

## 2. Fundamentos matemáticos
- Descenso por gradiente (full-batch):
	$$\theta_{t+1} = \theta_t - \eta \, \nabla_\theta L(\theta_t)$$
	donde $\eta$ es la tasa de aprendizaje (learning rate).
- SGD (mini-batch): usa estimadores estocásticos del gradiente; introduce ruido que puede ayudar a escapar mínimos locales.
- El tamaño de batch influye en la varianza del estimador del gradiente: batches grandes ⇒ pasos más estables; batches pequeños ⇒ más ruido.

## 3. SGD y aceleración (momentum)
- SGD simple (por minibatch):
	$$\theta_{t+1} = \theta_t - \eta \, g_t, \quad g_t \approx \nabla_\theta L(\theta_t)$$
- Momentum (clásico): introduce una velocidad $v_t$ que acumula gradientes:
	$$v_{t} = \gamma v_{t-1} + \eta g_t$$
	$$\theta_{t+1} = \theta_t - v_t$$
	con $\gamma\in[0,1)$ (por ejemplo 0.9). El momentum suaviza y acelera la convergencia en valles largos.
- Nesterov Accelerated Gradient (NAG): calcula el gradiente en una posición adelantada; suele dar mejor estimación del paso.

## 4. Métodos adaptativos (Adagrad / RMSProp / Adam)
Objetivo: adaptar la tasa por parámetro según historial de gradientes.

- Adagrad (acumula cuadrados):
	$$r_t = r_{t-1} + g_t^2$$
	$$\theta_{t+1} = \theta_t - \dfrac{\eta}{\sqrt{r_t + \epsilon}} \, g_t$$
	Problema: $r_t$ crece monotónicamente y la tasa efectivamente se vuelve muy pequeña.

- RMSProp (decay exponencial del segundo momento):
	$$s_t = \beta s_{t-1} + (1-\beta) g_t^2$$
	$$\theta_{t+1} = \theta_t - \dfrac{\eta}{\sqrt{s_t + \epsilon}} \, g_t$$

- Adam (combina momentum y RMSProp) — con corrección de sesgos:
	$$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$$
	$$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$$
	(correcciones de sesgo)
	$$\hat m_t = m_t/(1-\beta_1^t),\quad \hat v_t = v_t/(1-\beta_2^t)$$
	$$\theta_{t+1} = \theta_t - \eta\,\dfrac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}$$

- AdamW: modifica Adam para aplicar weight decay (decaimiento de pesos) de forma correcta separándolo de la penalización L2 en la actualización adaptativa; a menudo mejora generalización.

## 5. Weight decay vs L2
- L2 regularization añade $\lambda\|\theta\|^2$ a la pérdida; su efecto en GD es equivalente a restar $\eta\lambda\theta$ en cada paso.
- En optimizadores adaptativos la interacción entre L2 y el escalado por segundo momento puede no comportarse como un simple weight decay; por eso se recomienda usar AdamW o aplicar weight decay explícitamente.

## 6. Schedulers y técnicas de ajuste de tasa de aprendizaje
- Decaimiento exponencial: $\eta_t = \eta_0 \cdot \alpha^t$.
- Step decay: reducir $\eta$ por factores en pasos predefinidos.
- Cosine annealing (Ej. SGDR):
	$$\eta_t = \eta_{min} + \tfrac{1}{2}(\eta_{max}-\eta_{min})(1+\cos(\pi t / T))$$
- Warmup: iniciar con tasas pequeñas y aumentarlas gradualmente (útil en Transformers y grandes batchs).
- OneCycle / Cyclical LR: variar $\eta$ siguiendo un ciclo para acelerar convergencia y mejorar generalización.

## 7. Consideraciones prácticas y recomendaciones
- Elección inicial:
	- Para modelos de visión conv. grandes y cuando se busca mejor generalización: `SGD + momentum` + LR schedule.
	- Para prototipos y modelos donde se quiere convergencia rápida: `Adam` o `AdamW`.
- Reglas empíricas:
	- Si aumentas `batch_size`, incrementa la `learning_rate` proporcionalmente (regla lineal heurística).
	- Use `weight_decay` en AdamW; evita mezclar L2 sin ajustar en optimizadores adaptativos.
- Diagnóstico:
	- Curvas de entrenamiento/validación, histograma de gradientes, grad-norm, velocidad de cambio de pesos.

## 8. Comparativa rápida
- SGD: simple, robusto, buena generalización si se ajusta LR y schedule.
- SGD+momentum: converge más rápido que SGD puro en valles alargados.
- RMSProp: útil en problemas con señales ruidosas; adapta la tasa.
- Adam: converge rápido y es estable; puede sobreajustar y requiere tuning de weight decay.
- AdamW: versión recomendada de Adam para mejor generalización.

## 9. Implementaciones (rápido)
- Keras: `tf.keras.optimizers.SGD`, `Adam`, `RMSprop`, `AdamW` (desde TF Addons o TF 2.11+)
- PyTorch: `torch.optim.SGD`, `torch.optim.Adam`, `torch.optim.AdamW`, `torch.optim.RMSprop`.
- JAX/Optax: `optax.sgd`, `optax.adam`, `optax.adamw`, `optax.rmsprop`.

## 10. Referencias y lecturas recomendadas
- D. P. Kingma and J. Ba. "Adam: A Method for Stochastic Optimization" (2014).
- I. Loshchilov and F. Hutter. "Decoupled Weight Decay Regularization" (2019) — AdamW.
- L. N. Smith. "Cyclical Learning Rates for Training Neural Networks" (2017).
- Articles and docs: PyTorch docs, TensorFlow docs, Optax documentation, blog posts by Sebastian Ruder.

## 11. Ejercicios sugeridos
- Reproducir experimentos comparativos en Fashion‑MNIST usando los notebooks prácticos (Keras, PyTorch, JAX).
- Evaluar sensibilidad a `learning_rate`, `batch_size`, `weight_decay` y schedulers.
- Implementar y comparar `OneCycleLR` y `CosineAnnealingLR` en PyTorch.

---

Siguiente paso: si quieres, genero figuras de ejemplo (curvas sintéticas) o complemento con fragmentos de código en cada API. ¿Lo añado ahora?

## Ejemplo ilustrativo (numérico)
Para aclarar cómo cambia una actualización entre SGD (con o sin momentum) y Adam, consideremos la función cuadrática simple
$$L(\theta)=\theta^2$$
con gradiente $g=\nabla_\theta L=2\theta$. Tomemos $\theta_0=1$.

- SGD puro con tasa $\eta=0.1$:
	- Paso: $\theta_1 = \theta_0 - \eta g = 1 - 0.1\cdot 2 = 0.8$.

- SGD con momentum ($\gamma=0.9$, inicial $v_0=0$, misma $\eta=0.1$):
	- $v_1=\gamma v_0 + \eta g = 0 + 0.1\cdot 2 = 0.2$ → $\theta_1=1-0.2=0.8$ (mismo que SGD el primer paso),
	- Segundo paso (si el gradiente sigue siendo 2): $v_2=0.9\cdot0.2+0.1\cdot2=0.38$ → $\theta_2=0.8-0.38=0.42$. El momentum acelera los pasos sucesivos en la misma dirección.

- Adam (valores típicos $\beta_1=0.9,\beta_2=0.999,\epsilon\approx10^{-8}$). Con $\eta=0.01$ y $g_1=2$:
	- $m_1=(1-\beta_1)g_1=0.1\cdot2=0.2$,  $v_1=(1-\beta_2)g_1^2=0.001\cdot4=0.004$,
	- Correcciones de sesgo: $\hat m_1=m_1/(1-\beta_1)=0.2/0.1=2$, $\hat v_1=v_1/(1-\beta_2)=0.004/0.001=4$,
	- Actualización aproximada: $\Delta\theta\approx\eta\dfrac{\hat m_1}{\sqrt{\hat v_1}+\epsilon}=0.01\cdot\dfrac{2}{2}=0.01$, por tanto $\theta_1\approx0.99$.

Comentario: los pasos numéricos dependen mucho de la elección de $\eta$ y de los hiperparámetros; el ejemplo muestra que Adam aplica un ajuste por parámetro (normaliza por la raíz del segundo momento) y suele usar tasas efectivas distintas a SGD. Para comparaciones reproducibles y experimentales, mira los notebooks prácticos donde se ejecutan los mismos modelos con distintos optimizadores y schedules.