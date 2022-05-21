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
        super().__init__(email)
        self.nombre = nombre
        self.poder = poder

    def atacar(self):
        print(f'Atacando con un poder de {self.poder}')


mago1 = Mago('Merlin', 50, 'saisna@gmail.com')
mago1.iniciaSesion()
mago1.atacar()
print(mago1.email)

# Introspeccion de los métodos de la clase
print(dir(mago1))
