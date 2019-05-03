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

dic = { 'Pixel' : pixel['Número de visitas'], 'Facebook' : facebook['Número de visitas' , 'Wordpress Tienda' : wTienda['Número de visitas'], 'GA Tienda' : gaTienda['Número de visitas']] }

datosnvisitas = pd.DataFrame(dic)

print(datosnvisitas)
#aovrm = AnovaRM(datosnvisitas, )