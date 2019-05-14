import pandas as pd
from statsmodels.stats.anova import AnovaRM
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


print('Voy a realizar pruebas estadísticas para analizar la variable "Número de visitas" con sus distintas procedencias.')
print('Me encuentro con que tengo un experimento con muestras repetidas: las mediciones de Pixel, Facebook, GA Tienda y Wordpress Tienda toman datos de la misma web (Wordpress Tienda).')
print('Por otro lado, también tengo muestras pareadas en GA Catálogo y Wordpress Catálogo. También los analizaremos juntos.')
print('Analizaremos los dos subconjuntos independientes por separado, para luego establecer conclusiones en común')
print('')
print('1º) ANOVA Repeated Measures')
print('Manipulación de los datos y descriptivos')

rm = { 'Mes' : ['Oct-18','Nov-18','Dic-18','Ene-19','Feb-19'] , 'Pixel' : pixel['Número de visitas'] , 'Facebook' : facebook['Número de visitas'] , 'Wordpress Tienda' : wTienda['Número de visitas'][(len(wTienda['Número de visitas'])-len(gaTienda['Número de visitas'])):] , 'GA Tienda' : gaTienda['Número de visitas'] }
repeatedMeasures = pd.DataFrame(rm)
print(repeatedMeasures)
#paso de formato wide a long porque por lo visto es el que hay que usar
longRM = pd.melt(repeatedMeasures, id_vars= 'Mes', value_vars= ['Pixel','Facebook','Wordpress Tienda', 'GA Tienda'], value_name='Número de visitas', var_name='Procedencia')
print(longRM)

print('')
print('Gráfico de cajas y bigotes:')
data_to_plot = [rm['Pixel'], rm['Facebook'], rm['Wordpress Tienda'], rm['GA Tienda']]
bp = plt.boxplot(data_to_plot)
plt.show(bp)
print('A simple vista parece que varía el Número de visitas dependiendo de la procedencia de la medición.')
print('Destacar los puntos outliers, excesivamente por encima de los demás en las muestras de Facebook y GA Tienda. Posible estudio a posteriori.')

print('')
print('Comprobamos ahora que se satisfacen las hipótesis para esta prueba estadística:')
print('*) Normalidad:')
normalidadPixel = stats.shapiro(pixel['Número de visitas'])
print('Test de Shapiro-Wilk para Pixel: ', normalidadPixel)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Pixel sigue una distribución normal" % normalidadPixel[1])
print('')
normalidadFB = stats.shapiro(facebook['Número de visitas'])
print('Test Shapiro-Wilk para Facebook: ', normalidadFB)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Facebook sigue una distribución normal" % normalidadFB[1])
print('')
normalidadWt = stats.shapiro(wTienda['Número de visitas'])
print('Test de Shapiro-Wilk para Wordpress Tienda: ', normalidadWt)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Wordpres tienda sigue una distribución normal" % normalidadWt[1])
print('')
normalidadgaT = stats.shapiro(gaTienda['Número de visitas'])
print('Test de Shapiro-Wilk para GA Tienda: ', normalidadgaT)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en GA Tienda no sigue una distribución normal" % normalidadgaT[1])
print('')
print('No podemos decir que el análisis es robusto para el supuesto de normalidad, pero no estamos violando una hipótesis muy fuerte y es sólo en una medición')
print('')
print('Valores atípicos (outliers): tan sólo tenemos dos')
print('')
print('Igualdad de varianzas de las diferencias ente niveles de tratamiento:')
homo = stats.levene(facebook['Número de visitas'], pixel['Número de visitas'], wTienda['Número de visitas'])
print(homo)
print("El test de Levene para la prueba de igualdad de varianzas me da un p-valor = %f " % homo.pvalue)
print('Se cumple la hipótesis de homocedasticidad (hipótesis fuerte)')
print('')

print('Realizo ahora la prueba ANOVA-MR')
aovrm = AnovaRM(longRM, 'Número de visitas', 'Mes', ['Procedencia'])
ajuste = aovrm.fit()
print(ajuste.summary())
print('Obtengo un p-valor = 0.1550. Por tanto no rechazo la hipótesis nula de igualdad de medias')
print('CONCLUSIÓN: en este subconjunto no importa la procedencia de la variable Número de visitas, pues me proporcionan la misma información')
print('')

