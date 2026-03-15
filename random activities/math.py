# # from math import *
# # import math
# # print(e**4, sin(pi/2))
# # print(sin(2))
# from platform import platform, machine, processor, system, version
# print(platform())
# print(platform(1))
# print(platform(0, 1))
# print(machine())
# print(processor())
# print(system())
# print(version())
# from platform import python_implementation, python_version_tuple
# print(python_implementation())
# for atr in python_version_tuple():
#     print(atr)
# import math
# for name in dir(math):
#         print(name, end="\t")

if __name__ == "__main__":
   print("name == main ")
   print(__name__)
else:
   print("main != main")


from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))



import module
import module2







