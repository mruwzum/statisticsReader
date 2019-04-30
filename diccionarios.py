import numpy as np 
import pandas as pd 
import datareader as dr
import os
import sys

#por lo pronto voy a cargar las vbles que creo convenientes. ya cuando las estudie meteré algo más si veo bien

def diccionarioFB():
    #Leo el excel FBAnalytics
    dataFB = dr.loadFBanalytics()

    #Hoja "Visitas a la página" de FBAnalytics
    visitf = dataFB[0]
    visitf = np.array(visitf)
    #Defino las variables que me interesan de esta hoja
    nvisitasFB = visitf[:,1]
    nvisitantesFB = visitf[:,2]

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
    
    return facebook



def diccionarioGAcatalogo():
    #Leo el excel Google Analytics catálogo
    dataGAc=dr.loadGAcatalogo()

    #Hoja "Visión general" de GAcatalogo
    visionc = dataGAc[0]
    visionc = np.array(visionc)
    #Defino las variables que me interesan de esta hoja
    usuariosGAc = visionc[:,1]
    usuariosnuevosGAc = visionc[:,2]
    sesionesGAc = visionc[:,3]
    nvisitasGAc = visionc[:,4]
    porcentajereboteGAc = visionc[:,6]
    duracionmediasesionGAc = visionc[:,7]


    #Diccionario
    gaCatalogo = {'Usuarios' : usuariosGAc, 'Usuarios nuevos' : usuariosnuevosGAc, 'Sesiones' : sesionesGAc, 
              'Número de visitas' : nvisitasGAc, 'Porcentaje de rebote' : porcentajereboteGAc, 
              'Duración media de la sesión' : duracionmediasesionGAc}
    
    return gaCatalogo


def diccionarioGAtienda():
    #Leo el excel Google Analytics tienda
    dataGAt=dr.loadGAtienda()

    #Hoja "Visión general" de GAtienda
    visiont = dataGAt[0]
    visiont = np.array(visiont)
    #Defino las variables que me interesan de esta hoja
    usuariosGAt = visiont[:,1]
    usuariosnuevosGAt = visiont[:,2]
    sesionesGAt = visiont[:,3]
    nvisitasGAt = visiont[:,4]
    tasareboteGAt = visiont[:,6]
    duracionmediasesionGAt = visiont[:,7]


    #Diccionario
    gaCatalogo = {'Usuarios' : usuariosGAt, 'Usuarios nuevos' : usuariosnuevosGAt, 'Sesiones' : sesionesGAt, 
              'Número de visitas' : nvisitasGAt, 'Tasa de rebote' : tasareboteGAt, 
              'Duración media de la sesión' : duracionmediasesionGAt}
    
    return gaCatalogo



def diccionarioPixel():
    #Leo el excel Google Analytics catálogo
    dataPixel=dr.loadPixel()

    #Hoja "Visitas a la página" de Pixel Analytics
    visitp = dataPixel[0]
    visitp = np.array(visitp)
    #Defino las variables que me interesan de esta hoja
    nvisitasP = visitp[:,1]
    nvisitantesP = visitp[:,2]
    sesionesP = visitp[:,4]
    duracionmediasesionP = visitp[:,5]
    tasareboteP = visitp[:,8]


    #Diccionario
    pixel = {'Número de visitas' : nvisitasP, 'Visitantes' : nvisitantesP, 'Sesiones' : sesionesP, 'Tasa de rebote' : tasareboteP, 
        'Duración media de la sesión' : duracionmediasesionP}
    
    return pixel


    