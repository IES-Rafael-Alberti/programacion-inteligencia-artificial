import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.metrics import mean_squared_error

# Cargar el dataset
dataframe = pd.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values

# Separar variables predictoras y objetivo
X = dataset[:, 0:13]  # Las primeras 13 columnas son las características
y = dataset[:, 13].reshape(-1, 1)  # La última columna es la variable objetivo

# Normalizar los datos
scaler = StandardScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y)

# Convertir a tensores de PyTorch
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)

# Definir el modelo en PyTorch
class WiderModel(nn.Module):
    def __init__(self):
        super(WiderModel, self).__init__()
        self.fc1 = nn.Linear(13, 20)  # Capa oculta con 20 neuronas y activación ReLU
        self.fc2 = nn.Linear(20, 1)   # Capa de salida
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))  # Aplicar función de activación ReLU
        x = self.fc2(x)  # Capa de salida sin activación
        return x

# Crear una clase para integrar el modelo de PyTorch con scikit-learn
class PyTorchRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, epochs=100, batch_size=5, learning_rate=0.001):
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.model = WiderModel()
        self.criterion = nn.MSELoss()  # Función de pérdida: Error cuadrático medio
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)  # Optimizador Adam
    
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
    
    def predict(self, X):
        self.model.eval()
        X_tensor = torch.tensor(X, dtype=torch.float32)
        with torch.no_grad():
            return self.model(X_tensor).numpy()  # Predicción sin calcular gradientes

# Crear pipeline con normalización y modelo de PyTorch
pipeline = Pipeline([
    ('standardize', StandardScaler()),  # Normalización de datos
    ('mlp', PyTorchRegressor(epochs=100, batch_size=5, learning_rate=0.001))  # Modelo de red neuronal
])

# Validación cruzada con 10 particiones
kfold = KFold(n_splits=10, shuffle=True, random_state=42)  # KFold para validación cruzada
results = cross_val_score(pipeline, X, y, cv=kfold, scoring='neg_mean_squared_error')  # Evaluación del modelo

# Mostrar el error cuadrático medio (MSE) medio y desviación estándar
print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))