# https://platzi.com/clases/1775-poo-python/25259-introduccion-a-la-complejidad-algoritmica/
# midiendo el tiempo para cuando nos aproximamos a infinito para ver cual algoritmo es más eficiente
import time
import sys


def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n-1)


if __name__ == "__main__":
    sys.setrecursionlimit(2000000)
    n = 50000000

    comienzo = time.time()
    r = factorial(n)
    final = time.time()
    print(f' tiempo= {final - comienzo}')

    # comienzo = time.time()
    # r = factorial_r(n)
    # final = time.time()
    # print(f' tiempo= {final - comienzo}')
