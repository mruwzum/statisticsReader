import numpy as np 
import pandas as pd 
import os
import sys
import diccionarios as dc
from scipy import stats
from matplotlib import pyplot as plt

#Cargo todos los diccionarios
facebook = dc.diccionarioFB()

#Estudio las visitas (modelo lineal simple)
#Estudio descriptivo
plt.scatter(facebook['Visitantes'],facebook['Número de visitas'])
plt.xlabel('Visitantes')
plt.ylabel('Número de visitas')
plt.show()
print('Podemos observar que hay una relación lineal entre el número de visitas y los visitantes')
#Vemos cómo están correladas las variables
rho = stats.pearsonr(facebook['Visitantes'],facebook['Número de visitas'])

print('El coeficiente de correlación de Pearson es ',rho[0])
print('')
print('Las variables están claramente correladas directamente')
print('Planteamos la regresión lineal con los visitantes como variable explicativa, y el número de visitas como variable respuesta')
#regresión lineal simple
regr = stats.linregress(facebook['Número de visitas'].astype(float),facebook['Visitantes'].astype(float))
print('Mi modelo es: ', "visitas = %f + %f*visitantes" % (regr.intercept, regr.slope))
print('Observemos la bondad del ajuste: ', "R-cuadrado = %f" % regr.rvalue**2)
print('Mi modelo explica el 88% de la variabilidad de las visitas')
print("error estandarizado %f" % regr.stderr)
#Gráfica de los datos con la recta de regresión
plt.plot(facebook['Visitantes'],facebook['Número de visitas'], 'o', label='original data')
x = facebook['Visitantes']
y = regr.intercept + regr.slope*x
plt.plot(x, y, 'r', label='fitted line')
#TODO: Mirar la recta b0 +b1*x 
plt.legend()
plt.show()