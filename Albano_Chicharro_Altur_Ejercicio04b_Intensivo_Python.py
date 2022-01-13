# Albano Chicharro Altur
# Ejercicio 4b
# Intensivo Python
# 12/01/2022

"""     Ejercicio 4-b

Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una petición a
https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={API%20key} ,
obtén la temperatura máxima y mínima, para la ciudad que proporcione el usuario.

        Objetivo:
- Aprender a utilizar librerías externas (en este caso, requests)
- Manipular el resultado de la petición (JSON)

Parte 2 del ejercicio:

- Podéis ampliar este, sacando la previsión a 7 días y haciendo la temperatura media
temp_maxima_media y temp_minima_media
"""

import requests

ciudad = input('Introduce una ciudad: ')
pais = input('Introduce el código de país, dos letras: ')
ciudad = ciudad + ',' + pais
api_key = 'a6561e292241f23f5d875e5714837aeb'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
url_completa = base_url + 'q=' + ciudad + '&units=metric' + '&appid=' + api_key

solicitud_cordenadas = requests.get(url_completa)
cordenadas = solicitud_cordenadas.json()

capital = cordenadas['name']
lat = cordenadas['coord']['lat']
lon = cordenadas['coord']['lon']
latitud = str(lat)
longitud = str(lon)

no_incluir = 'current,hourly,minutely,alerts'
api_key = 'a6561e292241f23f5d875e5714837aeb'
base_url2 = 'https://api.openweathermap.org/data/2.5/onecall?'
url_cord = base_url2 + 'lat=' + latitud + '&lon=' + longitud + '&exclude=' + no_incluir + '&units=metric' + '&appid=' + api_key

solicitud = requests.get(url_cord)
menu = solicitud.json()

temp_min = []
temp_max = []

for i in menu['daily']:
    temp_min.append(i['temp']['min'])
    temp_max.append(i['temp']['max'])
    media_min = sum(temp_min) / len(temp_min)
    media_max = sum(temp_max) / len(temp_max)


imprimir = f'\n{capital} - Temperatura Max-Min 7 dias\n'

for i in range(len(temp_min[:-1])):

    if i == 0:
        imprimir += f'\nDia: {i + 1}\n'

    else:
        imprimir += f'\nDia: {i + 1}\n'

    imprimir += 'Temperatura Max: ' + str(temp_min[i]) + '°C' + "\n"
    imprimir += 'Temperatura Min: ' + str(temp_max[i]) + '°C' + "\n"

imprimir2 = f'Media, para los proximos 7 dias:'
imprimir3 = f'Temperatura maxima: {round(media_min)}º\nTemperatura minima: {round(media_max)}º'

print(imprimir)
print(imprimir2)
print(imprimir3)
