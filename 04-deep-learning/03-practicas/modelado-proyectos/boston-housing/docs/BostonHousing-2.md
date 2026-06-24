### **Explicación del código en PyTorch (Segundo Ejemplo)**

Este código implementa una red neuronal en PyTorch con validación cruzada usando `KFold`, integrando el modelo en un `Pipeline` de `scikit-learn`.

---

## **1. Carga y preprocesamiento de datos**
```python
dataframe = pd.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values

X = dataset[:, 0:13]  # Las primeras 13 columnas son las características
y = dataset[:, 13].reshape(-1, 1)  # La última columna es la variable objetivo

scaler = StandardScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y)
```
- Se **carga** el dataset y se **separan** las características (**X**) y la variable objetivo (**y**).
- Se **normalizan** los datos con `StandardScaler()` para mejorar el rendimiento del modelo.

---

## **2. Definición del modelo en PyTorch**
```python
class WiderModel(nn.Module):
    def __init__(self):
        super(WiderModel, self).__init__()
        self.fc1 = nn.Linear(13, 20)  # Capa oculta con 20 neuronas
        self.fc2 = nn.Linear(20, 1)   # Capa de salida
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))  # Aplicar ReLU en la capa oculta
        x = self.fc2(x)  # Capa de salida sin activación
        return x
```
- Se define una **red neuronal simple** con:
  - **Capa de entrada:** 13 neuronas (una por cada característica del dataset).
  - **Capa oculta:** 20 neuronas con **ReLU**.
  - **Capa de salida:** 1 neurona para predecir el precio de la vivienda.

---

## **3. Creación de un `Regressor` compatible con `scikit-learn`**
```python
class PyTorchRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, epochs=100, batch_size=5, learning_rate=0.001):
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.model = WiderModel()
        self.criterion = nn.MSELoss()  # Función de pérdida: MSE
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)  # Optimizador Adam
```
- Se **crea una clase que actúa como un modelo de scikit-learn** (`BaseEstimator` y `RegressorMixin`).
- Se inicializa la **red neuronal**, el **criterio de pérdida** (MSE) y el **optimizador** (Adam).

---

## **4. Implementación del método `fit()`**
```python
    def fit(self, X, y):
        X_tensor = torch.tensor(X, dtype=torch.float32)
        y_tensor = torch.tensor(y, dtype=torch.float32)
        dataset = torch.utils.data.TensorDataset(X_tensor, y_tensor)
        dataloader = torch.utils.data.DataLoader(dataset, batch_size=self.batch_size, shuffle=True)
        
        for epoch in range(self.epochs):
            self.model.train()
            for batch_X, batch_y in dataloader:
                self.optimizer.zero_grad()
                outputs = self.model(batch_X)
                loss = self.criterion(outputs, batch_y)  # Calcular pérdida
                loss.backward()  # Retropropagación
                self.optimizer.step()  # Actualizar pesos
        return self
```
- Convierte `X` e `y` en **tensores** y los almacena en un **DataLoader**.
- Implementa **entrenamiento en mini-batches**:
  1. Activa el **modo de entrenamiento** con `self.model.train()`.
  2. Procesa los **mini-batches** de datos.
  3. Calcula la **pérdida** con `MSELoss()`.
  4. Ejecuta **retropropagación** (`loss.backward()`) y **actualiza pesos** (`optimizer.step()`).

---

## **5. Implementación del método `predict()`**
```python
    def predict(self, X):
        self.model.eval()
        X_tensor = torch.tensor(X, dtype=torch.float32)
        with torch.no_grad():
            return self.model(X_tensor).numpy()
```
- Convierte `X` en **tensor** y desactiva el cálculo de gradientes (`torch.no_grad()`).
- **Devuelve predicciones en formato numpy** para compatibilidad con `scikit-learn`.

---

## **6. Validación cruzada y evaluación del modelo**
```python
pipeline = Pipeline([
    ('standardize', StandardScaler()),  # Normalización de datos
    ('mlp', PyTorchRegressor(epochs=100, batch_size=5, learning_rate=0.001))  # Modelo de red neuronal
])

kfold = KFold(n_splits=10, shuffle=True, random_state=42)  # 10 particiones para validación cruzada
results = cross_val_score(pipeline, X, y, cv=kfold, scoring='neg_mean_squared_error')  # Evaluación

print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))
```
- **Crea un pipeline** con `StandardScaler()` y el `PyTorchRegressor()`.
- Aplica **validación cruzada con 10 folds (`KFold(n_splits=10)`)**.
- **Calcula el error cuadrático medio (MSE)** en cada fold.

---

## **Comparación con el código en Keras**
| **Componente**        | **Keras**  | **PyTorch** |
|----------------------|------------|------------|
| **Definir el modelo** | `Sequential()` con capas `Dense` | `nn.Module` con capas `Linear` |
| **Activación** | `activation="relu"` en `Dense` | `nn.ReLU()` |
| **Compilación** | `model.compile(loss="mse", optimizer="adam")` | `criterion = nn.MSELoss(); optimizer = optim.Adam()` |
| **Entrenamiento** | `model.fit(X, y, epochs=100, batch_size=5)` | `for epoch in range(epochs):` con `loss.backward()` y `optimizer.step()` |
| **Validación cruzada** | `cross_val_score(pipeline, X, Y, cv=kfold, scoring='neg_mean_squared_error')` | Igual, pero usando `PyTorchRegressor` en el pipeline |
| **Predicción** | `model.predict(X_test)` | `with torch.no_grad(): model(X_test_tensor)` |

---

## **Diferencias clave**
1. **Estructura del modelo**  
   - En **Keras**, `Sequential()` facilita la creación de modelos.
   - En **PyTorch**, se define una clase `nn.Module`, proporcionando más flexibilidad.

2. **Entrenamiento**  
   - En **Keras**, `model.fit()` maneja el entrenamiento automáticamente.
   - En **PyTorch**, se realiza manualmente con `for epoch in range(epochs)`.

3. **Integración con `scikit-learn`**  
   - En **Keras**, se usa `KerasRegressor()`.
   - En **PyTorch**, se usa `PyTorchRegressor()`, que hereda de `BaseEstimator`.

4. **Validación cruzada**  
   - En ambos casos se usa `cross_val_score()`, pero en PyTorch se requiere una clase personalizada (`PyTorchRegressor`).

---

### **Conclusión**
- **Keras** es más fácil de usar y abstracto.
- **PyTorch** ofrece más control y flexibilidad, útil para modelos más personalizados.

