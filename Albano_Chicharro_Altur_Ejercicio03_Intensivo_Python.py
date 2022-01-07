
# Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.
# Objetivo: 
# - Uso de bucles anidados
# - El uso de colecciones

# Albano Chicharro Altur
# Ejercicio 3
# Intensivo Python
# 06/01/2022

n = int(input('Introduce un número: '))
startnum = 1
listnumbers = []

while startnum <= n:
    counter = 1
    x = 0
    while counter <= startnum:
        if startnum % counter == 0:
            x = x + 1
        counter = counter + 1
    if x == 2:
        listnumbers.append(startnum)
    startnum = startnum + 1

print(f'Lista de números primos entre 1 y {n}\n{listnumbers}')