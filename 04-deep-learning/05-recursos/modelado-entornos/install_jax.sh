#!/bin/bash

# Instalación de entorno para JAX (Flax/Equinox)
# Uso: bash install_jax.sh

echo "Creando entorno conda para JAX..."

# Crear entorno
conda create -n dl_jax python=3.11 -y

# Activar entorno
conda activate dl_jax

# Instalar JAX (CPU o GPU)
# Para CPU:
pip install jax jaxlib

# Para GPU (NVIDIA):
# pip install jax[cuda12] jaxlib[cuda12]

# Instalar librerías adicionales
pip install flax equinox optax
pip install numpy pandas scikit-learn matplotlib seaborn
pip install jupyterlab ipython
pip install tensorboard

echo "Entorno dl_jax listo!"
echo "Para activar: conda activate dl_jax"
