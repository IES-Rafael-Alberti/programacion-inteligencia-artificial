---
title: "Métricas en Pytorch y Keras"
output: pdf_document
date: "2025-03-12"
---

# Guía Exhaustiva de Métricas en PyTorch

En el aprendizaje automático, las métricas son fundamentales para evaluar el rendimiento de un modelo. PyTorch, aunque no incluye una librería de métricas integrada como TensorFlow (con `tf.keras.metrics`), ofrece flexibilidad para implementar métricas personalizadas o utilizar librerías externas como **TorchMetrics**. Esta guía cubre las métricas más comunes y cómo implementarlas en PyTorch.

---

## 1. **Métricas Básicas**

### 1.1. **Exactitud (Accuracy)**
La exactitud mide la proporción de predicciones correctas respecto al total de predicciones.

```python
def accuracy(y_pred, y_true):
    # y_pred: Logits o probabilidades (shape: [batch_size, num_classes])
    # y_true: Etiquetas (shape: [batch_size])
    y_pred = torch.argmax(y_pred, dim=1)  # Obtener la clase predicha
    correct = (y_pred == y_true).float()  # Comparar con las etiquetas verdaderas
    acc = correct.sum() / len(correct)    # Calcular la exactitud
    return acc
```

**Uso**:
```python
y_pred = torch.tensor([[0.2, 0.8], [0.6, 0.4]])  # Logits
y_true = torch.tensor([1, 0])                   # Etiquetas
print(accuracy(y_pred, y_true))  # Salida: 0.5
```

---

### 1.2. **Precisión, Exhaustividad y F1-Score**
Estas métricas son útiles en problemas de clasificación binaria o multiclase.

```python
from sklearn.metrics import precision_score, recall_score, f1_score

def precision_recall_f1(y_pred, y_true):
    y_pred = torch.argmax(y_pred, dim=1).cpu().numpy()  # Convertir a numpy
    y_true = y_true.cpu().numpy()
    
    precision = precision_score(y_true, y_pred, average='macro')
    recall = recall_score(y_true, y_pred, average='macro')
    f1 = f1_score(y_true, y_pred, average='macro')
    
    return precision, recall, f1
```

**Uso**:
```python
y_pred = torch.tensor([[0.2, 0.8], [0.6, 0.4]])
y_true = torch.tensor([1, 0])
print(precision_recall_f1(y_pred, y_true))  # Salida: (0.5, 0.5, 0.5)
```

---

### 1.3. **Pérdida (Loss)**
PyTorch incluye funciones de pérdida comunes en `torch.nn`:
- **Clasificación binaria**: `nn.BCELoss`, `nn.BCEWithLogitsLoss`.
- **Clasificación multiclase**: `nn.CrossEntropyLoss`.
- **Regresión**: `nn.MSELoss`.

**Ejemplo**:
```python
loss_fn = nn.CrossEntropyLoss()
y_pred = torch.tensor([[0.2, 0.8], [0.6, 0.4]])
y_true = torch.tensor([1, 0])
loss = loss_fn(y_pred, y_true)
print(loss)  # Salida: valor de la pérdida
```

---

## 2. **Métricas Avanzadas**

### 2.1. **Curva ROC y AUC**
La curva ROC (Receiver Operating Characteristic) y el área bajo la curva (AUC) son métricas comunes para evaluar modelos de clasificación binaria.

**Implementación con TorchMetrics**:
```python
from torchmetrics import ROC, AUC

# Crear métricas
roc = ROC(pos_label=1)
auc = AUC()

# Calcular métricas
y_pred = torch.tensor([0.1, 0.4, 0.35, 0.8])  # Probabilidades de la clase positiva
y_true = torch.tensor([0, 1, 0, 1])           # Etiquetas verdaderas

fpr, tpr, thresholds = roc(y_pred, y_true)
auc_score = auc(fpr, tpr)
print(auc_score)  # Salida: valor del AUC
```

---

### 2.2. **Matriz de Confusión**
La matriz de confusión es útil para visualizar el rendimiento de un modelo de clasificación.

