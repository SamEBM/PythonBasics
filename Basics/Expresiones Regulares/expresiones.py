import re

patron = re.compile('Buscar algo')
igual = re.compile('Buscar algo en este texto con algo')
cadena = 'Buscar algo en este texto con algo'

print('Buscar' in cadena)

# a = re.search('algo',cadena) # Objeto de tipo "Match"
a = patron.search(cadena)
b = patron.findall(cadena)   # Recolecta todas las ocurrencias
print(a.span())              # Indice donde empieza y termina lo que buscas
print(a.group())             
print(b)

# Verificar si dos cadenas son iguales
c = igual.fullmatch(cadena)
print(c)

# Subcadena
d = patron.match(cadena)     # La cadena contiene el patron buscado
print(d)