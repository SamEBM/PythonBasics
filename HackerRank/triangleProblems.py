# Print the next triangle of numbers in just 2 lines of code, one for loop and no string operations
# 1
# 22
# 333
# 4444
print('Ingresa el tamaño del triangulo: ')
for i in range(1,int(input())): 
    print(i*int((10**i-1)/9))

# Print the next triangle of numbers in just 2 lines of code, one for loop and no string operations
# 1
# 121
# 12321
# 1234321
# 123454321
print('\nIngresa el tamaño del triangulo: ')
for i in range(1,int(input())+1):
    print(int((10**i-1)/9)**2)