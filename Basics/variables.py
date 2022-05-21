# LOCAL & GLOBAL variables

total = 0

def count():
	global total 
	total += 1
	return total

print(count())
print(count())
print(count())

def superior():
	x = "local" #Variable local de superior()
	def interior():
		nonlocal x #Variable local de superior()
		x = "NO local"
		print("Interior: ", x)

	interior()
	print("Superior: ", x)

superior()