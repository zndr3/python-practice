import numpy as np
import matplotlib.pyplot as plt


A = np.array([[1, 1, 0, 0],
              [0, 0, 1, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 1]])

b = np.array([475, 489, 542, 422])

solution = np.linalg.solve(A, b)

# print("Solution:", solution)


labels = ['A → C', 'A → D', 'B → C', 'B → D']
for label, value in zip(labels, solution):
    print(f"{label}: {value:.2f} beers/week")


# from mpl_toolkits.mplot3d import Axes3D

# # Define the equations
# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
# X, Y = np.meshgrid(x, y)

# Z1 = 6 - X - Y  # From x + y + z = 6
# Z2 = (14 - 2*X + Y) / 3  # From 2x - y + 3z = 14
# Z3 = 2 + X - 2*Y  # From -x + 2y - z = -2

# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plot the planes
# ax.plot_surface(X, Y, Z1, alpha=0.5, color='blue', label='x + y + z = 6')
# ax.plot_surface(X, Y, Z2, alpha=0.5, color='red', label='2x - y + 3z = 14')
# ax.plot_surface(X, Y, Z3, alpha=0.5, color='green', label='-x + 2y - z = -2')

# # Plot the solution point
# ax.scatter(1, 2, 3, color='black', label='Solution (1, 2, 3)')

# # Add labels and legend
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# plt.title('Unique Solution: Planes Intersect at One Point')
# plt.show()






# A = np.array([[1,1],[2,-1]])
# b = np.array([4,1])
# solution = np.linalg.solve(A,b)
# print("The solution is: ", solution)
# plt.plot(solution)
# plt.show()




#Unique Solution
# x = np.linspace(0, 5, 100)  # Generate x values from 0 to 5

# # Solve for y in terms of x
# y1 = 4 - x  # From x + y = 4  → y = 4 - x
# y2 = 2 * x - 1  # From 2x - y = 1 → y = 2x - 1

# # Solve the system of equations using numpy
# A = np.array([[1, 1], [2, -1]])
# b = np.array([4, 1])
# solution = np.linalg.solve(A, b)

# # Plot the lines
# plt.figure(figsize=(6, 6))
# plt.plot(x, y1, label=r'$x + y = 4$', color='blue')
# plt.plot(x, y2, label=r'$2x - y = 1$', color='red')

# # Mark the solution point
# plt.scatter(solution[0], solution[1], color='black', zorder=3, label=f'Solution ({solution[0]:.2f}, {solution[1]:.2f})')

# # Labels and grid
# plt.xlabel('XXX')
# plt.ylabel('YYY')
# plt.axhline(0, color='lightgreen', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.legend()
# plt.title('Visualization of the System of Equations')

# # Show the plot
# plt.show()





#No solution /  parallel
# # Define the equations
# x = np.linspace(-10, 10, 100)
# y1 = 4 - x  # From x + y = 4
# y2 = 5 - x  # From x + y = 5

# # Plot the lines
# plt.plot(x, y1, label='x + y = 4')
# plt.plot(x, y2, label='x + y = 5')

# # Add labels and legend
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid(True)
# plt.title('No Solution: Parallel Lines Never Intersect')
# plt.show()






#Infinitely Many Solutions
# Define the equations
# x = np.linspace(-10, 10, 100)
# y1 = 4 - x  # From x + y = 4
# y2 = (8 - 2*x) / 2  # From 2x + 2y = 8

# # Plot the lines
# plt.plot(x, y1, label='x + y = 4')
# plt.plot(x, y2, '--', label='2x + 2y = 8')

# # Add labels and legend
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid(True)
# plt.title('Infinitely Many Solutions: Lines Overlap Completely')
# plt.show()




# A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(A)
# print("\n")

# I = np.eye(3)
# print(I)
# print("\n")

# Z = np.zeros((3,3))
# print(Z)
# print("\n")

# D = np.diag([1,2,3])
# print(D)
# print("\n")

# U5 = np.triu(np.random.randint(1,10,(5,5)))
# print(U5)
# print("\n")

# L4 = np.tril(np.random.randint(1,10,(4,4)))
# print(L4)




# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 35]

# # Plotting
# plt.plot(x, y)

# # Customizing
# plt.title("Simple Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# # Show the plot
# plt.show()