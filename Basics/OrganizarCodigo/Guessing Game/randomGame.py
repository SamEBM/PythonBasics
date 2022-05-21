from random import randint
import sys

# Generate a number between 1 - 10
respuesta = randint(int(sys.argv[1]),int(sys.argv[2]))

# Input from user
# Check that input is a number between 1 - 10
while True:
    try:
        intento = int(input(f'Adivina el numero del {int(sys.argv[1])} al {int(sys.argv[2])}: '))
        if  0 < intento <= 10:
            if(respuesta == intento):
                print('GANASTE! ')
                break
            else:
                print('Intenta otra vez')
    except:
        print('Por favor ingresa un numero entre 1 y 10')
        continue

# Check if number is the right guess. Otherwise ask again.
#if(respuesta == )

