import numpy as np 
import pandas as pd 
import datareader as dr
import os
import sys

#esto me imprime todas las hojas del GA Catálogo separadas por ---------

dataGAc=dr.loadGAcatalogo()

for i in range(len(dataGAc)):
    print(dataGAc[i])
    print("-----------------------------------------------------------------------------------------------")