from collections import Counter, defaultdict, OrderedDict
from array import array
import datetime

lista = [1,2,3,4,5,6,7,7]
print(Counter(lista))

frase = 'blah blah jaja'
print(Counter(frase))

# Con defaultdict si se accede a un lugar desconocido, se le da un valor por default
diccionario = defaultdict(lambda: 5,{'a': 1, 'b': 2 })
print(diccionario['c'])

diccionario2 = OrderedDict()
diccionario2['a'] = 1
diccionario2['b'] = 2

diccionario3 = OrderedDict()
diccionario3['a'] = 1
diccionario3['b'] = 2

# Son iguales porque tienen el mismo orden y valor
print(diccionario2 == diccionario3)

############## datetime ################
print('\n')
print(datetime.time(5,45,2))
print(datetime.date.today())
########################################

############### arrays #################
print('\n')
arreglo = array('i', [1,2,3])
print(arreglo[0])

