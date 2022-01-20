# Albano Chicharro Altur
# Ejercicio 6
# 19/01/2022

"""   Ejercicio 6

Enunciado:

Crea una función que convierta un password (entre 6 y 12 caracteres) es una cadena de texto alfanumérica de
32 caracteres. La función SIEMPRE debe devolver el mismo resultado para la misma entrada.

Objetivo:

- Aprender a manejar los bucles y las cadena de texto.
- Mejorar la capacidad algorítmica.

"""

import random


class Encriptar:

    def __init__(self):
        self.__password = None
        self.__crypto = None

    def pedirPassword(self):

        while True:
            try:
                self.__password = input('Introduce una Contraseña:\n')
                if (len(self.__password) >= 6) and (len(self.__password) <= 12):
                    if self.__password.isalnum():
                        return self.diccionario()
                    else:
                        print('La contraseña debe de ser alfanumérica.')
                else:
                    print('La contraseña debe contener entre 6 y 12 caracteres.')
            except:
                print('Ha ocurrido un ERROR')

    def encriptar_password(self):

        lista = []

        while len(lista) <= 32:
            numeroAleatorio = random.randint(0, 9)
            lista.append(numeroAleatorio)
            minusculaAleatoria = chr(random.randint(ord('a'), ord('z')))
            lista.append(minusculaAleatoria)
            mayusculaAleatoria = chr(random.randint(ord('A'), ord('Z')))
            lista.append(mayusculaAleatoria)

        self.__crypto = "".join(map(str, lista))
        return self.__crypto

    def diccionario(self):

        diccionario = {'7uU4cA2hC1kD8hT0cX3qC4bA6hA9dS0dQ': 'albano12',
                       '9vG8hY7kG9gD4bU3mN0cA5cN9fX5nN6sM': 'albano13',
                       '8wI7bA7xS8zW9zR4iK9gX4eS6bK4qN2hH': 'albano14'}

        try:
            if self.__password in diccionario.values():
                print('La contraseña ya existe')
                self.pedirPassword()
            else:
                self.encriptar_password()
                diccionario.update({self.__crypto: self.__password})
                print('La contraseña no existe - Contraseña almacenada', self.__crypto)
        except:
            print('Algo salio mal en el diccionario')


encriptar_un_password = Encriptar()
encriptar_un_password.pedirPassword()



