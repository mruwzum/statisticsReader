import numpy as np 
import pandas as pd 
import datareader as dr
import os
import sys
from scipy import stats
from matplotlib import pyplot as plt



#####################################################3

dataGAc=dr.loadGAcatalogo()

#esto me imprime todas las hojas del GA Catálogo separadas por ---------

print("Google Analytics Catálogo")

for i in range(len(dataGAc)):
    print(dataGAc[i])
    print("-----------------------------------------------------------------------------------------------")


#hoja "visión general" de GA catálogo
vg = dataGAc[0]
nombresvg = vg.columns

print("Visión general")
print(vg)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
vgnumpy = np.array(vg)

#Usuarios
usuarios = vgnumpy[:,1]
usuarioss = usuarios.tolist()
usuarioss.insert(0,nombresvg[1])

print(usuarioss)

#Usuarios nuevos
usuariosnuevos = vgnumpy[:,2]
usuariosnuevoss = usuariosnuevos.tolist()
usuariosnuevoss.insert(0,nombresvg[2])

print(usuariosnuevoss)

#Sesiones
sesiones = vgnumpy[:,3]
sesioness = sesiones.tolist()
sesioness.insert(0,nombresvg[3])

print(sesioness)

#Número de visitas a página
nvisitas = vgnumpy[:,4]
nvisitass = nvisitas.tolist()
nvisitass.insert(0,nombresvg[4])

print(nvisitass)



###############################################################################

dataGAt=dr.loadGAtienda()

#esto me imprime todas las hojas del GA Tienda separadas por ---------

print("Google Analytics Tienda")

for i in range(len(dataGAt)):
    print(dataGAt[i])
    print("-----------------------------------------------------------------------------------------------")


#hoja "visión general" de GA tienda
vgtienda = dataGAt[0]
nombresvgt = vgtienda.columns

print("Visión general")
print(vgtienda)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
vgtnumpy = np.array(vgtienda)

#Usuarios
usuariost = vgtnumpy[:,1]
usuariosst = usuariost.tolist()
usuariosst.insert(0,nombresvgt[1])

print(usuariosst)

#Usuarios nuevos
usuariosnuevost = vgtnumpy[:,2]
usuariosnuevosst = usuariost.tolist()
usuariosnuevosst.insert(0,nombresvgt[2])

print(usuariosnuevosst)

#Sesiones
sesionest = vgtnumpy[:,3]
sesionesst = sesionest.tolist()
sesionesst.insert(0,nombresvgt[3])

print(sesionesst)

#Número de visitas a página
nvisitast = vgtnumpy[:,4]
nvisitasst = nvisitast.tolist()
nvisitasst.insert(0,nombresvgt[4])

print(nvisitasst)



###############################################################################

dataFB = dr.loadFBanalytics()

#esto me imprime todas las hojas del FBAnalytics separadas por ---------

print("Facebook Analytics")

for i in range(len(dataFB)):
    print(dataFB[i])
    print("-----------------------------------------------------------------------------------------------")

#hoja "visitas a la página" de FBAnalytics
visitas = dataFB[0]
nombresFB = visitas.columns

print("Visitas a la página")
print(visitas)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
visnumpy = np.array(visitas)

#Número de visitas
nvisitasf = visnumpy[:,1]
nvisitassf = nvisitasf.tolist()
nvisitassf.insert(0,nombresFB[1])

print(nvisitassf)

#Usuarios únicos (visitantes)
visitantes = visnumpy[:,2]
visitantess = visitantes.tolist()
visitantess.insert(0,nombresFB[2])

print(visitantess)


#Hoja "Reacciones a las publicaciones" deFBAnalytics

reac = dataFB[3]
nombresFBr = reac.columns

print("Reacciones a las publicaciones")
print(reac)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
reacnumpy = np.array(reac)

#Reacciones a posts
reacciones = reacnumpy[:,1]
reaccioness = reacciones.tolist()
reaccioness.insert(0,nombresFBr[1])

print(reaccioness)

#Usuarios únicos (reactioners)
reactioners = reacnumpy[:,2]
reactionerss = reactioners.tolist()
reactionerss.insert(0,nombresFBr[2])

print(reactionerss)


#hoja "publicaciones compartidas" de FBAnalytics

pub = dataFB[4]
nombresFBp = pub.columns

print("Publicaciones compartidas")
print(pub)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
pubnumpy = np.array(pub)

#Publicaciones compartidas
shared = pubnumpy[:,1]
sharedd = shared.tolist()
sharedd.insert(0,nombresFBp[1])

print(sharedd)

