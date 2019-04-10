import numpy as np 
import pandas as pd 
import os
import sys

GAcatagolo = pd.ExcelFile(r'Datos\Google_Analytics-Catálogo_EBA.xlsx')

generalc         = pd.read_excel(GAcatagolo,sheet_name='Visión general')
usuariosActivosc = pd.read_excel(GAcatagolo,sheet_name='Usuarios activos')
nuevovsrecuc     = pd.read_excel(GAcatagolo,sheet_name='Nuevos vs. recu')
frecc            = pd.read_excel(GAcatagolo,sheet_name='Frecuencia y asiduidad')
interc           = pd.read_excel(GAcatagolo,sheet_name='Interacción')
demogrc          = pd.read_excel(GAcatagolo,sheet_name='Datos demográficos')
ubic             = pd.read_excel(GAcatagolo,sheet_name='Ubicación')
tvidac           = pd.read_excel(GAcatagolo,sheet_name='Valor tiempo de vida cliente')


# listadelistas = [generalc, usuariosActivosc, nuevovsrecuc, frecc, interc, demogrc, ubic, tvidac]

# print(generalc[1][1])