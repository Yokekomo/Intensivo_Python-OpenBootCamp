# Albano Chicharro Altur
# Ejercicio 4
# Intensivo Python
# 12/01/2022

"""     Ejercicio 4

Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una petición a
https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={API%20key} ,
obtén la temperatura máxima y mínima, para la ciudad que proporcione el usuario.

        Objetivo:
- Aprender a utilizar librerías externas (en este caso, requests)
- Manipular el resultado de la petición (JSON)
"""

import requests

def temperatura_max_min_ciudad():

    ciudad = input('Introduce una ciudad: ')
    pais = input('Introduce el código de país, dos letras: ')
    ciudad = ciudad + ',' + pais
    api_key = 'a6561e292241f23f5d875e5714837aeb'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    url_completa = base_url + 'q=' + ciudad + '&units=metric' + '&appid=' + api_key
    respuesta = requests.get(url_completa)
    tiempo = respuesta.json()

    if tiempo['cod'] != '404':
        menu_tiempo = tiempo['main']
        temperatura_max = round(menu_tiempo['temp_max'])
        temperatura_min = round(menu_tiempo['temp_min'])
        return f'Temperatura maxima: {temperatura_max}º\nTemperatura minima: {temperatura_min}º'
    else:
        return 'Ciudad no encontrada.'


print(temperatura_max_min_ciudad())
