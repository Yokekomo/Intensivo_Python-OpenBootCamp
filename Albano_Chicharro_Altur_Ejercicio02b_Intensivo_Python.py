
# Ampliación del ejercicio 2:
# - Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
#   Introduce un nombre: Pep
#   Resultados: 
#   - Pepe 659331013
#   - Pepe Martín 633743551

# Albano Chicharro Altur
# Ejercicio 2b
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
    print(f'{barbottom}\n{barhead}\n1. {addoption}\n2. {searchphone}\n3. {searchoption}\n{barbottom}')
    chousemenu = input('Introduce una opción del menu: ')
    print(f'{barbottom}')
    if chousemenu == '1':
        inputname = input("Nombre: ")
        inputphone = input('Teléfono: ')
        myagenda[inputphone] = inputname
        myagenda[inputname] = inputphone
        print(f'{barbottom}\nSe ha guardado la información correctamente\n{barbottom}')
        menu()
    if chousemenu == '2' or '3':
        name = input('Introduzca nombre o teléfono: \n')
        for index in range(len(name)):
            charname = name[index]
        for charname in myagenda:
            if charname.startswith(name):
                print(f' - {charname} {myagenda[charname]}')
        menu()
    else:
        menu()
                
menu()
