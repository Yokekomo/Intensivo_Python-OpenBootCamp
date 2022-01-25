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
import pickle


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

        with open('archivo', 'wb') as archivo:
            pickle.dump(self.__password, archivo)
        with open('archivo', 'rb') as archivo:
            byte = archivo.read()
            from os import remove
            archivo.close()
            remove('archivo')

        byte = str(byte)

        password = ''

        for caracter in byte:
            nuevo_caracter = ord(caracter)
            nuevo_numero_desplazado = (int(nuevo_caracter) + 4) % 10
            nuevo_numero_desplazado = str(nuevo_numero_desplazado)
            password += nuevo_numero_desplazado

        password = list(password)

        lista_a = []
        lista_b = []

        while True:
            try:
                if len(password) >= 0:
                    lista_a.append(password.pop(0))
                    lista_b.append(password.pop(0))
            except IndexError:
                break

        lista_a = ''.join(lista_a)
        contador_a = 0

        while len(lista_a) > 7:
            try:
                contador_a += 1
                lista_a = int(lista_a) // 100
                lista_a = str(lista_a)
            except IndexError:
                break

        lista_b = ''.join(lista_b)
        contador_b = 0

        while len(lista_b) > 8:
            try:
                contador_b += 1
                lista_b = int(lista_b) // 100
                lista_b = str(lista_b)
            except IndexError:
                break

        crypto_final = lista_a + lista_b + str(contador_a) + str(contador_b)
        crypto2 = ''

        for caracter in crypto_final:
            nuevo_caracter = ord(caracter)
            caracter_crypto = str(nuevo_caracter)
            crypto2 += caracter_crypto

        crypto2 = hex(int(crypto2))
        crypto2 = str(crypto2)

        if len(crypto2) < 32:
            crypto2 += 'Z'

        self.__crypto = crypto2

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
                print('La contraseña no existe\nContraseña almacenada', self.__crypto,
                      '\nLa contraseña almacenada tiene', len(self.__crypto), 'caracteres')
        except:
            print('Algo salio mal en el diccionario')


if __name__ == "__main__":
    usuario = Encriptar()
    usuario.pedirPassword()
