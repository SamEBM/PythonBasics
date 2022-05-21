class MyGen():
    actual = 0
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if (MyGen.actual < self.fin):
            num = MyGen.actual
            MyGen.actual += 1
            return num
        raise StopIteration

gen = MyGen(0,100)
for i in gen:
    print(i)