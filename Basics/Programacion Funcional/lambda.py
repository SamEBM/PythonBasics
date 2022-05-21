# LAMBDA EXPRESSIONS
# lambda parametro: action(parametro)
from functools import reduce    # Para importar la funcion 'reduce'

lista = [1, 2, 3]
print(list(map(lambda item: item*2, lista)))
print(list(filter(lambda item: item % 2 != 0, lista)))
print(reduce(lambda acc, item: acc + item, lista))

miLista = [5, 4, 3]
print(list(map(lambda item: item**2, miLista)))

# List Sorting: Acomodar las tuplas con su segundo valor empezando con el menor
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