**Implementación**:
```python
from sklearn.metrics import confusion_matrix

def confusion_matrix_metric(y_pred, y_true):
    y_pred = torch.argmax(y_pred, dim=1).cpu().numpy()
    y_true = y_true.cpu().numpy()
    return confusion_matrix(y_true, y_pred)
```

**Uso**:
```python
y_pred = torch.tensor([[0.2, 0.8], [0.6, 0.4]])
y_true = torch.tensor([1, 0])
print(confusion_matrix_metric(y_pred, y_true))
```

---

### 2.3. **Pérdida de Regresión (MSE, MAE)**
Para problemas de regresión, las métricas comunes son el Error Cuadrático Medio (MSE) y el Error Absoluto Medio (MAE).

**Implementación**:
```python
def mse(y_pred, y_true):
    return torch.mean((y_pred - y_true) ** 2)

def mae(y_pred, y_true):
    return torch.mean(torch.abs(y_pred - y_true))
```

**Uso**:
```python
y_pred = torch.tensor([1.0, 2.0, 3.0])
y_true = torch.tensor([1.5, 2.5, 2.8])
print(mse(y_pred, y_true))  # Salida: MSE
print(mae(y_pred, y_true))  # Salida: MAE
```

---

## 3. **TorchMetrics: Librería Especializada**

**TorchMetrics** es una librería diseñada para calcular métricas de manera eficiente en PyTorch. Soporta métricas como:
- Exactitud (Accuracy).
- Precisión, Exhaustividad, F1-Score.
- Curva ROC, AUC.
- Matriz de confusión.
- Pérdidas de regresión (MSE, MAE).

**Instalación**:
```bash
pip install torchmetrics
```

**Ejemplo de uso**:
```python
from torchmetrics import Accuracy

# Crear métrica
acc_metric = Accuracy(task="multiclass", num_classes=2)

# Calcular métrica
y_pred = torch.tensor([[0.2, 0.8], [0.6, 0.4]])
y_true = torch.tensor([1, 0])
print(acc_metric(y_pred, y_true))  # Salida: exactitud
```

---

## 4. **Métricas Personalizadas**

Si necesitas una métrica específica, puedes implementarla fácilmente en PyTorch. Por ejemplo, para calcular la **Dice Coefficient** (común en segmentación de imágenes):

```python
def dice_coefficient(y_pred, y_true, smooth=1e-6):
    y_pred = y_pred.view(-1)  # Aplanar tensores
    y_true = y_true.view(-1)
    
    intersection = (y_pred * y_true).sum()
    dice = (2.0 * intersection + smooth) / (y_pred.sum() + y_true.sum() + smooth)
    return dice
```

**Uso**:
```python
y_pred = torch.tensor([0.1, 0.9, 0.8])
y_true = torch.tensor([0, 1, 1])
print(dice_coefficient(y_pred, y_true))  # Salida: coeficiente de Dice
```

---

## 5. **Consejos para Usar Métricas en PyTorch**

1. **Elige métricas relevantes**:
   - Para clasificación: Exactitud, Precisión, Exhaustividad, F1-Score, AUC.
   - Para regresión: MSE, MAE.
   - Para segmentación: Dice Coefficient, IoU.

2. **Usa TorchMetrics**:
   - Es eficiente y está optimizado para PyTorch.
   - Soporta métricas avanzadas como la curva ROC y AUC.

3. **Calcula métricas en el conjunto de validación**:
   - Evalúa el rendimiento del modelo en datos no vistos.

4. **Visualiza métricas**:
   - Usa herramientas como Matplotlib o TensorBoard para visualizar curvas ROC, matrices de confusión, etc.

---

## 6. **Ejemplo Completo: Entrenamiento con Métricas**

```python
from torchmetrics import Accuracy

# Definir métrica
acc_metric = Accuracy(task="multiclass", num_classes=2)

# Bucle de entrenamiento
for epoch in range(epochs):
    model.train()
    for X, y in train_dataloader:
        X, y = X.to(device), y.to(device)
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    # Evaluación
    model.eval()
    with torch.no_grad():
        for X, y in val_dataloader:
            X, y = X.to(device), y.to(device)
            y_pred = model(X)
            acc = acc_metric(y_pred, y)
    print(f"Epoch {epoch}, Accuracy: {acc}")
```

