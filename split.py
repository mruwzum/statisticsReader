import numpy as np 
import pandas as pd 
import os
import sys
import diccionarios as dc
from scipy import stats
from matplotlib import pyplot as plt
from sklearn import linear_model, model_selection, feature_selection
from sklearn.metrics import mean_squared_error, r2_score

#Cargo todos los diccionarios
facebook = dc.diccionarioFB()
gaCatalogo = dc.diccionarioGAcatalogo()
gaTienda = dc.diccionarioGAtienda()
pixel = dc.diccionarioPixel()
wCatalogo = dc.diccionarioWcatalogo()
wTienda = dc.diccionarioWtienda()

data_to_model = {'Número de visitas' : wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(facebook['Visitantes'])):] , 
                    'Visitantes' : facebook['Visitantes'] , 
                    'Sesiones' : pixel['Sesiones'] , 
                    'Duración media de la sesión' : gaCatalogo['Duración media de la sesión'] , 
                    'Tasa de rebote': pixel['Tasa de rebote']}
data_to_model = pd.DataFrame(data_to_model)

print(data_to_model)
print('Dividimos la muestra en aprendizaje-validación mediante validación cruzada')
X = data_to_model.values.copy()

X_train, X_test, y_train, y_test = model_selection.train_test_split(X[:, :-1], X[:, -1], train_size=0.60, random_state=0)
print('La muestra de aprendizaje es:')
print((X_train, y_train))
print('La muestra de validación es:')
print((X_test, y_test))

lm = linear_model.LinearRegression()
# Train the model using the training sets
lm.fit(X_train, y_train)
coeficientes = pd.DataFrame(zip(data_to_model.columns,lm.coef_), columns = ['features','estimatedCoefficients'])
print(coeficientes)