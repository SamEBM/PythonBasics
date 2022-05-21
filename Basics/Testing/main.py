def Cinco(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Ingresa un numero'
    except ValueError as err:
        return err