---


(Due to technical issues, the search service is temporarily unavailable.)

# Guía Exhaustiva de Métricas en Keras

Keras, como parte de TensorFlow, ofrece una amplia gama de métricas integradas para evaluar el rendimiento de modelos de aprendizaje automático. Estas métricas son fáciles de usar y están optimizadas para trabajar con modelos de Keras. Esta guía cubre las métricas más comunes, cómo usarlas y cómo crear métricas personalizadas.

---

## 1. **Métricas Integradas en Keras**

Keras proporciona métricas listas para usar en el módulo `tf.keras.metrics`. Algunas de las más comunes son:

### 1.1. **Exactitud (Accuracy)**
Mide la proporción de predicciones correctas respecto al total de predicciones.

```python
from tensorflow.keras.metrics import Accuracy

# Crear métrica
accuracy_metric = Accuracy()

# Actualizar métrica
y_true = [0, 1, 1, 0]
y_pred = [0.1, 0.9, 0.8, 0.2]  # Probabilidades o logits
accuracy_metric.update_state(y_true, y_pred)

# Obtener resultado
print(accuracy_metric.result().numpy())  # Salida: exactitud
```

---

### 1.2. **Precisión, Exhaustividad y F1-Score**
Estas métricas son útiles para problemas de clasificación binaria o multiclase.

```python
from tensorflow.keras.metrics import Precision, Recall

# Crear métricas
precision_metric = Precision()
recall_metric = Recall()

# Actualizar métricas
y_true = [0, 1, 1, 0]
y_pred = [0.1, 0.9, 0.8, 0.2]
precision_metric.update_state(y_true, y_pred)
recall_metric.update_state(y_true, y_pred)

# Obtener resultados
print(precision_metric.result().numpy())  # Salida: precisión
print(recall_metric.result().numpy())    # Salida: exhaustividad
```

---

### 1.3. **AUC (Área Bajo la Curva ROC)**
Mide el área bajo la curva ROC, útil para evaluar modelos de clasificación binaria.

```python
from tensorflow.keras.metrics import AUC

# Crear métrica
auc_metric = AUC()

# Actualizar métrica
y_true = [0, 1, 1, 0]
y_pred = [0.1, 0.9, 0.8, 0.2]
auc_metric.update_state(y_true, y_pred)

# Obtener resultado
print(auc_metric.result().numpy())  # Salida: AUC
```

---

### 1.4. **Pérdida (Loss)**
Keras incluye funciones de pérdida comunes en `tf.keras.losses`:
- **Clasificación binaria**: `BinaryCrossentropy`.
- **Clasificación multiclase**: `CategoricalCrossentropy`.
- **Regresión**: `MeanSquaredError`.

**Ejemplo**:
```python
from tensorflow.keras.losses import BinaryCrossentropy

# Crear función de pérdida
loss_fn = BinaryCrossentropy()

# Calcular pérdida
y_true = [0, 1, 1, 0]
y_pred = [0.1, 0.9, 0.8, 0.2]
loss = loss_fn(y_true, y_pred)
print(loss.numpy())  # Salida: valor de la pérdida
```

---

## 2. **Métricas en Modelos de Keras**

Puedes especificar métricas al compilar un modelo en Keras. Estas métricas se calcularán automáticamente durante el entrenamiento y la validación.

**Ejemplo**:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Crear modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])

# Compilar modelo con métricas
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', Precision(), Recall(), AUC()])

# Entrenar modelo
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
```

---

## 3. **Métricas Personalizadas**

Si necesitas una métrica específica, puedes crear una métrica personalizada subclasificando `tf.keras.metrics.Metric`.

**Ejemplo: Coeficiente de Dice (para segmentación de imágenes)**:
```python
import tensorflow as tf

