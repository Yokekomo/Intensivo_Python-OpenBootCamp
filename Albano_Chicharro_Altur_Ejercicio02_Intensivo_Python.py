
# Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
# 1) Añadir a cualquier persona, indicando nombre y después teléfono
# 2) Buscar el teléfono de una persona
# Objetivo: 
# - Aprender a manejar la entrada y la salida por consola.
# - El uso de colecciones (array o diccionario)

# Albano Chicharro Altur
# Ejercicio 2
# Intensivo Python
# 06/01/2022

barhead = '---------- AGENDA DE TELÉFONOS ----------'
searchoption = 'Buscar por nombre'
searchphone = 'Buscar por teléfono'
addoption = 'Añadir contacto'
printoption = 'Ver listado de contactos'
barbottom = '-----------------------------------------'

myagenda = {}

def menu():
    print(f'{barhead}\n1. {addoption}\n2. {searchphone}\n3. {searchoption}\n4. {printoption}\n{barbottom}')
    chousemenu = input('Introduce una opción del menu: ')
    print(f'{barbottom}')
    if chousemenu == '1':
        inputname = input("Nombre: ")
        inputphone = input('Teléfono: ')
        myagenda[inputphone] = inputname
        myagenda[inputname] = inputphone
        print(f'{barbottom}\nSe ha guardado la información correctamente\n{barbottom}')
        menu()
    if chousemenu == '2':
        phone = input('Introduzca el teléfono que busca: \n')
        print(f'{barbottom}\nEl propietario del {phone} es: {myagenda[phone]}\n{barbottom}')
        menu()
    if chousemenu == '3':
        name = input('Introduzca el nombre que busca: \n')
        print(f'{barbottom}\nEl teléfono de {name} es: {myagenda[name]}\n{barbottom}')
        menu()
    else:
        menu()
                
menu()
