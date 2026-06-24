### **Explicación del código en PyTorch (Primer Ejemplo)**

Este código implementa una red neuronal en PyTorch para predecir los precios de viviendas usando el dataset **Boston Housing**. Se divide en varias secciones:

#### **1. Carga y preprocesamiento de datos**
```python
dataframe = pd.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values

X = dataset[:, 0:13]  # Las primeras 13 columnas son las características
y = dataset[:, 13].reshape(-1, 1)  # La última columna es la variable objetivo

scaler = StandardScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y)
```
- Se carga el dataset y se separan las variables predictoras (**X**) de la variable objetivo (**y**).
- Se normalizan los datos con `StandardScaler`, lo cual es importante para mejorar la convergencia del modelo.

#### **2. Conversión de datos a tensores de PyTorch**
```python
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)
```
- Se convierten los datos preprocesados en **tensores** para que puedan ser utilizados en PyTorch.

#### **3. Definición del modelo de red neuronal**
```python
class HousingModel(nn.Module):
    def __init__(self):
        super(HousingModel, self).__init__()
        self.fc1 = nn.Linear(13, 500)
        self.fc2 = nn.Linear(500, 100)
        self.fc3 = nn.Linear(100, 50)
        self.fc4 = nn.Linear(50, 1)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        return x
```
- Se define una **clase que representa el modelo de red neuronal** en PyTorch.
- La arquitectura tiene:
  - **Capa de entrada:** 13 neuronas (una por cada variable del dataset).
  - **Tres capas ocultas** con 500, 100 y 50 neuronas respectivamente, usando **ReLU** como función de activación.
  - **Capa de salida:** 1 neurona para predecir el precio de la vivienda.

#### **4. Entrenamiento del modelo**
```python
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 20
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    y_pred = model(X_train_tensor)
    loss = criterion(y_pred, y_train_tensor)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
```
- Se usa **Mean Squared Error (MSE)** como función de pérdida.
- Se usa **Adam** como optimizador.
- El entrenamiento ocurre en un bucle `for` de **20 épocas**:
  1. Se pone el modelo en modo `train()`.
  2. Se calcula la predicción.
  3. Se computa el error (`loss`).
  4. Se realiza retropropagación (`loss.backward()`).
  5. Se actualizan los pesos con `optimizer.step()`.

#### **5. Evaluación del modelo**
```python
model.eval()
with torch.no_grad():
    y_train_pred = model(X_train_tensor)
    y_test_pred = model(X_test_tensor)

rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred.numpy()))
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred.numpy()))

print(f"Train RMSE: {rmse_train:.4f}")
print(f"Test RMSE: {rmse_test:.4f}")
```
- Se evalúa el modelo sin actualizar gradientes (`torch.no_grad()`).
- Se calcula el error cuadrático medio (**RMSE**) para los datos de entrenamiento y prueba.

---

### **Comparación con el código en Keras**
Veamos cómo se traduce cada parte:

| **Componente**        | **Keras**  | **PyTorch** |
|----------------------|------------|------------|
| **Definir el modelo** | `Sequential()` con capas `Dense` | `nn.Module` con capas `Linear` |
| **Activación** | `activation="relu"` en `Dense` | `nn.ReLU()` |
| **Compilación** | `model.compile(loss="mse", optimizer="adam")` | `criterion = nn.MSELoss(); optimizer = optim.Adam()` |
| **Entrenamiento** | `model.fit(X_train, y_train, epochs=20)` | `for epoch in range(epochs):` con `loss.backward()` y `optimizer.step()` |
| **Predicción** | `model.predict(X_test)` | `with torch.no_grad(): model(X_test_tensor)` |

#### **Diferencias clave**
1. **Estructura del modelo**  
   - En **Keras**, `Sequential()` facilita la creación de modelos.
   - En **PyTorch**, se define una clase `nn.Module`, proporcionando más flexibilidad.

2. **Entrenamiento**  
   - En **Keras**, `model.fit()` maneja el entrenamiento automáticamente.
   - En **PyTorch**, se realiza manualmente con `for epoch in range(epochs)`.

3. **Evaluación**  
   - En **Keras**, `model.predict()` devuelve predicciones directamente.
   - En **PyTorch**, se necesita `with torch.no_grad()` para evitar cálculos de gradiente.

### **Conclusión**
- **Keras** es más fácil de usar y abstracto.
- **PyTorch** ofrece más control y flexibilidad, útil para modelos más personalizados.

