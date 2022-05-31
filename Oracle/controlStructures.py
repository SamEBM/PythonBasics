if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    for i in range(len(lst)):
        print(lst[i], end = " ")
    
    # for j in range(0,10):
    #     print(j, end = " ")

    print('\n')
    
    m = 5
    i = 0
    while i < m:
        print(i, end = " ")
        i = i + 1
        if i == 3:
            break
    print("End")

    num1 = int(input("Ingresa un valor N para construir un arreglo: "))
    for j in range(num1):
        print(j, end = " ")

    spam = ['hello', 'hi', 'howdy', 'heyas']
    'cat' not in spam

    # Dictionaries 
    print('\n')
    spam = {'color': 'red', 'age': 23}
    for item in spam.values():
        print(item)

    for key in spam.keys():
        print(key)
    
    for tup in spam.items():
        print(tup)

    a = [1, 3, 5, 7, 9, 11]
    print([i - 1 for i in a])

    age = 15
    print('kid' if age < 18 else 'adult')