import random

# ---------------RANDOM---------------
# help(random)
# print(dir(random))
lista = [1,2,3,4,5]
print(random.randint(1,10))
print(random.choice(lista))
random.shuffle(lista)
print(lista)