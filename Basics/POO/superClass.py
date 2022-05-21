class SuperList(list):  # Hereda de la clase list
    def __len__(self):
        return 1000


lista = SuperList()
print(len(lista))
lista.append(5)
print(lista[0])
print(issubclass(SuperList, list))
