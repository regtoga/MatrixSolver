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

#weights = [3, -4]

Matrix1 = [
    [1, 3, -3, 0],
    [3, 10, -6, -3],
    [3, 11, -1, -8]
    
]

Matrix2 = [
    [-5, 8],
    [-3, 2]
]

Matrix3 = [
    [8],
    [2]
]


print(f"Startingfn:")
printMatrix(Matrix1)

#printMatrix(ATimesWeights(Matrix1, weights))

printMatrix(AddAllColums(Matrix2))

#printMatrix(scalerow(1/7, 2, Matrix1))

printMatrix(addrowtorow(2, -3, 1, Matrix1))

printMatrix(addrowtorow(3, -3, 1, Matrix1))

printMatrix(addrowtorow(3, -2, 2, Matrix1))

printMatrix(scalerow(1/2, 3, Matrix1))

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