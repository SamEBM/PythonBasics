# Generators are iterables
# Iterables are not always generators

range(100)
list(range(100))

def generatorFun(num):
    for i in range(num):
        yield i*2

g = generatorFun(10)

print(next(g))  # 1er numero: 0
print(next(g))  # 2do numero: 2
print(next(g))  # 3er numero: 4

for item in generatorFun(10):
    print(item)

#def makeList(num):
#    result = []
#    for i in range(num):
#        result.append(i*2)
#    return result

#lista = makeList(100)
#print(lista)