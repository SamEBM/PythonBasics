# HASH TABLE COMPLEXITY
# Worst case: O(n) when a key has more than one value 
# Average case: O(1)

if __name__ == "__main__":
    nameDict = {
        'Samuel': 1,
        'Azul': 2,
        'Daniel': 3,
        'Alonso': 4,
    }
    numbers = [1, 2, 3, 4, 5]
    for i, value in enumerate(numbers):
        print(str(i) + ": " + str(value))

