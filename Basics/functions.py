# FUNTIONS
# DRY: Do not Repeat Yourself

#Default Parameters
def sayHello(name = 'SAMUEL', emoji = '☻'):
	print (f'Helloooo {name}. Your emoji is {emoji}')

#Positional Arguments
nombre = input('Ingresa tu nombre: ')
emoji = input('Ingresa un emoji: ')
sayHello(nombre,emoji)

#Keyword Arguments
sayHello(emoji='♫',name='Ale')

#Default Arguments
sayHello()
sayHello('NombreX')

print('\n')
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def Tree():
	for image in picture:
		for pixel in image:	
			if (pixel == 0):
				print(' ',end='')
			else:
				print('*',end='')
		print('')	

Tree()
Tree()

#Location in Memory
print(f'Funcion Creada: {Tree}')

def sumar(num1,num2):
	'''
	INFO: Esta funcion regresa la suma de dos numeros
	'''
	return num1 + num2

print(f'El resultado es: {sumar(4,5)}')

#Function Information
help(sumar)
print(sumar.__doc__)