while True:
    try:
        edad = int(input('¿Cual es tu edad? '))
        10/edad
    except ValueError:
        print('Por favor ingresa un numero')
    except ZeroDivisionError:
        print('Por favor ingresa una edad valida')
    else:
        print('Gracias')
        break

def division(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as error:
        print(f'[{error}] Ingresa dos numeros')

print(division(1,'0'))
print(division('1',0))
print(division(1,0))