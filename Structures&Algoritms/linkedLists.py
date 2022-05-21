# Linked lists operations
# Add.- 
# Remove.-
# Find.-
# Print List.-

class Node:

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    
    def __str__(self):
        return '(' + str(self.data) + ')'

nodo1 = Node(5)
print(nodo1)

class LinkedList:
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, d):
        # El primer nodo para a ser el segundo
        new_node = Node(d, self.root)
        # El nuevo primer nodo es el valor insertado apuntando al root anterior
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return this_node.data
            else:
                this_node = this_node.next_node
        return None
    
    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None: # El nodo no es el root
                    prev_node.next_node = this_node.next_node
                else: # El valor esta en el nodo root
                    self.root = this_node.next_node
                self.size -= 1
                return True # Valor eliminado
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False # Valor no encontrado

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end="->")
            this_node = this_node.next_node
        print("None")

myList = LinkedList()
myList.add(5)
myList.add(10)
myList.add(15)
myList.add(20)

myList.print_list()

print("Tamaño de la lista = " + str(myList.size))
myList.remove(10)
print("Tamaño de la lista = " + str(myList.size))
print(myList.find(15))
print(myList.root)