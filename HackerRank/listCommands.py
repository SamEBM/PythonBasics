# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example 
# N = 4
# append 1
# append 2
# insert 3 1
# print

# Output:
# [1, 3, 2]

# Input Format
# The first line contains an integer, n, denoting the number of commands. 
# Each line  of the  subsequent lines contains one of the commands described above.
# Constraints
# The elements added to the list must be integers.
# Output Format
# For each command of type print, print the list on a new line.

mylist = []

if __name__ == '__main__':
    N = int(input())
    operations = []
    for _ in range(N):
        arr = input().split()
        operations.append(list(arr))
    print(operations)
    
    def listOperation(op, args = []):
        if op == 'insert':
            return mylist.insert(int(args[0]),int(args[1]))
        elif op == 'print':
            print(mylist)
        elif op == 'remove':
            return mylist.remove(int(args[0]))
        elif op == 'append':
            return mylist.append(int(args[0]))
        elif op == 'sort':
            return mylist.sort()
        elif op == 'pop':
            return  mylist.pop()
        elif op == 'reverse':
            return mylist.reverse()
        else: 
            pass

    for command in operations:
        if len(command) > 1:
            listOperation(command[0], command[1:])
        else:
            listOperation(command[0])