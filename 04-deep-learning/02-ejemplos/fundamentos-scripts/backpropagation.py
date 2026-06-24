import numpy as np
import matplotlib.pyplot as plt

class RedNeuronalVisual:
    def __init__(self, capas):
        """
        capas: lista con número de neuronas por capa
        Ej: [2, 3, 1] = 2 entradas, 3 neuronas ocultas, 1 salida
        """
        self.num_capas = len(capas)
        self.capas = capas
        
        # Inicializar pesos y sesgos aleatoriamente
        self.pesos = [np.random.randn(capas[i], capas[i+1]) * 0.5 
                      for i in range(len(capas)-1)]
        self.sesgos = [np.random.randn(1, capas[i+1]) * 0.5 
                       for i in range(len(capas)-1)]
        
        # Para almacenar valores intermedios
        self.activaciones = []
        self.z_valores = []
        
    def sigmoid(self, z):
        """Función de activación sigmoid"""
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))
    
    def sigmoid_derivada(self, z):
        """Derivada de sigmoid"""
        s = self.sigmoid(z)
        return s * (1 - s)
    
    def feedforward(self, X, verbose=False):
        """Propagación hacia adelante"""
        self.activaciones = [X]
        self.z_valores = []
        
        if verbose:
            print("\n=== FEEDFORWARD ===")
            print(f"Entrada: {X}")
        
        activacion = X
        for i, (W, b) in enumerate(zip(self.pesos, self.sesgos)):
            z = np.dot(activacion, W) + b
            self.z_valores.append(z)
            activacion = self.sigmoid(z)
            self.activaciones.append(activacion)
            
            if verbose:
                print(f"\nCapa {i+1}:")
                print(f"  z = X·W + b = {z}")
                print(f"  a = sigmoid(z) = {activacion}")
        
        return activacion
    
    def calcular_perdida(self, y_pred, y_real, verbose=False):
        """Error cuadrático medio (MSE)"""
        perdida = np.mean((y_pred - y_real) ** 2)
        if verbose:
            print(f"\n=== FUNCIÓN DE PÉRDIDA ===")
            print(f"Predicción: {y_pred}")
            print(f"Real: {y_real}")
            print(f"MSE = {perdida}")
        return perdida
    
    def backpropagation(self, X, y, verbose=False):
        """Propagación hacia atrás del error"""
        m = X.shape
        
        # Gradientes
        dW = [np.zeros_like(w) for w in self.pesos]
        db = [np.zeros_like(b) for b in self.sesgos]
        
        if verbose:
            print("\n=== BACKPROPAGATION ===")
        
        # Error en la capa de salida
        delta = (self.activaciones[-1] - y) * self.sigmoid_derivada(self.z_valores[-1])
        delta = np.atleast_2d(delta)  # Asegurar que sea 2D
        
        if verbose:
            print(f"\nCapa de salida:")
            print(f"  δ = (a - y) * σ'(z) = {delta}")
            print(f"  Forma de δ: {delta.shape}")
        
        # Retropropagar el error
        for i in range(self.num_capas - 2, -1, -1):
            # Asegurar que activaciones[i] sea 2D
            a_i = np.atleast_2d(self.activaciones[i])
            
            # Asegurar que delta sea 2D
            delta = np.atleast_2d(delta)
            
            dW[i] = np.dot(a_i.T, delta) / m
            db[i] = np.sum(delta, axis=0, keepdims=True) / m
            
            if verbose:
                print(f"\nGradientes capa {i+1}:")
                print(f"  dW forma: {dW[i].shape}, valores:")
                print(f"  db forma: {db[i].shape}, valores:\n{db[i]}")
            
            if i > 0:
                # Propagar error a la capa anterior (regla de la cadena)
                delta = np.dot(delta, self.pesos[i].T) * self.sigmoid_derivada(self.z_valores[i-1])
                delta = np.atleast_2d(delta)  # Asegurar que sea 2D
                
                if verbose:
                    print(f"  δ anterior = {delta}")
        
        return dW, db
    
    def actualizar_pesos(self, dW, db, tasa_aprendizaje, verbose=False):
        """Gradiente descendente: actualizar pesos y sesgos"""
        if verbose:
            print("\n=== ACTUALIZACIÓN DE PESOS ===")
            print(f"Tasa de aprendizaje: {tasa_aprendizaje}")
        
        for i in range(len(self.pesos)):
            if verbose:
                print(f"\nCapa {i+1}:")
                print(f"  W_anterior = {self.pesos[i]}")
            
            self.pesos[i] -= tasa_aprendizaje * dW[i]
            self.sesgos[i] -= tasa_aprendizaje * db[i]
            
            if verbose:
                print(f"  W_nuevo = {self.pesos[i]}")
    
    def entrenar_paso_a_paso(self, X, y, tasa_aprendizaje=0.5):
        """Un paso completo de entrenamiento con explicaciones"""
        print("\n" + "="*60)
        print("PASO DE ENTRENAMIENTO COMPLETO")
        print("="*60)
        
        # 1. Feedforward
        y_pred = self.feedforward(X, verbose=True)
        
        # 2. Calcular pérdida
        perdida = self.calcular_perdida(y_pred, y, verbose=True)
        
        # 3. Backpropagation
        dW, db = self.backpropagation(X, y, verbose=True)
        
        # 4. Actualizar pesos
        self.actualizar_pesos(dW, db, tasa_aprendizaje, verbose=True)
        
        return perdida
    
    def entrenar(self, X, y, epocas=1000, tasa_aprendizaje=0.5, mostrar_cada=100):
        """Entrenamiento completo"""
        historial_perdidas = []
        
        for epoca in range(epocas):
            y_pred = self.feedforward(X)
            perdida = self.calcular_perdida(y_pred, y)
            historial_perdidas.append(perdida)
            
            dW, db = self.backpropagation(X, y)
            self.actualizar_pesos(dW, db, tasa_aprendizaje)
            
            if epoca % mostrar_cada == 0:
                print(f"Época {epoca}: Pérdida = {perdida:.6f}")
        
        return historial_perdidas


# ===== EJEMPLO DE USO =====
if __name__ == "__main__":
    print("EJEMPLO: Aprender la función XOR")
    print("="*60)
    
    # Datos de entrenamiento (XOR)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])
    
    # Crear red: 2 entradas, 4 neuronas ocultas, 1 salida
    red = RedNeuronalVisual([2, 4, 1])
    
    # Entrenar PASO A PASO (primeros 3 pasos)
    print("\n\n### ENTRENAMIENTO PASO A PASO ###")
    for paso in range(3):
        print(f"\n\n{'#'*60}")
        print(f"### ITERACIÓN {paso + 1} ###")
        print(f"{'#'*60}")
        perdida = red.entrenar_paso_a_paso(X, y, tasa_aprendizaje=0.5)
    
    # Entrenar el resto sin detalles
    print("\n\n### CONTINUANDO ENTRENAMIENTO... ###")
    historial = red.entrenar(X, y, epocas=5000, tasa_aprendizaje=0.5, mostrar_cada=1000)
    
    # Resultados finales
    print("\n\n### RESULTADOS FINALES ###")
    y_pred = red.feedforward(X)
    for i in range(len(X)):
        print(f"Entrada: {X[i]} -> Predicción: {y_pred[i]:.4f} (Real: {y[i]})")
    
    # Graficar pérdida
    plt.figure(figsize=(10, 5))
    plt.plot(historial)
    plt.title('Evolución de la Pérdida durante el Entrenamiento')
    plt.xlabel('Época')
    plt.ylabel('Pérdida (MSE)')
    plt.grid(True)
    plt.show()