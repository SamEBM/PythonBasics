class Usuario:
    def iniciaSesion(self):
        print('Iniciando sesion...')


class Mago(Usuario):
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def atacar(self):
        print(f'Atacando con un poder de {self.poder}')


class Arquero(Usuario):
    def __init__(self, nombre, flechas):
        self.nombre = nombre
        self.flechas = flechas

    def verFlechas(self):
        print(f'Flechas restantes: {self.flechas}')

    def correr(self):
        print('Corriendo')


class MagoArquero(Mago, Arquero):
    def __init__(self, nombre, poder, flechas):
        Arquero.__init__(self, nombre, flechas)
        Mago.__init__(self, nombre, poder)


hibrido = MagoArquero('Merlin', 50, 100)
hibrido.iniciaSesion()
hibrido.correr()
hibrido.verFlechas()
