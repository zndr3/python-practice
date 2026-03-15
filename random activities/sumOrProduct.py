# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))


# def sumOrProduct(num1 , num2):
#     num3 = num1 * num2
#     if num3 > 1000:
#         sum = num1 + num2
#         return sum
#     else:
#         return num3
# result = sumOrProduct(num1 , num2)
# print("The result is: ", result)


# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0
# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i


# num_list = [10, 20, 33, 46, 55]
# print("Given list:", num_list)
# print('Divisible by 5:')
# new_list = []
# for num in num_list:
#     if num % 5 == 0:
#         new_list.append(num)
# print('Divisible by 5:', new_list)


# start = int(input("Enter start number: "))
# stop = int(input("Enter stop number: "))
# step = int(input("Enter step number: "))
# for i in range(start , stop , step):
#     print(i)



# string = str(input("Enter a string: "))
# for i in range(0 , len(string) - 1 , 2):
#     print(i)
#     print(string[i])


# numbers_x = [10, 20, 30, 40, 10]
# if numbers_x[0] == numbers_x[len(numbers_x)-1]:
#     print(True)
# else:
#     print(False)


# string = str(input("Enter a string: "))
# find = str(input("What to find?: "))

# count = string.count(find)
# print(count)

# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")


# salary = int(input("Enter salary: "))
# tax = 0 

# if salary <= 10000:
#     tax = 0
# elif salary <= 20000:
#     newSalary = salary - 10000
#     tax = newSalary*0.10
# else:
#     tax = 0
# taxOne = salary*0
# salary-= 10000
# print(salary)

# taxTwo = 10000*0.10
# salary-= 10000
# print(salary)

# taxThree = salary*0.20
# print(salary)

# print("Tax payable is ", taxOne + taxTwo + taxThree)



# for i in range(5 , 0 , -1):
#     while i > 0:
#         print("*" , end=" ")
#         i -= 1
#     print("\t")


name, age, marks = input("Enter your Name, Age, Percentage separated by space ").split()
print("\n")
print("User Details: ", name, age, marks)