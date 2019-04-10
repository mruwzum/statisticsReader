import numpy as np 
import pandas as pd 
import datareader as dr
import os
import sys

dataGAC=dr.loadGAcatalogo()

print(dataGAC.generalc.columns)
