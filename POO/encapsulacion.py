# https://platzi.com/clases/1775-poo-python/25225-encapsulacion-getters-and-setters/

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


casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
print(casilla.region)
casilla.region = 'Ciudad de Mexico'
print(casilla.region)
