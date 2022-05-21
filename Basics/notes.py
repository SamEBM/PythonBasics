#PYTHON NOTES

#FOR LOOPS
#ITERABLE -List, Dictionary, Tuple, Set, String
# is iterated -> one by one check each item in the collection
user = {
	'name': 'Golem',
	'age': 5006,
	'can_swim': False
}

for i in user.items():
	print(i)

for i in user.values():
	print(i)

for i in user.keys():
	print(i)

for key, value in user.items():
	print(key,value)

for item in (1,2,3,4,5):
	for x in ['a','b','c']:
		print (item, x)

counter = 0
my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
	counter = counter + i
print (counter)


#RANGE
print('\n\n\n')
print(range(0,100))

for number in range(0,100): #Iterar range veces
	print (number)

for number in range(10,0,-1): #Iterar range veces
	print (number)

#ENUMERATE
print('\n\n\n')
for i,char in enumerate('Helloooo'):
	print(i,char)

print('\n')
for i,char in enumerate(list(range(100))):
	if(char == 50):
		print(f'Index of 50 is: {i}')


#WHILE LOOP
print('\n\n\n')
i=0
while (i < 10):
	print(i)
	i += 1
else:
	print('Acabo')

print('\n')
my_list = [1,2,3]

for item in my_list:
	print (item)

i=0
while (i < len(my_list)):
	print(my_list[i])
	i += 1

while True:
	response = input('Di algo > ')
	if(response == 'bye'):
		break