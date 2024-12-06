# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:03:40 2024

@author: HP
"""

import pandas as pd 
datos = pd.read_csv('ATP.csv')
print(datos.info())

print(datos.iloc[[0,3,5,23]])