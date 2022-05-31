# Average and Worst cases: O(n^2)
# Best case: O(n)
# It maintains a sorted subarray on left and the unsorted part values are placed 
# on at the correct position in the sorted part

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i - 1
        current = arr[i]
        while (arr[j] > current) and (j >= 0):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

# Regresa el indice del pivote ya acomodado
def partition(arr, left, right):
    pivot = arr[right] # El ultimo elemento de la lista es el pivote
    ptr = left # Mientras que el primero es el apuntador, que terminara siendo el indice de la posicion del pivote
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    
    # Finalmente se intercambian lugares el ultimo valor y el indice de donde debe ir el pivote
    arr[ptr], arr[right] = arr[right], arr[ptr]
    return ptr

# Worst case scenario: O(n^2)
# Average case scenario: O(nlog(n))
def quickSort(arr, left, right):
    # La lista contiene al menos 2 elementos, si left = right, entonces se tiene un solo elemento
    if left < right:
        pivot_index = partition(arr, left, right)
        # QuickSort en los elementos menores que el pivote
        quickSort(arr, left, pivot_index - 1)
        # QuickSort en los elementos mayores que el pivote
        quickSort(arr, pivot_index + 1, right)


if __name__ == '__main__':
    numbers1 = [15, 10, 4, 1, 2, 6, 24, 100, 59, 15]
    numbers2 = [1, 10, 4, 3, 22, 4, 45, 311, 529, 5, 4, 6, 2]
    insertionSort(numbers1)
    print(numbers1)
    quickSort(numbers2, 0, len(numbers2) - 1)
    print(numbers2)