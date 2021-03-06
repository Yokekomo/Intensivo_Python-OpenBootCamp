# Albano Chicharro Altur
# Ejercicio 6
# 19/01/2022

# Hecho con hash

"""   Ejercicio 6

Enunciado:

Crea una función que convierta un password (entre 6 y 12 caracteres) es una cadena de texto alfanumérica de
32 caracteres. La función SIEMPRE debe devolver el mismo resultado para la misma entrada.

Objetivo:

- Aprender a manejar los bucles y las cadena de texto.
- Mejorar la capacidad algorítmica.

"""

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

        crypto = ''

        for caracter in self.__password:

            if caracter.isupper():

                indice_caracter = ord(caracter) - ord('A')
                caracter_desplazado = (indice_caracter + 9) % 26 + ord('A')
                nuevo_caracter = str(caracter_desplazado)
                crypto += nuevo_caracter

            elif caracter.islower():

                indice_caracter = ord(caracter) - ord('a')
                caracter_desplazado = (indice_caracter + 9) % 26 + ord('a')
                nuevo_caracter = str(caracter_desplazado)
                crypto += nuevo_caracter

            elif caracter.isdigit():

                if caracter == '0':
                    caracter = '100'
                    crypto += caracter
                elif caracter == '1':
                    caracter = '133'
                    crypto += caracter
                elif caracter == '2':
                    caracter = '134'
                    crypto += caracter
                elif caracter == '3':
                    caracter = '135'
                    crypto += caracter
                elif caracter == '4':
                    caracter = '136'
                    crypto += caracter
                elif caracter == '5':
                    caracter = '137'
                    crypto += caracter
                elif caracter == '6':
                    caracter = '173'
                    crypto += caracter
                elif caracter == '7':
                    caracter = '174'
                    crypto += caracter
                elif caracter == '8':
                    caracter = '175'
                    crypto += caracter
                elif caracter == '9':
                    caracter = '146'
                    crypto += caracter

            else:
                crypto += caracter

        crypto = int(crypto)

        self.__crypto = hex(crypto)

        if len(self.__crypto) < 32:
            self.__crypto += 'z'

        while len(self.__crypto) < 32:
            self.__crypto += self.__crypto

        while len(self.__crypto) > 32:
            self.__crypto = self.__crypto[:-1]

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


if __name__ == "__main__":
    usuario = Encriptar()
    usuario.pedirPassword()
