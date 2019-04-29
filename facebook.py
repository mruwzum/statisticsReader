import numpy as np 
import pandas as pd 
import datareader as dr
import os
import sys
from scipy import stats
from matplotlib import pyplot as plt

#Leo el excel FBAnalytics
dataFB = dr.loadFBanalytics()

#Hoja "Visitas a la página" de FBAnalytics
visit = dataFB[0]
visit = np.array(visit)
#Defino las variables que me interesan de esta hoja
nvisitasFB = visit[:,1]
nvisitantesFB = visit[:,2]

#Hoja "Reacciones a las publicaciones" de FBAnalytics
reac = dataFB[3]
reac = np.array(reac)
#Defino las variables que me interesan de esta hoja
reaccionesFB = reac[:,1]
reaccionadoresFB = reac[:,2]

#Hoja "Publicaciones compartidas" de FBAnalytics
pub = dataFB[4]
pub = np.array(pub)
#Defino las variables que me interesan de esta hoja
pubcompartidasFB = pub[:,1]
compartidoresFB = pub[:,2]

#Hoja "Comentarios en las publicaciones" deFBAnalytics
coment = dataFB[4]
coment = np.array(coment)
#Defino las variables que me interesan de esta hoja
comentariosFB = coment[:,1]
comentadoresFB = coment[:,2]

#Hoja "Mensajes enviados" deFBAnalytics
mensj = dataFB[5]
mensj = np.array(mensj)
#Defino las variables que me interesan de esta hoja
mensajesFB = coment[:,1]
mensajeadoresFB = coment[:,2]


#Diccionario
facebook = {'Número de visitas' : nvisitasFB, 'Visitantes' : nvisitantesFB,
            'Reacciones a publicaciones' : reaccionesFB, 'Personas que han reaccionado' : reaccionadoresFB,
            'Publicaciones compartidas' : pubcompartidasFB, 'Personas que han compartido' : compartidoresFB,
            'Comentarios' : comentariosFB , 'Personas que han comentado' : comentadoresFB,
            'Mensajes' : mensajesFB , 'Personas que han mensajeado' : mensajeadoresFB}

#print(facebook['Número de visitas'])
#print(type(facebook['Número de visitas']))
#print(facebook)


#ESTADÍSTICA

#Estudio las visitas (modelo lineal simple)
#Estudio descriptivo
plt.scatter(facebook['Visitantes'],facebook['Número de visitas'])
plt.xlabel('Visitantes')
plt.ylabel('Número de visitas')
plt.show()
print('Podemos observar que hay una relación lineal entre el número de visitas y los visitantes')
#Vemos cómo están correladas las variables
rho = stats.pearsonr(facebook['Visitantes'],facebook['Número de visitas'])

print('El coeficiente de correlación de Pearson es ',rho[0], ' con un p-valor de ', rho[1])