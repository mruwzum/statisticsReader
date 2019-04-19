import numpy as np 
import pandas as pd 
import datareader as dr
import os
import sys
from scipy import stats
from matplotlib import pyplot as plt


dataGAc=dr.loadGAcatalogo()


#hoja "visión general" de GA catálogo
vg = dataGAc[0]
nombres = vg.columns

print(vg)

print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
vgnumpy = np.array(vg)

#Usuarios
usuarios = vgnumpy[:,1]
usuarioss = usuarios.tolist()
usuarioss.insert(0,nombres[1])

print(usuarioss)

#Usuarios nuevos
usuariosnuevos = vgnumpy[:,2]
usuariosnuevoss = usuariosnuevos.tolist()
usuariosnuevoss.insert(0,nombres[2])

print(usuariosnuevoss)

#Sesiones
sesiones = vgnumpy[:,3]
sesioness = sesiones.tolist()
sesioness.insert(0,nombres[3])

print(sesioness)

#Número de visitas a página
nvisitas = vgnumpy[:,4]
nvisitass = nvisitas.tolist()
nvisitass.insert(0,nombres[4])

print(nvisitass)



#usuarios = vgnumpy[:,1]
#usuariosnuevos = vgnumpy[:,2]

#veo la correlación entre las variables usuarios y usuariosnuevos

#p = stats.pearsonr(usuarios,usuariosnuevos) ##devuelve el coef de correlación y el p-valor del test
#print(p)
#veo que coef=0.99, p-valor casi 0, hay una correlación significante entre ellos 

#plt.scatter(usuarios, usuariosnuevos)
#plt.show()    
#veo que practicamente me muestra la recta y=x

