# Given a 2D array, print it in spiral form. See the following examples.
# Input:  {{1,    2,   3,   4},
#          {5,    6,   7,   8},
#          {9,   10,  11,  12},
#          {13,  14,  15,  16 }}
# Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

# Approach: The problem can be solved by dividing the matrix into loops or squares or boundaries. It can be seen that the elements of the outer loop are printed first in a clockwise manner then the elements of the inner loop is printed. So printing the elements of a loop can be solved using four loops that print all the elements. Every ‘for’ loop defines a single direction movement along with the matrix. The first for loop represents the movement from left to right, whereas the second crawl represents the movement from top to bottom, the third represents the movement from the right to left, and the fourth represents the movement from bottom to up.

# Algorithm: 
# Create and initialize variables k – starting row index, m – ending row index, l – starting column index, n – ending column index
# Run a loop until all the squares of loops are printed.
# In each outer loop traversal print the elements of a square in a clockwise manner.
# Print the top row, i.e. Print the elements of the kth row from column index l to n, and increase the count of k.
# Print the right column, i.e. Print the last column or n-1th column from row index k to m and decrease the count of n.
# Print the bottom row, i.e. if k < m, then print the elements of m-1th row from column n-1 to l and decrease the count of m
# Print the left column, i.e. if l < n, then print the elements of lth column from m-1th row to k and increase the count of l.
# Below is the implementation of the above algorithm: 

def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m and l < n):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
 
        k += 1
 
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
 
        n -= 1
 
        # Print the last row from
        # the remaining rows
        if (k < m):
 
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
 
            m -= 1
 
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
 
            l += 1
 
 
# Driver Code
a = [[ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ],
     [ 9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ]]
 
R = 4
C = 4
 
# Function Call
spiralPrint(R, C, a)

# Time Complexity: O(m*n). 
# To traverse the matrix O(m*n) time is required.
# Auxiliary Space: O(1). 
# No extra space is required.
