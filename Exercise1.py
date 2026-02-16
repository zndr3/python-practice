import numpy as np
import matplotlib.pyplot as plt


# Define the system of equations
# Let x = number of popcorn, y = number of soda
# x + y = 10 (total popcorn)
# 5x + 3y = 40 (budget)

x = np.linspace(0, 50, 100)  # Generate x values from 0 to 5

# # Solve for y in terms of x
y1 = 50 - x 
y2 = (120 - 2 * x) / 3 

# # Solve the system of equations using numpy
A = np.array([[1, 1], [2, 3]])
b = np.array([50, 120])
solution = np.linalg.solve(A, b)

vanilla, chocolate = solution

print("Chocolate and vanilla: ", vanilla)
print("Chocolate Cone: ", chocolate)

# # Plot the lines
plt.figure(figsize=(4, 4))
plt.plot(x, y1, label=r'$x + y = 50$', color='green')
plt.plot(x, y2, label=r'$2x + 3y = 120$', color='purple')

# Mark the solution point
plt.scatter(solution[0], solution[1], color='black', zorder=3, label=f'Solution ({vanilla}, {chocolate})')

# Labels and grid
plt.xlabel('Vanilla')
plt.ylabel('Chocolate Cone')
plt.axhline(0, color='lightgreen', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title('Visualization of the System of Equations')

# Show the plot
plt.show()
