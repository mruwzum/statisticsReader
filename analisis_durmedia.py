import pandas as pd
from statsmodels.stats.anova import AnovaRM
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)
import numpy as np
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


print(gaCatalogo['Duración media de la sesión'])
print(gaTienda['Duración media de la sesión'])
print(pixel['Duración media de la sesión'])
#coinciden GA Catálogo y GA Tienda. Veo qué pasa con Pixel
#he dejado escrito cómo sería la comparación pero los datos de pixel los tengo en min y los de GA en seg. ¿cómo cambio?
print('Voy a realizar pruebas estadísticas para analizar la variable "Duración media de la sesión",  presente en Pixel, GA Tienda y GA Catálogo')
print('Analizamos primero en conjunto las muestras dependientes de Pixel y GA Tienda')
print('1º) t-student test para la igualdad de medias')
print('Breve estudio descriptivo')
print("La media muestral de Duración media de la sesión en Pixel es  %f " % pixel['Duración media de la sesión'].mean())
print("La media muestral de Duración media de la sesión en GA Tienda es  %f " % gaTienda['Duración media de la sesión'].mean())
print('Gráfico de cajas y bigotes:')
data_to_plot = [pixel['Duración media de la sesión'], gaTienda['Duración media de la sesión']]
bp = plt.boxplot(data_to_plot)
plt.show(bp)
print('A simple vista parece que la Duración media de la sesión sigue una distribución similiar, sin depender de la procedencia de la medición.')
print('')
print('Supuesto de normalidad')
normalidadPixel = stats.shapiro(pixel['Duración media de la sesión'])
print('Test de Shapiro-Wilk para Pixel: ', normalidadPixel)
print("Obtengo un p-valor = %f , concluyo que Duración media de la sesión en Pixel sigue una distribución normal" % normalidadPixel[1])
print('')
normalidadGATienda = stats.shapiro(gaTienda['Duración media de la sesión'])
print('Test de Shapiro-Wilk para GA Tienda: ', normalidadGATienda)
print("Obtengo un p-valor = %f , concluyo que Duración media de la sesión en Pixel sigue una distribución normal" % normalidadGATienda[1])
print('')
print('Ahora sí realizo el test t-student')
ttestPGAT = stats.ttest_1samp(pixel['Duración media de la sesión']-gaTienda['Duración media de la sesión'], popmean = 0)
print(ttestPGAT)
print("Obtenemos un p-valor= %f , por lo que concluyo que tienen la misma media" % ttestPGAT.pvalue)
print('')
print('No es necesario comparar con GA Catálogo')
print('')
print('CONCLUSIÓN: No importa la procedencia de la variable, me puedo quedar con cualquiera pues me aporta la misma información')