print('2º) Prueba estadística para muestras pareadas')
print('Breve estudio descriptivo')
print('Gráfico de cajas y bigotes:')
bp2 = plt.boxplot([gaCatalogo['Número de visitas'], wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(gaCatalogo['Número de visitas'])):]])
plt.show(bp2)
print('A simple vista parece que varía el Número de visitas dependiendo de la procedencia de la medición.')
print('Destacar un punto outlier, excesivamente por encima de los demás en la muestra de GA Catálogo. Posible estudio a posteriori.')

print('')
print('Comprobamos ahora que si siguen una distribución normal estas muestras:')
normalidadgaC = stats.shapiro(gaCatalogo['Número de visitas'])
print('Test de Shapiro-Wilk para GA Catálogo: ', normalidadgaC)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en GA Catálogo no sigue una distribución normal" % normalidadgaC[1])
print('')
normalidadWc = stats.shapiro(wCatalogo['Número de visitas'])
print('Test de Shapiro-Wilk para Wordpress Catálogo: ', normalidadWc)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Wordpres catálogo no sigue una distribución normal" % normalidadWc[1])
print('')
print('No se cumple la hipótesis de normalidad')
print('')

kwGAWc = stats.kruskal(gaCatalogo['Número de visitas'], wCatalogo['Número de visitas'][(len(wCatalogo['Número de visitas'])-len(gaCatalogo['Número de visitas'])):])
print('Realizamos el test de Kruskal-Wallis (no se cumple normalidad) para la diferencia de las variables procedentes de GA catálogo y Wordpress Catálogo')
print(kwGAWc)
print("Obtenemos un p-valor= %f , por lo que concuyo que tienen la misma media" % kwGAWc.pvalue)
print('')

print('3º)  ANOVA en conjunto para los subconjuntos independientes: ')
print('Como he visto que se verifica la igualdad de medias, da igual el representante que escoja de cada grupo')
print('Hago la prueba por ejemplo con las muestras procedentes de Facebook y Wordpress Catálogo')
#The ANOVA test has important assumptions that must be satisfied in order for the associated p-value to be valid.
#1. The samples are independent. 
print('Mis muestas procedente de Facebook y Wordpress Catálogo son independientes')
print('Se cumple la hipótesis de muestras independientes')
#2. Each sample is from a normally distributed population.
print('Vimos que el supuesto de normalidad se cumple en Facebook pero no en W Catálogo. Aunque no es una hipótesis fuerte')
#3. Homoscedasticity. 
homo2 = stats.levene(facebook['Número de visitas'], wCatalogo['Número de visitas'])
print(homo2)
print("El test de Levene para la prueba de igualdad de varianzas me da un p-valor = %f " % homo2.pvalue)
print('Se cumple la hipótesis de homocedasticidad (hipótesis fuerte)')
print('')
print('Realizo la prueba anova para ver contrastar si en mi modelo con variable respuesta Número de visitas existe el efecto del factor procedencia con sus distintos niveles: Facebook, Wordpress Catálogo')

anova = stats.f_oneway(facebook['Número de visitas'], wCatalogo['Número de visitas'])

print(anova)
print("El test anova me da un p-valor= %f , por tanto concluyo que los niveles del factor no influyen, tienen la misma media" %anova.pvalue)
print('')
print('No sé si creerme el resultado pues no se cumplen todas las hipótesis del modelo, aunque sólo no se cumple una normalidad')
print('')

#If these assumptions are not true for a given set of data, it may still be possible to use 
# the Kruskal-Wallis H-test (scipy.stats.kruskal) although with some loss of power.
print('Realizo una prueba de inferencia no paramétrica just in case')
kw = stats.kruskal(facebook['Número de visitas'], wCatalogo['Número de visitas'])
print(kw)
print("El test de Kruskal-Wallis me da un p-valor= %f , concluyo que todos tienen la misma media" % kw.pvalue)
print('')

print('CONCLUSIÓN GLOBAL: no importa la procedencia de la variable Número de visitas, pues me proporcionan la misma información')
print('Me quedo con la variable de la que tengo más datos, Wordpress Catálogo')
plt.bar(['May-18','Jun-18','Jul-18','Ago-18','Sep-18','Oct-18','Nov-18','Dic-18','Ene-19','Feb-19'], wCatalogo['Número de visitas'])
plt.xlabel('Mes')
plt.ylabel('Número de visitas')
plt.show()