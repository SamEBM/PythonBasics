from functools import reduce    # Para importar la funcion 'reduce'
lista = [1, 2, 3]


def acumulador(acumulable, item):
    print(acumulable, item)
    return acumulable + item


print(reduce(acumulador, lista, 0))
print(reduce(acumulador, lista, 10))
