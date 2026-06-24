#!/bin/bash

# Instalación de entorno para ONNX (Deployment)
# Uso: bash install_onnx.sh

echo "Creando entorno conda para ONNX..."

# Crear entorno
conda create -n dl_onnx python=3.11 -y

# Activar entorno
conda activate dl_onnx

# Instalar ONNX y ONNX Runtime
pip install onnx
pip install onnxruntime

# Instalar herramientas adicionales
pip install onnxoptimizer
pip install onnxsim
pip install tf2onnx
pip install skl2onnx

# Instalar FastAPI para deployment
pip install fastapi uvicorn

# Instalar librerías adicionales
pip install numpy pandas scikit-learn
pip install torch tensorflow keras

echo "Entorno dl_onnx listo!"
echo "Para activar: conda activate dl_onnx"
