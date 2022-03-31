from random import randint


def ordenamiento_de_burbuja(lista):  # O(n**2)
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j + 1] = lista[j+1], lista[j]

    return lista


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamaño será la lista?: "))

    lista = ([randint(0, 100) for i in range(tamano_de_lista)])
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(
        lista_ordenada)