class DiceCoefficient(tf.keras.metrics.Metric):
    def __init__(self, name='dice_coefficient', **kwargs):
        super(DiceCoefficient, self).__init__(name=name, **kwargs)
        self.intersection = self.add_weight(name='intersection', initializer='zeros')
        self.union = self.add_weight(name='union', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_true = tf.cast(y_true, tf.bool)
        y_pred = tf.cast(y_pred > 0.5, tf.bool)  # Umbral para obtener máscara binaria
        
        intersection = tf.reduce_sum(tf.cast(y_true & y_pred, tf.float32))
        union = tf.reduce_sum(tf.cast(y_true | y_pred, tf.float32))
        
        self.intersection.assign_add(intersection)
        self.union.assign_add(union)

    def result(self):
        return (2.0 * self.intersection) / (self.union + tf.keras.backend.epsilon())

    def reset_states(self):
        self.intersection.assign(0.0)
        self.union.assign(0.0)

# Uso
dice_metric = DiceCoefficient()
y_true = [[1, 0], [0, 1]]
y_pred = [[0.9, 0.1], [0.4, 0.6]]
dice_metric.update_state(y_true, y_pred)
print(dice_metric.result().numpy())  # Salida: coeficiente de Dice
```

---

## 4. **Métricas para Problemas Específicos**

### 4.1. **Clasificación Multiclase**
- **Exactitud**: `tf.keras.metrics.Accuracy`.
- **Precisión, Exhaustividad, F1-Score**: `tf.keras.metrics.Precision`, `tf.keras.metrics.Recall`.
- **Matriz de Confusión**: Usa `sklearn.metrics.confusion_matrix`.

**Ejemplo**:
```python
from sklearn.metrics import confusion_matrix

y_true = [0, 1, 2, 2]
y_pred = [0, 2, 2, 1]
print(confusion_matrix(y_true, y_pred))
```

---

### 4.2. **Regresión**
- **Error Cuadrático Medio (MSE)**: `tf.keras.metrics.MeanSquaredError`.
- **Error Absoluto Medio (MAE)**: `tf.keras.metrics.MeanAbsoluteError`.

**Ejemplo**:
```python
from tensorflow.keras.metrics import MeanSquaredError, MeanAbsoluteError

mse_metric = MeanSquaredError()
mae_metric = MeanAbsoluteError()

y_true = [1.0, 2.0, 3.0]
y_pred = [1.5, 2.5, 2.8]
mse_metric.update_state(y_true, y_pred)
mae_metric.update_state(y_true, y_pred)

print(mse_metric.result().numpy())  # Salida: MSE
print(mae_metric.result().numpy())  # Salida: MAE
```

---

### 4.3. **Segmentación de Imágenes**
- **Coeficiente de Dice**: Implementación personalizada (ver arriba).
- **IoU (Intersección sobre Unión)**: `tf.keras.metrics.MeanIoU`.

**Ejemplo**:
```python
from tensorflow.keras.metrics import MeanIoU

# Crear métrica
iou_metric = MeanIoU(num_classes=2)

# Actualizar métrica
y_true = [[0, 1], [1, 0]]
y_pred = [[0, 1], [1, 0]]
iou_metric.update_state(y_true, y_pred)

# Obtener resultado
print(iou_metric.result().numpy())  # Salida: IoU
```

---

## 5. **Consejos para Usar Métricas en Keras**

1. **Elige métricas relevantes**:
   - Para clasificación: Exactitud, Precisión, Exhaustividad, F1-Score, AUC.
   - Para regresión: MSE, MAE.
   - Para segmentación: Dice Coefficient, IoU.

2. **Usa métricas durante el entrenamiento**:
   - Especifica métricas al compilar el modelo para monitorear el rendimiento.

3. **Visualiza métricas**:
   - Usa TensorBoard para visualizar métricas en tiempo real.

4. **Crea métricas personalizadas**:
   - Si necesitas una métrica específica, implementa una subclase de `tf.keras.metrics.Metric`.

---

## 6. **Ejemplo Completo: Entrenamiento con Métricas**

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import Accuracy, Precision, Recall, AUC

# Crear modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])

# Compilar modelo con métricas
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=[Accuracy(), Precision(), Recall(), AUC()])

# Entrenar modelo
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
```

---

