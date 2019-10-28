import streamlit as st
import pandas as pd
import numpy as np
import time
import uber_display

"#### Luis Angel Castro Parra A0132967"
"#### Alejando Garza Castro A01380852"
"#### Ivan Sol Ontiveros A00819920"

"# Pandas Tutorial"
"### Semana i 2019"

"Made in Streamlit"

"- **Filtrar elementos que no esten en un Series**"
ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series([4,5,6,7,8])
ser1
ser2
# answer
result = ser1[~ser1.isin(ser2)]
result

"- **Declarar un Pandas Series de la sig lista**"
mylist = list('abcdefghijklmnopqrstuvwxyz')
mylist

# answer
result = pd.Series(mylist)
result

"- **Manipular un dataframe de strings**"
df = pd.DataFrame(['how', 'to', 'kick','ass?'])
df
#answer
#result = df[0].str.capitalize()
result = df[0].apply(lambda x : x[0].upper()+x[1:])
result

"- **Convertir numpyarr a dataframe de un tamaño en especifico, a una matriz 7 x 5**"
ser = np.random.randint(1,10,35)
ser
#answer
result = pd.DataFrame(ser.reshape(7,5))
result

"- **Calcular distancia euclediana entre dos vectores**"
p = pd.Series([1,2,3,4,5,6,7,8,9,10])
q = pd.Series([10,9,8,7,6,5,4,3,2,1])
p
q
#answer
result = np.linalg.norm(q.values-p.values)
result