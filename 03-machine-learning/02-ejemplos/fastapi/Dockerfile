# Dockerfile – API FastAPI con modelo de ML

FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar dependencias y código
COPY requirements.txt .
COPY main.py ./main.py
COPY outputs/ ./outputs

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
