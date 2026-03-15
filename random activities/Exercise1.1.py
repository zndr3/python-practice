import numpy as np
import matplotlib.pyplot as plt

# Coefficient matrix (A)
A = np.array([
    [1, 1],
    [2, 3]
])

# Right-hand side (b)
b = np.array([50, 120])

# Solve the system of equations
solution = np.linalg.solve(A, b)
x, y = solution

print(f"Number of vanilla cones sold: {int(x)}")
print(f"Number of chocolate cones sold: {int(y)}")

# Visualization
x_vals = np.linspace(0, 50, 100)

# Lines for equations
y1_vals = 50 - x_vals  # from x + y = 50
y2_vals = (120 - 2 * x_vals) / 3  # from 2x + 3y = 120

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1_vals, label=r'$x + y = 50$', color='blue')
plt.plot(x_vals, y2_vals, label=r'$2x + 3y = 120$', color='green')
plt.scatter(x, y, color='red', marker='o', label=f'Solution: ({int(x)}, {int(y)})')

plt.xlabel("Number of Vanilla Cones (x)")
plt.ylabel("Number of Chocolate Cones (y)")
plt.title("Ice Cream Cone Sales")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
