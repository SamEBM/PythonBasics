# Merge Sort
# Divide and Conquer: Solution of subproblems are combined to solve the original problem
# Running time: O(n*log(n))
# ALGORITHM:
# 1.- Split array in half
# 2.- Call MergeSort on each half to sort them recursively
# 3.- Merge both sorted halves into one sorted array
# 4.- Continue until reach array of 1 element

def MergeSort(arr):
    # Si el arreglo no tiene un solo valor (ya esta "ordenado") divide el arreglo en dos mitades
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2] # Desde el indice 0 a la mitad del arreglo
        right_arr = arr[len(arr)//2:] # Desde la mitad hasta el final del arreglo
    
        # Recursion
        MergeSort(left_arr)
        MergeSort(right_arr)

        # Merge Step
        i = 0 # Left array index
        j = 0 # Rigth array index
        k = 0 # Merge array index
        
        # Ir comparando los elementos del arreglo izquierdo con el derecho para así agregarlos al arreglo superior
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Si ya se acabaron los elementos del arreglo derecho pero aún quedan en el izquierdo
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        # Si ya se acabaron los elementos del arreglo izquierdo pero aún quedan en el derecho
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    numbers = [2,3,5,1,7,4,4,4,2,6,0]
    MergeSort(numbers)
    print(numbers)