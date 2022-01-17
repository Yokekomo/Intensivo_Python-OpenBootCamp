# Albano Chicharro Altur
# Ejercicio 5
# Intensivo Python
# 17/01/2022

"""    Ejercicio 5

Enunciado: Convierte un Excel a CSV
Objetivo:
Aprender a trabajar con ficheros
Usar la librería pandas de Python

"""
import csv

import pandas as pd

archivo_excel = pd.read_excel(r'\Descargas\excel.xlsx')
nombre = []
email = []
telf = []
diccionario = []

for i in archivo_excel['Nombre'[:]]:
    nombre.append(i)
for j in archivo_excel['Email'[:]]:
    email.append(j)
for k in archivo_excel['Telf'[:]]:
    telf.append(k)

for l in range(len(nombre)):
    dict1 = {'Nombre': nombre[l], 'Email': email[l], 'Telf': telf[l]}
    diccionario.append(dict1)


df = pd.DataFrame(diccionario)
df.to_csv(r'\Descargas\nuevo.csv', index=False)
