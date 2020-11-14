# We import infinity from math module to indicate min and max value in our matrix
from math import inf

# We import dot() from numpy module to get the result of scalar multiplication as a simplification of matrix
# multiplication
# The use of it is dot(vector_a, vector_b) and the result is value corresponding to the position in new matrix
from numpy import dot

# Here we define class named "matrix"
class matrix:
    ''' A class used to represent matrix

    Init parameters:
    ----------
    num_row : int
        a number representing number of rows
    num_col : int
        a number representing number of columns
    mode : str
        a string selecting what kind of matrix we want to create (default = input)'''
# This function is our constructor, it takes arguments we present to it and sets it as our starting variables
# It also creates empty list of lists - our matrix
# Double underscore means that vairable is private and we have access to it by getters and setters 
# Mode argument allows us to choose what kind of matrix we want to initiate:
#   "input" as a default mode creates matrix to be filled by the user
#   "empty" mode creates matrix filled with 0s to use in diffrent methods
#   "test" modes create matrices with predefined list of lists
    def __init__(self, num_row, num_col, mode = "input"):
        self.__rows = num_row
        self.__columns = num_col
        # Here is defined how we create matrix in default mode
        if mode == "input":
            # Here we create list of lists full of 0s
            self.m_matrix = self.empty_matrix()
            # Here the user is asked to input values "the most efficient way" which is inputing as many numbers 
            # in one run of a loop as we can
            if self.get_columns() >= self.get_rows():
                for row in range(self.get_rows()):
                    print("Input", self.get_columns(), "values in row no.", row)
                    for i in range(self.get_columns()):
                        self.m_matrix[row][i] = int(input())
            else:
                for column in range(self.get_columns()):
                    print("Input", self.get_rows(), "values in column no.", column)
                    for i in range(self.get_rows()):
                        self.m_matrix[i][column] = int(input())
        # Here is defined what matrix is created in diffrent modes
        elif mode == "empty":
            self.m_matrix = self.empty_matrix()

        elif mode == "test1":
            self.m_matrix = [[5, 4, 7], [1, 7, 3]]

        elif mode == "test2":
            self.m_matrix = [[5, 8], [4, 3], [1, 4]]

        elif mode == "test3":
            self.m_matrix = [[20, 16, 28], [4, 28, 12]]

        elif mode == "test4":
            self.m_matrix = [[48, 80], [36, 41]]

        else:
            print("Error: wrong mode")

