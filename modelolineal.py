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
                    'Visitantes' : facebook['Visitantes'] , 
                    'Sesiones' : pixel['Sesiones'] , 
                    'Duración media de la sesión' : gaCatalogo['Duración media de la sesión'] , 
                    'Tasa de rebote': pixel['Tasa de rebote']}
#print( pd.DataFrame(data_to_model).describe() )
data_to_model = pd.DataFrame(data_to_model)

#TRAINING AND TESTING THE MODEL
print('Dividimos la muestra en aprendizaje-validación mediante validación cruzada')
#We first convert the data frame into an array structure using values.copy() of data_to_model
variables = data_to_model.values.copy()
X = variables[:,1:]
y = variables[:,0]
#We then use the train_test_split function of model_selection from sklearn to divide the data into training and test set for 60% of the data.
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.60, random_state=0)
print('La muestra de aprendizaje es:')
print((X_train, y_train))
print('La muestra de validación es:')
print((X_test, y_test))

#LINEAR REGRESSION
print('Hacemos la regresión lineal y obtengo los coeficientes:')
model = linear_model.LinearRegression(fit_intercept=True).fit(X_train, y_train)
print('Intercept is %f' % model.intercept_)
coeficientes = pd.DataFrame(zip(data_to_model.columns[1:] , model.coef_), columns = ['features','estimatedCoefficients'])
print(coeficientes)

#r square
print('Estudio la bondad de mi ajuste')
r2 = model.score(X_test,y_test)
print("Obtengo un R^2 con un valor de %f " % r2)
print("Mi modelo explica la variabilidad del Número de visitas en un 41%")

#mean squared error
ypred = model.predict(X_test)
print("Y la media de los cuadrados de los errores es %f" % mean_squared_error(ypred,y_test) )
print('Es un error bastante grande')

#the actual versus the predicted plot
fig, ax = plt.subplots(1, 1)
ax.scatter(y_test, ypred)
ax.set_xlabel('Actual')
ax.set_ylabel('Predicted')
plt.show()

#feature selection
print('Hacemos selección de variables para ver si mejora mi modelo')
#feature_selection.SelectKBest(score_func=<function f_classif>, k=4)