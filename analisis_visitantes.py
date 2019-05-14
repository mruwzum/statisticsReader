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


print('Voy a realizar pruebas estadísticas para analizar la variable "Visitantes" (equivalente a "Usuarios") con sus distintas procedencias.')
print('Me encuentro con que tengo un experimento con muestras repetidas: las mediciones de Pixel, Facebook, GA Tienda y Wordpress Tienda toman datos de la misma web (Wordpress Tienda).')
print('Por otro lado, también tengo muestras pareadas en GA Catálogo y Wordpress Catálogo. También los analizaremos juntos.')
print('Analizaremos los dos subconjuntos independientes por separado, para luego establecer conclusiones en común')
print('')
print('1º) ANOVA Repeated Measures')
print('Manipulación de los datos y descriptivos')

rm = { 'Mes' : ['Oct-18','Nov-18','Dic-18','Ene-19','Feb-19'] , 'Pixel' : pixel['Visitantes'] , 'Facebook' : facebook['Visitantes'] , 'Wordpress Tienda' : wTienda['Visitantes'][(len(wTienda['Visitantes'])-len(gaTienda['Usuarios'])):] , 'GA Tienda' : gaTienda['Usuarios'] }
repeatedMeasures = pd.DataFrame(rm)
print(repeatedMeasures)
#paso de formato wide a long porque por lo visto es el que hay que usar
longRM = pd.melt(repeatedMeasures, id_vars= 'Mes', value_vars= ['Pixel','Facebook','Wordpress Tienda', 'GA Tienda'], value_name='Visitantes', var_name='Procedencia')
print(longRM)

print('')
print('Gráfico de cajas y bigotes:')
data_to_plot = [rm['Pixel'], rm['Facebook'], rm['Wordpress Tienda'], rm['GA Tienda']]
bp = plt.boxplot(data_to_plot)
plt.show(bp)
print('A simple vista parece que los Visitantes varían dependiendo de la procedencia de la medición.')
print('Destacar un punto outlier, excesivamente por encima de los demás en la muestra de GA Tienda. Posible estudio a posteriori.')

print('')
print('Comprobamos ahora que se satisfacen las hipótesis para esta prueba estadística:')
print('*) Normalidad:')
normalidadPixel = stats.shapiro(pixel['Visitantes'])
print('Test de Shapiro-Wilk para Pixel: ', normalidadPixel)
print("Obtengo un p-valor = %f , concluyo que Visitantes en Pixel sigue una distribución normal" % normalidadPixel[1])
print('')
normalidadFB = stats.shapiro(facebook['Visitantes'])
print('Test Shapiro-Wilk para Facebook: ', normalidadFB)
print("Obtengo un p-valor = %f , concluyo que Visitante en Facebook sigue una distribución normal" % normalidadFB[1])
print('')
normalidadWt = stats.shapiro(wTienda['Visitantes'])
print('Test de Shapiro-Wilk para Wordpress Tienda: ', normalidadWt)
print("Obtengo un p-valor = %f , concluyo que Visitantes en Wordpres tienda sigue una distribución normal" % normalidadWt[1])
print('')
normalidadgaT = stats.shapiro(gaTienda['Usuarios'])
print('Test de Shapiro-Wilk para GA Tienda: ', normalidadgaT)
print("Obtengo un p-valor = %f , concluyo que Visitantes en GA Tienda sigue una distribución normal" % normalidadgaT[1])
print('')
print('El análisis es robusto para el supuesto de normalidad')
print('')
print('Valores atípicos (outliers): tan sólo tenemos uno')
print('')
print('Igualdad de varianzas de las diferencias ente niveles de tratamiento:')
homo = stats.levene(facebook['Visitantes'], pixel['Visitantes'], wTienda['Visitantes'])
print(homo)
print("El test de Levene para la prueba de igualdad de varianzas me da un p-valor = %f " % homo.pvalue)
print('Se cumple la hipótesis de homocedasticidad (hipótesis fuerte)')
print('')


print('Realizo ahora la prueba ANOVA-MR')
aovrm = AnovaRM(longRM, 'Visitantes', 'Mes', ['Procedencia'])
ajuste = aovrm.fit()
print(ajuste.summary())
print('Obtengo un p-valor = 0.8436. Por tanto no rechazo la hipótesis nula de igualdad de medias')
print('CONCLUSIÓN: en este subconjunto no importa la procedencia de la variable Visitantes, pues me proporcionan la misma información')
print('')

