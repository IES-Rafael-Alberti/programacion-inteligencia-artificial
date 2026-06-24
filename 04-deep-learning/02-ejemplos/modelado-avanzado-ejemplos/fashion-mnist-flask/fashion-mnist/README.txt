## Instrucciones para la ejecución del caso práctico

### Pasos

1. python3 -m virtualenv .
2. source bin/activate
3. pip3 install -r requirements.txt
4. python3 train.py
5. python3 application.py
6. Utiliza alguna de las imágenes de la carpeta /imgs
7. Por ejemplol, ejecuta: curl -H "Content-Type: application/json" -X POST -d '{"key": "dress.png"}' localhost:5000/predict