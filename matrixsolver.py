from typing import List
from fractions import Fraction
import copy

def swaprows(r1:int, r2:int, matrix:List[List[int]], Print:bool = False) -> List[List[int]]:
    """this function takes three int arguments, it will swap the two rows given"""
    newr1 = r1 - 1
    newr2 = r2 - 1

    row_r1 = matrix[newr1]
    row_r2 = matrix[newr2]

    matrix[newr1] = row_r2
    matrix[newr2] = row_r1

    if Print:
        print(f"Swap {row_r1} with {row_r2}\n Final = {matrix}")

    return matrix

def scalerow(scale:float, row:int, matrix:List[List[int]], Print:bool = False) -> List[List[int]]:
    """
    This function takes three arguments,
    first being a value to scale the row by.
    Seccond being the row number to be scaled.
    Third the actual matrix itself"""

    newrow = row - 1

    if Print:
        print(f"Scale row{newrow} by {scale}, row{newrow}: {matrix[newrow]}")

    counter = 0
    for num in matrix[newrow]:
        temp = scale * matrix[newrow][counter]
        matrix[newrow][counter] = Fraction(temp).limit_denominator()

        counter += 1

    return matrix


def addrowtorow(r1:int, scale:float, r2:int, matrix:List[List[int]], Print:bool = False) -> List[List[int]]:
    """
    this function takes four arguments,
    it takes a row to be changed,
    it takes a row to be scaled and added to the row to be changed,
    it takes a scaler value,
    and it takes a matrix.
    """
    newr1 = r1 - 1
    newr2 = r2 - 1

    if Print:
        print(f"add {scale}*{matrix[newr2]} -> {matrix[newr1]}")

    add_to_r1 = scalerow(scale, r2, copy.deepcopy(matrix))

    counter = 0
    for num in matrix[newr1]:
        matrix[newr1][counter] += add_to_r1[newr2][counter]
        counter += 1

    return matrix    

def MultiplyMatrices(A_Matrix:List[List[int]], x_weights:List[int]) -> List[List[int]]:
    """
    This functions multiplies a matrix (A) by weights(x) and returns the result
    A = any matrix
    x = weights

    There NEEDS to be the same ammount of weights as columns, if this isnt the case nothing will happen
    """
    answer = makeNull(len(A_Matrix))
    temp = makeNull(len(A_Matrix))

    #if the lengths arent the same do nothing
    if len(A_Matrix[0]) != len(x_weights):
        print("The matrix provided does not match with the weights provided! nothing happend!")
        return A_Matrix
    else:
        for h in range (0, len(x_weights)):
            
            for i in range(0, len(A_Matrix)):
                for j in range(0, len(A_Matrix[i])):
                    temp[j][i] = A_Matrix[j][i] * x_weights[i][h]

            partialanswer = AddAllColums_scalar(temp)
            
            for i in range(0, len(A_Matrix)):
                answer[i][h] = partialanswer[i]

        return answer

def AddAllColums_scalar(matrix:List[List[int]]) -> List[int]:
    """
    Adds up all the rows returns a scalar instead of a matrix
    """
    answer = [0] * len(matrix)

    if len(matrix[0]) < 1:
        print("You cannot sum a matrix that doesnt have more than one x value")
        return answer

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            answer[i] += matrix[i][j]

    return answer

def AddAllColums_matrix(matrix:List[List[int]]) -> List[List[int]]:
    """
    Adds up all the rows returns a matrix
    """
    answer = []
    for item in range(0, len(matrix)):
        answer.append([0])

    if len(matrix[0]) < 1:
        print("You cannot sum a matrix that doesnt have atleast one x value")
        return answer

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            answer[i][0] += matrix[i][j]

    return answer

def printMatrix(matrix:List[List[int]]) -> None:
    """Prints the matrix"""
    print("==================")
    for row in matrix:
        rowintext = ""
        for item in row:
            rowintext += str(item) + ", "

        print(rowintext)
    print("==================\n")


