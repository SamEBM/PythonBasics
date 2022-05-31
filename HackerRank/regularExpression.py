## Reemplazar todas las ocurrencias de ' && ' y ' || ' por ' and ' y ' or ' en un texto de N lineas
## Tomar en cuenta los espacios, si se encuentra un &&& o '|| no debe reemplazarlos

import re

def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

print('Ingresa el numero de lineas de texto a ingresar y cada una de ellas: ')
for _ in range(int(input())):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", change,input()))

# Expresión regular para validar numeros romanos
print("Ingresa un numero romano: ")
print(str(bool(re.match(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", input()))))

# Expresión regular que valide un numero de telefono de 10 digitos que comience con 7, 8 o 9
# Enter your code here. Read input from STDIN. Print output to STDOUT
expresion = r"^(7|8|9)[0-9]{9}$"
print("Ingresa la cantidad de numeros a introducir: ")
n = int(input())
for _ in range(n):
    print("Ingresa el numero de telefono a validar: ")
    if bool(re.match(expresion, input())):
        print("YES")
    else:
        print("NO")