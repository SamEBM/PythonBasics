# SET es como un conjunto matemático

set1 = {char for char in 'hello'}
set2 = {number for number in range(0, 100)}
set3 = {number**2 for number in range(0, 100)}
set4 = {number**2 for number in range(0, 100) if number % 2 == 0}

print(set1)
print(set4)

diccionario = {
    'a': 1,
    'b': 2
}

diccionarioPro = {key: valor**2 for key, valor in diccionario.items()}
print(f'Diccionario elevado al cuadrado: {diccionarioPro}')

diccionarioPro2 = {key: valor**2 for key,
                   valor in diccionario.items() if valor % 2 == 0}
print(f'Diccionario elevado al cuadrado con numeros pares: {diccionarioPro2}')

# Key = num, value = num * 2
diccionarioNuevo = {num: num*2 for num in [1, 2, 3]}
print(diccionarioNuevo)
