#!/bin/bash

# Instalación de entorno para Keras 3 (multi-backend)
# Uso: bash install_keras3.sh

echo "Creando entorno conda para Keras 3..."

# Crear entorno
conda create -n dl_keras3 python=3.11 -y

# Activar entorno
conda activate dl_keras3

# Instalar Keras 3 y backends
pip install keras>=3.0
pip install tensorflow
pip install torch
pip install jax jaxlib flax optax

# Instalar librerías adicionales
pip install numpy pandas scikit-learn matplotlib seaborn
pip install jupyterlab ipython

echo "Entorno dl_keras3 listo!"
echo "Para activar: conda activate dl_keras3"
echo "Para usar con PyTorch: export KERAS_BACKEND=torch"
echo "Para usar con JAX: export KERAS_BACKEND=jax"
echo "Para usar con TensorFlow: export KERAS_BACKEND=tensorflow"
