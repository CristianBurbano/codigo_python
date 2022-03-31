# https://platzi.com/clases/1775-poo-python/25258-polimorfismo/
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("ando caminando")


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista("Daniela")
    ciclista.avanza()


if __name__ == "__main__":
    main()
