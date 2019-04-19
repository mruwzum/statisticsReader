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
vgnumpy = np.array(vg)

#Usuarios
u = vgnumpy[:,1]
usuarios = u.tolist()
usuarios.insert(0,nombres[1])

print(usuarios)

#Usuarios nuevos
un = vgnumpy[:,2]
usuariosnuevos = un.tolist()
usuariosnuevos.insert(0,nombres[2])

print(usuariosnuevos)


#intento de hacerlo de manera general con for










#usuarios = vgnumpy[:,1]
#usuariosnuevos = vgnumpy[:,2]

#veo la correlación entre las variables usuarios y usuariosnuevos

#p = stats.pearsonr(usuarios,usuariosnuevos) ##devuelve el coef de correlación y el p-valor del test
#print(p)
#veo que coef=0.99, p-valor casi 0, hay una correlación significante entre ellos 

#plt.scatter(usuarios, usuariosnuevos)
#plt.show()    
#veo que practicamente me muestra la recta y=x

