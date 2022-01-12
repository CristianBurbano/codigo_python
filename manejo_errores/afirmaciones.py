def primera_lista(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras


if __name__ == '__main__':
    lista = ['', 5, 'Esta es una oracion', 'Otra oración',
             'Mas oraciones por si acaso', 'Rayos! ya no quiero hacer mas oraciones']
    print(primera_lista(lista))
