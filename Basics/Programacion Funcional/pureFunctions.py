# PURE FUNCTION
def mul2(li):
    nuevaLista = []
    for item in li:
        nuevaLista.append(item*2)
    return nuevaLista


print(mul2([1, 2, 3]))

# NON PURE FUNCTION
lista = []


def mul(li):
    for item in li:
        lista.append(item*2)
    return lista


print(mul([1, 2, 3]))
