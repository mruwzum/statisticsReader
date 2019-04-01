import numpy as np 
import pandas as pd 


#lectura Google Analytics Catálogo EBA

general=pd.read_excel(r'C:\Users\nurit\Dropbox\Estadísticas EBA Nuria\Mi trabajo\Google Analytics Catálogo EBA.xlsx',sheet_name='Visión general')
print(general.columns)

usuariosActivos=pd.read_excel(r'C:\Users\nurit\Dropbox\Estadísticas EBA Nuria\Mi trabajo\Google Analytics Catálogo EBA.xlsx',sheet_name='Usuarios activos')
print(usuariosActivos.columns)

