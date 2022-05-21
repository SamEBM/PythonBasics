class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.diccionario = {
            'name': 'Yoyo',
            'hasPets': False
        }

    def __str__(self):
        return f'El color del juguete es: {self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return('A la orden')

    def __getitem__(self, i):
        return self.diccionario[i]


figura = Toy('red', 0)
print(figura.__str__())
print(figura)          # Equivalente a toString en Java
print(len(figura))
print(figura())
print(figura['name'])  # Accedemos como si fuera un arreglo
