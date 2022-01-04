# - Obtén todos los ficheros y directorios de un directorio en concreto. Para ello necesitas una función existente en la librería os (Sistema Operativo) de Python.
# - Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.
# - Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os. 

# Albano Chicharro Altur
# Ejercicio 1
# Intensivo Python
# 03/01/2022

import os

def downloads():
    if os.path.exists('\Descargas'):
        for root, dirs, files in os.walk('\Descargas', topdown=True):
            for name in files:
                if name.endswith('.txt'):
                    print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))
    pass

downloads() 