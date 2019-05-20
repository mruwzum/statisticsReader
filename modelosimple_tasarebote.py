import numpy as np 
import pandas as pd 
import os
import sys
import diccionarios as dc
from scipy import stats
from matplotlib import pyplot as plt

#Cargo todos los diccionarios
facebook = dc.diccionarioFB()
pixel = dc.diccionarioPixel()

#Estudio las visitas (modelo lineal simple)
#Estudio descriptivo
plt.scatter(pixel['Tasa de rebote'],facebook['Número de visitas'])
plt.xlabel('Tasa de rebote')
plt.ylabel('Número de visitas')
plt.show()
print('Podemos observar que no hay una relación lineal entre el número de visitas y las sesiones')
#Vemos cómo están correladas las variables
rho = stats.pearsonr(pixel['Tasa de rebote'],facebook['Número de visitas'])

print('El coeficiente de correlación de Pearson es ',rho[0])
print('')
print('Las variable están poco correladas')
print('Planteamos la regresión lineal con las sesiones como variable explicativa, y el número de visitas como variable respuesta')
#regresión lineal simple
regr = stats.linregress(facebook['Número de visitas'].astype(float),pixel['Tasa de rebote'].astype(float))
print('Mi modelo es: ', "visitas = %f + %f*tasa de rebote" % (regr.intercept, regr.slope))
print('Observemos la bondad del ajuste: ', "R-cuadrado = %f" % regr.rvalue**2)
print('Mi modelo explica el 53% de la variabilidad de las visitas')
print("error estandarizado %f" % regr.stderr)
#Gráfica de los datos con la recta de regresión
plt.plot(pixel['Tasa de rebote'],facebook['Número de visitas'], 'o', label='original data')
x = pixel['Tasa de rebote']
y = regr.intercept + regr.slope*x
plt.plot(x, y, 'r', label='fitted line')
#TODO: Mirar la recta b0 +b1*x 
plt.legend()
plt.show()

print('')
print('La tasa de rebote no sirven para modelar por sí solas el número de visitas')