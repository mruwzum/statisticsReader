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
print(dataGAc[0])

print("------------")

#quiero tener los elementos de la hoja por columnas en variables
print(vg.columns)

vgnumpy = np.array(vg)

#esto me imprime todas las filas de la columna 1 (lo que luego defino como usuarios)
print(vgnumpy[:,1])

usuarios = vgnumpy[:,1]
usuariosnuevos = vgnumpy[:,2]

#veo la correlación entre las variables usuarios y usuariosnuevos

p = stats.pearsonr(usuarios,usuariosnuevos) ##devuelve el coef de correlación y el p-valor del test
print(p)
#veo que coef=0.99, p-valor casi 0, hay una correlación significante entre ellos 

plt.scatter(usuarios, usuariosnuevos)
plt.show()    
#veo que practicamente me muestra la recta y=x

