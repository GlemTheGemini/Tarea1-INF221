import numpy as np
from time import time

from random import randint
def generate_matrix(rows, cols):
    return [[randint(1, 10) for i in range(cols)] for j in range(rows)]

def padMatrix(matrix, targetSize):
    # Se obtienen las dimensiones originales de la matriz.
    originalRows, originalColumns = matrix.shape
    newRows, newColumns = targetSize, targetSize

    # Crear una nueva matriz de tamaño targetSize x targetSize llena de ceros.
    paddedMatrix = np.zeros((newRows, newColumns))
    
    # Copiar los valores de la matriz original en la esquina superior izquierda de la nueva matriz.
    paddedMatrix[:originalRows, :originalColumns] = matrix
    
    return paddedMatrix  # Se retorna la matriz rellenada.

def unpadMatrix(matrix, originalDimension):
    # Se obtienen las dimensiones originales de la matriz.
    originalRows, originalColumns = originalDimension

    # Se retorna la matriz recortada a su tamaño original.
    return matrix[:originalRows, :originalColumns]

def strassenProcess(matrixA, matrixB):
    # Guardar las dimensiones originales de las matrices A y B.
    original_dimensionA = matrixA.shape
    original_dimensionB = matrixB.shape
    
    # Se determina el tamaño máximo entre las dimensiones para el relleno (padding).
    maxSize = max(original_dimensionA[0], original_dimensionA[1], original_dimensionB[0], original_dimensionB[1])
    
    # Asegurarse de que el tamaño objetivo sea una potencia de 2, usando la función de bit_length.
    targetSize = 1 << (maxSize - 1).bit_length()
    
    # Rellenar las matrices A y B para que sean cuadradas con tamaño potencia de 2.
    paddedA = padMatrix(matrixA, targetSize)
    paddedB = padMatrix(matrixB, targetSize)

    # Realizar la multiplicación utilizando el algoritmo de Strassen.
    paddedC = strassen(paddedA, paddedB)

    # Recortar la matriz resultante al tamaño original de las matrices.
    matrixC = unpadMatrix(paddedC, (original_dimensionA[0], original_dimensionB[1]))

    # Convertir la matriz final en una lista de listas con enteros para facilitar la comparación.
    matrixC = matrixC.astype(int).tolist()

    return matrixC  # Retornar la matriz multiplicada y recortada.

def strassen(A, B):
    n = len(A)  # Obtener el tamaño de la matriz (n x n).
    
    # Caso base: cuando las matrices tienen tamaño menor o igual a 2x2, se usa la multiplicación estándar.
    if n <= 2:
        return np.dot(A, B)

    # Dividir las matrices A y B en cuatro submatrices cada una.
    mid = n // 2
    A11 = A[:mid, :mid]  # Submatriz superior izquierda de A.
    A12 = A[:mid, mid:]  # Submatriz superior derecha de A.
    A21 = A[mid:, :mid]  # Submatriz inferior izquierda de A.
    A22 = A[mid:, mid:]  # Submatriz inferior derecha de A.
    B11 = B[:mid, :mid]  # Submatriz superior izquierda de B.
    B12 = B[:mid, mid:]  # Submatriz superior derecha de B.
    B21 = B[mid:, :mid]  # Submatriz inferior izquierda de B.
    B22 = B[mid:, mid:]  # Submatriz inferior derecha de B.
    
    # Aplicar las siete multiplicaciones de Strassen, recursivamente.
    P1 = strassen(A11, B12 - B22)  # P1 = A11 * (B12 - B22)
    P2 = strassen(A11 + A12, B22)  # P2 = (A11 + A12) * B22
    P3 = strassen(A21 + A22, B11)  # P3 = (A21 + A22) * B11
    P4 = strassen(A22, B21 - B11)  # P4 = A22 * (B21 - B11)
    P5 = strassen(A11 + A22, B11 + B22)  # P5 = (A11 + A22) * (B11 + B22)
    P6 = strassen(A12 - A22, B21 + B22)  # P6 = (A12 - A22) * (B21 + B22)
    P7 = strassen(A11 - A21, B11 + B12)  # P7 = (A11 - A21) * (B11 + B12)

    # Combinar los resultados intermedios para obtener las submatrices de C.
    C11 = P5 + P4 - P2 + P6  # Submatriz superior izquierda de C.
    C12 = P1 + P2            # Submatriz superior derecha de C.
    C21 = P3 + P4            # Submatriz inferior izquierda de C.
    C22 = P5 + P1 - P3 - P7  # Submatriz inferior derecha de C.
    
    # Combinar las submatrices para obtener la matriz resultante C.
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    
    return C  # Retornar la matriz C resultante de la multiplicación.

# Código extraido de: https://www.geeksforgeeks.org/strassen-algorithm-in-python/

A = generate_matrix(1024, 1024)
B = generate_matrix(1024, 1024)

matrix_A = np.array(A)
matrix_B = np.array(B)

start_time = time()

C = strassenProcess(matrix_A, matrix_B)

end_time = time()

print(f"Tiempo de ejecución: {end_time - start_time} segundos de Strassen")
