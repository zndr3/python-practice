import numpy as np

# Coefficient matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 10]])

# Constant vector
b = np.array([6, 15, 25])

# Solve the system
x = np.linalg.solve(A, b)

print("Solution:")
print("x =", x[0], ", y =", x[1], ", z =", x[2])

# Verify the solution
verification = np.dot(A, x)
print("\nVerification (A * x):")
print(verification)  # Should match the vector b

