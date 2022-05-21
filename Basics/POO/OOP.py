class BigObject:  # Clase
    pass


obj1 = BigObject()  # Instancia
print(type(obj1))


class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name='Anonimo', age=0):
        if(PlayerCharacter.membership):
            if(age >= 18):
                self._name = name  # Por convencion, a los atributos privados se les pone _
                self._age = age

    def shout(self):
        print(f'Mi nombre es {self._name} y tengo {self._age} años')

    @classmethod
    def SumarEdades(cls, num1, num2):
        return cls('Creado', num1 + num2)

    @staticmethod
    def Sumar(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Samuel', 21)
player2 = PlayerCharacter('Daniel', 21)
player3 = PlayerCharacter(age=18)
player2.attack = 50

print(player1)
print(player1._name)
print(player2.attack)
player1.shout()
player2.shout()
player3.shout()

# No necesitas instanciar un objeto para usarlo
print(PlayerCharacter.SumarEdades(2, 3))
