import numpy as np

# Định nghĩa ma trận A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Hàm tính định thức của ma trận con
def det_minor(matrix, i, j):
    minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
    return np.linalg.det(minor)

# Tạo ma trận hệ số kép
def cofactor_matrix(matrix):
    n = matrix.shape[0]
    cofactor = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            minor_det = det_minor(matrix, i, j)
            cofactor[i, j] = ((-1) ** (i + j)) * minor_det
            
    return cofactor

# Tính ma trận hệ số kép của A
C = cofactor_matrix(A)
print("Ma trận hệ số kép C là:")
print(C)
