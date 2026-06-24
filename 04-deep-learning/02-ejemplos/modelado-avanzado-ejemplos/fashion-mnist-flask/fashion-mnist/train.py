#!/usr/bin/python3

import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images,
                               test_labels) = keras.datasets.fashion_mnist.load_data()

# Output: (60000, 28, 28)
train_images.shape

# Output: 60000
len(train_labels)

# Output: (10000, 28, 28)
test_images.shape

# Output: 1000
len(test_labels)

# Output: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8)
np.unique(train_labels)

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(512, activation='relu', kernel_initializer='he_uniform'),
    keras.layers.Dense(10, activation='softmax')
])
model.summary()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, batch_size=64, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=0)

print('\nTest loss:', test_loss)
print('\nTest accuracy:', test_acc)

predictions = model.predict(test_images)
np.argmax(predictions[1])

test_labels[1]

model.save('model/fashion_mnist')