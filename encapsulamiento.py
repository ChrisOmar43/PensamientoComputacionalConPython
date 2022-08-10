def opciones():
    print (f'Opciones para hallar raiz cuadrada \n (1) Enumeracion exhaustiva \n (2) Aproximacion de soluciones \n (3) Busqueda binaria')
    opcion = int(input('Elija una opcion: '))
    numero = int(input('Elija un numero: '))
    while opcion < 1 or opcion > 3:
        print(f'Escriba una opcion valida')
        opcion = int(input('Elija una opcion: '))
        numero = int(input('Elija un numero: '))
    
    if opcion == 1:
        enumeracion(numero)
    elif opcion == 2:
        aproximacion(numero)
    elif opcion == 3:
        busqueda_binaria(numero)
    else:
        print(f'Prueba fallida')

def enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso 

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada {objetivo} es {respuesta}') 

def busqueda_binaria(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta 
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

opciones()