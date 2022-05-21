# @classmethod
# @staticmethod

def hello():
    print('Helloooo')


greet = hello
del hello
print(greet)
# hello()   Saldria error, porque ya no existe, aunque greet aún puede ser llamada
greet()

# Las funciones son como variables
print('\n\nEJEMPLO DE ANIDACION DE FUNCIONES,')


def funcion1(funcion2):
    funcion2()


def funcion2():
    print('Soy la funcion 2')


a = funcion1(funcion2)
print(a)

# Hight Order Function HOC

# Una funcion que acepta una funcion como parametro
def saludar(func):
    func()

# Una funcion que retorna otra funcion
def saludar2():
    def func():
        return 5
    return func


# Decorators
print('\n\nEJEMPLO DE DECORATORS')

def miDecorator(funcion):
    def wrapFuncion():
        print('*********')
        funcion()
        print('*********')
    
    return wrapFuncion

@miDecorator
def hello():
    print('Hellooo')

@miDecorator
def bye():
    print('See ya')

hello()
bye()

def miDecorator2(funcion):
    def wrapFuncion(*args,**kwargs):
        print('*********')
        funcion(*args,**kwargs)
        print('*********')
    
    return wrapFuncion

@miDecorator2
def hello2(saludo, emoji = ':('):
    print(saludo, emoji)

hello2('HOLAAAA', '♣')
hello2('HI')