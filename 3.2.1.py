import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
print("Addition (A + B):")
a=matrix_a + matrix_b
print(a)
# Subtraction
print("Subtraction (A - B):")
b=matrix_a - matrix_b
print(b)
# Multiplication (element-wise)
print("Element-wise Multiplication (A * B):")
m=matrix_a*matrix_b
print(m)

# Matrix multiplication (dot product)
print("A dot B:")
d=np.dot(matrix_a,matrix_b)
print(d)
# Transpose
print("Transpose of A:")
t=np.transpose(matrix_a)
print(t)
