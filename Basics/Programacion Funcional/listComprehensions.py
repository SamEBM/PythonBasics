lista = []
for char in 'hello':
    lista.append(char)
print('Lista normal')
print(lista)

lista2 = [char for char in 'hello']
print('\nLista rápida')
print(lista2)

lista3 = [number for number in range(0, 100)]
print('\nLista de números de 0 a 100')
print(lista3)

lista4 = [number**2 for number in range(0, 100)]
print('\nLista de números de 0 a 100 elevados al cuadrado')
print(lista4)

lista5 = [number**2 for number in range(0, 100) if number % 2 == 0]
print('\nLista de números pares de 0 a 100 elevados al cuadrado')
print(lista5)
