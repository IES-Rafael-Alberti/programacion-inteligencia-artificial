#!/bin/bash

# Instalación de entorno para MLX (Apple Silicon)
# Uso: bash install_mlx.sh
# Nota: Requiere Mac con chip M1/M2/M3

echo "Creando entorno para MLX (solo Apple Silicon)..."

# Verificar que es Apple Silicon
if [[ $(uname -m) != 'arm64' ]]; then
    echo "Error: MLX solo funciona en Apple Silicon (M1/M2/M3)"
    exit 1
fi

# Crear entorno
conda create -n dl_mlx python=3.11 -y

# Activar entorno
conda activate dl_mlx

# Instalar MLX
pip install mlx

# Instalar MLX para LLMs
pip install mlx-lm

# Instalar librerías adicionales
pip install numpy pandas scikit-learn
pip install jupyterlab ipython

echo "Entorno dl_mlx listo!"
echo "Para activar: conda activate dl_mlx"
