# El número par mayor

def parMayor(li):
    pares = []
    for i in li:
        if(i % 2 == 0):
            pares.append(i)
    return max(pares)


print(f'El numero par mayor de la lista es: {parMayor([10,2,3,4,8,11])}')
