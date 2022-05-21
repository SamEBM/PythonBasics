# *args y **kwargs

def funcion(*args, **kwargs):
    total = 0
    # Imprime los elementos de la lista
    print(*args)
    # Imprime la lista
    print(args)
    # Imprime un diccionario
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(funcion(1, 2, 3, 4, 5, num1=5, num2=10))


# RULE: parameters, *args, default parameters, **kwargs

def funcion2(name, *args, i='Hi', **kwargs):
    total = 0
    # Imprime los elementos de la lista
    print(*args)
    # Imprime la lista
    print(args)
    # Imprime un diccionario
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(funcion2('Samuel', 1, 2, 3, 4, 5, num1=5, num2=10))
