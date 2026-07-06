import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([[1, 2, 3]])  # Entrada
Y = np.array([[0.5, 0.8]])  # Salida real

# Parámetros iniciales
W1 = np.random.randn(3, 2)  # Pesos capa oculta
b1 = np.random.randn(1, 2)  # Sesgos capa oculta
W2 = np.random.randn(2, 2)  # Pesos capa de salida
b2 = np.random.randn(1, 2)  # Sesgos capa de salida

# Forward Pass
Z1 = np.dot(X, W1) + b1
A1 = np.maximum(0, Z1)  # ReLU
Z2 = np.dot(A1, W2) + b2
Y_pred = Z2  # Regresión lineal

# Función de pérdida (MSE)
loss = np.mean((Y - Y_pred) ** 2)

# Backward Pass
dZ2 = Y_pred - Y
dW2 = np.dot(A1.T, dZ2)
db2 = np.sum(dZ2, axis=0, keepdims=True)
dA1 = np.dot(dZ2, W2.T)
dZ1 = dA1 * (Z1 > 0)  # Derivada de ReLU
dW1 = np.dot(X.T, dZ1)
db1 = np.sum(dZ1, axis=0, keepdims=True)

# Actualización de parámetros
eta = 0.1  # Tasa de aprendizaje
W1 -= eta * dW1
b1 -= eta * db1
W2 -= eta * dW2
b2 -= eta * db2

# Gráfica de la función de pérdida
plt.plot(loss, marker="o")
plt.xlabel("Iteración")
plt.ylabel("Pérdida (MSE)")
plt.title("Evolución de la Pérdida durante el Backpropagation")
plt.show()