from random import randint


def busqueda_binaria():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
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

    print(f'la raiz cuadrada de {objetivo} es {respuesta}')

# https://platzi.com/clases/1775-poo-python/25264-busqueda-binaria/


def busqueda_binaria_recursiva(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1 ]}')
    if comienzo > final:
        return False
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria_recursiva(lista, comienzo, medio - 1, objetivo)


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamaño será la lista?: "))
    objetivo = int(input('Que número quieres encontrar?'))

    lista = sorted([randint(0, 100) for i in range(tamano_de_lista)])
    encontrado = busqueda_binaria_recursiva(lista, 0, len(lista), objetivo)
    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista ')
