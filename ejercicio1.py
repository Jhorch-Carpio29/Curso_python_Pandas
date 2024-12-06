# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:32:38 2024

@author: HP
"""

import pandas as pd
import numpy as np
datos = {'Nombre': ['Leo', 'Aldair', 'Rodri', 'jerfer'],
         'Calificacioenes': ['09', '12', '14', '20'],
         'Deportes': ['Basquet', 'Futbol', 'Voley', 'Ajedrez'],
         'Materias': ['Calculo', 'Fisica', 'POO', 'Discreta']
         }
df = pd.DataFrame(datos)
print(df)
print('\n'*4)

datos2 = {'Nombre': ['N/A', 'Aldair', 'Rodri', 'jerfer'],
         'Calificacioenes': ['09', '12', np.nan, '20'],
         'Deportes': ['Basquet', 'N/A', 'Voley', 'Ajedrez'],
         'Materias': ['Calculo', 'Fisica', 'POO', 'N/A']
         }
df2 = pd.DataFrame(datos2)
print(df2)
print('\n'*4)
#ESTADÍSTICA  BÁSICA
print(df2.info())
print('\n'*4)
print(df2.describe())
