from typing import List
import copy

Matrix0 = [
    [1, 3, 5, 7],
    [3, 5, 7, 9],
    [5, 7, 9, 1]
]

Matrix1 = [
    [1, -6, 3],
    [4, -17, -16],
    [-1, 3, 1],
]

Matrix2 = [
    [1, 0, 2],
    [-3, 15, -8],
]

def swaprows(r1:int, r2:int, matrix:List[List[int]]) -> List[List[int]]:
    """this function takes three int arguments, it will swap the two rows given"""
    newr1 = r1 - 1
    newr2 = r2 - 1

    row_r1 = matrix[newr1]
    row_r2 = matrix[newr2]

    matrix[newr1] = row_r2
    matrix[newr2] = row_r1

    print(f"Swap {row_r1} with {row_r2}\n Final = {matrix}")
    return matrix

def scalerow(scale:float, row:int, matrix:List[List[int]]) -> List[List[int]]:
    """
    This function takes three arguments,
    first being a value to scale the row by.
    Seccond being the row number to be scaled.
    Third the actual matrix itself"""

    newrow = row - 1

    print(f"Scale row{newrow} by {scale}, row{newrow}: {matrix[newrow]}")

    counter = 0
    for num in matrix[newrow]:
        matrix[newrow][counter] = scale * matrix[newrow][counter]
        counter += 1

    return matrix


def addrowtorow(r1:int, scale:float, r2:int, matrix:List[List[int]]) -> List[List[int]]:
    """
    this function takes four arguments,
    it takes a row to be changed,
    it takes a row to be scaled and added to the row to be changed,
    it takes a scaler value,
    and it takes a matrix.
    """
    newr1 = r1 - 1
    newr2 = r2 - 1

    print(f"add {scale}*{matrix[newr2]} -> {matrix[newr1]}")

    add_to_r1 = scalerow(scale, r2, copy.deepcopy(matrix))

    counter = 0
    for num in matrix[newr1]:
        matrix[newr1][counter] += add_to_r1[newr2][counter]
        counter += 1

    return matrix    

def ATimesWeights(A_Matrix:List[List[int]], x_weights:List[int]) -> List[List[int]]:
    """
    This functions multiplies a matrix (A) by weights(x) and returns the result
    A = any matrix
    x = weights

    There NEEDS to be the same ammount of weights as columns, if this isnt the case nothing will happen
    """
    #if the lengths arent the same do nothing
    if len(A_Matrix[0]) != len(x_weights):
        print("The matrix provided does not match with the weights provided! nothing happend!")
        return A_Matrix
    else:
        for i in range(0, len(A_Matrix)):
            for j in range(0, len(A_Matrix[i])):
                A_Matrix[i][j] = A_Matrix[i][j] * x_weights[j]

        return A_Matrix

def AddAllColums(matrix:List[List[int]], Augmented:bool = False) -> List[int]:
    """
    pretty self explanetry its adds up all the rows 
    """
    answer = [0] * len(matrix)

    if len(matrix[0]) <= 1:
        print("You cannot sum a matrix that doesnt have more than one x value")
        return answer

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            answer[i] += matrix[i][j]

    return answer

def printMatrix(matrix:List[List[int]]) -> None:
    print("==================")
    for row in matrix:
        print(row)
    print("==================\n")


def matrix_solver(matrix:List[List[int]], Augmented:bool, Print:bool = False) -> List[List[int]]:
    #find the dimentions
    rows_matrix = len(matrix)
    columns_matrix = len(matrix[0])

    currentrow = 0
    currentcolumn = 0

    #print starting matrix
    if Print:
        print("Starting Matrix:")
        printMatrix(matrix)
    

    for column in range(0, columns_matrix-1):

        if matrix[currentrow][currentcolumn] != 1 and matrix[currentrow][currentcolumn] != 0:
            #look at the matrix and scale the first row by the inverse of the pivot
            scalerow(1/matrix[currentrow][currentcolumn], currentrow+1, matrix)
            if Print:
                printMatrix(matrix)

        currentpoviotrow = currentrow + 1

        for row in range(0, rows_matrix-currentpoviotrow):
            currentrow += 1 #move down to the next row so that we can MURDER the leading term becaust the next one is the pivot

            #look at the 2nd row and add it to a scaled version of the first row to make the first x a zero
            if matrix[currentrow][currentcolumn] != 0:
                addrowtorow(currentrow+1, -matrix[currentrow][currentcolumn], currentpoviotrow, matrix)
                if Print:
                    printMatrix(matrix)
            #repeat last step all the way down

        currentrow = currentpoviotrow
        currentcolumn += 1

    #move up a row if there are more rows to move up pivot is now the 2nd term because your in the 2nd row

    #repeat everything up to this point

    #repeat untill you either make it all the way down, or if its an augmented matrix you get the the answers row.

    #should be in echlon form

    #-------

    #do all of that but upside down

    #should be in reduced row echlon form

    return matrix
#weights = [3, -4]

Matrix1 = [
    [1, 3, -3, 0],
    [3, 10, -6, -3],
    [3, 11, -1, -8]
]
matrix_solver(Matrix1, True, True)
#printMatrix(matrix_solver(Matrix0, True))

Matrix2 = [
    [-5, 8],
    [-3, 2]
]

Matrix3 = [
    [8],
    [2]
]

"""
print(f"Startingfn:")
printMatrix(Matrix1)

printMatrix(AddAllColums(Matrix2))

printMatrix(addrowtorow(2, -3, 1, Matrix1))

printMatrix(addrowtorow(3, -3, 1, Matrix1))

printMatrix(addrowtorow(3, -2, 2, Matrix1))

printMatrix(scalerow(1/2, 3, Matrix1))

"""

#printMatrix(ATimesWeights(Matrix1, weights))

#printMatrix(scalerow(1/7, 2, Matrix1))

#printMatrix(scalerow(1/8, 3, Matrix1))

#printMatrix(addrowtorow(2, -3, 3, Matrix1))

#printMatrix(addrowtorow(1, 3, 3, Matrix1))

#printMatrix(addrowtorow(1, -3, 2, Matrix1))

#printMatrix(addrowtorow(1, -3, 2, Matrix1))

#printMatrix(addrowtorow(3, 1, 1, Matrix1))

#printMatrix(scalerow(1/7, 2, Matrix1))

#printMatrix(addrowtorow(1, 6, 2, Matrix1))

#printMatrix(addrowtorow(3, 3, 2, Matrix1))

#printMatrix(swaprows(3, 4, Matrix1))



"""
Question 1:
Matrix1 = [
    [1, 3, -3, -3],
    [-3, -2, 2, 23],
    [4, 3, 5, -22]
]

print(f"Startingfn:")
printMatrix(Matrix1)

printMatrix(addrowtorow(2, 3, 1, Matrix1))

printMatrix(addrowtorow(3, -4, 1, Matrix1))

printMatrix(scalerow(1/7, 2, Matrix1))

printMatrix(addrowtorow(3, 9, 2, Matrix1))

printMatrix(scalerow(1/8, 3, Matrix1))

printMatrix(addrowtorow(2, 1, 3, Matrix1))

printMatrix(addrowtorow(1, 3, 3, Matrix1))

printMatrix(addrowtorow(1, -3, 2, Matrix1))
"""
#----------------
"""
Question 3:

"""
#----------------
"""
Question 7:

"""
#----------------
"""
Question 18: 

"""