# These are our getters so we can acces our values
    def get_columns(self):
        return self.__columns
    
    def get_rows(self):
        return self.__rows
    
    def list_of_columns(self):
        '''Returns list of lists being a column vector of a matrix'''
        # Which in fact is just transposed matrix...
        new_lists = []
        for column in range(self.get_columns()):
            new_list = []
            for row in range(self.get_rows()):
                new_list.append(self.m_matrix[row][column])
            new_lists.append(new_list)
        return new_lists

    def input_values_in_column(self, column):
        '''Inputs values - first inputs whole column
        Parameters:
        ----------
        column : int
            number of the column'''

        print("Input", self.get_rows(), "values in column no.", column)
        for i in range(self.get_rows()):
            self.m_matrix[column][i] = int(input())

    def input_values_in_row(self, row):
        '''Inputs values - first inputs whole row
        Parameters:
        ----------
        row : int
            a number of the row'''

        print("Input", self.get_columns(), "values in column no.", row)
        for i in range(self.get_columns()):
            self.m_matrix[i][row] = int(input())

    def input_value_in_position(self, row, column):
        '''Inputs one valuse in specific position in matrix
        Parameters:
        ----------
        row : int
            a number of the row
        column : int
            a number of the column'''

        self.m_matrix[row][column] = int(input())

    def empty_matrix(self):
        '''Returns "empty matrix" - list of lists full of 0s'''
        new_matrix = [[0 for i in range(self.get_columns())] for j in range(self.get_rows())]
        return new_matrix

    def sum_values(self):
        '''Returns the sum of values in our matrix'''
        value = 0
        for column in self.m_matrix:
            for value_in_row in column:
                if value_in_row != None and column != None:
                    value += value_in_row
        return value

    def find_min(self):
        '''Returns minimal value in our matrix by checking if the value we are looking at is smaller than 
        the previous one (starting from infinity)'''
        value = inf
        for column in self.m_matrix:
            for value_in_row in column:
                if value_in_row < value:
                    value = value_in_row
        return value

    def find_max(self):
        '''Returns maximal value in our matrix by checking if the value we are looking at is greater than
        the previous one (starting from negative infinity)'''
        value = -inf
        for column in self.m_matrix:
            for value_in_row in column:
                if value_in_row > value:
                    value = value_in_row
        return value

    def average(self):
        '''Returns average of values in our matrix by takeing the sum of them and dividing it 
        by number of values in matrix, calulated by multiplying number of columns by number of rows'''
        return (self.sum_values()/(self.get_columns() * self.get_rows()))

    def sum_row(self, row):
        '''Returns the sum of values in given row
        Parameters:
        ----------
        row : int 
            a number of the row'''
        value = 0
        for i in range(self.get_columns()):
            value += self.m_matrix[row][i]
        return value

    def sum_column(self, column):
        '''Returns the sum of values in given column
        Parameters:
        ----------
        column : int
            a number of the column'''
        value = 0
        for i in range(self.get_rows()):
            value += self.m_matrix[i][column]
        return value
    
    def sum_in_columns(self):
        '''Returns the list of sums of values in all columns'''
        value = [0 for i in range(self.get_columns())]        
        for i in range(0, self.get_columns()):
            value[i] += self.sum_column(i)
        return value

    def sum_in_rows(self):
        '''Returns the list of sums of values in all rows'''
        values = [0 for i in range(self.get_rows())]
        for i in range(0, self.get_rows()):
            values[i] += self.sum_row(i)        
        return values

    def average_in_columns(self):
        '''Returns the list of means of values in all columns'''
        values = self.sum_in_columns()       
        for i in range(len(values)):
            values[i] = values[i]/self.get_rows()        
        return values
    
    def average_in_rows(self):
        '''Returns the list of means of values in all rows'''
        values = self.sum_in_rows()        
        for i in range(len(values)):
            values[i] = values[i]/self.get_columns()        
        return values

    def is_square(self):
        '''Returns boolean value representing weather the matrix is square or not'''
        return self.get_rows() == self.get_columns()
            
    def multiply_diagonal(self):
        '''Returns the result of multiplication of values on the diagonal'''
        value = 1
        if self.is_square():
            for i in range(self.get_columns()):
                value = value * self.m_matrix[i][i]      
        return value

    def multiply_by_numerical_value(self, value):
        '''Returns new matrix object with values from original matrix multiplied by given numerical value
        Parameters:
        ----------
        value : int
            numerical value to multiply the matrix by'''
        # Here we create new matrix to return
        new_matrix = matrix(self.get_rows(), self.get_columns(), "empty")
        for row in range(self.get_rows()):
            for column in range(self.get_columns()):
                # Here we fill our new matrix with results of multiplying original matrix by numerical value
                new_matrix.m_matrix[row][column] = self.m_matrix[row][column] * value        
        return new_matrix

    def add_matrix(self, matrix_b):
        '''Returns new matrix object with values from given matrix added to original matrix
        Parameters:
        ----------
        matrix_b : matrix object 
            a matrix which is to be added to original matrix'''
        # First we check if our matrices have the same dimensions
        new_matrix = matrix(self.get_rows(), self.get_columns(), "empty")
        if self.get_columns() == matrix_b.get_columns() and self.get_rows() == matrix_b.get_rows():
            # And then we add the values
            for column in range(self.get_columns()):
                for row in range(self.get_rows()):
                    new_matrix.m_matrix[row][column] = self.m_matrix[row][column] + matrix_b.m_matrix[row][column]
            return new_matrix
        else:
            return None     

    def multiply_by_matrix(self, matrix_b):
        '''Returns new matrix object being a product of multiplying original matrix by given matrix
        Parameters:
        ----------
        matrix_b : matrix object
            a matrix by which original matrix is to be multiplied'''
        # First we check if it is possible to multiply the matrices
        # Due to Cauchys' definition we can only multiply matrices if number of columnss in matrix A is equal to number of rows
        # in matrix B 
        if self.get_columns() == matrix_b.get_rows():
            # Here we create new matrix with dimensions given in the Cauchys' definition: multiplying n×m matrix by m×p matrix
            # results in n×p matrix
            new_matrix = matrix(self.get_rows(), matrix_b.get_columns(), "empty")
            # To get the results we use the fact that we can simplify the multiplication of matices to the scalar
            # multipliaction of row vector and column vector
            # Here we create column vector 
            column_vector = matrix_b.list_of_columns()
            for column in range(matrix_b.get_columns()):
                for row in range(self.get_rows()):
                    # Here we use dot() function from numpy to get the result of scalar multiplication
                    # We take m_matrix[row] as our row vector
                    new_matrix.m_matrix[row][column] = dot(self.m_matrix[row], column_vector[column])
            return new_matrix
        else:
            return None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

test_matrix_1 = matrix(2, 3, "test1")

assert test_matrix_1.sum_values() == 27
assert test_matrix_1.find_max() == 7
assert test_matrix_1.find_min() == 1
assert test_matrix_1.average() == 4.5
assert test_matrix_1.average_in_columns() == [3.0, 5.5, 5.0]
assert test_matrix_1.average_in_rows() == [5.333333333333333, 3.6666666666666665]
assert test_matrix_1.multiply_diagonal() == 1
assert test_matrix_1.is_square() == False

test_matrix_2 = matrix(3, 2, "test2")

test_result_matrix = matrix(2, 3, "test3")

test_result_matrix_2 = matrix(2, 2, "test4")

# We test only m_matrix member of each object due to objects taking up different places in memory 
# We can compare m_matrix due to them being identical and taking up the same place in memory
A = test_matrix_1.multiply_by_numerical_value(4)
# Due to the fact that the tested matrices don't have the same dimensions we cannot add them to each other
# so the method returns NoneType object
B = test_matrix_1.add_matrix(test_matrix_2)
C = test_matrix_1.multiply_by_matrix(test_matrix_2)

assert A.m_matrix == test_result_matrix.m_matrix
# Same comment as in lines 249-250
assert B == None
assert C.m_matrix == test_result_matrix_2.m_matrix
