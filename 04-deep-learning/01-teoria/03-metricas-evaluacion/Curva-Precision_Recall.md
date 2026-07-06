---
title: "Curva precision-recall (precisión-exhaustividad)"
output: pdf_document
---
**Curva Precision-Recall: Definición**
La curva precision-recall es una representación gráfica del equilibrio entre la precisión y el recall para diferentes umbrales de probabilidad de un clasificador binario. Se usa comúnmente para evaluar el rendimiento de los modelos en tareas donde las clases están desequilibradas (por ejemplo, detección de fraude, diagnóstico médico).

**Precisión:** Mide la proporción de instancias positivas correctamente predichas entre todas las instancias predichas como positivas. Responde a la pregunta: "De todos los elementos etiquetados como positivos, ¿cuántos fueron realmente positivos?"

**Recall:** Mide la proporción de instancias positivas correctamente predichas entre todas las instancias realmente positivas. Responde a la pregunta: "De todos los elementos positivos reales, ¿cuántos fueron identificados correctamente?"

**Propósito e Interpretación**
La curva precision-recall ayuda a visualizar el rendimiento de un clasificador a lo largo de una gama de umbrales de decisión. Proporciona información sobre:

- **Rendimiento del Modelo en Diferentes Umbrales:** La curva muestra cómo cambian la precisión y el recall al variar el umbral para clasificar una instancia como positiva.

- **Equilibrio entre Precisión y Recall:** A menudo, hay un equilibrio entre la precisión y el recall. Al aumentar el umbral (haciendo el modelo más estricto), la precisión tiende a aumentar, pero el recall disminuye. Por el contrario, al disminuir el umbral (haciendo el modelo más permisivo), el recall tiende a aumentar, pero la precisión disminuye.

- **Comparación de Modelos:** Puedes comparar las curvas precision-recall de diferentes modelos para ver cuál funciona mejor para una tarea dada. Un modelo con una curva más alta y hacia la derecha generalmente se considera mejor.

- **Área Bajo la Curva (AUC):** El área bajo la curva precision-recall (AUC-PR) es una métrica única que resume el rendimiento general del modelo. Un AUC-PR más alto indica un mejor rendimiento.

**Escenario de Ejemplo**
Imagina un sistema de detección de fraude. Quieres identificar transacciones fraudulentas (clase positiva) mientras minimizas los falsos positivos (clasificar incorrectamente transacciones legítimas como fraudulentas).

- **Alta Precisión:** Significa que cuando el modelo predice una transacción como fraudulenta, es muy probable que sea correcta. Esto es importante para evitar inconvenientes a los clientes legítimos.

- **Alto Recall:** Significa que el modelo es capaz de identificar una gran proporción de las transacciones fraudulentas reales. Esto es crucial para prevenir pérdidas financieras.
La curva precision-recall te ayuda a encontrar un umbral que equilibre estos dos objetivos según tus necesidades específicas.

**En el Código**
El código que proporcionaste utiliza la siguiente función para generar y agregar una curva precision-recall a TensorBoard:

```python
def add_pr_curve_tensorboard(class_index, test_probs, test_label, global_step=0):
    # ... (código para calcular precisión y recall) ...
    writer.add_pr_curve(classes[class_index], tensorboard_truth,
    tensorboard_probs, global_step=global_step)
```

Esto te permite visualizar el equilibrio precision-recall para cada clase en la tarea de clasificación Fashion-MNIST.

