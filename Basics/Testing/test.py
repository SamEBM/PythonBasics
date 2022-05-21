import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('Vamos a hacer una prueba')
    
    def testCinco1(self):
        '''Primera prueba'''
        argumento = 10
        result = main.Cinco(argumento)
        self.assertEqual(result, 15)    # El resultado debe ser 15, si le ponemos otro número manda error

    def testCinco2(self):
        argumento = 'asasaf'
        result = main.Cinco(argumento)
        self.assertTrue(isinstance(result, ValueError))    # Debe causar un ValueError por intentar sumar una cadena con un entero y debe ser verdadero
    
    def testCinco3(self):
        argumento = None
        result = main.Cinco(argumento)
        self.assertEqual(result, 'Ingresa un numero')

    def testCinco4(self):
        argumento = ''
        result = main.Cinco(argumento)
        self.assertEqual(result, 'Ingresa un numero')

    def tearDown(self):
        print('Limpiando')

if __name__ == '__main__':
    unittest.main()

# COMANDO DESDE TERMINAL: python -m unittest -v
# Con el se pueden ver todos los test y hasta los comentarios