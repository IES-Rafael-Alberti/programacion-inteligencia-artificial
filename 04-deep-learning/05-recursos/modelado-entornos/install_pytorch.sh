#!/bin/bash

# Instalación de entorno para Deep Learning con PyTorch
# Uso: bash install_pytorch.sh

echo "Creando entorno conda para PyTorch..."

# Crear entorno
conda create -n dl_pytorch python=3.11 -y

# Activar entorno
conda activate dl_pytorch

# Instalar PyTorch
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y

# Instalar librerías adicionales
pip install numpy pandas scikit-learn matplotlib seaborn
pip install jupyterlab ipython
pip install torchinfo tensorboard
pip install optuna neptune-api

echo "Entorno dl_pytorch listo!"
echo "Para activar: conda activate dl_pytorch"
