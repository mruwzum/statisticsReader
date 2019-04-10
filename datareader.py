import numpy as np 
import pandas as pd 


# lectura Google Analytics Catálogo EBA

def loadGAcatalogo():

    GAcatagolo = pd.ExcelFile(r'Datos\Google_Analytics-Catálogo_EBA.xlsx')

    generalc         = pd.read_excel(GAcatagolo,sheet_name='Visión general')
    usuariosActivosc = pd.read_excel(GAcatagolo,sheet_name='Usuarios activos')
    nuevovsrecuc     = pd.read_excel(GAcatagolo,sheet_name='Nuevos vs. recu')
    frecc            = pd.read_excel(GAcatagolo,sheet_name='Frecuencia y asiduidad')
    interc           = pd.read_excel(GAcatagolo,sheet_name='Interacción')
    demogrc          = pd.read_excel(GAcatagolo,sheet_name='Datos demográficos')
    ubic             = pd.read_excel(GAcatagolo,sheet_name='Ubicación')
    tvidac           = pd.read_excel(GAcatagolo,sheet_name='Valor tiempo de vida cliente')


# lectura Google Analytics Tienda EBA

def loadGAtienda():

    GAtienda = pd.ExcelFile(r'Datos\Google_Analytics-Catálogo_EBA.xlsx')

    generalt         = pd.read_excel(GAtienda,sheet_name='Visión general')
    usuariosActivost = pd.read_excel(GAtienda,sheet_name='Usuarios activos')
    nuevovsrecut     = pd.read_excel(GAtienda,sheet_name='Nuevos vs. recu')
    frect            = pd.read_excel(GAtienda,sheet_name='Frecuencia y asiduidad')
    intert           = pd.read_excel(GAtienda,sheet_name='Interacción')
    demogrt          = pd.read_excel(GAtienda,sheet_name='Datos demográficos')
    ubit             = pd.read_excel(GAtienda,sheet_name='Ubicación')
    tvidat           = pd.read_excel(GAtienda,sheet_name='Valor tiempo de vida cliente')


# lectura Facebook Analytics

def loadFBanalytics():

    fbanalytics = pd.ExcelFile(r'Datos\Facebook_Analytics.xlsx')

    visitasf     = pd.read_excel(fbanalytics,sheet_name='Visitas a la página')
    retencionf  = pd.read_excel(fbanalytics,sheet_name='Retención de usuarios')
    postreacf    = pd.read_excel(fbanalytics,sheet_name='Post reactions por post')
    reacf        = pd.read_excel(fbanalytics,sheet_name='Reacciones a las publicaciones')
    compartidof  = pd.read_excel(fbanalytics,sheet_name='Publicaciones compartidas')
    comentariosf = pd.read_excel(fbanalytics,sheet_name='Comentarios en las publicacione')
    mensajesf    = pd.read_excel(fbanalytics,sheet_name='Mensajes enviados')


# lectura Píxel Analytics

def loadPixel():

    pixel = pd.ExcelFile(r'Datos\Píxel_Analytics.xlsx')

    visitasp   = pd.read_excel(pixel,sheet_name='Visitas a la página')
    ingresos   = pd.read_excel(pixel,sheet_name='Ingresos')
    retencionp = pd.read_excel(pixel,sheet_name='Retención de usuarios')
    demogrp    = pd.read_excel(pixel,sheet_name='Datos demográficos')


# lectura Wordpress Catálogo EBA

def loadWcatalogo():

    Wcatalogo = pd.ExcelFile(r'Datos\Wordpress_Catálogo_EBA.xlsx')

    traficoc     = pd.read_excel(Wcatalogo,sheet_name='Tráfico')
    paginasc     = pd.read_excel(Wcatalogo,sheet_name='Entradas y páginas')
    paisesc      = pd.read_excel(Wcatalogo,sheet_name='Países')
    clicsc       = pd.read_excel(Wcatalogo,sheet_name='Clics')
    referenciasc = pd.read_excel(Wcatalogo,sheet_name='Referencias')
    tiendac      = pd.read_excel(Wcatalogo,sheet_name='Tienda')


# lectura Wordpress Tienda EBA

def loadWtienda():

    Wtienda = pd.ExcelFile(r'Datos\Wordpress_Tienda_EBA.xlsx')

    traficot     = pd.read_excel(Wtienda,sheet_name='Tráfico')
    paginast     = pd.read_excel(Wtienda,sheet_name='Entradas y páginas')
    paisest      = pd.read_excel(Wtienda,sheet_name='Países')
    clicst       = pd.read_excel(Wtienda,sheet_name='Clics')
    referenciast = pd.read_excel(Wtienda,sheet_name='Referencias')
    tiendat      = pd.read_excel(Wtienda,sheet_name='Tienda')