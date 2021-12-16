# BUCLE WHILE
def main():
    LIMITE = 1000
    
    contador=0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a '+ str(contador)+ 'es igual a: '+ str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

# BUCLE FOR
def main2():
    for contador in range(1000):
        print(contador)

if __name__ == '__main__':
    main()