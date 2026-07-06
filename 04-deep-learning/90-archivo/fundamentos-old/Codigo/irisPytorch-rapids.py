import cudf
import cupy as cp
import torch
import torch.nn as nn
import torch.optim as optim
from cuml.model_selection import train_test_split
from cuml.preprocessing import StandardScaler

# Cargar el dataset desde UCI con cudf
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset = cudf.read_csv(url, names=names)

# Convertir las clases categóricas a valores numéricos
dataset['class'] = dataset['class'].factorize()[0]

# Separar características y etiquetas
X = dataset.iloc[:, :4]
y = dataset.iloc[:, 4]

# Dividir en conjunto de entrenamiento y prueba con cuML
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# Normalizar los datos con cuML StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convertir datos a tensores de PyTorch en GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
X_train = torch.tensor(cp.asnumpy(X_train), dtype=torch.float32).to(device)
X_test = torch.tensor(cp.asnumpy(X_test), dtype=torch.float32).to(device)
y_train = torch.tensor(cp.asnumpy(y_train), dtype=torch.long).to(device)
y_test = torch.tensor(cp.asnumpy(y_test), dtype=torch.long).to(device)

# Definir el modelo en PyTorch
class IrisNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4, 8)  # 4 entradas, 8 neuronas ocultas
        self.fc2 = nn.Linear(8, 3)  # 3 salidas (clases)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = IrisNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Entrenamiento del modelo
for epoch in range(100):
    optimizer.zero_grad()
    output = model(X_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()

# Evaluación del modelo
with torch.no_grad():
    predictions = model(X_test).argmax(dim=1)
    accuracy = (predictions == y_test).float
