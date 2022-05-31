# Encontrar la suma máxima posible de valores contiguos
# Input: [-2, -3, 4, -1, -2, 1, 5, -3]
# Output: 7 ya que 4 - 1 - 2 + 1 + 5 es la suma máxima posible

def maxSubArraySum(a,size):

    max_so_far = a[0]
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only  
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far

if __name__ == "__main__":
    numbers = []
    n = int(input("¿De qué tamaño es tu arreglo? "))
    for i in range(n):
        numbers.append(int(input("Siguiente numero: ")))
    
    print("El numero máximo contiguo es: ", maxSubArraySum(numbers, len(numbers)))