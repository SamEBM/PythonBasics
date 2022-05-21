# Usuarios
#   Magos
#   Arqueros
#   Etc

class Usuario:
    def __init__(self, email):
        self.email = email

    def iniciaSesion(self):
        print('Iniciando sesion...')


class Mago(Usuario):
    def __init__(self, nombre, poder, email):
        Usuario.__init__(self, email)
        self.nombre = nombre
        self.poder = poder

    def atacar(self):
        print(f'Atacando con un poder de {self.poder}')


class Arquero(Usuario):
    def __init__(self, nombre, flechas, email):
        Usuario.__init__(self, email)
        self.nombre = nombre
        self.flechas = flechas

    def atacar(self):
        print(f'Atacando con flecha. Flechas restantes: {self.flechas}')


mago1 = Mago('Merlin', 50, 'saisna@gmail.com')
mago1.iniciaSesion()
mago1.atacar()

arquero1 = Arquero('Robin', 100, 'jaja@hotmail.com')
arquero1.atacar()

print(isinstance(mago1, Mago))  # Verdadero
print(isinstance(mago1, Usuario))  # Verdadero
print(isinstance(mago1, object))  # 'object' es la clase padre de todas


# POLIMORFISMO
def ataqueJugador(personaje):
    personaje.atacar()


ataqueJugador(mago1)
ataqueJugador(arquero1)

for personaje in [mago1, arquero1]:
    personaje.atacar()
