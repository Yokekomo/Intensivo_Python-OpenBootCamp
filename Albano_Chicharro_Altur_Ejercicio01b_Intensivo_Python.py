
# - mientras pongo el de hoy, podéis ampliar con lo siguiente:
# - Lista los tamaños de los ficheros en formato humano.
# - Recorre de manera recursiva todos los directorios desde tu carpeta personal y muestra los ficheros de cada directorio y su tamaño.

# Albano Chicharro Altur
# Ejercicio 1b
# Intensivo Python
# 04/01/2022


# Primero instalamos 
# pip install humanize

import os
from humanize import naturalsize

def downloads():
    if os.path.exists('\Descargas'):
        for root, dirs, files in os.walk('\Descargas', topdown=True):
            for name in files:
                print(os.path.join(root, name), naturalsize(os.path.getsize(os.path.join(root, name))))
    pass

downloads()
