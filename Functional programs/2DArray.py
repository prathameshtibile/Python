"""
* AUTHOR : Prathamesh Tibile
* Date   : 28-07-21
* Time   : 7.00 PM
* Title  : create 2 dimensional array in memory to read in M rows and N cols.
"""
Rows = int(input("Enter the number of rows:"))
Col = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries in row wise:")

for M in range(Rows):
    array = []
    for N in range(Col):
        array.append(int(input()))  # ---->ADDING INPUT IN ARRAY
    matrix.append(array)
print("The 2D array is given below:")
for M in range(Rows):
    for N in range(Col):
        print(matrix[M][N], end=" ")
    print()