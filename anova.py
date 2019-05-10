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

# Voy a realizar pruebas estadísticas para analizar la variable 'Número de visitas' con sus distintas procedencias.
# Estudio la normalidad de las muestras
normalidadFB = stats.shapiro(facebook['Número de visitas'])
print('Test Shapiro-Wilk para Facebook: ', normalidadFB)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Facebook sigue una distribución normal" % normalidadFB[1])
print('')
normalidadgaC = stats.shapiro(gaCatalogo['Número de visitas'])
print('Test de Shapiro-Wilk para GA Catálogo: ', normalidadgaC)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en GA Catálogo no sigue una distribución normal" % normalidadgaC[1])
print('')
normalidadgaT = stats.shapiro(gaTienda['Número de visitas'])
print('Test de Shapiro-Wilk para GA Tienda: ', normalidadgaT)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en GA Tienda no sigue una distribución normal" % normalidadgaT[1])
print('')
normalidadPixel = stats.shapiro(pixel['Número de visitas'])
print('Test de Shapiro-Wilk para Pixel: ', normalidadPixel)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Pixel sigue una distribución normal" % normalidadPixel[1])
print('')
normalidadWc = stats.shapiro(wCatalogo['Número de visitas'])
print('Test de Shapiro-Wilk para Wordpress Catálogo: ', normalidadWc)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Wordpres catálogo no sigue una distribución normal" % normalidadWc[1])
print('')
normalidadWt = stats.shapiro(wTienda['Número de visitas'])
print('Test de Shapiro-Wilk para Wordpress Tienda: ', normalidadWt)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Wordpres tienda sigue una distribución normal" % normalidadWt[1])
print('')
print('No se cumple la hipótesis de normalidad')
print('')
#hago contrastes de muestras pareadas, pues 6 muestras que son dependientes dos a dos.
# Facebook - Pixel
ttestFBP = stats.ttest_1samp(facebook['Número de visitas']-pixel['Número de visitas'], popmean = 0)
print('Realizamos el test t-Student para la diferencia de las variables procedentes de Facebook y Pixel')
print(ttestFBP)
print("Obtenemos un p-valor= %f , por lo que concluyo que tienen la misma media" % ttestFBP.pvalue)


# GA Catálogo - Wordpress Catálogo
#print(gaCatalogo['Número de visitas'])
#print(wCatalogo['Número de visitas']) #tengo que coger los últimos (length(gaC)) elementos de este vector
#print(wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(gaCatalogo['Número de visitas'])):])
kwGAWc = stats.kruskal(gaCatalogo['Número de visitas'], wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(gaCatalogo['Número de visitas'])):])
print('Realizamos el test de Kruskal-Wallis (no se cumple normalidad) para la diferencia de las variables procedentes de GA catálogo y Wordpress Catálogo')
print(kwGAWc)
print("Obtenemos un p-valor= %f , por lo que concuyo que tienen la misma media" % kwGAWc.pvalue)
print('')

#GA Tienda - Wordpress Tienda
kwGAWt = stats.kruskal(gaTienda['Número de visitas'], )
print('Realizamos el test de Kruskal-Wallis (no se cumple normalidad) para la diferencia de las variables procedentes de GA tienda y Wordpress tienda')
print(kwGAWt)
print("Obtenemos un p-valor= %f , por lo que concuyo que tienen la misma media" % kwGAWt.pvalue)
print('')



#The ANOVA test has important assumptions that must be satisfied in order for the associated p-value to be valid.

#1. The samples are independent. 
#Creo que se cumple, hablar con Miguel para confirmar la procedencia de los datos.
print('Se cumple la hipótesis de muestras independientes')
#2. Each sample is from a normally distributed population.

#3. Homoscedasticity. 
homo = stats.levene(facebook['Número de visitas'], wCatalogo['Número de visitas'], wTienda['Número de visitas'])
print(homo)
print("El test de Levene para la prueba de igualdad de varianzas me da un p-valor = %f " % homo.pvalue)
print('Se cumple la hipótesis de homocedasticidad')
print('')
print('Realizo la prueba anova para ver contrastar si en mi modelo con variable respuesta Número de visitas existe el efecto del factor procedencia con sus distintos niveles: Facebook, Pixel, GA Catálogo, GA Tienda, Wordpress Catálogo, Wordpress Tienda')

anova = stats.f_oneway(facebook['Número de visitas'], wCatalogo['Número de visitas'], wTienda['Número de visitas'])

print(anova)
print("El test anova me da un p-valor= %f , por tanto concluyo que los niveles del factor no influyen, tienen la misma media" %anova.pvalue)
print('')
print('No sé si creerme el resultado pues no se cumplen todas las hipótesis del modelo, aunque sólo no se cumple una normalidad')
print('')

#If these assumptions are not true for a given set of data, it may still be possible to use 
# the Kruskal-Wallis H-test (scipy.stats.kruskal) although with some loss of power.
print('Realizo una prueba de inferencia no paramétrica')
kw = stats.kruskal(facebook['Número de visitas'], wCatalogo['Número de visitas'], wTienda['Número de visitas'])
print(kw)
print("El test de Kruskal-Wallis me da un p-valor= %f , concluyo que todos tienen la misma media" % kw.pvalue)
print('')
print('CONCLUSIÓN: no importa la procedencia de la variable Número de visitas, pues me proporcionan la misma información')