def matrix_solver(matrixx:List[List[int]], Augmented:bool, Print:bool = False, FindInverse:bool = False) -> List[List[int]]:
    """
    This function uses a redimentary algorithm that we learned in class to solve a matrix using reduced eclon form.
    """
    matrix = copy.deepcopy(matrixx)
    #find the dimentions
    rows_matrix = len(matrix)
    if Augmented:
        columns_matrix = len(matrix[0]) - 1
        if FindInverse:
            FindInverse = False
            print("You cant find inverse with a Augmented matrix, bc im to lazy to think about it.")
    else:
        columns_matrix = len(matrix[0])

    currentrow = 0
    currentcolumn = 0

    IdentityMatrix = makeIdentity(rows_matrix)

    #print starting matrix
    if Print:
        print("Starting Matrix:")
        printMatrix(matrix)

    if (FindInverse and not Augmented) and Print:
        print("Inverse:")
        printMatrix(IdentityMatrix)

    for column in range(0, columns_matrix):

        if matrix[currentrow][currentcolumn] != 1 and matrix[currentrow][currentcolumn] != 0:
            #look at the matrix and scale the first row by the inverse of the pivot
            scale = 1/matrix[currentrow][currentcolumn]
            scalerow(scale, currentrow+1, matrix, Print)

            if Print:
                printMatrix(matrix)

            if FindInverse and not Augmented:
                scalerow(scale, currentrow+1, IdentityMatrix, Print)
                if Print:
                    print("Inverse:")
                    printMatrix(IdentityMatrix)

        #move up a row if there are more rows to move up pivot is now the 2nd term because your in the 2nd row
        currentpoviotrow = currentrow + 1

        for row in range(0, rows_matrix-currentpoviotrow):
            currentrow += 1 #move down to the next row so that we can MURDER the leading term becaust the next one is the pivot

            #look at the 2nd row and add it to a scaled version of the first row to make the first x a zero
            if matrix[currentrow][currentcolumn] != 0:
                scale = -matrix[currentrow][currentcolumn]
                addrowtorow(currentrow+1, scale, currentpoviotrow, matrix, Print)

                if Print:
                    printMatrix(matrix)

                if FindInverse and not Augmented:
                    addrowtorow(currentrow+1, scale, currentpoviotrow, IdentityMatrix, Print)
                    if Print:
                        print("Inverse:")
                        printMatrix(IdentityMatrix)
            #repeat last step all the way down

        currentrow = currentpoviotrow
        currentcolumn += 1
        
        #repeat everything up to this point

    #repeat untill you either make it all the way down, or if its an augmented matrix you get the the answers row.

    #should be in echlon form

    #-------

    #do all of that but upside down

    for column in range(0, columns_matrix):
        currentpoviotrow = currentrow
        currentcolumn -= 1
        for row in range(0, currentrow-1):
            currentrow -= 1
            
            if matrix[currentrow-1][currentcolumn] != 0:
                scale = -matrix[currentrow-1][currentcolumn]
                addrowtorow(currentrow, scale, currentpoviotrow, matrix, Print)
                
                if Print:
                    printMatrix(matrix)

                if FindInverse and not Augmented:
                    addrowtorow(currentrow, scale, currentpoviotrow, IdentityMatrix, Print)
                    if Print:
                        print("Inverse:")
                        printMatrix(IdentityMatrix)

        currentrow = currentpoviotrow - 1

    #should be in reduced row echlon form

    if FindInverse and not Augmented:
        if matrix == makeIdentity(rows_matrix):
            return IdentityMatrix
        else:
            if Print:
                print("======================")
                print("There wasnt a Inverse!")
                print("======================")
            return False
    else:
        return matrix

def makeIdentity(size:int) -> list[list[int]]:
    #This funciton should take a dimetion and return the Identity matrix of that size.
    
    Identity = []
    counter = 0
    for height in range(0, size):
        Identity.append([])
        for width in range(0, size):
            if width == counter:
                Identity[height].append(1)
            else:
                Identity[height].append(0)
        counter += 1

    return Identity

def makeNull(size:int) -> list[list[int]]:
    #This funciton should take a dimetion and return the Null matrix of that size.
    
    Identity = []
    for height in range(0, size):
        Identity.append([])
        for width in range(0, size):
            Identity[height].append(0)

    return Identity

def findInverse(matrix:list[list[int]], Print:bool = False)-> list[list[int]]:
    #This function should...
    return matrix_solver(matrix, False, Print, True)

#this is what the weights should look like for the A_Time_x function
weights = [1, 0]

#Some test matrixes

Matrix_1 = [
    [0],
    [1]
]

Matrix0 = [
    [-3, 1],
    [5, 0]
]

Matrix1 = [
    [5, 3, 9],
    [-6,-3, 4]
]

Matrix2 = [
    [1, 0, 2],
    [-3, 15, -8],
]

Matrix2 = [
    [1, 3, -3, -3],
    [-3, -2, 2, 23],
    [4, 3, 5, -22]
]
Matrix3 = [
    [1, 2, 3],
    [-2, 5, 7],
    [-5, 6, 3]
]

Matrix4 = [
    [4, -2, 6, -9],
    [-5, 7, -7, 0],
    [7, 9, 6, 2],
    [5, -3, 7, -10]
]

Matrix5 = [
    [0, 2],
    [1, 0]
]

Matrix6 = [
    [1, -2],
    [1, 0]
]

#printMatrix(MultiplyMatrices(Matrix0, Matrix1))

#matrix_solver(Matrix3, True, True, False)

printMatrix(Matrix4)

printMatrix(findInverse(Matrix4, False))

printMatrix(MultiplyMatrices(Matrix4, findInverse(Matrix4, False)))

#printMatrix(MultiplyMatrices(Matrix5, Matrix6))

#printMatrix(findInverse(findInverse(Matrix0)))
