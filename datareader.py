import numpy as np 
import pandas as pd 


#lectura Google Analytics Catálogo EBA

GAcatagolo=pd.ExcelFile(r'C:\Users\nurit\Dropbox\Estadísticas EBA Nuria\Mi trabajo\Google_Analytics-Catálogo_EBA.xlsx')

general = pd.read_excel(GAcatagolo,sheet_name='Visión general')
usuariosActivos = pd.read_excel(GAcatagolo,sheet_name='Usuarios activos')
nuevovsrecu = pd.read_excel(GAcatagolo,sheet_name='Nuevos vs. recu')
frec = pd.read_excel(GAcatagolo,sheet_name='Frecuencia y asiduidad')
inter = pd.read_excel(GAcatagolo,sheet_name='Interacción')
demogr = pd.read_excel(GAcatagolo,sheet_name='Datos demográficos')
ubi = pd.read_excel(GAcatagolo,sheet_name='Ubicación')
tvida = pd.read_excel(GAcatagolo,sheet_name='Valor tiempo de vida cliente')

#lectura Google Analytics Tienda EBA

