# https://platzi.com/clases/1775-poo-python/25225-encapsulacion-getters-and-setters/
# En este ejercicio se utiliza el decorador @property, pero tambien se puede hacer el proceso manual, o utilizando la funcion property:
#

class CasillaDeVotacion:

    def __init__(self, identificador, pais) -> None:
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(
                f'la region {region} no es valida en {self.__pais}')

    # generando getters and setters con el metodo property, no tan escalable como el decorador

    def __get_identificador(self):
        return self.__identificador

    def __set_identificador(self, nuevo_identificador):
        print(
            f'se esta modificando el identificador a {nuevo_identificador}. Aiuuuuda!!!!')
        self.__identificador = nuevo_identificador

    identificador = property(__get_identificador, __set_identificador)


casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
print(casilla.region)
casilla.region = 'Ciudad de Mexico'
print(casilla.region)


casilla.identificador = 15
