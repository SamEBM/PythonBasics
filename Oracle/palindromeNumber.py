# Given an integer, write a function that returns true if the given number is palindrome, else false. 
# For example, 12321 is palindrome, but 1451 is not palindrome. 
def checkPalindrome(str):
    for i in range(0, len(str) // 2):
        if str[i] != str[len(str)-1-i]:
            return print("El numero --{}-- no es un palíndromo.".format(str))
    return print("El numero --{}-- sí es un palíndromo.".format(str))

if __name__ == "__main__":
    number = input("Ingresa un numero para verificar si es un palíndromo: ")
    checkPalindrome(number)

