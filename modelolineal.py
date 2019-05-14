import numpy as np 
import pandas as pd 
import os
import sys
import diccionarios as dc
from scipy import stats
from matplotlib import pyplot as plt

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
plt.scatter(facebook['Visitantes'],wCatalogo['Número de visitas'])
plt.xlabel('Visitantes')
plt.ylabel('Número de visitas')
plt.show()
print('Podemos observar que hay una relación lineal entre el número de visitas y los visitantes')
#Vemos cómo están correladas las variables
rho = stats.pearsonr(facebook['Visitantes'],facebook['Número de visitas'])

print('El coeficiente de correlación de Pearson es ',rho[0], ' con un p-valor de ', rho[1])
print('')
print('Las variables están claramente correladas directamente')
