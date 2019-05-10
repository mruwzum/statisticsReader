import pandas as pd
from statsmodels.stats.anova import AnovaRM
import numpy as np
import os
import sys
import diccionarios as dc

#Cargo todos los diccionarios
facebook = dc.diccionarioFB()
gaCatalogo = dc.diccionarioGAcatalogo()
gaTienda = dc.diccionarioGAtienda()
pixel = dc.diccionarioPixel()
wCatalogo = dc.diccionarioWcatalogo()
wTienda = dc.diccionarioWtienda()

#Las Repeated Measures son Facebook, Pixel, WTienda, gaTienda

rm = { 'Mes' : ['Oct-18','Nov-18','Dic-18','Ene-19','Feb-19'] , 'Pixel' : pixel['Número de visitas'] , 'Facebook' : facebook['Número de visitas'] , 'Wordpress Tienda' : wTienda['Número de visitas'][(len(wTienda['Número de visitas'])-len(gaTienda['Número de visitas'])):] , 'GA Tienda' : gaTienda['Número de visitas'] }
 
repeatedMeasures = pd.DataFrame(rm)

print(repeatedMeasures)

#paso de formato wide a long porque por lo visto es el que hay que usar
longRM = pd.melt(repeatedMeasures, id_vars= 'Mes', value_vars= ['Pixel','Facebook','Wordpress Tienda', 'GA Tienda'], value_name='Número de visitas', var_name='Procedencia')

print(longRM)

aovrm = AnovaRM(longRM, 'Número de visitas', 'Mes', ['Pixel','Facebook','Wordpress Tienda', 'GA Tienda'])
#ajuste = aovrm.fit()

#print(ajuste.summary())