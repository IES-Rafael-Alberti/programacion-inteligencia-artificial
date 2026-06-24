#!/bin/bash

# Instalación de entorno para TensorFlow (standalone)
# Uso: bash install_tensorflow.sh

echo "Creando entorno conda para TensorFlow..."

# Crear entorno
conda create -n dl_tensorflow python=3.11 -y

# Activar entorno
conda activate dl_tensorflow

# Instalar TensorFlow (CPU o GPU)
pip install tensorflow

# Para GPU:
# pip install tensorflow[and-cuda]

# Instalar TensorFlow Addons y extensiones
pip install tensorflow-addons
pip install tensorflow-hub
pip install tensorflow-datasets

# Instalar librerías adicionales
pip install numpy pandas scikit-learn matplotlib seaborn
pip install jupyterlab ipython

echo "Entorno dl_tensorflow listo!"
echo "Para activar: conda activate dl_tensorflow"
