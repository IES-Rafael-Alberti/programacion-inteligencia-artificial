import numpy as np
import matplotlib.pyplot as plt
import sys

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.maximum(alpha * x, x)

def softplus(x):
    return np.log(1 + np.exp(x))

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

# a function that receives an ax of a plot with subplot and a function, and plots the function on the subplot, and returns the subplot
def plot_function_on_ax(func, ax, x,xlabel="Entrada", ylabel="Salida",color="c", label=""):
    ax.axhline(0, color='black', linewidth=.5)
    ax.axvline(0, color='black', linewidth=.5)
    ax.grid(True, which='both')
    ax.plot(x, func(x), color, label=label)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    #return ax



def plot_function_on_subplot(func, subplot_pos, x,color, label):
    fig, ax = plt.subplots(2, 3, figsize=(15, 10))

    subplot_row, subplot_col = subplot_pos

    ax[subplot_row, subplot_col].axhline(0, color='black', linewidth=.5)
    ax[subplot_row, subplot_col].axvline(0, color='black', linewidth=.5)
    ax[subplot_row, subplot_col].grid(True, which='both')
    ax[subplot_row, subplot_col].plot(x, func(x), 'c')
    ax[subplot_row, subplot_col].set(xlabel="Entrada", ylabel="Salida")
    plt.show()

def plot_activation_functions(x):
    fig, ax = plt.subplots(2, 3, figsize=(15, 10))

    ax[0, 0].axhline(0, color='black', linewidth=.5)
    ax[0, 0].axvline(0, color='black', linewidth=.5)
    ax[0, 0].grid(True, which='both')
    ax[0, 0].plot(x, sigmoid(x), 'r', label='Sigmoid')
    ax[0, 0].legend()

    ax[0, 1].axhline(0, color='black', linewidth=.5)
    ax[0, 1].axvline(0, color='black', linewidth=.5)
    ax[0, 1].grid(True, which='both')
    ax[0, 1].plot(x, tanh(x), 'g', label='Tanh')
    ax[0, 1].legend()

    ax[0, 2].axhline(0, color='black', linewidth=.5)
    ax[0, 2].axvline(0, color='black', linewidth=.5)
    ax[0, 2].grid(True, which='both')
    ax[0, 2].plot(x, relu(x), 'b', label='ReLU')
    ax[0, 2].legend()

    ax[1, 0].axhline(0, color='black', linewidth=.5)
    ax[1, 0].axvline(0, color='black', linewidth=.5)
    ax[1, 0].grid(True, which='both')
    ax[1, 0].plot(x, leaky_relu(x), 'y', label='Leaky ReLU')
    ax[1, 0].legend()

    ax[1, 1].axhline(0, color='black', linewidth=.5)
    ax[1, 1].axvline(0, color='black', linewidth=.5)
    ax[1, 1].grid(True, which='both')
    ax[1, 1].plot(x, softplus(x), 'c', label='Softplus')
    ax[1, 1].legend()

    ax[1, 2].axhline(0, color='black', linewidth=.5)
    ax[1, 2].axvline(0, color='black', linewidth=.5)
    ax[1, 2].grid(True, which='both')
    ax[1, 2].plot(x, softmax(x), 'c', label='SoftMax')
    ax[1, 2].legend()
    ax[1, 2].set(xlabel="Entrada",ylabel="Probabilidad")
    plt.show()
    plt.savefig(sys.stdout.buffer)


x = np.linspace(-5, 5, num=100)
x = np.arange(-5, 5, 0.1)
listOfFunctions = [sigmoid, tanh, relu, leaky_relu, softplus, softmax]
dictOfFunctionLabel = {sigmoid: "Sigmoid", tanh: "Tanh", relu: "ReLU",  leaky_relu: "Leaky ReLU", softplus: "Softplus", softmax: "Softmax"}
dictOfFunctionColor = {sigmoid: "r", tanh: "g", relu: "b",  leaky_relu: "y", softplus: "c", softmax: "m"}
xlabel = "Entrada"
fig, ax = plt.subplots(2, 3, figsize=(15, 10))
for f in listOfFunctions:
    ylabel = "Salida" if f is not softmax else "Probabilidad"
    plot_function_on_ax(f,
    ax[listOfFunctions.index(f)//3,
    listOfFunctions.index(f) % 3],
    x, xlabel, ylabel,
    dictOfFunctionColor[f], dictOfFunctionLabel[f])
plt.show()

#plot_activation_functions(x)