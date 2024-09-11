from random import randint

def generate_matrix(rows, cols):
    return [[randint(1, 10) for i in range(cols)] for j in range(rows)]

def iterative_cubic(matrixA, matrixB):
    rowsA, colsA = len(matrixA), len(matrixA[0])
    rowsB, colsB = len(matrixB), len(matrixB[0])

    if colsA != rowsB:
        print("Las matrices no son multiplicables")

    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result 

# Test the function
from time import time

# Generate random matrices
matrixA = generate_matrix(2048,2048)
matrixB = generate_matrix(2048,2048)

start_time = time()

# Multiply the matrices
C = iterative_cubic(matrixA, matrixB)

end_time = time()

print(f"Time: {end_time - start_time} seconds for iterative cubic")