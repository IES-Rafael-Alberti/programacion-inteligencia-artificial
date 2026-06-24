#https://www.pluralsight.com/guides/regression-keras

#El dataset de Boston Housing Price es un dataset de 506 muestras y 13 atributos.
#El atributo MEDV es el valor medio de las viviendas en miles de dólares.
#El objetivo es predecir el valor medio de las viviendas en Boston en función de los atributos del dataset (MEDV).
#El dataset se puede descargar de https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data
#El dataset se puede cargar con la función read_csv de pandas.  El dataset no tiene encabezado, por lo que se especifica header=None.
#El dataset no tiene separadores, por lo que se especifica delim_whitespace=True o  delimiter=r"\s+".
#El dataset no tiene nombres de columnas, por lo que se especifica names=column_names.
#Con column_names se especifican los nombres de las columnas, que son: 
# CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT, MEDV.
#La descripción está en el fichero BostonHousingDesc.txt.
#El dataset no tiene índices, por lo que se especifica index_col=None.
#El dataset no tiene valores faltantes, por lo que no es necesario tratarlos.
#El dataset no tiene valores atípicos, por lo que no es necesario tratarlos.
#El dataset no tiene valores categóricos, por lo que no es necesario tratarlos.


# Import required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
# Keras specific
import keras
from keras.models import Sequential
from keras.layers import Dense

#Ponemos nombre a las columnas y cargamos el dataset
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df = pd.read_csv("housing.csv",  delimiter=r"\s+", header=None, names=column_names)
print(df.shape)
df.describe()
#Ponemos com target la columna MEDV
target_column = ['MEDV'] 
#Separamos el target de los predictores
predictors = list(set(list(df.columns))-set(target_column))
df[predictors] = df[predictors]/df[predictors].max()
df.describe()

#Separamos el dataset en train y test
X = df[predictors].values
y = df[target_column].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
print(X_train.shape); print(X_test.shape)


# Definimos el modelo
model = Sequential()
model.add(Dense(500, input_dim=13, activation= "relu"))
model.add(Dense(100, activation= "relu"))
model.add(Dense(50, activation= "relu"))
model.add(Dense(1))
model.summary() #Print model Summary

# Compilamos el modelo con el optimizador Adam y la función de pérdida MSE
model.compile(loss= "mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])
# Entrenamos el modelo
model.fit(X_train, y_train, epochs=20)

# Evaluamos el modelo con los datos de entrenamiento y de test
#Entrenamiento
pred_train= model.predict(X_train)
print(np.sqrt(mean_squared_error(y_train,pred_train)))
#Test
pred= model.predict(X_test)
print(np.sqrt(mean_squared_error(y_test,pred))) 