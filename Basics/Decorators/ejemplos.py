from time import time

def performance(funcion):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = funcion(*args, **kwargs)
        t2 = time()
        print(f'La funcion se ejecuto en [{t2-t1}] seg')
        return result
    return wrapper

@performance
def muchoTiempo():
    for i in range(10000000):
        i*5

muchoTiempo()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True   # Si cambia a False no se ejecuta la funcion
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)