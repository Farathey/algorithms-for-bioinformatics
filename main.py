'''
3. Develop a class to keep numerical matrices. The attributes of the class should be the
number of rows, number of columns, and a list of lists keeping the elements of the matrix.
Implement a constructor to create an empty matrix given the number of rows and
columns. Implement methods with a functionality similar to the ones listed in the previous
question:

a.
b. indicate the largest (smallest) value in the matrix;
c. calculate the mean of the values in the matrix;
d. calculate the mean (or sum) of the values in each row (or column); the result should
be a list;
e. calculate the multiplication of the values in the diagonal;
f. check if the matrix is square (same number of rows and columns);
g. multiply all elements by a numerical value, returning another matrix;
h. add two matrices (assuming they have the same dimension);
i. multiply two matrices.
'''
from classes import matrix

print("Creating first matrix:")
# Here we ask the user how many rows and columns he wishes to have
rows = int(input("Input the number of rows "))
columns = int(input("Input the number of columns "))

# Here we create matrix object consisting of given numeber of rows and columns
A = matrix(rows, columns)

# Here we print the sum of values in matrix A
print("Sum of values in matrix A:", A.sum_values())

# Here we print the largest and the smallest value in matrix A
print("The largest value:", A.find_max())
print("The smallest value:", A.find_min())

# Here we print the mean of the values in matrix A
print("The mean of values:", A.average())

# Here we print the mean of values in each column and each row
print("The mean of values in columns :", A.average_in_columns())
print("The mean of values in rows :", A.average_in_rows())

# Here we print the product of multiplication of values on the diagonal, only if our matrix is square - and our matrix is
print("The product of multiplication of values on the diagonal:", A.multiply_diagonal())

# Here we check if our matrix is square
print("Matrix is square:", A.is_square())

# Here we ask user for the value with witch we want multpiply our matrix by and we print the product of this multipication
value = int(input("Input the value you want to multiply matrix by: "))
C = A.multiply_by_numerical_value(value)
print("The product of multiplying matrix by value:", C.m_matrix)

# Here we create second matrix for last exercies 
print("Creating second matrix:")

# Again we ask the user how many rows and columns he wishes to have
rows = int(input("Input the number of rows "))
columns = int(input("Input the number of columns "))

# Again we create matrix object consisting of given numeber of rows and columns
B = matrix(rows, columns)

# Here we print the product of adding matrix B to matrix A
D = A.add_matrix(B)
if D != None:
    print("First matrix + second matrix =", D.m_matrix)
else:
    print("Error: we cannot add matrices due to them not haveing the same dimensions")

# Here we print the product of multiplying matrix A by matrix B (only if it's possible!)
E = A.multiply_by_matrix(B)
if E != None:
    print("First matrix * second matrix =", E.m_matrix)
else:
    print('''Error: we cannot multiply this matrixes by each other
Number of columns in original matrix must be equal to number of rows in matrix which is to be multiplied by''')