# Albano Chicharro Altur
# Ejercicio 6b
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
import hashlib


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


        caracteres_password = []

        for i in self.__password:
            caracteres_password.append(i)

        if (len(self.__password) <= 12) and (len(self.__password) >= 6):

            nuevo_password = []

            for i in range(len(self.__password)):
                i = (ord(caracteres_password[i]))
                while len(str(i)) < 10:
                    i *= 3
                decimal = 0
                numero_de_bits = len(str(i))

                for n in range(numero_de_bits):
                    decimal = decimal + int(str(i)[-(n + 1)]) * 2 ** n
                hexadecimal = hex(decimal)
                hexadecimal = hexadecimal.replace('0x', '')
                nuevo_password.append(hexadecimal)

            nuevo_password_01 = ''.join(str(x) for x in nuevo_password)

            caracteres_password = []

            for i in nuevo_password_01:
                caracteres_password.append(i)

            nuevo_password_02 = ' '.join(str(x) for x in caracteres_password)
            lista_numeros = [int(num) for num in nuevo_password_02.split() if num.isdigit()]
            lista_caracteres = [str(x) for x in nuevo_password_02.split() if not x.isdigit()]

            for i in lista_numeros:
                x = i * 3 * 6
                lista_numeros.remove(i)
                lista_numeros.append(x)

            for i in reversed(lista_numeros):
                x = i * 3 * 6
                lista_numeros.remove(i)
                lista_numeros.append(x)

            for i in lista_numeros:
                x = i * 3 * 6
                lista_numeros.remove(i)
                lista_numeros.append(x)

            for i in reversed(lista_numeros):
                x = i * 3 * 6
                lista_numeros.remove(i)
                lista_numeros.append(x)

            lista_para_saber_numero_caracteres = lista_numeros + lista_caracteres
            cadena = ''.join(str(x) for x in lista_para_saber_numero_caracteres)

            cadena2 = ''.join(str(x) for x in lista_numeros)
            cadena3 = ''.join(str(x) for x in lista_caracteres)

            numero_32 = 32 - len(cadena3)

            cadena2 = cadena2[:numero_32:]

            lista_numeros_final = []

            for i in cadena2:
                lista_numeros_final.append(i)

            lista_final = []

            while True:
                try:
                    if len(lista_numeros_final) >= 0:
                        lista_final.append(lista_numeros_final.pop(0))
                    if len(lista_caracteres) >= 0:
                        lista_final.append(lista_caracteres.pop(0))
                except IndexError:
                    break

            while True:
                try:
                    if len(lista_numeros_final) >= 0:
                        lista_final.append(lista_numeros_final.pop(0))
                except IndexError:
                    break

            while True:
                try:
                    if len(lista_caracteres) >= 0:
                        lista_final.append(lista_caracteres.pop(0))
                except IndexError:
                    break

            self.__crypto = ''.join(str(x) for x in lista_final)
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



