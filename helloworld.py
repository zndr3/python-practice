import numpy as np
# # print(numpy.__version__)


# my_list = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

# num_rows = len(my_list)

# num_columns = len(my_list[0])

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)

# for row in my_list:
#     print(row)

# Row vector

# Input 3 values
values = [input("Enter value 1: "), input("Enter value 2: "), input("Enter value 3: ")]

print("Your list of values:")
print(values)


row_vector = np.array([1, 2, 3])
print("Row Vector:")
print(row_vector)

# Column vector
column_vector = np.array([[1], [2], [3]])
print("\nColumn Vector:")
print(column_vector)
