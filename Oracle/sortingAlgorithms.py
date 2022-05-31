# MaxHeap
# Complete Binary Tree where every node <= its parent
# Insert in O(log n)
# GetMax in O(1)
# Remove Max in O(log n)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def siftDown(lst, i, upper):
    while(True):
        l, r = i*2+1, i*2+2
        if max(l, r) < upper:
            if lst[i] >= max(lst[l], lst[r]): break
            elif lst[l] > lst[r]: 
                swap(lst, i, l)
                i = l
            else:
                swap(lst, i, r)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, i, l)
                i = l
            else: break
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst, i, r)
                i = r
            else: break
        else: break

def HeapSort(numberList):
    for j in range(len(numberList)-2//2, -1, -1):
        siftDown(numberList, j, len(numberList))

    for end in range(len(numberList)-1, 0, -1):
        swap(numberList, 0, end)
        siftDown(numberList, 0, end)

# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    
    # Pointer for greater element
    i = low - 1
    
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
        
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
        
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    
    # Return the position from where partition is done
    return i + 1

# Function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':
    numbers1 = [5,16,8,14,20,1,26]
    numbers2 = [5,16,8,14,20,1,26]
    numbers3 = [0,16,10,0,0,12,0]
    HeapSort(numbers1)
    print(numbers1)
    quick_sort(numbers2, 0, len(numbers2) - 1)
    print(numbers2)
    mergeSort(numbers3)
    print(numbers3)