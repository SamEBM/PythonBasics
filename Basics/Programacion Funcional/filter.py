def soloImpares(item):
    return item % 2 != 0


print(list((filter(soloImpares, [1, 2, 3, 4]))))