#Usuarios únicos (compartidores)
sharer = pubnumpy[:,2]
sharerr = sharer.tolist()
sharerr.insert(0,nombresFBp[2])

print(sharerr)


#Hoja "Comentarios en las publicaciones" deFBAnalytics

com = dataFB[4]
nombresFBc = com.columns

print("Comentarios en las publicaciones")
print(com)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
comnumpy = np.array(com)

#Comentarios
comentarios = comnumpy[:,1]
comentarioss = comentarios.tolist()
comentarioss.insert(0,nombresFBc[1])

print(comentarioss)

#Usuarios únicos (comentadores)
comentadores = comnumpy[:,2]
comentadoress = comentadores.tolist()
comentadoress.insert(0,nombresFBc[2])

print(comentadores)


#Hoja "Mensajes enviados" deFBAnalytics

men = dataFB[5]
nombresFBm = men.columns

print("Mensajes enviados")
print(men)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
mennumpy = np.array(men)

#Mensajes
mensajes = mennumpy[:,1]
mensajess = mensajes.tolist()
mensajess.insert(0,nombresFBm[1])

print(mensajess)

#Usuarios únicos (texter)
texter = mennumpy[:,2]
texterr = texter.tolist()
texterr.insert(0,nombresFBm[2])

print(texterr)



#############################################################

dataPixel = dr.loadPixel()

#esto me imprime todas las hojas del Pixel Analytics separadas por ---------

print("Pixel Analytics")

for i in range(len(dataPixel)):
    print(dataPixel[i])
    print("-----------------------------------------------------------------------------------------------")

#hoja "visitas a la página" de Pixel Analytics
visitasp = dataPixel[0]
nombresp = visitasp.columns

print("Visitas a la página")
print(visitasp)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
vispnumpy = np.array(visitasp)

#Número de visitas
nvisitasp = vispnumpy[:,1]
nvisitassp = nvisitasp.tolist()
nvisitassp.insert(0,nombresp[1])

print(nvisitassp)

#Usuarios únicos (visitantes)
visitantesp = vispnumpy[:,2]
visitantessp = visitantesp.tolist()
visitantessp.insert(0,nombresp[2])

print(visitantessp)

#Sesiones
sesionesp = vispnumpy[:,4]
sesionessp = sesionesp.tolist()
sesionessp.insert(0,nombresp[4])

print(sesionessp)



######################################################################

dataWc=dr.loadWcatalogo()

#esto me imprime todas las hojas del W Catálogo separadas por ---------

print("Wordpress Catálogo")

for i in range(len(dataWc)):
    print(dataWc[i])
    print("-----------------------------------------------------------------------------------------------")


#hoja "trafico" de W catálogo
traficoc = dataWc[0]
nombresWc = traficoc.columns

print("Tráfico")
print(traficoc)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
tracnumpy = np.array(traficoc)

#Visitas
visitasWc = tracnumpy[:,1]
visitassWc = visitasWc.tolist()
visitassWc.insert(0,nombresWc[1])

print(visitassWc)

#Visitantes
visitantesWc = tracnumpy[:,1]
visitantessWc = visitantesWc.tolist()
visitantessWc.insert(0,nombresWc[2])

print(visitantessWc)



######################################################################

dataWt=dr.loadWtienda()

#esto me imprime todas las hojas del W Catálogo separadas por ---------

print("Wordpress Tienda")

for i in range(len(dataWt)):
    print(dataWt[i])
    print("-----------------------------------------------------------------------------------------------")


#hoja "trafico" de W catálogo
traficot = dataWt[0]
nombresWt = traficot.columns

print("Tráfico")
print(traficot)
print("------------")

#quiero tener los elementos que me interesen de la hoja por columnas en variables
#los voy a tener por una parte en array de solo valores y por otra en una lista encabezada por el nombre
tratnumpy = np.array(traficot)

#Visitas
visitasWt = tratnumpy[:,1]
visitassWt = visitasWt.tolist()
visitassWt.insert(0,nombresWt[1])

print(visitassWt)

#Visitantes
visitantesWt = tratnumpy[:,1]
visitantessWt = visitantesWt.tolist()
visitantessWt.insert(0,nombresWt[2])

print(visitantessWt)












#usuarios = vgnumpy[:,1]
#usuariosnuevos = vgnumpy[:,2]

#veo la correlación entre las variables usuarios y usuariosnuevos

#p = stats.pearsonr(usuarios,usuariosnuevos) ##devuelve el coef de correlación y el p-valor del test
#print(p)
#veo que coef=0.99, p-valor casi 0, hay una correlación significante entre ellos 

#plt.scatter(usuarios, usuariosnuevos)
#plt.show()    
#veo que practicamente me muestra la recta y=x

