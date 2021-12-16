def run():
    mi_diccionario = {
        'llave1': 1,
        "llave2": 2,
        "llave3": 3
    }
    # print(mi_diccionario['llave1'])

    poblaciones_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    for pais, poblacion in poblaciones_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()