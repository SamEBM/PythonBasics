from functools import reduce    # Para importar la funcion 'reduce'

# 1 Capitalize all of the pet names and print the list (Con MAP)
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def ponerMayuscula(item):
    return item.capitalize()


print(list(map(ponerMayuscula, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest. (Con ZIP)
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

# Sorted los ordena de menor a mayor
print(list((zip(my_strings, sorted(my_numbers)))))

# 3 Filter the scores that pass over 50% (Con FILTER)
scores = [73, 20, 65, 19, 76, 100, 88]


def mayores50(item):
    return item > 50


print(list((filter(mayores50, scores))))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total? (Con REDUCE)


def total(acumulable, item):
    return acumulable + item


print(reduce(total, my_numbers + scores))
