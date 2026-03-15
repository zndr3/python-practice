import numpy as np

import matplotlib.pyplot as plt

# Define the system of equations
# Let x = number of popcorn, y = number of soda
# x + y = 10 (total popcorn)
# 5x + 3y = 40 (budget)



# Visualize the solution

x = np.linspace(0, 8, 100)
y1 = 10 - x  # From x + y = 9
y2 = (40 - 5 * x) / 3  # From 10x + 12y = 100

A = np.array([[1, 1], [5, 3]])
b = np.array([10, 40])

# Solve the system
solution = np.linalg.solve(A, b)
popcorn, soda = solution

print("Popcorn:", round(popcorn))
print("Soda:", round(soda))

plt.figure(figsize=(4, 4))
plt.plot(x, y1, label='x + y = 10', color='green')
plt.plot(x, y2, label='5x + 3y = 40', color='purple')
plt.plot(popcorn, soda, 'ro', label='Solution')
plt.xlabel('Popcorn')
plt.ylabel('Soda')
plt.legend()
plt.grid(True, linestyle='--', alpha=1)
plt.title('Popcorn Soda Problem')
plt.show()


