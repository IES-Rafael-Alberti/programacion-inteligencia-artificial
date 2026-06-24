#!/usr/bin/python3

# Import packages
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, request, Response, abort

# Create Flask application
application = Flask(__name__)

# Load fashion mnist model
new_model = tf.keras.models.load_model('model/fashion_mnist')

def reshape_img(key):
    img = cv2.imread(f'img/{key}', 0)
    img = img / 255.0
    img = (np.expand_dims(img, 0))
    return img

# /predict endpoint
@application.route('/predict', methods=['POST'])
def predict():
    key = request.get_json()['key']
    if key is None:
        abort(400)

    img = reshape_img(key)
    prediction = new_model.predict(img)
    print(prediction.argmax())
    return Response(status=200)

# Run the app
if __name__ == "__main__":
    application.debug = True
    application.run() # Running on http://127.0.0.1:5000/