import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Definir la arquitectura de la red LSTM multivariable


class MultivariateLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(MultivariateLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size,
                            num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(
            0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(
            0), self.hidden_size).to(x.device)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])

        return out

# Crear un conjunto de datos personalizado para series temporales multivariables


class MultivariateTimeSeriesDataset(Dataset):
    def __init__(self, data, sequence_length):
        self.data = data
        self.sequence_length = sequence_length

    def __len__(self):
        return len(self.data) - self.sequence_length

    def __getitem__(self, idx):
        # Todas las características excepto la última columna
        x = self.data[idx:idx+self.sequence_length, :-1]
        # Última columna (variable objetivo)
        y = self.data[idx+self.sequence_length, -1]
        return x, y


# Parámetros del modelo y entrenamiento
input_size = 3  # Número de características en los datos de entrada
hidden_size = 32
num_layers = 2
output_size = 1  # Número de características en la salida (variable objetivo)
sequence_length = 10
batch_size = 16
num_epochs = 100

# Crear el modelo LSTM multivariable
model = MultivariateLSTM(input_size, hidden_size, num_layers, output_size)

# Definir la función de pérdida y el optimizador
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Preparar los datos de entrenamiento
data = [[1, 2, 3, 10], [2, 4, 6, 20], [3, 6, 9, 30], [4, 8, 12, 40], [
    5, 10, 15, 50]]  # Ejemplo de datos de serie temporal multivariable
dataset = MultivariateTimeSeriesDataset(data, sequence_length)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Entrenamiento del modelo
for epoch in range(num_epochs):
    for inputs, targets in dataloader:
        inputs = inputs.unsqueeze(-1)
        targets = targets.unsqueeze(-1)

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # Backward pass y optimización
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f'Epoch: {epoch+1}/{num_epochs}, Loss: {loss.item()}')

# Ejemplo de predicción para una nueva secuencia de entrada
# Ejemplo de predicción para una nueva secuencia de entrada
# Nueva secuencia de entrada para predecir la variable objetivo
new_data = [[6, 12, 18, 60], [7, 14, 21, 70], [8, 16, 24, 80]]
model.eval()
with torch.no_grad():
    # Agregar una dimensión adicional para el lote
    test_inputs = torch.tensor(new_data).unsqueeze(0)
    predicted_output = model(test_inputs)
    print(f'Predicted output: {predicted_output.item()}')
