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


print('Voy a realizar pruebas estadísticas para analizar la variable "Sesiones",  presente en Pixel, GA Tienda y GA Catálogo')
print('Analizamos primero en conjunto las muestras dependientes de Pixel y GA Tienda')
print('1º) t-student test para la igualdad de medias')
print('Breve estudio descriptivo')
print("La media muestral de Sesiones en Pixel es  %f " % pixel['Sesiones'].mean())
print("La media muestral de Sesiones en GA Tienda es  %f " % gaTienda['Sesiones'].mean())
print('Gráfico de cajas y bigotes:')
data_to_plot = [pixel['Sesiones'], gaTienda['Sesiones']]
bp = plt.boxplot(data_to_plot)
plt.show(bp)
print('A simple vista parece que las Sesiones varían dependiendo de la procedencia de la medición.')
print('Destacar un punto outlier, excesivamente por encima de los demás en la muestra de GA Tienda. Posible estudio a posteriori.')
print('¡OJO! este punto outlier se ha repetido más de una vez. Esto hay que verlo, ¿qué pasó ese mes?')
print('')
print('Supuesto de normalidad')
normalidadPixel = stats.shapiro(pixel['Sesiones'])
print('Test de Shapiro-Wilk para Pixel: ', normalidadPixel)
print("Obtengo un p-valor = %f , concluyo que Visitantes en Pixel sigue una distribución normal" % normalidadPixel[1])
print('')
normalidadGATienda = stats.shapiro(gaTienda['Sesiones'])
print('Test de Shapiro-Wilk para Pixel: ', normalidadGATienda)
print("Obtengo un p-valor = %f , concluyo que Visitantes en Pixel sigue una distribución normal" % normalidadGATienda[1])
print('')
print('Ahora sí realizo el test t-student')
ttestPGAT = stats.ttest_1samp(pixel['Sesiones']-gaTienda['Sesiones'], popmean = 0)
print(ttestPGAT)
print("Obtenemos un p-valor= %f , por lo que concluyo que tienen la misma media" % ttestPGAT.pvalue)
print('')
print('2º) ANOVA para las muestras independientes GA Catálogo y por ejemplo, (escojo solo una) Pixel')
#The ANOVA test has important assumptions that must be satisfied in order for the associated p-value to be valid.

#1. The samples are independent. 
#Creo que se cumple, hablar con Miguel para confirmar la procedencia de los datos.
print('Se cumple la hipótesis de muestras independientes')
#2. Each sample is from a normally distributed population.

#3. Homoscedasticity. 
homo = stats.levene(gaCatalogo['Sesiones'], pixel['Sesiones'])
print(homo)
print("El test de Levene para la prueba de igualdad de varianzas me da un p-valor = %f " % homo.pvalue)
print('Se cumple la hipótesis de homocedasticidad')
print('')
print('Realizo la prueba anova para ver contrastar si en mi modelo con variable respuesta Visitantes existe el efecto del factor procedencia con sus distintos niveles: Pixel, GA Catálogo')

anova = stats.f_oneway(gaCatalogo['Sesiones'], pixel['Sesiones'])

print(anova)
print("El test anova me da un p-valor= %f , por tanto concluyo que los niveles del factor no influyen, tienen la misma media" %anova.pvalue)
print('')

print('CONCLUSIÓN: no importa la procedencia de la variable Sesiones, pues me proporcionan la misma información')


#plotting
plt.bar(['Oct-18','Nov-18','Dic-18','Ene-19','Feb-19'], pixel['Sesiones'])
plt.xlabel('Mes')
plt.ylabel('Sesiones')
plt.show()