print('2º) Prueba estadística para muestras pareadas')
print('Breve estudio descriptivo')
print('Gráfico de cajas y bigotes:')
bp2 = plt.boxplot([gaCatalogo['Usuarios'], wCatalogo['Visitantes'][(len(wCatalogo['Visitantes'])-len(gaCatalogo['Usuarios'])):]])
plt.show(bp2)
print('A simple vista parece que Visitantes varía dependiendo de la procedencia de la medición.')
print('Destacar un punto outlier, excesivamente por encima de los demás en la muestra de GA Catálogo. Posible estudio a posteriori.')

print('')
print('Comprobamos ahora que si siguen una distribución normal estas muestras:')
normalidadgaC = stats.shapiro(gaCatalogo['Usuarios'])
print('Test de Shapiro-Wilk para GA Catálogo: ', normalidadgaC)
print("Obtengo un p-valor = %f , concluyo que Visitantes en GA Catálogo sigue una distribución normal" % normalidadgaC[1])
print('')
normalidadWc = stats.shapiro(wCatalogo['Visitantes'])
print('Test de Shapiro-Wilk para Wordpress Catálogo: ', normalidadWc)
print("Obtengo un p-valor = %f , concluyo que el Número de visitas en Wordpres catálogo no sigue una distribución normal" % normalidadWc[1])
print('')
print('No se cumple la hipótesis de normalidad')
print('')

kwGAWc = stats.kruskal(gaCatalogo['Usuarios'], wCatalogo['Visitantes'][(len(wCatalogo['Visitantes'])-len(gaCatalogo['Usuarios'])):])
print('Realizamos el test de Kruskal-Wallis (no se cumple normalidad) para la diferencia de las variables procedentes de GA catálogo y Wordpress Catálogo')
print(kwGAWc)
print("Obtenemos un p-valor= %f , por lo que concuyo que tienen la misma media" % kwGAWc.pvalue)
print('')

print('3º)  ANOVA en conjunto para los subconjuntos independientes: ')
print('Como he visto que se verifica la igualdad de medias, da igual el representante que escoja de cada grupo')
print('Hago la prueba por ejemplo con las muestras procedentes de Facebook y GA Catálogo')
#The ANOVA test has important assumptions that must be satisfied in order for the associated p-value to be valid.
#1. The samples are independent. 
print('Mis muestras procedente de Facebook y GA Catálogo son independientes')
print('Se cumple la hipótesis de muestras independientes')
#2. Each sample is from a normally distributed population.
print('Vimos que el supuesto de normalidad también se cumple.')
#3. Homoscedasticity. 
homo2 = stats.levene(facebook['Visitantes'], gaCatalogo['Usuarios'])
print(homo2)
print("El test de Levene para la prueba de igualdad de varianzas me da un p-valor = %f " % homo2.pvalue)
print('Se cumple la hipótesis de homocedasticidad (hipótesis fuerte)')
print('')
print('Realizo la prueba anova para ver contrastar si en mi modelo con variable respuesta Número de visitas existe el efecto del factor procedencia con sus distintos niveles: Facebook, Wordpress Catálogo')

anova = stats.f_oneway(facebook['Número de visitas'], gaCatalogo['Usuarios'])

print(anova)
print("El test anova me da un p-valor= %f , por tanto concluyo que los niveles del factor influyen." %anova.pvalue)
print('')
print('Tengo que ver qué nivel del factor tiene mayor media. Tengo que realizar un analisis post hoc')
print('Test de Tukey para la comparación de medias')

comparar = {'Mes' : ['Oct-18','Nov-18','Dic-18','Ene-19','Feb-19'] ,'Facebook' : facebook['Visitantes'] , 'GA Catálogo' : gaCatalogo['Usuarios'] }
comparar = pd.DataFrame(comparar)
longComp = pd.melt(comparar, id_vars= 'Mes', value_vars= ['Facebook','GA Catálogo'], value_name='Visitantes', var_name='Procedencia')

mc = MultiComparison(longComp['Visitantes'].values.tolist(), longComp['Procedencia'].values)
result = mc.tukeyhsd(alpha=0.05)
print(result)
print('La tabla nos muestra, aunque diga que no es significativa, que la diferencia mediaGAC - mediaFB = -12.2')
print('Por lo que concluyo que la media en facebook es más grande')


#plotting 

plt.bar(['Oct-18','Nov-18','Dic-18','Ene-19','Feb-19'], gaCatalogo['Usuarios'])
plt.xlabel('Mes')
plt.ylabel('Visitantes en GA Catálogo')
plt.show()

plt.bar(['Oct-18','Nov-18','Dic-18','Ene-19','Feb-19'], facebook['Visitantes'])
plt.xlabel('Mes')
plt.ylabel('Visitantes en Facebook')
plt.show()