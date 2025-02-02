from typing import List
import copy

Matrix0 = [
    [1, -4, 0, -1, 0, -9],
    [0, 1, 0, 0, -3, 8],
    [0, 0, 0, 1, 4, 5],
    [0, 0, 0, 0, 0, 0],
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

def printMatrix(matrix:List[List[int]]):
    print("==================")
    for row in matrix:
        print(row)
    print("==================\n")

Matrix1 = [
    [1, -6, 3],
    [4, -17, -16],
    [-1, 3, 1],
]

print(f"Startingfn:")
printMatrix(Matrix1)

printMatrix(addrowtorow(2, -4, 1, Matrix1))

printMatrix(addrowtorow(3, 1, 1, Matrix1))

printMatrix(scalerow(1/7, 2, Matrix1))

printMatrix(addrowtorow(1, 6, 2, Matrix1))

printMatrix(addrowtorow(3, 3, 2, Matrix1))

#printMatrix(swaprows(3, 4, Matrix1))



"""
Question 1:
Matrix0 = [
    [1, 2, -2],
    [3, 8, -2]
]

print(f"Startingfn:")
printMatrix(Matrix0)

printMatrix(addrowtorow(2, -3, 1, Matrix0))

printMatrix(scalerow(1/2, 2, Matrix0))

printMatrix(addrowtorow(1, -2, 2, Matrix0))
"""
#----------------
"""
Question 3:
Matrix0 = [
    [1, -3, 0, 0, -4],
    [0, 1, -1, 0, -6],
    [0, 0, 1, -2, 3],
    [0, 0, 0, 1, 2],
]

print(f"Startingfn:")
printMatrix(Matrix0)

printMatrix(addrowtorow(3, 2, 4, Matrix0))

printMatrix(addrowtorow(2, 1, 3, Matrix0))

printMatrix(addrowtorow(1, 3, 2, Matrix0))
"""
#----------------
"""
Question 7:
Matrix0 = [
    [1, -4, 0, -1, 0, -9],
    [0, 1, 0, 0, -3, 8],
    [0, 0, 0, 1, 4, 5],
    [0, 0, 0, 0, 0, 0],
]

print(f"Startingfn:")
printMatrix(Matrix0)

printMatrix(swaprows(3, 4, Matrix0))

printMatrix(addrowtorow(1, 4, 2, Matrix0))

printMatrix(addrowtorow(1, 1, 4, Matrix0))
"""
#----------------
"""
Question 18: you have to take the abs of the bottom right and also add one for some reason?
Matrix1 = [
    [1, -6, 3],
    [4, -17, -16],
    [-1, 3, 1],
]

print(f"Startingfn:")
printMatrix(Matrix1)

printMatrix(addrowtorow(2, -4, 1, Matrix1))

printMatrix(addrowtorow(3, 1, 1, Matrix1))

printMatrix(scalerow(1/7, 2, Matrix1))

printMatrix(addrowtorow(1, 6, 2, Matrix1))

printMatrix(addrowtorow(3, 3, 2, Matrix1))
"""