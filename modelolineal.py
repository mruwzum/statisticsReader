import numpy as np 
import pandas as pd 
import os
import sys
import diccionarios as dc
from scipy import stats
from matplotlib import pyplot as plt
from sklearn import linear_model, model_selection, feature_selection, preprocessing
import statsmodels.formula.api as sm
from statsmodels.tools.eval_measures import mse
from statsmodels.tools.tools import add_constant
from sklearn.metrics import mean_squared_error

#Cargo todos los diccionarios
facebook = dc.diccionarioFB()
gaCatalogo = dc.diccionarioGAcatalogo()
gaTienda = dc.diccionarioGAtienda()
pixel = dc.diccionarioPixel()
wCatalogo = dc.diccionarioWcatalogo()
wTienda = dc.diccionarioWtienda()

print('Tras haber realizado contrastes para analizar las variables que me proporcionan información sobre la actividad de EBA,')
print('Procedemos a realizar un modelo lineal que nos explique el Número de visitas en función de las demás variables')
print('para posteriormente hacer selección de variables y mejorar la interpretabilidad y economía de mi modelo')
print('')

print('Breve estudio descriptivo:')
print('Veo la posible correlación entre las variables con Número de visitas')

print('NÚMERO DE VISITAS - VISITANTES')
plt.scatter(facebook['Visitantes'],wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(facebook['Visitantes'])):])
plt.xlabel('Visitantes')
plt.ylabel('Número de visitas')
plt.show()
print('Podemos observar que hay una relación lineal entre el número de visitas y los visitantes')
#Vemos cómo están correladas las variables
rho = stats.pearsonr(facebook['Visitantes'],wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(facebook['Visitantes'])):])

print('El coeficiente de correlación de Pearson es ',rho[0], ' con un p-valor de ', rho[1])
print('Las variables están correladas directamente')
print('')

print('NÚMERO DE VISITAS - SESIONES')
plt.scatter(pixel['Sesiones'],wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(pixel['Sesiones'])):])
plt.xlabel('Sesiones')
plt.ylabel('Número de visitas')
plt.show()
print('A simple vista parece que no hay un patrón lineal entre el número de visitas y las sesiones')
#Vemos cómo están correladas las variables
rho2 = stats.pearsonr(pixel['Sesiones'],wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(pixel['Sesiones'])):])

print('El coeficiente de correlación de Pearson es ',rho2[0], ' con un p-valor de ', rho2[1])
print('Las variables están correladas directamente')
print('')

print('NÚMERO DE VISITAS - DURACIÓN MEDIA DE LA SESIÓN')
plt.scatter(gaCatalogo['Duración media de la sesión'],wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(gaCatalogo['Duración media de la sesión'])):])
plt.xlabel('Sesiones')
plt.ylabel('Duración media de la sesión')
plt.show()
print('Parece que hay un patrón lineal entre el número de visitas y la duración media de la sesión')
#Vemos cómo están correladas las variables
rho3 = stats.pearsonr(gaCatalogo['Duración media de la sesión'],wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(pixel['Duración media de la sesión'])):])

print('El coeficiente de correlación de Pearson es ',rho3[0], ' con un p-valor de ', rho3[1])
print('Las variables están correladas directamente')
print('')

print('NÚMERO DE VISITAS - TASA DE REBOTE')
plt.scatter(pixel['Tasa de rebote'],wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(pixel['Tasa de rebote'])):])
plt.xlabel('Sesiones')
plt.ylabel('Duración media de la sesión')
plt.show()
print('No hay patrón lineal aparente entre el número de visitas y la tasa de rebote')
#Vemos cómo están correladas las variables
rho4 = stats.pearsonr(pixel['Tasa de rebote'],wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(pixel['Tasa de rebote'])):])

print('El coeficiente de correlación de Pearson es ',rho4[0], ' con un p-valor de ', rho4[1])
print('Las variables están correladas directamente')
print('')
print('')
print('Planteamos la regresión lineal:')
data_to_model = {'Número de visitas' : wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(facebook['Visitantes'])):] , 
                    'Visitantes' : facebook['Visitantes'] , 'Sesiones' : pixel['Sesiones'] , 
                    'Duración media de la sesión' : gaCatalogo['Duración media de la sesión'] , 'Tasa de rebote': pixel['Tasa de rebote']}
#print( pd.DataFrame(data_to_model).describe() )
data_to_model = pd.DataFrame(data_to_model)

#TRAINING AND TESTING THE MODEL
X = data_to_model.values.copy()
#X_train, X_valid, y_train, y_valid = cross_validation.train_test_split( X[:, :-1], X[:, -1], train_size=0.80)
#ya no existe el modulo cross_validation, ahora es model_selection INDAGAR EN ESTO