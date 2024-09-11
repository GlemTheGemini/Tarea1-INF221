from random import randint

def generate_matrix(rows, cols):
    return [[randint(1, 10) for i in range(cols)] for j in range(rows)]

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def iterative_cubic_traspuesta(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])

    B_Traspuesta = transpose_matrix(B)

    C = [[0] * p for _ in range(n)]

    for i in range(n):
        for j in range(p):
            suma = 0
            for k in range(m):
                suma += A[i][k] * B_Traspuesta[j][k]
            C[i][j] = suma

    return C

# Test the function
from time import time

# Generate random matrices
matrixA = generate_matrix(1000,1000)
matrixB = generate_matrix(1000,1000)

start_time = time()

# Multiply the matrices
C = iterative_cubic_traspuesta(matrixA, matrixB)

end_time = time()

print(f"Time: {end_time - start_time} seconds for optimized cubic")