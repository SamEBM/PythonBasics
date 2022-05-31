# Quick Sort
# Pivot: Any number which will help to compare all the other values (se puede usar el ultimo valor, el primero o la mediana)
# If the number is greater it goes to one list, if it is smaller to other list
# Worst case scenario O(n^2)
# Average Time Complexity O(n*log(n))

def QuickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for number in sequence:
        if(number < pivot):
            items_greater.append(number)
        else:
            items_lower.append(number)
    
    return QuickSort(items_lower) + [pivot] + QuickSort(items_greater)


if __name__ == '__main__':
    #print(QuickSort([5,6,7,1,3,6,8,10,23,5454,135,90,23]))
    print(QuickSort([0,1,1,0,1,0,1,1,1,0,0,0,1]))