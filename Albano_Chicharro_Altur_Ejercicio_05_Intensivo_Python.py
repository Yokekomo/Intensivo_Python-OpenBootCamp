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

import pandas as pd

archivo_excel = pd.read_excel(r'\Descargas\archivo_excel.xlsx')
archivo_excel.to_csv(r'\Descargas\nuevo_archivo.csv', index=None, header=True)

