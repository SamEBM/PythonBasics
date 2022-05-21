from collections import deque
from re import S

numbers = [1,2,3,4,5]
squares = [x**2 for x in numbers]
odds = [x for x in range(10) if x%2 == 1]

## STACK - LIFO
my_stack = list()
my_stack.append(3)
my_stack.append(4)
my_stack.append(5)
my_stack.append(6)

# print(my_stack.pop())

## PILA como una clase
class Stack(): 
    def __init__(self) -> None:
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self) -> str:
        return  str(self.stack)

pila = Stack()
pila.push(3)
pila.push(2)
pila.push(1)

print(pila.pop())
print(pila.peek())

## QUEUE - FIFO
cola  = deque()
cola.append(5)
cola.append(10)
print(cola)
print(cola.popleft())

## MaxHeap
## Complete Binary Tree where every node <= its parent
## Insert in O(log n)
## Get max in O(1)
## Remove Max in O(log n)

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
    
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        return self.heap[1] if self.heap[1] else False
    
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self) -> str:
        return str(self.heap)

pilaMaxima = MaxHeap([95,3,21])
pilaMaxima.push(10)
print(pilaMaxima)
print(pilaMaxima.pop())
print(pilaMaxima.peek())