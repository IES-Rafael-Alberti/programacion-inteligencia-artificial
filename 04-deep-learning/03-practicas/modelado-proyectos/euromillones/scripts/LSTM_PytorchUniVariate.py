
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Definir la arquitectura de la red LSTM


class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
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

# Crear un conjunto de datos personalizado


class TimeSeriesDataset(Dataset):
    def __init__(self, data, sequence_length):
        self.data = data
        self.sequence_length = sequence_length

    def __len__(self):
        return len(self.data) - self.sequence_length

    def __getitem__(self, idx):
        x = self.data[idx:idx+self.sequence_length]
        y = self.data[idx+self.sequence_length]
        return x, y


# Parámetros del modelo y entrenamiento
input_size = 1
hidden_size = 32
num_layers = 2
output_size = 1
sequence_length = 10
batch_size = 16
num_epochs = 100

# Crear el modelo LSTM
model = LSTMModel(input_size, hidden_size, num_layers, output_size)

# Definir la función de pérdida y el optimizador
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Preparar los datos de entrenamiento
# Ejemplo de datos de series temporales
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
dataset = TimeSeriesDataset(data, sequence_length)
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

# Ejemplo de predicción
test_data = [16, 17, 18, 19, 20]  # Datos para la predicción
model.eval()
with torch.no_grad():
    test_inputs = torch.tensor(test_data).unsqueeze(0).unsqueeze(-1)
    predicted_output = model(test_inputs)
    print(f'Predicted output: {predicted_output.item()}')
