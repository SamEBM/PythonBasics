while True:
    try:
        edad = int(input('¿Cual es tu edad? '))
        10/edad
        raise ValueError('Ayudaaa')
    except ZeroDivisionError:
        print('Por favor ingresa una edad valida')
    else:
        print('Gracias')
        break