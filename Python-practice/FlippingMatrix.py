import numpy as np
matrix = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

def suma(A, matrix):
    B = [matrix[A[0][0]][A[0][1]], matrix[A[1][0]][A[1][1]], matrix[A[2][0]][A[2][1]], matrix[A[3][0]][A[3][1]]]
    return max(B)

def summat(A, B):
    C = []
    for i in range(len(A)):
        C.append((int(A[i][0] + B[i][0]), int(A[i][1] + B[i][1])))
    return C

def flipmatrix(matrix):
    n = int(len(matrix))
    le = int(len(matrix)/2)
    sum = 0
    A = [(0,0), (0, n-1), (n-1, 0), (n-1, n-1)]


    rowA = [(0,1), (0,-1), (0,1), (0,-1)]
    rowb = [(0,-1), (0,+1), (0,-1), (0,+1)]

    colA = [(1,0), (1,0), (-1,0), (-1,0)]
    
    for i in range(le):
        for j in range(le):  
            sum += suma(A, matrix) 
            A = summat(A,rowA)  
        for j in range(le):
            A = summat(A,rowb)
        A = summat(A, colA)

    return sum

def flipmatrix2(matrix):
    n = len(matrix)
    s = 0

    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s

print(flipmatrix(matrix))