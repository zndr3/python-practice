import numpy as np

# Define the matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Multiply matrices
result = A @ B
print("\nMatrix Multiplication (A @ B):")
print(result)
